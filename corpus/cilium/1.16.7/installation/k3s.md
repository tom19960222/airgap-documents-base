---
collection: cilium
version: "1.16.7"
title: "Installation Using K3s"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/installation/k3s.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="k3s_install"></a>

# Installation Using K3s

This guide walks you through installation of Cilium on [K3s](https://k3s.io/),
a highly available, certified Kubernetes distribution designed for production
workloads in unattended, resource-constrained, remote locations or inside IoT
appliances.

Cilium is presently supported on amd64 and arm64 architectures.

## Install a Master Node

The first step is to install a K3s master node making sure to disable support
for the default CNI plugin and the built-in network policy enforcer:

> **Note:**
> If running Cilium in [kubeproxy-free](../network/kubernetes/kubeproxy-free.md#kubeproxy-free) mode, add option ``--disable-kube-proxy``

```shell-session
curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC='--flannel-backend=none --disable-network-policy' sh -
```

## Install Agent Nodes (Optional)

K3s can run in standalone mode or as a cluster making it a great choice for
local testing with multi-node data paths. Agent nodes are joined to the master
node using a node-token which can be found on the master node at
``/var/lib/rancher/k3s/server/node-token``.

Install K3s on agent nodes and join them to the master node making sure to
replace the variables with values from your environment:

```shell-session
curl -sfL https://get.k3s.io | K3S_URL='https://${MASTER_IP}:6443' K3S_TOKEN=${NODE_TOKEN} sh -
```

Should you encounter any issues during the installation, please refer to the
[troubleshooting_k8s](../network/kubernetes/troubleshooting.md#troubleshooting_k8s) section and/or seek help on Cilium Slack <!-- unresolved-rst-link: kind=named target=Cilium Slack -->.

Please consult the Kubernetes [k8s_requirements](../network/kubernetes/requirements.md#k8s_requirements) for information on  how
you need to configure your Kubernetes cluster to operate with Cilium.

## Configure Cluster Access

For the Cilium CLI to access the cluster in successive steps you will need to
use the ``kubeconfig`` file stored at ``/etc/rancher/k3s/k3s.yaml`` by setting
the ``KUBECONFIG`` environment variable:

```shell-session
export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
```

## Install Cilium

Included file `Documentation/installation/cli-download.rst`:

> **Warning:**
> Make sure you install [cilium-cli v0.15.0](https://github.com/cilium/cilium-cli/releases/tag/v0.15.0)
> or later. The rest of instructions do not work with older versions of
> cilium-cli. To confirm the cilium-cli version that's installed in your system,
> run:
>
> ```shell-session
> cilium version --client
> ```
>
> See [Cilium CLI upgrade notes](../operations/upgrade.md#upgrade_cilium_cli_helm_mode) for more details.

Install the latest version of the Cilium CLI. The Cilium CLI can be used to
install Cilium, inspect the state of a Cilium installation, and enable/disable
various features (e.g. clustermesh, Hubble).

.. tabs::
   .. group-tab:: Linux

     .. code-block:: shell-session

       CILIUM_CLI_VERSION=$(curl -s https://raw.githubusercontent.com/cilium/cilium-cli/main/stable.txt)
       CLI_ARCH=amd64
       if [ "$(uname -m)" = "aarch64" ]; then CLI_ARCH=arm64; fi
       curl -L --fail --remote-name-all https://github.com/cilium/cilium-cli/releases/download/${CILIUM_CLI_VERSION}/cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}
       sha256sum --check cilium-linux-${CLI_ARCH}.tar.gz.sha256sum
       sudo tar xzvfC cilium-linux-${CLI_ARCH}.tar.gz /usr/local/bin
       rm cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}

   .. group-tab:: macOS

     .. code-block:: shell-session

       CILIUM_CLI_VERSION=$(curl -s https://raw.githubusercontent.com/cilium/cilium-cli/main/stable.txt)
       CLI_ARCH=amd64
       if [ "$(uname -m)" = "arm64" ]; then CLI_ARCH=arm64; fi
       curl -L --fail --remote-name-all https://github.com/cilium/cilium-cli/releases/download/${CILIUM_CLI_VERSION}/cilium-darwin-${CLI_ARCH}.tar.gz{,.sha256sum}
       shasum -a 256 -c cilium-darwin-${CLI_ARCH}.tar.gz.sha256sum
       sudo tar xzvfC cilium-darwin-${CLI_ARCH}.tar.gz /usr/local/bin
       rm cilium-darwin-${CLI_ARCH}.tar.gz{,.sha256sum}

   .. group-tab:: Other

     See the full page of [releases](https://github.com/cilium/cilium-cli/releases/latest).

.. only:: not stable

   Clone the Cilium GitHub repository so that the Cilium CLI can access the
   latest unreleased Helm chart from the main branch:

   .. parsed-literal::

      git clone git@github.com:cilium/cilium.git
      cd cilium

> **Note:**
> Install Cilium with ``--set=ipam.operator.clusterPoolIPv4PodCIDRList="10.42.0.0/16"`` to match k3s default podCIDR 10.42.0.0/16.

> **Note:**
> If you are using Rancher Desktop, you may need to override the cni path by adding the additional flag ``--set 'cni.binPath=/usr/libexec/cni'``

Install Cilium by running:

.. parsed-literal::

   cilium install |CHART_VERSION| --set=ipam.operator.clusterPoolIPv4PodCIDRList="10.42.0.0/16"

## Validate the Installation

Included file `Documentation/installation/cli-status.rst`:

To validate that Cilium has been properly installed, you can run

```shell-session
$ cilium status --wait
   /¯¯\
/¯¯\__/¯¯\    Cilium:         OK
\__/¯¯\__/    Operator:       OK
/¯¯\__/¯¯\    Hubble:         disabled
\__/¯¯\__/    ClusterMesh:    disabled
   \__/

DaemonSet         cilium             Desired: 2, Ready: 2/2, Available: 2/2
Deployment        cilium-operator    Desired: 2, Ready: 2/2, Available: 2/2
Containers:       cilium-operator    Running: 2
                  cilium             Running: 2
Image versions    cilium             quay.io/cilium/cilium:v1.9.5: 2
                  cilium-operator    quay.io/cilium/operator-generic:v1.9.5: 2
```

Included file `Documentation/installation/cli-connectivity-test.rst`:

Run the following command to validate that your cluster has proper network
connectivity:

```shell-session
$ cilium connectivity test
ℹ️  Monitor aggregation detected, will skip some flow validation steps
✨ [k8s-cluster] Creating namespace for connectivity check...
(...)
---------------------------------------------------------------------------------------------------------------------
📋 Test Report
---------------------------------------------------------------------------------------------------------------------
✅ 69/69 tests successful (0 warnings)
```

> **Note:**
> The connectivity test may fail to deploy due to too many open files in one
> or more of the pods. If you notice this error, you can increase the
> ``inotify`` resource limits on your host machine (see
> [Pod errors due to "too many open files"](https://kind.sigs.k8s.io/docs/user/known-issues/#pod-errors-due-to-too-many-open-files)).

Congratulations! You have a fully functional Kubernetes cluster with Cilium. 🎉

Included file `Documentation/installation/next-steps.rst`:

## Next Steps

 * [hubble_setup](../observability/hubble/setup.md#hubble_setup)
 * [hubble_cli](../observability/hubble/hubble-cli.md#hubble_cli)
 * [hubble_ui](../observability/hubble/hubble-ui.md#hubble_ui)
 * [gs_http](../security/http.md#gs_http)
 * [clustermesh](../internals/security-identities.md#clustermesh)
