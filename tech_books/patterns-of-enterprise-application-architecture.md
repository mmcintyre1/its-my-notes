---
last_modified_date: "2021-11-14 19:40:54.029576"
nav_order: 99
---
# Patterns of Enterprise Application Architecture
## What is Architecture?
1. high level breakdown of system into parts
2. decisions that are hard to change

> In the end, architecture boils down to the important stuff -- whatever that is. (2)

- most widely used technique is to break (decompose) the application into layers and how these layers work together

## Enterprise Applications
- they involve persistent data around for multiple runs of an application
- lots of data
- many users access data concurrently which involves potential access issues
- lots of user interface screens to interact with data
- need to integrate with other apps in a variety of different languages/stacks
- conceptual dissonance between technology and data -- needs to be read, munged, & written in a variety of syntactic and semantic flavors
- complex business "illogic" to handle domain complexity

## Performance
- any performance advice shouldn't be treated as fact until actually tested
- basic, universal advice - **minimize remote calls**
- significant changes to config will invalidate assumptions about performance
- some performance vocab
  - **response time** - time it takes for system to process response fromt he outside
  - **responsiveness** - how quickly system acknowledges requests as opposed to processing
  - **latency** - minimum time required to get any form of response
  - **throughput** - how much stuff you can do in a given time
  - **load** - how much stress a system is under
  - **load sensitivity** - how response time varies under load (a system degrades under load)
  - **efficiency** - performance divided by resources
  - **capacity** - max effective throughput or load
  - **scalability** - how additional resources affect performance and can either be horizontal (scaling out, adding new machines) or vertical (scaling up, adding memory, CPU, storage to a machine)

## Pattern

> Each  pattern  describes  a  problem which  occurs  over  and over  again in our environment, and then describes the core of the solution to that problem, in a  way  that  you  can  use  this  solution  a  million  times  over, without  ever doing it the same way twice. (9)

- focus of a pattern is a common and effective solution to a particular problem
- don't read all the details of each pattern, just enough to know what to look up
- never apply a solution blindly
- value isn't giving you the idea of a pattern but rather helping you communicate it


## Layers
- way to decompose complicated software systems
- high level layer uses lower level services, but lower level should remain unaware of higher level
- benefits:
  - single layer as a coherent whole without knowing much about other layers
  - you can substitute layers
  - minimize dependencies between layers
  - layers are good places for standardization
  - lower layers can be reused for multiple higher level services
- downsides:
  - you can't encapsulate everything (thinking adding an additional UI element requires database changes and corresponding changes to all intermediary layers)
  - performance hit for layering

## 3 Principal Layers
- **presentation** - handles interaction between user and software - interprets actions/commands and displays info to user
- **data source** - communicates with other systems that carry out task on behalf of the application
- **domain logic** - business logic that is work the application does for the domain you're working in

| Layer        | Responsibilities                                                                                                                                                                      |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Presentation | Provision of services, display of information (e.g., in Win-dows or HTML, handling of user request (mouse clicks, keyboardhits), HTTP requests, command-line invoca-tions, batch API) |
| Domain Logic | that is the real point of the system                                                                                                                                                  |
| Data Source  | Communication with databases, messaging systems, trans-action managers, other packages                                                                                                |

- **hexagonal architecture** - any system as a core surrounded by interfaces to external systems -- this is a symmetrical view that doesn't distinguish between services you provide and services you consume
- choose most appropriate for of separation for problem, but make sure there is separation
- domain and data source should never be dependent on presentation
- generally, we are talking about logical layers -- typically physical layers break down to client vs. server
- don't separate layers into discrete processes unless needed.
- **complexity boosters**: they all come at a cost. *e.g.,* extreme performance requirements, explicit multi-threading, distribution, paradigm chasms

## Domain Logic
3 patterns to organize domain logic
- _transaction script_
- _domain model_
- _table module_

## Transaction Script
- _transaction_ here is used in the sense of a business operation, not an ACID-compliant database transaction
- single procedure for each action a user might want to do
- useful for very simple domains, since as logic increases in complexity, duplication increases, and application code becomes hard to untangle
- all behavior for action is within the transaction script

## Domain Model
- build a model of the domain around the nouns in the domain
- behavior then is in the interactions between objects
- moving to domain model involves a paradigm shift to object-oriented thinking
- have to deal with more complex mapping to database

## Table Module
- looks like domain model, but instead of object for all nouns, you get an object for every table in the database
- pulls all records as a _Record Set_ from the database, and in order to work on 1 you'd pass in an `id` to that _Record Set_
- there needs to be special tooling for these _Record Sets_

## Record Set
- in memory representation of tabular data
- looks exactly like the result of a SQL query but can be manipulated by other parts of the system
- can easily be manipulated by domain logic
- typically a list of maps: `[{...}, {...} ...]`
- can have an implicit or implicit interface (think `person['name']` vs `person.name`)
- can be connected (need active connection to database), or disconnected (can be manipulated offline)

## Service Layer
- defines application boundary with a layer of services that establish a set of available actions (API) & coordinates the applications response to each operation
- lay over a _Domain Model_ or a _Table Module_ and provides a clean API & a good spot to put things like transaction control and security
- minimal case is to make it a _Façade_, maximal is to put business logic in it
- **controller entity** - have logic and behavior exclusive to use case or transaction in a separate _Transaction Script_ called a controller or service type

## Gateway (Base Pattern)
- an object that encapsulates access to an external resource or system
- in reality, this is a simple wrapper pattern
- good spot to apply service stub
- some overlap with Gang of Four patterns _Façade_ and _Adapter_
- useful for encapsulating an awkward interface for something rather than letting it affect rest of code
- if you need to decouple subsystems, another choice is _Mapper_, but this is more complicated

## Mapper (Base Pattern)
- an object that sets up communication between two independent objects
- similar to _Mediator_
- useful when you want neither subsystem to have dependency on their interaction, like with a database (_Data Mapper_)
