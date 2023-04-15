---
last_modified_date: "2022-08-13 19:40:54.029576"
nav_order: 3
book_title: "The Fundamentals of Software Architecture"
subtitle: "An Engineering Approach"
author: "Mark Richards and Neal Ford"
nav_exclude: true
parent: Tech Books
publication_year: 2020
---
# The Fundamentals of Software Architecture: An Engineering Approach
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
1. TOC
{:toc}
</details>

# Defining Software Architecture

1. **the structure of the system**
  - refers to the type of architecture style (or styles) the system is implemented in (such as microservices, layered, or microkernel)
2. **architecture characteristics**
  - The architecture characteristics define the success criteria of a system, which is generally orthogonal to the functionality of the system
3. **architecture decisions**
  - define the rules for how a system should be constructed
4. **design principles**
  - A design principle differs from an architecture decision in that a design principle is a guideline rather than a hard-and-fast rule

# Expectations of an Architect
1. **make architecture decisions**
 - An architect is expected to dene the architecture decisions and design principles used to guide technology decisions within the team, the department, or across the enterprise.
2. **continually analyze the architecture**
  - An architect is expected to continually analyze the architecture and current technology environment and then recommend solutions for improvement.
3. **keep current with the latest trends**
  - An architect is expected to keep current with the latest technology and industry trends.
4. **ensure compliance with decisions**
  - An architect is expected to ensure compliance with architecture decisions and design principles.
5. **diverse exposure and experience**
  - An architect is expected to have exposure to multiple and diverse technologies, frameworks, platforms, and environments.
6. **have business domain knowledge**
  - An architect is expected to have a certain level of business domain expertise.
7. **possess interpersonal skills**
  - An architect is expected to possess exceptional interpersonal skills, including teamwork, facilitation, and leadership.
8. **understand and navigate politics**
  - An architect is expected to understand the political climate of the enterprise and be able to navigate the politics.

- useful to separate software development _process_ from _engineering practices_
- **process** - how teams are formed and managed, how meetings are conducted, and workflow organization; it refers to the mechanics of how people organize and interact
- **engineering practices** - process-agnostic practices that have illustrated, repeatable benefit
- **architectural fitness functions**: an objective integrity assessment of some architectural characteristic(s)

# Laws of Software Architecture
1. Everything in software architecture is a trade-off
   1. If an architect thinks they have discovered something that isn’t a trade-off, more likely they just haven’t identified the trade-off yet
2. _Why_ is more important than _how_

# Thinking Like an Architect
1. understand the difference between architecture and design, and understand how to collaborate with dev teams to make architecture work
2. have a wide breadth of technical knowledge while still maintaining a certain level of technical depth -- see solutions and possibilities others do not
  - breadth is more important than depth
  - **frozen caveman anti-pattern** -- someone who always reverts back to their pet irrational concern for every architecture
3. understanding, analyzing, and reconciling trade-offs between various solutions and technologies
4. understanding the importance of business drivers and how they translate to architectural concerns

# Modularity
**modularity** - a logical grouping of related code, which could be a group of classes in an object-oriented language or functions in a structured or functional language, e.g., `package` in Java, `namespace` in .NET

## Cohesion
**Cohesion** refers to what extent the parts of a module should be contained within the same module -- less precise than coupling

From best to worst cohesion
1. **functional cohesion** - every part of the module is related to the other, and the module contains everything essential to function
2. **sequential cohesion** - two modules interact, where one outputs data that becomes the input for the other
3. **communicational cohesion** - two modules form a communication chain, where each operates on info and/or contributes to some output
4. **procedural cohesion** - two modules must execute code in a particular order
5. **temporal cohesion** - modules are related based on timing dependencies
6. **logical cohesion** - data within modules is related logically but not functionally
7. **coincidental cohesion** - elements in a module are not related other than being in the same source file

- the **Chidamber and Kemerer Object- oriented metrics suite** is a well-known suite of metrics to test cohesion (and coupling) like cyclomatic complexity
- **Chidamber and Kemerer Lack of Cohesion in Methods** (LCOM) -- The sum of sets of methods not shared via sharing fields

<div style="text-align:center">
  <a href="/assets/img/fundamentals-of-software-architecture/lcom.jpg">
    <img src="/assets/img/fundamentals-of-software-architecture/lcom.jpg" alt="">
  </a>
</div>

## Coupling
**afferent coupling** - measures the number of _incoming_ connections to a code artifact (component, class, function, etc)

**efferent coupling** - measures number of _outgoing_ connections to a code artifact

**abstractness** - ratio of abstract artifacts (abstract classes, interfaces, etc) to concrete artifacts (implementation)

**instability** - ratio of efferent coupling to the sum of both efferent and afferent coupling -- determines volatility of code base; an unstable codebase breaks more easily when changed

**distance from the main sequence**
$D = |A + I - 1|$
- A = abstractness and I = instability

<div style="text-align:center">
  <a href="/assets/img/fundamentals-of-software-architecture/distance-from-main-sequence.jpg">
    <img src="/assets/img/fundamentals-of-software-architecture/distance-from-main-sequence.jpg" alt="">
  </a>
</div>

## Connascence
Two components are **connascent** if a change in one would require the other to be modified in order to maintain the overall correctness of the system -- recasting efferent and afferent coupling for object-oriented language (those measures of coupling predate OOP)

### Static Connascence
{: .no_toc }
- source-code-level coupling

- **Connascence of Name (CoN)**Multiple components must agree on the name of an entity.
- **Connascence of Type (CoT)** Multiple components must agree on the type of an entity.
- **Connascence of Meaning (CoM) or Connascence of Convention (CoC)** Multiple components must agree on the meaning of particular values.
- **Connascence of Position (CoP)** Multiple components must agree on the order of values.
- **Connascence of Algorithm (CoA)** Multiple components must agree on a particular algorithm.


### Dynamic Connascence
{: .no_toc }
- calls executed at runtime

- **Connascence of Execution (CoE)** The order of execution of multiple components is important
- **Connascence of Timing (CoT)** The timing of execution of multiple components is important
- **Connascence of Values (CoV)** Occurs when several values rely on one another and must change together
- **Connascence of Identity (CoI)** Multiple components must reference the same entity

