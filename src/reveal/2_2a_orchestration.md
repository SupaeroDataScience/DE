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

![orchestra](https://media.giphy.com/media/DPA3NUsVluONq/giphy.gif)

<!--v-->

You just deployed your ML model in production **on one machine** <!-- .element: class="fragment" data-fragment-index="1" -->

<!--v-->

#### Questions

Suppose I have a large pool of machines available

* How do I **deploy my container on all machines ?** <!-- .element: class="fragment" data-fragment-index="1" -->
* How do I **put the right containers at the right spot ?** <!-- .element: class="fragment" data-fragment-index="2" -->
* How do I **scale (up and down) to demand ?** <!-- .element: class="fragment" data-fragment-index="3" -->
* How do I **expose the http endpoints ?** <!-- .element: class="fragment" data-fragment-index="4" -->
* How do I **manage failure of containers ?** <!-- .element: class="fragment" data-fragment-index="5" -->
* How do I **update my model without downtime** <!-- .element: class="fragment" data-fragment-index="6" -->

<!--v-->

### In reality, it's much more complex...

![](static/img/modelserving_complex.png)  <!-- .element: height="50%" width="50%" -->

<!--v-->

### Orchestration

<img src="https://devopedia.org/images/article/37/6042.1530784538.jpg" alt="" style="width: 40%; height: 40%; background:none; border:none; box-shadow:none;"/>

<!--v-->

#### The next step

![](https://miro.medium.com/v2/resize:fit:4800/format:webp/1*chfFaFDHCiHCfcUAycQSHA.png)

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

![ecosystem](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F996C7D4B5AF43B6C27)

<!--v-->

![kub](https://miro.medium.com/max/1320/1*Mdj9wylSl0wqJ9sB0ENbRA.png)

<!--s-->

### Kubernetes ("Helmsman")

![helm](https://media.giphy.com/media/l0Iyj8mER3cwNqJ6o/giphy.gif)

<!--v-->

![borg](https://s3-eu-west-1.amazonaws.com/risingstack-resources/History+of+Kubernetes/borg-omega-and-kubernetes.jpg) <!-- .element: height="30%" width="30%" -->

Kubernetes (or k8s) comes from Google's internal systems [Borg](https://github.com/SupaeroDataScience/DE/blob/master/readings/borg.pdf)

It is open source now <https://github.com/kubernetes> and used... everywhere ?

<!--v-->

### [Kubernetes](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)

![k8s](https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,w_250,h_195/https://assets.ubuntu.com/v1/767f38a4-kubernetes-stacked-color.svg)

Kubernetes manages your containers on a cluster of machine while taking care of 

- Creation, deletion, and movement of containers
- Scheduling (match containers to machines by ressources etc.)
- Scaling of containers
- Serving of containers through unified endpoints
- Monitoring and healing

<!--v-->

Kubernetes is part of [Cloud Native Computing Foundation](https://www.cncf.io/)

![cncf](https://landscape.cncf.io/images/cncf-landscape-horizontal-color.svg) <!-- .element: height="40%" width="40%" -->

> As part of the Linux Foundation, we provide support, oversight and direction for fast-growing, cloud native projects, including Kubernetes, Envoy, and Prometheus.

<!--v-->

[Cloud Native Computing Foundation Landscape](https://landscape.cncf.io/) 

![cncf](https://www.civo.com/assets/public/academy/courses/kubernetes-introduction/cncf-and-its-landscapes/cncf-landscape-lg-76deb3155685ef877c983fca1eb2d6bde90598d42e0806f6f3b119f72aee3dde.jpg) <!-- .element: height="50%" width="60%" -->

<!--v-->

[Cloud Native Computing Foundation Projects](https://landscape.cncf.io/)

![cncf](https://www.cncf.io/wp-content/uploads/2020/08/CNCF_TrailMap_latest-1.png) <!-- .element: height="30%" width="30%" -->

<!--v-->

😱 😱 😱 😱

![k8s](https://platform9.com/wp-content/uploads/2019/05/kubernetes-constructs-concepts-architecture-1024x800.jpg) <!-- .element: height="40%" width="40%" -->

<!--v-->

🤗 🤗 🤗

![k8s](static/img/k8s.png)  <!-- .element: height="40%" width="40%" -->

<!--v-->

Pods

![pods](https://www.jeremyjordan.me/content/images/2019/11/deployment_spec.png)  <!-- .element: height="50%" width="50%" -->

<!--v-->

Pods, Nodes

![pods-nodes](https://matthewpalmer.net/kubernetes-app-developer/articles/networking-overview.png) <!-- .element: height="50%" width="50%" -->

<!--v-->

Endpoints

![service](https://storage.googleapis.com/static.ianlewis.org/prod/img/753/endpoints.png) <!-- .element: height="50%" width="50%" -->

<!--v-->

Updating

![rolling](static/img/rolling.png) <!-- .element: height="50%" width="50%" -->

<!--v-->

"Declarative" programming, cloud agnostic

![declarative](https://miro.medium.com/max/1126/1*bwrbghRAwtf6lEVvoJCbyQ.png)

<!--v-->

"Declarative" programming : Welcome to YAML

`kubectl apply -f deployment.yaml`

![declarative](https://www.jeremyjordan.me/content/images/2019/11/deployment_spec.png)

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

![helm](static/img/helm.png)  <!-- .element: height="50%" width="50%" -->

Example: <https://artifacthub.io/packages/helm/dask/dask>

<!--v-->

GCP + k8s = ❤️‍

![GKE](https://venturebeat.com/wp-content/uploads/2018/05/image11.png?w=1200&strip=all) <!-- .element: height="50%" width="50%" -->

<!--v-->

![sailing](static/img/sailing.png)

[comic](https://cloud.google.com/kubernetes-engine/kubernetes-comic/)

<!--v-->

Play with k8s

<https://www.katacoda.com/courses/kubernetes>

<https://labs.play-with-k8s.com/>

<https://github.com/yogeek/kubernetes-local-development>
