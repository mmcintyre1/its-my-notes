---
last_modified_date: "2021-08-11 19:40:54.029576"
parent: Tech Books
nav_exclude: true
nav_order: 3
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
  <a href="/assets/img/domain-driven-design/diagram.svg">
    <img src="/assets/img/domain-driven-design/diagram.svg" alt="ddd-diagram">
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
  <a href="/assets/img/domain-driven-design/layered.png">
    <img src="/assets/img/domain-driven-design/layered.png" alt="ddd-layered-architecture">
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
  <a href="/assets/img/domain-driven-design/lifecycle-of-domain-object.svg">
    <img src="/assets/img/domain-driven-design/lifecycle-of-domain-object.svg" alt="lifecycle-of-domain-object">
  </a>
</div>

### Aggregates
- a cluster of associated objects that we treat as a unit for the purpose of data changes
- the root of an aggregate is the only member of the **AGGREGATE** that outside objects are allowed to hold references to
- it is difficult to guarantee consistency of changes to objects in a model with complex associations
- invariants need to be maintained that apply to closely related groups of objects, not just discrete objects
- cautious locking schemes cause multiple useers to interfere pointlessly with each other to make the system almost unusable

<div style="text-align:center">
  <a href="/assets/img/domain-driven-design/aggregate.svg">
    <img src="/assets/img/domain-driven-design/aggregate.svg" alt="aggregate">
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

<div style="text-align:center">
  <a href="/assets/img/domain-driven-design/supple-design.jpg">
    <img src="/assets/img/domain-driven-design/supple-design.jpg" alt="supple-design">
  </a>
</div>

### Intention-Revealing Interfaces
- if you need to be aware of implementation of component to use it, you lose value of encapsulation
- name classes and operations to describe effect and purpose without means to which they do what they promise
- names should conform to **ubiquitous language**
- use test-driven development by writing test for behavior before implementing

### Side-Effect-Free Functions
- **side effect** - any change in the state of the system that will affect future operations
- **command** - method that result in modification to observable state
- need to limit so developers can make changes without needing to understand full cascading effects
- place logic of program into functions that return results with no observable side effects
- segregate commands into simple operations that do not return domain information

### Assertions
- can be used to state post-conditions of operations and invariants of class **AGGREGATES**
- most OO languages don't directly support, but good unit tests can make up gap

