# Clean Architecture
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
1. TOC
{:toc}
</details>

## Chapter 1: What is Design and Architecture?
Traditionally, architecture seems to imply high level details, while design is low-level structures and details, but little details support high-level details-- it's all part of the same whole of the system.

**The goal of software architecture is to minimize the human resources required to build and maintain the required system.**

The measure of design quality is measure of effort required to meet needs of customer.

Developers tell themselves two lies:
1. "We can clean it up later; we just have to get to market first" -- never clean it up because market is always moving
2. writing messy code is faster than clean code -- it never is

"The only way to go fast is to go well".

### Summary
Avoid overconfidence and take software design seriously.

In order to take software design seriously, you need to know what good design and architecture is -- you need to know attributes of a system that minimizes effort and maximizes productivity.

## Chapter 2: A Tale of Two Values
Every software system provides two different values to stakeholders:

**Behavior**
- the way a system behaves, written in a functional specification or requirements document then written in code
- when system doesn't behave the way it is supposed to, programmers then debug

**Architecture**
- software of a system, subject to change
- difficulty in making a change should be proportional to the scope of the change, not shape
- new requirements roughly fit the same scope, but they often no longer fit the shape of the system and thus are increasingly difficult
- architectures should be as shape-agnostic as practical

Is a system working (behavior) or the ease of change (architecture) more important? If a program is impossible to change, it will become useless, but if it is easy to change, it can be made useful.

**Eisenhower's Matrix**

|---|---|
| important & urgent | important & NOT urgent |
| NOT important & urgent | NOT important & NOT urgent |

- _behavior_ is urgent but not always particularly important
- _architecture_ is important but never particularly urgent

Business managers are not equipped to evaluate the importance of architecture, so it is responsibility of software dev team to assert importance of architecture over urgency of features.

## Chapter 3: Paradigm Overview

### Structured Programming
{: .no_toc }
- discovered by Edsger Wybe Dijkstra in 1968
- `goto` statements harmful to program structure, replace with `if/then/else` and `do/while/until` constructs
- _"Structured programming imposes discipline on the direct transfer of control"_

### Object-Oriented Programming
{: .no_toc }
- discovered by Ole Johan Dahl and Kristen Nygaard in 1966
- _"Object-oriented programming imposes discipline on the indirect transfer of control"_

### Functional Programming
{: .no_toc }
- discovered before computers by Alonzo Church who in 1936 invented $$ \lambda$$-calculus (lambda calculus)
- typically no assignment statements
- _"Functional programming imposes discipline on assignment"_

Patterns typically _take_ something away and are negative in intent, meaning there likely isn't anything else to take away and there won't be any other paradigms. All three were invented before 1968 and there's been nothing since.

### Summary
- we use polypmorphism to cross architectural boundaries
- we use functional programming to impose discipline on the location of and access to data
- we use structured programming as the algorithmic foundation of our modules

## Chapter 4: Structured Programming
