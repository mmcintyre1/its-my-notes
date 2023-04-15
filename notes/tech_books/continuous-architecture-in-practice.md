---
last_modified_date: "2021-01-18 19:40:54.029576"
parent: Tech Books
nav_exclude: true
nav_order: 3
---
# Continuous Architecture In Practice


<details open markdown="block">
  <summary>
    Table of contents
  </summary>
1. TOC
{:toc}
</details>

## 1: Why Software Architecture is More Important than Ever
- goal of architecture is to deliver business value, but with increasing speed of delivery, architecture needs to change
- demands from stakeholders have also increased, leading to practices of agile, continuous delivery, and DevOps

### What is Architecture
1. Achieve quality attribute requirements for a software system
  - things like scalability, security, performance, resiliency
2. Define the guiding principles and standards for a project or product and develop blueprints
  - blueprints allow architecture to be abstracted for tech or business stakeholders
3. Build usable (and perhaps reusable) services
  - defining good interfaces for services
4. Create a roadmap to an IT future state
  - transition planning activities to create an IT blueprint

- while architecture might be creating a blueprint up front, many large organizations eschew this as wasted effort because blueprints are hard to maintain and are useless if outdated
- some orgs replace blueprints with standards and common services

### Software Industry Today
1. Monolithic (1980s)
  - large software stack on single machine provided by manufacturer
2. client/server, or distributed monolith (1990s)
  - splitting application into tiers, meaning decisions started needing to be made about where business logic goes
3. Internet-connected (2000s)
  - enhanced client/server, now quality attributes need to be considered
4. Internet & Cloud Computing (2010s)
  - rise of cloud computing and software and infra as a service
5. Intelligent Connected (2020s)

- limitations of up front planning led to agile
- historical challenges still remain
  - achieving complex system attributes like resilience and security
  - meeting needs of stakeholders
  - ensuring technical cohesion across a large system

### Current Challenges with Software Architecture
1. Focus on Tech Details Rather than Business Context
  - gaining understanding of business and its needs not typically done
  - IT architects more comfortable solving technological problems than business ones
2. Perception of Architects not Adding Value
  - architecture broken up into enterprise, solution, and application (system)
  - often enterprise architects aren't close enough to problem domain to add actionable insights
3. Architectural Practices Might be Too Slow
  - increased speed of feedback from stakeholders has come with need for increased speed of delivery
  - many architectural decisions are implicit in the software
  - many architectural practices are geared towards older _systems of record_ rather than _systems of engagement_
  - many of the best architects are deeply involved in building process
4. Some Architects May be Uncomfortable with Cloud Platforms
  - speed of movement means learning is constant and keeping up to date difficult

### Software Architecture in an Increasingly Agile World
- agile started with Extreme Programming (XP) in 1996
- in this model, no need for architects, because "the best architectures, requirements, and design emerge from self-organizing teams" (Agile Manifesto, Principle 11)
- paved the way for _emergent_ architecture, or architectures that in the aggregate exhibit properties beyond just individual parts
- does not scale well for quality attributes, and tech debt and tech features often get deferred
- **Scaled Agile Framework** (SAFe) - architectural runway, or long-term architectural plan
- Large Scale Scrum (LeSS) framework
- Disciplined Agile Deliver (DaD)

### Continuous Architecture
1. Principle 1: Architect products; evolve from projects to products
2. Principle 2: Focus on quality attributes, not on functional requirements
3. Principle 3: Delay design decisions until they are absolutely necessary
4. Principle 4: Architect for change -- leverage the "power of small"
5. Principle 5: Architect for build, test, deploy, and operate
6. Principle 6: Model the organization of your teams after the design of the system you are working on

- the goal of continuous architecture is to speed up the software dev and delivery process by systematically applying an architecture perspective and discipline continuously throughout the process (15)
- artifacts should be a means, not an end

### Continuous Architecture Benefits
- in the typical time, cost, and quality triangle, continuous architecture allows for balance of time and cost constraints while not sacrificing quality
- most innovation teams focus on building an MVP, but when that needs to be turned into a production-grade software that leads to problems, sometimes a complete rewrite -- continuous architecture tends to avoid this

## 2: Architecture in Practice: Essential Activities
- goal of architecture is to balance customer demand and delivery capacity to create a sustainable and coherent system
- system should meet functional and quality attributes
- historically, it was one all-seeing and wise individual doing architecture, but now we refer to "architecture work" and "architectural responsibility"
- Fred Brookes in _Mythical Man Month_ puts emphasis on conceptual integrity -- can be achieved by close collaboration in a team
- models, perspectives, views are valuable architectural artifacts, but are means to an end -- to create a sustainable system

