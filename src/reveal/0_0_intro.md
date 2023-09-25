---
title: Tools of Big Data
theme: evo
highlightTheme: vs
separator: <!--s-->
verticalSeparator: <!--v-->
revealOptions:
    transition: 'fade'
    transitionSpeed: 'default'
    controls: true
    slideNumber: true
    width: '100%'
    height: '100%'
---

## Tools of Big Data

**SDD, 2021**

Dennis WILSON

[supaerodatascience.github.io/DE](https://supaerodatascience.github.io/DE/)

<!--s-->

### Software as a Service

![](static/img/web_simple.png)

What happens when:

+ There are more clients than one server can handle?
+ There's more data than one database can store?
+ There are different data types which aren't adapted for your data?
+ You want to show live analysis of the data which integrates the user's request?

<!--s-->

### A growing issue

<table width="30%">
    <tr><td>1 </td><td>	B</td><td> 	byte</td></tr>
    <tr><td>1000 </td><td>	kB</td><td> 	kilobyte</td></tr>
    <tr><td>1000^2 </td><td>	MB</td><td> 	megabyte</td></tr>
    <tr><td>1000^3 </td><td>	GB</td><td> 	gigabyte</td></tr>
    <tr><td>1000^4 </td><td>	TB</td><td> 	terabyte</td></tr>
    <tr><td>1000^5 </td><td>	PB</td><td> 	petabyte</td></tr>
    <tr><td>1000^6 </td><td>	EB</td><td> 	exabyte</td></tr>
    <tr><td>1000^7 </td><td>	ZB</td><td> 	zettabyte</td></tr>
</table>

![](static/img/datasphere.png)

source: [IDC](https://www.seagate.com/files/www-content/our-story/trends/files/idc-seagate-dataage-whitepaper.pdf)

<!--s-->

### Big Data Architectures

![](static/img/big-data-pipeline.png)

source: [Microsoft Azure](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/)

<!--s-->

### Data Architecture Requirements

+ Availability
+ Recoverability
+ Redundancy
+ Consistency
+ Usability

![](static/img/referential_integrity.png)

How to ensure these characteristics for increasing amounts of data requiring large infrastructure?

<!--s-->

### File system storage

<img src="static/img/inodes.png" width="50%">

Unix [inodes](https://man7.org/linux/man-pages/man7/inode.7.html)

<!--s-->

### Databases

![](static/img/database.png)

[Relational Database](https://www.researchgate.net/publication/323466947_Design_and_Analysis_of_a_Relational_Database_for_Behavioral_Experiments_Data_Processing)

<!--s-->

### Beyond Data

+ Store unstructured data that doesn't fit well into a database
+ Store analysis processes
+ Present different interfaces for internal and external processes

![](static/img/datalake.png)

<!--s-->

### Silos, lakes, warehouses

![](static/img/lake_vs_warehouse.png)

[Amazon AWS](https://aws.amazon.com/big-data/datalakes-and-analytics/what-is-a-data-lake/?nc=sn&loc=2)

<!--s-->

### AWS Data Lake

<img src="static/img/Zaloni-Data-Lake-2.png" width="70%">

Zaloni data lake on [AWS](https://aws.amazon.com/blogs/apn/turning-data-into-a-key-enterprise-asset-with-a-governed-data-lake-on-aws/)

<!--s-->

### Data analysis

+ Separable from production data manipulation
+ Transferable between test environment and hardware types
+ Access to high performance CPUs or GPUs
+ High level languages like Python
+ Visualization interface

![](static/img/jupyter.png)

<!--s-->

### Virtualization

<img src="static/img/virtualization.png" width="60%">

Source: [unixtutorial.org](https://www.unixtutorial.org/hw-virtualization/)

Why is this suboptimal for machine learning pipelines?

<!--s-->

### Computing systems

![](static/img/hpc_cloud.bmp)

Cloud advantage:
<br/>hardware based on component requirements

<!--s-->

### Cloud: the new compute paradigm

![](static/img/cloud_providers.jpg)

Source: [DigitalCMO](https://www.digitalcmo.fr/offre-cloud-vous-avez-de-plus-en-plus-le-choix/)

<!--s-->

### Data distribution

<img src="static/img/akamai_latency.png" width="40%">

[Dyn](https://help.dyn.com/understanding-cdn-performance/) on Akamai latency

+ size of data
+ data transfer latency
+ redundancy
+ calculation parallelism

<!--s-->

### The problem

<img src="static/img/distributed.png"  width="40%" >

How do we execute a query when our data is distributed:
+ across multiple different servers?
+ across different replicas?
+ efficiently?

<!--s-->

### Example: word count

<img src="static/img/mapreduce.png" width="40%">

+ Split data tasks into distributable components
+ Define operators and manipulate them
+ Send operations between different servers
+ Use **functional programming**

<!--s-->

### Spark

<img src="static/img/spark.png" width="40%">

+ Data operations (functions) can be passed as objects
+ Written in Scala, a functional programming language
+ Interfaces in Python, C++, Java, and more

<!--s-->

### Tools of Big Data

Understanding modern Big Data tools and systems, focusing on Machine Learning integration

+ Databases
    + 13h, Dennis Wilson and Failor Elfassi (MP Data)
    + SQL, NoSQL, PostgreSQL
    + Database presentation project
+ Data computation
    + 18h, Florient Chouteau (Airbus DS)
    + Cluster and cloud compute
    + Containers and orchestration
    + GPU computer (Laurent Risser)
+ Data distribution
    + 15h, Guillaume Eynard-Bontemps (CNES)
    + MapReduce, Spark, HDFS
    + Orchestration with Kubernetes
    + Dask BE evalutation

<!--s-->

Introduction | | | Readings |
--- | --- | --- | ---
[Introduction to Big Data](slides/0_0_intro.md) | 2h | 27/09/2021 | [Global Datasphere](https://github.com/SupaeroDataScience/DE/tree/master/readings/idc_data.pdf)

Databases | | | |
--- | --- | --- | ---
[Databases overview](0_1_databases.md) | 2h | 27/09/2021 | [Databases and SQL](https://github.com/SupaeroDataScience/DE/tree/master/readings/fntdb07-architecture.pdf)
[PostgeSQL TP](0_2_postgres.md) | 3h | 29/09/2021 | [PostgeSQL](https://www.postgresql.org/docs/manuals/)
[Databases Project](0_3_project.md) | 3h | 06/10/2021 |
[Project presentations](0_3_project.md) | 3h | 02/11/2021 |

<!--s-->

Data Computation | | | Readings |
--- | --- | --- | ---
[Cloud Computing & Google Cloud Platform](1_1_overview.md) | 3h | 18/01/2022 | [Readings](1_7_readings.md#about-cloud-computing)
[Containers](1_3_containers.md) | 2h| 19/01/2022 | [Readings](1_7_readings.md#about-orchestration)
[Orchestration](1_4_orchestration.md) | 1h | 19/01/2022 | [Readings](1_7_readings.md#about-containers) |
[Cloud Compute BE](1_4_be.md) | 6h | 25/01/2022 | 
[GPU computing](1_5_gpu.md) | 3h <br/> 3h | 01/02/2022 <br/> 02/02/2022 | [GPGPU TP](https://lms.isae.fr/course/view.php?id=1226&section=2) |

<!--s-->

| Data Distribution | | | Readings |
| --- | --- | --- | --- |
| [Hadoop and MapReduce](2_3_mapreduce.md) | 3h | 08/02/2022 | [MapReduce](https://github.com/SupaeroDataScience/DE/tree/master/readings/mapreduce.pdf) |
| [Spark](2_4_spark.md) | 3h | 08/02/2022 | [Spark](https://github.com/SupaeroDataScience/DE/tree/master/readings/spark.pdf), [PySpark](https://spark.apache.org/docs/latest/api/python/pyspark.html) |
| [Dask on Kubernetes](2_5_dask.md)| 3h | 14/02/2022 | [Dask documentation](https://docs.dask.org/en/latest/setup/kubernetes.html) |
| [Dask project](2_6_project.md) | 6h | 16/02/2022 | [Dask](https://github.com/SupaeroDataScience/DE/tree/master/readings/dask.pdf) |

<!--s-->

### Case study: all the IPOs

Choose one of the following companies and come up with a short explanation of
what the company offers. Do they sell hard drives? Compute time on a virtual
machine? Specialized artificial intelligence?

+ Snowflake
+ Alteryx
+ Cloudera
+ Talend
+ Splunk
+ Dataiku

Use simple language that could be understood by your grandparents. Post your
explanation on Slack.
