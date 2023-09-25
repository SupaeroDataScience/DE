# Data Engineering

The amount of data in the world, the form these data take, and the ways to
interact with data have all increased exponentially in recent years. The
extraction of useful knowledge from data has long been one of the grand
challenges of computer science, and the dawn of "big data" has transformed the
landscape of data storage, manipulation, and analysis. In this module, we will
look at the tools used to store and interact with data.

The objective of this class is that students gain:

+ First hand experience with and detailed knowledge of computing models, notably cloud computing
+ An understanding of distributed programming models and data distribution
+ Broad knowledge of many databases and their respective strengths

As a part of the [Data and Decision Sciences](https://supaerodatascience.github.io/)
Master's program, this module aims specifically at providing the tool set
students will use for data analysis and knowledge extraction using skills
acquired in the Algorithms of Machine Learning and Digital Economy and Data Uses
classes.

## Class structure

The class is structured in three parts:

### Data storage

  In the first 10 hours of the course, the history of data storage from single
  databased management systems to distributed filesystems will be presented. For
  evaluation, students will install and manipulate data in PostgreSQL.
  
### Data computation

  20 hours on the computing platforms used in the data ecosystem. We will
  briefly cover cluster computing and then go in depth on cloud computing, using
  Google Cloud Platform as an example. Finally, a class on GPU computing will be
  given in coordination with the deep learning section of the AML class.

### Data distribution

  20 hours on the distribution of data, with a focus on distributed programming
  models. We will introduce functional programming and MapReduce, then use these
  concepts in a practical session on Spark. Finally, students will do a graded
  exercise with Dask.

## Class schedule

Data Storage | | | Readings |
--- | --- | --- | ---
[SQL](0_1_databases.md) | 3h | 18/09/2023 | [Databases introduction (fr)](https://raw.githubusercontent.com/SupaeroDataScience/DE/master/readings/bdd.pdf)
[PostgeSQL](0_2_postgres.md) | 3h | 25/09/2023 | [PostgeSQL](https://www.postgresql.org/docs/manuals/)
[Parallel DBMS](0_3_dbms.md) | 4h | 04/10/2023 | [Slides](https://raw.githubusercontent.com/SupaeroDataScience/DE/master/readings/Cours__Methodes_Outils_Big_Data_A3_Sept_2022_AH.pdf)

Data Computation | | | Readings |
--- | --- | --- | ---
[Cloud Computing](1_2_cloud.md) | 3h | 21/11/2023 | [Readings](1_7_readings.md#about-cloud-computing) |
[Containers](1_3_containers.md) | 3h | 28/11/2023 | [Readings](1_7_readings.md#about-containers)
[Cloud Compute BE](1_4_be.md) | 3h | 29/11/2023 | 
[Distributed DBMS](1_5_distributed.md) | 3h | 04/12/2023 | 
GPU computing | 6h | 13/12/2023 |
Exam | 2h | 19/12/2023 |

| Data Distribution | | | Readings |
| --- | --- | --- | --- |
| [Orchestration](1_5_deployment.md) | 3h | 08/01/2024 | [Readings](1_7_readings.md#about-orchestration) |
| [Deployment TP](1_5_deployment_tp.md) | 3h | 09/01/2024 | [Readings](1_7_readings.md#about-orchestration) |
| [Hadoop and MapReduce](2_3_mapreduce.md) | 3h | 16/01/2024 | [MapReduce](https://raw.githubusercontent.com/SupaeroDataScience/DE/master/readings/mapreduce.pdf) |
| [Spark](2_4_spark.md) | 4h | 17/01/2024 | [Spark](https://raw.githubusercontent.com/SupaeroDataScience/DE/master/readings/spark.pdf) [PySpark](https://spark.apache.org/docs/latest/api/python/pyspark.html) |
| [Cloud DBMS](2_5_cloud.md) | 3h | 04/12/2023 | 
| [Dask](2_5_dask.md)| 3h | 13/02/2024 | [Dask documentation](https://docs.dask.org/en/latest/setup/kubernetes.html) |
| [Dask project](2_6_project.md) | 3h | 13/02/2024 | [Dask](https://raw.githubusercontent.com/SupaeroDataScience/DE/master/readings/dask.pdf) |


