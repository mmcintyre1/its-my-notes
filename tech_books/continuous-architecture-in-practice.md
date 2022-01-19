---
last_modified_date: "2021-01-18 19:40:54.029576"
nav_order: 98
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
