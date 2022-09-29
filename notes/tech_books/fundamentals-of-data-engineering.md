---
last_modified_date: "2022-09-29 19:40:54.029576"
parent: Tech Books
nav_exclude: true
author: "Joe Reis and Matt Housley"
publication_year: 2022
nav_order: 1
---

# Fundamentals of Data Engineering
{: .no_toc }


<details open markdown="block">
  <summary>
    Table of contents
  </summary>
1. TOC
{:toc}
</details>


## 1: Data Engineering Described

**what is data engineering?**
> Data engineering is the development, implementation, and maintenance of systems and processes that take in raw data and produce high-quality, consistent information,that supports downstream use cases, such as analysis and machine learning. Data engineering is the intersection of security, data management, DataOps, data architecture, orchestration, and software engineering. A data engineer manages the data engineering lifecycle, beginning with getting data from source systems and ending with serving data for use cases, such as analysis or machine learning.


<div style="text-align:center">
  <a href="/assets/img/fundamentals-of-data-engineering/data-engineering-lifecycle.png">
    <img src="/assets/img/fundamentals-of-data-engineering/data-engineering-lifecycle.png" alt="aggregate">
  </a>
</div>

### Evolution of Data Engineer
{: .no_toc }
- has it's roots in the business data warehouse (coined by Bill Inmon in 1989 but predates this to the 70s)
- IBM creates SQL in the 90s
- massively parallel processing (MPP) databases expanded the utility of data crunching
- in early 2000s, powerhouse tech companies emerge (Google, Yahoo, Amazon, etc)
- these companies begin working on big data and creating open source utilities (like Yahoo and Hadoop or Google and MapReduce) to handle
- big data engineers evolved to use these big data tools
- eventually, big data began to lose steam because of simplification (big data tools are tricky to work with and require specialization)
- with advent of cloud, that brought about decentralized, modularized, managed, and highly abstracted tools and generalized big data engineer to just data engineer

<div style="text-align:center">
  <a href="/assets/img/fundamentals-of-data-engineering/hierarchy-of-needs.png">
    <img src="/assets/img/fundamentals-of-data-engineering/hierarchy-of-needs.png" alt="aggregate">
  </a>
</div>

- data engineering straddles the divide between getting data and getting value from data

### Data Engineering Skills
{: .no_toc }
- skill set of a data engineer encompasses the “undercurrents” of data engineering: security, data management, DataOps, data architecture, and software engineering
- the data engineer juggles a lot of complex moving parts and must constantly optimize along the axes of cost, agility, scalability, simplicity, reuse, and interoperability
- data engineer typically doesn't build ML models, create reports or dashboards, perform data analysis, build key performance indicators (KPIs), or develop software applications
- data engineer must understand both data and technology, know best practice around data management, be aware of various options for tools, their interplay and tradeoff
- requires good understanding of software engineering, DataOps, and data architecture
- must understand requirements of data consumers
- languages: SQL, python, JVM (Java, Scala, Groovy), bash/powershell

### Data Maturity
{: .no_toc }
- Data maturity is the progression toward higher data utilization, capabilities, and integration across the organization
1. starting with data
    - fuzzy, loosely defined (or no) goals with data
    - adoption and utilization low
    - data team is small
    - data engineer's goal is to move fast, get traction, and add value
2. scaling with data
    - moved away from ad-hoc data requests to formal data practices
    - challenge is creating scalable data architecture and planning for a future where company is data-driven
    - data engineer moves from generalist to specialist
3. leading with data
    - company is data-driven
    - automated pipelines allow people in company to self-serve analytics and ML
    - introducing new data sources is seamless

### Business Responsibilities
{: .no_toc }
- Know how to communicate with nontechnical and technical people
- Understand how to scope and gather business and product requirements
- Understand the cultural foundations of Agile, DevOps, and DataOps
- Control costs
- Learn continuously

**type A data engineers**
- A for abstraction
- avoids heavy lifting
- keeps data architecture abstract and straightforward
- use off-the-shelf products

**type B data engineers**
- B for build
- build data tools and systems that scale and leverage company's core competency and competitive advantage
- more often found at more data mature orgs

### Stakeholders
{: .no_toc }
**upstream stakeholders**
- data architects
- software engineers
- DevOps engineers and site-reliability engineers

**downstream stakeholders**
- data scientists
- data analysts
- machine learning engineers and AI researchers