---
title: Google Cloud Platform
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

# Google Cloud Platform

![gcp](https://cloud.orange-business.com/wp-content/uploads/2020/11/logo-google-cloud-platform.png)  <!-- .element: height="40%" width="40%" -->

<!--v-->

- One of the main cloud provider
- Behind AWS in SaaS (serverless...)
- More "readable" product line (for a Cloud Provider...)
- Very good "virtual machine" management  
  * per second billing
  * fine-grained resource allocation

<!--v-->

![gcp](https://www.turbogeek.co.uk/wp-content/uploads/2019/02/word-image-4.png
)  <!-- .element: height="40%" width="40%" -->

<!--v-->

<img src="https://raw.githubusercontent.com/gregsramblings/google-cloud-4-words/master/Poster-medres.png" alt="" width="50%" height="50%" style="background:none; border:none; box-shadow:none;"/>

[GCP Services in 4 words or less](https://googlecloudcheatsheet.withgoogle.com/)

<!--v-->

### Concepts

<!--v-->

#### Zones and Regions

![](https://cloud.google.com/docs/images/overview/regions-zones.svg)

<!--v-->

#### Projects

![](https://cloud.google.com/docs/images/overview/console-ids.png)

- Access (Enabling API/Services)
- Ressources (Quota by project)
- Networking
- Billing

<!--v-->

#### Concepts: Identity and Access Management (IAM)

![iam](https://miro.medium.com/max/638/0*kGyUfNWZCk78hmPU.)

<!--v-->

#### Main Products we are going to be looking at

- Google Compute Engine (virtual machine solutions)
- Google Cloud Storage (storage solutions)

<!--v-->

#### Google Compute Engine (GCE)

- The VM solution for GCP
- Images: Boot disks for VM instances
    example:  `ubuntu-1804`
- Machine Types: Ressources available to your instance
    example: `n1-standard-8` (8 vCPU, 30 Gb RAM)
- Storage Options: "Attached disk" that can persist once the instance is destroyed... can be HDD, SDD...
- Preemptible: "Spot instances" on AWS", cheap but can be killed any minute by GCP

<!--v-->

#### Google Cloud Storage (GCS)

- Cheaper storage than persistent disks
- Can be shared between multiple instances / zones
- Higher latency
- Several types of storage (w/ different r/w costs & performance)
- Data is stored in "buckets" **whose name are globally unique**

<!--v-->

#### Interacting with GCP: The Console

<img src="https://cloud.google.com/docs/images/overview/console.png" alt="" width="50%" height="50%" style="background:none; border:none; box-shadow:none;"/>

<https://console.cloud.google.com>

<!--v-->

#### Interacting with GCP: SDK & Cloud Shell

- Using the gcloud CLI: https://cloud.google.com/sdk/install
- Using Google Cloud Shell: A small VM instance you can connect to with your browser (that we won't use)

![](https://cloud.google.com/shell/docs/images/cloud-shell-gcloud.gif)

<!--s-->

### Self-paced hands-on

![student](https://media.giphy.com/media/KCqO4k31TnkC2pT5LY/giphy.gif)

<!--v-->

#### Objectives

- ✅ Discover GitHub Codespace
- ✅ Create your GCP account, configure your credentials
- Create your first VMs and connect to it via SSH
    - Learn to use Tmux for detachable SSH sessions
- Interact with Google Cloud Storage
- End to End example : 
    - Write code in your codespace
    - Transfer it to your GCE instance
    - Run the code, it produces a model
    - Transfer the model weights to google cloud storage
    - Get it back from your codespace
- Bonus content
    - Managed SQL
    - Infrastructure as code

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

😨 but what if the machine is not available from the public internet / local network ?

➡️ Enter SSH with port forwarding

![ssh-tunnel](https://iximiuz.com/ssh-tunnels/local-port-forwarding-2000-opt.png)  <!-- .element: height="50%" width="50%" -->

[Visual guide](https://iximiuz.com/en/posts/ssh-tunnels/)

<!--v-->

#### Tunnels of tunnels

* Some of you did Local Machine -> (browser) -> Codespace -> (ssh) -> VM -> Jupyterlab on port 8888
* With port transfers !
* What happens when you go to `http://(url-generated-by-codespaces):8888` in this case ?

![tunnelception](static/img/codespaceception.png)

<!--v-->

#### Demo
