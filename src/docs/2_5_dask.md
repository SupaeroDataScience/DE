# Dask on Kubernetes

In this class, we focus on getting a [Dask](https://docs.dask.org/en/latest/) cluster running in Kubernetes, which we will then use in the [Dask project](https://supaerodatascience.github.io/DE/2_6_project.html). Dask is a parallel computing library in Python which integrates well with machine learning tools like scikit-learn.

This class builds on the
[orchestration](https://supaerodatascience.github.io/DE/1_5_deployment.html)
class, going into further detail on K8S specifics.

[Kubernetes](https://supaerodatascience.github.io/DE/slides/2_3_kubernetes.html#/)

[Dask presentation](https://docs.google.com/presentation/d/e/2PACX-1vSTH2kAR0DCR0nw8pFBe5kuYbOk3inZ9cQfZbzOIRjyzQoVaOoMfI2JONGBz-qsvG_P6g050ddHxSXT/pub?start=false&loop=false&delayms=60000#slide=id.p)

Students will use GCP for this class. Be sure to stop your cluster after class to conserve GCP credits.

Additional resources can be found in the [dask documentation](https://docs.dask.org/en/latest/setup/kubernetes.html).

# Deploying a Dask Hub

This material is taken from the following docs:

+ [https://docs.dask.org/en/latest/setup/kubernetes-helm.html](https://docs.dask.org/en/latest/setup/kubernetes-helm.html)
+ [https://zero-to-jupyterhub.readthedocs.io/en/latest/kubernetes/setup-kubernetes.html](https://zero-to-jupyterhub.readthedocs.io/en/latest/kubernetes/setup-kubernetes.html)
+ [https://zero-to-jupyterhub.readthedocs.io/en/latest/kubernetes/setup-helm.html](https://zero-to-jupyterhub.readthedocs.io/en/latest/kubernetes/setup-helm.html)

## Creating a Kubernetes Cluster

First, you need to enable the Kubernetes API if not already done:

+ Go to [console.cloud.google.com](https://console.cloud.google.com/)
+ Select the Kubernetes Engine in the menu
+ Enable the API if not already done.

Then you'll need a terminal with `gcloud` and `kubectl`. The simplest is just to use the Google Cloud Shell from console.cloud.google.com. If you prefer, you can follow the links above to find how to install everything on your computer.

Ask Google Cloud to create a managed Kubernetes cluster and a default node pool to get nodes from:

```
gcloud container clusters create \
  --machine-type n1-standard-4 \
  --enable-autoscaling \
  --min-nodes 1 \
  --max-nodes 10 \
  --num-nodes 1 \
  --zone europe-west1-b \
  --cluster-version 1.23 \
  dask-hub-k8s
```

Yhis will take a few minutes (maybe 2 or 3).

```
gcloud container clusters list
```

You can then test if the cluster is running:

```
kubectl get node
```

Then get permissions to perform all administrative actions needed.

**⚠️Don't forget to replace your email below.⚠️**

```
kubectl create clusterrolebinding cluster-admin-binding \
  --clusterrole=cluster-admin \
  --user=<GOOGLE-EMAIL-ACCOUNT>
```

## Setting up Helm

From your Google Cloud Shell or terminal:

```
curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash
helm list
```

should return:

```
NAME    NAMESPACE       REVISION        UPDATED STATUS  CHART   APP VERSION
```

## Helm install a Dask Hub

Default Daskhub configuration uses dask-gateway, which is here to handle multiple users with fine grain authorisations. We don't need this, and it iss a little more complicated setup than what we'll do.

Instead, we'll deploy a Daskhub with dask-kubernetes, which assumes some authorisations inside the Pods of the Kubernetes cluster (potential security leak), but is more straightforward for our usage.

Verify that you’ve set up a Kubernetes cluster and added Dask’s helm charts:

```
helm repo add dask https://helm.dask.org/
helm repo update
```

Generate token to configure Jupyterhub:

```
openssl rand -hex 32  > token1.txt
cat token1.txt
```

Create the file below (for example using vim or cloud shell editor) and substitute the <token-1> value.

```
# file: daskhub-config.yaml
jupyterhub:
  proxy:
    secretToken: "<token-1>"
  scheduling:
    podPriority:
      enabled: true
    userPlaceholder:
      # Specify three dummy user pods will be used as placeholders
      replicas: 1
    userScheduler:
      enabled: true
  singleuser:
    serviceAccountName: daskkubernetes
    image:
      name: guillaumeeb/pangeo-ml-notebook # Image to use for singleuser environment. Must include dask-kubernetes.
      tag: 2021.11.14

dask-gateway:
  enabled: false
  gateway:
    auth:
      type: simple
      simple:
        password: "unused"

dask-kubernetes:
  enabled: true
```

Now we just install Dask Hub:

```
helm upgrade --wait --install --render-subchart-notes \
    --namespace daskhub \
    --create-namespace \
    dhub dask/daskhub \
    --values=daskhub-config.yaml
```

This will again take a few minutes.

```
helm list -n daskhub
```

Check install and go to Jupyter!

To get the public IP of your hub deployment:

```
kubectl --namespace=daskhub get service proxy-public
```

Get the external IP, and open it in your browser. You should be able to login with any username/password
Ensure Dask is working, and K8S mecanisms too!

## Create a dask-kubernetes cluster

Create a yaml file within the Jupyterhub interface:

```
# worker-spec.yaml

kind: Pod
metadata:
  labels:
    foo: bar
spec:
  restartPolicy: Never
  containers:
  - image: guillaumeeb/pangeo-ml-notebook:2021.11.14
    imagePullPolicy: IfNotPresent
    args: [dask-worker, --nthreads, '2', --no-dashboard, --memory-limit, 6GB, --death-timeout, '60']
    name: dask
    env:
      - name: EXTRA_PIP_PACKAGES
        value: xgboost
    resources:
      limits:
        cpu: "2"
        memory: 6G
      requests:
        cpu: "1.7"
        memory: 6G
```

Just open a notebook in your newly created Dask enabled hub, and try to copy and past the following cells:

Set some config to ease usage.

```python
import dask
import dask.distributed  # populate config with distributed defaults
import dask_kubernetes

dask.config.set({"kubernetes.worker-template-path": "worker-spec.yaml"})
dask.config.set({"distributed.dashboard.link": "{JUPYTERHUB_SERVICE_PREFIX}proxy/{port}/status"})
```

Create a cluster object.

```python
from dask_kubernetes import KubeCluster

cluster = KubeCluster(deploy_mode='local') # Scheduler is started in the notebook process
cluster
```

This should display a fancy widget. You can open the Dask Dashboard from here.

Now scale the cluster to get Dask-workers and connect to it.

```python
cluster.scale(20)
```

```python
from distributed import Client

client = Client(cluster)
client
```

What's happening in your K8S cluster after some seconds/minutes?
Launch some computation, what about Pi?

We'll use Dask array, a Numpy extension, for this:

```python
import dask.array as da

sample = 10_000_000_000  # <- this is huge!
xxyy = da.random.uniform(-1, 1, size=(2, sample))
norm = da.linalg.norm(xxyy, axis=0)
summ = da.sum(norm <= 1)
insiders = summ.compute()
pi = 4 * insiders / sample
print("pi ~= {}".format(pi))
```

How many workers did you get? Why?

Now just close the cluster.

```python
cluster.close()
```

What happens after a few minutes?

## Deleting a Kubernetes Cluster

Get your cluster name and region

```
gcloud container clusters list
```

Delete your kubernetes cluster

```
gcloud container clusters delete <YOUR_CLUSTER_NAME> --region <YOUR_CLUSTER_REGION>
```

