---
collection: cilium
version: "1.16.7"
title: "Installation k0s Using k0sctl"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/installation/k0s.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="k0s_install"></a>

# Installation k0s Using k0sctl

This guide walks you through installation of Cilium on [k0s](https://k0sproject.io/),
an open source, all-inclusive Kubernetes distribution,
which is configured with all of the features needed to build a Kubernetes cluster.

Cilium is presently supported on amd64 and arm64 architectures.

## Install a Master Node

Ensure you have the k0sctl binary installed locally.

Setup your VMs:

How to do this is out of the scope of this guide, please refer to your favorite virtualization tool.
After deploying the VMs, export their IP addresses to environment variables (see example below). These will be used in a later step.

```shell-session
export node1_IP=192.168.2.1
export node2_IP=192.168.2.2
export node3_IP=192.168.2.3
```

Prepare the yaml configuration file k0sctl will use:

```shell-session
# The following command assumes the user has deployed 3 VMs
# with the default user "k0s" using the default ssh-key (without passphrase)
k0sctl init --k0s -n "myk0scluster" -u "k0s" -i "~/.ssh/id_rsa" -C "1" "${node1_IP}" "${node2_IP}" "${node3_IP}" > k0s-myk0scluster-config.yaml
```

Next step is editing ``k0s-myk0scluster-config.yaml``:

```
# replace
 ...
   provider: kube-router
 ...
# with
 ...
   provider: custom
 ...
```

Finally apply the config file:

```shell-session
k0sctl apply --config k0s-myk0scluster-config.yaml --no-wait
```

> **Note:**
> If running Cilium in [kubeproxy-free](../network/kubernetes/kubeproxy-free.md#kubeproxy-free) mode disable kube-proxy in the k0s config file
>
> ```shell-session
> # edit k0s-myk0scluster-config.yaml
>
> # replace
> ...
>    network:
>       kubeProxy:
>          disabled: false
> ...
> # with
> ...
>    network:
>       kubeProxy:
>          disabled: true
> ...
> ```

## Configure Cluster Access

For the Cilium CLI to access the cluster in successive steps you will need to
generate the ``kubeconfig`` file, store it in ``~/.kube/k0s-mycluster.config`` and setting
the ``KUBECONFIG`` environment variable:

```shell-session
k0sctl kubeconfig --config k0s-myk0scluster-config.yaml > ~/.kube/k0s-mycluster.config
export KUBECONFIG=~/.kube/k0s-mycluster.config
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

Install Cilium by running:

.. parsed-literal::

   cilium install |CHART_VERSION|

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
