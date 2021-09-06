---
last_modified_date: "2021-08-11 19:40:54.029576"
nav_order: 100
---
# AWS for Solution Architects
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
1. TOC
{:toc}
</details>

# 1: Understanding AWS Cloud Principles and Key Characteristics
The cloud is just a bunch of servers and other computing resources managed by a third-party provider in a data center somewhere

## Cloud Elasticity
{: .no_toc }
One important characteristic of the leading cloud providers is the ability to quickly and frictionlessly provision resources. In a cloud environment, instead of needing potentially months to provision your servers, they can be provisioned in minutes.

Another powerful characteristic of a cloud computing environment is the ability to quickly shut down resources and, importantly, not be charged for that resource while it is down.

**elasticity** is the ability of a computing environment to adapt to changes in workload by automatically provisioning or shutting down computing resources to match the capacity needed by the current workload.

## Cloud Virtualization
{: .no_toc }
**Virtualization** is the process of running multiple virtual instances on top of a physical computer system using an abstract layer sitting on top of actual hardware.

A **hypervisor** is a computing layer that enables multiple operating systems to execute in the same physical compute resource. These operating systems running on top of these hypervisors are **Virtual Machines** (VMs).

## Definition of the Cloud
{: .no_toc }
The **cloud computing** model is one that offers computing services such as compute, storage, databases, networking, software, machine learning, and analytics over the internet and on demand. You generally only pay for the time and services you use.

## The Five Pillars of a Well-Architected Framework
{: .no_toc }

### Pillar 1: Security
{: .no_toc }
- Always enable traceability.
- Apply security at all levels.
- Implement the principle of least privilege.
- Secure the system at all levels: application, data, operating system, and hardware.
- Automate security best practices

### Pillar 2: Reliability
{: .no_toc }
- Continuously test backup and recovery processes.
- Design systems so that they can automatically recover from a single component failure.
- Leverage horizontal scalability whenever possible to enhance overall system availability.
- Use automation to provision and shutdown resources depending on traffic and usage to minimize resource bottlenecks.
- Manage change with automation.

### Pillar 3: Performance Efficiency
{: .no_toc }
- Democratize advanced technologies.
- Take advantage of AWS's global infrastructure to deploy your application globally with minimal cost and to provide low latency.
- Leverage serverless architectures wherever possible.
- Deploy multiple configurations to see which one delivers better performance.

### Pillar 4: Cost Optimization
{: .no_toc }
- Use a consumption model.
- Leverage economies of scale whenever possible.
- Reduce expenses by limiting the use of company-owned data centers.
- Constantly analyze and account for infrastructure expenses

### Pillar 5: Operational Excellence
{: .no_toc }
Measured across three dimensions:
1. Agility
2. Reliability
3. Performance

- Provision infrastructure through code (for example, via CloudFormation).
- Align operations and applications with business requirements and objectives.
- Change your systems by making incremental and regular changes.
- Constantly test both normal and abnormal scenarios.
- Record lessons learned from operational events and failures.
- Write down and keep standard operations procedures manual up to date.

# 2: Leveraging the Cloud for Digital Transformation
## Regions, Availability Zones, and Local Zones
AWS breaks their infrastructure down into parts:
- **AWS Regions** exist in separate geographic areas, and are made up of several isolated and independent data centers
- **Availability Zones** (AZ) are the data centers within a region
- **Local Zones** are mini AZs that provide core services that are latency sensitive

![AWS for Solution Architects Infrastructure](assets/aws-for-solution-architects-infra.jpg)

### Regions
{: .no_toc }
Regions are separate from each other and this promotes availability, fault tolerance, and stability.

Sometimes a service might not be generally available (GA) and is only in one region.

Some services are available globally and aren't region specific Simple Storage Service (S3), Identity Management Service (IAM), and other services have inter-Region fault tolerance -- e.g., RDS with read replicas

AWS has a dedicated region just for the government called AWS GovCloud.

### Availability Zones
{: .no_toc }
The same as a data center. Have multiple power sources, redundant connectivity, and redundant resources.