### Quality Attributes
**functional requirements** - describe the business capabilities that the system must provide and runtime behavior
**quality attributes (non-functional requirements** - quality attributes a system must meet in delivering functional requirements, the so-called _-ilities_

- SQuaRe model comprises 8 quality characteristics - Functional Suitability, Performance Efficiency, Compatibility, Usability, Reliability, Security, Maintainability, Portability
- ~10 quality attribute scenarios are manageable for a software system
- **architecturally significant** - decisions which have most impact on architecture of the system
- about balancing tradeoffs between functional and quality attributes

#### ATAM utility tree
- tool for architecture trade-off analysis
1. stimulus - what event triggers architectural scenario
2. response - how a system should be expected to respond
3. measurement - quantify the response to the stimulus
4. environment (optional) - the context in which the stimulus occurs

### Architectural Decisions
- typically, an architect would create a diagram and that would be called architecture
- complex diagram has limited use, since it requires (1) explanation from the creator and (2) it can be hard to change
- the **architectural decision** is the unit of work of an architect

important facets of architectural decision:
1. clearly articulate all constraints
2. focus on quality attributes, not functional requirements
3. all options considered and rationale need to be documented
4. tradeoff between options and effect on quality attributes considered
5. who made the decision and when

#### Making and Governing Architectural Decisions
- the closer you get to implementation, the more decisions are made

**Guidelines**
- main job of higher governance bodies is to define guidelines
- the higher you go, the fewer principles there are

**Visibility**
- create visibility of architectural decisions and circulate at all levels of the institution will minimize architectural compromises
- creating a culture for sharing arch. decisions is difficult to realize, as it requires discipline, perseverance, and open communication

#### Architectural Decisions in Agile Projects
- by clearly defining all known architectural decision, we create architectural backlog
- taking a risk-based approach, you focus on architecturally significant scenarios
- 50% of architecture is communication and collaboration

### Technical Debt
- metaphor for challenge caused by several short-term decisions resulting in long-term challenges
- so widely used it is difficult to define
- the focus on _maintainability_ and _evolvability_ is key to how to think about technical debt
- if a system is not expected to evolve, concern with technical debt is minimal

divide technical debt into three categories:
1. code
2. architecture
3. production infrastructure

#### Capturing Technical Debt
- a tech debt registry is a key artifact

for each tech debt item, need to understand:
1. consequences of not addressing
2. remediation approach for addressing tech debt item

- need to agree on process for prioritization of tech debt, potentially basing on consequences of not resolving
- need to ignore "technical purity" and focus on impact to business value
- product owner decides what items should be prioritized
- you can also carve out protected channel for tech debt
- four main channels of work: 1) features 2) defects 3) technical debt 4) risk (security, compliance, etc.)

### Feedback Loops
- output of a process is fed back as an input into the same process

**key goal of agile and DevOps is:**
1) to achieve greater flow of change
2) increasing the number of feedback loops
3) minimizing time between change happening and feedback being received

steps to implement a feedback loop:
1. *collect measurements* - a small number of meaningful measurements
2. *assess* - multi-disciplinary group to analyze output of feedback
3. *schedule incrementally* - determine incremental change to arch. based on analysis
4. *implement changes* - back to step 1

- pair programming, unit tests, continuous integration, scrums, springs, demos are all tools for feedback loops

- **fitness function** - provides an objective integrity assessment of some architectural characteristics
- **continuous testing** - implements a *shift-left* approach (push testing to the left), using an automated process to improve speed of testing -- every component can be tested as soon as it is developed

### Common Themes in Today's Software Architecture Practice
#### Principles as Architecture Guidelines
principles need to be
1. clear - like slogans, easy to understand and remember
2. provide guidance for decisions
3. atomic - does not require any other context or knowledge

#### Team-Owned Architecture
- star developers are hard to find
- build effective teams in long run is more effective model
- architecture is increasingly becoming a skill rather than role
  - ability to design
  - leadership
  - stakeholder focus
  - ability to conceptualize and address systemwide concerns
  - life cycle involvement
  - ability to balance concerns
  - accountable for conceptual integrity of system

#### Models and Notation
- communication is key, so plenty of time is spent discussing exact meaning of terms
- UML developed to this pursuit
- We cannot overcommunicate!

