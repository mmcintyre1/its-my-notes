# Designing Data Intensive Applications
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
1. TOC
{:toc}
</details>

# Chapter 1: Reliable, Scalable, and Maintainable Applications

## Data Systems
{: .no_toc }
We can group data components (databases, caches, queues, etc.) under the umbrella of data systems instead of as separate components because
  1. many new systems have emerged that blur the typical line (Kafka, Redis)
  2. many use cases are covered by stitching together data components with application code

## Three concerns for software systems
{: .no_toc }
1. *Reliability*
	- The system should continue to work correctly even in the face of adversity
2. *Scalability*
	- As the system grows, there should be reasonable ways of dealing with growth
3. *Maintainability*
	- Over time, many different people will work on the system, and they should all be able to work on it productively

## Reliability
- Things that can go wrong are called faults, and a system that can withstand them is fault-tolerant or resilient
- fault: component of system deviates from spec
- failure: (different from a fault) when the system stops providing the required service to a user
- we generally prefer tolerating faults over preventing faults

### Types of Faults
{: .no_toc }
#### Hardware Faults
{: .no_toc }
- e.g. hard disks crash, RAM becomes faulty, etc
	- hard disks have a mean time to failure (MTTF) of about 10 to 50 years
	- typically we can add redundancy to a system or individual components by adding additional hardware (additional machines, backup generators, etc)
	- move toward systems that can tolerate loss of entire machines (Netflix's Chaos Engine takes machines offline to test recovery)

#### Software Faults
{: .no_toc }
- systematic error within system
- lots of small things can help minimize software faults: thinking about assumptions and interactions, process isolation, data observation

#### Human Errors
{: .no_toc }
- might be leading cause of errors
- mitigating design choices can be:
  - build well-designed abstractions, APIs, and admin interfaces, make it easy to 'do the right thing'
  - use fully featured sandbox environments
  - test thoroughly at all levels (unit tests, whole-system integration tests, manual tests)
  - make recovery quick and easy
  - build detailed and clear monitoring (telemetry)

## Scalability
the term we use to describe a system's ability to cope with increased load

### Describing Load
{: .no_toc }
- load on a system can be described with a few numbers which we call *load parameters*
- the best choice of load parameters depends on architecture of your system: could be requests/second, or ratio of reads/writes to a database
- *fan-out*: in transaction processing systems, describes the number of requests to other services that we need to make in order to serve one incoming request

### Describing Performance
{: .no_toc }
- when you increase load parameters:
	- and keep system resources the same, how is performance affected
	- how much do you need to increase resources to keep performance the same
- in batch processing systems (like Hadoop) we care about throughput
- in online systems, we care about response time
- *latency*: time request is waiting to be handled
- *response time*: total time a client sees, so time to process (service time), queuing delays, etc
- measuring performance
  - we use arithmetic mean (synonymous with average), or median with percentiles
  - p95, p99, p999 (95%, 99%, 99.9%) to reflect thresholds of percentiles past the median
  - typically used in service level objectives (SLO) and service level agreements (SLA)
- *head of line blocking*: it only takes a small number of slow responses to hold up the processing of subsequent requests (packet at front holds up a line of packets)

### Coping with Load
{: .no_toc }
- *scaling up* - vertical scaling, moving to a more powerful machine
- *scaling out* - horizontal scaling, distributing the load across multiple smaller machines
  - *shared-nothing architecture* - distributing load across multiple machines
- some systems are *elastic* (scaled automatically based on load) while some are scaled manually
- *magic scaling sauce* - the false idea that there is a one size fits all solution to scaling
- an architecture that scales well for a particular application is built around assumption of which operations will be common and which will be rare (informed by *load parameters*)

## Maintainability
The majority of the cost of software is not in its initial development but ongoing maintenance

### Operability
{: .no_toc }
make it easy for operations teams to keep systems running smoothly

### Simplicity
{: .no_toc }
make it easy for new engineers to understand the system by removing complexity, or avoiding a big ball of mud
- *accidental complexity* - complexity not inherent in the problem space but arises because of the implementation
- an abstraction is a useful technique to hide non-important implementation details behind a façade

### Evolvability
{: .no_toc }
make it easy for engineers to make changes to the system in the future (aka *extensibility*, *modifiability*, or *plasticity*)

## Chapter Summary
- an application must meet various requirements to be useful
	- *functional requirements* - what it should do, like allow data to be stored, retrieved, searched
	- *non-functional requirements* - general properties, like reliability, compliance, scalability, maintainability
- **Reliability** means making systems work correctly, even when faults occur. Faults can be in hardware (typically random and uncorrelated), software (bugs are typically systematic and hard to deal with), and human (who inevitability make mistakes from time to time). Fault tolerance techniques can hide certain types of faults from the end user
- **Scalability** means having strategies for keeping performance good, even when load increases. In order to discuss scalability, we first need ways of describing load and performance quantitatively. In scalable systems, you can add processing capacity in order to remain reliable under high load.
- **Maintainability** has many facets, but in essence it's about making life better for the engineering and operations teams who need to work with the system. Good abstractions can help reduce complexity and make the system easier to modify and adapt for new use cases. Good operability means having good visibility into the system's health, and having effective ways of managing it.


# Chapter 2: Data Models and Query Languages

- Data models are perhaps the most important part of developing software -- most applications are built by layering one data model on top of another, with each layer hiding the complexity of the layers below it by providing a clean data model

- Cascading levels of data models:
1. as an app developer, you model the real world in terms of objects or data structures, and APIs used to manipulate those structures
2. when you want to store that data, you use a general-purpose data model such as JSON or XML
3. engineers who built the database software decided on ways of representing that general-purpose data model as bytes in memory, on disk, or on a network
4. hardware engineers have figured out how to represent bytes in terms of electrical currents, pulses of light, etc.

### Relational Model
- SQL based off relational model proposed by Edgar Codd in 1970
- data is organized in *relations* (tables in SQL) where each relation is an unordered collection of *tuples* (rows in SQL)
- object databases came and went in late 80's and early 90's
- XML databases appeared in early 2000's but only have niche audience
- much of the current web is based on relational model
- *impedance mismatch* - a borrowed electronics term which can refer to the need for a translation layer to take objects generated from object-oriented paradigms and write to a relational model
  - Object-relational mapping (ORM) frameworks like ActiveRecord, Hibernate, SQLAlchemy might reduce boilerplate code for that translation layer, but they don't hide it completely

### Document Model
- use cases for 'NoSQL':
  - need for greater scalability, including for very large datasets or very high write throughput
  - preference for free and open source software
  - specialized query operations not well supported by relational model
  - frustration with restrictiveness of relational schemas, and desire for more expressive and dynamic data model
- *polyglot persistence*: many future use cases might employ document and relational models

### Graph Model
- graph consists of two objects:
  - *vertices* (aka *nodes* or *entities*)
  - *edges* (aka *relationships* or *arcs*)
- several different implementations of graph model, including property graph, triple-stores, semantic web

#### property graph
{: .no_toc }
- implemented by Neo4j, Titan, and InfiniteGraph (among others)
- each vertex contains:
  - a unique identifier
  - a set of outgoing edges
  - a set of incoming edges
  - a collection of properties (key:value pairs)
- each edge contains:
  - a unique identifer
  - a vertex where the edge starts (the tail vertex)
  - a vertex where the edge ends (the head vertex)
  - a label to describe the kind of relationship between the two vertices
  - a collection of properties (key:value pairs)
- think of the graph storing two relational tables, one for vertices, one for edges

#### triple-stores
{: .no_toc }
- similar to property graphs, just describes things with different words
- all info stored as three-part statement - subject, predicate, object. e.g. JIM LIKES EGGS (JIM - subject, LIKES - predicate, EGGS - object)

##### semantic web
{: .no_toc }
- while not all triple-stores are synonymous with the semantic web, they are interlinked in many minds
- semantic web is the idea that websites could publish machine-readable information about their sites in a consistent format to form a 'web of data' (note Berners-Lee constantly says there is no data layer for the internet)
- *Resource Description Framework* (RDF) - is positioned as that format
	- Apache Jena popular tool for this

### Many-to-One and Many-to-Many Relationships
{: .no_toc }
- Storing standardized list of data, so you can join to that data and prevent duplication (*normalized* data)
- 1st Normal Form (NF), 2NF, 3NF, etc have little practical difference -- rule of thumb, if you are duplicating values that could be stored in one place, your schema is not normalized
- normalizing requires a many-to-one relationship, something not supported well with document model (support for joins is weak), meaning you need to shift that logic to application code over database model logic

### Relational vs Document
#### simpler application code
{: .no_toc }
- if your data is document-like, use document (*shredding* - relational technique of splitting a document-like structure into multiple tables, makes for complicated application code)
- if you need many-to-many or joins, use relational

#### schema flexibility
{: .no_toc }
- *schema-on-write* (relational): structure of data is explicit and database ensures all data conforms to it
- *schema-on-read* (document): structure of data is implicit and only interpreted when data is read
> NOTE: `ALTER TABLE` typically fast except for MySQL, where the entire table is copied

#### data locality
{: .no_toc }
- if joins aren't required for your document, then there is a performance advantage to all data in a single document (called *storage locality*)
- some relational databases group related data together to achieve storage locality
  - Google's Spanner (allows schema to declare table's rows interleaved (nested) with a parents)
  - Oracle through *multi-table index cluster tables*
  - Bigtable (Cassandra and HBase) through *column-family*

#### convergence
{: .no_toc }
Many data systems support multiple models.
- many relational databases support JSON (PostGreSQL 9.3+, MySQL 5.7+)
- many relational databases support XML (other than MySQL)

