---
title: Cloud Computing
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

## Intro to Cloud Computing

![the office](static/img/img_7591cdb9.gif)

<!--v-->

### What is the Cloud ?

<img src="static/img/the_cloud.png" alt="xkcd" width="75%" height="50%" style="background:none; border:none; box-shadow:none;"/>

<!--v-->

![cloud](static/img/main-qimg-6a4c094bd9465389d35529b12b6caa77.webp)

<!--v-->

But it's a bit bigger...

<img src="static/img/fb_datacenter.jpg" alt="" width="25%" height="25%" style="background:none; border:none; box-shadow:none;"/>

<img src="static/img/openrack2-640x426.jpg" alt="" width="25%" height="25%" style="background:none; border:none; box-shadow:none;"/>

<img src="static/img/GM23qAAlFJW8xm4BABnMiwAAAAAAbj0JAAAD.png" alt="" width="25%" height="25%" style="background:none; border:none; box-shadow:none;"/>

(Facebook's data center & server racks)

<!--v-->

![gcloud_datacenter.png](static/img/gcloud_datacenter.png)

Google Cloud Platform datacenters locations

<!--v-->

> The cloud is a real physical place - accessed over the internet - where a service is performed for you or where your stuff is stored. Your stuff is stored in the cloud, not on your device because the cloud is not on any device; the cloud lives in datacenters. A program running on your device accesses the cloud over the internet. The cloud is infinite, accessible from anywhere, at any time

**Todd Hoff in "Explain the Cloud like I'm 10"**

<!--v-->

### What about "Cloud Computing" ?

For us the cloud is a set of *cloud providers* renting *cloud services* 

which become increasingly "abstracted" from the hardware they run on...

<!--v-->

#### Services ?

- "Renting a server" ... (this is pure "cloud computing")
- "Replicated & Secure storage space" ...
- "Autoscaling deployment of a microservice" ...

<!--v-->

<img src="static/img/AWS-Services.png" alt="" width="50%" height="50%" style="background:none; border:none; box-shadow:none;"/>

(a portion of aws services)

<!--v-->

#### How is it possible ?

![](static/img/xmagic.png)

The magic of... virtualization !

<!--v-->

#### Virtualization ?

> In computing, virtualization refers to the act of creating a virtual (rather than actual) version of something, including virtual computer hardware platforms, storage devices, and computer network resources.

Wikipedia

> Basically we are running software on "abstract hardware" which is a "portion" of a real computer ("bare metal")

<!--v-->

<img src="static/img/virtualization.png" alt="" width="75%" height="75%" style="background:none; border:none; box-shadow:none;"/>

<!--v-->

Hardware visualisation: Server Example

<img src="static/img/virtualization2.png" alt="" width="50%" height="50%" style="background:none; border:none; box-shadow:none;"/>

<!--v-->

![virtualisation](static/img/medium_86e960ee.png)

<!--v-->

#### Definitions

**Hypervisor** : A program for creating and running virtual machines. 

**Virtual Machine**: The emulated equivalent of a computer system that runs on top of another system

**Containers**: Isolated environments that share the same underlying OS & resources

<!--v-->

#### Hypervisor : KVM example (Kernel Virtual Machine)

![kvm](static/img/400px-Kernel-based_Virtual_Machine.svg.png) <!-- .element: height="30%" width="30%" -->

<!--v-->

#### Nested Hypervisors : Google Compute Engine

![gce](static/img/nested-virtualization-diagram.svg) <!-- .element: height="30%" width="30%" -->

<!--v-->

#### Consequence

![more ram](static/img/Technologically-Impaired-Duck-Where-can-I-download--More-RAM8.jpg)

> Any sufficiently advanced technology is indistinguishable from magic.

Clarke Third Law

<!--v-->

#### Hardware abstraction

- Hardware Abstraction ("download more RAM")
- Fine-grained resource allocation / sharing
- Decouple maintenance of hardware from maintenance of software

<!--v-->

#### Reliability, security...

![balancing](static/img/vm_charge_repartition.gif)

<!--s-->

### Where does it come from ?

![aws](static/img/aws-logo.png)

<!--v-->

Once upon a time...

Amazon (the e-commerce store) has "scaling" issues

![aws](static/img/jeff_bezos_big_mandate.jpg)

<!--v-->

So basically Amazon became very good at *running* scalable infrastructure as *services*

- For themselves...
- ... but also for other partners (target)

And that infrastructure is often there to answer peak load...

<!--v-->

2002-2003; The idea

> Building an infrastructure that is completely standardized, completely automated, and relied extensively on web services for things like storage 

http://blog.b3k.us/2009/01/25/ec2-origins.html

<!--v-->

Let's sell it !

![aws](static/img/ec2.png)

<!--v-->

#### How does Amazon can offer free shipping to everybody

<img src="static/img/aws_fuel.png" alt="" width="60%" height="60%" style="background:none; border:none; box-shadow:none;"/>

<!--v-->

#### How does Amazon can offer free shipping to everybody

<img src="static/img/aws_growth.png" alt="" width="60%" height="60%" style="background:none; border:none; box-shadow:none;"/>

<!--s-->

### The many layers of Cloud Computing

<!--v-->

Hybrid Cloud ? Private Cloud ? Public Cloud ?

<img src="static/img/cloud.png" alt="" width="50%" height="50%" style="background:none; border:none; box-shadow:none;"/>

<!--v-->

Cloud providers are offering services with increasing layers of abstraction...

![cloud](static/img/medium_3675ed2b.jpeg) <!-- .element: height="50%" width="50%" -->

<!--v-->

<img src="static/img/saas-vs-paas-vs-iaas.png" alt="" width="50%" height="50%" style="background:none; border:none; box-shadow:none;"/>

<!--v-->

#### Examples

- Renting a server with hard drive and storing data
- Using data storage service like google cloud storage without managing the infrastructure
- Using google drive

<!--v-->

#### Examples

- Renting a server with hard drive and storing data **IaaS**
- Using data storage service like google cloud storage without managing the infrastructure **PaaS**
- Using Dropbox **SaaS**

<!--v-->

#### Examples

- Renting a GPU farm to deploy your Large Language Model and serve it **IaaS**
- Using the HuggingFace API to serve predictions from your model **PaaS**
- Using ChatGPT **SaaS**

<!--v-->

#### It gets harder

![cloud](static/img/cloudabstraction.jpg)  <!-- .element: height="65%" width="65%" -->

<!--v-->

#### Useful analogy (1)

![paas](static/img/3-pizza-as-a-service.png)  <!-- .element: height="50%" width="50%" -->

<!--v-->

#### Useful analogy (2)

![paas2](static/img/pizzaasaservicev2.jpg)  <!-- .element: height="50%" width="50%" -->

<!--s-->

### Public Cloud Providers

<!--v-->

#### Major cloud providers

![cloud_vendors](static/img/Top-10-Cloud-Service-Providers-Globally-in-2022.jpg.webp)  <!-- .element: height="50%" width="50%" -->

<!--v-->

#### Private Cloud Stack

![privatecloud](http://1.bp.blogspot.com/-1BuI8MUh498/Uc4BOPBpChI/AAAAAAAAGjk/XWA0iYO5drA/s1028/Screen+Shot+2013-06-28+at+12.03.11+PM.png)

<!--v-->

#### AI Cloud Providers

![paperspace](static/img/medium_0de29265.png)  <!-- .element: height="50%" width="50%" -->

- https://www.paperspace.com/core
- https://lambdalabs.com/
- https://huggingface.co/hardware

<!--v-->

#### French Cloud Providers 🐓🧀🐸🇫🇷

<img src="static/img/ovhcloud.png" alt="" width="20%" height="20%" style="background:none; border:none; box-shadow:none;"/>

<img src="static/img/scaleway_logo_2018.png" alt="" width="20%" height="20%" style="background:none; border:none; box-shadow:none;"/>

<img src="static/img/3DS_OUTSCALE_Dark-Blue_RGB.png" alt="" width="20%" height="20%" style="background:none; border:none; box-shadow:none;"/>

<img src="static/img/bleu.png" alt="" width="20%" height="20%" style="background:none; border:none; box-shadow:none;"/>

- OVH went public in 2021
- Scaleway is leading the charge for AI in France (& Europe)
- Outscale is focusing on SecNumCloud
- BleuCloud is CapGemini x Orange

<!--v-->

#### US dependency ?

**Cloud Act** : a US law that allows US authorities to compel US-based tech companies to provide data stored on their servers.

Even if that data is physically located outside the United States.

**SecNumCloud** :  SecNumCloud est une qualification délivrée par l’ANSSI, autorité nationale de cybersécurité, attestant qu’un service de cloud présente un haut niveau de sécurité, adapté aux usages sensibles de l’Etat et des entreprises françaises. 

[SecNumCloud en pas si bref](https://www.linkedin.com/pulse/secnumcloud-en-pas-si-bref-vincent-strubel-505ge/)

<!--v-->

#### US dependency ?

| Project | Partners | Tech | Status |
|:---:|---|---|---|
| Bleu | Orange + Capgemini (100% French ownership), <br>Microsoft as tech partner (not shareholder) | Azure + M365 | Commercial operations launched 2024.<br>First clients include EDF, Dassault Aviation. |
| S3NS. | Thales (majority) <br>Google Cloud (minority shareholder, <24%) | GCP | SecNumCloud 3.2 obtained December 2024.<br>Offers IaaS/PaaS/CaaS |

<!--v-->

🇪🇺 GAIA-X : Cloud Federation in Europe

[https://www.data-infrastructure.eu/GAIAX/](https://www.data-infrastructure.eu/GAIAX/)

[https://www.contexte.com/article/tech/gaia-x-souverainete-cloud_150712.html](https://www.contexte.com/article/tech/gaia-x-souverainete-cloud_150712.html)

<!--v-->

#### Cloud Market Share (World)

![cloud](static/img/18819.jpeg) <!-- .element: height="40%" width="40%" -->

[source, 2025](https://www.statista.com/chart/18819/worldwide-market-share-of-leading-cloud-infrastructure-service-providers/)

<!--v-->

#### Cloud Market Share (Europe)

![europan_cloud](static/img/euro_cloud_share.png)  <!-- .element: height="40%" width="40%" -->

[source, 2025](https://www.srgresearch.com/articles/european-cloud-providers-local-market-share-now-holds-steady-at-15)

<!--v-->

#### Cloud Market Share (France)

![france](static/img/cloudshare2022.webp) <!-- .element: height="50%" width="50%" -->

[source, 2021](https://www.larevuedudigital.com/le-marche-du-cloud-concentre-en-france-entre-amazon-microsoft-et-google/)

<!--s-->

### Cloud Computing & Environment

<img src="static/img/Comparatif-DC-RVB-website-2048x1751.jpg" alt="" width="50%" height="50%" style="background:none; border:none; box-shadow:none;"/>

<!--v-->

I am not competent to say anything about this. Some sources

- The Shift Project : https://theshiftproject.org/article/deployer-la-sobriete-numerique-rapport-shift/
- Scaleway : https://www.scaleway.com/fr/leadership-environnemental/
- Google : https://cloud.google.com/sustainability
- Earth.org : https://earth.org/environmental-impact-of-cloud-computing/

<!--v-->

On "Artificial Intelligence" & sustainability, entry points

- [Power Hungry Processing: Watts Driving the Cost of AI Deployment?](https://arxiv.org/abs/2311.16863)
- [ The Environmental Impacts of AI -- Primer ](https://huggingface.co/blog/sasha/ai-environment-primer)

<!--s-->

## "Using" the Cloud

![datacenter lost](static/img/comic.png)

<!--v-->

### Cloud Computing: A technical *evolution*

- More Virtualization
- More API
- More Managed Services

<!--v-->

### Cloud Computing: A usage **revolution**

<!--v-->

#### Autonomy : access to computing power

- Outsourcing infra, maintenance, security, development of new services
- Pay-per-use with "Infinitely scalable" infrastructure
- "No need to plan out" infrastructure
  - Enabling innovation
  - Power in the hands of developpers/builders

<!--v-->

#### Changing the way we interact with hardware

We interact with cloud providers using APIs...

```bash
gcloud compute --project=deeplearningsps instances create ${INSTANCE_NAME} \
    --zone=${ZONE} \
    --machine-type=n1-standard-8 \
    --scopes=default,storage-rw,compute-rw \
    --maintenance-policy=TERMINATE \
    --image-family=ubuntu-1804-lts \
    --image-project=ubuntu-os-cloud \
    --boot-disk-size=200GB \
    --boot-disk-type=pd-standard \
    --accelerator=type=nvidia-tesla-p100,count=1 \
    --metadata-from-file startup-script=startup_script.sh
```

<!--v-->

#### Before...

![catcomputer](static/img/6b92a03c8b87aa448f8206ee57b5a4fc.jpg)

<!--v-->

#### After...

```yaml
resources:
- name: vm-created-by-deployment-manager
  type: compute.v1.instance
  properties:
    zone: us-central1-a
    machineType: zones/us-central1-a/machineTypes/n1-standard-1
    disks:
    - deviceName: boot
      type: PERSISTENT
      boot: true
      autoDelete: true
      initializeParams:
        sourceImage: projects/debian-cloud/global/images/family/debian-9
    networkInterfaces:
    - network: global/networks/default
```

<!--v-->

#### Infrastructure as Code

- Infra is now managed via text files
- Data is securely stored on storage
- So we store code + urls on git... and everything is reproducible !
- We use automated deployment tools (terraform, gcp deployment manager...)

<!--v-->

#### Pet vs Cattle

![petvscattle](static/img/pet-vs-cattle.png)

<!--v-->

#### Cloud Native Computing Foundation

![CNCF](static/img/CNCF-Logo.jpg)

<!--v-->

#### Cloud Native Computing Foundation

![CNCF](static/img/cncf-landscape-lg-76deb3155685ef877c983fca1eb2d6bde90598d42e0806f6f3b119f72aee3dde.jpg)

<!--v-->

### Let's discuss

<!--v-->

**Is using cloud computing less expensive ?**

- 👍 Depend on your {normal / peak} utilization
- 👍 Access to latest hardware without investment
- 👎 Fully utilized hardware is more expensive on the cloud
- 👎 CLOUD HYGIENE !
  - ⚠️ Watch for unused services / storage
  - ⚠️ Shutdown machines when not used
  - ⚠️ Services stack up...

<!-- .element: class="fragment" -->

<!--v-->

**Is using cloud computing more secure / safer ?**

- 👍 The best engineers in the world working on it
- 👍 Secure regions / private cloud...
- 👎 Your data somewhere in some datacenter...
- 👎 "Dependency" towards your cloud provider...

<!-- .element: class="fragment" -->

<!--s-->

### Cloud Native Culture example : Object Storage

<!--v-->

#### File Storage vs Object Storage

| Aspect | File Storage | Object Storage |
|---|---|---|
| Model | Hierarchical directories and files | Buckets and objects (flat namespace) |
| Access | Mount as network drive, POSIX (NFS/SMB) | HTTP API (REST) |
| Use case | Shared storage, legacy apps, home directories | Data lakes, ML datasets, backups |
| Scalability | Limited to file system capacity | Built with scale in mind (abstraction over the storage location) |

<!--v-->

![file](static/img/FileStorage.png)
![object](static/img/ObjectStorage.png)

<!--v-->

#### Object Storage Model

- **Bucket**: Container for objects (like a top-level folder)
- **Object**: File + metadata (stored as key-value)
- **Key**: Object path (e.g., `data/train/image_001.jpg`)

No real hierarchy, just a flat namespace with "/" in keys

<!--v-->

#### Permissions: POSIX vs Object Storage

| POSIX (files) | Object Storage |
|---------------|----------------|
| User/Group/Other | IAM policies (users, groups, service accounts) |
| rwx bits | Fine-grained: read, write, delete, list, admin |
| Per-file only | Per-bucket or per-object |
| Local to machine | Managed centrally (cloud IAM) |

Object storage enables **sharing across teams/projects** without managing OS users

<!--v-->

#### Why Object Storage for Data Science?

- **Cheap**: ~$0.02/GB/month (vs $0.10+ for disk)
- **Accessible**: HTTP API from anywhere
- **Scalable**: Petabytes without infrastructure management
- **Shareable**: Easy to share datasets across teams/machines

<!--v-->

#### Object Storage Providers

| Provider | Service | URI Format |
|----------|---------|------------|
| AWS | S3 | `s3://bucket/key` |
| GCP | GCS | `gs://bucket/key` |

Same concepts, similar APIs, different CLIs

<!--s-->

### Cloud usage, some anecdotes

<!--v-->

#### Big Tech public cloud bills

- Apple in 2019 [350m$ on AWS / year](https://www.theverge.com/2019/4/22/18511148/apple-icloud-cloud-services-amazon-aws-30-million-per-month)
- Spotify in 2018 [150m$ on GCP / year](https://www.cnbc.com/2018/03/20/spotify-will-spend-nearly-450-million-on-google-cloud-over-3-years.html)
- Lyft in 2019 [100m$ on AWS / year](https://www.cnbc.com/2019/03/01/lyft-plans-to-spend-300-million-on-aws-through-2021.html)

<!--v-->

#### Pokemon Go Launch (2016)

![pokemon](static/img/google-cloud-pokemon-go-1kwkj.max-700x700.PNG)

[source](https://cloud.google.com/blog/products/gcp/bringing-pokemon-go-to-life-on-google-cloud)

<!--v-->

#### Doctolib (2021)

![doctolib](https://miro.medium.com/max/700/0*PMcEcSFsRKEm_4yG)

[source](https://medium.com/doctolib/monday-july-12-at-doctolib-a-retrospective-9ac15c46ac19)

<!--v-->

#### Facebook October 2021 Failure

![](static/img/Facebook-outage-traffic-dropoff__cropped_.png)

https://blog.cloudflare.com/october-2021-facebook-outage/

<!--v-->

#### AWS US-EAST-1 Failure (2022)

> 13 June 2023: AWS. The largest AWS region (us-east-1) degraded heavily for 3 hours, impacting 104 AWS services. A joke says that when us-east-1 sneezes the whole world feels it, and this was true: Fortnite matchmaking stopped working, McDonalds and Burger King food orders via apps couldn’t be made, and customers of services like Slack, Vercel, Zapier and many more all felt the impact. (incident details). We did a deepdive into this incident earlier in AWS’s us-east-1 outage.

https://aws.amazon.com/message/12721/

<!--v-->

#### Links

<http://highscalability.com>

<http://highscalability.com/all-time-favorites>

[Netflix: What happens when you press play - 2017](http://highscalability.com/blog/2017/12/11/netflix-what-happens-when-you-press-play.html)

[Mind boggling statistics on Amazon Prime Day](https://aws.amazon.com/blogs/aws/amazon-prime-day-2019-powered-by-aws/)

[Scaling ChatGPT](https://newsletter.pragmaticengineer.com/p/scaling-chatgpt)

<!--s-->

## Cloud Computing & AI

<!--v-->

### All about that scale

This was in 2022,

[BLOOM: A 176B-Parameter Open-Access Multilingual Language Model](https://arxiv.org/pdf/2211.05100)

> Training BLOOM took about 3.5 months to complete and consumed 1,082,990 compute hours. Training was conducted on 48 nodes, each having 8 NVIDIA A100 80GB GPUs (a total of 384 GPUs);

<!--v-->

### All about that scale

This was 2024,

![alt text](static/img/llama.png)

https://dblalock.substack.com/p/2024-8-4-arxiv-roundup-llama-31-training

<!--v-->

### AI Distributed Computing

![](static/img/distributed_computing.png)

<!--v-->

### Stable Diffusion

![](static/img/63cf7cb6264c4050ed2ea00e_Screen_Shot_2023-01-23_at_10.37.19_PM.png) <!-- .element: height="60%" width="60%" -->

[Stable Diffusion Training Times](https://www.databricks.com/blog/stable-diffusion-2)

<!--v--> 

### AI Cloud Providers

![](static/img/4.png)  <!-- .element: height="50%" width="50%" -->

<!--v-->

## Very quick intro to MLOps

- https://huyenchip.com/machine-learning-systems-design/toc.html
- https://ml-ops.org/content/references.html


<!--v-->

![mlsystems](static/img/ml_project_flow.png) <!-- .element: height="40%" width="40%" -->

<!--v-->

MLOps Lifecycle

![mlops](static/img/mlops_lifecycle.png)  <!-- .element: height="50%" width="50%" -->

<!--v-->

MLOps Loop

![mlops](static/img/mlops-loop-en.jpg) <!-- .element: height="50%" width="50%" -->

<!--v-->

Deployment architecture

![mlops](static/img/Intro.png) <!-- .element: height="50%" width="50%" -->

<!--v-->

### Layers of "enabling technology"

![mlops](static/img/mlopsinfra.png) <!-- .element: height="75%" width="75%" -->

<!--v-->

### A full workflow 

![vertex](static/img/end-to-end-mlops-on-vertex-ai.png)

<!--v-->

### The need for tech to orchestrate ML workflows

![](static/img/anyscale.png)  <!-- .element: height="50%" width="50%" -->

(And dask !)

<!--s-->

## What about me ?

What does it mean for YOU ?

![me](static/img/img_2190bc5d.gif)

<!--v-->

<img src="static/img/mlroles2.png" alt="" width="50%" height="50%" style="background:none; border:none; box-shadow:none;"/>

<!--v-->

<img src="static/img/mlroles.png" alt="" width="50%" height="50%" style="background:none; border:none; box-shadow:none;"/>

<!--v-->

#### Your mileage may vary

depending on:

- Your company
- Your role

but you will "deal with" cloud computing one way or another !

<!--v-->

### Personal Experience

![gcp](static/img/infra_army_of_one.png)
