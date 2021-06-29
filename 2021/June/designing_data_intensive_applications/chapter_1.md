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
scaling up- vertical scaling, moving to a more powerful machine
scaling out - horizontal scaling, dstributing the load across multiple smaller machines