### Query Languages
#### SQL
{: .no_toc }
- SQL is a *declarative* language which follows the structure of relational algebra closely
- other declarative languages examples: XSL, CSS
- *imperative* languages tell the computer to perform operations in order (most programming languages)
- declarative languages lend themselves to parallel execution

#### MapReduce Querying
{: .no_toc }
- programming model for processing large amounts of data across multiple machines created by Google
- you specify two functions -- `map` (aka `collect`), and a `reduce` (aka `fold` or `inject`). Below is MapReduce implemented in MongoDB:
- MongoDB allows you to embed javascript in a MapReduce query:
```javascript
db.observations.mapReduce(
  function map() {
    // this function returns a key and a value to be passed to
    // the reduce function, and must be pure (no side effects)
    var year = this.observationTimestamp.getFullYear();
    var month = this.observationTimestamp.getMonth() + 1;
    emit(year + "-" + month, this.numAnimals);
  },
  function reduce(key, values) {
    // this pure function takes the key and values from map
    return Array.sum(values);
  },
  {
    query: {family: "Sharks"},
    out: "monthlySharkReport"
  }
```

#### Cypher
{: .no_toc }
- declarative language implemented by Neo4j and used to query property graphs

#### Querying Graph Models with SQL
{: .no_toc }
- you can query graph models in SQL, it is just extremely verbose, and relies on a *recursive common table expression* e.g. `WITH RECURSIVE`
- *common table expressions* - temporary data set returned by a query, which is then used by another query. It’s temporary because the result is not stored anywhere; it exists only when the query is run -- e.g. `WITH expression_name AS (CTE definition)`

#### SPARQL
{: .no_toc }
- query language for triple-stores using RDF data model
- similar to Cypher (Cypher borrows its pattern matching from SPARQL)

#### Datalog
{: .no_toc }
- predates SPARQL
- is a subset of Prolog
- need to define rules at outset, and while it might be harder for one-off queries, rules are reusable and Datalog might fit use case if data is complex

## Chapter Summary
- Historically, data started out being represented as one big tree (the hierarchical model), but that wasn't good for representing many-to-many relationships, so the relational model was invented to solve that problem. More recently, developers found that some apps don't fit well within the relational model either. New nonrelational "NoSQL" datastores have diverged in two main directions
	1. *Document databases* target use cases where data comes in self-contained documents and relationships between one document and another are rare.
	2. *Graph databases* go in the opposite direction, targeting use cases where anything is potentially related to everything.
- All three models (document, relational, and graph) are widely used. Each is good in its domain. One model can be emulated in terms of another model (e.g. graph data can be represented in a relational db), but the result is often awkward. There is no single one-size-fits-all solution
- graph databases and document databases don't typically enforce schema for data they store, however, application most likely still assumes that data has a certain structure. just a question of whether the schema is explicit (schema-on-write) or implicit (schema-on-read)
- each model comes with its own query language or framework, e.g. SQL, MapReduce, MongoDB's aggregation pipeline, Cypher, SPARQL, Datalog


# Chapter 3: Storage and Retrieval

at a fundamental level, a database needs to do two things:
1. when you give it data it should store the data
2. when you ask it later it should give the data back to you

## Log-structured storage
{: .no_toc }
- many databases internally use a log, or append only sequence of records, to store data (different from application logs, which are typically text files emitted by an application to describe what is happening)
> *log* used here is different than a machine-generated output explaining what is happening. log here means append only sequence of records

### Indexes
- an *additional structure* used to efficiently find data within a database
- keep some additional metadata on the side which acts a signpost to help you locate the data you want
- speeds up read performance but degrades write performance (typically because index needs to be updated after every write)

#### Hash Indexes
{: .no_toc }
- simple index of key:value pairs stored in a hash map/dictionary on disk, where each key is associated with a byte offset to lookup the value on disk
- Bitcask, the default storage engine for Riak, does this
- this sort of use case is well-suited for frequent updates to values and where the hash map can fit in memory
- important things to consider for this implementation:
	- **file format**: binary format that first encodes the length of string in bytes then the raw string (without needing to escape chars)
	- **deleting records**: if you want to delete a record, you need to append a special delete record (sometimes called a tombstone) to signal during compaction merge to remove the record
	- **crash recovery**: since the hash map is in memory, restarts mean you lose the hash map. you can store version on disk to warm start the hash map
	- **partially written records**: crashes can happen at any time, even partially through writes. Bitcask uses checksums to ignore corrupted parts of log
	- **concurrency control**: since writes are sequential append only, its common to only have a single writer. Data files are append only and immutable, so they can be read concurrently

##### segment files
{: .no_toc }
- since the log is an append-only structure, we need break it up into *segment files* to prevent running out of space
- after a segment file reaches a certain size, we can create a new one to write to, then perform *compaction* on the older segment files, meaning, throwing away duplicate keys in the log and keeping only the most recent update
	- older segment files are merged in the background then swapped without interruption to writes

#### SSTables
{: .no_toc }
- **Sorted String Table** (SSTable) - takes the idea for hash indexes, but requires that segment files be sorted in order by key. also requires that each key only appears once in each merged segment table (because in order to do compaction, we need to mergesort, which relies on uniqueness of keys when comparing one file to another)
- keys duplicated across segment files don't matter, since most recent segment contains most up to date value per key
- your in-memory hash index can be sparse, because keys are sorted and so easy to scan (typically one index per every few kilobytes is sufficient)
- you can compress blocks and then just point the index at a block, saving disk space and I/O

##### LSM-Trees
{: .no_toc }
- described in Patrick O'Neil et al *Log-Structured Merge-Tree* or LSM-tree
- *memtable* and SSTable introduced by Google's Bigtable paper
- how do we maintain sorted order? much easier in memory than on disk
	- write comes in, add to a balanced tree data structure (e.g. a red-black tree) - this is typically called a *memtable*
	- when *memtable* is larger than a threshold, write that *memtable* as an SSTable file to disk. start new *memtable* while old is being written to disk
	- to serve a read request, first check *memtable*, then first segment file, then second, etc.
	- from time to time, run a merging and compaction process for older segment files
	- maintain an append only log on disk that holds all writes, to recover the *memtable* in case of crash (you can delete after current *memtable* is written to disk)

#### B-Trees
{: .no_toc }
- keeps indexes sorted by value, but instead of storing database in segment files, B-Trees store database in fixed size *blocks* or *pages*, which corresponds more closely to underlying hardware
- you start at the root of the tree. each page contains references (like pointers but on disk) to child pages until you get to a page of individual keys (a leaf page), which either contains the value or references to the page where the value can be found
- number of references to child pages called the *branching factor*
- trees are balanced, so traversal is always O(log *n*) -- most databases can fit into a B-tree that is three or four levels deep (e.g. a four-level tree of 4 KB pages with a branching factor of 500 can store 256 TB)

##### Reliability
{: .no_toc }
- many B-tree impl. use *write-ahead logs* (WAL), aka *redo logs*, to persist all writes to the database in an append only log before it can be applied to pages

#### B-Trees vs LSM-Trees
{: .no_toc }
- B-Trees need to write data twice, once to the write-ahead log and once to page
- Log-structured indexes might write data multiple times due to repeated compaction and merging (write amplification) and is particularly concerning for SSDs, which can only overwrite blocks a limited amount of times before wearing out
- LSM-Trees typically able to sustain higher write throughput because they often have lower write amplification
- B-Trees have keys that exist exactly one place in index, which is good for databases that want strong transactional semantics via transaction isolation and locks

#### Secondary Indexes
{: .no_toc }
- both log-structured and B-Trees can work as secondary indexes in addition to a primary key index. These secondary indexes don't need to be unique (unless you add that constraint)

#### Storing values within the index
{: .no_toc }
- the value of the index might be an actual row, or it might be a reference to the row, typically stored in a *heap file* -- data in these heap files are not stored in any particular order
- updating a value in a heap file can be efficient by overwriting the data in place (assuming the data is the same length)
- *clustered index* - storing the row directly in the index, and secondary indexes just refer to the primary key
- a compromise between clustered and non-clustered is a *covering index*, or *index with included columns*, which stores some of the tables columns within an index, allowing queries to be 'covered' or answered by an index alone

#### Multi-column indexes
{: .no_toc }
- concatenated indexes used to store indexes for multiple columns, which is good for searching full index combinations, but not individual columns after the primary key
- multi-dimensional indexes are a good way to query several columns at once, especially for geospatial data. R-Trees are typically used instead of B-Trees

#### Full-text search and fuzzy indexes
{: .no_toc }
- Lucene is able to search for words within a certain edit distance (edit distance meaning when 1 letter has been added, removed, or replaced)
- *Levenshtein distance* - used to figure out amount of edits required to go from one word to another

#### In memory databases
{: .no_toc }
- we typically use disks because they are durable and cost less per gigabyte than RAM (the second argument is becoming less relevant)
- **Memcached** - an entirely in memory cache (lost if restarted)
- other in-memory databases aim for more durability, writing log of changes to disk, writing periodic snapshots, etc.
- **VoltDB**, **MemSQL**, and **Oracle TimesTen** are relational in-memory databases
- anti-caching approach is a way around working with datasets larger than memory, by persisting data to disk when out of memory, and bringing back into memory when used (this is similar to virtual memory and swap files at OS level)
- new area of research - *nonvolatile memory* (NVM); still in infancy

### Transactions vs Analytics

| Property | Transaction processing systems (OLTP) | Analytics systems (OLAP) |
|--|--|--|
| Main read pattern | small number of records per query, fetched by key | aggregate over large number of records  |
| Main write pattern | Random-access, low-latency writes from user input | Bulk import (ETL) or event stream |
| Primarily used by | End user/customer via web application | Internal analyst, for decision support |
| What data represents | Latest state of data (current point in time) | History of events that happened over time |
| Dataset size | Gigabytes to terabytes | Terabytes to petabytes |

