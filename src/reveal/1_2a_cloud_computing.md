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

<!--s-->

### What is the Cloud ?

<img src="https://imgs.xkcd.com/comics/the_cloud.png" alt="xkcd" width="75%" height="50%" style="background:none; border:none; box-shadow:none;"/>

<!--v-->

![cloud](https://qph.fs.quoracdn.net/main-qimg-6a4c094bd9465389d35529b12b6caa77.webp)

<!--v-->

But it's a bit bigger...

<img src="static/img/fb_datacenter.jpg" alt="" width="30%" height="30%" style="background:none; border:none; box-shadow:none; float:left;margin:0 10px 0 20px;"/>

<img src="https://www.datacenterknowledge.com/sites/datacenterknowledge.com/files/wp-content/uploads/2013/06/lulea-rows.jpg" alt="" width="25%" height="25%" style="background:none; border:none; box-shadow:none;"/>

<img src="https://www.datacenterknowledge.com/sites/datacenterknowledge.com/files/wp-content/uploads/2013/06/fb-lulea-external-fans.jpg" alt="" width="25%" height="25%" style="background:none; border:none; box-shadow:none;"/>

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

![cloud](https://lh3.googleusercontent.com/Zpw-v4ZOiAkbLm9ARSl68tGaZFYsFsz1ABwRbl8Cj_ozj12jCTPmgVGKBARz3Xwum1CUsMQ7Hog=e14-rj-sc0xffffff-h2000-w2000)  <!-- .element: height="50%" width="50%" -->

<!--v-->

![cloud](https://www.catapultsystems.com/wp-content/uploads/2020/03/pizza-model-vert.jpeg)  <!-- .element: height="50%" width="50%" -->


<!--s-->

### Public Cloud Providers

<!--v-->

![cloud_vendors](https://yogeek.github.io/enseignement/Introduction_Virtualisation_CloudComputing/img/cloud_vendors.jpg)  <!-- .element: height="50%" width="50%" -->

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

<img src="static/img/marketshare.png" alt="" width="50%" height="50%" style="background:none; border:none; box-shadow:none;"/>

<!--v-->

![france](static/img/cloudshare2022.webp) <!-- .element: height="50%" width="50%" -->

![source](https://www.larevuedudigital.com/le-marche-du-cloud-concentre-en-france-entre-amazon-microsoft-et-google/)

<!--s-->

### Cloud Computing & Environment

<img src="https://images-www.scaleway.com/wp-content/uploads/2020/10/22094354/Comparatif-DC-RVB-website-2048x1751.jpg" alt="" width="50%" height="50%" style="background:none; border:none; box-shadow:none;"/>

<!--v-->

I am not competent to say anything about this. Some sources

- The Shift Project : https://theshiftproject.org/article/deployer-la-sobriete-numerique-rapport-shift/
- Scaleway : https://www.scaleway.com/fr/leadership-environnemental/
- Google : https://cloud.google.com/sustainability
- Earth.org : https://earth.org/environmental-impact-of-cloud-computing/
