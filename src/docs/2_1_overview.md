# Introduction to Data Distribution

[Course Introduction](https://guillaumeeb.github.io/isae-supaero-aibt103-bigdata/00_Course_Introduction.html)

## Course Overview

- Data Distribution & Big Data Processing

Harnessing the complexity of large amounts of data is a challenge in itself. 

But Big Data processing is more than that: originally characterized by the 3 Vs of Volume, Velocity and Variety, 
the concepts popularized by Hadoop and Google requires dedicated computing solutions (both software and infrastructure), 
which will be explored in this module.

## Objectives

By the end of this module, participants will be able to:

- Understand the differences and usage between main distributed computing architectures (HPC, Big Data, Cloud, CPU vs GPGPU)
- Implement the distribution of simple operations via the Map/Reduce principle in PySpark
- Understand the principle of Kubernetes
- Deploy a Big Data Processing Platform on the Cloud
- Implement the distribution of data wrangling/cleaning and training machine learning algorithms using PyData stack, Jupyter notebooks and Dask


## Program

### Big Data & Distributed Computing (3h)

- [Introduction to Big Data and its ecosystem (1h)](https://guillaumeeb.github.io/isae-supaero-aibt103-bigdata/01_Introduction_Big_Data.html)
  - What is Big Data?
  - Legacy “Big Data” ecosystem
  - Big Data use cases
  - Big Data to Machine Learning
- [Big Data platforms, Hadoop & Beyond (2h)](https://guillaumeeb.github.io/isae-supaero-aibt103-bigdata/02_Big_Data_Platforms.html)
  - Hadoop, HDFS and MapReduce,
  - Datalakes, Data Pipelines
  - From HPC to Big Data to Cloud and High Performance Data Analytics 
  - BI vs Big Data
  - Hadoop legacy: Spark, Dask, Object Storage ...

### Spark (3.5h)

- [Spark Introduction (1h)](https://guillaumeeb.github.io/isae-supaero-aibt103-bigdata/03_Spark_Introduction.html)
- [Play with MapReduce through Spark (Notebook on small datasets) (2.5h)](https://mybinder.org/v2/gh/guillaumeeb/isae-supaero-aibt103-bigdata/main?urlpath=lab)

### Kubernetes & Dask (3.5h)

- [Containers Orchestration (1h)](https://guillaumeeb.github.io/isae-supaero-aibt103-bigdata/12_OrchestrationKubernetes.html)
  - Kubernetes & CaaS & PaaS (Databricks, Coiled)
  - Play with Kubernetes (if we have time)
- [Dask Presentation (1h)](https://guillaumeeb.github.io/isae-supaero-aibt103-bigdata/22_Dask_Pangeo.html)
- [Deploy a Data processing platform on the Cloud based on Kubernetes and Dask (1.5h)](https://guillaumeeb.github.io/isae-supaero-aibt103-bigdata/13_Dask_On_Cloud.html)
  - Exercise: DaskHub or Dask Kubernetes or Pangeo


### Evaluation (7h)

- Prerequisite: Pangeo platform deployed before
- Clean big amounts of data using Dask in the cloud (3h)
- Train machine learning models in parallel (hyper parameter search) (3h)
- Notebook with cell codes to fill or answers to give

[Evaluation introduction slides](https://guillaumeeb.github.io/isae-supaero-aibt103-bigdata/30_Evaluation.html)