### Data Warehouses and Column-Oriented Storage
- you store data in an OLAP data warehouse as it will be insulated from live transaction processing and queries won't affect live customer-facing systems
- typically perform Extract-Transform-Load (ETL) operations to populate the database
- Data warehouses typically sell their systems under expensive commercial licenses (e.g. Amazon RedShift is a host version of ParAccel)
- Some are based on the ideas from Google's Dremel
- many data warehouses can have hundreds of columns
- The typical use case for OLAP queries are only accessing a small amount of many columns -- unlike OLTP systems which are *row-oriented storage*, meaning that a row is stored in contiguous bytes on disks, OLAP systems are *column-oriented storage*, which stores a column in contiguous bytes.

##### Star and Snowflake Schema
{: .no_toc }
- many data warehouses use *star schema* as their data model (known as *dimensional modeling*)
- at the center of the schema is a *fact table*, most often representing a particular event
- some of the columns are attributes of the event, while others are foreign key references to other tables called *dimension tables*, which typically represent the who, what, where, when, how, and why of the event
- *snowflake schema* - a variation of the star schema, but dimensions are broken even further into sub-dimensions

##### Column Compression
{: .no_toc }
- since there are far less distinct values in a column than there are rows, we can compress this data. a popular method is *bitmap encoding*, which details all the unique values in a column, then encodes an array of 1s and 0s for whether a row contains that value, which creates sparse data sets, which can be compressed more easily by encoding run length (how many 1s or 0s in a row)

##### Vectorized Processing
{: .no_toc }
- the query engine can take a chunk of compressed column data that fits in the CPU's L1 cache, and iterate through in a tight loop (no function calls) much more quickly than if many function calls are required, e.g. to type-cast data formats

##### Materialized Views
{: .no_toc }
- for expensive queries (like aggregation functions), it might make sense to actually store the results in a table. materialized views differ from regular views (which are just shorthand for queries) because they are an actual table stored on disk, and they need to be recomputed when the underlying data changes
- a special use case is a *data cube*, which is a grid of aggregates based on various dimensions (e.g. product sales for a given day, also rolled to a total)

## Chapter Summary
- storage engines fall into two broad categories
	1. optimized for transaction processing (OLTP)
	2. optimized for analytics processing (OLAP)
- OLTP systems are typically user-facing, which means they see a huge volume of requests. In order to handle the load, applications usually only touch a small number of records in each query. The application requests records using some kind of key, and the storage engine uses an index to find the data for the requests key. Disk seek time is often a bottleneck.
- Data warehouses and similar analytics used by business analysts, not end users. They handle much lower volume of queries, and each query is demanding, requiring many million records to be scanned in short time. Disk bandwith is often bottleneck
- On storage engine side, there are two main schools of thought:
	1. log-structured: only permits appending to files and deleting obsolete files, but never updates a file that has been written. e.g. Bitcask, SSTables, LSM-Trees, LevelDB, Cassandra, HBase, Lucene, etc
	2. update-in-place: treats the disk as a set of fixed-size pages that can be overwritten. e.g. B-Trees
- log-structured storage engines are comparatively new --- the key is they systematically turn random-access writes into sequential writes which enables higher write throughput

# Chapter 4: Encoding and Evolution

## Formats for Encoding Data
- Programs typically work with data in two ways:
  1. in memory: kept in objects (list, array, struct, hash table, etc.) and efficiently accessed and manipulated by CPU (typically via pointers)
  2. out of memory: you need to encode data into a self-contained sequence of bytes to write to file or send over network, etc
- **encoding** - the translation of in-memory representation to byte sequence (aka *serialization* or *marshalling*), and the opposite action is *decoding* (aka *parsing*, *deserialization*, *unmarshalling*)

### Language-Specific Formats
{: .no_toc }
- many languages have built-in support for encoding in-memory objects to byte sequences:
  - `java.io.Serializable` for Java
  - 'Marshal` for Ruby
  - `pickle` for python
- this languages bind you to the programming language, and instantiate arbitrary classes or execute arbitrary code, which is a security risk

### JSON, XML, and Binary Variants
{: .no_toc }
- JSON, XML, and CSV are textual formats and will remain valuable especially as interchange formats between organizations, but there are limitations:
  - **ambiguity around encoding numbers** - in XML and CSV, you can't distinguish between a number a string that happens to consist of digits. JSON doesn't distinguish integers and floats, and doesn't distinguish precision, which is a problem with large numbers (> 2<sup>53</sup>)
  - **binary strings** - JSON and XML have good support for Unicode character strings, but not binary strings -- binary strings are typically encoded as text using Base64, which is hacky and increases data footprint by 33%
  - **schema support** - schema support is ubiquitous for XML, but used less often for JSON, and there is no schema support for CSV. Schema languages are powerful but complicated to learn
- Binary variants for JSON - BSON, BJSON, UBJSON, BISON, Smile, etc
- Binary variants for XML - WBXML, Fast Infoset, etc

### Thrift and Protocol Buffers
{: .no_toc }
- binary encoding libraries that encode object name and type using a schema
- Google invented Thrift, Facebook invented protobuf
- Thrift has two encoding formats, BinaryProtocol and CompactProtocol

### Avro
{: .no_toc }
- started in 2009 as a subproject of Hadoop
- has two schema languages
  - Avro interface domain language (IDL) for human editing
  - JSON for more easy machine reading
- data type isn't encoded in the binary, so you need to read the data along with the schema to determine data type, meaning you need to decode with the exact same schema used to write the data

- **backward and forward compatibility**:
  - writer and reader schema don't need to be the same, just compatible
  - **writer's schema** - schema used to write data
  - **reader's schema** - schema used to read data
  - if the code reading the data encounters a field that appears in the writer's schema but not in the reader's schema, it is ignored
  - if the code reading the data expects some field but the writer's schema does not contain a field of that name, it is filled in with a default value declared in the reader's schema

- schema can be:
  - declared at the beginning of a large container file with many records
  - referenced by a version number stored elsewhere at the beginning of a record
  - negotiated on connection setup over a network via something like the Avro RPC protocol

- Thrift and Protocol Buffer rely on code generation, which is good for static typed languages but less good for dynamic typed languages
- Avro provides optional code generation because it is *self-describing*, containing all necessary metadata
  - this is particularly useful for dynamically typed data processing languages like Apache Pig

> Many of these encodings share a lot with ASN.1, a schema definition language. It's binary encoding (DER) is still used to encode SSL certs (X.509)

- Binary encodings have a few nice properties over JSON, XML, & CSV
  - much more compact
  - schema is a valuable document, and since it is required for reading you know it's up to date
  - keeping a database of schemas allows you to check forward and backward compatibility
  - for static typed languages, ability to generate code from schemas is useful

## Modes of Dataflow

### Dataflow through Databases
- process that writes to the database encodes the data, process that reads from the database decodes it
- several processes might be accessing a database at the same time, so some might be running newer code and some older, so forward compatibility is important
- *data outlives code*
- you can rewrite data into a new schema (*migration*) but it is expensive and time consuming on larger datasets
- schema evolution allows the entire database to appear as if it was encoded with a single schema, even though underlying records were written with various versions
- when you do a data dump, it is written in one go and is immutable afterwards, so object containers like Avro might be a good fit, or analytics-friendly column-oriented format such as Parquet

### Dataflow through Services: REST and RPC
- when two processes need to communicate over a network, the most common way is to have two roles: *clients* & *servers* -- servers expose an API and the clients connet to the servers to make requests to that API as a *service*
- web -> clients (web browsers) make requests to web servers, send `GET` requests to download HTML, CSS, JS, etc, and send `POST` requests to submit data to server
- native app also make network requests
- a client-side JS app running in browser can use XMLHttpRequest to become an HTTP client (*Ajax*)
- *service-oriented architecture* (SOA) or *microservice architecture* -- to decompose a larger app into smaller services
  - key idea is to make app easier to change and maintain by making services independently deployable and evolvable

#### Web Services
{: .no_toc }
- when HTTP is used for the underlying protocol of talking to the service, it is called a *web service*
- two popular approaches: REST and SOAP, which are almost opposite in terms of philosophy

##### REST
{: .no_toc }
- REST is not a protocol but a design philosophy
  - simple data formats
  - URLs for identifying resources
  - using HTTP for cache control, authentication, and content type negotiations
- an API designed according to REST principles is *RESTful*
- definition format such as OpenAPI (aka Swagger) can be used to describe RESTful APIs and produce documentation

##### SOAP
{: .no_toc }
- XML based protocol for making API requests, most commonly used over HTTP but comes with a complex plethora of related standards (*web service framework*, aka *WS-\**)
- described using Web Services Description Language (WSDL), which is not designed to be human-readable
- ostensibly standardized, but interoperability between different vendor impl. might cause problems

#### RPC
{: .no_toc }
- many implementations of making API calls over network, all based on *remote procedure call* (RPC)
  - Enterprise JavaBeans (EJB) and Java's Remote Method Invocation (RMI) - limited to Java
  - Distributed Component Object Model (DCOM) limited to Microsoft platforms
  - Common Object Request Broker Architecture (CORBA) overly complex and neither forward or backward compatible
- RPC tries to make calling a remote service look the same as calling a function within programming language (called *location transparency*)
- this approach is flawed because:
  - a local function call either succeeds or fails, but a network request is unpredictable
  - a local function returns a result or throws an exception, but a network request might timeout
  - there is no inherent mechanism for idempotence with network calls
  - network calls have variable execution time
  - local function calls allow you to pass pointers, but network calls require those parameters to be encoded into a sequence of bytes
  - the client might be in a different programming language, causing the need for a translation of data types

