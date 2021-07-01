
# Chapter 3: Storage and Retrieval

at a fundamental level, a database needs to do two things:

1. when you give it data it should store the data
2. when you ask it later it should give the data back to you

## Log-structured storage
- many databases internally use a log, or append only sequence of records, to store data (different from application logs, which are typically text files emitted by an application to describe what is happening)

### Indexes
- an *additional structure* used to efficiently find data within a database
- keep some additional metadata on the side which acts a signpost to help you locate the data you want
- speeds up read performance but degrades write performance (typically because index needs to be updated after every write)

#### Hash Indexes
- simple index of key:value pairs stored in a hash map/dictionary on disk, where each key is associated with a byte offset to lookup the value on disk
- Bitcask, the default storage engine for Riak, does this
- this sort of use case is well-suited for frequent updates to values and where the hash map can fit in memory
- important things to consider for this implementation:
	- **file format**: binary format that first encodes the length of string in bytes then the raw string (without needing to escape chars)
	- **deleting records**: if you want to delete a record, you need to append a special delete record (sometimes called a tombstone) to signal during compaction merge to remove the record
	- **crash recovery**: since the hash map is in memory, restarts mean you lose the hash map. you can store version on disk to warm start the hash map
	- **partially written records**: crashes can happen at any time, even partially through writes. Bitcask uses checksums to ignore corrupted parts of log
	- **concurrency control**: since writes are sequential append only, its common to only have a single writer. Data files are append only and immutable, so they can be read concurrently
	-
##### segment files
- since the log is an append-only structure, we need to keep *segment files* to prevent running out of space
- after a segment file reaches a certain size, we can create a new one to write to, then perform *compaction* on the older segment files, meaning, throwing away duplicate keys in the log and keeping only the most recent update
	- older segment files are merged in the background then swapped without interruption to writes

#### SSTables
- **Sorted String Table** (SSTable) - takes the idea for hash indexes, but requires that segment files be sorted in order by key. also requires that each key only appears once in each merged segment table (because in order to do compaction, we need to mergesort, which relies on uniqueness of keys)
- keys duplicated across segment files don't matter, since most recent segment contains most up to date value per key
- your in memory hash index can be sparse, because keys are sorted and so easy to scan (typically one index per every few kilobytes is sufficient)
- you can compress blocks and then just point the index at a block, saving disk space and I/O
##### LSM-Trees
- described in Patrick O'Neil et al *Log-Structured Merge-Tree* or LSM-tree
- *memtable* and SSTable introduced by Google's Bigtable paper
- how do we maintain sorted order? much easier in memory than on disk
	- write comes in, add to a balanced tree data structure (e.g. a red-black tree) - this is typically called a *memtable*
	- when *memtable* is larger than a threshold, write that *memtable* as an SSTable file to disk. start new *memtable* while old is being written to disk
	- to serve a read request, first check *memtable*, then first segment file, then second, etc.
	- from time to time, run a merging and compaction process for older segment files
	- maintain an append only log on disk that holds all writes, to recover the *memtable* in case of crash (you can delete after current *memtable* is written to disk)

#### B-Trees
- keeps indexes sorted by value, but instead of storing database in segment files, B-Trees store database in fixed size *blocks* or *pages*, which corresponds more closely to underlying hardware
- you start at the root of the tree. each page contains references (like pointers but on disk) to child pages until you get to a page of individual keys (a leaf page), which either contains the value or references to the page where the value can be found
- number of references to child pages called the *branching factor*
- trees are balanced, so traversal is always O(log *n*) -- most databases can fit into a B-tree that is three or four levels deep (e.g. a four-level tree of 4 KB pages with a branching factor of 500 can store 256 TB)

##### reliability
- many B-tree impl. use write-ahead logs (WAL), aka redo logs, to persist all writes to the database in an append only log before it can be applied to pages

#### B-Trees vs LSM-Trees
- B-Trees need to write data twice, once to the write-ahead log and once to page
- Log-structured indexes might write data multiple times due to repeated compaction and merging (write amplification) and is particularly concerning for SSD's, which can only overwrite blocks a limited amount of times before wearing out
- LSM-Trees typically able to sustain higher write throughput because they often have lower write amplification
- B-Trees have keys that exist exactly one place in index, which is good for databases that want strong transactional semantics via transaction isolation and locks

