---
last_modified_date: "2022-02-22 12:24:15.090424"
nav_order: 1
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

## Virtualization
### Processes
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

### Key Process API Terms
{: .no_toc }
- Each process has a name; in most systems, that name is a number known as a **process ID**  (PID).
- The `fork()` system call is used in UNIX systems to create a new process. The creator is called the parent; the newly created process is called the child.
- The `wait()` system call allows a parent to wait for its child to complete execution.
- The `exec()` family of system calls allows a child to break free from its similarity to its parent and execute an entirely new program.
- A UNIX shell commonly uses `fork()`, `wait()`, and `exec()` to launch user commands; the separation of fork and exec enables features like input/output redirection, pipes, and other cool features, all without changing anything about the programs being run.
- Process control is available in the form of signals, which can cause jobs to stop, continue, or even terminate.
- Which processes can be controlled by a particular person is encapsulated in the notion of a user; the operating system allows multiple users onto the system, and ensures users can only control their own processes.
- A superuser can control all processes (and indeed do many other things); this role should be assumed infrequently and with caution for security reasons.

### Limited Direct Execution
- in order to run programs as fast as possible, OS developers run them directly on the CPU (direct execution)
- this requires time sharing of the resource (limited)

#### Restricted Operations
{: .no_toc }
_how do you perform restricted operations like I/O without giving process full control over the system?_

- The CPU should support at least two modes of execution: a restricted **user mode** and a privileged (non-restricted) **kernel mode**.
- Typical user applications run in user mode, and use a **system call** to trap into the kernel to request operating system services.
- The trap instruction saves register state carefully, changes the hardware status to kernel mode, and jumps into the OS to a pre-specified destination: the **trap table**.
- When the OS finishes servicing a system call, it returns to the user program via another special **return-from-trap** instruction, which reduces privilege and returns control to the instruction after the trap that jumped into the OS.
- The trap tables must be set up by the OS at boot time, and make sure that they cannot be readily modified by user programs. All of this is part of the limited direct execution protocol which runs programs efficiently but without loss of OS control.

#### Switching Between Processes
{: .no_toc }
_how can the OS regain control of the CPU so that it can switch processes?_

two approaches to giving OS control back:
- cooperative approach, where OS waits for system calls from processes to regain control
- non-cooperative approach, where something like an _interrupt timer_ is implemented (via hardware) that periodically gives control back to the CPU

- Sometimes the OS, during a timer interrupt or system call, might wish to switch from running the current process to a different one, a low-level technique known as a **context switch**

### CPU Scheduling
- scheduling is higher level policy for _when_ to apply lower level mechanism (e.g., context switching) when virtualizing resources
- in order to compare different scheduling policies, need metrics to compare

#### Key Metrics
- **turnaround time**
  - time in which a job completes minus the time a job arrives
  - $ T_{turnaround} = T_{completion} - T_{arrival} $
- **fairness**
  - the equality with which jobs are treated
  - one example is Jain's Fairness Index
  - often at odds with performance, as most fair way to run jobs isn't often the most performant
- **response time**
  - time when a job arrives to when it's first scheduled
  - optimizations for turnaround time might not be helpful for response time
  - $ T_{response} = T_{firstrun} - T_{arrival} $
- **overlap**
  - when dealing with I/O (or any blocking task), it is good to kick off the blocking task then switch, or to overlap executions

#### First In, First Out Queue
- simplest algo for scheduling -- job that arrives is first to be processed
- suffers from **convoy effect** -- large, expensive job blocks small, fast jobs
- normally only works when all jobs run in same amount of time

#### Shortest Job First (SJF)
- jobs are organized based on job length at arrival
- if not all jobs arrive at same time, you need to add **preemption** (like an interrupt for new arrivals), called **Shortest Time-to-Completion First** (STCF)
- most modern schedulers are preemptive

#### Round Robin
{: .no_toc }
- instead of running job to completion, jobs are run for a _time slice_ (aka scheduling quantum)
- need to _amortize_ cost (spread cost out over long term) of context switching, so you don't want to switch context too often or wait too long so as to remove all benefits of round robin algo
- round robin is more fair and like any policy that is fair will perform more poorly on turnaround time -- can run shorter jobs to completion if you are willing to be unfair, which might affect response time

#### Multi-Level Feedback Queue (MLFQ)
- for most jobs, we won't know length of jobs, so 1) how do we optimize for turnaround time, and 2) how do we make a system feel responsive for interactive users?
- multi-level feedback queue has multiple levels of queues, and uses feedback to determine priority of given job
-  instead of demanding _a priori_ knowledge of the nature of a job, it observes the execution of a job and prioritizes it accordingly.
-  manages to achieve the best of both worlds: it can deliver excellent overall performance (similar to SJF/STCF) for short-running interactive jobs, and is fair and makes progress for long-running CPU-intensive workloads
- many systems, including BSD UNIX derivatives, Solaris, and Windows NT and subsequent Windows operating systems use a form of MLFQ as their base scheduler
- some schedulers allow you to give **advice** to help set priority (can be used or ignored) - e.g., linux tool `nice`
- other schedulers use a **decay-usage** algorithm to adjust priorities (instead of a table or exact rules below)

general rules outlined:
- **Rule 1:** If Priority(A) > Priority(B), A runs (B doesn’t).
- **Rule 2:** If Priority(A) == Priority(B), A & B run in round-robin fashion using the time slice (quantum length) of the given queue.
- **Rule 3:** When a job enters the system, it is placed at the highest priority (the topmost queue).
- **Rule 4:** Once a job uses up its time allotment at a given level (regardless of how many times it has given up the CPU), its priority is reduced (i.e., it moves down one queue).
- **Rule 5:** After some time periodS, move all the jobs in the system to the topmost queue.

### Multiprocessor Scheduling
flashcards:

- What is the difference between hardware caches and main memory?
- Caches hold copiers of popular data and the main memory holds all the data, but access to the main memory is slower

- {{c1::temporal locality}} is when a piece of data is accessed, it is likely to be accessed again in the near future
- {{c1::spatial locality}} is when a program access data at address _x_ it is likely to access data items near _x_ as well

- cache coherence
- bus snooping
- invalidate or update a cache