### Dataflow though async messages
- async message-passing systems are somewhere between RPC and databases
- a client's request (*message*) is passed to another process with low latency, to an intermediary called a *message broker*, or *message queue*
- using a message queue has advantages
  - it can act as a buffer if recipient is overloaded or unavailable
  - it can automatically redeliver messages to a crashed process so nothing is lost
  - it avoid sender needing to know IP and port of recipient, where virtual machines come and go
  - it allows one message to be sent to several recipients
  - it logically decouples sender from recipient
- In the past, message brokers were dominated by commercial enterprise (TIBCO, IBM WebSphere, webMethods), but more recently, open source impl. like RabbitMQ, ActiveMQ, HornetQ, NATS, and Apache Kafka are populate
- They typically work like this: one process (producer) sends a message to a named queue or topic, and the broker ensures that the message is delivered to one or more consumers or subscribers to that queue or topic -- there can be many producers and consumers

#### Distributed actor frameworks
{: .no_toc }
- *actor model* - programming model for concurrency in a single process. logic is encapsulated in an actor, and that sends async messages

## Chapter Summary
- many services need to support rolling upgrades, where a new version of a service is gradually deployed to a few nodes at a time
- rolling upgrades allow a new version of a service to be released without downtime (thus encouraging frequent small releases over rare big releases) and make deployments less risky -- these properties are hugely important for evolvability
- during rolling upgrades (or for various other reasons) we must assume that different nodes are running different versions of our application's code -- it is important that all data flowing around the system is encoded in a way that provides backward (new code can read old data) and forward (old code can read new data) compatibility
- there are several data encoding formats
  - programming language-specific encodings are restricted to a single programming language and often fail to provide forward and backward compatibility
  - textual formats like JSON, XML, and CSV are widespread, and their compatibility depends on how you use them -- they have optional schema languages, which are sometimes helpful and sometimes a hindrance, and these formats are sometimes vague about datatypes, so you have to be careful with things like numbers and binary strings
  - binary schema-driven formats like Thrift, Protocol Buffers, and Avro allow compact, efficient encoding with clearly defined forward and backward compatible semantics -- these schemas can be useful for documentation and code generation in statically typed languages
- there are several modes of dataflow
  - databases, where the process writing to the database encodes the data and the process reading from the database decodes it
  - RPC and REST APIs, where the client encodes a request, the server decodes the request and encodes a response, and the client finally decodes the response
  - asynchronous message passing (using message brokers or actors) where nodes communicate by sending each other messages that are encoded by the sender and decoded by the recipient

# Chapter 5: Replication

- *replication* - keeping a copy of the same data on multiple machines that are connected via a network
- you might need to replicate data to:
  - **reduce latency** keep data geographically close to your users
  - **increase availability** - allow the system to continue working even if some of its parts have failed
  - **increase throughput** - scale out the number of machines that can serve read queries
- all of the difficulty in replication lies in handling changes over time to replicated data
- almost all distributed databases use one of three algorithms:
    1. *single leader*
    2. *multi-leader*
    3. *leaderless*

## Leaders and Followers
{: .no_toc }
- *replica* - each node that stores a copy of the database
- every write to a database must be processed by every replica, otherwise the replica would no longer contain the same data

### Leader-based replication
- aka *active/passive* or *master-slave*
- generally works like this:
  - one replica is designated leader (aka *master* or *primary*) and writes are sent to this node
  - other replicas are known as *followers* (*read replicas*, *slaves*, *secondaries*, *hot standbys*) -- when a leader writes new data, changes are sent to replicas via *replication log* or *change stream*, and writes are applied the same way they were initially received
  > there are different definitions for hot, warm, and cold standbys which aren't material to this section
  - reads can go to leader or any followers
  - PostgreSQL (since 9.0), MySQL, Oracle Data Guard, SQL Server's AlwaysOn Availability Groups, MongoDB, RethinkDB, Espresso, Kafka and RabbitMQ highly available queues all use leader-based replication

#### Asynchronous vs. Synchronous
{: .no_toc }
- replication to followers can either be
  - *asynchronous* - writes don't wait for replication to followers to report success to client/user
  - *synchronous* - writes replicate to all followers before reporting success
- in sync models, one bad follower can halt the entirety of the write, so *semi-synchronous* method is employed where writes are synchronous to a single follower and all others are replicated asynchronously
- often, leader-based is also fully asynchronous, so if leader fails any writes that weren't replicated are lost

#### Creating New Followers
{: .no_toc }
- sometimes you need to create a new follower node, but copying files or locking the database isn't desirable as this won't reflect all changes and is slow
- a more desirable process might:
  1. take a snapshot of leader database
  2. copy snapshot to follower node
  3. follower connects to leader and requests changes since snapshot -- as long as the exact position in the log is known (PostgreSQL - *log sequence number*, or MySQL - *binlog coordinates*)
  4. once backlog of changes are processed, the follower has 'caught up'

#### Node Outages
{: .no_toc }
- how do we achieve high availability with leader-based replication?
  - **follower failure: catch-up recovery** - a follower knows exact place in log, so if network interruptions or failures happen, follower can connect to leader after resolution and catch up
  - **leader failure: failover** - one of followers needs to be promoted to new leader, which can happen manually or automatically
    - steps needed to failover
      - determine leader has failed - can happen for many reasons, and might be determined by timeout
      - choose new leader - typically, the follower with most up to date data
      - reconfigure system to use new leader - clients need to send write requests to new leader, and if old leader comes back on needs to be demoted to follower
    - some potential failover problems:
      - if async is enabled, writes to original leader might cause problems when leader comes back, so these are typically discarded
      - two nodes might believe they are both leader - *split brain*
      - if storage systems outside the database need to be coordinated with the database contents (e.g. an incrementing key in a database, and a Redis cache using those keys -- database goes down so some primary keys entries are written to a failover leader but aren't propagated and need to be discarded, but those primary keys still exist in Redis cache, leading to the exposure of private data (database has 123 as user a, but Redis cache has 123 as user b))
      - determining timeout to declare leader 'dead' might lead to false positives for longer running tasks

#### Replication Methods
{: .no_toc }
- several leader-based replication methods
  - **statement based** - leader sends SQL statements to followers (`INSERT`, `UPDATE`, `DELETE`)
    - difficult if there are non-deterministic functions (`NOW()`) or side effects (triggers, stored procedures, user-defined functions)
  - **write ahead log shipping** - we can use the append only sequence of records to replicate data, used in PostgreSQL and Oracle
    - WAL contains very low level data (which bytes where changed in which disk blocks) closely coupling replication and storage engine
  - **logical (row-based) log** - store different log format for replication (logical) and for storage engine (physical) -- logical log stores changes to database at granularity of rows
    - easier to parse as its decoupled from storage engine
  - **trigger-based** - move replication to the application layer by using *triggers* or *stored procedures* within database
    - useful if you need more flexibility, but difficult to maintain

#### Replication Lag & Types of Consistency
{: .no_toc }
- *read scaling architecture* - many models need only single leader and many read replicas, so you can scale those out to take increased load
- **eventual consistency** - if app reads from async follower, sometimes that data might be out of date -- if you wait for all writes to complete all followers will eventually have up-to-date data
- **read-after-write consistency** - when a user writes to a database, this guarantee is that if the user refreshes the page they will see their writes reflected, which might not happen if they write to one node then read from a follower that hasn't been replicated to yet
  - you might enforce reading from the leader when reading something a user modified, or using other criteria such as using timestamps of most recent write and serving from replicas that are at least that up to date, either as a logical timestamp (sequence of writes) or actual system clock
  - you might also need to provide *cross-device* read-after-write consistency
- **monotonic reads** - guarantee that users won't see things moving back in time because their queries were served by two followers that were progressively more stale
  - lesser guarantee than strong consistency, but stronger than eventual consistency
- **consistent prefix reads** - guarantees that if a sequence of writes happens in a certain order, anyone reading those writes would see them appear in same order -- a problem of *causality* where one write precedes the write that seems to have caused it, like an answer before a question
  - particular problem in partitioned/sharded databases
- worth thinking about what would happen if replication lag increases to several minutes or several hours when thinking about what consistency you need to guarantee

### Multi-Leader Replication
- aka *master-master* or *active/active*
- each node that processes a write must forward to all other nodes
- some databases support by default, but most need external tools to handle (Tungsten Replication for MySQL, BDR for PostgreSQL, and GoldenGate for Oracle)
- use cases for multi-leader replication
  - **multiple datacenters** - rarely makes sense to use multi-leader in a single datacenter, but if you have multiple data centers, you can have a leader in each one, and each leader replicates their changes to other leaders in other datacenters
  - **clients with offline operation** - useful if you have an application that needs to continue to work even when offline (calendar apps, email apps) - data stored on local database acting as leader, and synced when internet is next available. CouchDB operates in this mode by default
  - **collaborative editing** - things like Google Docs allow many people to edit a doc at once, but each local copy is a leader that replicates to all other copies -- you need to lock a doc before someone else can use it, but you can make the unit of change as small as a keystroke to limit the locks

#### Handling Write Conflicts
{: .no_toc }
- biggest problem with multi-leader is write conflicts can occur (two leaders make conflicting writes)
- some methods to avoid write conflicts:
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
{: .no_toc }
- replication topology describes communication path which writes are propagated from one node to another
- **all-to-all** - every leader sends its writes to every other leader
- **star** - one designated root node forwards writes to all other nodes (tree)
- **circular** - each node receives writes from one node and forwards to another

### Leaderless Replication
- allows any node to accept writes
- Amazon used for its in-house *Dynamo* system, and Riak, Cassandra, and Voldemort adopted it
> not to be confused with AWS's DynamoDB
- in a leaderless configuration, failover doesn't exist, so reads and writes are sent to multiple nodes, and up to date data is determined by version numbers
- how does a node that was offline catch up?
  - **read repair** - when client makes a read from several nodes in parallel, it can detect stale responses by version number
  - **anti-entropy process** - some datastores have a background process that looks for differences in data between replicas and updates the stale data

#### Read and Write Quorum Consistency
{: .no_toc }
- used to determine how many nodes would be required for a write to be successful
- if there are *n* replicas, every write must be confirmed by *w* nodes to be considered successful, and we need to query *r* nodes for each read, so as long as *r* + *w* > *n* we expect an up to date value when reading

#### Limitations of Quorum Consistency
{: .no_toc }
- even with *w* + *r* > *n*, there are edge cases where stale values might be returned
  - if sloppy quorum is used, *w* writes may end up on different nodes than *r* reads, so there is no guarantee of overlap
  - two concurrent writes, so it is unclear which write happened first -- if winner is picked based on timestamp, writes might be lost to clock skew
  - write happens concurrent to read
  - write succeeds on some replicas and fails on others
  - unlucky with timing
- monitoring staleness:
  - for leader-based replication, you can see how far behind a leader the replicas are as a quantitative measurement, but that is not possible with leaderless because there is no required sequence of writes

#### Sloppy Quorums and Hinted Handoffs
{: .no_toc }
- in distributed leaderless architectures, network outages might knock off too many nodes to reach a quorum, so if a quorum can't be reached, should we:
  - **sloppy quorums** - accept writes anyway - when network connection is restored, any writes accepted on behalf of a down leader are sent to their respective home (*hinted handoffs*) -- not a quorum at all but an assurance of durability
  - return errors for all requests

#### Detecting Concurrent Writes
{: .no_toc }
- writes can arrive in different orders on different nodes, and if each node overwrote the value for a key, the nodes would be permanently inconsistent
- **last write wins** - you could discard concurrent writes, as long as there is a way to determine which write is more 'recent'
  - only conflict resolution supported in Cassandra, optional in Riak
  - achieves goal of eventual convergence at cost of durability - if there are several concurrent writes only the last one will be successful despite all showing as success to user
- **"happens-before" relationship and concurrency** - with two events, A & B, either 1) A happened before B, B happened before A, or A & B are concurrent

