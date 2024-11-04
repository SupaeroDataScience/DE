# Docker: Hands on

!!! note

    If you are lost, `docker system prune` will remove dangling images and stopped containers 

## 0. How to run this ?

!!! abstract

    We will discover the basics of docker and you will be able to manipulate your first images and containers !

You should be inside the Github Codespace you created and have google cloud SDK installed in it

If not, refer to the previous tutorial and do step 2 and 3

This codespace has everything you need, including docker

If you want to do everything from your linux machine you can [install docker](https://docs.docker.com/engine/install/ubuntu/) but I don't recommend it for now

## 1. Manipulating docker for the 1st time

Source: <https://github.com/docker/labs>

To get started, let's run the following in our terminal:

```
$ docker pull alpine
```

The `pull` command fetches the alpine **image** from the **Docker registry** and saves it in our system. You can use the `docker images` command to see a list of all images on your system.
```
$ docker images
REPOSITORY              TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
alpine                 latest              c51f86c28340        4 weeks ago         1.109 MB
hello-world             latest              690ed74de00f        5 months ago        960 B
```

### 1.1 Docker Run

Great! Let's now run a Docker **container** based on this image. To do that you are going to use the `docker run` command.

```
$ docker run alpine ls -l
total 48
drwxr-xr-x    2 root     root          4096 Mar  2 16:20 bin
drwxr-xr-x    5 root     root           360 Mar 18 09:47 dev
drwxr-xr-x   13 root     root          4096 Mar 18 09:47 etc
drwxr-xr-x    2 root     root          4096 Mar  2 16:20 home
drwxr-xr-x    5 root     root          4096 Mar  2 16:20 lib
......
......
```

What happened? Behind the scenes, a lot of stuff happened. When you call `run`,

1. The Docker client contacts the Docker daemon
2. The Docker daemon checks local store if the image (alpine in this case) is available locally, and if not, downloads it from Docker Store. (Since we have issued `docker pull alpine` before, the download step is not necessary)
3. The Docker daemon creates the container and then runs a command in that container.
4. The Docker daemon streams the output of the command to the Docker client

When you run `docker run alpine`, you provided a command (`ls -l`), so Docker started the command specified and you saw the listing.

Let's try something more exciting.

```
$ docker run alpine echo "hello from alpine"
hello from alpine
```
OK, that's some actual output. In this case, the Docker client dutifully ran the `echo` command in our alpine container and then exited it. If you've noticed, all of that happened pretty quickly. Imagine booting up a virtual machine, running a command and then killing it. Now you know why they say containers are fast!

Try another command.

```bash
docker run alpine /bin/sh
```

Wait, nothing happened! Is that a bug? Well, no. These interactive shells will exit after running any scripted commands, unless they are run in an interactive terminal - so for this example to not exit, you need to `docker run -it alpine /bin/sh`.

You are now inside the container shell and you can try out a few commands like `ls -l`, `uname -a` and others. Exit out of the container by giving the `exit` command.

Ok, now it's time to see the `docker ps` command. The `docker ps` command shows you all containers that are currently running.

```
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```

Since no containers are running, you see a blank line. Let's try a more useful variant: `docker ps -a`

```
$ docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                      PORTS               NAMES
36171a5da744        alpine              "/bin/sh"                5 minutes ago       Exited (0) 2 minutes ago                        fervent_newton
a6a9d46d0b2f        alpine             "echo 'hello from alp"    6 minutes ago       Exited (0) 6 minutes ago                        lonely_kilby
ff0a5c3750b9        alpine             "ls -l"                   8 minutes ago       Exited (0) 8 minutes ago                        elated_ramanujan
c317d0a9e3d2        hello-world         "/hello"                 34 seconds ago      Exited (0) 12 minutes ago                       stupefied_mcclintock
```

What you see above is a list of all containers that you ran. Notice that the `STATUS` column shows that these containers exited a few minutes ago. You're probably wondering if there is a way to run more than just one command in a container. Let's try that now:

```
$ docker run -it alpine /bin/sh
/ # ls
bin      dev      etc      home     lib      linuxrc  media    mnt      proc     root     run      sbin     sys      tmp      usr      var
/ # uname -a
Linux 97916e8cb5dc 4.4.27-moby #1 SMP Wed Oct 26 14:01:48 UTC 2016 x86_64 Linux
```
Running the `run` command with the `-it` flags attaches us to an interactive tty in the container. Now you can run as many commands in the container as you want. Take some time to run your favorite commands.

That concludes a whirlwind tour of the `docker run` command which would most likely be the command you'll use most often. It makes sense to spend some time getting comfortable with it. To find out more about `run`, use `docker run --help` to see a list of all flags it supports. As you proceed further, we'll see a few more variants of `docker run`.

### 1.2 Terminology

In the last section, you saw a lot of Docker-specific jargon which might be confusing to some. So before you go further, let's clarify some terminology that is used frequently in the Docker ecosystem.

* *Images* - The file system and configuration of our application which are used to create containers. To find out more about a Docker image, run `docker inspect alpine`. In the demo above, you used the `docker pull` command to download the **alpine** image. When you executed the command `docker run hello-world`, it also did a `docker pull` behind the scenes to download the **hello-world** image.
* *Containers* - Running instances of Docker images &mdash; containers run the actual applications. A container includes an application and all of its dependencies. It shares the kernel with other containers, and runs as an isolated process in user space on the host OS. You created a container using `docker run` which you did using the alpine image that you downloaded. A list of running containers can be seen using the `docker ps` command.
* *Docker daemon* - The background service running on the host that manages building, running and distributing Docker containers.
* *Docker client* - The command line tool that allows the user to interact with the Docker daemon.
* *Docker Store* - A [registry](https://store.docker.com/) of Docker images, where you can find trusted and enterprise ready containers, plugins, and Docker editions. You'll be using this later in this tutorial.

## 2.0 Webapps with Docker

Source: <https://github.com/docker/labs>

Great! So you have now looked at `docker run`, played with a Docker container and also got the hang of some terminology. Armed with all this knowledge, you are now ready to get to the real stuff &#8212; deploying web applications with Docker.

### 2.1 Run a static website in a container

>**Note:** Code for this section is in this repo in the website directory

Let's start by taking baby-steps. First, we'll use Docker to run a static website in a container. The website is based on an existing image. We'll pull a Docker image from Docker Store, run the container, and see how easy it is to set up a web server.

The image that you are going to use is a single-page website that was already created for this demo and is available on the Docker Store as [`dockersamples/static-site`](https://store.docker.com/community/images/dockersamples/static-site). You can download and run the image directly in one go using `docker run` as follows.

```bash
docker run -d dockersamples/static-site
```

Files:

* [Dockerfile](https://github.com/docker/labs/blob/master/beginner/static-site/Dockerfile)
* [hello_docker.html](https://github.com/docker/labs/blob/master/beginner/static-site/Hello_docker.html)

>**Note:** The current version of this image doesn't run without the `-d` flag. The `-d` flag enables **detached mode**, which detaches the running container from the terminal/shell and returns your prompt after the container starts. We are debugging the problem with this image but for now, use `-d` even for this first example.

So, what happens when you run this command?

Since the image doesn't exist on your Docker host, the Docker daemon first fetches it from the registry and then runs it as a container.

Now that the server is running, do you see the website? What port is it running on? And more importantly, how do you access the container directly from our host machine?

Actually, you probably won't be able to answer any of these questions yet! &#9786; In this case, the client didn't tell the Docker Engine to publish any of the ports, so you need to re-run the `docker run` command to add this instruction.

Let's re-run the command with some new flags to publish ports and pass your name to the container to customize the message displayed. We'll use the *-d* option again to run the container in detached mode.

First, stop the container that you have just launched. In order to do this, we need the container ID.

Since we ran the container in detached mode, we don't have to launch another terminal to do this. Run `docker ps` to view the running containers.

```bash
$ docker ps
CONTAINER ID        IMAGE                  COMMAND                  CREATED             STATUS              PORTS               NAMES
a7a0e504ca3e        dockersamples/static-site   "/bin/sh -c 'cd /usr/"   28 seconds ago      Up 26 seconds       80/tcp, 443/tcp     stupefied_mahavira
```

Check out the `CONTAINER ID` column. You will need to use this `CONTAINER ID` value, a long sequence of characters, to identify the container you want to stop, and then to remove it. The example below provides the `CONTAINER ID` on our system; you should use the value that you see in your terminal.

```bash
$ docker stop a7a0e504ca3e
$ docker rm   a7a0e504ca3e
```

>**Note:** A cool feature is that you do not need to specify the entire `CONTAINER ID`. You can just specify a few starting characters and if it is unique among all the containers that you have launched, the Docker client will intelligently pick it up.

Now, let's launch a container in **detached** mode as shown below:

```bash
$ docker run --name static-site -e AUTHOR="Your Name" -d -P dockersamples/static-site
e61d12292d69556eabe2a44c16cbd54486b2527e2ce4f95438e504afb7b02810
```

In the above command:

*  `-d` will create a container with the process detached from our terminal
* `-P` will publish all the exposed container ports to random ports on the Docker host
* `-e` is how you pass environment variables to the container
* `--name` allows you to specify a container name
* `AUTHOR` is the environment variable name and `Your Name` is the value that you can pass

Now you can see the ports by running the `docker port` command.

```bash
$ docker port static-site
443/tcp -> 0.0.0.0:32772
80/tcp -> 0.0.0.0:32773
```

If you are on codespace, create [a port forwarding on port 80](https://docs.github.com/en/codespaces/developing-in-codespaces/forwarding-ports-in-your-codespace) to connect to the website
 
If you are running [Docker for Mac](https://docs.docker.com/docker-for-mac/), [Docker for Windows](https://docs.docker.com/docker-for-windows/), or Docker on Linux, you can open `http://localhost:[YOUR_PORT_FOR 80/tcp]`. For our example this is `http://localhost:32773`.

If you are using Docker Machine on Mac or Windows, you can find the hostname on the command line using `docker-machine` as follows (assuming you are using the `default` machine).

```bash
$ docker-machine ip default
192.168.99.100
```
You can now open `http://<YOUR_IPADDRESS>:[YOUR_PORT_FOR 80/tcp]` to see your site live! For our example, this is: `http://192.168.99.100:32773`.

You can also run a second webserver at the same time, specifying a custom host port mapping to the container's webserver.

```bash
$ docker run --name static-site-2 -e AUTHOR="Your Name" -d -p 8888:80 dockersamples/static-site
```

<img src="https://raw.githubusercontent.com/docker/labs/master/beginner/images/static.png" title="static">

To deploy this on a real server you would just need to install Docker, and run the above `docker` command(as in this case you can see the `AUTHOR` is Docker which we passed as an environment variable).

Now that you've seen how to run a webserver inside a Docker container, how do you create your own Docker image? This is the question we'll explore in the next section.

But first, let's stop and remove the containers since you won't be using them anymore.

```bash
$ docker stop static-site
$ docker rm static-site
```

Let's use a shortcut to remove the second site:

```bash
$ docker rm -f static-site-2
```

Run `docker ps` to make sure the containers are gone.

```bash
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```

### 2.2 Docker Images

In this section, let's dive deeper into what Docker images are. You will build your own image, use that image to run an application locally.

Docker images are the basis of containers. In the previous example, you **pulled** the *dockersamples/static-site* image from the registry and asked the Docker client to run a container **based** on that image. To see the list of images that are available locally on your system, run the `docker images` command.

```bash
$ docker images
REPOSITORY             TAG                 IMAGE ID            CREATED             SIZE
dockersamples/static-site   latest              92a386b6e686        2 hours ago        190.5 MB
nginx                  latest              af4b3d7d5401        3 hours ago        190.5 MB
python                 2.7                 1c32174fd534        14 hours ago        676.8 MB
postgres               9.4                 88d845ac7a88        14 hours ago        263.6 MB
containous/traefik     latest              27b4e0c6b2fd        4 days ago          20.75 MB
node                   0.10                42426a5cba5f        6 days ago          633.7 MB
redis                  latest              4f5f397d4b7c        7 days ago          177.5 MB
mongo                  latest              467eb21035a8        7 days ago          309.7 MB
alpine                 3.3                 70c557e50ed6        8 days ago          4.794 MB
java                   7                   21f6ce84e43c        8 days ago          587.7 MB
```

Above is a list of images that I've pulled from the registry and those I've created myself (we'll shortly see how). You will have a different list of images on your machine. The `TAG` refers to a particular snapshot of the image and the `ID` is the corresponding unique identifier for that image.

For simplicity, you can think of an image akin to a git repository - images can be [committed](https://docs.docker.com/engine/reference/commandline/commit/) with changes and have multiple versions. When you do not provide a specific version number, the client defaults to `latest`.

For example you could pull a specific version of `ubuntu` image as follows:

```bash
$ docker pull ubuntu:12.04
```

If you do not specify the version number of the image then, as mentioned, the Docker client will default to a version named `latest`.

So for example, the `docker pull` command given below will pull an image named `ubuntu:latest`:

```bash
$ docker pull ubuntu
```

To get a new Docker image you can either get it from a registry (such as the Docker Store) or create your own. There are hundreds of thousands of images available on [Docker Store](https://store.docker.com). You can also search for images directly from the command line using `docker search`.

An important distinction with regard to images is between _base images_ and _child images_.

- **Base images** are images that have no parent images, usually images with an OS like ubuntu, alpine or debian.

- **Child images** are images that build on base images and add additional functionality.

Another key concept is the idea of _official images_ and _user images_. (Both of which can be base images or child images.)

- **Official images** are Docker sanctioned images. Docker, Inc. sponsors a dedicated team that is responsible for reviewing and publishing all Official Repositories content. This team works in collaboration with upstream software maintainers, security experts, and the broader Docker community. These are not prefixed by an organization or user name. In the list of images above, the `python`, `node`, `alpine` and `nginx` images are official (base) images. To find out more about them, check out the [Official Images Documentation](https://docs.docker.com/docker-hub/official_repos/).

- **User images** are images created and shared by users like you. They build on base images and add additional functionality. Typically these are formatted as `user/image-name`. The `user` value in the image name is your Docker Store user or organization name.

### 2.3 Create your first image

>**Note:** The code for this section is in this repository in the [flask-app](https://github.com/docker/labs/tree/master/beginner/flask-app) directory.

Now that you have a better understanding of images, it's time to create your own. Our goal here is to create an image that sandboxes a small [Flask](http://flask.pocoo.org) application.

**The goal of this exercise is to create a Docker image which will run a Flask app.**

We'll do this by first pulling together the components for a random cat picture generator built with Python Flask, then _dockerizing_ it by writing a _Dockerfile_. Finally, we'll build the image, and then run it.

- [Create a Python Flask app that displays random cat pix](#231-create-a-python-flask-app-that-displays-random-cat-pix)
- [Write a Dockerfile](#232-write-a-dockerfile)
- [Build the image](#233-build-the-image)
- [Run your image](#234-run-your-image)
- [Dockerfile commands summary](#235-dockerfile-commands-summary)

### 2.3.1 Create a Python Flask app that displays random cat pix

For the purposes of this workshop, we've created a fun little Python Flask app that displays a random cat `.gif` every time it is loaded - because, you know, who doesn't like cats?

Start by creating a directory called ```flask-app``` where we'll create the following files:

- [app.py](#apppy)
- [requirements.txt](#requirementstxt)
- [templates/index.html](#templatesindexhtml)
- [Dockerfile](#dockerfile)

Make sure to ```cd flask-app``` before you start creating the files, because you don't want to start adding a whole bunch of other random files to your image.

#### app.py

Create the **app.py** with the following content:

```python
from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
   "https://storage.googleapis.com/fchouteau-isae-cloud/gifs/gif1.gif",
   "https://storage.googleapis.com/fchouteau-isae-cloud/gifs/gif2.gif",
   "https://storage.googleapis.com/fchouteau-isae-cloud/gifs/gif3.gif",
   "https://storage.googleapis.com/fchouteau-isae-cloud/gifs/gif4.gif",
   "https://storage.googleapis.com/fchouteau-isae-cloud/gifs/gif5.gif",
   "https://storage.googleapis.com/fchouteau-isae-cloud/gifs/gif6.gif",
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
```

#### requirements.txt

In order to install the Python modules required for our app, we need to create a file called **requirements.txt** and add the following line to that file:

```
flask
typer
```

#### templates/index.html

Create a directory called `templates` and create an **index.html** file in that directory with the following content in it:

```html
<html>
  <head>
    <style type="text/css">
      body {
        background: black;
        color: white;
      }
      div.container {
        max-width: 500px;
        margin: 100px auto;
        border: 20px solid white;
        padding: 10px;
        text-align: center;
      }
      h4 {
        text-transform: uppercase;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h4>Cat Gif of the day</h4>
      <img src="{{url}}" />
    </div>
  </body>
</html>
```

### 2.3.2 Write a Dockerfile

We want to create a Docker image with this web app. As mentioned above, all user images are based on a _base image_. Since our application is written in Python, we will build our own Python image based on [Alpine](https://store.docker.com/images/alpine). We'll do that using a **Dockerfile**.

A [Dockerfile](https://docs.docker.com/engine/reference/builder/) is a text file that contains a list of commands that the Docker daemon calls while creating an image. The Dockerfile contains all the information that Docker needs to know to run the app &#8212; a base Docker image to run from, location of your project code, any dependencies it has, and what commands to run at start-up. It is a simple way to automate the image creation process. The best part is that the [commands](https://docs.docker.com/engine/reference/builder/) you write in a Dockerfile are *almost* identical to their equivalent Linux commands. This means you don't really have to learn new syntax to create your own Dockerfiles.


1. Create a file called **Dockerfile**, and add content to it as described below.

  We'll start by specifying our base image, using the `FROM` keyword:

  ```
  FROM alpine:3.18
  ```

  Note : If you use the latest version of alpine which is 3.20, follow this [tutorial](https://jairoandres.com/python-dependencies-break-your-system-if-you-want/) to handle an error you might be getting

2. The next step usually is to write the commands of copying the files and installing the dependencies. But first we will install the Python pip package to the alpine linux distribution. This will not just install the pip package but any other dependencies too, which includes the python interpreter. Add the following [RUN](https://docs.docker.com/engine/reference/builder/#run) command next. Additionnally, we will do something to handle the newest python rules []

  ```
  RUN apk add --update py-pip
  ```

3. Let's add the files that make up the Flask Application.

  Install all Python requirements for our app to run. This will be accomplished by adding the lines:

  ```
  COPY requirements.txt /usr/src/app/
  RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt
  ```

  Copy the files you have created earlier into our image by using [COPY](https://docs.docker.com/engine/reference/builder/#copy)  command.

  ```
  COPY app.py /usr/src/app/
  COPY templates/index.html /usr/src/app/templates/
  ```

4. Specify the port number which needs to be exposed. Since our flask app is running on `5000` that's what we'll expose.

  ```
  EXPOSE 5000
  ```

5. The last step is the command for running the application which is simply - `python ./app.py`. Use the [CMD](https://docs.docker.com/engine/reference/builder/#cmd) command to do that:

  ```
  CMD ["python", "/usr/src/app/app.py"]
  ```

  The primary purpose of `CMD` is to tell the container which command it should run by default when it is started.

6. Verify your Dockerfile.

  Our `Dockerfile` is now ready. This is how it looks:

  ```
  # our base image
  FROM alpine:3.18

  # Install python and pip
  RUN apk add --update py-pip

  # install Python modules needed by the Python app
  COPY requirements.txt /usr/src/app/
  RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

  # copy files required for the app to run
  COPY app.py /usr/src/app/
  COPY templates/index.html /usr/src/app/templates/

  # tell the port number the container should expose
  EXPOSE 5000

  # run the application
  CMD ["python", "/usr/src/app/app.py"]
  ```

### 2.3.3 Build the image

Now that you have your `Dockerfile`, you can build your image. The `docker build` command does the heavy-lifting of creating a docker image from a `Dockerfile`.

The `docker build` command is quite simple - it takes an optional tag name with the `-t` flag, and the location of the directory containing the `Dockerfile` - the `.` indicates the current directory:

`docker build -t myfirstapp:1.0 .`

```
$ docker build -t myfirstapp:1.0 .
Sending build context to Docker daemon 9.728 kB
Step 1 : FROM alpine:18
 ---> 0d81fc72e790
Step 2 : RUN apk add --update py-pip
 ---> Running in 8abd4091b5f5
fetch http://dl-4.alpinelinux.org/alpine/v3.3/main/x86_64/APKINDEX.tar.gz
fetch http://dl-4.alpinelinux.org/alpine/v3.3/community/x86_64/APKINDEX.tar.gz
(1/12) Installing libbz2 (1.0.6-r4)
(2/12) Installing expat (2.1.0-r2)
(3/12) Installing libffi (3.2.1-r2)
(4/12) Installing gdbm (1.11-r1)
(5/12) Installing ncurses-terminfo-base (6.0-r6)
(6/12) Installing ncurses-terminfo (6.0-r6)
(7/12) Installing ncurses-libs (6.0-r6)
(8/12) Installing readline (6.3.008-r4)
(9/12) Installing sqlite-libs (3.9.2-r0)
(10/12) Installing python (2.7.11-r3)
(11/12) Installing py-setuptools (18.8-r0)
(12/12) Installing py-pip (7.1.2-r0)
Executing busybox-1.24.1-r7.trigger
OK: 59 MiB in 23 packages
 ---> 976a232ac4ad
Removing intermediate container 8abd4091b5f5
Step 3 : COPY requirements.txt /usr/src/app/
 ---> 65b4be05340c
Removing intermediate container 29ef53b58e0f
Step 4 : RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt
 ---> Running in a1f26ded28e7
Collecting Flask==0.10.1 (from -r /usr/src/app/requirements.txt (line 1))
  Downloading Flask-0.10.1.tar.gz (544kB)
Collecting Werkzeug>=0.7 (from Flask==0.10.1->-r /usr/src/app/requirements.txt (line 1))
  Downloading Werkzeug-0.11.4-py2.py3-none-any.whl (305kB)
Collecting Jinja2>=2.4 (from Flask==0.10.1->-r /usr/src/app/requirements.txt (line 1))
  Downloading Jinja2-2.8-py2.py3-none-any.whl (263kB)
Collecting itsdangerous>=0.21 (from Flask==0.10.1->-r /usr/src/app/requirements.txt (line 1))
  Downloading itsdangerous-0.24.tar.gz (46kB)
Collecting MarkupSafe (from Jinja2>=2.4->Flask==0.10.1->-r /usr/src/app/requirements.txt (line 1))
  Downloading MarkupSafe-0.23.tar.gz
Installing collected packages: Werkzeug, MarkupSafe, Jinja2, itsdangerous, Flask
  Running setup.py install for MarkupSafe
  Running setup.py install for itsdangerous
  Running setup.py install for Flask
Successfully installed Flask-0.10.1 Jinja2-2.8 MarkupSafe-0.23 Werkzeug-0.11.4 itsdangerous-0.24
You are using pip version 7.1.2, however version 8.1.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
 ---> 8de73b0730c2
Removing intermediate container a1f26ded28e7
Step 5 : COPY app.py /usr/src/app/
 ---> 6a3436fca83e
Removing intermediate container d51b81a8b698
Step 6 : COPY templates/index.html /usr/src/app/templates/
 ---> 8098386bee99
Removing intermediate container b783d7646f83
Step 7 : EXPOSE 5000
 ---> Running in 31401b7dea40
 ---> 5e9988d87da7
Removing intermediate container 31401b7dea40
Step 8 : CMD python /usr/src/app/app.py
 ---> Running in 78e324d26576
 ---> 2f7357a0805d
Removing intermediate container 78e324d26576
Successfully built 2f7357a0805d
```

If you don't have the `alpine:3.18` image, the client will first pull the image and then create your image. Therefore, your output on running the command will look different from mine. If everything went well, your image should be ready! Run `docker images` and see if your image (`<YOUR_USERNAME>/myfirstapp`) shows.

### 2.3.4 Run your image

The next step in this section is to run the image and see if it actually works.

```bash
$ docker run -p 8888:5000 --name myfirstapp myfirstapp:1.0
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

Head over to `http://localhost:8888` and your app should be live. **Note** If you are using Docker Machine, you may need to open up another terminal and determine the container ip address using `docker-machine ip default`.

![catgif](https://raw.githubusercontent.com/docker/labs/master/beginner/images/catgif.png)

Hit the Refresh button in the web browser to see a few more cat images.

### 2.3.5 Dockerfile commands summary

Here's a quick summary of the few basic commands we used in our Dockerfile.

* `FROM` starts the Dockerfile. It is a requirement that the Dockerfile must start with the `FROM` command. Images are created in layers, which means you can use another image as the base image for your own. The `FROM` command defines your base layer. As arguments, it takes the name of the image. Optionally, you can add the Docker Cloud username of the maintainer and image version, in the format `username/imagename:version`.

* `RUN` is used to build up the Image you're creating. For each `RUN` command, Docker will run the command then create a new layer of the image. This way you can roll back your image to previous states easily. The syntax for a `RUN` instruction is to place the full text of the shell command after the `RUN` (e.g., `RUN mkdir /user/local/foo`). This will automatically run in a `/bin/sh` shell. You can define a different shell like this: `RUN /bin/bash -c 'mkdir /user/local/foo'`

* `COPY` copies local files into the container.

* `CMD` defines the commands that will run on the Image at start-up. Unlike a `RUN`, this does not create a new layer for the Image, but simply runs the command. There can only be one `CMD` per a Dockerfile/Image. If you need to run multiple commands, the best way to do that is to have the `CMD` run a script. `CMD` requires that you tell it where to run the command, unlike `RUN`. So example `CMD` commands would be:

```
  CMD ["python", "./app.py"]

  CMD ["/bin/bash", "echo", "Hello World"]
```

* `EXPOSE` creates a hint for users of an image which ports provide services. It is included in the information which
 can be retrieved via `$ docker inspect <container-id>`.     

>**Note:** The `EXPOSE` command does not actually make any ports accessible to the host! Instead, this requires 
publishing ports by means of the `-p` flag when using `$ docker run`.  

* `PUSH` pushes your image to Docker Cloud, or alternately to a [private registry](https://docs.docker.com/registry/)

>**Note:** If you want to learn more about Dockerfiles, check out [Best practices for writing Dockerfiles](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/).

## 3. Running CLI apps packaged in docker while mounting volumes

Beyond serving web applications, Docker also enables the deployment of packaged applications, such as command-line interfaces and training scripts. This allows for seamless delivery of self-contained apps with bespoke installations to end-users. A particularly valuable use case is packaging machine learning environments for distributed training, facilitating efficient collaboration and scalability

To do so, we have to learn about : 
- Executing command line applications packaged inside docker images
- Passing both text and files inputs, including files not in the docker image
- Getting accesss to file outputs such as models

For that we will do several things : 
- Write a CLI application using [typer](https://typer.tiangolo.com/), a very useful tool for the rest of your career
- Package the CLI application with both text / file inputs in a docker image
- Mounting volumes when running a docker images to provide it with the input files, and having access to the results from the main computer

### 3.1 A local CLI application

* Let's modify the `app.py` in 2. with the following code.

```python
import time
from pathlib import Path
from typing import Annotated, Optional

import typer

app = typer.Typer()


@app.command()
def say_hello(name: str):
    typer.echo(f"Hello {name}")


@app.command()
def run_training(
    config: Annotated[
        Path,
        typer.Option(
            exists=True,
            file_okay=True,
            dir_okay=False,
            writable=False,
            readable=True,
            resolve_path=True,
        ),
    ],
    output_dir: Annotated[
        Path,
        typer.Option(
            dir_okay=True,
            writable=True,
            readable=True,
            resolve_path=True,
            file_okay=False,
        ),
    ],
):
    text = config.read_text()
    print(f"Config file contents: {text}")

    print(f"Running training in {output_dir}...")

    time.sleep(10)

    output_dir.mkdir(exist_ok=True,parents=True)

    with open(output_dir / "results.txt", "w") as f:
        f.write("Training successful !")


if __name__ == "__main__":
    app()

```

* Test the application locally using `pip install typer`then `python app.py say-hello {my name}` or `python app.py run-training --config {my config} --output-dir {somewhere}`

### 3.2 Packaging it in a dockerfile

We will now package it in a docker file

* Modify the dockerfile : 
  * Replace `CMD ["python3", "/usr/src/app/app.py"]`
  * By `ENTRYPOINT ["python3", "/usr/src/app/app.py"]`

* [Differences between CMD and ENTRYPOINT](https://spacelift.io/blog/docker-entrypoint-vs-cmd)

* Rebuild your docker image (maybe give it another name)

### 3.3 Mounting volumes

* Now to run the CLI you just have to pass the arguments when running the docker `docker run --rm {your image} {your args}`. Try it with `docker run {...} hello {your name}`

!!! warning
    once you have built your container and it works, don't rebuild it again ! We will test the volume mounting options now

* In order to pass a config file, or data to your docker, you need to make it available to your docker. To do that, we have to [mount volumes](https://docs.docker.com/storage/volumes/)

Create a dummy config file (`config.txt`) in another folder (ex: `config/`) then mount it when you run the docker container. You can expose the output directory as well to be able to get your results

```bash
docker run --rm \
  -v {local path to your configs}:/home/configs \
  -v {local path to your outputs}:/home/outputs \
  --workdir /home/ \
  {your image} \
  run-training --config {path to your config in DOCKER, eg /home/configs/config.txt}  \
  --output-dir /home/outputs/
```

Note that since you mounted volumes, you must pass the **local path in the docker container** to your config file for it to work and not the **path in your codespace**

!!! success
    To be successful here you have to be able to pass a config file that is in your codespace and get the results in your codespace, all while not rebuilding the image as long as the first `hello` passes

## 4. Containers Registry

Remember Container Registries ? Here as [some explainers](https://blogs.vmware.com/cloudnative/2017/06/21/what-is-a-container-registry/)

The main container registry is dockerhub, [https://hub.docker.com/](https://hub.docker.com/)

All docker engines that have access to the internet have access to this main hub, and this is where we pulled our base images from before

Example, the [Python Image](https://hub.docker.com/_/python)

Google Cloud has an [Artifacts Registry](https://cloud.google.com/artifact-registry/docs/repositories/create-repos) per project, which ensures the docker images you build are accessible for the people who have access to your project only.

We will follow [this tutorial](https://cloud.google.com/artifact-registry/docs/docker/store-docker-container-images) to push our images to artifact registry

* First, create a Docker Artifact registry using this [tutorial](https://cloud.google.com/artifact-registry/docs/repositories/create-repos#create-console), example `fch-sdd2425-artifacts-registry` (that's mine, name it with your name). Set the repository in `multi-region/europe`

* Pushing our images requires authenticating, `gcloud auth configure-docker europe-docker.pkg.dev`

* Pushing our images requires tagging them in a [specific way](https://cloud.google.com/artifact-registry/docs/docker/store-docker-container-images#add-image) : `europe-docker.pkg.dev/${PROJECT_ID}/${REPO_ID}/${IMAGE}:${TAG}`

* Use the [docker cli to tag](https://cloud.google.com/container-registry/docs/pushing-and-pulling#tag_the_local_image_with_the_registry_name) your previous `myfirstapp` image to the right namespace

  `docker tag myfirstapp:1.0 europe-docker.pkg.dev/${PROJECT_ID}/${REPO_ID}/myfirstapp:1.0`

* Upload it on container registry 

  `docker push europe-docker.pkg.dev/${PROJECT_ID}/${REPO_ID}/[IMAGE]:[TAG]`

!!! hint
    to get your project id: `PROJECT_ID=$(gcloud config get-value project 2> /dev/null)`
    to get your artifact repository id look at [this page](https://console.cloud.google.com/artifacts/docker/), you can get your project id this way as well

* Go to your artifact registry [https://console.cloud.google.com/artifacts](https://console.cloud.google.com/artifacts), you should see your docker image :)

## 5. Bonus. Data Science Standardized Environment and mounting volumes

Note : This may not run in your native github codespace due to the storage available. If you encounter a storage error, run `docker system prune` to cleanup everything

The purpose of this tutorial is to reproduce a sort of google colab environment using docker and github codespace.

### 5.1 Intro

Those of us who work on a team know how hard it is to create a standardize development environment. Or if you have ever updated a dependency and had everything break, you understand the importance of keeping development environments isolated.

Using Docker, we can create a project / team image with our development environment and mount a volume with our notebooks and data.

The benefits of this workflow are that we can:

* Separate out projects
* Spin up a container to onboard new employees
* Build an automated testing pipeline to confirm upgrade dependencies do not break code

### 5.2 Jupyter Stack Docker Image

For this exercise we will use [Jupyter Stack Docker Image](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/running.html#) which is a fully configured docker image that can be used as a data science container

Take a look at the documentation and [the dockerhub repository](https://hub.docker.com/r/jupyter/scipy-notebook/tags/)

To get the docker image, run

```bash
docker pull jupyter/scipy-notebook:lab-3.5.3
```

### 5.3 Get the algorithm in ML git in your Virtual Machine

* From your vm, run `git clone https://github.com/erachelson/MLclass.git`, this should setup your AML class inside your VM

### 5.4 Mounting volumes and ports

Now let's run the image. This container has a jupyter notebook accessible from port 8080 so we will need to map the host port 8888 (the one accessible from the ssh tunnel) to the docker port 8080, we will use [port forwarding](https://docs.docker.com/config/containers/container-networking/)

We will also need to make available the notebooks on the VM to the container... we will [mount volumes](https://docs.docker.com/storage/volumes/). Your data is located in `/home/${USER}/MLClass` and we want to miunt it in `/tmp/workdir`

```bash
docker run --rm -it \
  -p 8888:8888 \
  -v /home/${USER}/MLclass:/home/jovyan/work/MLClass \
  --workdir /home/jovyan/work \
  jupyter/scipy-notebook:lab-3.5.3
```

Note: this image is large, delete it afterwards using `docker rmi`

Options breakdown:

* `--rm` remove the container when we stop it
* `-it` run the container in interactive mode
* `-p` forward port from host:container
* other: options from the kaggle container

You should now see a jupyter lab with mlclass accessible if you do another port mapping

So to connect to the jupyter lab we mapped the ports local 8888 to vm 8888 and vm 8888 to docker 8888

We also exposed the local disk to the container

## 6. Bonus - Docker Compose

Docker Compose is used to manage applications and increase efficiency in container development. Configurations are defined in a single YAML file, making applications easy to build and scale. Docker Compose is often used to set up a local environment

The tutorial below aims to introduce fundamental concepts of Docker Compose by guiding you through the development of a basic Python web application.

Using the Flask framework, the application features a hit counter in Redis, providing a practical example of how Docker Compose can be applied in web development scenarios.

The concepts demonstrated here should be understandable even if you're not familiar with Python.

This is a non-normative example that just highlights the key things you can do with Compose.

[https://docs.docker.com/compose/gettingstarted/](https://docs.docker.com/compose/gettingstarted/)

You can find a more extensive example here : 

<https://hackernoon.com/practical-introduction-to-docker-compose-d34e79c4c2b6>

<https://github.com/docker/labs/blob/master/beginner/chapters/votingapp.md>

## 7. Bonus - Using Google Cloud Tools for Docker

Using codespace, you should be able to do the Hello World Dockerfile exercise except that instead of using docker build you use Google Cloud Build

Tutorial: <https://cloud.google.com/cloud-build/docs/quickstart-docker>

Example command :`gcloud builds submit --tag eu.gcr.io/$PROJECT_ID/{image}:{tag} .`

!!! help
    to get your project id: `PROJECT_ID=$(gcloud config get-value project 2> /dev/null)`

!!! example
    Try to build the hello world app

## 8. Bonus - Going further

<https://container.training/>
