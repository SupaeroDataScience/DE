---
title: Intro to Orchestration
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

## Containers Orchestration

![orchestra](static/img/gif-orchestra-conductor.gif)

<!--v-->

You just deployed your ML model in production **on one machine** <!-- .element: class="fragment" data-fragment-index="1" -->

<!--v-->

#### Questions

Suppose I have a large pool of machines available

* How do I **deploy my container on several machines ?** <!-- .element: class="fragment" data-fragment-index="1" -->
* How do I **put the right containers at the right spot ?** <!-- .element: class="fragment" data-fragment-index="2" -->
* How do I **scale (up and down) to demand ?** <!-- .element: class="fragment" data-fragment-index="3" -->
* How do I **expose the http endpoints ?** <!-- .element: class="fragment" data-fragment-index="4" -->
* How do I **manage failure of containers ?** <!-- .element: class="fragment" data-fragment-index="5" -->
* How do I **update my model without downtime** <!-- .element: class="fragment" data-fragment-index="6" -->

<!--v-->

### In reality, it's much more complex...

![](static/img/model-serving-complex.png)  <!-- .element: height="50%" width="50%" -->

<!--v-->

### Orchestration

<img src="static/img/container-orchestration-overview.jpg" alt="" style="width: 40%; height: 40%; background:none; border:none; box-shadow:none;"/>

<!--v-->

#### The next step

![](static/img/docker-swarm-vs-k8s.png)

<!--v-->

#### Orchestration

- containers are a lightweight mechanism for isolating an application's environment
- specify the system configuration and libraries to install
- avoid conflicts with other applications
- each application as a container image which can be executed reliably on any machine
- place multiple workloads on the same physical machine or distributed over many machines
- orchestration for fail cases of containers or machines
- allow for updates without downtime by creating new containers

<!--v-->

### Orchestration Design Principles

- **Declarative** - describe ideal system state
- **Distributed** - use multiple machines for scale & properly use each machine resources
- **Microservice** - decouple applications into individual services
- **Immutable** - Change image versions, not instances

<!--v-->

### Examples...

- Docker Swarm
- CoreOS Fleet
- [Apache Mesos](https://mesos.apache.org/) / [Marathon](https://github.com/mesosphere/marathon)

... and so many more !

![ecosystem](static/img/k8s-ecosystem.jpg)

<!--v-->

![kub](static/img/k8s-cluster-overview.png)

<!--s-->

### Kubernetes ("Helmsman")

![helm](static/img/gif-helm-wheel.gif)

<!--v-->

![borg](static/img/borg-omega-kubernetes.jpg) <!-- .element: height="30%" width="30%" -->

Kubernetes (or k8s) comes from Google's internal systems [Borg](https://github.com/SupaeroDataScience/DE/blob/master/readings/borg.pdf)

It is open source now <https://github.com/kubernetes> and used... everywhere ?

<!--v-->

### [Kubernetes](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)

![k8s](static/img/kubernetes-logo.svg)

Kubernetes manages your containers on a cluster of machine while taking care of 

- Creation, deletion, and movement of containers
- Scheduling (match containers to machines by ressources etc.)
- Scaling of containers
- Serving of containers through unified endpoints
- Monitoring and healing

<!--v-->

Kubernetes is part of [Cloud Native Computing Foundation](https://www.cncf.io/)

![cncf](static/img/cncf-landscape-logo.svg) <!-- .element: height="40%" width="40%" -->

> As part of the Linux Foundation, we provide support, oversight and direction for fast-growing, cloud native projects, including Kubernetes, Envoy, and Prometheus.

<!--v-->

[Cloud Native Computing Foundation Landscape](https://landscape.cncf.io/) 

![cncf](static/img/cncf-landscape.jpg) <!-- .element: height="50%" width="60%" -->

<!--v-->

[Cloud Native Computing Foundation Projects](https://landscape.cncf.io/)

![cncf](static/img/cncf-trail-map.png) <!-- .element: height="30%" width="30%" -->

<!--v-->

😱 😱 😱 😱

![k8s](static/img/k8s-constructs-architecture.jpg) <!-- .element: height="40%" width="40%" -->

<!--v-->

🤗 🤗 🤗

![k8s](static/img/kubernetes-architecture.png)  <!-- .element: height="40%" width="40%" -->

<!--v-->

Pods

![pods](static/img/k8s-deployment-spec.png)  <!-- .element: height="50%" width="50%" -->

<!--v-->

Pods, Nodes

![pods-nodes](static/img/k8s-networking-overview.png) <!-- .element: height="50%" width="50%" -->

<!--v-->

Endpoints

![service](static/img/k8s-service-endpoints.png) <!-- .element: height="50%" width="50%" -->

<!--v-->

Updating

![rolling](static/img/kubernetes-rolling-update.png) <!-- .element: height="50%" width="50%" -->

<!--v-->

"Declarative" programming, cloud agnostic

![declarative](static/img/k8s-declarative-config.png)

<!--v-->

"Declarative" programming : Welcome to YAML

`kubectl apply -f deployment.yaml`

![declarative](static/img/k8s-deployment-spec.png)

<!--v-->

"Declarative" programming : Welcome to YAML

`kubectl apply -f deployment.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
```

<!--v-->

![helm](static/img/helm-overview.png)  <!-- .element: height="50%" width="50%" -->

Example: <https://artifacthub.io/packages/helm/dask/dask>

<!--v-->

GCP + k8s = ❤️‍

![GKE](static/img/gke-dashboard.png) <!-- .element: height="50%" width="50%" -->

<!--v-->

![sailing](static/img/kubernetes-sailing-meme.png)

[comic](https://cloud.google.com/kubernetes-engine/kubernetes-comic/)

<!--v-->

Play with k8s

<https://www.katacoda.com/courses/kubernetes>

<https://labs.play-with-k8s.com/>

<https://github.com/yogeek/kubernetes-local-development>
