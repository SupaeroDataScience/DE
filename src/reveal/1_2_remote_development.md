---
title: Remote Development
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

### Remote Development

<!--v-->

### Why "remote development" ?

AI / Data Science = Data + Compute + Software

- Your job consist in handling huge volume of data
- Your job requires high computational resources
- You're working as a team with centralized computing platform
- You're working remotely

<!--v-->

### Key use case

![remote](https://cf-assets.www.cloudflare.com/slt3lc6tev37/yTvHLFlopPBrpiKavwp9M/0c9b06fb175472bf20f7310a67e1bdcd/access-replicated_2x--1-.png) <!-- .element: height="50%" width="50%" -->

<!--v-->

### Key use case

![remote](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5f009c59-64f4-46ff-8097-c5be8f865eaf_1616x1372.png) <!-- .element: height="40%" width="40%" -->

https://newsletter.pragmaticengineer.com/p/cloud-development-environments-why-now

<!--v-->

#### Your future daily routine

![hub](https://geohackweek.github.io/Introductory/fig/geohackweek_aws_setup.png)  <!-- .element: height="40%" width="40%" -->

Another example (more managed) [Google Colab](https://colab.research.google.com/)

<!--v-->

#### Your future daily routine

An AI-centric example, https://lightning.ai/studios

![studio](https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/work_project.png)  <!-- .element: height="40%" width="40%" -->

<!--v-->

#### Your future daily routine

![remote](https://blog.uber-cdn.com/cdn-cgi/image/width=1810,quality=80,onerror=redirect,format=auto/wp-content/uploads/2022/12/Figure-2-Devpod-overview-Remote-development-environment-@-Uber.png)  <!-- .element: height="40%" width="40%" -->

[Uber Blog describing their way of working](https://www.uber.com/en-FR/blog/devpod-improving-developer-productivity-at-uber/)

<!--v-->

### Problematics

- How to transfer code ?
- How to interact with the machines ?
- How to get access to the data ?

<!--v-->

![codespaces](https://github.blog/wp-content/uploads/2021/08/1200x630-codespaces-social.png) <!-- .element: height="50%" width="50%" -->

<!--v-->

#### [Github Codespaces](https://docs.github.com/en/codespaces/overview)

* [Github Codespaces](https://docs.github.com/en/codespaces) : A managed development environment by Microsoft Azure
* A virtual machine and a [containerized development environment](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers)
* A lot of built-in bonuses including "in-browser" connection & TCP port forwarding with reverse proxy

![](https://docs.github.com/assets/cb-79257/images/help/codespaces/port-forwarding.png)  <!-- .element: height="40%" width="40%" -->