## Chapter Summary
- Replication can serve several purposes:
  - *High Availability*
    - keeping the system running, even when on machine (or several machines, or an entire datacenter) goes down
  - *Disconnected Operation*
    - Allowing an application to continue working when there is a network interruption
  - *Latency*
    - Placing data geographically close to users, so that users can interact with it faster
  - *Scalability*
    - Being able to handle a higher volume of reads than a single machine could handle by performing reads on replicas
- Replication requires careful thinking about concurrency and all the things that could go wrong, and dealing with the consequences of those faults
- at a minimum, need to deal with unavailable nodes and network interruptions
- Three main approaches to replication
  - *Single-leader replication*
    - clients send all writes to a single node (leader) which streams data to other replicas (followers) -- reads can be performed on any replica
  - *Multi-leader replication*
    - clients send writes to one of several leader nodes and that leader node streams data to everything else
  - *Leaderless replication*
    - clients send writes to several nodes in parallel in order to detect and correct nodes with stale data
- single leader is popular because it is fairly easy to understand and there is no conflict resolution to worry about
- multi-leader and leaderless can be more robust in the presence of faulty nodes and latency spikes but are harder to reason about and only provide weak consistency guarantees
- replication can be synchronous or asynchronous -- asynchronous can be fast when system is running smoothly, but failover is more difficult
- some consistency models:
  - *read-after-write consistency* - users should always see data that they submitted themselves
  - *monotonic reads* - after users have seen the data at one point in time, they shouldn't later see the data fromm some earlier point in time
  - *consistent prefix reads* - users should see the data in a state that makes causal sense: for example, seeing a question and reply in the correct order
- because writes can happen concurrently in multi-leader and leaderless, conflicts occur

# Chapter 6: Partitioning

- for very large datasets or high query throughput, replication isn't enough, we need to break up data into *partitions* (aka *sharding*)
> *partition* is *shard* in MongoDB, Elasticsearch and SolrCloud, *region* in HBase, *tablet* in Bigtable, *vnode* in Cassandra and Riak, *vBucket* in Couchbase
- each partition is like a small database on its own
- main use case for partitioning is scalability -- different partitions can be placed on different nodes in *shared-nothing architecture*

### Partitioning and Replication
{: .no_toc }
- partitioning is normally combined with replication for fault tolerance, so copies of partitions are stored on multiple nodes

### Partitioning of Key-Value Data
- goal of partitioning is to spread data and query load evenly across nodes
- *skewed* - if partition is unfair, meaning some nodes have more query load or data than others
- a partition with a disproportionately high load is called a *hot spot*
- you might assign values to nodes randomly, but this is disadvantageous if you want to read data since you'd need to guess what node data is on

#### Partitioning by Key Range
{: .no_toc }
- you might partition by a continuous range of keys, from a minimum to a maximum
- range of keys might not be evenly spaced, so partition boundaries need to adapt to data
  - partition boundaries might be chosen by an administrator or by the database itself
- within each partition, keys can be kept in sorted order
  - the key can treated as a concatenated index to fetch related records
- we can use range to do efficient range queries
- downside is that certain access patterns can lead to hot spots, e.g. using a timestamp as a key means all writes end up going to the same partition
  - need to use something other than timestamp as the first element of the key

#### Partitioning by Hash of Key
{: .no_toc }
- because of the risk of skew and hot spots, many distributed datastores use a hash function to determine partition for a given key
- doesn't need to be cryptographically strong
  - Cassandra and MongoDB use MD5
  - Voldemort uses Fowler-Noll-Vo function
- some programming language hash functions might generate a different hash for the same data in different processes
- this can lead to *consistent hashing*, or partitions are chosen pseudo-randomly - better to avoid the term and call it *hash partitioning* (consistency is a loaded and ambiguous term)
- this method means you can't do efficient range queries
- Cassandra reaches a compromise by using *compound primary keys*, which take the first part of a key for hashing, but additional fields can be used to sort data in Cassandra's SSTables, which helps with concatenated queries (e.g. hash(user_id), timestamp would allow all updates for a particular user in a timespan)

#### Skewed Workloads and Relieving Hot Spots
{: .no_toc }
- extreme case where all requests still routed to same partition
- currently, most data systems can't compensate for this skewed workload, so application code needs to be written to accommodate
- for example, you might add two digits to hot keys, then you must keep track of them to access later

### Partitioning & Secondary Indexes
- secondary indexes are indispensable for relational databases, but they don't map neatly to partitions
- two main approaches to partitioning a database with secondary indexes:
  1. document-based partitioning
  2. term-based-partitioning

#### Partitioning Secondary Indexes by Document
{: .no_toc }
- primary indexes are maintained (document ids)
- each partition is completely separate, and indexes added are *local* to the partition
- downsides are that there is no reason that all fields with a particular value would be in the same partition, so queries would need to be sent to all partitions, which might get expensive
- *scatter/gather* - querying a partitioned database across all partitions using secondary index, then aggregated the results
- MongoDB, Riak, Cassandra, Elasticsearch, SolrCloud, and VoltDB all use document-partitioned secondary indexes

#### Partitioning Secondary Indexes by Term
{: .no_toc }
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
{: .no_toc }
- don't use modulo, since that encodes a specific number of nodes say, mod *n* means if you have n+1 nodes, all data needs to be shifted

##### Fixed Number of Partitions
{: .no_toc }
- practice of assigning many more partitions to each node, so any new node can 'borrow' partitions from each node until load is evenly spread
- e.g. each node has 100 partitions, across 10 nodes, that is 1,000 partitions. if an 11th node is adding, that node can take ~9 partitions from each node
- number of partitions is usually fixed when database is set up, making this less ideal if the size of the data set is variability (might grow much larger over time)
- hard to achieve 'just right' partition amount

##### Dynamic Partitioning
{: .no_toc }
- fixed number of partitions wouldn't work well with key range partitioned databases, so dynamic partitioning might be more effective
- when a partition grows larger than a fixed size  (HBase, default is 10GB), that partition is split and might be sent to separate nodes to balance the load
- if partition shrinks, it might be combined with adjacent partition
- can also be used for hash-partitioned data

##### Partitioning Proportionally to Nodes
{: .no_toc }
- have a fixed number of partitions per node, and those partitions grow larger with dataset size, but adding a node decreases size of partitions again
- requires hash-based partitioning, as new node randomly takes data from other nodes, and if hash-based partitioning isn't used, this would lead to unfair splits

#### Automatic or Manual Rebalancing
{: .no_toc }
- generally a good idea to have a human in the loop, as rebalancing is expensive and automation might be unpredictable

### Request Routing
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

# Chapter 7: Transactions

### What is a Transaction?
- many things can go wrong with modern data systems, and thinking around how to tolerate those faults is difficult
- **transactions** are a way to group reads and writes into one unit of work that either succeeds (*commits*) or fails (*aborts*, or *rollbacks*) to simplify the programming model for applications accessing a database
- **safety guarantees** - using transactions, applications are free to ignore certain potential error scenarios and concurrency issues because the database takes care of them
- the idea of a *transaction* came out of IBM's System R (1975), and modern transaction support is very similar still

### ACID
- term coined in 1983 by Theo Harder and Andreas Reuter to document fault-tolerance mechanisms of databases
- ACID is ambiguous and depends on implementation
- opposite is BASE (Basically Available, soft state, and eventual consistency), although this term was somewhat of a joke

**Atomicity**
  - all writes either succeed (commit) or don't (rollback), so if a fault happens during a write there is no partial write state
  - *abortability* might be a better term
> not a principle of concurrency, as in some domains concurrency means that no threads could see a half-finished state

