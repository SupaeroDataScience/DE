# Bureau d'études Docker - Déploiement

## 3.1 - Introduction

In the previous sessions, you learned Docker basics: building images from Dockerfiles, running containers, and pushing images to a registry.

In this session, we focus on **deployment**: taking a containerized application and running it on a cloud VM that's accessible from the internet. You won't need to write any Dockerfile - the image is already built. The goal is to understand the deployment workflow.

## 3.2 - The Application

The application files are already available in the `be-docker-deploy/` folder of your codespace. This is a Streamlit app that visualizes neural network activation functions - useful reference material after your Deep Learning class.

Let's test it locally first:

```bash
cd be-docker-deploy
pip install -r requirements.txt
streamlit run app.py
```

Access the app on port 8501 in your codespace (click the port forwarding notification or use the Ports tab).

Explore the interface, then quit the server with `Ctrl+C`.

!!! question
    What does this application visualize? How could it help you understand neural networks?

## 3.3 - The Docker Image

For this exercise, the Docker image has been **pre-built and pushed** to our shared Artifact Registry. You already learned how to build and push images in the previous workshops - this session focuses purely on deployment.

The pre-built image is:

```
europe-docker.pkg.dev/isae-sdd-481407/isae-sdd-de-2526-docker/demo-streamlit-activation-function:1.0
```

!!! note "For teachers"
    If you need to rebuild the image, the source files are in `be-docker-deploy/`:

    ```bash
    cd be-docker-deploy
    docker build -t europe-docker.pkg.dev/isae-sdd-481407/isae-sdd-de-2526-docker/demo-streamlit-activation-function:1.0 .
    docker push europe-docker.pkg.dev/isae-sdd-481407/isae-sdd-de-2526-docker/demo-streamlit-activation-function:1.0
    ```

## 3.4 - Deploy to GCE VM

We'll create a VM that automatically runs our container at boot - no SSH required.

Run this command, replacing `FIRSTNAME` with your unique identifier (e.g., `streamlit-vm-marie`):

```bash
gcloud compute instances create-with-container streamlit-vm-FIRSTNAME \
    --project=isae-sdd-481407 \
    --zone=europe-west9-a \
    --machine-type=e2-small \
    --image-family=cos-stable --image-project=cos-cloud \
    --boot-disk-size=10GB \
    --container-image=europe-docker.pkg.dev/isae-sdd-481407/isae-sdd-de-2526-docker/demo-streamlit-activation-function:1.0 \
    --container-restart-policy=always \
    --tags=http-server-8501
```

**Key differences from previous VM creation:**

| Flag | Purpose |
|------|---------|
| `--container-image` | Deploys the container automatically at boot |
| `--image=.../cos-...` | Uses Container-Optimized OS (lightweight, designed for containers) |
| `--tags=http-server-8501` | Labels the VM so firewall rules can target it |
| `--container-restart-policy=always` | Restarts the container if it crashes |

## 3.5 - Expose to the Web

By default, GCP blocks all incoming traffic to VMs. A **firewall rule** opens specific ports.

A firewall rule for port 8501 already exists in our project:

```bash
# This rule already exists - no need to run it
# gcloud compute firewall-rules create allow-8501 \
#     --allow=tcp:8501 \
#     --target-tags=http-server-8501
```

**How it works:**

- The rule `allow-8501` permits TCP traffic on port 8501
- `--target-tags=http-server-8501` applies only to VMs with that tag
- Your VM has this tag (we set it with `--tags` above)

**Get your VM's external IP:**

```bash
gcloud compute instances list --filter="name=streamlit-vm-FIRSTNAME"
```

Or find it in the Google Cloud Console: **Compute Engine** > **VM instances**

**Access your app:**

Open your browser and go to: `http://EXTERNAL_IP:8501`

!!! warning
    This won't work on ISAE wifi due to network restrictions. Try eduroam or mobile data.

## 3.6 - Going to Production (Conceptual)

### Current Situation

Accessing via `http://IP:8501` works for learning, but it isn't production-ready:

- IP addresses are hard to remember
- IPs can change when VMs are recreated
- No encryption (HTTP, not HTTPS)
- Non-standard port (8501 instead of 80/443)

### sslip.io Trick

For a slightly more readable URL, you can use [sslip.io](https://sslip.io) - a free DNS service that resolves hostnames to embedded IP addresses.

If your VM's IP is `35.205.123.45`, you can access it via:

```
http://35-205-123-45.sslip.io:8501
```

How it works: sslip.io resolves `35-205-123-45.sslip.io` to `35.205.123.45`.

You still need to specify port 8501, but at least you have a hostname instead of raw numbers.

### What's Missing for Production

A production setup typically looks like this:

```
┌──────────┐    ┌─────────────────┐    ┌─────────┐    ┌───────────┐
│   User   │───▶│  Load Balancer  │───▶│   VM    │───▶│ Container │
└──────────┘    │   (HTTPS:443)   │    │ (:8501) │    │  (:8501)  │
                └─────────────────┘    └─────────┘    └───────────┘
                        │
                ┌───────┴───────┐
                │ SSL Certificate│
                │ Custom Domain  │
                │ (myapp.com)    │
                └────────────────┘
```

**What we're missing:**

- **HTTPS**: Encrypted connection (SSL/TLS certificate)
- **Standard ports**: 80 (HTTP) or 443 (HTTPS) instead of 8501
- **Custom domain**: `myapp.com` instead of IP address
- **Load balancing**: Distribute traffic, handle failures

### Why We're Not Doing This

Setting up production infrastructure requires:

- A domain name (cost + DNS configuration)
- SSL certificates (Let's Encrypt or paid)
- Load balancer configuration (complexity + cost)

For learning purposes, accessing via IP:port is sufficient.

### What's Next

In the next session, we'll discover **Cloud Run** which provides:

- Automatic HTTPS with a public URL
- No infrastructure to manage
- Auto-scaling based on traffic
- Pay only when your app is running

## 3.7 - Cleanup

Delete your VM to avoid unnecessary charges:

```bash
gcloud compute instances delete streamlit-vm-FIRSTNAME --zone=europe-west9-a
```

Confirm the deletion when prompted.

!!! note
    The firewall rule stays - it's shared across all students and doesn't cost anything.

## 3.8 - Conclusion

!!! success
    You have successfully deployed a containerized webapp to a public VM!

**What you learned:**

- Deploying containers to GCE VMs with Container-Optimized OS
- How firewall rules control network access
- Using pre-built images from Artifact Registry
- Conceptual understanding of production infrastructure (load balancers, domains, HTTPS)

**Next steps:**

- Finish previous hands-on if time remains (docker-compose section)
- Next session: Cloud Run for fully managed deployments