keys to a model:
1. simplicity
2. accessibility to target audience
3. consistency (in shapes and connections)

#### Design Patterns
- patterns are helpful to communicate archetypes and understand tradeoffs

## 3: Data Architecture
- processing data is the reason information systems exist

### What is Data?
**DIKW Pyramid**
- **data (what)** is the bits and bytes we collect
- **information (what)** is data structured so that i can be understood and processed
- **knowledge (how)** comes from using the data and information to answer questions
- **wisdom (why)** - a little more elusive but can be seen as uncovering connections in data, information, and knowledge

#### Common Language
- having a well-defined and communicated data model is a pre-requisite for successful software dev
- **Domain-Driven Design** - approach to that common language
  - *bounded context* - subdomains that the larger domain split into, each with separate data model, definitions, relationships, and components
  - *ubiquitous language* - language used by dev team and business sponsors within a bounded context
- build cohesive teams around components
- helpful to use a language glossary

### NoSQL and Polyglot Persistence
**polyglot persistence**
- applying the right technology to address each of the different data access patterns required in a system
- goes hand in hand with _microservices_, each component has its own persistence mechanism and shares data only via well-defined APIs
- some problems with microservices:
  1. managing dependencies and interaction patterns can be tricky and high cognitive load
  2. performance issues in all services communicating
  3. each database tech requires specific expertise

types of NoSQL storage:

| type        | main differentiators (strengths)                                                                                                    | limitations                                                                              | typical application                                                                                                      | examples                                      |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| key-value   | Scalability, availability, partition tolerance                                                                                      | Limited query functionality; cannot update part of the value separately                  | Storage of session data, chat room enablement, cache solutions                                                           | Memcached, Redis, Amazon Dynamo, Riak         |
| document    | Flexible data model, easy to develop with because data representation is close to code data structures; some have ACID capabilities | Analytic processing, time series analysis; cannot update part of the document separately | Internet of Things data capture, product catalogs, content management applications; changing or unpredictable structures | MongoDB, CouchDB, Amazon Document DB          |
| wide column | Ability to store large datasets at high reads, scalability, availability, partition tolerance                                       | Analytic processing, aggregation heavy workloads                                         | Catalog searches, Time series data warehouses                                                                            | Cassandra, HBase                              |
| graph       | Relationship-based graph algorithms                                                                                                 | Transactional processing, not easy to configure for scalability                          | Social networking, n-degree relationships                                                                                | Neo4j, Amazon Neptune, Janus Graph, GraphBase |

- **Lightweight Evaluation and Architecture Prototyping for Big Data (LEAP4PD)** provides a good reference for evaluating data solutions

### Scale and Availability
- **CAP thereom** - distributed systems can only guarantee two of the three properties: consistency, availability, and partition tolerance
  - most distributed systems provide partition tolerance, so choice between consistency (will the data returned be right) and availability (will query return answer)
  - _eventual consistency_ - at some point in time in the future, the data will be right
- **PACELC** - If a partition **(P)** occurs, a system must trade availability **(A)** against consistency **(C)**. Else **(E)**, in the usual case of no partition, a system must trade latency **(L)** against consistency **(C)**

### Event Sourcing
- common use of traditional database system is to maintain the state of an application (querying gives a consistent view of domain being represented)
- event sourcing captures all _events_ that go into system, so we can re-create state at any point
- often used in conjunction qith Command Query Responsibility Segregation (CQRS) - one model to update info, another to read

### Data Ownership and Metadata
- important to understand which component is going to master (source of truth) the data
- sharing data by reference means consuming services can't update data (immutable)
  - might lead to race conditions inherent in distributed data
  - also creates additional communications between components and increased read workload

a case for increased metadata:
1. sufficient metadata allows you to discover, integrate, and analyze data sources in an efficient manner
2. track data lineage and provenance
3. metadata is strong enabler of automating software dev and data management process like data pipelines

### Data Integration
two reasons for data integration
1. business process - sharing data between components
2. analytics - move data from multiple sources to single component to facilitate analysis and monitoring

**REST** (representational state transfer)
- relies on concept of resource (a data structure you can expect to be returned by a web endpoint)
- move from a verb-centric view (get_customer_data, delete_invoice, etc) to a noun-centric view and rely on simple HTTP vers to act on your nouns
- eliminates complext, centrally managed middleware

### Data (Schema) Evolution
- **Postel's Law** - be conservative in what you do, liberal in what you accept -- Tolerant Reader
- **Expand and Contract Pattern** - expand to support both old and new version of schema, then, contract to support only new version

