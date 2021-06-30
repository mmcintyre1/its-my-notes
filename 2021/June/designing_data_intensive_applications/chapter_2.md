# Chapter 2: Data Models and Query Languages
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
	- Object-relational mapping (ORM) frameworks like ActiveRecord, Hibernate, SQLAlchemy might reduce boilerplate code for that layer, but they don't hide it completely

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
-
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


## Chapter Summary
