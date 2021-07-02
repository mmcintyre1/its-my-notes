# Chapter 4: Encoding and Evolution
- [Chapter 4: Encoding and Evolution](#chapter-4-encoding-and-evolution)
  - [Formats for Encoding Data](#formats-for-encoding-data)
    - [Language-Specific Formats](#language-specific-formats)
    - [JSON, XML, and Binary Variants](#json-xml-and-binary-variants)
    - [Thrift and Protocol Buffers](#thrift-and-protocol-buffers)
    - [Avro](#avro)
  - [Modes of Dataflow](#modes-of-dataflow)
    - [Dataflow through Databases](#dataflow-through-databases)
    - [Dataflow through Services: REST and RPC](#dataflow-through-services-rest-and-rpc)
      - [Web Services](#web-services)
        - [REST](#rest)
        - [SOAP](#soap)
      - [RPC](#rpc)
    - [Dataflow though async messages](#dataflow-though-async-messages)
      - [Distributed actor frameworks](#distributed-actor-frameworks)
  - [Chapter Summary](#chapter-summary)

## Formats for Encoding Data
- Programs typically work with data in two ways:
  1. in memory: kept in objects (list, array, struct, hash table, etc.) and efficiently accessed and manipulated by CPU (typically via pointers)
  2. out of memory: you need to encode data into a self-contained sequence of bytes to write to file or send over network, etc
- **encoding** - the translation of in-memory representation to byte sequence (aka *serialization* or *marshalling*), and the opposite action is *decoding* (aka *parsing*, *deserialization*, *unmarshalling*)

### Language-Specific Formats
- many languages have built-in support for encoding in-memory objects to byte sequences:
  - `java.io.Serializable` for Java
  - 'Marshal` for Ruby
  - `pickle` for python
- this languages bind you to the programming language, and instantiate arbitrary classes or execute arbitrary code, which is a security risk

### JSON, XML, and Binary Variants
- JSON, XML, and CSV are textual formats and will remain valuable especially as interchange formats between organizations, but there are limitations:
  - **ambiguity around encoding numbers** - in XML and CSV, you can't distinguish between a number a string that happens to consist of digits. JSON doesn't distinguish integers and floats, and doesn't distinguish precision, which is a problem with large numbers (> 2<sup>53</sup>)
  - **binary strings** - JSON and XML have good support for Unicode character strings, but not binary strings -- binary strings are typically encoded as text using Base64, which is hacky and increases data footprint by 33%
  - **schema support** - schema support is ubiquitous for XML, but used less often for JSON, and there is no schema support for CSV. Schema languages are powerful but complicated to learn
- Binary variants for JSON - BSON, BJSON, UBJSON, BISON, Smile, etc
- Binary variants for XML - WBXML, Fast Infoset, etc

### Thrift and Protocol Buffers
- binary encoding libraries that encode object name and type using a schema
- Google invented Thrift, Facebook invented protobuf
- Thrift has two encoding formats, BinaryProtocol and CompactProtocol

### Avro
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
- when HTTP is used for the underlying protocol of talking to the service, it is called a *web service*
- two popular approaches: REST and SOAP, which are almost opposite in terms of philosophy

##### REST
- REST is not a protocol but a design philosophy
  - simple data formats
  - URLs for identifying resources
  - using HTTP for cache control, authentication, and content type negotiations
- an API designed according to REST principles is *RESTful*
- definition format such as OpenAPI (aka Swagger) can be used to describe RESTful APIs and produce documentation

##### SOAP
- XML based protocol for making API requests, most commonly used over HTTP but comes with a complex plethora of related standards (*web service framework*, aka *WS-\**)
- described using Web Services Description Language (WSDL), which is not designed to be human-readable
- ostensibly standardized, but interoperability between different vendor impl. might cause problems

#### RPC
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
  -
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
