---
title: Deployment
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

## Intro to deployment

<!--v-->

### Architecturing (web) applications

![api](static/img/webapp_architecture.jpg)  <!-- .element: height="50%" width="50%" -->

<!--v-->

### Communicating between applications

[Application Programming Interface](https://glossary.cncf.io/application-programming-interface/)

> Une API (application programming interface ou « interface de programmation d’application ») est une interface logicielle qui permet de « connecter » un logiciel ou un service à un autre logiciel ou service afin d’échanger des données et des fonctionnalités.

<!--v-->

### API

![api](static/img/infographie_api.jpg) <!-- .element: height="50%" width="50%" -->

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

- **Backend** How to expose an ML model to a community of users through a web app
- **Frontend** How to build a companion app to interact with your model in an ergonomic fashion
- **Deployment** How to deploy both applications on a single instance

<!--v-->

In the data science workflow, 

![](static/img/mlworkflow.png)  <!-- .element: height="50%" width="50%" -->

<!--v-->

I have an **awesome** ML model

![model](static/img/meme_2.jpg)  <!-- .element: height="50%" width="50%" -->

<!--v-->

(Just kidding)

![model](static/img/meme_3.jpg)  <!-- .element: height="50%" width="50%" -->

<!--v-->

I want to deploy it on the cloud for other to use

![model](static/img/mistralserving.png)  <!-- .element: height="50%" width="50%" -->

<!--v-->

Today we will do it by hand

![deploy](static/img/deployment.png)  <!-- .element: height="50%" width="50%" -->

<!--v-->

Other methods for ML Model packaging behind a web server

![package](static/img/packaging.png)

- cog : https://github.com/replicate/cog
- pesto : https://github.com/AirbusDefenceAndSpace/pesto
- litserve : https://github.com/Lightning-AI/LitServe

<!--v-->

Interaction with user ? We use CURL 👎 

```bash
curl -X POST "http://my-instance/predict" \
    -H  "accept: application/json" \
    -H  "Content-Type: application/json" \
    -d "{\"model\":\"string\",\"image\":\"...\"}"
```

<!--v-->

Interaction with user ? We use CURL 👎 

![json](static/img/json.png)  <!-- .element: height="30%" width="30%" -->

<!--v-->

Interaction with users ? 👍

![results](static/img/results.png)  <!-- .element: height="50%" width="50%" -->

<!--v-->

Webapp builder for data scientists

![streamlit](static/img/streamlit.png)  <!-- .element: height="50%" width="50%" -->


[you've seen it before](http://supaerodatascience.github.io/DE/1_4_be.html#6-lets-discover-streamlit)

<!--v-->

Webapp builder for data scientists

- [streamlit](https://streamlit.io/)
- [gradio](https://gradio.app/)

<!--v-->

Let's build it !

- A model behind a Restful API, packaged in a docker
- A frontend using streamlit, packaged in a docker
- Deploy it on Google Cloud Platform using GCE & docker-compose
- Send it to your friends !

<!--v-->

In reality, it's much more complex...

![](static/img/modelserving_complex.png)  <!-- .element: height="50%" width="50%" -->

<!--v-->

How to scale deployment ?

- [CS229 - Class by Chip Huyen](https://docs.google.com/presentation/d/1U_zKs19VLJKnGE02JDRnzxJ8lgeVF22WSZ_GrA646fY/edit#slide=id.p)
- [CS229 - Deployment with Ray Serve](https://github.com/anyscale/academy/blob/main/ray-serve/e2e/tutorial.ipynb)
- https://docs.ray.io/en/latest/serve/develop-and-deploy.html

<!--v-->

Some links

- https://github.com/EthicalML/awesome-production-machine-learning
- Machine Learning System Designs https://stanford-cs329s.github.io/
