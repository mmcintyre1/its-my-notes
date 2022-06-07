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

## 6: The Life Cycle of a Domain Object
![Life Cycle of a Domain Object](assets/ddd-lifecycle-of-domain-object.svg)

### Aggregates
- a cluster of associated objects that we treat as a unit for the purpose of data changes
- the root of an aggregate is the only member of the **AGGREGATE** that outside objects are allowed to hold references to
- it is difficult to guarantee consistency of changes to objects in a model with complex associations
- invariants need to be maintained that apply to closely related groups of objects, not just discrete objects
- cautious locking schemes cause multiple useers to interfere pointlessly with each other to make the system almost unusable

![Aggregate](assets/ddd-aggregate.svg)

- cluster **ENTITIES** and **VALUE OBJECTS** into **AGGREGATES** and define boundaries around each
- choose one **ENTITY** to be root, and control access for everything inside via the root (external objects can only hold reference to the root)
- transient references to internal members can be passed out only for single operation
- because root controls access, it will be aware of changes to internals
- you can then enforce invariants for anything within the **AGGREGATE**

### Factories

### Repositories