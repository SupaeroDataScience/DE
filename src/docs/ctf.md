# Data Engineering Fundamentals Capture the Flag

This class is a five day Capture the Flag event to get to know with the basics of systems usage, specifically linux, git, and ssh. There is also a large section on python, with an emphasis on data science scripting practices using numpy and pandas in jupyter notebooks.

This is a self-guided exercise with resources and questions on this site. You, the participant, must look for the answer to the questions through reading documentation, discussing with others, and trying things. Try to avoid searching for answers online in a search engine; the answers can almost always be found in documentation.

Answers can be submitted through an API with the CTF server. Questions will be made available over the course of 5 sessions. Responding correctly to a question gives 1 point, and an additional 0.5 points are awarded for being the first to submit the correct answer to a question. That half point is the flag - be the first to capture it!

If you're speeding through the questions, consider helping others learn the material. Depending on your background, you may have varied experience with these tools. Get to know the other participants by helping them capture a flag too.

## Linux

Linux is an open-source operating system based on Unix. It is a standard choice for development and is the most dominant operating system for web servers, cloud computing, and high performance computing at 80% of global public servers. There are many different [distributions](https://en.wikipedia.org/wiki/List_of_Linux_distributions) but they share a common set of tools, notably [GNU](https://en.wikipedia.org/wiki/GNU) software. A very common Linux distribution is Android, at [73% of all mobile devices](https://en.wikipedia.org/wiki/Usage_share_of_operating_systems), so you might be a Linux user already without realizing it!

You most likely don't use Linux as the operating system of your personal computer, however. If you **are** using one the 2.5 % of personal computers with Linux, you can skip straight to the Submission section

MacOS is also based on Unix, so if you're using MacOS, most things should work just as in Linux! A few commands will be different from the course instructions, and the questions will always refer to Linux resources, for example documentation. It is highly recommended to install homebrew (https://brew.sh/) which will allow for package installation via the command line.

### Installation on Windows

The easiest way to use Linux on Windows is through the Windows Subsystem for Linux. Installation instructions are here: [https://docs.microsoft.com/en-us/windows/wsl/install](https://docs.microsoft.com/en-us/windows/wsl/install). Make sure to follow all instructions carefully. If asked to join a "Windows Insiders Program", ignore this. By default, this installs Ubuntu, which is good for this systems class and for all of SDD.

The WSL is similar to a virtual machine inside of Windows, but it integrates with some existing components of Windows. You can access your Windows files from Linux at `/mnt/`, but you should make sure you're familiar with Linux first.

- [About the WSL](https://docs.microsoft.com/en-us/windows/wsl/about)
- [WSL FAQ](https://docs.microsoft.com/en-us/windows/wsl/faq)
- [How to Access WSL Linux Files from Windows](https://www.howtogeek.com/426749/how-to-access-your-linux-wsl-files-in-windows-10/)

### Submission

All questions will be posted to the [CTF github repository](https://github.com/SupaeroDataScience/ctf2025). In the second class, we will use git to download this repository locally, and it will be used to host the files and data needed to respond to questions.

The CTF server's IP address is [`34.163.196.38`](http://34.163.196.38/). You can see a leaderboard there and it is the address for submitting answers. The first way we'll look at submitting answers is with `curl` in Linux.

Once you have a Unix-type environment, either native Linux or macOS, or through the WSL, you're ready to submit to the CTF. You will use the `curl` command; you can verify that you have `curl` by running `which curl` in the command line. `curl` is a tool for transferring data from or to a server. How do you know that? By checking the documentation of `curl` using `man curl`. Try it out!

To respond to a question, send a POST request with the data of the question `number` and `answer`, and your username as `user` (your username should be your ISAE login, but you can also check on the leaderboard). For example, the first question asks where the `curl` executable is (hint: use `which`). Then use `curl`:

```bash
curl -X POST 'http://34.163.196.38/' \
    -d 'number=1' \
    -d 'answer=your answer here' \
    -d 'user=your username here'
```

Some of the questions will require access to some files, called `file_a.txt`, `file_b.txt`, and `file_c.txt`. Those are available on the CTF git repository.

You are ready to start answering questions! If you don't know an answer, check the resources below and read documentation using `man`.

You can see which questions you have answered by sending a GET request:

```bash
curl 'http://34.163.196.38/user/d.wilson'
```

You can also see which questions have remaining flags, the bonus points associated with answering the question for the first time, with a GET request:

```bash
curl 'http://34.163.196.38/answers/'
```

### Python Submission

Note that you can use the `requests` library to submit responses:

```python
import requests
data = {"number": "1",
        "answer": "",
        "user": "d.wilson"}
r = requests.post("http://34.163.196.38/", data=data)
```

### Bash Resources

- [ISAE class on CLI, Linux, and Bash](https://lms.isae.fr/course/view.php?id=1111)
- [Shell class from MIT](https://missing.csail.mit.edu/2020/course-shell/)
- [Bash exercises](https://www.learnshell.org)
- [More bash exercises](https://exercism.io/tracks/bash)
- [Short exercises in regular expressions](https://regexone.com/)

## Linux tools

Now that you're an expert in Linux, let's quickly look at some useful tools. You may need to install some of these, either using `apt`, `brew`, `yum`, `pacman`, or whichever package manager you use. Linux comes with many programs installed by default, especially distributions like Ubuntu, however the tools in this section will be more useful than the base Linux tools. We'll cover four: `apt` for package management, `top` for system monitoring, `tmux` for terminal management, and `vim` for file editing. There are alternatives to all of these programs that are great, but it is worth being familiar with these four.

### Linux Resources

- [apt manual](https://manpages.ubuntu.com/manpages/xenial/man8/apt.8.html)
- [Alternatives to top](https://itsfoss.com/linux-system-monitoring-tools/)
- [Guide to tmux](https://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/)
- [tmux cheat sheet](https://tmuxcheatsheet.com/)
- [Editors from MIT class](https://missing.csail.mit.edu/2020/editors/)
- [Vim adventures](https://vim-adventures.com/)
- [tldr, short man pages](https://tldr.sh/)

## Git

Git is a version control system used worldwide for maintaining code, documents, video games, and much more. It has seen wide adoption with servers like Github and Gitlab while being an open-source tool that anyone can install as a client or server. In this class, we will look at repositories hosted on Github, but git is much larger than that and many organizations like ISAE have their own private [git server](https://iris.isae-supaero.fr/git).

### Installation

If you're using Ubuntu, chances are you already have `git`. If not, simply do:

`sudo apt install git`

These questions concern two repositories: the Machine Learning class in SDD ([https://github.com/SupaeroDataScience/machine-learning](https://github.com/SupaeroDataScience/machine-learning)) and the Seaborn library, a popular graphing library ([https://github.com/mwaskom/seaborn](https://github.com/mwaskom/seaborn)). You will need to download both repositories. First choose a directory to host them in, for example `~/SDD/FSD312`:

```bash
mkdir -p ~/SDD/FSD312
cd ~/SDD/FSD312
```

and then download them using git clone:

```bash
git clone https://github.com/SupaeroDataScience/machine-learning.git
git clone https://github.com/mwaskom/seaborn.git
```

The commit for all questions on the `seaborn` repository is `1e6739` :

```bash
git checkout 1e6739
```

### Git Resources

- [Git course](https://www.youtube.com/playlist?list=PLjwdMgw5TTLXuY5i7RW0QqGdW0NZntqiP)
- [Introduction to github](https://lab.github.com/githubtraining/introduction-to-github)
- [Github video course](https://www.youtube.com/playlist?list=PL0lo9MOBetEHhfG9vJzVCTiDYcbhAiEqL)
- [Learn git branching](https://learngitbranching.js.org/)
- [Git SCM book](https://git-scm.com/book/en/v2)
- [Git cheat sheet](https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf)

### Git Exercise

In order to access the server for the next parts of the CTF, you will need to provide your public ssh key. The SSH section has references explaining [public-key cryptography](https://en.wikipedia.org/wiki/Public-key_cryptography), but in general you will make a key pair with a private side and public side. You will give the public side to services like this class or Github to perform secure communication, keeping your private key secret to prove that it is you.

First, start by making a key pair and uploading your public key to Github. This will allow you use to SSH to make push requests, instead of using a personal access token. [Create an SSH key and add it to your Github account](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

Then, we will use git as a way for you to transfer your public key to the class. We could use another means, like a USB key, email, or a very large QR code, but for this exercise we will use git.

- First [make a fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) of the [https://github.com/SupaeroDataScience/ctf2025](https://github.com/SupaeroDataScience/ctf2025) repository.
- Then, [make a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) with your key as a file in `keys/`. Please name your key with your name, like the example `keys/dennis-wilson.pub`. Be sure to upload **only your public key**. Do not ever upload your private key to public servers.

Once your key is in the repository, you are ready for the SSH and Python portions of the CTF.

## SSH

For the ssh section, you will connect to a new server to answer questions about the remote environment.

**Pre-requisite**: Your public key must be uploaded to the git repository above to get access to the server. You will use the corresponding private key to access the server.

Your user on the server is `ctf` and the IP is: `35.190.209.18`.

Please note that _ISAE-EDU and ethernet block ssh to most servers_, including this one and `github.com`. In order to ssh to the server, you will need to either use the eduroam network or a different network like a mobile hotspot.

### SSH Resources

- [Ubuntu ssh manual](https://doc.ubuntu-fr.org/ssh)
- [Guide in French](https://openclassrooms.com/en/courses/43538-reprenez-le-controle-a-laide-de-linux/41773-la-connexion-securisee-a-distance-avec-ssh)
- [Cryptographie Asymétrique](https://www.youtube.com/watch?v=MuNyEoU5tSo)
- [How SSH works](https://www.youtube.com/watch?v=ORcvSkgdA58)

## Python

An overview and reminder of the python programming language, with a focus on numpy and pandas manipulation using Jupyter.

### Installation

You most likely have python installed on your Linux system, but it is worthwhile to make sure and to upgrade. Python 3.8, 3.9, or 3.10 are all supported.

There are multiple ways to setup Python.The recommended one is to install Python through Anaconda. Conda, or the platform Anaconda, can be useful on Windows as many packages are built specifically for windows, but not all packages are available via conda.

The installation instructions can be found [on the Anaconda website](https://www.anaconda.com/docs/getting-started/anaconda/install#basic-install-instructions).

It is highly recommended to make a `virtual environment` to manage your python packages. This feature is directly available with `conda` .

For example the following command creates a `conda` virtual environment named `myenv` with Python 3.12:

```bash
conda create -y -n myenv -c conda-forge python=3.12
```

Then activate the newly created environment with:

```bash
conda activate myenv
```

Within the virtual environment all operations implying Python (`pip install` , running `python script.py`...) are isolated from the Python (or "system Python", the Python used by the OS itself) already installed on the laptop. This mitigates the risk of dealing unrecoverable damage to the OS (and avoids to reinstall everything from scratch).

More information can be found in [Conda's docs](https://docs.conda.io/en/latest/).

There are other well-known libraries for virtual environments:

- [Virtualenv](https://docs.python.org/3/tutorial/venv.html) most straight-forward and convenient for new users on Linux with Python already installed.
- [Pipenv](https://pipenv.pypa.io/en/latest/) is an exciting project aimed at Python developers, but it adds additional complexity.

Once you have a virtual environment **created and activated**, please install the following packages for the rest of the Seminars class:

```
numpy
pandas
scipy
matplotlib
jupyter
```

The following packages will also be used in SDD:

```
seaborn
scikit-learn
keras
torch
geos
graphviz
nltk
networkx
statsmodels
pyspark
cython
cma
gym
```

### Jupyter

[Jupyter](https://jupyter.org/) (stands for the three original languages in the project: Julia, Python, and R) is a way to use and develop code interactively in the browser. Once you've installed the jupyter package, you can run a Jupyter notebook by simply running `jupyter notebook`.

For Windows users, you can run Jupyter in the WSL. As explained in [this blog post](https://harshityadav95.medium.com/jupyter-notebook-in-windows-subsystem-for-linux-wsl-8b46fdf0a536), you simply need to execute `jupyter notebook --no-browser` on the WSL and then copy and paste the URL and token generated into a Windows browser.

Some additional packages for improving Jupyter are `nbopen nbdime RISE`. Be sure to read their documentation before installing to verify if these are relevant to you.

### Python Resources

- [Python 3 Documentation](https://docs.python.org/3/index.html)
- [Pip documentation](https://pypi.org/project/pip/)
- [Pandas cheatsheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [Stanford Python and Numpy tutorial](https://cs231n.github.io/python-numpy-tutorial/)
- [Python seminar](https://github.com/xoolive/pyseminar)
- [Google Colab](https://colab.research.google.com/): Jupyter notebooks on the cloud
- [Binder](https://mybinder.org/): Also Jupyter notebooks on the cloud, not hosted by Google
