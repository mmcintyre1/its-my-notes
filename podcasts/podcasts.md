# Podcasts
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
1. TOC
{:toc}
</details>


## Data Lineage: Understanding Data Lineage at Scale with Julien Le Dem

| podcast name | Data Skeptic |
| description  | An overview of the OpenTelemetry project  |
| listened on  | 02/24/2022  |
| thoughts     | While ostensibly about data lineage, they don't much get into it until the very end. It's mostly a history of data engineering, from its outset with Hadoop and HDFS at Yahoo through to the move towards SQL, to where we are now, which is a more mature space. They talk about storage formats like Parquet, or Apache Arrow, as well as compute engines like Spark or Flink, to orchestration/event platforms like Apache Pig or Airflow. Julien Le Dem is a highly regarded data engineer in the industry. |
| questions    | Does event sourcing also fulfil this data lineage need? |
| more reading | https://softwareengineeringdaily.com/2021/07/12/data-lineage-understanding-data-lineage-at-scale-with-julien-le-dem/ |

## Open Telemetry

| podcast name | Data Skeptic |
| description  | An overview of the OpenTelemetry project |
| listened on  | 02/23/2022  |
| thoughts     |  OpenTelemetry Cloud Native Computing Foundation (CNCF) sponsored project and is an attempt to standardize service instrumentation. Broadly speaking, it is a set of specifications, APIs, and libraries/SDKs. You implement them in your services, and then you can implement a generic collector which all services pass data to. OpenTelemetry isn't about the storage or viz layers of an observability stack, but rather standardizing the schemas for three types of observability signals:<br> - metrics<br> - logs<br> - traces |
| questions    | Where does the ELK stack fit into OpenTelemetry? |
| more reading | https://newrelic.com/blog/best-practices/what-is-opentelemetry<br>https://github.com/open-telemetry |