### Conceptual Contours
- without boundaries between elements of a model, functionality gets duplicated, and meaning is hard to understand
- conversely, too fine-grained of boundaries make objects lose all meaning (half a uranium atom isn't uranium)
- decompose design elements into cohesive units
- observe _axes of change_ to identify **CONCEPTUAL CONTOURS**

### Standalone Classes
- adding dependencies to a module increases difficulties in understanding drastically
- implicit is much more difficult than explicit concepts
- _low coupling is fundamental to object design_
- if you can, eliminate all other concepts from the class, so it can be studied and understood alone

**Closure of Operations** (p 268)
**Domain-Specific Languages** (p 272)

> Generating a running program from a declaration of model properties is a kind of Holy Grail of MODEL-DRIVEN DESIGN (271)

- **Strategy (AKA Policy)** (p 311)
- **Composite** (p 315)

## Context
### Bounded Context
- always multiple models on any large project, but when you combine code from distinct models, things are buggy and hard to understand
- need to explicitly define context within which a model applies
- boundaries defined via --> teams organization, usage within parts of app, physical manifestations (code bases, database schemas, infra)
- delimits applicability of particular model so there is a clear and shared understanding of what has to be consistent
- *bounded contexts are not modules*
- _duplicate concepts_ - two model elements that represent the same thing
- _false cognates_ - the same term applied to two different things (similar to polysemes)

### Continuous Integration
- general tendency for a model to fragment, to lose valuable coherency and integration
- all work within context is being merged and made consistent frequently enough that splinters are caught and corrected quickly
- for code, requires:
  - step-by-step, reproducible merge/build technique
  - automated test suites
  - rules that set some reasonably small upper limit on lifetime of unintegrated changes
- for conceptual integration, requires:
  - constant exercise of the ubiquitous language

### Context Map
- the act of defining each model in a project's **BOUNDED CONTEXT**,
- including points of contact between models and any explicit translation between models or shared info
- after you make context map, you might see changes to org of teams or design you want to change
- important to test points of contact between bounded contexts
-
### Relationships Between Bounded Contexts

<div style="text-align:center">
  <a href="/assets/img/domain-driven-design/context-relations.jpg">
    <img src="/assets/img/domain-driven-design/context-relations.jpg" alt="relationship between contexts">
  </a>
</div>

#### Shared Kernel

<div style="text-align:center">
  <a href="/assets/img/domain-driven-design/shared-kernel.jpg">
    <img src="/assets/img/domain-driven-design/shared-kernel.jpg" alt="shared kernel">
  </a>
</div>

- subset of domain two teams agree to share
- useful for when teams are moving quickly and don't want to spend time on translation or integration of models

#### Customer/Supplier Dev Teams
- establish clear customer/supplier relationship between teams, where downstream plays customer
- jointly develop automated acceptances tests as part of upstreams continuous integration, freeing them to make changes that won't affect downstream team
- customer's needs are paramount

#### Conformist
- when two models are incompatible, downstream can choose to adopt upstream, esp. if code quality is decent and compatibility relatively high already
- simplifies integration, but prevents downstream from designing and innovating on their domain

#### Anti-Corruption Layer
- when two systems absolutely can't integrate, you can create an isolating layer between the two
- ADAPTER or FACADE pattern, essentially

#### Separate Ways
- integration is always expensive and sometimes benefit is small
- you can declare a bounded context to have no connection with others at all

#### Open Host Service
- when a subsystem needs many integrations, design a protocol
- anyone can use, and expand and extend to handle new requirements

#### Published Language
- use a well-documented shared language that can express necessary domain language (e.g., XML and DTD)

## Distillation
- the process of separating the components of a mixture to extract the essence in a form that makes it more valuable and useful, e.g., a model is a distillation of knowledge

<div style="text-align:center">
  <a href="/assets/img/domain-driven-design/distillation.jpg">
    <img src="/assets/img/domain-driven-design/distillation.jpg" alt="distillation">
  </a>
</div>

### Core Domain
- a system that is hard to understand is hard to change
- not all parts of design are refined equally, and priorities need to be set
- need to boil model down, make the **CORE DOMAIN** small, bringing most valuable and specialized concepts into sharp relief
- also need to apply top talent -- investment in non-CORE needs to be justified
- **CORE DOMAIN** is what you do in house

### Generic Subdomains
- some parts of model add complexity without specialized knowledge, muddying the **CORE DOMAIN**
- need to identify cohesive subdomains that are not motivation for project, and factor out these to separate modules
- consider buying off-shelf, don't put best devs on these -- little domain knowledge to be gained

**Off-the-Shelf Solution**
pros:
- less code, less maintenance, code is mature
cons:
- still need to evaluate and understand
- might be over-engineered
- might be difficult to integrate

**Published Design or Model**
pros:
- more mature than homegrown and reflects many people's insight
- instant, high-quality docs
cons:
- might not quite fit needs or is over-engineered

**Outsourced Implementation**
pros:
- keeps core team free
- can do dev without permanently enlarging team
- forces interface-oriented design
cons:
- still requires time
- significant overhead in transferring ownership back
- code quality can vary

**In-House Implementation**
pros:
- easy integration
- get what you want and nothing extra
- temporary contractors can be assigned
cons:
- ongoing maintenance and training
- easy to underestimate time and cost of developing packages

### Domain Vision Statement
- short description (one page) of **CORE DOMAIN** and value it will bring
- write early and revise as you go
- gives team shared direction

### Highlighted Core
- write a distillation document that describes the **CORE** domain and primary interactions among **CORE** elements
- useful as a process tool

### Cohesive Mechanisms
- encapsulate mechanisms into separate light framework
- frees the model to talk about the what and delegate the how to the cohesive mechanisms
- motivated by same desire as generic subdomain, to unburden the **CORE DOMAIN**
- a model proposes, a mechanism disposes

### Segregated Core
- similar to generic subdomains, but from the other direction
- MM Note: not sure I understand the difference between segregated core and generic subdomain? These all seem pedantic distinctions to remove extraneous chaff from the core

### Declarative Style
- declare!

## Large-Scale Structures

<div style="text-align:center">
  <a href="/assets/img/domain-driven-design/large-scale.jpg">
    <img src="/assets/img/domain-driven-design/large-scale.jpg" alt="large scale structures">
  </a>
</div>

### Evolving Order
- need to find balance between design free-for-alls and too much design up front, which takes power out of the hands of the developer
- have your structures evolve with the application -- don't overconstrain
- ill-fitting structure is worse than none
- _less is more_

### System Metaphor
- a loose easily understood large-scale structure that is harmonious with the object paradigm
- however, a persuasive metaphor introduces risk that design will take on aspects of the metaphor that were not desirable
- need to continuously re-assess metaphor, and drop if necessary -- there to serve communication and understanding

### Responsibility Layers
- give coherence to model by assigning responsibilities to larger segments of structures
- organize along axes of change, make sure that domain object, aggregate, and module fit neatly within on layer
- responsibilities should tell a story of the high-level purpose and design of system
- some good layers based on:
  - storytelling
  - conceptual dependency
  - conceptual contours
- example:

<div style="text-align:center">
  <a href="/assets/img/domain-driven-design/con-layer.jpg">
    <img src="/assets/img/domain-driven-design/con-layer.jpg" alt="conceptual layers example">
  </a>
</div>

### Knowledge Level
- a group of objects that describe how another group of objects should behave
- used to describe and constrain the structure and behavior of the basic model

### Pluggable Component Framework
- distill abstract core of interfaces and interactions and build framework that allows diverse implementations of those interfaces to be freely substituted

Three basic principles of strategic design:
1. context
2. distillation
3. large-scale structures

<div style="text-align:center">
  <a href="/assets/img/domain-driven-design/all-together.jpg">
    <img src="/assets/img/domain-driven-design/all-together.jpg" alt="bringing it all together">
  </a>
</div>

## Six Essentials for Strategic Design Decision Making (492)
1. decisions must reach the entire team
2. the decision process must absorb feedback
3. the plan must allow for evolution
4. architecture teams must not siphon off all the best and brightest
5. strategic design requires minimalism and humility
6. objects are specialists; developers are generalists