AZs within Regions are interconnected, which gives you fully redundant, high bandwith, low latency, scalable, encrypted, and dedicated connections.

Some services allow you to choose AZ while some are automatically assigned.

### Local Zones
{: .no_toc }
Allow low latency for select services. Like a subset of an AZ, but doesn't have all the services available in an AZ.

Use Case: Applications which require single-digit millisecond latencies to your end-users, latency-sensitive applications

### Direct Connect
{: .no_toc }
A low-level infrastructure service that enables AWS customers to set up a dedicated network connection between their on-premise facilities and AWS that allows bypassing public internet.

Does not provide encryption in transit, so a separate service (e.g., AWS Site-to-Site VPN) can be paired to encrypt data in transit.

Uses IEEE 802.1Q (I triple E eight oh two dot 1 Q) to create VLANs.

Can reduce costs when workloads require high bandwith by:
1. transfers data from on-prem to cloud, directly reducing ISP commitments
2. costs to transfer data are billed using AWS Direct Connect transfer rate rather than internet data transfer rates, which is typically lower

## Implementing a Digital Transformation Program
Moving legacy on-prem to cloud
Some questions to ask:
- should we do bare minimum, or is it an opportunity to refactor, enhance, and optimize workloads?
- should the transformation be purely technological, or should we transform business processes too?

### Rehost
{: .no_toc }
_lift and shift_
least amount of work, services are simply migrated as is, and any problems with existing applications will come along during the migration.

**Use case**: If you are confident your processes and workflows are solid and don't need to change.

### Refactor
{: .no_toc }
Not only migrating services, but changing their underlying architecture.

**Use case**: You are comfortable with current application but want to take advantage of certain cloud advantages and functionality, such as database failover.

### Revise
{: .no_toc }
Modify, optimize, and enhance existing applications and code base before migrating, then you can rehost or refactor. Good for maintaining business continuity and creating business enhancements, but sub-optimal sometimes because of cost of changing and testing code upfront.

**Use case**: If you know your applications are sub-optimal and need to be revised anyway.

### Rebuild
{: .no_toc }
Completely rewrite and rearchitect the existing applications, which will be considerable work and considerable cost, and might contribute to vendor lock-in.

**Use case**: If the most radical change is needed.

### Replace
{: .no_toc }
Get rid of applications but replace with SaaS alternatives, which may or may not be more expensive than rebuilding depending on talent pool. Learning curve and development life cycle is shortened, but software will require additional licenses.

**Use case**: If there is a commercially available software as a service available and your talent pool is short.


### Migration Assessment Tools
{: .no_toc }
- **AWS Migration Hub**: central repository to keep track of a migration project
- **AWS Application Discovery Service**: automates the discovery and inventory tracking of different infrastructure resources, such as servers, and any dependencies among them
- **AWS Migration Pattern Library**: collection of migration templates and design patterns that can assist in the comparison of migration options and
alternatives
- **CloudEndure Migration**: simplifies cloud migration by automating many of the steps necessary to migrate to the cloud
- **AWS Data Migration Service**: facilitate the migration of data from your on-premises databases to the cloud, e.g., into Amazon RDS

**Digital transformation** involves using the cloud and other advanced technology to create new or change existing business flows. It often involves changing the company culture to adapt to this new way of doing business. The end goal of digital transformation is to enhance the customer experience and to meet ever-changing business and market demand.

### Digital Transformation Tips
{: .no_toc }

1. **ask the right questions**
- how can we be doing what we do, faster and better?
- how can we change what we do to better serve our customers
- can we eliminate certain lines of business, departments, and processes
- what are the desired business outcomes when interfacing with customers
2. **get leadership buy-in**
- need buy-in from C-Suite
- can still do Proof of Concept work to prove value
3. **clearly delineate goals and objectives**
- what are you trying to achieve with migration and ruthlessly pursue that
4. **apply agile methodology to digital transformation**
- small, iterative improvement to realize value earlier, as opposed to waterfall
- look for singles, not home runs
- pick low-hanging fruit and migrate those workloads first, which will build momentum for other, harder tasks later
5. **encourage risk-taking**
- fail, but fail fast and try different things
- it is better to disrupt yourself than someone else do it
6. **clear delineation of roles and responsibilities**
- make sure all team members are aligned on their responsibilities

