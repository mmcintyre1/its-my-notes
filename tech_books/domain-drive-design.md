---
last_modified_date: "2021-08-11 19:40:54.029576"
nav_order: 1
---
# Domain Driven Design: Tackling Complexity in the Heart of Software
{: .no_toc }
Eric Evans, 2003

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
1. TOC
{:toc}
</details>

## Ubiquitous Language
- a common language that is more robust than lowest common denominator
- made up of names of classes, prominent operations
- supplemented with terms from high-level organizing principles and names of patterns identified by team
- should be used to describe not just _artifacts_ but _tasks_ and _functionality_
- when language is fractured between technical members and subject matter experts (speaking two different nomenclatures), project faces serious problems
  - translation is required between the two, and this blunts communication and requires significant knowledge crunching
- holds all the parts together
- should be a dynamic and evolving language based on **knowledge crunching**
- _If sophisticated domain experts don't understand the model, there is something wrong with the model_

### Knowledge Crunching
- take a torrent of info and probe for relevant trickly
- continuously try one organizing principle after another until one fits
- process of distillation -- move away from waterfall where all knowledge defined up front (knowledge trickles in one direction but never accumulates)
- without input from domain experts, knowledge is anemic and naive
- _When we set out to write software, we never know enough_
- all projects leak knowledge, so hard-earned knowledge needs to be expressed in a usable (and durable) form to protect against when the oral tradition is interrupted (and knowledge is lost)

### Modelling Documents and Diagrams
- _the model is not the diagram_ -- the diagrams and documents purpose is to help communicate and explain the model
- UML documents miss two important things 1) the meaning of the objects it represents & 2) what the objects are meant to do
- using UML as an implementation language is missing the point, because you will still need something to communicate the uncluttered model (the model isn't just the code)
- greatest value of a design document is to:
  1. explain the concepts of the model
  2. help navigate the detail of the code
  3. give insight into the model's intended style of use

<div style="text-align:center">
  <a href="/assets/img/ddd-diagram.svg">
    <img src="/assets/img/ddd-diagram.svg" alt="ddd-diagram">
  </a>
</div>

## Model-Driven Design
- tightly relating the code to an underlying model gives the code meaning and makes the model relevant
- need to relate the design to the domain model -- key is not to divide analysis and design as two separate models -- they both serve to create and refine the same model
- one approach:
  - design portion of software to reflect the domain model so mapping is obvious, then build upon that
- code is an expression of the model, and changes to the code require changes to the model
- this sort of development really only makes sense for object-oriented programming (based on modelling paradigm) where you can slavishly tie model to implementation
- revealing the model to the user (e.g., bookmarks as files rather than obscuring the model via abstraction) gives the user more access to the potential of the software and yields consistent, predictable behavior
- need _hands-on modellers_ -- people who write code should feel responsible to update model. needs to be that feedback

## Modelling Building Blocks
### Layered Architecture

<div style="text-align:center">
  <a href="/assets/img/ddd-layered.png">
    <img src="/assets/img/ddd-layered.png" alt="ddd-layered-architecture">
  </a>
</div>

- business logic and UI and infra can become intertwined, making changes to anything (for example, an update to a widget in the UI) require large changes and be difficult to reason about
- essential principle is that any element of a layer depends only on other elements in the same layer or on elements of the layers "beneath" it, and communication upwards must pass through some indirect method
- need to partition complex program into layers
- each layer is cohesive and depends only on layers below
- then, concentrate all code that pertaints to domain model and isolate from the UI, application, and infrastructure code
- domain objects can then worry solely about expressing the domain model, which allows a model to evolve and be rich and clear enough to capture essential business knowledge
- also important to judiciously apply frameworks, as they can be heavyweight and obscure the domain model

### Smart UI (Anti-Pattern)
- sometimes, a simple project doesn't require all the overhead of domain-driven design, which is costly, takes a while to onboard new team members, time consuming, etc.
- can use the Smart UI pattern (which is an anti-pattern generally)
  - put all business logic into the user interface
  - chop application into small functions and implement as separate user interfaces
  - automate as much of the UI building as possible
- downsides are: 1) integrations are difficult (except through the db), 2) no reuse of behavior or abstractions 3) rapid prototyping and iteration eventually reach a natural limit 4) complexity buries you quickly

### Entities (Reference Objects)
- an object defined by its identity, not just its attributes
- has continuity through a lifecycle and distinctions independent of attributes that are important to the app's user
- need to keep a means of distinguishing each object via its *identity* that is guaranteed to return **unique** result to that object and be **immutable**
- most basic responsibility of an **ENTITY** is to establish continuity so that behavior can be clear and predictable

