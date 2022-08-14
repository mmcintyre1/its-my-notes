---
last_modified_date: 2022-08-13 12:00:00 -0500
nav_order: 1
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

## Defining Software Architecture

1. **the structure of the system**
  - refers to the type of architecture style (or styles) the system is implemented in (such as microservices, layered, or microkernel)
2. **architecture characteristics**
  - The architecture characteristics define the success criteria of a system, which is generally orthogonal to the functionality of the system
3. **architecture decisions**
  - define the rules for how a system should be constructed
4. **design principles**
  - A design principle differs from an architecture decision in that a design principle is a guideline rather than a hard-and-fast rule

## Expectations of an Architect
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
- **architectural fittness functions**: an objective integrity assessment of some architectural characteristic(s)

## Laws of Software Architecture
1. Everything in software architecture is a trade-off
   1. If an architect thinks they have discovered something that isn’t a trade-off, more likely they just haven’t identified the trade-off yet
2. _Why_ is more important than _how_

## Thinking Like an Architect
1. understand the difference between architecture and design, and understand how to collaborate with dev teams to make architecture work
2. have a wide breadth of technical knowledge while still maintaining a certain level of technical depth -- see solutions and possibilities others do not
  - breadth is more important than depth
  - **frozen caveman anti-pattern** -- someone who always reverts back to their pet irrational concern for every architecture
3. understanding, analyzing, and reconciling trade-offs between various solutions and technologies
4. understanding the importance of business drivers and how they translate to architectural concerns

## Modularity
**modularity** - a logical grouping of related code, which could be a group of classes in an object-oriented language or functions in a structured or functional language, e.g., `package` in Java, `namespace` in .NET

### Cohesion
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

### Coupling
**afferent coupling** - measures the number of _incoming_ connections to a code artifact (component, class, function, etc)

**efferent coupling** - measures number of _outgoing_ connections to a code artifact

**abstractness** - ratio of abstract artifacts (abstract classes, interfaces, etc) to concrete artifacts (implementation)

**instability** - ratio of efferent coupling to the sum of both efferent and afferent coupling -- determines volatility of code base; an unstable codebase breaks more easily when changed

**distance from the main sequence**
$ D = \|A + I - 1\| $
- A = abstractness and I = instability

<div style="text-align:center">
  <a href="/assets/img/fundamentals-of-software-architecture/distance-from-main-sequence.jpg">
    <img src="/assets/img/fundamentals-of-software-architecture/distance-from-main-sequence.jpg" alt="">
  </a>
</div>

### Connascence
Two components are **connascent** if a change in one would require the other to be modified in order to maintain the overall correctness of the system -- recasting efferent and afferent coupling for object-oriented language (those measures of coupling predate OOP)

#### Static Connascence
{: .no_toc }
- source-code-level coupling

**Connascence of Name (CoN)**
Multiple components must agree on the name of an entity.

**Connascence of Type (CoT)**
Multiple components must agree on the type of an entity.

**Connascence of Meaning (CoM) or Connascence of Convention (CoC)**
Multiple components must agree on the meaning of particular values.

**Connascence of Position (CoP)**
Multiple components must agree on the order of values.

**Connascence of Algorithm (CoA)**
Multiple components must agree on a particular algorithm.


#### Dynamic Connascence
{: .no_toc }
- calls executed at runtime