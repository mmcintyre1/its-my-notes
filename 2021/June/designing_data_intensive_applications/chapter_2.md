
# Chapter 2: Data Models and Query Languages
- [Chapter 2: Data Models and Query Languages](#chapter-2-data-models-and-query-languages)
    - [Relational Model](#relational-model)
    - [Document Model](#document-model)
    - [Graph Model](#graph-model)
      - [property graph](#property-graph)
      - [triple-stores](#triple-stores)
        - [semantic web](#semantic-web)
    - [Many-to-One and Many-to-Many Relationships](#many-to-one-and-many-to-many-relationships)
    - [Relational vs Document](#relational-vs-document)
      - [simpler application code](#simpler-application-code)
      - [schema flexibility](#schema-flexibility)
      - [data locality](#data-locality)
      - [convergence](#convergence)
    - [Query Languages](#query-languages)
      - [SQL](#sql)
      - [MapReduce Querying](#mapreduce-querying)
      - [Cypher](#cypher)
      - [Querying Graph Models with SQL](#querying-graph-models-with-sql)
      - [SPARQL](#sparql)
      - [Datalog](#datalog)
  - [Chapter Summary](#chapter-summary)

Data models are perhaps the most important part of developing software -- most applications are built by layering one data model on top of another, with each layer hiding the complexity of the layers below it by providing a clean data model
1. as an app developer, you model the real world in terms of objects or data structures, and APIs manipulate those structures
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
- use cases for 'NoSQL'
- need for greater scalability, including for very large datasets or very high write throughput
    - preference for free and open source software
    - specialized query operations not well supported by relational model
    - frustration with restrictiveness of relational schemas, and desire for more expressive and dynamic data model
- *polyglot persistence*: many future use cases might employ document and relational models

### Graph Model
- graph consists of two objects:
    - *vertices* (aka *nodes* or *entities*)
    - *edges* (aka *relationships* or *arcs*)

#### property graph
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
- similar to property graphs, just describes things with different words
- all info stored as three-part statement - subject, predicate, object. e.g. JIM LIKES EGGS (JIM - subject, LIKES - predicate, EGGS - object)
##### semantic web
- while not all triple-stores are synonymous with the semantic web, they are interlinked in many minds
- semantic web is the idea that websites could publish machine-readable information about their sites in a consistent format to form a 'web of data' (note Berners-Lee constantly says there is no data layer for the internet)
- *RDF* - Resource Description Framework - is positioned as that format
	- Apache Jena popular tool for this

### Many-to-One and Many-to-Many Relationships
- Storing standardized list of data, so you can join to that data and prevent duplication (normalized data)
- 1st Normal Form (NF), 2NF, 3NF, etc have little practical difference -- rule of thumb, if you are duplicating values that could be stored in one place, your schema is not normalized
- normalizing requires a many-to-one relationship, something not supported well with document model (support for joins is weak), meaning you need to shift that logic to application code over database model logic

### Relational vs Document

#### simpler application code
- if your data is document-like, use document (*shredding* - relational technique of splitting a document-like structure into multiple tables, makes for complicated application code)
- if you need many-to-many or joins, use relational

#### schema flexibility
- *schema-on-write* (relational): structure of data is explicit and database ensures all data conforms to it
- *schema-on-read* (document): structure of data is implicit and only interpreted when data is read
- NOTE: `ALTER TABLE` typically fast except for MySQL, where the entire table is copied

#### data locality
- if joins aren't required for your document, then there is a performance advantage to all data in a single document (called *storage locality*)
- some relational databases group related data together to achieve storage locality
    - Google's Spanner (allows schema to declare table's rows interleaved (nested) with a parents)
    - Oracle through *multi-table index cluster tables*
    - Bigtable (Cassandra and HBase) through *column-family*

#### convergence
- many relational databases support JSON (PostGreSQL 9.3+, MySQL 5.7+)
- many relational databases support XML (other than MySQL)

### Query Languages

#### SQL
- SQL is a *declarative* language which follows the structure of relational algebra closely
- other declarative languages are XSL or CSS
- *imperative* languages tell the computer to perform operations in order (most programming languages)
- declarative languages lend themselves to parallel execution
-
#### MapReduce Querying
- programming model for processing large amounts of data across multiple machines created by Google
- you specify two functions -- `map` (aka `collect`), and a `reduce` (aka `fold` or `inject`). Below is MapReduce implemented in MongoDB:
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
- declarative language implemented by Neo4j and used to query property graphs

#### Querying Graph Models with SQL
- you can query graph models in SQL, it is just extremely verbose, and relies on a *recursive common table expression* `WITH RECURSIVE`

#### SPARQL
- query language for triple-stores using RDF data model
- similar to Cypher (Cypher borrows its pattern matching from SPARQL)

#### Datalog
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