**Consistency**
  - *consistency* is an overloaded term -- might mean: replica consistency, consistent hashing, linearizability in the C in CAP theorem, or in the ACID context "being in a good state"
  - in ACID context, consistency means that your data doesn't violate any *invariants*, or generally statements about your data that must be true, e.g. that no invoice dollar amounts are negative, that all accounts are balanced across all nodes, etc.
  - databases can't typically guarantee invariants aren't violated, so *consistency* in this context is an attribute of the application rather than the database

**Isolation**
  - concurrently executing transactions are isolated from each other
  - typically cast as *serializability*, or the idea that each transaction can pretend that it is the only transaction running, as if transactions are run serially (one after another) even if it was actually concurrently
  - in practice, serial isolation is rarely used because it has a performance penalty, so often, *snapshot isolation* is implemented

**Durability**
  - the promise that once a transaction has completed, data won't be forgotten
  - data is fsync'd to nonvolatile storage (HDD or SSD), or written to write-ahead log, or in distributed systems, replicated to nodes
  - no such thing as perfect durability, since all nodes and backups could be destroyed

#### Multi-object Writes
{: .no_toc }
- atomicity and isolation should apply when multiple objects need to be updated in a transaction, e.g. one table is updated, then another object is incremented in another table (typically achieved by explicitly wrapping SQL as a transaction e.g., `BEGIN TRANSACTION [...] COMMIT`)
- some use cases for multi-object atomicity and isolation
  - foreign key updates
  - in a document data model, fields that need to be updated are within the same document, but if denormalized data is stored that require two or more documents to be updated, you need multi-object guarantees
  - databases with secondary indexes

#### Single-object Writes
{: .no_toc }
- databases and datastores almost universally aim to provide atomicity and isolation on the level of a single object on a single node
- some provide more complex operations such as an increment operation (removing the need for a read, modify, write cycle)
- also, some provide compare-and-set operations, which only allow a value to be changed if it has not been concurrently changed by someone else

#### Handling Errors and Aborts
{: .no_toc }
- the whole point of aborts are to allow safe retries, although certain ORM tools don't allow them out of the box (Rail's ActiveRecord and Django)
- retries aren't foolproof:
  - network might fail upon alerting the client to a successful commit,
  - if the error is due to overload,
  - if there is a more permanent error,
  - if the transaction has side effects, or
  - if the client process fails while writing causing data loss

### Weak (Non-Serializable) Isolation Levels
- concurrency issues (race conditions) only come into play when two or more transactions are reading or modifying the same data
- **transaction isolation** - databases trying to hide concurrency issues from application developers
- *serializable* isolation is the highest level, but there is a performance cost, so databases mostly use weaker forms of isolation

#### Read Committed
- makes two guarantees:
  - **no dirty reads** - when reading from a database, you will only see data that has been committed
  - **no dirty writes** - when writing to a database you will only overwrite data that has been committed, typically achieved by delaying the second write until the first write's transaction is committed or aborted
- default setting in Oracle 11g, PostgreSQL, SQL Server 2012, MemSQL
- most commonly, databases prevent dirty writes by implementing row locks
- for dirty reads, locks for writes would be bad for operability -- one long-running write might slow down many reads, so typically, databases will remember the old value during a write and give that to any read until the write is committed

