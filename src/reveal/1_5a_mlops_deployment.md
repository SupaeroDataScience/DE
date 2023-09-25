---
title: Deployment & MLOPS
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

This class

- **Quick notions about MLOPS**
- **Cloud Computing & Docker applied to AI**
- **Hands on : Deploy your model in production**

<!--s-->

## Very quick intro to MLOps

<!--v-->

![mlsystems](https://huyenchip.com/machine-learning-systems-design/assets/ml_project_flow.png) <!-- .element: height="40%" width="40%" -->

<!--v-->

![mlops](static/img/mlops_lifecycle.png)  <!-- .element: height="50%" width="50%" -->

<!--v-->

![mlops](https://ml-ops.org/img/mlops-loop-en.jpg) <!-- .element: height="50%" width="50%" -->

<!--v-->

### Layers of "enabling technology"

![mlops](static/img/mlopsinfra.png) <!-- .element: height="75%" width="75%" -->

<!--v-->

- https://huyenchip.com/machine-learning-systems-design/toc.html
- https://ml-ops.org/content/references.html

<!--s-->

## Cloud Computing & AI

<!--v-->

### My usage : Flexibility

![gcp](static/img/infra_army_of_one.png)

<!--v-->

### A full workflow 

![vertex](https://www.royalcyber.com/blog/wp-content/uploads/2022/05/end-to-end-mlops-on-vertex-ai.png)

<!--v-->

### All about that scale

[BLOOM: A 176B-Parameter Open-Access Multilingual Language Model](https://arxiv.org/pdf/2211.05100)

> Training BLOOM took about 3.5 months to complete and consumed 1,082,990 compute hours. Training was conducted on 48 nodes, each having 8 NVIDIA A100 80GB GPUs (a total of 384 GPUs);

<!--v-->

### AI Distributed Computing

![](static/img/distributed_computing.png)

<!--v-->

### Stable Diffusion

![](https://assets-global.website-files.com/61fd4eb76a8d78bc0676b47d/63cf7cb6264c4050ed2ea00e_Screen%20Shot%202023-01-23%20at%2010.37.19%20PM.png) <!-- .element: height="60%" width="60%" -->

[Stable Diffusion Training Times](https://www.mosaicml.com/blog/training-stable-diffusion-from-scratch-costs-160k)

<!--v--> 

### AI Cloud Providers

![](https://geekflare.com/wp-content/uploads/2021/08/lambdagpu-1.jpg)  <!-- .element: height="50%" width="50%" -->

<!--v-->

### The need for tech

![](static/img/anyscale.png)  <!-- .element: height="50%" width="50%" -->

And dask !

<!--s-->

## Containers & AI

<!--v-->

#### Data Science is about reproducibility

* Experimental science
* Communicating results
* Hands-out to other teams
* Deployment and versioning of models

<!--v-->

#### So... containers ?

* ... for standardized development environments
* ... dependency management
* ... for complex / large scale workflows
* ... for deployment

~it works on my notebook !~ *here's the model ready to run !*

<!--v-->

Reproducible development environment

![](https://sp-ao.shortpixel.ai/client/to_webp,q_glossy,ret_img/https://godatadriven.com/wp-content/uploads/2022/10/devcontainer-overview-4.png)  <!-- .element: height="55%" width="55%" -->

<!--v-->

Reproducible development environment [at scale](https://medium.com/netflix-techblog/scheduling-notebooks-348e6c14cfd6) !

![netflix](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*WOEEJizYnO8ibtU2l9jWbA.jpeg)

<!--v-->

[Netflix and notebook scheduling](https://medium.com/netflix-techblog/scheduling-notebooks-348e6c14cfd6)

![netflix](https://miro.medium.com/v2/resize:fit:1400/0*058TIxB_YEFxmUDy)  <!-- .element: height="55%" width="55%" -->

<!--v-->

https://www.kubeflow.org/

![kubeflow](https://miro.medium.com/max/2446/1*ZQsFV3o1c3Amu26Z-IEd7w.png) <!-- .element: height="55%" width="55%" -->

<!--s-->

## Intro to deployment

<!--v-->

### Architecturing (web) applications

![](https://axisbits.com/storage/app/uploads/public/7da/cc4/ec1/7dacc4ec1c9bc16b7aa58185cb8efa5a.png)

<!--v-->

### Communicating between applications

![api](https://www.aloi.io/wp-content/uploads/2019/09/api-visual.png) <!-- .element: height="50%" width="50%" -->

<!--v-->

### REST API

Representational state transfer (REST)

![rest](https://images.tutorialedge.net/uploads/rest-api.png) <!-- .element: height="50%" width="50%" -->

<!--v-->

### Microservices vs "monoliths"

![microservices](https://www.sourcefuse.com/wp-content/uploads/2021/01/D-image4-min.png) <!-- .element: height="50%" width="50%" -->

PS: [Microservices are hard](https://dwmkerr.com/the-death-of-microservice-madness-in-2018/)

<!--v-->

### Multi applications & docker

![docker-compose](https://hosting.analythium.io/content/images/2021/06/compose-3.png) <!-- .element: height="50%" width="50%" -->

<!--v-->

### How does it relate to me ?

<!--v-->

### Hands-On

- How to expose an ML model to a community of users through a web app
- How to build a companion app to interact with your model in an ergonomic fashion
- How to deploy both applications on a single instance (for now)

<!--v-->

![](static/img/mlworkflow.png)  <!-- .element: height="50%" width="50%" -->

<!--v-->

### I have an **awesome** ML model

![model](static/img/meme_2.jpg)  <!-- .element: height="30%" width="30%" -->

<!--v-->

### Just kidding

![model](static/img/meme_3.jpg)  <!-- .element: height="30%" width="30%" -->

<!--v-->

### What I want to do...

![deploy](https://pbs.twimg.com/media/DoGygAjXkAE-ORD.jpg) <!-- .element: height="30%" width="30%" -->

<!--v-->

### How I would do it

![deploy](static/img/deploy.jpg)  <!-- .element: height="50%" width="50%" -->

<!--v-->

### Modern way of doing things

![package](static/img/packaging.png)

- cog : https://github.com/replicate/cog
- pesto : https://github.com/AirbusDefenceAndSpace/pesto

Today, we will do it "manually"

<!--v-->

### Interaction with user ? We use CURL 👎 


```bash
curl -X POST "http://my-instance/predict" \
    -H  "accept: application/json" \
    -H  "Content-Type: application/json" \
    -d "{\"model\":\"string\",\"image\":\"...\"}"
```

<!--v-->

### Interaction with user ? We use CURL 👎 

![json](static/img/json.png)  <!-- .element: height="30%" width="30%" -->

<!--v-->

### Interaction with users ? 👍

![](static/img/results.png)  <!-- .element: height="50%" width="50%" -->

<!--v-->

### Webapp builder for data scientists

![](static/img/streamlit.png)  <!-- .element: height="50%" width="50%" -->

<!--v-->

### Webapp builder for data scientists

- [streamlit](https://streamlit.io/)
- [gradio](https://gradio.app/)

<!--v-->

### Let's build it !

- A model behind a Restful API, packaged in a docker
- A frontend using streamlit, packaged in a docker
- Deploy it on Google Cloud Platform using GCE & docker-compose
- Send it to your friends !

<!--v-->

### More links

- https://github.com/EthicalML/awesome-production-machine-learning