### Properties of Connascence
{: .no_toc }

**strength**
- the ease with which a developer can refactor that type of coupling
- refactor towards better types of connascence
- prefer static to dynamic, as its easier for static code analysis

<div style="text-align:center">
  <a href="/assets/img/fundamentals-of-software-architecture/connascence-refactor-guide.jpg">
    <img src="/assets/img/fundamentals-of-software-architecture/connascence-refactor-guide.jpg" alt="">
  </a>
</div>

**locality**
- how proximal modules are to each other in code base
- must consider strength and locality together

**degree**
- the size of its impact -- does it affect a few classes or many?

**guide for using connascence to improve system modularity**
1. Minimize overall connascence by breaking the system into encapsulated elements
2. Minimize any remaining connascence that crosses encapsulation boundaries
3. Maximize the connascence within encapsulation boundaries

_Rule of Degree_: convert strong forms of connascence into weaker forms of connascence
_Rule of Locality_: as the distance between software elements increases, use weaker forms of connascence

<div style="text-align:center">
  <a href="/assets/img/fundamentals-of-software-architecture/connascence-and-coupling.jpg">
    <img src="/assets/img/fundamentals-of-software-architecture/connascence-and-coupling.jpg" alt="">
  </a>
</div>

# Architecture Characteristics
meets three criteria:
- **Specifies a non-domain design consideration** - operational and design criteria for success; how to implement requirements and why choices were made
- **Influences some structural aspect of the design**
- **Is critical or important to application success** - choose the fewest architecture characteristics rather than the most possible

- **explicit** architecture characteristics appear in requirements, where **implicit** ones need to be identified and extracted
- architect able to translate domain concerns to identify the right architectural characteristics
- anti-pattern of creating a _generic architecture_ that tries to solve too much and solves nothing

## Operational Architecture Characteristics

| characteristic     | description                                                                                                                                                                                                              |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Availability       | How long the system will need to be available (if 24/7, steps need to be in place to allow the system to be up and running quickly in case of any failure).                                                              |
| Continuity         |  Disaster recover ability                                                                                                                                                                                                |
| Performance        | Includes stress testing, peak analysis, analysis of the frequency of functions used, capacity required, and response times. Performance acceptance sometimes requires an exercise of its own, taking months to complete. |
| Recoverability     | Business continuity requirements (e.g., in case of a disaster, how quickly is the system required to be online again?). This will affect the backup strategy and requirements for duplicated hardware.                   |
| Reliability/safety | Assess if the system needs to be fail-safe, or if it is mission critical in a way that affects lives. If it fails, will it cost the company large sums of money?                                                         |
| Robustness         | Ability to handle error and boundary conditions while running if the internet connection goes down or if there’s a power outage or hardware failure.                                                                     |
| Scalability        | Ability for the system to perform and operate as the number of users or requests increases.                                                                                                                              |

## Structural Architecture Characteristics