### Digital Transformation Pitfalls
{: .no_toc }
1. **lack of commitment from the C-Suite**
- might fail to provide vision and path to success or resources
2. **not having the right team in place**
- inexperience with cloud migration, you don't know what you don't know
3. **internal resistance from the ranks**
- people whose roles may be diminished would resist
4. **going too fast**
- moving too much at once without doing any proof of concept work
5. **going too slow**
- spending forever planning or migrating small things might make interest wane
6. **outdated rules and regulations**
- some industries are difficult to disrupt because older regulations exist, e.g., real estate requiring wet signatures

# 3: Storage in AWS
## Amazon Elastic Block Storage (EBS)
hard drive for a server, and can easily detach from one server and attach to another, and useful for persistent data, in comparison to the ephemeral data of an EC2 instance. replicated by design, so no need to set up a RAID or another redundancy strategy.

Snapshots are iterative and stored on S3. They can be compressed, mirrored, transferred across AWS AZs (by Amazon Data Lifecycle Manager). Stored as Amazon Machine Images (AMI) so they can be used to launch an EC2 instance.

using Elastic File Storage (EFS), you can attach the block storage device to multiple EC2 instances

Amazon provides 99.999% availability

- **General-purpose Solid State Devices (SSDs)**
  - solid balance of cost and performance
  - useful for virtual desktops, development and staging environments, application developmenet
- **Provisioned IOPS SSD**
  - provisioned inputs and outputs per second ideal for mission critical apps
  - business applications, production databases
- **Throughput Optimized HDD**
  - good value and reasonable cost for workloads that need high performance and high throughput
  - big data, log processing, streaming applications, data warehouse applications
- **Cold HDD**
  - optimize cost with large volumes of data
  - data the is infrequently accessed

## Amazon Elastic File System (EFS)
Implements a fully managed Network File System (NFS), and several EC2 instances can be mounted to an EFS volume at the same time.

Often used for:
- hosting content management systems
- hosting CRM applications that need to be hosted within an AWS data center but need to be managed by customer

## Simple Storage Service (S3)
Object storage, and AWS's second oldest product, right after EC2. Time To First Byte (TTFB) used to measure performance of a service.

![S3 Performance Chart](assets/aws-for-solution-architects-s3-performance.jpg)

### Comparison of Storage
{: .no_toc}
![Storage Comparison](assets/aws-for-solution-architects-storage.png)

### Enhancing S3 performance
{: .no_toc}
You should be cognizant of where users are going to access content and design around that.

One way is to scale horizontally -- S3 allows as many connections to an S3 bucket as possible.

#### CloudFront
{: .no_toc}
A Content Delivery Network (CDN) that caches S3 content to be served across disperse geographic regions with thousands of Points of Presence (PoP).

#### ElastiCache
{: .no_toc}
Managed AWS service that allows you to store objects in memory rather than disk. When retrieving objects, need to check the cache first then S3.

#### Elemental MediaStore
{: .no_toc}
Supports transfer of video files.

#### S3 Transfer Acceleration
{: .no_toc}
Can achieve single-digit millisecond using CloudFront edge locations to accelerate data transfer over long distances. Useful for transferring data over AWS Regions.

[S3 best practices](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html)

# 4: Cloud Computing

## first computer
{: .no_toc}
- first large-scale electronic general-purpose computer the Electronic Numerical Integrator and Computer (ENIAC)
- built between 1943 and 1945
- design proposed by physicist John Mauchly

## paradigm shift
{: .no_toc}
- introduced 1962 by Thomas Kuhn in _The Structure of Scientific Revolutions_
- scientists accept predominant paradigm, but constantly challenge questioning it
- eventually new paradigm replaces the old paradigm
- e.g. heliocentric replaced geocentric view of solar system

