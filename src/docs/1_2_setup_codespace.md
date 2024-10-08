Remote Development hands-on

## 1. Abstract

!!! abstract
    In this hands on you will start to manipulate a Github Codespace remote development environment to get familiar about manipulating code and data not stored in your computer
    We will also discover streamlit which is a python library used to build frontend, and discover how to preview some things from the github codespace to your machine

!!! warning
    Some things may only work on **eduroam** or in 4G...
    Some things may only works on Google Chrome

!!! warning
    Don't forget to shutdown everything when you're done !

!!! note
    When the TP says to replace "{something}" with a name, don't include the brackets so write “yourname"

## 1. Early Setup : Google Cloud Platform

In order to anticipate for the next session, you will each create a Google Cloud Platform account and project using the student credits given this year,

We will do the Google Cloud Platform class next week, however by doing this now we will gain precious time in the next class

[Overview link](https://cloud.google.com/docs/overview)

* Create an account within [Google cloud Platform](https://console.cloud.google.com) using your ISAE e-mail
* Use the code given by Dennis to redeem your free credits
* You should have a [free tier](https://cloud.google.com/free) available to you as well as coupons
* From [the interface](https://console.cloud.google.com) you should [create a project](https://cloud.google.com/resource-manager/docs/creating-managing-projects) with a name of your choice (it is recommended to put for example sdd2425-yourname so that it is clear)

## 2. My first "Virtual Machine", Github Codespaces

First, you will need a [GitHub](https://github.com/) account. You should already have one, otherwise create one.

### Intro to Github Codespaces

* [Github Codespaces](https://github.com/features/codespaces) is a "managed VM" made available to develop without needing to configure locally your environment.
* Compared to configured a VM by yourself, this one comes loaded with developer tools, and thus is faster to use,
* You have a free tier of 60 CPU hours / months and some disk space
* You pay for the CPI when the VM is ON and for the disk when the codespace is create

Have a look at the overview : [https://docs.github.com/en/codespaces/overview](https://docs.github.com/en/codespaces/overview) 

!!! question
    * Can you describe it with your own words ?
    * How would ChatGPT (or any LLM) describe it ?

!!! note
    Google Cloud has a similar service with Google Cloud Shell but since Codespaces is way more powerful, we will be using that

### Create your codespace and connect to it

Go to [https://github.com/fchouteau/isae-cloud-computing-codespace](https://github.com/fchouteau/isae-cloud-computing-codespace)

![](slides/static/img/codespacefchouteau.png)

* Click on the top left corner for a new codespace
* It should launch a browser with a vscode
* Launch a terminal using the top right menu

**If that does not work,** go to [https://github.com/github/codespaces-blank](https://github.com/github/codespaces-blank) and create a codespace from there

![](slides/static/img/codespacesblank.png)

You should arrive to a VScode instance

![](slides/static/img/codespacevscode.png)

!!! question
    * Where is it running ?

If you go to the core page of [https://github.com/codespaces](https://github.com/codespaces) you should see your codespace running

![img.png](slides/static/img/codespace.png)

### Explore github codespaces

[Github Codespace Getting Started](https://docs.github.com/en/codespaces/getting-started)

Identify the following features in the interface

    Code editor (e.g., VS Code)
    Terminal
    File explorer
    Debugging tools (e.g., breakpoints, console output)

You can then carry these commands in order to get a feel of the "computer" behind

* Check available disk space

??? note "Bash command to run"
    `df -h`

* Check the OS name

??? note "Bash command to run"
    `cat /etc/os-release`

* Check the CPU model

??? note "Bash command to run"
    `cat /proc/cpuinfo`

* This is the hardware model... how many cores do you have available ? Which amount of RAM ?

??? note "Help"
    `htop` will give you your current usage and available cores, or you can do `nproc`

* Try and upload a file from your computer to the codespace by right clicking on the file explorer on the left

* Create a new file and write a simple python "Hello World", then execute it from the terminal

### A demo of codespace port forwarding / web preview

* In your codespace, run `jupyter lab` to launch the jupyter lab installed in it
* Check the "port" preview : It should have a new entry with the 8888 port. If not, create it manually
* Click on open in browser
* Copy the token from your terminal to the web browser
* You are new in a jupyterlab hosted on your github codespace VM !

!!! question
    Magic !? What do you think is happening ? Try to describe it with your own words

* Cancel (CTRL+C) the jupyter process

To learn more about port forwarding in codespaces, refer to the [documentation](https://docs.github.com/en/codespaces/developing-in-codespaces/forwarding-ports-in-your-codespace)

## 3. Running your notebooks in the VM

As an exercise, you will setup your development environment in the codespace and run an MLClass Notebook inside the VM,

- Transfer a notebook you are working on from your computer
- Transfer the data as well if it's not downloaded
- Setup your environment using pip, conda, etc... as you would do in your local machine
- Run jupyter lab or jupyter notebook from your codespace and connect to it like previously
- You can continue your script / etc... 

If you don't have anything at hand you can use this simple repo as an example (you will see that later on your DL classes) : 
[https://github.com/pytorch/examples/tree/main/mnist](https://github.com/pytorch/examples/tree/main/mnist)

!!! question
    How comfortable do you feel with this remote machine ? Is it easy to get data in or out ? Code in or out ?

## 4. Let's discover Streamlit

We will now introduce streamlit, which is a very nice tool to build quick webapps in python !

In this TP you will build your first interactive webapp in python and preview it using codespace. This will help you get a feel of using the remote vscode

First, look at this video, 

<video width="320" height="240" controls>
  <source src="https://s3-us-west-2.amazonaws.com/assets.streamlit.io/videos/hero-video.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>

Then, take a look at an [introduction to streamlit](https://www.askpython.com/python-modules/introduction-to-streamlit) and [the streamlit application gallery](https://streamlit.io/gallery)

!!! question
    Can you describe what exactly is streamlit ?
    Could you find any way it could be useful to you ?

### 4.1. Your first streamlit application

Take a look at the code below, 

```python
import streamlit as st
from streamlit_image_comparison import image_comparison
import cv2

st.set_page_config("Webb Space Telescope vs Hubble Telescope", "🔭")

st.header("🔭 J. Webb Space Telescope vs Hubble Telescope")

st.write("")
"This is a reproduction of the fantastic [WebbCompare](https://www.webbcompare.com/index.html) app by [John Christensen](https://twitter.com/JohnnyC1423). It's built in Streamlit and takes only 10 lines of Python code. If you like this app, please star [John's original repo](https://github.com/JohnEdChristensen/WebbCompare)!"
st.write("")

st.markdown("### Southern Nebula")
image_comparison(
    img1="https://www.webbcompare.com/img/hubble/southern_nebula_700.jpg",
    img2="https://www.webbcompare.com/img/webb/southern_nebula_700.jpg",
    label1="Hubble",
    label2="Webb",
)


st.markdown("### Galaxy Cluster SMACS 0723")
image_comparison(
    img1="https://www.webbcompare.com/img/hubble/deep_field_700.jpg",
    img2="https://www.webbcompare.com/img/webb/deep_field_700.jpg",
    label1="Hubble",
    label2="Webb",
)

st.markdown("### Carina Nebula")
image_comparison(
    img1="https://www.webbcompare.com/img/hubble/carina_2800.png",
    img2="https://www.webbcompare.com/img/webb/carina_2800.jpg",
    label1="Hubble",
    label2="Webb",
)

st.markdown("### Stephan's Quintet")
image_comparison(
    img1="https://www.webbcompare.com/img/hubble/stephans_quintet_2800.jpg",
    img2="https://www.webbcompare.com/img/webb/stephans_quintet_2800.jpg",
    label1="Hubble",
    label2="Webb",
)
```

!!! question
    Can you describe, by reading the documentation, what does the code do ?

### 4.2. Local deployment in codespace

First, we will install in the codespace the dependencies for our application,

`pip install streamlit streamlit opencv-python-headless`

Then create a file `streamlit_jswt.py` and copy/paste the code above.

Then execute it `streamlit run streamlit_jswt.py`

This will launch the application on the port 8501 (by default) of our codespace. You can connect to it as usual.

🤩 Nice, isn't it ?

Now you can quit the server.

### 4.3. A more complex application

We will run and package a more complex application, but a lot more useful for your deep learning class.

If you started your github codespace from the isae cloud computing codespace, you should have a folder called `demo-streamlit-activation-function`.

Otherwise, clone the repository `git clone https://github.com/fchouteau/isae-cloud-computing-codespace.git`

cd to the directory `cd isae-demo-streamlit-activation-functions` then as last time, install the dependencies `pip install -r requirements.txt` then run the application `streamlit run app.py`

You can visualize it as last time. This should be quite useful for you given you just left (or will just start, it's early in the year...) the Deep Learning Class !