| characteristic        | description                                                                                                                                            |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Configurability       | Ability for the end users to easily change aspects of the software’s configuration (through usable interfaces).                                        |
| Extensibility         | How important it is to plug new pieces of functionality in.                                                                                            |
| Installability        | Ease of system installation on all necessary platforms.                                                                                                |
| Leverageability/reuse | Ability to leverage common components across multiple products.                                                                                        |
| Localization          | Support for multiple languages on entry/query screens in data fields; on reports, multibyte character requirements and units of measure or currencies. |
| Maintainability       | How easy it is to apply changes and enhance the system?                                                                                                |
| Portability           | Does the system need to run on more than one platform? (For example, does the frontend need to run against Oracle as well as SAP DB?                   |
| Supportability        | What level of technical support is needed by the application? What level of logging and other facilities are required to debug errors in the system?   |
| Upgradeability        | Ability to easily/quickly upgrade from a previous version of this application/solution to a newer version on servers and clients.                      |

## Cross-Cutting Architecture Characteristics

| characteristic          | description                                                                                                                                                                                                                            |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Accessibility           | Access to all your users, including those with disabilities like colorblindness or hearing loss.                                                                                                                                       |
| Archivability           | Will the data need to be archived or deleted after a period of time? (For example, customer accounts are to be deleted after three months or marked as obsolete and archived to a secondary database for future access.)               |
| Authentication          | Security requirements to ensure users are who they say they are.                                                                                                                                                                       |
| Authorization           | Security requirements to ensure users can access only certain functions within the application (by use case, subsystem, webpage, business rule, field level, etc.).                                                                    |
| Legal                   | What legislative constraints is the system operating in (data protection, Sarbanes Oxley, GDPR, etc.)? What reservation rights does the company require? Any regulations regarding the way the application is to be built or deployed? |
| Privacy                 | Ability to hide transactions from internal company employees (encrypted transactions so even DBAs and network architects cannot see them).                                                                                             |
| Security                | Does the data need to be encrypted in the database? Encrypted for network communication between internal systems? What type of authentication needs to be in place for remote user access?                                             |
| Supportability          | What level of technical support is needed by the application? What level of logging and other facilities are required to debug errors in the system?                                                                                   |
| Usability/achievability | Level of training required for users to achieve their goals with the application/solution. Usability requirements need to be treated as seriously as any other architectural issue.                                                    |

# Measuring and Governing Architecture Characteristics
problems with definitions of architectural characteristics:
1. they aren't easily measured or observed
2. definitions vary wildly
3. too composite

need to agree on objective definition of these architecture characteristics

- operational measures, like performance, or request time
- structural measures, like cyclomatic complexity (cyclocamatic complexity = edges - nodes + 2)
- process measures, like testability or deployability

**architecture fitness functions** - any mechanism that provides an objective integrity assessment of some architecture characteristic or combination of architecture characteristics
- cyclic dependencies -- how many modules import other modules; code reviews help, but a fitness function as part of continuous integration is better
- distance from the main sequence -- again, best as fitness function test as part of continuous integration -- metrics tools like JDepend or ArchUnit (Java) NetArchTest (.NET) for fitness testing

## Architectural Quanta
- An independently deployable artifact with high functional cohesion and synchronous connascence
- derived from physics term quantum, which is minimum amount of any physical entity involved in an interaction

**independently deployable** - includes all necessary components to function independently from other parts of the architecture
**high functional cohesion** - how well the contained code is unified -- a quantum does something purposeful
**synchronous connascence** - synchronous calls within an application context or between distributed services that form the quantum

**bounded context** - from domain-driven design -- everything related to the domain is visible internally but opaque to other bounded contexts -- each entity works best within a localized context

# Components
- **component** - the physical manifestation of a module (`jar` in Java, `dll` in .NET, `gem` in ruby, etc)
- Components form the fundamental modular building block in architecture, making them a critical consideration for architects -- top-level partitioning is important concern
- component is often the lowest level of a software system an architect interacts with directly (outside of code quality metrics)

## Partitioning
- domain partitioning - breaking the architecture into domains or workflows
- technical partitioning - breaking the architecture into technical capabilities (presentation, business rules, services, etc)

<div style="text-align:center">
  <a href="/assets/img/fundamentals-of-software-architecture/top-level-partitioning.jpg">
    <img src="/assets/img/fundamentals-of-software-architecture/top-level-partitioning.jpg" alt="">
  </a>
</div>

**Architecture Exposition Cycle**
1. *identify initial components* - what partitioning to use, what components, etc.
2. *assign requirements to components* - align to see how well they fit
3. *analyze roles and responsibilities* - allows architect to align component and domain granularity
4. *analyze architecture characteristics* - think about how these characteristics impact component division and granularity
5. *restructure components* - based on feedback, continuously iterate with developers

Identifying Components
- **actor/actions** - architects identify actors who perform activities with the application and the actions those actors may perform
- **event storming** - assuming the project uses messages and/or events to communicate components, the team tries to determine which events occur in the system based on requirements and identified roles, and build components around those events and message handlers
- **workflow approach** - The workflow approach models the components around workflows, much like event storming, but without the explicit constraints of building a message-based system; a workflow approach identifies the key roles, determines the kinds of workflows these roles engage in, and builds components around the identified activities.

**entity trap anti-pattern** - take each entity and create a `Manager` for it -- this isn't an architecture, it's an object-relational mapping (ORM) of a framework of a database; should just use an off-the-shelf solution like Naked Objects in .NET or Isis in Java to create simple front-ends on databases

# Architecture Styles
## Fundamental Patterns
### Big Ball of Mud
- absence of any discernible architecture structure
- from a [1997 paper](http://www.cin.ufpe.br/~sugarloafplop/mud.pdf) by Brian Foote and Joseph Yoder

### Unitary Architecture
- all architecture on the same machine
- few exist outside of embedded systems and constrained environments

### Client/Server
- separates technical functionality between front-end and backend
- also known as two-tier
- database server + desktop
- browser + web server
- also three-tier architecture, which separates back-end database from an application tier and a front-end tier for presentation (typically in HTML or JS

## Distributed Computing

### Fallacies of Distributed Computing
{: .no_toc }

- set of [assertions](https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing) by Peter Deutsch at Sun Microsystems in the 90s

1. the network is reliable
2. latency is zero
3. bandwith is infinite
4. the network is secure
5. the topology never changes
6. there is only one administrator
7. transport cost is zero
8. the network is homogenous

### Other Distributed Computing Concerns
{: .no_toc }
1. **distributed logging** - consolidating logs is important and difficult; many off-the-shelf solutions exist
2. **distributed transactions** - single-node solutions can rely on transactions and ACID properties, but distributed systems need other ways to propagate data and fail gracefully; things like transactional sagas, BASE considerations, compensating transactions, etc., are made to help this
3. **contract maintenance and versioning** - a contract is behavior and data that is agreed upon by both the client and service

## Layered Architecture Style
- most common architecture styles, technically partitioned
- can build effective roles and responsibility models within architecture because concerns are separated
- aka _n-tiered_
- components are organized into logical horizontal layers, each layer performing a specific role within the application

<div style="text-align:center">
  <a href="/assets/img/fundamentals-of-software-architecture/layered-topology.jpg">
    <img src="/assets/img/fundamentals-of-software-architecture/layered-topology.jpg" alt="">
  </a>
</div>

- each layer can either be _closed_ or _open_
  - _closed_ means that as request moves top-down through layers, it can't skip any layer
  - _open_ means it can
  - **fast lane reader pattern** - request might go directly to database to serve simple requests
- open or closed is important for _isolation of concerns_
  - change in one layer shouldn't affect others if contracts between remain the same
  - also allows layers to be replaced (e.g., replacing presentation running angular with react)
- **architecture sinkhole anti-pattern** - requests move from layer to layer as simple pass-through processing with no business logic, meaning layered might not be correct architecture style

### Pros and Cons
{: .no_toc }
- good for small, simple applications or web-sites
- good as a starting point, for situations with tight budget and time constraints
- very low cost because of simplicity and familiarity
- as system grows, maintainability, agility, testability, and deployability suffer

<div style="text-align:center">
  <a href="/assets/img/fundamentals-of-software-architecture/layered-ratings.jpg">
    <img src="/assets/img/fundamentals-of-software-architecture/layered-ratings.jpg" alt="">
  </a>
</div>

- Overall cost and simplicity are the primary strengths of the layered architecture style
- Deployability rates low due to the ceremony of deployment (effort to deploy), high risk, and lack of frequent deployments
- Elasticity and scalability rate very low primarily due to monolithic deployments and the lack of architectural modularity.
- does not lend itself to high-performance systems due to the lack of parallel processing, closed layering, and the sinkhole architecture anti-pattern.
- doesn't support fault tolerance due to monolithic deployments and lack of architectural modularity

## Pipeline Architecture Style

<div style="text-align:center">
  <a href="/assets/img/fundamentals-of-software-architecture/pipeline-topology.jpg">
    <img src="/assets/img/fundamentals-of-software-architecture/pipeline-topology.jpg" alt="">
  </a>
</div>

- technically partitioned, usually implemented as a monolith
- **pipes** form the communication channel between filters; typically unidirectional and point-to-point (rather than broadcast)
- **filters** are self-contained, independent from other filters, and generally stateless and perform one task only
  - *producer*: starting point in a process, outbound only, aka *source*
  - *transformer*: accepts input, potentially performs transformation, and forwards onward, aka *map*
  - *tester*: accepts input, tests one or more criteria, aka *reduce*
  - *consumer*: termination point for pipeline, and might persist final result

### Pros and Cons
{: .no_toc }

<div style="text-align:center">
  <a href="/assets/img/fundamentals-of-software-architecture/pipeline-ratings.jpg">
    <img src="/assets/img/fundamentals-of-software-architecture/pipeline-ratings.jpg" alt="">
  </a>
</div>

- Overall cost and simplicity combined with modularity are the primary strengths
- Deployability and testability, while only around average, rate slightly higher than the layered architecture due to the level of modularity achieved through filters
- reliability medium due to the lack of network traffic, bandwidth, and latency found in most distributed architectures
- elasticity and scalability low due to monolith
- doesn't support fault tolerance

## Microkernel Architecture Style
- aka the plug-in architecture
- consists of a _core system_ and _plug-in components_
- app logic divided between the two
- can be technically partitioned or domain partitioned within core system

<div style="text-align:center">
  <a href="/assets/img/fundamentals-of-software-architecture/microkernel-topology.jpg">
    <img src="/assets/img/fundamentals-of-software-architecture/microkernel-topology.jpg" alt="">
  </a>
</div>

**core system**
- minimum functionality to run the system, or happy path (general processing flow) through the application
- might have a monolithic presentation layer, either embedded within the core system or as a layer on top

**plug-in component**
- standalone, independent components that contain specialized processing, additional features, and custom code meant to extend or enhance the core system
- can also be used to isolate highly volatile code
- components should have no dependencies between them (other than core system)
- runtime plug-ins can be managed through frameworks without needing to redeploy system (Open Service Gateway Initiative, Penrose, Jigsaw (Java) or Prism (.NET))
- don't always need to use point-to-point communication -- can use REST or messaging to provide more decoupling
  - this creates better scalability and throughput and allows more runtime changes
  - makes it a distributed architecture
- not common for plug-in components to connect to centrally shared database (for decoupling purposes), each component has its own data store

**registry**
- contains information about each plug-in module, including things like name, data contract, and remote access protocol details
- can be internal, or external such as ZooKeeper or Consul

**contracts**
- contracts between plug-in components and core system are usually standard across domain
- include behavior, input data, and output data returned from plug-in

- IDEs, Jenkins, Jira, Confluence are a good example of this architecture

**domain/architecture isomorphism** - architecture tends to follow domain and team makeup (Conway's law)

### Pros and Cons
{: .no_toc }

<div style="text-align:center">
  <a href="/assets/img/fundamentals-of-software-architecture/microkernel-ratings.jpg">
    <img src="/assets/img/fundamentals-of-software-architecture/microkernel-ratings.jpg" alt="">
  </a>
</div>

- simplicity and overall cost are main strength
- testability, deployability, and reliability rate average because functionality can be isolated to independent plug-ins
- modularity and extensibility mean additional functionality can be added or removed
- performance rates decent because these apps tend to be small and don't grow as large as layered architecture

## Service-Based Architecture Style
- hybrid of microservices, typically 4-12 services
- domain-partitioned architecture
- distributed macro layered structure, separately deployed user interface, separately deployed remote coarse-grained services, and a monolithic database
- REST typically used to access services, but messaging, remote procedure calls, or even SOAP can be used
- use [service locator pattern](https://en.wikipedia.org/wiki/Service_locator_pattern) with registry in UI to discover services
- can have single UI, multiple domain based UIs, or service-based UIs
- can have monolithic database, or domain-scoped databases, or service-based databases
- good practice to also have API layer (as reverse proxy or gateway) when there are cross-cutting concerns, such as metrics, security, etc.

<div style="text-align:center">
  <a href="/assets/img/fundamentals-of-software-architecture/service-based-topology.jpg">
    <img src="/assets/img/fundamentals-of-software-architecture/service-based-topology.jpg" alt="">
  </a>
</div>

### Database Partitioning
{: .no_toc }
- single monolithic database might present issues when schema needs to change, as all services need to be updated then
- can create a shared library of entity objects, but isn't typically effective although shared library versioning helps -- still need to pull in new shared libraries on change
- better to logically partition database and manifest logical partitioning through federated shared libraries

### Pros and Cons
{: .no_toc }

<div style="text-align:center">
  <a href="/assets/img/fundamentals-of-software-architecture/service-based-ratings.jpg">
    <img src="/assets/img/fundamentals-of-software-architecture/service-based-ratings.jpg" alt="">
  </a>
</div>

- faster change (agility)
- better test coverage
- more frequent deployments and less risk
- high fault tolerance and availability
- tends to be simpler and cheaper than microservices, as well as more reliable than other distributed services
- a natural fit when doing domain-driven design -- very pragmatic architecture
- as services become more fine-grained, require orchestration/choreography
- **orchestration**: the coordination of multiple services through the use of a separate mediator service that controls and manages the workflow of the transaction (like a conductor in an orchestra)
- **choreography**: the coordination of multiple services by which each service talks to one another without the use of a central mediator

## Event-Driven Architecture Style
- distributed, async architecture
- domain partitioned
- most apps follow _request-based_ model, where requests made to system are sent to a _request orchestrator_, who directs to _request processors_
- contrast _request-based_ with _event-based_, where a particular situation occurs and action is taken based on that event
- **async communication** - relies on it for both fire-and-forget and request/reply processing
- **error handling** - can use the workflow event pattern of reactive architecture, where if an error occurs, it is immediately sent to a workflow processor that tries to fix the error and resend the message, or logs it to a centralized location where an operator can view it
- **broadcast** - can send message out without knowledge of who is receiving and what they do with it
- **request/reply** - a way of achieving synchronous communication -- typically achieved via a _correlation id_ so event producers can communicate backwards

<div style="text-align:center">
  <a href="/assets/img/fundamentals-of-software-architecture/event-topology.png">
    <img src="/assets/img/fundamentals-of-software-architecture/event-topology.png" alt="">
  </a>
</div>

### Broker Topology
{: .no_toc }
- useful when you need a degree of responsiveness and dynamic control over processing event
- since events are broadcast without a central mediator, you can add additional event processors easily, leading to extensibility

1. **initiating event** - initial event that starts the flow
2. **event broker** - channel where events are sent and **event processors** pick up processing
3. **event processor** - accepts events from **event broker** and performs specific task with event
4. **processing event** - after event is processed, the processor async advertises its actions

<div style="text-align:center">
  <a href="/assets/img/fundamentals-of-software-architecture/broker-topology.jpg">
    <img src="/assets/img/fundamentals-of-software-architecture/broker-topology.jpg" alt="">
  </a>
</div>

- performance, responsiveness, and scalability are strengths
- with no control over overall workflow, things like error handling are more difficult, and recoverability to restart a business transaction is difficult

| pros                              | cons                 |
|-----------------------------------|----------------------|
| Highly decoupled event processors | Workflow control     |
| High scalability                  | Error handling       |
| High responsiveness               | Recoverability       |
| High performance                  | Restart capabilities |
| High fault tolerance              | Data inconsistency   |

### Mediator Topology
{: .no_toc }
- tries to address problems of broker topology
- important to know types of events that will be processed through mediator so you can use different mediators for different types of events

1. **initiating event**
2. **event queue**
3. **event mediator**
4. **event channels**
5. **event processors**

<div style="text-align:center">
  <a href="/assets/img/fundamentals-of-software-architecture/mediator-topology.jpg">
    <img src="/assets/img/fundamentals-of-software-architecture/mediator-topology.jpg" alt="">
  </a>
</div>

- very difficult to declaratively model dynamic processing in complex event flow
- mediator must scale, potentially leading to bottleneck
- event processors aren't as highly decoupled

| pros                    | cons                              |
|-------------------------|-----------------------------------|
| workflow control        | more coupling of event processors |
| error handling          | lower scalability                 |
| recoverability          | lower performance                 |
| restart capabilities    | lower fault tolerance             |
| better data consistency | modeling complex workflows        |

### Preventing Data Loss
{: .no_toc }
- message getting dropped or never making it to final destination
- **synchronous send** - does a blocking wait on message producer until broker acknowledges message has been persisted
- **guaranteed delivery** - message broker stores message in memory and in physical data store in case of server going down
- **client acknowledge mode** - keeps message in queue and attaches client ID so no other consumer can read the message
- **last participant support** - removes message from persisted queue by acknowledging processing has been completed and message has been persisted

### Pros and Cons
{: .no_toc }
<div style="text-align:center">
  <a href="/assets/img/fundamentals-of-software-architecture/event-ratings.jpg">
    <img src="/assets/img/fundamentals-of-software-architecture/event-ratings.jpg" alt="">
  </a>
</div>

- great for performance, scalability, and fault tolerance, and highly evolutionary
- simplicity and testability are more difficult

## Space-Based Architecture
- specifically designed to address high scalability, elasticity, and concurrency
- gets its name from concept of tuple space, the technique of using multiple parallel processors communicating through shared memory
- remove database and replace with replicated in-memory grids
- data is async'd to database, usually via messaging with persistent queues

<div style="text-align:center">
  <a href="/assets/img/fundamentals-of-software-architecture/space-based-topology.jpg">
    <img src="/assets/img/fundamentals-of-software-architecture/space-based-topology.jpg" alt="">
  </a>
</div>

**processing unit**
- contains application code
- contains in-memory data grid and replication engine (implemented through things like Hazelcast, Apache Ignite, and Oracle Coherence)

**virtualized middleware**
- used to manage and coordinate the processing units
- made up of
  - **messaging grid** - handles input request and session state
  - **data grid** - most often implemented as a replicated cache
  - **processing grid** - optional component that handles orchestrated request processing when there are multiple processing units involved in single business request
  - **deployment manager** - manages dynamic startup and shutdown of processing units based on load

**data pumps**
- async send updated data to another processor and to the database
- usually implemented via messaging

**data writers**
- perform updates from the data pumps

**data readers**
- read database data and deliver it to processing units upon startup
- only invoked when
    1. crash of all processing units of the same named cache
    2. redeployment of all processing units with same named cache
    3. retrieving archive data not contained in the replicated cache

### Data Collisions
{: .no_toc }
- in a replicated cache in active/active state where updates can occur to any cache, data collisions are possible
- **data collision** - when data is updated in once cache instance (cache A) and during replication to another cache (cache B), the same data is updated by that cache (cache B)
- equation for collision rate:

<div style="text-align:center">
  <a href="/assets/img/fundamentals-of-software-architecture/collision-rate.png">
    <img src="/assets/img/fundamentals-of-software-architecture/collision-rate.png" alt="">
  </a>
</div>

Update rate (UR): 20 updates/second
Number of instances (N): 5
Cache size (S): 50,000 rows
Replication latency (RL): 100 milliseconds
Updates: 72,000 per hour
Collision rate: 14.4 per hour
Percentage: 0.02%

- **near cache** - caching hybrid that bridges in-memory data grids with a distributed cache
- distributed cache called the **full backing cache** carries all the data
- each processing unit has a most frequently used (mfu) or most recently used (mru) **front cache**
- performance is highly variable because front caches hold different data

<div style="text-align:center">
  <a href="/assets/img/fundamentals-of-software-architecture/space-based-ratings.jpg">
    <img src="/assets/img/fundamentals-of-software-architecture/space-based-ratings.jpg" alt="">
  </a>
</div>

- maximizes elasticity, scalability, and performance
- testing, however, is extremely difficult -- performance testing at scale isn't realistic
- also can be costly

## Orchestration-Driven Service-Oriented Architecture
- this is sort of an historical relic
- driving philosophy is centered around enterprise-level reuse

<div style="text-align:center">
  <a href="/assets/img/fundamentals-of-software-architecture/service-oriented-orchestration-topology.jpg">
    <img src="/assets/img/fundamentals-of-software-architecture/service-oriented-orchestration-topology.jpg" alt="">
  </a>
</div>

**business services** - sit at top and provide entry point
**enterprise services** - contain fine-grained, shared implementations; building blocks that make up coarse-grained business services
**application services** - one-off, single-implementation services
**infrastructure services** - supply operational concerns, such as monitoring, logging, authentication
**orchestration engine** - forms the heart of this distributed architecture, stitching together the business service implementations

- all requests go through orchestration engine
- ultimate danger was the extreme technical partitioning -- domain concepts end up spread exceptionally thin

<div style="text-align:center">
  <a href="/assets/img/fundamentals-of-software-architecture/service-oriented-orchestration-ratings.jpg">
    <img src="/assets/img/fundamentals-of-software-architecture/service-oriented-orchestration-ratings.jpg" alt="">
  </a>
</div>

- doesn't really do anything well

## Microservices Architecture
- built out of domain-driven design
- primary goal is high decoupling, physically modeling the logical notion of bounded context
- distributed architecture -- each service runs its own process either on a physical computer or virtual machine or container
- performance is a negative side effect, as network calls take longer than method calls, security verification at endpoints adds processing time
- determining granularity key to success

<div style="text-align:center">
  <a href="/assets/img/fundamentals-of-software-architecture/microservice-topology.jpg">
    <img src="/assets/img/fundamentals-of-software-architecture/microservice-topology.jpg" alt="">
  </a>
</div>

**bounded context**
- driving philosophy
- each service models a domain or workflow, and each service includes everything necessary to operate within the application
- granularity can be determined by
  - purpose - functional cohesion
  - transactions - what needs to cooperate in a transaction
  - choreography - if services require extensive communication to function, you can bundle to limit communication overhead

**data isolation**
- avoid coupling of schemas and databases as integration points
- need to abandon the idea of a single source of truth

**API layer**
- should not be used as a mediator or orchestration tool

**operational reuse**
- can use the sidecar pattern to handle all operational concerns that teams benefit from coupling together
- if you need to update all monitoring, for example, you can upgrade sidecar and then anyone using it can benefit from upgrade
- if each service requires a common sidecar, can build a **service mesh** to allow unified control across arch for things like logging and monitoring

**frontends**
- original idea had user interfaces as part of microservice, but this isn't practical (there might be concerns like common styling, deployment patterns, extra complexity)
- **monolithic user interface** - single user interface that calls through the API layer to satisfy requests
- **microfrontends** - components at the user interface level to create a synchronous level of granularity and isolation (frameworks like React)

**communication**
- must decide on sync or async communication
- typically use protocol-aware heterogenous interoperability
  - _protocol-aware_ - need to know which protocol to use (REST, SOAP, message queues, etc)
  - _heterogenous_ - fully supports polyglot environments
  - _interoperability_ - services can call each other to send and receive data
- for async communication, need events and messages

**choreography and orchestration**
- should look at _Domain/architecture isomorphism_ (how well the architecture fits the domain) when assessing how appropriate an architecture style is for a particular problem
- can use the _front controller_ pattern, where a nominally choreographed service becomes a more complex mediator

**transactions and sagas**
- building transactions across service boundaries violates the core decoupling principle
- **compensating transaction framework** - if a transaction across multiple services fails, some mediator needs to reverse the transaction on other services
  - requires significant complexity, creates lots of coordination traffic

<div style="text-align:center">
  <a href="/assets/img/fundamentals-of-software-architecture/microservice-ratings.jpg">
    <img src="/assets/img/fundamentals-of-software-architecture/microservice-ratings.jpg" alt="">
  </a>
</div>

# Architecture Decisions
- **the domain** - need to have a good understanding of domain
- **architecture characteristics that impact structure**
- **data architecture** - architects and DBAs must collaborate on database, schema, and other data concerns
- **organizational factors** - external factors such as cloud vendor cost
- **domain/architecture isomorphism** - does the problem domain match the topology of the architecture
- **monolith vs. distributed**
- **where does the data live**
- **async or synchronous**

- **backends for frontends pattern** - make the API layer a thin microkernel adaptor, supplying general info from backend, and translates to suitable format for frontend

**architecturally significant**: those decisions that affect
- structure: decisions that impact patterns or styles
- nonfunctional characteristics: architecture characteristics (-ilities)
- dependencies: coupling points between components and/or services
- interfaces: how services are accessed or orchestrated
- construction techniques: platforms, frameworks, tools, or processes

## Decision Anti-Patterns
**covering your assets**
- architect avoids making an architecture decision out of fear of making the wrong choice
- two ways to overcome:
    1. wait until the last responsible moment to make a decision
    2. collaborate with dev team to ensure that the decision you make can be implemented as expected

**groundhog day**
- people don't know what decision is made, so it keeps getting discussed over and over again
- when justifying architecture decisions, need to provide technical and business justifications
- most basic business justifications: cost, time to market, user satisfaction, and strategic positioning

**email-driven architecture**
- when people lose, forget, or don't even know an architecture decision has been made and can't implement
- first rule of communicating architecture decisions: don't include in the body of an email
- second rule: only notify those who care about the decision

## Architecture Decision Records
**Title**: Name
**Status**: Proposed, Accepted, Superseded
**Context**: what situation is forcing me to make this decision?
**Decision**: using affirmative language like "we will", what has been decided; more emphasis on the why than the how
**Consequences**: very important, details tradeoffs
**Compliance**: how the decision will be measured and governed
**Notes**: includes various metadata about ADR

## Assessing Risk
- risk matrix: classify risk as high, medium, or low

<div style="text-align:center">
  <a href="/assets/img/fundamentals-of-software-architecture/risk-matrix.jpg">
    <img src="/assets/img/fundamentals-of-software-architecture/risk-matrix.jpg" alt="">
  </a>
</div>

**Risk Storming**
- collaborative exercise used to determine architectural risk within a specific dimension
- Identification: each particpant individually identifying areas of risk within arch
- Consensus: highly collaborative with the goal of gaining consensus among all participants
- Mitigation: identifying changes or enhancements to certain areas

## Presenting Architecture
**Representational consistency** is the practice of always showing the relationship between parts of an architecture, either in diagrams or presentations, before changing views
**irrational artifact attachment** - relationship between a person's irrational attachment to some artifact and how long it took to produce

any diagramming tool needs:
- layers
- stencils/templates
- magnets

diagramming standards
- **UML** - unified model language -- mostly used for class and sequence diagrams to show structure and workflow
- **C4**
  - Context: entire context of system, include roles of users and external dependencies
  - Container: the physical (and logical) deployment boundaries and containers
  - Component: component view, mostly neatly aligns with architect's view
  - Class: UML class diagrams
- **Archimate**
  - Arch(itecture)(ani)mate
  - lightweight technical standard from the Open Group

presentations
- important to be able to use powerpoint and keynote as presentation tools
- key power of a presentation is ability to manipulate time, to allow ideas to play out over several slides
- avoid **bullet-riddled corpse** anti-pattern, where a slide is just the speaker's notes
- while speaking, presenter has two info channels: visual and verbal -- overwhelming one stops all fixation on the other
- **infodecks** - slide decks not meant to be projected but to summarize info graphically

# Assessment Questions
## Chapter 1: Introduction
{: .no_toc }
1. What are the four dimensions that define software architecture?
2. What is the difference between an architecture decision and a design principle?
3. List the eight core expectations of a software architect.
4. What is the First Law of Software Architecture?

## Chapter 2: Architectural Thinking
{: .no_toc }
1. Describe the traditional approach of architecture versus development and explain why that approach no longer works.
2. List the three levels of knowledge in the knowledge triangle and provide an example of each.
3. Why is it more important for an architect to focus on technical breadth rather than technical depth?
4. What are some of the ways of maintaining your technical depth and remaining hands-on as an architect?

## Chapter 3: Modularity
{: .no_toc }
1. What is meant by the term connascence?
2. What is the difference between static and dynamic connascence?
3. What does connascence of type mean? Is it static or dynamic connascence?
4. What is the strongest form of connascence?
5. What is the weakest form of connascence?
6. Which is preferred within a code base—static or dynamic connascence?

## Chapter 4: Architecture Characteristics Defined
{: .no_toc }
1. What three criteria must an attribute meet to be considered an architecture characteristic?
2. What is the difference between an implicit characteristic and an explicit one? Provide an example of each.
3. Provide an example of an operational characteristic.
4. Provide an example of a structural characteristic.
5. Provide an example of a cross-cutting characteristic.
6. Which architecture characteristic is more important to strive for—availability or performance?

## Chapter 5: Identifying Architecture Characteristics
{: .no_toc }
1.  Give a reason why it is a good practice to limit the number of characteristics (“-ilities”) an architecture should support.
2. True or false: most architecture characteristics come from business requirements and user stories.
3. If a business stakeholder states that time-to-market (i.e., getting new features and bug fixes pushed out to users as fast as possible) is the most important business concern, which architecture characteristics would the architecture need to support?
4. What is the difference between scalability and elasticity?
5. You find out that your company is about to undergo several major acquisitions to significantly increase its customer base. Which architectural characteristics should you be worried about?

## Chapter 6: Measuring and Governing Architecture Characteristics
{: .no_toc }
1. Why is cyclomatic complexity such an important metric to analyze for architecture?
2. What is an architecture fitness function? How can they be used to analyze an architecture?
3. Provide an example of an architecture fitness function to measure the scalability of an architecture.
4. What is the most important criteria for an architecture characteristic to allow architects and developers to create fitness functions?

## Chapter 7: Scope of Architecture Characteristics
{: .no_toc }
1. What is an architectural quantum, and why is it important to architecture?
2. Assume a system consisting of a single user interface with four independently deployed services, each containing its own separate database. Would this system have a single quantum or four quanta? Why?
3. Assume a system with an administration portion managing static reference data (such as the product catalog, and warehouse information) and a customer-facing portion managing the placement of orders. How many quanta should this system be and why? If you envision multiple quanta, could the admin quantum and customer-facing quantum share a database? If so, in which quantum would the database need to reside?

## Chapter 8: Component-Based Thinking
{: .no_toc }
1. We define the term component as a building block of an application—something the application does. A component usually consist of a group of classes or source files. How are components typically manifested within an application or service?
2. What is the difference between technical partitioning and domain partitioning? Provide an example of each.
3. What is the advantage of domain partitioning?
4. Under what circumstances would technical partitioning be a better choice over domain partitioning?
5. What is the entity trap? Why is it not a good approach for component identification?
6. When might you choose the workflow approach over the Actor/Actions approach when identifying core components?

## Chapter 9: Architecture Styles
{: .no_toc }
1. List the eight fallacies of distributed computing.
2. Name three challenges that distributed architectures have that monolithic architectures don’t.
3. What is stamp coupling?
4. What are some ways of addressing stamp coupling?

## Chapter 10: Layered Architecture Style
{: .no_toc }
1. What is the difference between an open layer and a closed layer?
2. Describe the layers of isolation concept and what the benefits are of this concept.
3. What is the architecture sinkhole anti-pattern?
4. What are some of the main architecture characteristics that would drive you to use a layered architecture?
5. Why isn’t testability well supported in the layered architecture style?
6. Why isn’t agility well supported in the layered architecture style?

## Chapter 11: Pipeline Architecture
{: .no_toc }
1. Can pipes be bidirectional in a pipeline architecture?
2. Name the four types of filters and their purpose.
3. Can a filter send data out through multiple pipes?
4. Is the pipeline architecture style technically partitioned or domain partitioned?
5. In what way does the pipeline architecture support modularity?
6. Provide two examples of the pipeline architecture style.

## Chapter 12: Microkernel Architecture
{: .no_toc }
1. What is another name for the microkernel architecture style?
2. Under what situations is it OK for plug-in components to be dependent on other plug-in components?
3. What are some of the tools and frameworks that can be used to manage plug-ins?
4. What would you do if you had a third-party plug-in that didn’t conform to the standard plug-in contract in the core system?
5. Provide two examples of the microkernel architecture style.
6. Is the microkernel architecture style technically partitioned or domain partitioned?
7. Why is the microkernel architecture always a single architecture quantum?
8. What is domain/architecture isomorphism?

## Chapter 13: Service-Based Architecture
{: .no_toc }
1. How many services are there in a typical service-based architecture?
2. Do you have to break apart a database in service-based architecture?
3. Under what circumstances might you want to break apart a database?
4. What technique can you use to manage database changes within a service-based architecture?
5. Do domain services require a container (such as Docker) to run?
6. Which architecture characteristics are well supported by the service-based architecture style?
7. Why isn’t elasticity well supported in a service-based architecture?
8. How can you increase the number of architecture quanta in a service-based architecture?

## Chapter 14: Event-Driven Architecture Style
{: .no_toc }
1. What are the primary differences between the broker and mediator topologies?
2. For better workflow control, would you use the mediator or broker topology?
3. Does the broker topology usually leverage a publish-and-subscribe model with topics or a point-to-point model with queues?
4. Name two primary advantage of asynchronous communications.
5. Give an example of a typical request within the request-based model.
6. Give an example of a typical request in an event-based model.
7. What is the difference between an initiating event and a processing event in event-driven architecture?
8. What are some of the techniques for preventing data loss when sending and receiving messages from a queue?
9. What are three main driving architecture characteristics for using event-driven architecture?
10. What are some of the architecture characteristics that are not well supported in event-driven architecture?

## Chapter 15: Space-Based Architecture
{: .no_toc }
1. Where does space-based architecture get its name from?
2. What is a primary aspect of space-based architecture that differentiates it from other architecture styles?
3. Name the four components that make up the virtualized middleware within a space-based architecture.
4. What is the role of the messaging grid?
5. What is the role of a data writer in space-based architecture?
6. Under what conditions would a service need to access data through the data reader?
7. Does a small cache size increase or decrease the chances for a data collision?
8. What is the difference between a replicated cache and a distributed cache? Which one is typically used in space-based architecture?
9. List three of the most strongly supported architecture characteristics in space-based architecture.
10. Why does testability rate so low for space-based architecture?

## Chapter 16: Orchestration-Driven Service-Oriented Architecture
{: .no_toc }
1. What was the main driving force behind service-oriented architecture?
2. What are the four primary service types within a service-oriented architecture?
3. List some of the factors that led to the downfall of service-oriented architecture.
4. Is service-oriented architecture technically partitioned or domain partitioned?
5. How is domain reuse addressed in SOA? How is operational reuse addressed?

## Chapter 17: Microservices Architecture
{: .no_toc }
1. Why is the bounded context concept so critical for microservices architecture?
2. What are three ways of determining if you have the right level of granularity in a microservice?
3. What functionality might be contained within a sidecar?
4. What is the difference between orchestration and choreography? Which does microservices support? Is one communication style easier in microservices?
5. What is a saga in microservices?
6. Why are agility, testability, and deployability so well supported in microservices?
7. What are two reasons performance is usually an issue in microservices?
8. Is microservices a domain-partitioned architecture or a technically partitioned one?
9. Describe a topology where a microservices ecosystem might be only a single quantum.
10. How was domain reuse addressed in microservices? How was operational reuse addressed?

## Chapter 18: Choosing the Appropriate Architecture Style
{: .no_toc }
1. In what way does the data architecture (structure of the logical and physical data models) influence the choice of architecture style?
2. How does it influence your choice of architecture style to use?
3. Delineate the steps an architect uses to determine style of architecture, data partitioning, and communication styles.
4. What factor leads an architect toward a distributed architecture?

## Chapter 19: Architecture Decisions
{: .no_toc }
1. What is the covering your assets anti-pattern?
2. What are some techniques for avoiding the email-driven architecture anti-pattern?
3. What are the five factors Michael Nygard defines for identifying something as architecturally significant?
4. What are the five basic sections of an architecture decision record?
5. In which section of an ADR do you typically add the justification for an architecture decision?
6. Assuming you don’t need a separate Alternatives section, in which section of an ADR would you list the alternatives to your proposed solution?
7. What are three basic criteria in which you would mark the status of an ADR as Proposed?

## Chapter 20: Analyzing Architecture Risk
{: .no_toc }
1. What are the two dimensions of the risk assessment matrix?
2. What are some ways to show direction of particular risk within a risk assessment? Can you think of other ways to indicate whether risk is getting better or worse?
3. Why is it necessary for risk storming to be a collaborative exercise?
4. Why is it necessary for the identification activity within risk storming to be an individual activity and not a collaborative one?
5. What would you do if three participants identified risk as high (6) for a particular area of the architecture, but another participant identified it as only medium (3)?
6. What risk rating (1-9) would you assign to unproven or unknown technologies?

## Chapter 21: Diagramming and Presenting Architecture
{: .no_toc }
1. What is irrational artifact attachment, and why is it significant with respect to documenting and diagramming architecture?
2. What do the 4 C’s refer to in the C4 modeling technique?
3. When diagramming architecture, what do dotted lines between components mean?
4. What is the bullet-riddled corpse anti-pattern? How can you avoid this anti-pattern when creating presentations?
5. What are the two primary information channels a presenter has when giving apresentation?

## Chapter 22: Making Teams Effective
{: .no_toc }
1. What are three types of architecture personalities? What type of boundary does each personality create?
2. What are the five factors that go into determining the level of control you should exhibit on the team?
3. What are three warning signs you can look at to determine if your team is getting
too big?
4. List three basic checklists that would be good for a development team.

## Chapter 23: Negotiation and Leadership Skills
{: .no_toc }
1. Why is negotiation so important as an architect?
2. Name some negotiation techniques when a business stakeholder insists on five nines of availability, but only three nines are really needed.
3. What can you derive from a business stakeholder telling you “I needed it yesterday”?
4. Why is it important to save a discussion about time and cost for last in a negotiation?
5. What is the divide-and-conquer rule? How can it be applied when negotiating architecture characteristics with a business stakeholder? Provide an example.
6. List the 4 C’s of architecture.
7. Explain why it is important for an architect to be both pragmatic and visionary.
8. What are some techniques for managing and reducing the number of meetings you are invited to?

## Chapter 24: Developing a Career Path
{: .no_toc }
1. What is the 20-minute rule, and when is it best to apply it?
2. What are the four rings in the ThoughtWorks technology radar, and what do they mean? How can they be applied to your radar?
3. Describe the difference between depth and breadth of knowledge as it applies to software architects. Which should architects aspire to maximize?
