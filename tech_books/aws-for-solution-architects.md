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
