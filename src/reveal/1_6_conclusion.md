---
title: Recap & Conclusion
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

## Wrapup

<!--v-->

### Why this class

* "General Knowledge" about cloud computing, docker, etc.
* "Pointers" to look at if you need them later
* "First experience" in manipulating very useful tools
* Mindset of "cloud computing"

<!--v-->

### Challenges

🧰 class about tooling ... 

💡 it will make sense  ... <!-- .element: class="fragment" data-fragment-index="1" -->

🔮 six months from now !   <!-- .element: class="fragment" data-fragment-index="2" -->

<!--v-->

### Why doesn't it work every time

That's the cloud for you: It depends on your environment, the network etc.

We try to abstract it with "remote development" (think codespaces)

It's all very new : two years ago, codespaces didn't exist !

<!--v-->

Remember the IT matrix from hell ?

![matrix-from-hell](https://pointful.github.io/docker-intro/docker-img/the-matrix-from-hell.png)

<!--v-->

The 🔥 **ISAE HYPERCUBE FROM HELL** 🔥

Consider the following variables:

* in class or at home
* laptop OS: Windows 10, Linux, MacOS, WSL for Linux, Linux VM
* web browser: Chrome, Firefox, Safari, with more or less adblocks etc.
* wi-fi network: Own 4G, own network, ISAE-EDU, eduroam
* Google Cloud SDK installed: yes, no
* proficiency with CLI/Terminal: high, medium, low

Compute the number of combinations. It's > to the number of students

<!--v-->

That's real life...

![engineering](static/img/elon.png)

<!--v-->

If you had to remember only one thing

![rick-morty](https://pbs.twimg.com/media/EUMLxNXWAAE6VfI.jpg) <!-- .element: height="40%" width="40%" -->

<!--s-->

### Take-away for Cloud Computing

<!--v-->

![vm](static/img/virtualization.png) <!-- .element: height="50%" width="50%" -->

<!--v-->

![vm](https://miro.medium.com/max/10698/1*wE7TrQmFyRTDwh6VpbkbMQ.png)  <!-- .element: height="50%" width="50%" -->

<!--v-->

![cloud](https://miro.medium.com/max/541/1*Ktb-8ccVdwGSUkf_2trstA.jpeg) <!-- .element: height="50%" width="50%" -->

<!--v-->

![cloud](https://www.catapultsystems.com/wp-content/uploads/2020/03/pizza-model-vert.jpeg)  <!-- .element: height="50%" width="50%" -->

<!--v-->

![cloud](https://cdn.statcdn.com/Infographic/images/normal/18819.jpeg) <!-- .element: height="50%" width="50%" -->

<!--v-->

Cloud, technical evolution, usage revolution

![petcattle](static/img/pet-vs-cattle.png)

<!--v-->

#### SSH Tunnel, Port Forwarding

> In computer networking, **a port is a communication endpoint**. At the software level, within an operating system, a port is a logical construct that identifies a specific process or a type of network service. **A port is identified for each transport protocol and address combination** by a 16-bit unsigned number, known as the port number. The most common transport protocols that use port numbers are the Transmission Control Protocol (TCP) and the User Datagram Protocol (UDP).

[Wikipedia](https://en.wikipedia.org/wiki/Port_(computer_networking))

<!--v-->

#### Examples of protocols & usual ports

Examples

* SSH on port 22
* HTTP on port 80
* HTTPS on port 443

http apps can serve content over specific ports

Example

* Jupyter default is 8888 (that's why you open http://localhost:8888)

<!--v-->

#### SSH Tunnels

We usually connect to web app using `http://{ip}:{port}`

😨 but what if the machine is not connected to the internet ?

➡️ Enter SSH with port forwarding

![ssh-tunnel](https://iximiuz.com/ssh-tunnels/local-port-forwarding-2000-opt.png)  <!-- .element: height="50%" width="50%" -->

[Visual guide](https://iximiuz.com/en/posts/ssh-tunnels/)

<!--v-->

#### [Github Codespaces](https://docs.github.com/en/codespaces/overview)

* [Github Codespaces](https://docs.github.com/en/codespaces) : A managed development environment by Microsoft Azure
* A virtual machine and a [containerized development environment](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers)
* A lot of built-in bonuses including "in-browser" connection & TCP port forwarding with reverse proxy

![](https://docs.github.com/assets/cb-79257/images/help/codespaces/port-forwarding.png)  <!-- .element: height="50%" width="50%" -->


<!--v-->

#### Remote Development : Your future daily routine

![remote](https://blog.uber-cdn.com/cdn-cgi/image/width=1810,quality=80,onerror=redirect,format=auto/wp-content/uploads/2022/12/Figure-2-Devpod-overview-Remote-development-environment-@-Uber.png)  <!-- .element: height="50%" width="50%" -->

[Uber Blog describing their way of working](https://www.uber.com/en-FR/blog/devpod-improving-developer-productivity-at-uber/)

<!--v-->

#### Tunnels of tunnels

* Some of you did Local Machine -> (browser) -> Codespace -> (ssh) -> VM -> Jupyterlab on port 8888
* With port transfers !
* What happens when you go to `http://(url-generated-by-codespaces):8888` in this case ?

![tunnelception](static/img/codespaceception.png)

<!--s-->

### Take-away for Containers

![](https://pointful.github.io/docker-intro/docker-img/docker.png)   <!-- .element: height="30%" width="30%" -->

[Docker](https://www.docker.com/)

<!--v-->

![shipping](https://pointful.github.io/docker-intro/docker-img/shipping-container-for-code.png)

<!--v-->

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*qUbRuYlBSrOaXXa_UO6pDg.png)

<!--v-->

![docker](static/img/buildshiprun.png) <!-- .element: height="70%" width="70%" --> 

<!--v-->

![container-vm](https://pointful.github.io/docker-intro/docker-img/containers-vs-vms.png) <!-- .element: height="70%" width="70%" -->

<!--v-->

![docker](static/img/containers_vs_vm.png)  <!-- .element: height="70%" width="70%" -->

<!--v-->

workflow

![docker](static/img/docker-jworkflow.jpg) <!-- .element: height="70%" width="70%" -->

<!--v-->

containers is not magic

![devops](https://miro.medium.com/max/1810/1*bB-rHCq8L-g5xzWLqsy3EQ.png)

<!--v-->

containers for data science

![mlsystems](https://ml-ops.org/img/mlops-phasen.jpg)  <!-- .element: height="50%" width="50%" -->

<!--v-->

### BE : Why ?

![](https://miro.medium.com/max/1400/1*b-NfGtOQXsqIBCLpckP66Q.png)  <!-- .element: height="70%" width="70%" -->

<!--v-->

### BE : Where the f*** am I ?

![](static/img/tunnelception2.png) <!-- .element: height="70%" width="70%" -->

<!--v-->

![](https://miro.medium.com/v2/resize:fit:750/format:webp/1*eONPUauKcQRHGHcrGxeftg.png)  <!-- .element: height="70%" width="70%" -->

<!--v-->

### More about docker

* Containers really shine when you are deploying multi-containers applications
  - [This tutorial on microservices w/ Compose](https://training.play-with-docker.com/microservice-orchestration/)
* Containers really shine when you are in a cluster world
  - [Docker swarm](https://training.play-with-docker.com/swarm-stack-intro/)
* Orchestration & Scheduling
  - [Read this excellent Kubernetes comic !](https://cloud.google.com/kubernetes-engine/kubernetes-comic/)

<!--s-->

### Take-away for Deployment & Orchestration

<!--v-->

- You can use docker to package & a ML model
- Usually we make "webapps" that communicate through "rest APIs"
- [streamlit](https://streamlit.io) may be very useful later in your life

<!--v-->

Orchestration is the "management" part of Containers

It tries to answer the following questions

* How do I **deploy my container** ?
* How do I **put the right containers at the right spot** ?
* How do I **scale (up and down) to demand** ?
* How do I **expose the http endpoints** ?
* How do I **manage failure of containers** ? 
* How do I **update my model without downtime** ?

<!--v-->

Kubernetes is **one** of the solutions (the hardest) available to you

Read this [comic](https://cloud.google.com/kubernetes-engine/kubernetes-comic/) 

Learn more on the Data Distribution class !

<!--v-->

Should you learn kubernetes ?

https://huyenchip.com/2021/09/13/data-science-infrastructure.html

<!--s-->

## The End

![end](https://media.giphy.com/media/l49FqlUguNsGDNCGk/giphy.gif)