### Value Objects
- an object that represents a descriptive aspect of the domain with no conceptual identiy
- objects that describe things
- transient, immutable pieces of data without identity, but could give information about an **ENTITY**
- e.g., a `Customer` could be an **ENTITY** but that `Customer`'s name is a **VALUE OBJECT**
- if a value object must be shared between objects, it must be immutable. otherwise, it _should not_ be shared

### Services
- an operation that is offered as an interface that stands alone in the model, without encapsulating state
- tends to be named for an activity, a verb, not a noun
- a **SERVICE** should still have a defined responsibility
- a good **SERVICE** has three characteristics:
  1. the operation relates to a domain concept that is not a natural part of an **ENTITY** or **VALUE OBJECT**
  2. the interface is defined in terms of other elements of the domain model
  3. the operation is stateless
- most **SERVICES** are purely technical and belong in infra layer

### Modules (Packages)
- cognitive overload is the primary motivation for modularity
- low coupling (decreases cost of understanding modules place) between modules and high cohesion (reduces scale of complexity within single module to manageable) within them
- give **MODULES** names that become part of the **UBIQUITOUS LANGUAGE**
- **MODULES** also tend to follow distribution model (e.g., code that is intended to run on the same server can be part of the same **MODULE**)


**Life cycle of a Domain Object**
<div style="text-align:center">
  <a href="/assets/img/ddd-lifecycle-of-domain-object.svg">
    <img src="/assets/img/ddd-lifecycle-of-domain-object.svg" alt="lifecycle-of-domain-object">
  </a>
</div>

### Aggregates
- a cluster of associated objects that we treat as a unit for the purpose of data changes
- the root of an aggregate is the only member of the **AGGREGATE** that outside objects are allowed to hold references to
- it is difficult to guarantee consistency of changes to objects in a model with complex associations
- invariants need to be maintained that apply to closely related groups of objects, not just discrete objects
- cautious locking schemes cause multiple useers to interfere pointlessly with each other to make the system almost unusable

<div style="text-align:center">
  <a href="/assets/img/ddd-aggregate.svg">
    <img src="/assets/img/ddd-aggregate.svg" alt="aggregate">
  </a>
</div>

- cluster **ENTITIES** and **VALUE OBJECTS** into **AGGREGATES** and define boundaries around each
- choose one **ENTITY** to be root, and control access for everything inside via the root (external objects can only hold reference to the root)
- transient references to internal members can be passed out only for single operation
- because root controls access, it will be aware of changes to internals
- you can then enforce invariants for anything within the **AGGREGATE**

### Factories
- instantiating objects can be ungainly, and when client needs to do it itself, it breaches encapsulation and overly couples the client to the implementation of the created object
- encapsulates knowledge required to create a complex object or **AGGREGATE**
- shift responsibility for creating objects to a separate object that might have no responsibility itself in the domain
- create a **FACTORY** to build something whose details you want to hide
- that said, sometimes a simple constructor is all you need (e.g., client cares about implementation like in the **STRATEGY** pattern)
- key parts of **FACTORY**: each operation is atomic, and the **FACTORY** will be coupled to its arguments
- can also use **FACTORY** to reconstitute objects -- need to make sure tracking ID is the same, and any invariant violation is handled appropriately

### Repositories
- client needs a way to acquire references to pre-existing domain objects
- **REPOSITORY** provides a global access method to domain objects (querying, persisting, updating, etc.) -- delegate all storage and access
- without **REPOSITORY** pattern, devs might take shortcuts e.g., direct database queries, which, while faster, break encapsulation and sprawl logic
- _reconstitution_ - restoring instance from stored data
- Evans recommends 1) abstracting type, 2) taking advantage of decoupling data access from the client, and 3) leave transaction control to the client
- **REPOSITORY** similar to **FACTORY** -- the former finds old objects, the latter makes new objects
- Evans also recommends against "find or create" functionality because usually the distinction between new object and existing object is important in the domain, and a framework that transparently combines them might muddy the waters

## Supple Design
### Intention-Revealing Interfaces
### Standalone Classes
### Conceptual Contours
### Assertions
### Side-Effect-Free Functions

## Context
### Bounded Context
### Context Map
### Continuous Integration

## Distillation
### Core Domain
### Domain Vision Statement
### Generic Subdomains
### Declarative Style
### Segregated Core

## Large-Scale Structures
### Evolving Order
### System Metaphor
### Responsibility Layers
### Knowledge Level
### Pluggable Component Framework

## Six Essentials for Strategic Design Decision Making (492)
