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
{: .no_toc }
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
- discovered before computers by Alonzo Church who in 1936 invented $ \lambda$-calculus (lambda calculus)
- typically no assignment statements
- _"Functional programming imposes discipline on assignment"_

Patterns typically _take_ something away and are negative in intent, meaning there likely isn't anything else to take away and there won't be any other paradigms. All three were invented before 1968 and there's been nothing since.

### Summary
{: .no_toc }
- we use polypmorphism to cross architectural boundaries
- we use functional programming to impose discipline on the location of and access to data
- we use structured programming as the algorithmic foundation of our modules

## Chapter 4: Structured Programming
Dijkstra saw that programming was hard, and the cognitive load was too high to keep all details in mind at once. His answer was to use the mathematical discipline of _proof_, or the idea of using composable elements to create programs.

The use of `goto` prevented a program from being able to be decomposed recursively, and that good uses of `goto` really corresponded to `if/then/else` or `do/while` control structures.

All programs can be built from three elements: _sequence_, _selection_, and _iteration_.

Eventually, `goto` was phased out, and we are all 'structured' programmers in the sense that languages don't give us the option to use undisciplined direct transfer of control.

Proofs ended up being too difficult, but the scientific method replaced proofs. The central idea is that things are _falsifiable_ but not provable, as in, you can only prove something is false rather than proving it is true.

Dijkstra: "Testing shows the presence, not the absence, of bugs".

Structured programming allows us to decompose a program into small provable functions that are falsifiable, i.e., testable.

### Summary
{: .no_toc }
Ability to create falsifiable units of programming that makes structured programming valuable today, and the reason unrestrained `goto`s aren't used.

Functional decomposition is great practice.

Software is like a science, from low to high level, and is driven by falsifiability. Architects define modules, components, and services that are easily testable (falsifiable), using restrictive disciplines.

## Chapter 5: Object-Oriented Programming
What is OOP? Some say "combo of data and function", but that implies that `o.f()` is different from `f(o)` , which is absurd. Others say it is a way to model real world, but this is too loose and evasive.

Many say it is attributes of _polymorphism_, _encapsulation_, and _inheritance_.

### Encapsulation
{: .no_toc }
Being able to draw a cohesive line around data and functions, seen as private data members and public functions of a class.

Perfect encapsulation exists in C, a non-OO language. Data structures and functions would be declared in header files and implementation files would take care of the details, and users didn't have access to implementation files. Once OO was introduced with C++, you lost perfect encapsulation.

Introducing `public`, `private`, and `protected` keywords a way to regain encapsulation, but this is a hack. **Many OO languages have little or no encapsulation.**

### Inheritance
{: .no_toc }
Inheritance is simply the redeclaration of a group of variables and functions within an enclosing scope.

OO languages allow for easier inheritance that isn't a workaround, as well as multiple inheritance, but this functionality exists in non-OO languages

### Polymorphism
{: .no_toc }
Giving a single interface to entities of different types (think, file interface in Unix)

```c
struct FILE {
  void (*open) (char* name, int mode);
  void (*close) ();
  int (*read) ();
  void (*write) (char) ;
  void (*seek) (long index, int mode);
}
```

Polymorphism is an application of pointers to functions, which have been in use for a long time. OO allowed this to be much safer, however, as pointers to functions are _dangerous_, relying on manual conventions. OO eliminates these conventions.

Unix chose to make IO devices plugins (polymorphism allows things to becomes plugins to the source code) because _device independent_ programs are more adaptable. For example, punch cards to magnetic tape. Most OS's implement this device independence.

### Dependency Inversion
{: .no_toc }
In typical calling tree, high level functions call mid level functions, which call low level functions, etc. The caller was forced to mention the name of the module that contained the callee, meaning that the flow of control was dictated by the behavior of the system.

```plantuml!
allow_mixing

interface interface {
+F()
}

class ML1 {
+F()
}

component HL1

HL1 -r-> interface
ML1 -u-|> interface
HL1 .d.> ML1
```
