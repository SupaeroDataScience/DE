---
title: Data Computation Intro
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

<img src="https://upload.wikimedia.org/wikipedia/commons/9/97/120106-G-IA651-272_%286668116881%29.jpg" alt="" width="40%" height="40%" style="background:none; border:none; box-shadow:none;"/>

<!--v-->

## Cloud Computing, Containers & Orchestration

by a data scientist, for data scientists

**ISAE-SUPAERO, SDD, November 2023**

Florient CHOUTEAU

<!--v-->

### Who ?

<img src="static/img/ads_logo.jpg" alt="" width="128px" height="128px" style="background:none; border:none; box-shadow:none;"/>

- **Florient CHOUTEAU**, SDD 2016
- Expert (Staff Engineer) in Artificial Intelligence for Space Systems at **Airbus Defence and Space**
- Computer Vision Team (Earth Observation, Space Exploration, Space Domain Awareness)
- Specialized in Satellite Imagery Processing & Deep Learning
- Working regularly on cloud infra, remote development environment, docker

Any question ? contact me on slack !

<!--v-->

### Objectives of this class

Introduction to global concepts of cloud computing, virtualisation, containers etc. from a **user** point of view

<!--v-->

eg. having manipulated and having a rough idea of...

... tools & concepts you **will** need in later workshops (DL, Spark, Dask, Hackathon)...

... tools & concepts you **may** need during your internships and early career...

... *cloud native* culture you **should** need later !

<!--v-->

### Disclaimer !

I am not a Cloud Engineer, or a Devops,  ... <!-- .element: class="fragment" data-fragment-index="1" -->

... so I'll be showing you these from a "AI Engineer" point of view  <!-- .element: class="fragment" data-fragment-index="2" -->

... and try to give you pointers for your internship / 1st job ...  <!-- .element: class="fragment" data-fragment-index="3" -->

... "as if I was the one on the other side of the classroom" <!-- .element: class="fragment" data-fragment-index="4" -->

<!--v-->

### This class will be successful if...

- You understand why & how the cloud can be useful for you <!-- .element: class="fragment" data-fragment-index="1" -->
- You can connect to and manipulate remote machines <!-- .element: class="fragment" data-fragment-index="3" -->
- You are familiar with remote development environments <!-- .element: class="fragment" data-fragment-index="4" -->
- You know the basics of containerisation and docker <!-- .element: class="fragment" data-fragment-index="5" -->
- And you have applied them to deploy your model into "production" <!-- .element: class="fragment" data-fragment-index="6" -->
- You have a rough idea of the problematic of orchestration <!-- .element: class="fragment" data-fragment-index="7" -->

<!--v-->

### Schedule

|  Date | Length | Content                                              |
|:-----:|:------:|------------------------------------------------------|
| 08/10 |   3h   | Intro to Cloud Computing & Remote Dev Env            |
| 15/10 |   3h   | Google Cloud Platform                                |
| 22/10 |   3h   | Containers & Docker                                  |
| 05/11 |   3h   | BE Docker & GCP                                      |
| 13/11 |   3h   | BE Deploy your ML Model in Production                |

<!--v-->

### ⚠️

Some things may go wrong, especially because of :
- The ISAE WIFI / 4G connection inside the room
- Your computer configuration (OS, browser, etc.)
- Google Cloud Platform responsiveness

Brace yourselves 💪
