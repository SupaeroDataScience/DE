# Kubernetes: Zero to Jupyterhub using Google Kubernetes Engine

## What is JupyterHub

JupyterHub brings the power of notebooks to groups of users. It gives users access to computational environments and resources without burdening the users with installation and maintenance tasks. Users - including students, researchers, and data scientists - can get their work done in their own workspaces on shared resources which can be managed efficiently by system administrators.

JupyterHub runs in the cloud or on your own hardware, and makes it possible to serve a pre-configured data science environment to any user in the world. It is customizable and scalable, and is suitable for small and large teams, academic courses, and large-scale infrastructure.
Key features of JupyterHub

Customizable - JupyterHub can be used to serve a variety of environments. It supports dozens of kernels with the Jupyter server, and can be used to serve a variety of user interfaces including the Jupyter Notebook, Jupyter Lab, RStudio, nteract, and more.

* Flexible - JupyterHub can be configured with authentication in order to provide access to a subset of users. Authentication is pluggable, supporting a number of authentication protocols (such as OAuth and GitHub).

* Scalable - JupyterHub is container-friendly, and can be deployed with modern-day container technology. It also runs on Kubernetes, and can run with up to tens of thousands of users.

* Portable - JupyterHub is entirely open-source and designed to be run on a variety of infrastructure. This includes commercial cloud providers, virtual machines, or even your own laptop hardware.

The foundational JupyterHub code and technology can be found in the JupyterHub repository. This repository and the JupyterHub documentation contain more information about the internals of JupyterHub, its customization, and its configuration.

## Zero to Jupyterhub using Kubernetes

![jupyterhub](https://zero-to-jupyterhub.readthedocs.io/en/latest/_static/logo.png)

JupyterHub allows users to interact with a computing environment through a webpage. As most devices have access to a web browser, JupyterHub makes it is easy to provide and standardize the computing environment of a group of people (e.g., for a class of students or an analytics team).

This project will help you set up your own JupyterHub on a cloud and leverage the clouds scalable nature to support large groups of users. Thanks to Kubernetes, we are not tied to a specific cloud provider.

## Instructions

* [Go here](https://zero-to-jupyterhub.readthedocs.io/en/latest/) and follow the instructions

* Use [Google Kubernetes Engine](https://zero-to-jupyterhub.readthedocs.io/en/latest/google/step-zero-gcp.html) to setup your cluster

!!! info
    You will use the same method later in the year to [setup a Dask Kubernetes cluster using helm](https://docs.dask.org/en/latest/setup/kubernetes-helm.html)

* Give some people the public IP of your cluster so that they can connect to it... try to make it scale !
