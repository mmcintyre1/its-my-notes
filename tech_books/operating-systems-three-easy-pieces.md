---
last_modified_date: "2022-02-22 12:24:15.090424"
nav_order: 2
---
# Operating Systems: Three Easy Pieces
{: .no_toc }
Remzi Arpaci-Dusseau, Andrea Arpaci-Dusseau. 2015

## Key Links
- https://pages.cs.wisc.edu/~remzi/OSTEP/Homework/homework.html
- https://pages.cs.wisc.edu/~remzi/OSTEP/
- https://github.com/remzi-arpacidusseau/ostep-code


<details open markdown="block">
  <summary>
    Table of contents
  </summary>
1. TOC
{:toc}
</details>

## Introduction
### Von Neumann computing
{: .no_toc }
a processor:
- fetches an instruction from memory
- decodes it
- executes it
- moves on to next instruction

### Virtualization
{: .no_toc }
- make a system easy to ease
- **virtualization**: taking a physical resource and transforming it into a more easy to use virtual form; a method OS's use to achieve ease of use
- OS can be thought of as resource manager
- can virtualize CPU (each program appears to have access to its own CPU) or memory (each program has it's own private virtual address space)

### Concurrency
{: .no_toc }
- **concurrency** - working on many things at once
- can lead to interesting problems when instructions are executing one at a time

### Persistence
{: .no_toc }
- storing data in volatile memory (e.g., RAM) leads to data loss if system stops
- **persistence** - storing data in a longer term storage, such as HDD, SSD, CDs (any I/O device)

### OS Design Goals
{: .no_toc }
- make the system easy to use through abstractions
- make the system performant by minimizing the OS overheads
- provide protection between applications
- ensure a high degree of reliability for the OS
- other goals: energy-efficiency, security, and mobility

## Processes
- a process is a running program
- in order to run multiple processes at once, the OS creates the illusion of multiple CPUs by virtualizing the CPU
- achieves this by:
  - _mechanisms_ - low level methods or protocols that implement a needed piece of functionality
- _policiies_ - algorithms for making some kind of decision within the OS

types of sharing:
- _time sharing_ - allowing one entity to use a resource for a little while then context switching to allow another entity to use the resource (e.g., CPU, network link)
- _space sharing_ - a resource is divided in space among users (e.g., disk space)

- understanding process is understanding machine state
  - memory - where programs instructions live via address space
  - registers - things like program counter/instruction pointer (what the next instruction is)
  - I/O info

### Process API
{: .no_toc }
- **create** - method to create new processes
- **destroy** - method to destroy running processes
- **wait** - method to pause a running process
- **misc. control** - other special methods, like suspend or resume
- **status** - get status info about process

how are programs turned into processes?
1. code and any static data loaded into memory
   1. this used to be done eagerly (load the whole program into memory), now it is typically done lazily (load only needed modules)
2. stack is provisioned
   1. in C programs, stack is used for variables, function parameters, etc
3. program might also allocate memory for program's heap
   1. in C programs, memory for heap gets provisioned with `malloc()` and freed with `free()`
4. OS will do other initialization tasks such as setting up file descriptors (standard out, standard in, standard err)

process states
RUNNING - the process is using the CPU right now
READY   - the process could be using the CPU right now
          but (alas) some other process is
WAITING - the process is waiting on I/O
          (e.g., it issued a request to a disk)
DONE    - the process is finished executing
ZOMBIE  - the process has completed executing but there is still an entry in the process table

- usually in unix systems processes return 0 for success, non-zero otherwise