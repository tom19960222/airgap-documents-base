---
collection: cilium
version: "1.16.7"
title: "Installation Using Kind"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/installation/kind.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="gs_kind"></a>

# Installation Using Kind

This guide uses [kind](https://kind.sigs.k8s.io/) to demonstrate deployment
and operation of Cilium in a multi-node Kubernetes cluster running locally on
Docker.

## Install Dependencies

Included file `Documentation/installation/kind-install-deps.rst`:

1. Install ``docker`` stable as described in
   [Install Docker Engine](https://docs.docker.com/engine/install/)

2. Install ``kubectl`` version >= v1.14.0 as described in the
   [Kubernetes Docs](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

3. Install ``helm`` >= v3.13.0 per Helm documentation:
   [Installing Helm](https://helm.sh/docs/intro/install/)

4. Install ``kind`` >= v0.7.0 per kind documentation:
   [Installation and Usage](https://kind.sigs.k8s.io/#installation-and-usage)

## Configure kind

Included file `Documentation/installation/kind-configure.rst`:

Configuring kind cluster creation is done using a YAML configuration file.
This step is necessary in order to disable the default CNI and replace it with
Cilium.

Create a kind-config.yaml <!-- unresolved-rst-link: kind=download target=./kind-config.yaml --> file based on the
following template. It will create a cluster with 3 worker nodes and 1
control-plane node.

Included file `Documentation/installation/kind-config.yaml`:

```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
- role: worker
- role: worker
- role: worker
networking:
  disableDefaultCNI: true
```

By default, the latest version of Kubernetes from when the kind release was
created is used.

To change the version of Kubernetes being run,  ``image`` has to be defined for
each node. See the
[Node Configuration](https://kind.sigs.k8s.io/docs/user/configuration/#nodes)
documentation for more information.

> **Tip:**
> By default, kind uses the following pod and service subnets:
>
> ```
> Networking.PodSubnet     = "10.244.0.0/16"
> Networking.ServiceSubnet = "10.96.0.0/12"
> ```
>
> If any of these subnets conflicts with your local network address range,
> update the ``networking`` section of the kind configuration file to specify
> different subnets that do not conflict or you risk having connectivity
> issues when deploying Cilium. For example:
>
> ```yaml
> networking:
>   disableDefaultCNI: true
>   podSubnet: "10.10.0.0/16"
>   serviceSubnet: "10.11.0.0/16"
> ```

## Create a cluster

Included file `Documentation/installation/kind-create-cluster.rst`:

To create a cluster with the configuration defined above, pass the
``kind-config.yaml`` you created with the ``--config`` flag of kind.

```shell-session
kind create cluster --config=kind-config.yaml
```

After a couple of seconds or minutes, a 4 nodes cluster should be created.

A new ``kubectl`` context (``kind-kind``) should be added to ``KUBECONFIG`` or, if unset,
to ``${HOME}/.kube/config``:

```shell-session
kubectl cluster-info --context kind-kind
```

> **Note:**
> The cluster nodes will remain in state ``NotReady`` until Cilium is deployed.
> This behavior is expected.

<a id="kind_install_cilium"></a>

## Install Cilium

Included file `Documentation/installation/k8s-install-download-release.rst`:

.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

.. only:: stable

   Setup Helm repository:

   .. code-block:: shell-session

      helm repo add cilium https://helm.cilium.io/

.. only:: not stable

   Download the Cilium release tarball and change to the kubernetes install directory:

   .. parsed-literal::

      curl -LO |SCM_ARCHIVE_LINK|
      tar xzf |SCM_ARCHIVE_FILENAME|
      cd |SCM_ARCHIVE_NAME|/install/kubernetes

Included file `Documentation/installation/kind-preload.rst`:

Preload the ``cilium`` image into each worker node in the kind cluster:

.. parsed-literal::

   docker pull quay.io/cilium/cilium:|IMAGE_TAG|
   kind load docker-image quay.io/cilium/cilium:|IMAGE_TAG|

Then, install Cilium release via Helm:

.. parsed-literal::

   helm install cilium |CHART_RELEASE| \\
      --namespace kube-system \\
      --set image.pullPolicy=IfNotPresent \\
      --set ipam.mode=kubernetes

> **Note:**
> To enable Cilium's Socket LB ([kubeproxy-free](../network/kubernetes/kubeproxy-free.md#kubeproxy-free)), cgroup v2 needs to be
> enabled, and Kind nodes need to run in separate [cgroup namespaces
>](https://man7.org/linux/man-pages/man7/cgroup_namespaces.7.html),
> and these namespaces need to be different from the cgroup namespace
> of the underlying host so that Cilium can attach BPF programs at the right
> cgroup hierarchy. To verify this, run the following commands, and ensure
> that the cgroup values are different:
>
> ```shell-session
> $ docker exec kind-control-plane ls -al /proc/self/ns/cgroup
> lrwxrwxrwx 1 root root 0 Jul 20 19:20 /proc/self/ns/cgroup -> 'cgroup:[4026532461]'
>
> $ docker exec kind-worker ls -al /proc/self/ns/cgroup
> lrwxrwxrwx 1 root root 0 Jul 20 19:20 /proc/self/ns/cgroup -> 'cgroup:[4026532543]'
>
> $ ls -al /proc/self/ns/cgroup
> lrwxrwxrwx 1 root root 0 Jul 19 09:38 /proc/self/ns/cgroup -> 'cgroup:[4026531835]'
> ```
>
> One way to enable cgroup v2 is to set the kernel parameter
> ``systemd.unified_cgroup_hierarchy=1``. To enable cgroup namespaces, a container
> runtime needs to configured accordingly. For example in Docker,
> dockerd's ``--default-cgroupns-mode`` has to be set to ``private``.
>
> Another requirement for the Socket LB on Kind to properly function is that either cgroup v1
> controllers ``net_cls`` and ``net_prio`` are disabled (or cgroup v1 altogether is disabled
> e.g., by setting the kernel parameter ``cgroup_no_v1="all"``), or the host kernel
> should be 5.14 or more recent to include this [fix
>](https://github.com/torvalds/linux/commit/8520e224f547cd070c7c8f97b1fc6d58cff7ccaa).
>
> See the [Pull Request](https://github.com/cilium/cilium/pull/16259) for more details.

Included file `Documentation/installation/k8s-install-validate.rst`:

## Validate the Installation

.. tabs::

   .. tab:: Cilium CLI

     .. include:: /installation/cli-download.rst
     .. include:: /installation/cli-status.rst
     .. include:: /installation/cli-connectivity-test.rst

   .. tab:: Manually

     .. include:: /installation/kubectl-status.rst
     .. include:: /installation/kubectl-connectivity-test.rst

Included file `Documentation/installation/next-steps.rst`:

## Next Steps

 * [hubble_setup](../observability/hubble/setup.md#hubble_setup)
 * [hubble_cli](../observability/hubble/hubble-cli.md#hubble_cli)
 * [hubble_ui](../observability/hubble/hubble-ui.md#hubble_ui)
 * [gs_http](../security/http.md#gs_http)
 * [clustermesh](../internals/security-identities.md#clustermesh)

## Attaching a Debugger

Cilium's Kind configuration enables access to Delve debug server instances running
in the agent and operator Pods by default. See [gs_debugging](../contributing/development/debugging.md#gs_debugging) to learn how
to use it.

## Troubleshooting

### Unable to contact k8s api-server

In the [Cilium agent logs](../operations/troubleshooting.md#ts_agent_logs) you will see:

```
level=info msg="Establishing connection to apiserver" host="https://10.96.0.1:443" subsys=k8s
level=error msg="Unable to contact k8s api-server" error="Get https://10.96.0.1:443/api/v1/namespaces/kube-system: dial tcp 10.96.0.1:443: connect: no route to host" ipAddr="https://10.96.0.1:443" subsys=k8s
level=fatal msg="Unable to initialize Kubernetes subsystem" error="unable to create k8s client: unable to create k8s client: Get https://10.96.0.1:443/api/v1/namespaces/kube-system: dial tcp 10.96.0.1:443: connect: no route to host" subsys=daemon
```

As Kind is running nodes as containers in Docker, they're sharing your host machines' kernel.
If the socket LB wasn't disabled, the eBPF programs attached by Cilium may be out of date
and no longer routing api-server requests to the current ``kind-control-plane`` container.

Recreating the kind cluster and using the helm command [kind_install_cilium](kind.md#kind_install_cilium) will detach the
inaccurate eBPF programs.

### Crashing Cilium agent pods

Check if Cilium agent pods are crashing with following logs. This may indicate
that you are deploying a kind cluster in an environment where Cilium is already
running (for example, in the Cilium development VM). This can also happen if you
have other overlapping BPF ``cgroup`` type programs attached to the parent ``cgroup``
hierarchy of the kind container nodes. In such cases, either tear down Cilium, or manually
detach the overlapping BPF ``cgroup`` programs running in the parent ``cgroup`` hierarchy
by following the [bpftool documentation](https://manpages.ubuntu.com/manpages/focal/man8/bpftool-cgroup.8.html).
For more information, see the [Pull Request](https://github.com/cilium/cilium/pull/16259).

:

```
level=warning msg="+ bpftool cgroup attach /var/run/cilium/cgroupv2 connect6 pinned /sys/fs/bpf/tc/globals/cilium_cgroups_connect6" subsys=datapath-loader
level=warning msg="Error: failed to attach program" subsys=datapath-loader
level=warning msg="+ RETCODE=255" subsys=datapath-loader
```

<a id="gs_kind_cluster_mesh"></a>

## Cluster Mesh

With Kind we can simulate Cluster Mesh in a sandbox too.

### Kind Configuration

This time we need to create (2) ``config.yaml``, one for each kubernetes cluster.
We will explicitly configure their ``pod-network-cidr`` and ``service-cidr`` to not overlap.

Example ``kind-cluster1.yaml``:

```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
- role: worker
- role: worker
- role: worker
networking:
  disableDefaultCNI: true
  podSubnet: "10.0.0.0/16"
  serviceSubnet: "10.1.0.0/16"
```

Example ``kind-cluster2.yaml``:

```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
- role: worker
- role: worker
- role: worker
networking:
  disableDefaultCNI: true
  podSubnet: "10.2.0.0/16"
  serviceSubnet: "10.3.0.0/16"
```

### Create Kind Clusters

We can now create the respective clusters:

```shell-session
kind create cluster --name=cluster1 --config=kind-cluster1.yaml
kind create cluster --name=cluster2 --config=kind-cluster2.yaml
```

### Setting up Cluster Mesh

We can deploy Cilium, and complete setup by following the Cluster Mesh guide
with [gs_clustermesh](../network/clustermesh/clustermesh.md#gs_clustermesh). For Kind, we'll want to deploy the ``NodePort`` service into the ``kube-system`` namespace.