#### Secondary Indexes
- both log-structured and B-Trees can work as secondary indexes in addition to a primary key index. These secondary indexes don't need to be unique (unless you add that constraint)

#### Storing values within the index
- the value of the index might be an actual row, or it might be a reference to the row, typically stored in a *heap file* -- data in these heap files are not stored in any particular order
- updating a value in a heap file can be efficient by overwriting the data in place (assuming the data is the same length)
- *clustered index* - storing the row directly in the index, and secondary indexes just refer to the primary key
- a compromise between clustered and non-clustered is a *covering index*, or *index with included columns*, which stores some of the tables columns within an index, allowing queries to be 'covered' or answered by an index alone

#### Multi-column indexes
- concatenated indexes used to store indexes for multiple columns, which is good for searching full index combinations, but not individual columns after the primary key
- multi-dimensional indexes are a good way to query several columns at once, especially for geospatial data. R-Trees are typically used instead of B-Trees

#### Full-text search and fuzzy indexes
- Lucene is able to search for words within a certain edit distance (edit distance meaning when 1 letter has been added, removed, or replaced)
- *Levenshtein distance* - used to figure out amount of edits required to go from one word to another

#### In memory databases
- we typically use disks because they are durable and cost less per gigabyte than RAM (the second argument is becoming less relevant)
- **Memcached** - an entirely in memory cache (lost if restarted)
- other in-memory databases aim for more durability, writing log of changes to disk, writing periodic snapshots, etc.
- **VoltDB**, **MemSQL**, and **Oracle TimesTen** are relational in-memory databases
- anti-caching approach is a way around working with datasets larger than memory, by persisting data to disk when out of memory, and bringing back into memory when used (this is similar to virtual memory and swap files at OS level)
- new area of research - *nonvolatile memory* (NVM); still in infancy

#### Transactions vs Analytics

| Property | Transaction processing systems (OLTP) | Analytics systems (OLAP) |
|--|--|--|
| Main read pattern | small number of records per query, fetched by key | aggregate over large number of records  |
| Main write pattern | Random-access, low-latency writes from user input | Bulk import (ETL) or event stream |
| Primarily used by | End user/customer via web application | Internal analyst, for decision support |
| What data represents | Latest state of data (current point in time) | History of events that happened over time |
| Dataset size | Gigabytes to terabytes | Terabytes to petabytes |

#### Data Warehouses
- you store data in an OLAP data warehouse as it will be insulated from live transaction processing and queries won't affect live customer-facing systems
- typically perform Extract-Transform-Load (ETL) operations to populate the database
- Data warehouses typically sell their systems under expensive commerical licenses (e.g. Amazon RedShift is a host version of ParAccel)
- Some are based on the ideas from Google's Dremel
- many data warehouses can have hundreds of columns
- The typical use case for OLAP queries are only accessing a small amount of many columns -- unlike OLTP systems which are *row-oriented storage*, meaning that a row is stored in contiguous bytes on disks, OLAP systems are *column-oriented storage*, which stores a column in contiguous bytes.

##### Star and Snowflake Schema
- many data warehouses use *star schema* as their data model (known as *dimensional modeling*)
- at the center of the schema is a *fact table*, most often representing a particular event
- some of the columns are attributes of the event, while others are foreign key references to other tables called *dimension tables*, which typically represent the who, what, where, when, how, and why of the event
- *snowflake schema* - a variation of the star schema, but dimensions are broken even further into sub-dimensions

##### Column Compression
- since there are far less distinct values in a column than there are rows, we can compress this data. a popular method is *bitmap encoding*, which details all the unique values in a column, then encodes an array of 1s and 0s for whether a row contains that value, which creates sparse data sets, which can be compressed more easily by encoding run length (how many 1s or 0s in a row)

##### Vectorized Processing
- the query engine can take a chunk of compressed column data that fits in the CPU's L1 cache, and iterate through in a tight loop (no function calls) much more quickly than if many function calls are required, e.g. to type cast data formats

##### Materialized Views
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