## 4: Security as an Architectural Concern
### Security in an Architectural Context
- it is important to involve security experts in your security work
- making a system secure can have an impact on almost any other quality property
- most quality attributes, like security, increase cost, so architectural decisions are about tradeoffs
- modern security has changed to be internet security -- most applications are no longer running in isolated data centers but in massive distributed cloud-based systems
reasons for hostile security environment:
- network-connected systems
- large number of pro and amateur attackers
- large amount of FOSS or external software in software supply chains
- limited general security awareness
- dark net packaging security exploits and attack mechanisms

#### CIA triad
- **Confidentiality** - limiting access to those who are authorized to access it
- **Integrity** - ensuring that only valid changes can be made to the system's data and can only be initiated by authorized parties
- **Availability** - ensuring that the system is available and can be accessed at all times

- from an arch perspective, need to understand requirements for CIA, threats system faces, and security mechanisms (people, processes, and technologies) to protect it
- because most security attributes are what _shouldn't_ happen they are difficult to quantify
- can use checklist approach, such as Open Web Application Security Project (OWASP) Application Security Verification Standard (ASVS)

#### Shifting Security Left
- security should be part of entire system delivery life cycle in small frequent steps ("little and often")
- this is a principle of DevSecOps, to address security as early as possible

### Architecting for Security
- **security threat** - what could go wrong as result of a malicious actor who wants to attack system

#### Threat Modelling
identifying things that can go wrong and working out mitigation
1. *understand* what you are building, i.e., system boundaries, deployment platform, system structure
2. *analyze* what could go wrong and what security problems this could cause (two popular models - **STRIDE** and **attack trees**)
3. *mitigate* the security problems, typically using security tech like single sign-on, role-based access control, attribute-based access control, encryption, digital signatures, etc
4. *validate* by taking a step back and seeing what has been done so far, e.g., talking with experts, testing, etc.

- keep incrementally threat modelling as you add features

#### Threat Identification
**STRIDE**
- *spoofing* - impersonate a security identity
- *tampering* - change data in a way that is not expected
- *repudication* - bypass identity controls
- *information disclosure* - access info without authorization
- *denial of service* - preventing the system from being used
- *elevation of privilege* - gaining security privs the attacker isn't meant to have

**attack trees**
- threat identification from the perspective of the attacker
- root of the tree is goal attributed to attacker
- each node is a strategy for achieving the goal
- continue to decompose each node until leaf node represents a specific and credible attack on the system
- can annotate with risk factors like impact, likelihood, difficulty, cost of attack, etc.

#### Prioritizing Threats
- can use a simple classification system to prioritize threats
- using Likert-scale of High, Medium, Low for likelihood and impact
- not a science, but helpful in comparing opinions
- if you think a threat is serious, it almost certainly is
- keep it simple and focused on threats
- other, more sophisticated threat modelling approaches:
  - Process for Attack Simulation and Threat Analysis (PASTA)
  - Visual, Agile and Simple Threat (VAST) modeling method
  - Operationally Critical Threat, Asset, and Vulnerability Evaluation (OCTAVE)
  - MITRE’s Common Attack Pattern Enumeration and Classification (CAPEC)
  - National Institute of Standards and Technology (NIST) model

### Architectural Tactics for Mitigation
- **Authentication** - confirm the identity of the security principal
- **Authorization** - control what actions security principal can perform and what info they have access to
- **Auditing** - monitor use of sensitive info and sensitive actions to prove security mechanism is working

#### Information Privacy and Integrity
**information privacy** - ability to reliably limit who can access data within a system or data passing between the system and other places
**information integrity**  - mitigation of tampering risks by preventing unauthorized security principals from changing info or authorized principals from changing data in an uncontrolled way

#### Nonrepudiation
**nonrepudiation** - mechanism to prevent security principals from denying their actions
- can be achieved by cryptographic signature for every action, or logging list of user actions in secure, tamper-resistant list

#### Availability
- denial of service attacks and ransomware attacks are common
- some methods to prevent:
  - throttling incoming requests
  - quotas to prevent one request from overwhelming the system
  - local or cloud-based filters to exclude large requests
  - elastic infra to expand as needed
- key tactic for mitigating ransomware is to prevent from happening in the first place
- constant end-user education about phishing attacks, the most common attack vector for ransomware

#### Secrets Management
three main parts to secrets management
1. choosing good secrets
2. keeping them secret
3. changing them reliably

