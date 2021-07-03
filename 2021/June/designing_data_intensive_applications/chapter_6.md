# Chapter 6: Partitioning
- [Chapter 6: Partitioning](#chapter-6-partitioning)
    - [Partitioning and Replication](#partitioning-and-replication)
    - [Partitioning of Key-Value Data](#partitioning-of-key-value-data)
      - [Partitioning by Key Range](#partitioning-by-key-range)
      - [Partitioning by Hash of Key](#partitioning-by-hash-of-key)
      - [Skewed Workloads and Relieving Hot Spots](#skewed-workloads-and-relieving-hot-spots)
    - [Partitioning & Secondary Indexes](#partitioning--secondary-indexes)
      - [Partitioning Secondary Indexes by Document](#partitioning-secondary-indexes-by-document)
      - [Partitioning Secondary Indexes by Term](#partitioning-secondary-indexes-by-term)
    - [Rebalancing Partitions](#rebalancing-partitions)
      - [Strategies for Rebalancing](#strategies-for-rebalancing)
        - [Fixed Number of Partitions](#fixed-number-of-partitions)
        - [Dynamic Partitioning](#dynamic-partitioning)
        - [Partitioning Proportionally to Nodes](#partitioning-proportionally-to-nodes)
      - [Automatic or Manual Rebalancing](#automatic-or-manual-rebalancing)
      - [Request Routing](#request-routing)
  - [Chapter Summary](#chapter-summary)

- for very large datasets or high query throughput, replication isn't enough, we need to break up data into *partitions* (aka *sharding*)
> *partition* is *shard* in MongoDB, Elasticsearch and SolrCloud, *region* in HBase, *tablet* in Bigtable, *vnode* in Cassandra and Riak, *vBucket* in Couchbase
- each partition is like a small database on its own
- main use case for partitioning is scalability -- different partitions can be placed on different nodes in *shared-nothing architecture*

### Partitioning and Replication
- partitioning is normally combined with replication for fault tolerance, so copies of partitions are stored on multiple nodes

### Partitioning of Key-Value Data
- goal of partitioning is to spread data and query load evenly across nodes
- *skewed* - if partition is unfair, meaning some nodes have more query load or data than others
- a partition with a disproportionately high load is called a *hot spot*
- you might assign values to nodes randomly, but this is disadvantageous if you want to read data since you'd need to guess what node data is on

#### Partitioning by Key Range
- you might partition by a continuous range of keys, from a minimum to a maximum
- range of keys might not be evenly spaced, so partition boundaries need to adapt to data
  - partition boundaries might be chosen by an administrator or by the database itself
- within each partition, keys can be kept in sorted order
  - the key can treated as a concatenated index to fetch related records
- we can use range to do efficient range queries
- downside is that certain access patterns can lead to hot spots, e.g. using a timestamp as a key means all writes end up going to the same partition
  - need to use something other than timestamp as the first element of the key

#### Partitioning by Hash of Key
- because of the risk of skew and hot spots, many distributed datastores use a hash function to determine partition for a given key
- doesn't need to be cryptographically strong
  - Cassandra and MongoDB use MD5
  - Voldemort uses Fowler-Noll-Vo function
- some programming language hash functions might generate a different hash for the same data in different processes
- this can lead to *consistent hashing*, or partitions are chosen pseudo-randomly - better to avoid the term and call it *hash partitioning* (consistency is a loaded and ambiguous term)
- this method means you can't do efficient range queries
- Cassandra reaches a compromise by using *compound primary keys*, which take the first part of a key for hashing, but additional fields can be used to sort data in Cassandra's SSTables, which helps with concatenated queries (e.g. hash(user_id), timestamp would allow all updates for a particular user in a timespan)

#### Skewed Workloads and Relieving Hot Spots
- extreme case where all requests still routed to same partition
- currently, most data systems can't compensate for this skewed workload, so application code needs to be written to accommodate
- for example, you might add two digits to hot keys, then you must keep track of them to access later

### Partitioning & Secondary Indexes
- secondary indexes are indispensable for relational databases, but they don't map neatly to partitions
- two main approaches to partitioning a database with secondary indexes:
  1. document-based partitioning
  2. term-based-partitioning

#### Partitioning Secondary Indexes by Document
- primary indexes are maintained (document ids)
- each partition is completely separate, and indexes added are *local* to the partition
- downsides are that there is no reason that all fields with a particular value would be in the same partition, so queries would need to be sent to all partitions, which might get expensive
- *scatter/gather* - querying a partitioned database across all partitions using secondary index, then aggregated the results
- MongoDB, Riak, Cassandra, Elasticsearch, SolrCloud, and VoltDB all use document-partitioned secondary indexes

#### Partitioning Secondary Indexes by Term
- instead of a local index, we can have a *global index*, but that global index also needs to be partitioned across nodes
- use either a hash of a term or the term itself to generate the index
- has the benefit of making reads faster, but writes are slower and more complicated since many nodes might need to be accessed to write the index

### Rebalancing Partitions
- over time, the database changes, e.g.:
  - query throughput increases, and you want to add CPU
  - dataset size increases and you want to add more RAM
  - machine fails, and other machines need to take over responsibilities
- **rebalancing** - process of moving load from one load to another
- after rebalancing, certain requirements should be met
  - the load should be shared fairly between nodes in the cluster
  - while rebalancing is happening, the database should continue accepting reads and writes
  - no more data than necessary should be moved between nodes, to make rebalancing fast and minimize network and disk I/O load

#### Strategies for Rebalancing
- don't use modulo, since that encodes a specific number of nodes say, mod *n* means if you have n+1 nodes, all data needs to be shifted

##### Fixed Number of Partitions
- practice of assigning many more partitions to each node, so any new node can 'borrow' partitions from each node until load is evenly spread
- e.g. each node has 100 partitions, across 10 nodes, that is 1,000 partitions. if an 11th node is adding, that node can take ~9 partitions from each node
- number of partitions is usually fixed when database is set up, making this less ideal if the size of the data set is variability (might grow much larger over time)
- hard to achieve 'just right' partition amount

##### Dynamic Partitioning
- fixed number of partitions wouldn't work well with key range partitioned databases, so dynamic partitioning might be more effective
- when a partition grows larger than a fixed size  (HBase, default is 10GB), that partition is split and might be sent to separate nodes to balance the load
- if partition shrinks, it might be combined with adjacent partition
- can also be used for hash-partitioned data

##### Partitioning Proportionally to Nodes
- have a fixed number of partitions per node, and those partitions grow larger with dataset size, but adding a node decreases size of partitions again
- requires hash-based partitioning, as new node randomly takes data from other nodes, and if hash-based partitioning isn't used, this would lead to unfair splits

#### Automatic or Manual Rebalancing
- generally a good idea to have a human in the loop, as rebalancing is expensive and automation might be unpredictable

#### Request Routing
- how does a client know which node to send a request to (who makes the routing decision)?
- an example of a more general problem called *service discovery*
- a few different approaches to the problem:
  1. allow clients to contact any node (e.g. via a round-robin loader balancer) -- if that node contains the information, return it, otherwise forward the request to the correct node
  2. send all requests to a routing tier first acting as a partition-aware load balancer
  3. require that clients be aware of partitioning and assignment of partitions, so a client can connect directly to a node
- many distributed data systems rely on a coordination service such as Zookeeper to keep track of this cluster metadata
- Espresso uses Helix
- HBase, SolrCloud, and Kafka use Zookeeper
- MongoDB uses its own *config server* and *mongos* daemon as the routing tier
- Cassandra and Riak use *gossip protocol*, putting more complexity into database nodes but doesn't require external coordination service
- DNS is sufficient for IP address lookup

## Chapter Summary
- goal of partitioning is to spread the data and query load evenly across multiple machines, avoiding hot spots
- this requires a partitioning scheme that is appropriate to the data, and rebalancing partitions when nodes are added to or removed from the cluster
- two types of partitioning
  - **key range partitioning**
    - keys are sorted and a partition owns all the keys from some minimum up to some max.
    - sorting has the advantage that efficient range queries are possible, but there is risk of hot spots if application often access keys that are close together in the sorted order
  - **hash partitioning**
    - where a has function is applied to each key, and a partition owns a range of hashes
    - destroys the ordering of keys making range queries inefficient, but may distribute load more evenly
    - when partitioning by hash it is common to create a fixed number of partitions in advance, to assign several partitions to each node, and to move entire partitions form one node to another when nodes are added or removed
- hybrid approaches are also possible, e.g. using one part for the hash and the second part for the sort order
- two types of secondary index partitions
  - **document-partitioned indexes (local indexes)**
    - secondary indexes stored in the same partition as the primary key and value
    - only a single partition needs to be updated on write, but read of secondary index requires scatter/gather across all partitions
  - **term-partitioned indexes (global indexes)**
    -  secondary index are partitioned separately using indexed values
    -  entry in the secondary index may include records from all partitions of the primary key
    -  when document is written, several partitions of the secondary index need to be updated, however a read can be served from a single partition
