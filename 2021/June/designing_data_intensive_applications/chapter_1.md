
# Chapter 1: Reliable, Scalable, and Maintainable Applications

### Data Systems
We can group data components (databases, caches, queues, etc.) under the umbrella of data systems instead of as separate components because
	1. many new systems have emerged that blur the typical line (Kafka, Redis)
	2. many use cases are covered by stitching together data components with application code

## Three concerns for software systems
1. *Reliability*
	- The system should continue to work correctly even in the face of adversity
2. *Scalability*
	- As the system grows, there should be reasonable ways of dealing with growth
3. *Maintainability*
	- Over time, many different people will work on the system, and they should all be able to work on it productively

## Reliability
- Things that can go wrong are called faults, and a system that can withstand them is fault-tolerant or resilient
- fault: component of system deviates from spec
- failure: where a failure is a when the system stops providing the required service to a user
- we generally prefer tolerating faults over preventing faults

### Types of Faults

#### Hardware Faults
- e.g. hard disks crash, RAM becomes faulty, etc
	- hard disks have a mean time to failure (MTTF) of about 10 to 50 years
	- typically we can add redundancy to a system or individual components
	- move toward system that can tolerate loss of entire machines
#### Software Faults
- systematic error within system
- lots of small things can help: thinking about assumptions and interactions, process isolation, data observation
#### Human Errors
- might be leading cause of errors
- way around:
  - build well-designed abstractions, APIs, and admin interfaces, make it easy to 'do the right thing'
  - fully featured sandbox environments
  - test thoroughly at all levels (unit tests, whole-system integration tests, manual tests)
  - quick and easy recovery
  - detailed and clear monitoring (telemetry)

## Scalability
the term we use to describe a system's ability to cope with increased load

### Describing Load
- load on a system can be described with a few numbers which we call load parameters
- the best choice of load parameters depends on architecture of your system: could be requests/second, or ratio of reads/writes to a database
- fan-out: in transaction processing systems, describes the number of requests to other services that we need to make in order to serve one incoming request

### Describing Performance
- once you know load on a system, you can look at what happens when load increases
- when you increase load parameter:
	- and keep system resources the same, how is performance affected
	- how much do you need to increase resources to keep performance the same
- in batch processing systems (like Hadoop) we care about throughput
- in online systems, we care about response time
- latency: time request is waiting to be handled
- response time: total time a client sees, so time to process (service time), queuing delays, etc
- measuring performance
  - we use arithmetic mean (synonymous with average), or median with percentiles
  - p95, p99, p999 (95%, 99%, 99.9%) to reflect thresholds of percentiles past the median
  - typically used in service level objectives (SLO) and service level agreements (SLA)
- head of line blocking: it only takes a small number of slow responses to hold up the processing of subsequent requests

### Coping with Load
- *scaling up* - vertical scaling, moving to a more powerful machine
- *scaling out* - horizontal scaling, dstributing the load across multiple smaller machines
  - *shared-nothing architecture* - distributing load across multiple machines
- some systems are *elastic* (scaled automatically based on load) while some are scaled manually
- *magic scaling sauce* - the false idea that there is a one size fits all solution to scaling
- an architecture that scales well for a particular application is built around assumption of which operations will be common and which will be rare (load parameters)

## Maintainability
The majority of the cost of software is not in its initial development but ongoing maintenance

### Operability
make it easy for operations teams to keep systems running smoothly

### Simplicity
make it easy for new engineers to understand the system by removing complexity, or avoiding a big ball of mud
- *accidental complexity* - complexity not inherent in the problem space but arises because of the implementation
- an abstraction is a useful technique to hide non-important implementation details behind a façade

### Evolvability
make it easy for engineers to make changes to the system in the future (aka *extensibility*, *modifiability*, or *plasticity*

## Chapter Summary
- an application must meet various requirements to be useful
	- *functional requirements* - what it should do, like allow data to be stored, retrieved, searched
	- *non-functional requirements* - general properties, like reliability, compliance, scalability, maintainability
- **Reliability** means making systems work correctly, even when faults occur. Faults can be in hardware (typically random and uncorrelated), software (bugs are typically systematic and hard to deal with), and human (who inevitability make mistakes from time to time). Fault tolerance techniques can hide certain types of faults from the end user
- **Scalability** means having strategies for keeping performance good, even when load increases. In order to discuss scalability, we first need ways of describing load and performance quantitatively. In scalable systems, you can add processing capacity in order to remain reliable under high load.
- **Maintainability** has many facets, but in essence it's about making life better for the engineering and operations teams who need to work with the system. Good abstractions can help reduce complexity and make the system easier to modify and adapt for new use cases. Good operability means having good visibility into the system's health, and having effective ways of managing it.
