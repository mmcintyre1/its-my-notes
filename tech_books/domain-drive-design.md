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
- holds all the parts together

<div style="text-align:center">
  <a href="/assets/img/ddd-diagram.svg">
    <img src="/assets/img/ddd-diagram.svg" alt="ddd-diagram">
  </a>
</div>

## Model-Driven Design

## Modelling Building Blocks

### Layered Architecture

### Smart UI (Anti-Pattern)

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

### Repositories

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
