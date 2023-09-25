---
title: Containers & Docker
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

## From Virtualisation to Containerisation

![](static/img/docker_meme.png)

<!--v-->

### Outline

* **Presentation** (30m)
* **Self-paced Workshop** (1h30)
* To be continued with Orchestration & Deployment (next Tuesday)

<!--v-->

#### This class will be successful if you understand

* why we need a tool like docker
* the basics of docker (containers, images) <!-- .element: class="fragment" data-fragment-index="1" -->
* the basics of a container registry <!-- .element: class="fragment" data-fragment-index="2" -->
* how to pull an image and run a container <!-- .element: class="fragment" data-fragment-index="3" -->
* what a Dockerfile looks like <!-- .element: class="fragment" data-fragment-index="4" -->

<!--s-->

### The need for Containers in software

![](static/img/meme.png)

<!--v-->

#### IT Multimodality

![](https://pointful.github.io/docker-intro/docker-img/the-challenge.png)

<!--v-->

#### The Matrix From Hell

![](https://pointful.github.io/docker-intro/docker-img/the-matrix-from-hell.png)

<!--v-->

#### Analogy

![](https://pointful.github.io/docker-intro/docker-img/cargo-transport-pre-1960.png)

<!--v-->

#### Solution ?

![](https://pointful.github.io/docker-intro/docker-img/intermodal-shipping-container.png)

<!--v-->

#### Solution !

![](https://pointful.github.io/docker-intro/docker-img/shipping-container-for-code.png)

<!--v-->

![](https://pointful.github.io/docker-intro/docker-img/separation-of-concerns.png)

<!--v-->

![docker](static/img/buildshiprun.png) <!-- .element: height="60%" width="60%" -->

<!--s-->

![](https://pointful.github.io/docker-intro/docker-img/docker.png)

<!--v-->

Docker is **a** solution that **standardizes** packaging and execution of software in isolated
 environments
 (**containers**) that share resources and can communicate between themselves

> Build, Share, and Run Any App, Anywhere

<!--v-->

[Docker](https://www.docker.com/)

* Created in 2013
* Open Source
* Not a new idea but set a new standard
* Docker is a company built around its main product (Docker Engine)
* in charge of dev of everything docker + additional paid services (Docker hub...)

<!--v-->

Docker is not the only solution for containers

<https://chimeracoder.github.io/docker-without-docker/#30>

<https://podman.io/>

<!--v-->

Docker is some fancy tech over linux kernel capabilities (containers)

![](https://miro.medium.com/max/700/1*4dxszUyIznfjjzSNgpI0nw.png)

[more info](https://medium.com/@goyalsaurabh66/docker-basics-cb006b9be243)

<!--v-->

But Docker is available on [Windows and MacOS](https://www.docker.com/products/docker-desktop) !

![desktop](https://www.docker.com/wp-content/uploads/2021/10/List-plus-running-compose.png) <!-- .element: height="50%" width="50%" -->

<!--v-->

![](https://res.cloudinary.com/practicaldev/image/fetch/s--KO9goPOF--/c_imagga_scale,f_auto,fl_progressive,h_900,q_auto,w_1600/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/p6v8jzajfg7sgcy7d8fs.png)  <!-- .element: height="40%" width="40%" -->

https://www.youtube.com/c/AurelieVache/videos

<!--s-->

### Containers or Virtual Machines

<!--v-->

#### Similarities

* Isolated environments for applications
* Movable between hosts

<!--v-->

#### Drawbacks of VMs

* VM Contains full OS at each install => Install + Resource overhead
* VM needs pre-allocation of resource for each VM (=> Waste if not used)
* Communication between VM <=> Communication between computers

<!--v-->

#### Container vs Virtual Machine

![](https://pointful.github.io/docker-intro/docker-img/containers-vs-vms.png)

<!--v-->

#### Why are docker containers lightweight ?

![](https://pointful.github.io/docker-intro/docker-img/why-are-containers-lightwight.png)

<!--v-->

#### Container vs Virtual Machine, an Analogy

![](https://www.dotnetcurry.com/images/azure/kubernetes/app-deployment-analogy.jpg)

<!--v-->

#### Resources allocation in containers

* Containers share underlying OS / Kernels
* The container engine can allocate resources (CPU, Storage, RAM) on the fly (!= VM)
* GPU is way easier to manage / share with containers

![](static/img/containers_vs_vm.png)

<!--v-->

#### Some drawbacks of containers

* Containers are based on linux tech  
  (Docker makes Windows container possible though)
* Isolation is not perfect since containers share underlying kernels (security and stability)

<!--s-->

### Containers for Data Science

<!--v-->

#### Multiple People

![people](https://i.pinimg.com/736x/8d/f1/bf/8df1bf6ae24e8b2fda7714f3bf3ccfff.jpg)

<!--v-->

#### Complex Workflows

![workflows](https://miro.medium.com/max/1566/1*_EDimQP_2_sen1v3Xf3fpw.jpeg) <!-- .element: height="40%" width="40%" -->

<!--v-->

#### Data Science is about reproducibility

* Experimental science
* Communicating results
* Hands-out to other teams
* Deployment and versioning of models

<!--v-->

#### So... containers ?

* ... for deployment
* ... for standardized development environments
* ... dependency management
* ... for complex / large scale workflows

~it works on my notebook !~ *here's the model ready to run !*

<!--v-->

[Netflix and notebook scheduling](https://medium.com/netflix-techblog/scheduling-notebooks-348e6c14cfd6)

<img src="https://miro.medium.com/max/1229/0*byeqo-pBXVPU6xjq" alt="" style="width: 60%; height: 60%; background:none; border:none; box-shadow:none;"/>

<!--v-->

https://www.kubeflow.org/

![kubeflow](https://miro.medium.com/max/2446/1*ZQsFV3o1c3Amu26Z-IEd7w.png) <!-- .element: height="55%" width="55%" -->

<!--s-->

### Using Docker in practice

![](static/img/docker-jworkflow.jpg)

<!--v-->

#### Vocabulary of Docker

* **Layer**: Set of read-only files to provision the system
* **Image**: Read-Only layer "snapshot" (or blueprint) of an environment. Can inherit from another **Image**. Image have a *name* and a *tag*
* **Container**: Read-Write instance of an **Image**
* **DockerFile**: Description of the process used to build an Image
* **Container Registry**: Repository of Docker Images
* **Dockerhub**: The main container registry of docker.com

<!--v-->

#### Workflow

![workflow](https://pointful.github.io/docker-intro/docker-img/basics-of-docker-system.png) <!-- .element: height="55%" width="55%" -->

<!--v-->

#### Layers, Container, Image

![layers](https://jfrog--c.documentforce.com/servlet/servlet.ImageServer?id=0151r000006uDeN&oid=00D20000000M3v0&lastMod=1584629516000) <!-- .element: height="45%" width="45%" -->

<!--v-->

#### Layer / Image Analogy

Docker:
```Dockerfile
FROM python:3.6
RUN pip install torch
CMD ipython
```

```bash
docker build -f Dockerfile -t my-image:1.0 .
docker run my-image
```

Python:
```python
class BaseImage:
    def __init__(self, a):
       self.a = a

class NewImage(BaseImage):
    def __init__(self, a, b):
       super(NewImage, self).__init__(a=a)
       self.b = b

container = NewImage(a=0,b=1)
```

<!--v-->

#### Dockerfile

* Used to build Images

```Dockerfile
FROM python:3.7
ENV MYVAR="HELLO"
RUN pip install torch
COPY my-conf.txt /app/my-conf.txt
ADD my-file.txt /app/my-file.txt
EXPOSE 9000
WORKDIR "/WORKDIR"
USER MYUSER
ENTRYPOINT ["/BIN/BASH"]
CMD ["ECHO” , "${MYVAR}"]
```

```bash
docker build -f Dockerfile -t my-image:1.0 .
docker run my-image
```

* Reproducible (if you include static data)
* Can be put under version control (simple text file)

<!--v-->

#### Architecture

![](https://docs.docker.com/engine/images/architecture.svg)

<!--v-->

#### Registry

* Local registry: All images/containers in your machine
* https://hub.docker.com/
* GCP Container Registry
* Social Dimension (share docker images to speed up development/deployment)

<!--v-->

#### In practice

<img src="static/img/docker_pratique.png" alt="" style="width: 50%; height: 50%; background:none; border:none; box-shadow:none;"/>

<!--v-->

### What about multi-applications containers ?

<!--v-->

#### Docker Compose

* Multi-containers application with networking (communication)
* "Glue" for complex applications and microservices

![compose](https://www.biaudelle.fr/wp-content/uploads/2021/07/docker-compose-archi.png)

<!--v-->

#### Docker Compose (example)

A database and a webapp

```yaml
version: '3'

services:
  app:
    build: .
    image: takacsmark/flask-redis:1.0
    environment:
      - FLASK_ENV=development
    ports:
      - 5000:5000

  redis:
    image: redis:4.0.11-alpine
```

`docker-compose up` starts both images (you will see that next week)

<!--v-->

#### REMEMBER THIS !!!

![docker](static/img/buildshiprun.png)

<!--s-->

### Docker and GCP

<!--v-->

#### GCP & Docker

* The per-project dockerhub is called [Container Registry](https://cloud.google.com/container-registry/) 
* Your images look like this `eu.gcr.io/project-id/a/b/c:1.0`
* You can use [Google Cloud Build](https://cloud.google.com/cloud-build/) to build dockerfiles remotely 
* `gcloud builds submit --tag gcr.io/[PROJECT_ID]/quickstart-image .`
* To use gcloud with docker: `gcloud auth configure-docker`
* You can even deploy ["virtual machines" with containers directly](https://cloud.google.com/compute/docs/containers)

<!--s-->

### Demo time

<!--v-->

#### bonus : play-with-docker

* You need to have a docker hub account : https://hub.docker.com/
* https://labs.play-with-docker.com/
* Free, interactive, cluster of vms to experiment docker with
* https://training.play-with-docker.com/ lots of resoures !

<!--v-->

![break](https://media.giphy.com/media/WSrMZn2cuMs2UQ6Rnq/giphy.gif)

<!--s-->

### Cheatsheets

<!--v-->

![cheatsheet](https://jrebel.com/wp-content/uploads/2016/03/Docker-cheat-sheet-by-RebelLabs.png)

<!--v-->

#### Dockerfile : Description d'une image

```Dockerfile
FROM python:3.7
ENV MYVAR="HELLO"
RUN pip install torch
COPY my-conf.txt /app/my-conf.txt
ADD my-file.txt /app/my-file.txt
EXPOSE 9000
WORKDIR "/WORKDIR"
USER MYUSER
ENTRYPOINT ["/BIN/BASH"]
CMD ["ECHO” , "${MYVAR}"]
```

```bash
docker build -f Dockerfile -t my-image:1.0 .
docker run my-image
```

<!--v-->

#### Images

    "docker search" sur un registry
        public (DokerHub)
        privé (entreprise)
    "docker build" à partir d'un Dockerfile
    "docker commit" sur un conteneur modifié
    "docker import" d'une arbo de base :
    
    cat centos6-base.tar | docker import - centos6-base

<!--v-->

#### Docker CLI

    docker create   : crée un conteneur
    docker run      : crée et démarre un conteneur
    docker stop     : arrête un conteneur
    docker start    : démarre un conteneur
    docker restart  : redémarre un conteneur
    docker rm       : supprime un conteneur
    docker kill     : envoie un SIGKILL au conteneur
    docker attach   : se connecte à un conteneur en exécution 
    docker exec     : exécute une cmd dans un conteneur

<!--v-->

#### Docker run

    -d, --detach       Run container in background and print ID
    -e, --env=[]       Set environment variables
    -i, --interactive  Keep STDIN open even if not attached
    -p, --publish=[]   Publish a container's port(s) to the host
    --rm        5_orchestration       Automatically rm container when it exits
    -t, --tty          Allocate a pseudo-TTY
    -v, --volume=[]    Bind mount a volume
    -w, --workdir      Working directory inside the container
