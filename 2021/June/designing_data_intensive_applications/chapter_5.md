# Chapter 5: Replication
- [Chapter 5: Replication](#chapter-5-replication)
  - [Leaders and Followers](#leaders-and-followers)
    - [Leader-based replication](#leader-based-replication)
      - [async vs sync](#async-vs-sync)
      - [creating new followers](#creating-new-followers)
      - [node outages](#node-outages)
      - [replication logs](#replication-logs)
      - [Replication Lag & Types of Consistency](#replication-lag--types-of-consistency)
    - [Multi-Leader Replication](#multi-leader-replication)
      - [Handling Write Conflicts](#handling-write-conflicts)
      - [Multi-Leader Replication Topologies](#multi-leader-replication-topologies)
    - [Leaderless Replication](#leaderless-replication)
      - [Read and Write Quorum Consistency](#read-and-write-quorum-consistency)

- *replication* - keeping a copy of the same data on multiple machines that are connected via a network
- reasons might be
  - **reduce latency** keep data geographically close to your users
  - **increase availability** - allow the system to continue working even if some of its parts have failed
  - **increase throughput** - scale out the number of machines that can serve read queries
- all of the difficulty in replication lies in handling changes to replicated data
- almost all distributed databases use one of three algorithms 1) *single leader* 2) *multi-leader* 3) *leaderless*

## Leaders and Followers
- *replica* - each node that stores a copy of the database
- every write to a database must be processed by every replica, otherwise the replica would no longer contain the same data

### Leader-based replication
- aka *active/passive* or *master-slave*
- generally works like this:
  - one replica is designated leader (aka *master* or *primary*) and writes are sent to this node
  - other replicas are known as *followers* (*read replicas*, *slaves*, *secondaries*, *hot standbys*) -- when a leader writes new data, changes are sent to replicas via *replication log* or *change stream*, and writes are applied the same way they were initially received
  - reads can go to leader or any followers
  - seen in - PostgreSQL (since 9.0), MySQL, Oracle Data Guard, SQL Server's AlwaysOn Availability Groups, MongoDB, RethinkDB, Espresso, Kafka and RabbitMQ highly available queues

#### async vs sync
- replication to followers can either be
  - *asynchronous* - writes don't wait for replication to followers to report success to client/user
  - *synchronous* - writes replicate to all followers before reporting success
- in sync models, one bad follower can halt the entirety of the write, so *semi-synchronous* method is employed where writes are synchronous to a single follower and all others are async
- often, leader-based is also fully asynchronous, so if leader fails any writes that weren't replicated are lost

#### creating new followers
- sometimes you need to create a new follower, but copying files or locking the database isn't desirable.
- the process:
  1. take a snapshot of leader database
  2. copy snapshot to follower node
  3. follower connects to leader and requests changes since snapshot -- as long as the exact position in the log is known (PostgreSQL - *log sequence number*, or MySQL - *binlog coordinates*)
  4. once backlog of changes are processed, the follower has caught up

#### node outages
- how do we achieve high availability with leader-based replication?
  - **follower failure: catch-up recovery** - a follower knows exact place in log, so if network interruptions or failures happen, follower can connect to leader after resolution and catch up
  - **leader failure: failover** - one of followers needs to be promoted to new leader, which can happen manually or automatically
    - determine leader has failed - can happen for many reasons, and might be determined by timeout
    - choose new leader - typically, the follower with most up to date data
    - reconfigure system to use new leader - clients need to send write requests to new leader, and if old leader comes back on needs to be demoted to follower
    - if async is enabled, writes to original leader might cause problems when leader comes back, so these are typically discarded
    - two nodes might believe they are both leader - *split brain*

#### replication logs
- several leader-based replication methods
  - **statement based** - leader sends SQL statements to followers (`INSERT`, `UPDATE`, `DELETE`)
    - difficult if there are non-deterministic functions (`NOW()`) or side effects (triggers, stored procedures, user-defined functions)
  - **write ahead log shipping** - we can use the append only sequence of records to replicate data, used in PostgreSQL and Oracle
    - WAL contains very low level data, which bytes where changed in which disk blocks, closely coupling replication and storage engine
  - **logical (row-based) log** - store different log format for replication (logical) and for storage engine (physical) -- logical log stores changes to database at granularity of rows
    - easier to parse as its decoupled from storage engine
  - **trigger-based** - move replication to the application layer by using *triggers* or *stored procedures* within database
    - useful if you need more flexibility

#### Replication Lag & Types of Consistency
- *read scaling architecture* - many models need only single leader and many read replicas, so you can scale those out to take increased load
- *eventual consistency* - if app reads from async follower, sometimes that data might be out of date -- if you wait for all writes to complete all followers will eventually have up-to-date data
- **read-after-write consistency** - when a user writes to a database, this guarantee is that if the user refreshes the page they will see their writes reflected, which might not happen if they write to one node then read from a follower that hasn't been replicated to yet
  - you might enforce reading from the leader when reading something a user modified, or using other criteria such as using timestamps of most recent write and serving from replicas that are at least that up to date, either as a logical timestamp (sequence of writes) or actual system clock
  - you might also need to provide *cross-device* read-after-write consistency
- **monotonic reads** - guarantee that users won't see things moving back in time because their queries were served by two followers that were progressively more stale
  - lesser guarantee than strong consistency, but stronger than eventual consistency
- **consistent prefix reads** - guarantees that if a sequence of writes happens in a certain order, anyone reading those writes would see them appear in same order -- a problem of *causality* where one write precedes the write that seems to have caused it
  - particular problem in partitioned/sharded databases
- worth thinking about what would happen if replication lag increases to several minutes or several hours when thinking about what consistency you need to guarantee

### Multi-Leader Replication
- aka *master-master* or *active/active*
- each node that processes a write must forward to all other nodes
- some databases support by default, but most need external tools to handle (Tungsten Replication for MySQL, BDR for PostgreSQL, and GoldenGate for Oracle)
- use cases for multi-leader replication
  - **multiple datacenters** - rarely makes sense to use multi-leader in a single datacenter, but if you have multiple data centers, you can have a leader in each one, and each leader replicates their changes to other leaders in other datacenters
  - **clients with offline operation** - if you have an application that needs to continue to work even when offline (calendar apps, email apps) - data stored on local database acting as leader, and synced when internet is next available. CouchDB operates in this mode by default
  - **collaborative editing** - things like Google Docs allow many people to edit a doc at once, but each local copy is a leader that replicates to all other copies -- you need to lock a doc before someone else can use it, but you can make the unit of change as small as a keystroke to limit the locks

#### Handling Write Conflicts
- biggest problem with multi-leader is write conflicts can occur (two leaders make conflicting writes)
- **conflict avoidance** - simplest way to deal with conflicts is to avoid them -- you could make sure that all edits to a record go through the same leader
- **converging toward a consistent state** - in multi-leader config, there is no defined ordering of writes
  - all replication must ensure that data is eventually the same in all replicas, so one method is to resolve conflicts in a *convergent* way, or to ensure that all replicas must arrive at the same final value when all changes have been replicated
  - if timestamp is used, you might use *last write wins* (LWW)
- **custom conflict resolution logic** - you might need to write application code to resolve conflicts
  - *on write* - as soon as database system detects conflict, it calls conflict handler to deal
  - *on read* - all conflicting writes are stored, but next time the data is read, all conflicting writes are given to the application to resolve
- other conflict resolution algorithms:
  - **conflict-free replicated datatypes** - family of data structures (maps, sets, etc) that can automatically resolve conflicts in sensible ways
  - **mergeable persistent data structures** - explicit tracking of history similar to git version control
  - **operational transformation** - behind Google Docs and Etherpad

#### Multi-Leader Replication Topologies
- replication topology describes communication path which writes are propagated from one node to another
- **all-to-all** - every leader sends its writes to every other leader
- **star** - one designated root node forwards writes to all other nodes (tree)
- **circular** - each node receives writes from one node and forwards to another

### Leaderless Replication
- allows any node to accept writes
- Amazon used for its in-house *Dynamo* system, and Riak, Cssanda, and Voldemort adopted it
> not to be confused with AWS's DynamoDB
- in a leaderless configuration, failover doesn't exist, so reads and writes are sent to multiple nodes, and up to date data is determined by version numbers
- how does a node that was offline catch up?
  - **read repair** - when client makes a read from several nodes in parallel, it can detect stale responses by version number
  - **anti-entropy process** - some datastores have a background process that looks for differences in data between replicas and updates the stale data

#### Read and Write Quorum Consistency
- used to determine how many nodes would be required for a write to be successful
- if there are *n* replicas, every write must be confirmed by *w* nodes to be considered successful, and we need to query *r* nodes for each read, so as long as *r* + *w* > *n* we expect an up to date value when reading
-