- best approach is to use a dedicated and proven secrets manager
- current view of experts, including NIST, is that you shouldn't force passwords to be changed unless they are compromised, but you should change them immediately if they are

#### Social Engineering Mitigation
- weakest link is typically humans interacting with the system
- need limit access of each user to level of access required for their role
- "four-eyes" approach, or two people to approve

#### Zero Trust Networks
- historically, approach to securing systems was to use _zones of trust_, with level of trust increasing the further into the network you are
  - Internet zone (area outside)
  - trusted zone (company's own private network)
  - demilitarized zone (area between trusted and Internet)
  - privileged zone (area within trusted zone with especially sensitive information)
- problem of this approach is that once a zone is breached, attacker has access to everything in that zone
- new approach is _zero trust networks_, with it's roots in Google's BeyondCorp model
  - need to validate trust relationships and assume that the network we use is hostile

## 5: Scalability as an Architectural Concern
- scalability can be defined as the property of a system to handle an increased workload by increasing the cost of the system
- _increased workload_ - higher transaction volumes or greater number of users
- _system_ combination of software and computing infrastructure, as well as human resources to operate

### Scalability in the Architectural Context
- scalability tactics used at large companies might not apply - need to be careful about too quickly scaling without understanding implications and understanding requirements

#### What Changed: The Assumption of Scalability
- in the past, need to scale was lower in part because:
  - business stakeholders expectations were lower
  - scaling was less possible due to physical constraints
  - scaling might not be needed because transactions were made through human intermediaries
- monolithic arch. led to service-oriented arch, which led to microservice-based architecture enabled by cloud infrastructure
- need for scaling increased as physical constraints disappeared and business requirements mandated it
- we can think about scaling in a supply and demand framework, where increase in demand requires increase in supply, but if demand dries up, supply becomes wasted inventory

#### Types and Misunderstandings of Scalability
- calling a system scalable is a common oversimplification - concept needs to be qualified
- _vertical scalability_, or scaling up, is increasing size of machine
  - expensive way of handling scaling but useful for scaling in-memory data structures
- _horizontal scaling_, or scaling out, is increasing number of compute nodes for an application

three approaches to scaling in increasing complexity:
1. segregating incoming traffic by some sort of partition, similar to sharding (difference between partitioning and sharding is sharding implies separate machines while partitioning might occur on same machine)
2. cloning the compute servers and replicating databases, then distributing traffic via a load balancer
3. splitting the functionality of app into services and distributing services and their associated data to separate infra resource sets (such as containers)

#### The Effect of Cloud Computing
- elastic scalability refers to scalability in the cloud
key concerns:
1. pay-per-use context, unused resources should be released (but not too quickly)
2. instantiating and releasing resources should be automated to keep cost of scalability as low as possible
- some concerns are commercial cloud environments might have scalability limits

### Architecting for Scalability: Architecture Tactics
#### Caching for Scalability
4 types of caches
1. **Database object cache** - fetch results of database query and store in memory, e.g., Memcached, Redis, etc.
2. **Application object cache** - store result of a service (that typically is computationally heavy)
3. **Proxy cache** - used to cache retrieved Web pages on a proxy server
4. **Precompute cache** - stores the results of complex queries on a database node for later retrieval

#### Using Asynchronous Communications for Scalability
- _synchronous_ - code execution will block request until response is received
- _asynchronous_ - code execution will continue while waiting for response
- synchronous is simpler and less costly to design and implement
- _smart endpoints and dumb pipes_ - [Martin Fowler's Microservices](https://martinfowler.com/articles/microservices.html)

#### Stateful and Stateless Services
- a _stateful_ service is on that needs additional data besides what is provided with the current request in order to successfully process the request
- _state_ might exist in the client (e.g., cookies), in the service instance, or outside the instance - only in the service instance is stateful
- a _stateless_ service does not need additional info beyond what is provided with the _request payload_
- stateless services are easier to scale because they decouple data and compute -- don't need to worry that a particular compute node is pointed at the right data
- can be difficult to implement stateless because engineers are used to working with stateful services, and dealing with user session data from stateless can be tricky (best approach might be to keep user session data small and cache to be accessible by any compute node)

#### Microservices and Serverless Scalability
- for microservices, size isn't as important as loose coupling, stateless design, and doing a few things well
- serverless, of function as a service (FaaS) architecture, e.g., AWS Lambda, Google Cloud Functions, etc.
- serverless usually increases dependency on cloud vendor

## 6: Performance as an Architectural Concern
- performance is about time and the software system's ability to meet its timing requirements
- it is also about management of systems resources in the face of particular types of demand to achieve acceptable timing behavior
- typically measured in _throughput_ and _latency_
- "Performance can also be defined as the ability for a system to achieve its timing requirements using available resources, under expected full-peak load"
- most systems have performance concerns; only systems with significantly variable workloads have scalability concerns

### Forces Affecting Performance
- one way to look at performance is as contention-based model -- system's performance determined by limiting constraints, such as operating environment
- performance can be improved by controlling resource demand as well as managing resource supply

### Architectural Concerns
- how do we measure, using clear, realistic, and measurable objectives, timing and computational resources
**timing**
- measure timings from the end-user point of view
  - response time/latency - how long to
  - turnaround time - time to complete a batch of tasks
  - throughput - amount of workload in a unit of time

**computational resources**
- measure computational resources
  - CPU usage
  - memory usage
  - disk usage
  - network usage

- also, cost effectiveness not commonly measured as quality attribute, but almost always a factor to consider

### Architecting for Performance
- **microservice architecture**
  - many architectures are moving to small, decoupled, single responsibility services
  - can lead to performance problems, as too many calls between services can lead to increased execution time
- **NoSQL Tech**
  - need to understand read and write patterns to choose appropriate NoSQL tech
  - choice of tech has large effect on performance of the system
- **Public/Commercial Clouds**
  - cloud provides important capabilities, such as pay-as-you-go, elasticity
  - performance is not just responsibility of cloud provider, as you need to build systems that can take advantage of these capabilities
  - also need to consider data locality (bring data to compute, or bring compute to data)
- **serverless architectures**
  - with serverless, engineers can ignore infrastructure -- provisioning, scaling, etc.
  - you can also run app code from anywhere, e.g., edge servers close to end users, increasing performance and decreasing latency, but comes at a cost

#### Performance Modeling
- a _performance model_ provides estimate of how software system is likely to perform against different demand factors
- allows you to estimate performance
- you also need data capture and analysis model that enables you to refine model based on performance test results

#### Performance Testing
- purpose of perf testing is to measure performance of software system under normal and expected max load
- need to test in env that is as close as possible to prod

different types of performance tests:
- _normal load testing_ - expected normal load, test response time, responsiveness, turnaround time, throughput, and cloud infra resource utilization
- _expected max load_ - similar to normal, but under expected max load
- _stress testing_ - beyond max load, helps establish corner cases

#### Tactics to Control Resource Demand-Related Forces
- **reduce overhead** - group smaller services into larger services
- **limit rates and resources** - use resource governors and rate limiters
- **increase resource efficiency** - code optimization in critical services

#### Tactics to Manage Resource Supply-Related Forces
- **increase resources** - scale up or out
- **increase concurrency** - process requests in parallel
- **use caching** - use caching to reduce roundtrips to database

#### Database Performance Tactics
- **materialized views** - a type of precompute cache, makes a physical copy of an input/output intensive query (typically with several joins)
- **indexes** - add indexes to speed read queries -- indexes add overhead to writes and require space on disk
- **data denormalization** - store data that would otherwise be normalized across tables in single table, which would speed up read queries

## 7: Resilience as an Architectural Concern
- in the past, high-availability meant we accepted a certain amount of planned an unplanned downtime
- now, approach is to aim for minimal downtime

### Resilience in an Architectural Context
- _fault_ - an accidentla condition that may cause system to fail
- _failure_ - when a system or component deviates from required behavior
- _availability_ - measurable quality attribute of a system -- ratio of time system is available to time it could be available
- _reliability_ - builds on availability and adds constraint of correct operations, "the probability of a failure-free software operation for a specified period of time in a specified environment"
- _high availability_ - tech that helps achieve availability, typically clustering or database replication
- _resilience_ - each part of a system be responsible for contributing to a system's availability by adapting its behavior when faults occur;
  - tolerating latency
  - retrying requests
  - automatically restarting processes
  - limiting error propagation, etc.

- failure is inevitable, so need to build systems that provide service even when some part is malfunctioning

four aspects to prevent failure:
1. knowing what to do - what automated mechanisms and manual processes are needed and where, e.g., failover, shedding load, restarting
2. knowing what to look for - so we can monitor systems for events that threaten availability, e.g., hardware failures, software failures, etc.
3. knowing what has happened - so we can learn from experience, successes and failures
4. knowing what to expect - both backward looking info and forward looking predictions

#### Business Context
- typically talk about number of 9's of availability (5 9s, or 99.999% is 1 second unavailable per day)

limited metric because:
1. most situations, more is assumed to be better, but 5 9s is expensive and complex
2. practical differences between amount of 9s is basically zero for most businesses
3. these measures don't consider timing of unavailability

two types of systems:
1. need to be available just about all the time
2. can tolerate longer periods of downtime

#### Availability Metrics
- **MTBF** - mean time between failures - used for system function
- **MTTR** - mean time to recovery - used for system function
- **RPO** - recovery point objective - how much data can be recovered (in time)
- **RTO** - recovery time objective - how long it takes to recover data

- minimizing time to recover is better than reducing time in between failures -- leads to more availability and more resilience

#### Resilient Organization
- competency of a resilient org is to know what has happened in past and learn from it
things to think about re: learning
1. although people want to share successes and failures, sometimes it just doesn't happen, either because people don't feel safe, or it isn't highly prioritized
2. when engaged in retros, needs to be data-drive, otherwise retros are based in incomplete memories and opinions rather than facts
3. while a good retro might happen, needs to be grounded in action and plan to build long-term impact

- a resilient organization works on resilience via people, processes, and tech to create culture and org that is resilient, not just the tech stack

### Architecting for Resilience
path to technical resilience:
1. **recognize** problem to diagnose and take remedial action
  - health checks, metric alerts
2. **isolate** problem so it doesn't affect other parts of the system
  - logical or physical separation in environments, fail fast
3. **protect** system components that might become overloaded
  - controlled retries
4. **mitigate** the problem, preferably through automated means
  - state replication, fault-tolerant request handling
5. **resolve** the problem by confirming mitigation is effective and complete or identifying further intervention
  - controlled restarts, failover

#### Measurements and Learning
- need to understand what is going on today, what happened in the past, and projecting what could happen
- generate a stream of learning opportunities
- _embed measurement mechanisms_ into the system
- _analyze data regularly_, ideally automatically
- _perform retrospectives_ on both good and bad periods
- _identify learning opportunities_ from data and retros
- _improve continuously and intentionally_ by building a learning culture

### Architectural Tactics for Resilience
#### fault recognition tactics
**health checks** - verify system is working, typically using synthetic transaction that mimics real load
**watchdogs and alerts** - watchdog is a piece of software that looks for a specific condition then performs an action, typically an alert

#### isolation tactics
**sync (RPC) vs. async (messages)** - an async system is much more resilient than a sync one -- faults propagate quickly
**bulkheads** - conceptual idea to limit scope of a failure to a specific part of the system
**defaults and caches** - use cache (or defaults as a rudimentary cache) to serve data even if system is down

#### protection tactics
**back pressure** - signal to callers that queue or message bus is full and to stop sending new requests until queue is clear
**load shedding** - reject workload that can't be processed or that would cause system to be unstable -- a variant is throttling/rate limiting
**timeouts** - define how long a caller should wait until caller should be notified that request failed
**circuit breakers** - a state machine-based proxy that sits in front of service meant to "trip" if certain conditions (count of aggregate errors, e.g.,) are met

#### mitigation tactics
**data consistency: rollback and compensation**
- ACID transactions to ensure state of system is consistent
- dealing with distributed transactions (across multiple systems), typical algorithm is two phase commit (2PC), which isn't very performant
- newer idea of compensating transactions or sagas, where if you have a sequence of, say, three writes that need to happen, each write is committed but if any fail, compensating transactions happen to the successful ones to revert state

**data availability: replication, checks, and backups**
- replication can be used to mitigate node failure by ensuring data is immediately available on another node
- checking involves checking both underlying storage mechanisms integrity and checking integrity of system data
- backup ensures a copy of data is available in case of disaster

### Maintaining Resilience
#### Operational Visibility
- key to operational visibility is monitoring, usually thought of as metrics, traces, and logs
- observability can be thought of as extending monitoring to provide insight into internal state of system to allow failure modes to be better predicted and understood

#### Testing for Resilience
- _chaos engineering_ - to introduce failures into system to check response

#### Dealing with Incidents
- old way was Information Technology Infrastructure Library (ITIL) based service delivery management (SDM)
- transitioned to devops, where team develop and operate (and mitigate incidents)
effective incident response requires:
1. well-structured, thoroughly rehearsed approach
2. well-defined roles, e.g., incident command, problem resolution, communications, etc.
3. effective, pre-agreed set of tools
4. well thought through approach to communication within resolution team and outwards

## 8: Software Architecture and Emerging Technologies
- benefit of architecture-led aproach when team uses emerging tech is architecture can be used to plan and communicate with stakeholders
- sound planning and clear communication reduce implementation and tech risk
- new tech is risk, and concentration should be on reducing risk

### Artificial Intelligence, Machine Learning, and Deep Learning
- _artificial intelligence_ - intelligence demonstrated by machines by imitating thinking funcitons associated with human brain, e.g., learning and problem solving
- _machine learning_ - augmenting software systems with statistical models to perform specfic task without explicit instructions
- _deep learning_ - subset of machine learning that uses artificial neural networks

#### Types of Machine Learning
- **supervised learning** - use labeled training datasets to learn model parameters to perform classification (divide input into two or more classes) of operational datasets
- **unsupervised learning** - finding structure in datasets consisting of input data without labelled responses
- **reinforcement learning** - computer interacts with a dynamic environment in which a certain goal must be attained (driving a car, winning a game, etc.)

#### Problems Solved by Machine Learning
- document classification
- chatbots and conversational interfaces for customer service
- data entry
- advanced analytics

- architectural concerns for training and deploying ML models are provenance of data, observability of ML task performance, metadata management, security, explainability (results make sense to humans)

### Shared Ledger, Blockchain, and Distributed Ledger Technologies
- _shared ledger_ - a comprehensive record of transactions, info, or events that are replicated, shared, and synchronized across multiple, sites, countries, or institutions
- _blockchain_ - secure and immutable list of blocks of information, each containing a cryptographic hash of the previous block, a timestamp, and a transaction
- _distributed ledger_ - a shared ledger that is maintained by multiple parties

problems solved by shared ledger:
- clearing and settlements of security trades
- international payments
- anti-money laundering
- verifying customer identity
- insurance
- trade finance

- often, use cases that supposedly require a shared ledger might be better served by a distributed database

## Thoughts on the Book
Most problems in technology are really communication problems. Most architecture problems then are ones of consensus; agreement between institutions and factions within an organization, between product, tech, the dev teams, that one dev manager who was a dev and was a MySQL pro who hasn't met a solution that MySQL couldn't answer. Building that consensus means you rarely arrive at a technically pure solution, one that meets all use cases optimally. There are just too many competing forces, often too much institutional inertia or too much tapering interests in projects that take longer than a 3 month program increment. This book attempts to define a language we can use when talking about architecture. What does scalability, or security, or performance really mean outside of the buzzwordy, euphemistic way the terms can be bandied about. One who is fulfilling the competencies of an architect then can use this language to build consensus, to get the sort of buy-in that is required for doing anything in the complicated ecosystems of today's enterprises. If you can agree that performance, or scalability can be reduced down to a series of quantifiable stimulus, response, and measurement triads, then picking the tech stack to meet those use cases is an implementation detail.

This book is an argument for "continuous architecture", building off the iterative and continuous delivery of software we have seen with the Agile and DevOps movements over the last ten years and staking out arguments for what a continuously delivered architecture looks like within that framework. The "in practice" part refers as much to the recurring case study of a trade finance system the book has threading through each chapter as it does to an emphasis on the process and people edges of the PPT framework.

So many book reviews of tech books hinge on whether or not the reader already knows what's in the book. A book is either castigated as a beginner sampler, or as reductive to the topics it addresses. I think in the case of this book, it isn't attempting to tread new ground but to build a ubiquitous language of architectural concerns. It breaks down topics and provides mini-frameworks for how to talk about them, giving you predominant trends and implementations within a given quality concern. Sure, after reading this books trim 268 pages you won't be ready to implement a microservice architecture, but you'll know the questions to ask, where to start, and what to concentrate on. And that is the strength of this book. It provides scaffolding for how to think about architecture, outlining 6 principles ((1)Architect products; evolve from projects to products, (2) Focus on quality attributes, not on functional requirements, (3) Delay design decisions until they are absolutely necessary, (4) Architect for change -- leverage the "power of small", (5) Architect for build, test, deploy, and operate, and (6) Model the organization of your teams after the design of the system you are working on), and harkening back to them constantly. Each quality attribute that the book addresses will reference these principles, providing a metronome-like repetition drill.

The book serves as as good as any an entry point for introduction into the increasingly diffuse competencies of an architect, and while I skipped their initial book about continuous architecture, I found this one to be an effective tool in building out my mental model of architecture.