![Service Resources](assets/aws-for-solution-architects-resource-mgmt.png)
## infrastructure as a service
{: .no_toc}
- **advantages**:
  - most flexibility
  - provisioning of computer, storage, and network resources can be done quickly
  - resources can be used for minutes, hours, or days
  - highly scalable and fault-tolerant
  - more thorough control of the infrastructure
- **disadvantages**:
  - security must be managed at all levels, and this is costly and difficult
  - legacy systems might not be able to be migrated to the cloud
  - training costs might be high to onboard new staff to the system
- **examples**:
  - Elastic Cloud Compute (EC2)
  - Elastic Block Storage (EBS)
- **use cases**:
  - backups and snapshots
  - disaster recovery
  - web hosting
  - software dev environments
  - data analytics

## platform as a service
{: .no_toc}
- **advantages**:
  - cost-effective and can use CI/CD principles
  - high availability
  - scalability
  - straightforward customization and config of app
  - reduction in dev effort and maintenance
  - security policies simplification and automation
- **disadvantages**:
  - difficult to integrate on-prem and AWS systems
  - regulations around data security might require securing data (not on third-party environment)
  - vendor lock-in (increasing scale from IaaS to PaaS to SaaS)
  - might be runtime issues because of lack of support for certain application needs
  - legacy systems might be difficult to integrate with AWS
  - can't customize some layers if needed
- **examples**:
  - Elastic Beanstalk
  - RDS
  - Lambda
  - Elastic Kubernetes Service (EKS)
- **use cases**:
  - business process management, like time clocks or company portal
  - business analytics/BI for internal data analytics
  - internet of things
  - communications applications
  - databases
  - API dev

## master data management
{: .no_toc}
- used to define and manage company's critical data, to provide single source of truth
- manages data throughout its lifecycle
- clean up data inconsistencies, duplicates, deliver to consumers

## software as a service
{: .no_toc}
- **advantages**:
  - reduce time, money, and effort on repetitive tasks
  - shift responsibility for installing, patching, configuring, and upgrading software
  - allow focus on tasks that require personal attention, such as customer service
- **disadvantages**:
  - interoperability with other services might not be straightforward
  - vendor lock-in
  - customization is very narrow
  - limited features
- **examples**:
  - WorkMail
  - WorkSpaces
  - QuickSight
  - Chime

## elastic compute (ec2)
{: .no_toc}

## ec2 - general purpose
{: .no_toc}

## ec2 - compute optimized
{: .no_toc}

## ec2 - accelerated computing
{: .no_toc}

## ec2 - memory optimized
{: .no_toc}

## ec2 - storage optimized
{: .no_toc}

# 5: Selecting the Right Database Service

## history of databases
{: .no_toc}

## types of databases
{: .no_toc}

## online transaction processing databases
{: .no_toc}

## third normal form (3NF)
{: .no_toc}

## online analytics processing databases
{: .no_toc}

## ACID model
{: .no_toc}

## BASE model
{: .no_toc}

## relational databases
{: .no_toc}

## document databases
{: .no_toc}

## key-value databases
{: .no_toc}

## wide-column store databases
{: .no_toc}

## elasticsearch
{: .no_toc}

## kendra
{: .no_toc}

## in memory databases
{: .no_toc}

## graph databases
{: .no_toc}

## time-series databases
{: .no_toc}

## ledger databases
{: .no_toc}

# 6: Amazon Athena

## what is amazon athena
{: .no_toc}

## athena supported formats - JSON & CSV
{: .no_toc}

## athena supported formats - ORC
{: .no_toc}

## athena supported formats - Avro
{: .no_toc}

## athena supported formats - Parquet
{: .no_toc}

## presto
{: .no_toc}

## athena federated query
{: .no_toc}

## athena workgroups
{: .no_toc}

## optimizing athena - data partitions
{: .no_toc}

## optimizing athena - data buckets
{: .no_toc}

## optimizing athena - file compression
{: .no_toc}

## optimizing athena - file size
{: .no_toc}

## optimizing athena - columnar data store generation
{: .no_toc}

## optimizing athena - column selection
{: .no_toc}

## optimizing athena - predicate pushdown
{: .no_toc}

## optimizing athena - join, order by, and group by
{: .no_toc}