#### Snapshot Isolation and Repeatable Read
- **non-repeatable read (read skew)** - one in which data read twice inside the same transaction cannot be guaranteed to contain the same value. Depending on the isolation level, another transaction could have nipped in and updated the value between the two reads.
- This is allowed in read committed isolation, but might not be tolerable for backups, analytics queries, or integrity checks
- **snapshot isolation** - each transaction reads from a consistent snapshot of the database, or, a transaction sees all data that was committed to the database at the start of the transaction
- *readers never block writers, and writers never block readers*
- **multi-version concurrency control (MVCC)** - used to keep several versions of an object side by side
- different implementations use different terms for snapshot isolation (Oracle - *serializable*, PostgreSQL and MySQL - *repeatable read*) -- there is no agreement on what *snapshot isolation*/*repeatable read* is per SQL standard

#### Lost Updates
{: .no_toc }
- if two writes occur concurrently, the second write might complete and clobber the first, especially in a *read-modify-write* cycle
- one way around this is **atomic write operations**, or something like

```sql
UPDATE counters SET value = value + 1 WHERE key = 'foo''
```

- you might also explicitly lock rows using SQL's `SELECT * FROM tbl WHERE value = 'abc' FOR UPDATE` in a transaction
- you could also automatically detect lost updates and abort a transaction (supported by PostgreSQL's repeatable read, Oracle's serializable, SQL Server's snapshot isolation, but not by MySQL's repeatable read)
- another way is to do a compare-set operation (which might not fail if snapshot isolation is enabled)

```sql
UPDATE wiki_pages SET content = 'new content'
  WHERE id = 1234 and content = 'old content';
```

#### Write Skews and Phantoms
{: .no_toc }
- **write skew anomaly** - two transactions (T1 and T2) concurrently read an overlapping data set (e.g. values V1 and V2), concurrently make disjoint updates (e.g. T1 updates V1, T2 updates V2), and finally concurrently commit, neither having seen the update performed by the other
- **phantom** - where a write in one transaction changes the results of a search query in another transaction -- often occurs when a check is executed for absence of rows matching a search condition and a write adds a row matching the same condition, so there is nothing to attach a lock onto with a `SELECT FOR UPDATE` query

Imagine Alice and Bob are two on-call doctors dealing with the invariant that one doctor always needs to be on call. They both initiate a request for a day off at the same time:

    ALICE                                   BOB

    ┌─ BEGIN TRANSACTION                    ┌─ BEGIN TRANSACTION
    │                                       │
    ├─ currently_on_call = (                ├─ currently_on_call = (
    │   select count(*) from doctors        │    select count(*) from doctors
    │   where on_call = true                │    where on_call = true
    │   and shift_id = 1234                 │    and shift_id = 1234
    │  )                                    │  )
    │  // now currently_on_call = 2         │  // now currently_on_call = 2
    │                                       │
    ├─ if (currently_on_call  2) {          │
    │    update doctors                     │
    │    set on_call = false                │
    │    where name = 'Alice'               │
    │    and shift_id = 1234                ├─ if (currently_on_call >= 2) {
    │  }                                    │    update doctors
    │                                       │    set on_call = false
    └─ COMMIT TRANSACTION                   │    where name = 'Bob'
                                            │    and shift_id = 1234
                                            │  }
                                            │
                                            └─ COMMIT TRANSACTION

- one method around this is to *materialize conflicts*, or explicitly create objects for those search conditions so locks can be applied directly, although it can be hard and error-prone to materialize conflicts

### Serializability
- serializability is the strongest form of isolation because:
  - isolation levels are hard to understand and variously implemented
  - application code might not clearly tell you what isolation level you need to run at
  - there are no good tools to detect race conditions because they are non-deterministic and subject to timing
- three current methods to implement serializability: actual serialized executions, two-phase locking, and serializable snapshot isolation (SSI)

#### Actual Serial Execution
- simplest way to avoid concurrency problems is to execute the queries serially
- historically, this was difficult because a single-threaded loop for executing transactions wasn't feasible:
  - cost of RAM too high
  - OLTP transactions were disambiguated from analytic transactions
- downsides of serialized execution:
  - throughput limited to a single core CPU, which is difficult for high write throughput use cases
- constraints of serial execution
  - every transaction must be small and fast
  - active dataset must fit into memory
  - write throughput needs to be low enough to be handled by single CPU or partitioned without requiring cross-partition coordination
  - cross-partition transactions are possible but limited

##### Stored Procedures
{: .no_toc }
- a way of encapsulating interactive multi-statement transactions that are often required of today's websites, or, the ability to complete multiple database queries (e.g., for an airline: query flights, book tickets, change seats, all within the same sesssion or as part of the same form submission)
- stored procedure can execute very fast, provided all data is in memory
- stored procedures can be difficult because:
  - each database vendor has a language for stored procedures (although many modern database systems are allowing for general purpose programming languages to be used)
  - code running in a database is difficult to manage (debug, check in to version control, etc.)

##### Partitioning
{: .no_toc }
- if you can find a way of partitioning a dataset so that each transaction only needs to read and write within a single partition, each partition can have its own transaction thread
- performance drops immensely when multiple partitions are used

#### Two-Phase Locking (2PL)
- only widely used algorithm for serializability for ~30 years (up to 1970s)
> 2PL is not 2PC
- if anyone wants to write (modify or delete) an object, exclusive access is required, blocking both readers and writers with locks
- this distinguishes it from snapshot isolation, where readers never block writers and writers never block readers, and this isolation protects against most race conditions
- 2PL is serializability model used by MySQL (InnoDB) and SQL Server, and is repeatable read isolation in DB2
- each object has a lock, operating in either *shared* or *exclusive* mode
  - reading an object requires getting lock in *shared* mode, and many transactions can hold the lock
  - once a transaction wants to write, it acquires the *exclusive* lock, and only one of those is every allowed to be held
  - you can upgrade a shared to an *exclusive* lock
  - must hold the lock until transaction commits or aborts, which is second part of two phase: *first phase* - transaction is executing / *exclusive* lock acquired, *second phase* - transaction ends / locks released
- **deadlock** can occur when one transaction is waiting on another to finish
- because of acquiring all those locks and 0 concurrency, performance is not great. also, deadlocks that require abort and retry are wasted work
- in order to prevent phantoms, *predicate locks* need to be created -- these locks are applied to objects that meet certain conditions.
- predicate locks do not perform well, so *index-range locks* (aka *next key locking* are needed, which are a more generalizable way to create predicate locks (instead of creating a predicate lock on a room 123 between 12 and 1, a predicate lock could be added to lock all bookings for room 123)

#### Serializable Snapshot Isolation (SSI)
- fairly new, first described in 2008
- two types of concurrency control:
  - *pessimistic* the assumption is that if anything might go wrong, its better to wait until the situation is safe again before doing anything, e.g., acquiring *exclusive* locks
  > like *mutual exclusions* (mutex) which are used to protect data structures in multi-threaded programming
  - *optimistic* - instead of blocking, transactions continue anyway, in the hope that things turn out all right, and if a transaction breaks an isolation then it will be aborted
- based on snapshot isolation -- all transactions read from a consistent snapshot of the database
- the idea is to limit the rate of aborts, which significantly affects performance of SSI

### Chapter Summary
- Transactions are an abstraction layer that allows an application to pretend that certain concurrency problems and certain kinds of hardware and software faults don't exist. Many errors reduced to simple *transaction abort*, and the application can just retry
- transactions probably won't help applications with simple access patterns (read or write a single record)
- without transactions:
  - various error scenarios (processes crashing, network interruptions, power outages, disk full, unexpected concurrency, etc.) mean data can become inconsistent e.g., denormalized data can go out of sync with source data
  - it becomes very difficult to reason about the effects that complex interacting accesses can have on the database
- several widely used methods of concurrency control: *read commited*, *snapshot isolation* (sometimes called *repeatable read*) and *serializable*
- examples of race conditions
  - **dirty reads** - one client reads another client's writes before they have been committed. read committed and stronger prevent dirty reads
  - **dirty writes** - one client overwrites the data that another client has written but not yet committed. almost all transaction implementations prevent dirty writes
  - **read skew (nonrepeatable reads)** - a client sees different parts of the database at different times. most commonly prevented by snapshot isolation, which allows a transaction to read from a consistent snapshot at one point of time, which is typically implemented with *multi-version concurrency control* (MVCC)
  - **lost updates** - two clients concurrently perform a read-modiy-write cycle. One overwrites the other's write without incorporating changes, so data is lost. some implementations of snapshot isolation prevent this, while others require a manual lock (`SELECT [...] FOR UPDATE`)
  - **write skew** - a transaction reads something, makes a decision based on the value it saw, and writes the decision to the database. by the time the write is made, the premise of the decision is no longer true. only prevented by serializable isolation
  - **phantom reads** - a transaction reads the objects that match some search condition and another client makes a write that affects the results of that search. snapshot isolation prevents straightforward phantom reads, but phantoms in the context of write skew require special treatment, such as index-range locks
- weak isolation protects against some of these race conditions, but the application developer might need to handle others manually. only full prevention is serializability, which takes three forms:
  - **literally executing transactions in serial order** - if you can make each transaction very fast to execute, and the transaction throughput is low enough to process on a single CPU core, this is simple and effective
  - **two-phase locking** - for decades this has been the standard way of implementing serializability, but many apps avoid using it because of its performance characterisitics
  - **serializable snapshot isolation (SSI)** - a fairly new algorithm that avoids most of the downsides of previous approaches. uses an optimistic approach, allowing transactions to proceed without blocking. when a transaction wants to commit, it is checked, and it is aborted if the execution was not serializable.


# Chapter 8: The Trouble with Distributed Systems

### Faults and Partial Failures
Writing a program on a single computer, things typically work or they don't. When the hardware is working, the same operation should always produce the same output (*deterministic*).

Computers are deliberately designed for total system failure when an internal fault occurs rather than producing the wrong result, because the wrong result is hard to debug.

If we are writing software to run on several computers, things are completely different. In distributed systems, there may be parts of the system that are broken in some unpredictable way, resulting in a *partial failure*. These *partial failures* tend to be *non-deterministic* and difficult to reason about.

#### Cloud Computing and Supercomputing
{: .no_toc }
There are two spectrums on how to build large-scale computer systems:

1. *high-performance computer (HPC)* - supercomputers with thousands of CPUs, used for computationally intensive scientific computing tasks

2. *cloud computing* - not well defined, but typically associated with multi-tenant datacenters, commodity computers, elastic/on-demand resource allocation, and metered billing

These philosophies handle faults differently. One approach for supercomputers is if there is any fault, to fail the entire system.

| Supercomputers | Cloud Computer |
|--|--|
| batch jobs can be started and stopped fairly easily | many internet applications are online, and any service unavailability is unacceptable |
| built from specialized hardware and communicate through *remote direct memory access* (RDMA) so faults are infrequent | due to economies of scale can be provided at lower cost but has higher failure rates |
| use specialized network topologies yielding higher performance | often communicate through IP and Ethernet arranged in Clos topologies that provide high bisection bandwith |
| assume all their nodes are close | nodes might be geographically distributed |

If we want to make distributed systems work, we must accept the possibility of partial failure and build fault tolerance mechanisms, i.e., to build reliable systems from unreliable components.

### Unreliable Networks
Many distributed systems are *shared-nothing systems*, i.e., a bunch of machines connected by a network without the ability to access each other's memory or disk. This has become the dominant way to build systems because:

- comparatively cheap
- requires no special hardware
- makes use of commoditized cloud computing services
- achieves high reliability through redundancy across multiple geographically distributed datacenters

The internet and internal networks are *asynchronous packed networks*, meaning one node can send a message (a packet) to another node, but no guarantees when it will arrive or if it will arrive at all. If you send a request to another node and don't receive a response, it is *impossible* to tell why

#### Network Faults in Practice
{: .no_toc }
Network faults (*network partitions* or *netsplits*) can be surprisingly common, e.g.,

- EC2 has frequent transient network glitches
- sharks could bite undersea cables
- software upgrade for a switch could trigger a network topology reconfig

If software is put in an unanticipated situation, it might do arbitrarily unexpected things. Handling faults doesn't always mean *tolerating* them; you might just raise the error.

#### Detecting Faults
{: .no_toc }
Many systems need to automatically detect nodes:

- load balancer needs to stop sending requests (take *out of rotation*)
- in single leader replication, leader *failover*

Some methods of detecting a failure might be:

- if you send requests to a node that is running but no process is listening, the OS will close or refuse TCP connections wtih a `RST` or `FIN` packet
- if the node's OS is still running, a script can notify other nodes about crash
- you might be able to query the network switches themselves to detect hardware failure
- router might see that an IP address is unavailable and send an ICMP Destination Unreachable packet.

#### Timeouts and Unbounded Delays
{: .no_toc }
How long should the timeout be? A long timeout means a long wait to see if node is dead, and a short timeout might incorrectly declare nodes dead for longer running queries. Prematurely declaring a node dead is problematic, as it might just be operating slowly under load. Declaring the node dead might cause a *cascading failure* as the system can't cope with increased load and fewer resources.

Asynchronous networks have *unbounded delays*, or, there is no upper limit on time it takes for packet to arrive.

##### Network Congestion and Queueing
{: .no_toc }
Variability in packet delays most often due to queueing.

- If several nodes send packets simultaneously, the network switch queues them, and on a busy network, the queue might fill up (*network congestion*).
- If all CPU cores are busy, the OS queues up the request.
- TCP performs *flow control* (aka *congestion avoidance* or *backpressure*) to limit is own rate of sending to avoid over-burdening a network link or receiving node

Choosing timeouts is trial and error, and the balance is between failure detection delay and risk of premature timeouts. Systems that continually measure repsonse times and variability (*jitter*) are better than manually tuning.

###### TCP vs UDP
{: .no_toc }
Latency sensitive applications (such as videoconferencing and VOIP) use UDP, which doesn't perform flow control or resend lost packets. UDP is good in situations where delayed data is worthless.

#### Synchronous vs. Asychronous Networks
{: .no_toc }
A telephone network estabilishes a circuit, we say is synchronous even as the data passes through several routers as it does not suffer from queing. The maximum end-to-end latency of the network is fixed (bounded delay).

A circuit is a fixed amount of reserved bandwidth which nobody else can use while the circuit is established, whereas packets of a TCP connection opportunistically use whatever network bandwidth is available.

Using circuits for bursty data transfers wastes network capacity and makes transfer unnecessary slow. By contrast, TCP dinamycally adapts the rate of data transfer to the available network capacity.

We have to assume that network congestion, queueing, and unbounded delays will happen. Consequently, there's no "correct" value for timeouts, they need to be determined experimentally.

### Unreliable Clocks
Time is tricky -- sending messages is not instantaneous, and because of delays in networks, it is difficult to determine order things happened. Also, each machine has its own clock, which is typically a hardware device: a quartz crystal oscillator, which may run faster or slower than other clocks. One way around this is to synchronize time, e.g. as used in Network Time Protocol (NTP).

- **time-of-day clocks** - returns date and time according to some calendar (*wall-clock time*), and usually synced with NTP, which means if it is running faster than the server it might appear to jump back in time, meaning it isn't suitable for *elapsed time* measurements.
- **monotonic clocks** - good for measuring *duration*, as it is always guaranteed to move forward. The value of the monotonic clock is arbitrary (it might be time since computer turned on), making it impossible to compare monotonic clock values from two computers.

#### Clock Synchronization and Accuracy
{: .no_toc }
Quartz clocks in computers might *drift* (Google assumes clock drift of 17 seconds for a clock that is synchronized to NTP once a day). Also, a clock that is too different might refuse to sync.

Leap seconds result in time dilation -- best way to deal is to *smear*, or spread out the difference over a whole day.

#### Relying on Synchronized Clocks
{: .no_toc }
Incorrect clocks often go unnoticed, so if clock drift would affect your processes, you must carefully monitor and declare dead any resources where the clock drifts too far afield.

#### Timestamps for Ordering Events
{: .no_toc }
**It is tempting, but dangerous to rely on clocks for ordering of events across multiple nodes.** This usually imply that _last write wins_ (LWW), often used in both multi-leader replication and leaderless databases like Cassandra and Riak, and data-loss may happen.

The definition of "recent" also depends on local time-of-day clock, which may well be incorrect.

_Logical clocks_, based on counters instead of oscillating quartz crystal, are safer alternative for ordering events. Logical clocks do not measure time of the day or elapsed time, only relative ordering of events. This contrasts with time-of-the-day and monotic clocks (also known as _physical clocks_).

#### Clock Readings Have a Confidence Interval
{: .no_toc }
It doesn't make sense to think of a clock reading as a point in time, it is more like a range of times, within a confidence internval: for example, 95% confident that the time now is between 10.3 and 10.5.

The most common implementation of snapshot isolation requires a monotonically increasing transaction ID.

Google's Spanner implements snapshot isolation across datacenters by using clock's confidence interval. If you have two confidence internvals where

```
A = [A earliest, A latest]
B = [B earliest, B latest]
```

And those two intervals do not overlap (`A earliest` < `A latest` < `B earliest` < `B latest`), then B definetively happened after A.

Spanner deliberately waits for the length of the confidence interval before commiting a read-write transaction, so their confidence intervals do not overlap.

Spanner needs to keep the clock uncertainty as small as possible, that's why Google deploys a GPS receiver or atomic clock in each datacenter.

#### Process Pauses
{: .no_toc }
One method of determining leader in a leader-based system is for the leader to get a lease, and renew it periodically. This process might be flawed for several reasons:
1. garbage collection might stop processing while garbage is cleaned(*stop-the-world*)
2. virtual machines can be suspended and resumed and this pause can last for an aribtrary length of time
3. execution might be suspended when user suspends their session (closing laptop lid)
4. when OS switches to another thread or hypervisor to another machine, threads can be paused (*steal time*)
5. thread paused for disk access
6. memory access resulting in page fault (thrashing, or spending most of its time swapping pages into and out of memory)
7. unix process can be paused via `SIGSTOP`

Fairly good tools for making things thread-safe: mutexes, semaphores, atomic counters, lock-free data structures, blocking queues, etc. But these tools don't translate to dsitributed system because there is no shared memory.

##### Response Time Guarantees
{: .no_toc }
There are systems that require software to respond before a specific _deadline_ (_real-time operating system, or RTOS_).

Library functions must document their worst-case execution times; dynamic memory allocation may be restricted or disallowed and enormous amount of testing and measurement must be done.

##### Limiting the Impact of Garbage Collection
{: .no_toc }
Garbage collection could be treated like brief planned outages. If the runtime can warn the application that a node soon requires a GC pause, the application can stop sending new requests to that node and perform GC while no requests are in progress.

A variant of this idea is to use the garbage collector only for short-lived objects and to restart the process periodically. For example, Instagram turned off Python's garbage collection entirely to be more performant.

### Knowledge and Truth in Distributed Systems
{: .no_toc }
In a distributed system, we can state the assumptions we are making about the behavior (_system model_) of a system.

#### The Truth is Defined by the Majority
{: .no_toc }
Many distributed systems rely on _quorums_, or majority votes, to determine what the truth is, e.g., whether a node is dead. There can only be one majority at a time.

##### Fencing Tokens
{: .no_toc }
We need to ensure that a node that is under a false belief of being "the chosen one" cannot disrupt the rest of the system

_fencing token_ - a monotonically increasing token that a client needs to include to a write to a data system, which should prevent undetected lease expiry.

#### Byzantine Faults
{: .no_toc }
_byzantine fault_ - is a condition of a computer system, particularly distributed computing systems, where components may fail and there is imperfect information on whether a component has failed.

**Byzantine General Problem**
> In its simplest form, the generals must decide only whether to attack or retreat. Some generals may prefer to attack, while others prefer to retreat. The important thing is that every general agree on a common decision, for a halfhearted attack by a few generals would become a rout, and would be worse than either a coordinated attack or a coordinated retreat.
>
> The problem is complicated by the presence of treacherous generals who may not only cast a vote for a suboptimal strategy, they may do so selectively. For instance, if nine generals are voting, four of whom support attacking while four others are in favor of retreat, the ninth general may send a vote of retreat to those generals in favor of retreat, and a vote of attack to the rest. Those who received a retreat vote from the ninth general will retreat, while the rest will attack (which may not go well for the attackers). The problem is complicated further by the generals being physically separated and having to send their votes via messengers who may fail to deliver votes or may forge false votes.


## Chapter Summary
- Whenever you try to send a packet over the network, it may be lost or arbitrarily delayed. Likewise, the reply may be lost or delayed, so if you don’t get a reply,you have no idea whether the message got through.
- A node’s clock may be significantly out of sync with other nodes (despite your best efforts to set up NTP), it may suddenly jump forward or back in time, and relying on it is dangerous because you most likely don’t have a good measure ofyour clock’s error interval.
- A process may pause for a substantial amount of time at any point in its execu‐tion (perhaps due to a stop-the-world garbage collector), be declared dead byother nodes, and then come back to life again without realizing that it waspaused.

The fact that such partial failures can occur is the defining characteristic of distributed systems. Whenever software tries to do anything involving other nodes,there is the possibility that it may occasionally fail, or randomly go slow, or not respond at all (and eventually time out). In distributed systems, we try to build tolerance of partial failures into software, so that the system as a whole may continue functioning even when some of its constituent parts are broken.

To tolerate faults, the first step is to detect them, but even that is hard. Most systems don’t have an accurate mechanism of detecting whether a node has failed, so most distributed algorithms rely on timeouts to determine whether a remote node is still available. However, timeouts can’t distinguish between network and node failures,and variable network delay sometimes causes a node to be falsely suspected of crash‐ing. Moreover, sometimes a node can be in a degraded state: for example, a Gigabit network interface could suddenly drop to 1 Kb/s throughput due to a driver bug.Such a node that is “limping” but not dead can be even more difficult to deal with than a cleanly failed node.

Once a fault is detected, making a system tolerate it is not easy either: there is no global variable, no shared memory, no common knowledge or any other kind of shared state between the machines. Nodes can’t even agree on what time it is, let alone on anything more profound. The only way information can flow from one node to another is by sending it over the unreliable network. Major decisions cannot be safely made by a single node, so we require protocols that enlist help from other nodes and try to get a quorum to agree.

If you’re used to writing software in the idealized mathematical perfection of a single computer, where the same operation always deterministically returns the same result,then moving to the messy physical reality of distributed systems can be a bit of a shock. Conversely, distributed systems engineers will often regard a problem as trivial if it can be solved on a single computer, and indeed a single computer can do a lot nowadays. If you can avoid opening Pandora’s box and simply keep things on a single machine, it is generally worth doing so.

However, as discussed in the introduction to Part II, scalability is not the only reason for wanting to use a distributed system. Fault tolerance and low latency (by placing data geographically close to users) are equally important goals, and those things can‐not be achieved with a single node.

Whether the unreliability of networks, clocks, and processes is an inevitable law of nature. We saw that it isn’t: it is possible to give hard real-time response guarantees and bounded delays in net‐works, but doing so is very expensive and results in lower utilization of hardware resources. Most non-safety-critical systems choose cheap and unreliable over expensive and reliable.

Also supercomputers, which assume reliable components and thus have to be stopped and restarted entirely when a component does fail. By contrast,distributed systems can run forever without being interrupted at the service level,because all faults and maintenance can be handled at the node level—at least in theory. (In practice, if a bad configuration change is rolled out to all nodes, that will still bring a distributed system to its knees.)


# Chapter 9: Consistency and Consensus
**consensus** - An important abstraction in distributed systems which means getting the nodes to all agree on something. This can be a tricky problem in the presence of network faults and process failures.

## Consistency Guarantees
When you look at two database nodes at the same time, you might see different data because write requests arrive to nodes at different times.

Most databases provide *eventual consistency*, or the idea that if you stop writing and wait an unspecified amount of time, all reads will return the same value. This might also be called *convergence*.

Transactions are not the same as distributed consistency models: transaction isolation is primarily about avoiding race conditions due to concurrently executing transactions, whereas distributed consistency is mostly about coordinating the state of replicats in the face of delays and faults.

## Linearizability
**linearizability** (aka *atomic consistency*, *strong consistency*, *immediate consistency*, *external consistency*) - A *recency guarantee* that a system appears as if there is only one copy of the data even if there are many, and all operations are automic.

### What Makes a System Linearizable?
{: .no_toc }
In linearizable systems there must be some point in time at which the value for a *register* (a single object, as in a key:value, a row, a document) must atomically switch from old value to new, and if one read returns the new value, all subsequent reads must return the new value.

three operations a database must have:
- `read(x) => v` read from register `x`, return value `v`
- `write(x, v) => r` client requests to set register `x` to `v` and returns response `r`
- <code>cas(x, v<sub>old</sub>, v<sub>new</sub>) => r</code> an atomic compare-and-set operation. If the value of the register x equals v_old, it is atomically set to v_new. If x != v_old the registers is unchanged and it returns an error

**serializability** - is an isolation property of transactions where every transaction may read or write multiple objects, and guarantees that transactions behave as if they were executed in *some* serial order

**linearizability** - a recency guarantee on reads and writes of a register (single object), so it doesn't prevent problems such as write skew

_strict serializability_ (aka _strong one-copy serializability_) - database rovides both linearizability and serializability

### Relying on Linearizability
{: .no_toc }
Some systems require linearizability:

- _locking and leader election_ - To ensure that there is indeed only one leader, a lock is used. It must be linearizable: all nodes must agree which nodes owns the lock; otherwise is useless. Apache Zookeeper and etcs are often used for distributed locks and leader election.
- _constraints and uniqueness guarantees_ - in order to enforce uniqueness, system needs to be linearizable.
- _cross-channel timing dependencies_ - if there are multiple communication channels for messages and data to travel, there might be a race condition between those two channels (think message queue and file system writes)

### Implementing Linearizable Systems
{: .no_toc }
