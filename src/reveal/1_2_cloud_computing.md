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

![the office](https://media.giphy.com/media/5wWf7H89PisM6An8UAU/giphy.gif)

<!--v-->

### What is the Cloud ?

<img src="https://imgs.xkcd.com/comics/the_cloud.png" alt="xkcd" width="75%" height="50%" style="background:none; border:none; box-shadow:none;"/>

<!--v-->

![cloud](https://qph.fs.quoracdn.net/main-qimg-6a4c094bd9465389d35529b12b6caa77.webp)

<!--v-->

But it's a bit bigger...

<img src="static/img/fb_datacenter.jpg" alt="" width="25%" height="25%" style="background:none; border:none; box-shadow:none;"/>

<img src="https://cdn.arstechnica.net/wp-content/uploads/2013/02/openrack2-640x426.jpg" alt="" width="25%" height="25%" style="background:none; border:none; box-shadow:none;"/>

<img src="https://engineering.fb.com/wp-content/uploads/2015/05/GM23qAAlFJW8xm4BABnMiwAAAAAAbj0JAAAD.png" alt="" width="25%" height="25%" style="background:none; border:none; box-shadow:none;"/>

(Facebook's data center & server racks)

<!--v-->

![datacenters](https://cloud.google.com/images/locations/regions.png)

Google Cloud Platform datacenters locations

<!--v-->

> The cloud is a real physical place - accessed over the internet - where a service is performed for you or where your stuff is stored. Your stuff is stored in the cloud, not on your device because the cloud is not on any device; the cloud lives in datacenters. A program running on your device accesses the cloud over the internet. The cloud is infinite, accessible from anywhere, at any time

**Todd Hoff in "Explain the Cloud like I'm 10"**

<!--s-->

### What about "Cloud Computing" ?


For us the cloud is a set of *cloud providers* renting *cloud services* 

which become increasingly "abstracted" from the hardware they run on...

<!--v-->

#### Services ?

- "Renting a server" ... (this is pure "cloud computing")
- "Replicated & Secure storage space" ...
- "Autoscaling deployment of a microservice" ...

<!--v-->

<img src="https://www.matthewb.id.au/cloud/images/AWS-Services.png" alt="" width="50%" height="50%" style="background:none; border:none; box-shadow:none;"/>

(a portion of aws services)

<!--v-->

#### How is it possible ?

![](https://blog.findthatlead.com/en/wp-content/uploads/2016/11/xmagic.jpg.pagespeed.ic.IbOWzrWHcR.jpg)

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

![vritualization](https://miro.medium.com/max/10698/1*wE7TrQmFyRTDwh6VpbkbMQ.png)

<!--v-->

#### Definitions

**Hypervisor** : A program for creating and running virtual machines. 

**Virtual Machine**: The emulated equivalent of a computer system that runs on top of another system

**Containers**: Isolated environments that share the same underlying OS & resources

<!--v-->

#### Hypervisor : KVM example (Kernel Virtual Machine)

![kvm](https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Kernel-based_Virtual_Machine.svg/400px-Kernel-based_Virtual_Machine.svg.png)

<!--v-->

#### Nested Hypervisors : Google Compute Engine

![gce](https://cloud.google.com/compute/images/nested-virtualization-diagram.svg)

<!--v-->

#### Consequence

![more ram](https://i.kym-cdn.com/photos/images/newsfeed/000/038/431/Technologically-Impaired-Duck-Where-can-I-download--More-RAM8.jpg)

> Any sufficiently advanced technology is indistinguishable from magic.

Clarke Third Law

<!--v-->

#### Hardware abstraction

- Hardware Abstraction ("download more RAM")
- Fine-grained resource allocation / sharing
- Decouple maintenance of hardware from maintenance of software

<!--v-->

#### Reliability, security...

![balancing](https://yogeek.github.io/enseignement/Introduction_Virtualisation_CloudComputing/img/vm_charge_repartition.gif)

<!--s-->

### Where does it come from ?

![aws](https://blog.scottlogic.com/dsmith/assets/featured/aws-logo.png)

<!--v-->

Once upon a time...

Amazon (the e-commerce store) has "scaling" issues

![aws](https://cdn.chiefmartec.com/wp-content/uploads/2016/11/jeff_bezos_big_mandate.jpg)

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

![cloud](https://miro.medium.com/max/541/1*Ktb-8ccVdwGSUkf_2trstA.jpeg) <!-- .element: height="50%" width="50%" -->

<!--v-->

<img src="https://blogs.bmc.com/wp-content/uploads/2017/09/saas-vs-paas-vs-iaas.png" alt="" width="50%" height="50%" style="background:none; border:none; box-shadow:none;"/>

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

#### Useful analogy

![cloud](static/img/pizzaasaservicev2.jpg)  <!-- .element: height="65%" width="65%" -->


<!--s-->

### Public Cloud Providers

<!--v-->

![cloud_vendors](https://dgtlinfra.com/wp-content/uploads/2022/06/Top-10-Cloud-Service-Providers-Globally-in-2022.jpg.webp)  <!-- .element: height="50%" width="50%" -->

<!--v-->

AI Cloud Providers

![paperspace](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*vuacjjmtbLQEoXoIbbFVNQ.png)  <!-- .element: height="50%" width="50%" -->

- https://www.paperspace.com/core
- https://lambdalabs.com/
- https://huggingface.co/hardware

<!--v-->

🐓🧀🐸🇫🇷

<img src="https://www.comptoir-hardware.com/images/stories/_logos/ovhcloud.png" alt="" width="20%" height="20%" style="background:none; border:none; box-shadow:none;"/>

<img src="static/img/scaleway_logo_2018.png" alt="" width="20%" height="20%" style="background:none; border:none; box-shadow:none;"/>

<img src="https://fr.outscale.com/wp-content/uploads/2018/08/3DS_OUTSCALE_Dark-Blue_RGB.png" alt="" width="20%" height="20%" style="background:none; border:none; box-shadow:none;"/>

<img src="https://cloud.orange.com/ui/app/static/assets/brand/logo_header_login.png" alt="" width="20%" height="20%" style="background:none; border:none; box-shadow:none;"/>

OVH went public in 2021

Scaleway is leading the charge for AI in France (& Europe)

<!--v-->

🐓🧀🐸🇫🇷

[Thales Cloud Souverain](https://thales-group.prezly.com/thales-et-google-cloud-annoncent-un-partenariat-strategique-pour-developper-conjointement-un--cloud-de-confiance--en-france#)

[OVH x Google Cloud](https://corporate.ovhcloud.com/fr/newsroom/news/ovhcloud-and-google-cloud-announce-strategic-partnership-co-build-trusted-cloud-solution-europe/)

[Scaleway et l'IA](https://www.lemonde.fr/economie/article/2023/09/26/xavier-niel-annonce-des-investissements-strategiques-dans-l-ia_6191008_3234.html)

<!--v-->

🇪🇺 GAIA-X : Cloud Federation in Europe

[https://www.data-infrastructure.eu/GAIAX/](https://www.data-infrastructure.eu/GAIAX/)

[https://www.contexte.com/article/tech/gaia-x-souverainete-cloud_150712.html](https://www.contexte.com/article/tech/gaia-x-souverainete-cloud_150712.html)

<!--v-->

![cloud](https://cdn.statcdn.com/Infographic/images/normal/18819.jpeg) <!-- .element: height="50%" width="50%" -->

<!--v-->

For France, 
![france](static/img/cloudshare2022.webp) <!-- .element: height="50%" width="50%" -->

[source, 2021](https://www.larevuedudigital.com/le-marche-du-cloud-concentre-en-france-entre-amazon-microsoft-et-google/)

<!--s-->

### Cloud Computing & Environment

<img src="https://images-www.scaleway.com/wp-content/uploads/2020/10/22094354/Comparatif-DC-RVB-website-2048x1751.jpg" alt="" width="50%" height="50%" style="background:none; border:none; box-shadow:none;"/>

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

![catcomputer](https://i.pinimg.com/originals/6b/92/a0/6b92a03c8b87aa448f8206ee57b5a4fc.jpg)

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

### Let's discuss

<!--v-->

**Is using cloud computing less expensive ?**

- 👍 Depend on your {normal / peak} utilization
- 👍 Access to latest hardware without investment
- 👎 Fully utilized hardware is more expensive on the cloud
- 👎 CLOUD HYGIENE !
  - Watch for unused services / storage
  - Shutdown machines when not used
  - Services stack up...

<!-- .element: class="fragment" -->

<!--v-->

**Is using cloud computing more secure / safer ?**

- 👍 The best engineers in the world working on it
- 👍 Secure regions / private cloud...
- 👎 Your data somewhere in some datacenter...
- 👎 "Dependency" towards your cloud provider...

<!-- .element: class="fragment" -->

<!--s-->

### Cloud usage, some anecdotes

<!--v-->

#### Big Tech public cloud bills

- Apple in 2019 [350m$ on AWS / year](https://www.theverge.com/2019/4/22/18511148/apple-icloud-cloud-services-amazon-aws-30-million-per-month)
- Spotify in 2018 [150m$ on GCP / year](https://www.cnbc.com/2018/03/20/spotify-will-spend-nearly-450-million-on-google-cloud-over-3-years.html)
- Lyft in 2019 [100m$ on AWS / year](https://www.cnbc.com/2019/03/01/lyft-plans-to-spend-300-million-on-aws-through-2021.html)

<!--v-->

#### Pokemon Go Launch (2016)

![pokemon](https://storage.googleapis.com/gweb-cloudblog-publish/images/google-cloud-pokemon-go-1kwkj.max-700x700.PNG)

[source](https://cloud.google.com/blog/products/gcp/bringing-pokemon-go-to-life-on-google-cloud)

<!--v-->

#### Doctolib (2021)

![doctolib](https://miro.medium.com/max/700/0*PMcEcSFsRKEm_4yG)

[source](https://medium.com/doctolib/monday-july-12-at-doctolib-a-retrospective-9ac15c46ac19)

<!--v-->

#### Facebook October 2021 Failure

![](https://upload.wikimedia.org/wikipedia/commons/2/26/Facebook-outage-traffic-dropoff_%28cropped%29.png)

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

<!--s-->

## Cloud Computing & AI

<!--v-->

### All about that scale

This was in 2022,

[BLOOM: A 176B-Parameter Open-Access Multilingual Language Model](https://arxiv.org/pdf/2211.05100)

> Training BLOOM took about 3.5 months to complete and consumed 1,082,990 compute hours. Training was conducted on 48 nodes, each having 8 NVIDIA A100 80GB GPUs (a total of 384 GPUs);

<!--v-->

### All about that scale

This is 2024,

![alt text](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F06b6c30c-ad4e-48b8-a506-328b16529a66_2390x570.png)

https://dblalock.substack.com/p/2024-8-4-arxiv-roundup-llama-31-training 

<!--v-->

### AI Distributed Computing

![](static/img/distributed_computing.png)

<!--v-->

### Stable Diffusion

![](https://assets-global.website-files.com/61fd4eb76a8d78bc0676b47d/63cf7cb6264c4050ed2ea00e_Screen%20Shot%202023-01-23%20at%2010.37.19%20PM.png) <!-- .element: height="60%" width="60%" -->

[Stable Diffusion Training Times](https://www.mosaicml.com/blog/training-stable-diffusion-from-scratch-costs-160k)

<!--v--> 

### AI Cloud Providers

![](https://salesforceventures.com/wp-content/uploads/2024/03/4.png)  <!-- .element: height="50%" width="50%" -->

<!--v-->

## Very quick intro to MLOps

- https://huyenchip.com/machine-learning-systems-design/toc.html
- https://ml-ops.org/content/references.html


<!--v-->

![mlsystems](https://huyenchip.com/machine-learning-systems-design/assets/ml_project_flow.png) <!-- .element: height="40%" width="40%" -->

<!--v-->

MLOps Lifecycle

![mlops](static/img/mlops_lifecycle.png)  <!-- .element: height="50%" width="50%" -->

<!--v-->

MLOps Loop

![mlops](https://ml-ops.org/img/mlops-loop-en.jpg) <!-- .element: height="50%" width="50%" -->

<!--v-->

Deployment architecture

![mlops](https://cdn.analyticsvidhya.com/wp-content/uploads/2024/07/Intro.png) <!-- .element: height="50%" width="50%" -->

<!--v-->

### Layers of "enabling technology"

![mlops](static/img/mlopsinfra.png) <!-- .element: height="75%" width="75%" -->

<!--v-->

### A full workflow 

![vertex](https://www.royalcyber.com/blog/wp-content/uploads/2022/05/end-to-end-mlops-on-vertex-ai.png)

<!--v-->

### The need for tech

![](static/img/anyscale.png)  <!-- .element: height="50%" width="50%" -->

And dask !

<!--s-->

## What about me ?

What does it mean for YOU ?

![me](https://media.giphy.com/media/cRKRlRJkEmoxglbufw/giphy.gif)

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
