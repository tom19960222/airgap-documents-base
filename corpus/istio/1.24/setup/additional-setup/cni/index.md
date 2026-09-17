---
collection: istio
version: "1.24"
title: "Install the Istio CNI node agent"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/additional-setup/cni/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Install and use the Istio CNI node agent, allowing operators to deploy workloads with lower privilege."
---
The Istio [shortcode gloss="cni"]CNI node agent is used to configure traffic redirection for pods in the mesh. It runs as a DaemonSet, on every node, with elevated privileges. The CNI node agent is used by both Istio data plane modes.

For the sidecar data plane mode, the Istio CNI node agent is optional. It removes the requirement of running privileged init containers in every pod in the mesh, replacing that model with a single privileged node agent pod on each Kubernetes node.

The Istio CNI node agent is **required** in the ambient data plane mode.

This guide is focused on using the Istio CNI node agent as an optional part of the sidecar data plane mode. Consult [the ambient mode documentation](../../../ambient/_index.md) for information on using the ambient data plane mode.

> **Tip:**
>
> Note: The Istio CNI node agent _does not_ replace your cluster's existing [shortcode gloss="cni"]CNI. Among other things, it installs a _chained_ CNI plugin, which is designed to be layered on top of another, previously-installed primary interface CNI, such as [Calico](https://docs.projectcalico.org), or the cluster CNI used by your cloud provider.
> See [compatibility with CNIs](index.md#compatibility-with-other-cnis) for details.

Follow this guide to install, configure, and use the Istio CNI node agent with the sidecar data plane mode.

## How sidecar traffic redirection works

### Using the init container (without the Istio CNI node agent)

By default Istio injects an init container, `istio-init`, in pods deployed in
the mesh. The `istio-init` container sets up the pod network traffic
redirection to/from the Istio sidecar proxy. This requires the user or
service-account deploying pods to the mesh to have sufficient Kubernetes RBAC
permissions to deploy [containers with the `NET_ADMIN` and `NET_RAW` capabilities](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-capabilities-for-a-container).

### Using the Istio CNI node agent

Requiring Istio users to have elevated Kubernetes RBAC permissions is
problematic for some organizations' security compliance, as is the requirement to deploy privileged init containers with every workload.

The `istio-cni` node agent is effectively a replacement for the `istio-init` container that enables the same
networking functionality, but without requiring the use or deployment of privileged init containers in every workload. Instead, `istio-cni` itself runs as a single privileged pod on the node. It uses this privilege to install a [chained CNI plugin](https://www.cni.dev/docs/spec/#section-2-execution-protocol) on the node, which is invoked after your "primary" interface CNI plugin. CNI plugins are invoked dynamically by Kubernetes as a privileged process on the host node whenever a new pod is created, and are able to configure pod networking.

The Istio chained CNI plugin always runs after the primary interface plugins, identifies user application pods with sidecars requiring traffic redirection, and sets up redirection in the Kubernetes pod lifecycle's network setup phase, thereby removing the need for privileged init containers, as well as the [requirement for `NET_ADMIN` and `NET_RAW` capabilities](../../../ops/deployment/application-requirements/index.md)
for users and pod deployments.

![Istio CNI](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/additional-setup/cni/cni.svg)

## Prerequisites for use

1. Install Kubernetes with a correctly-configured primary interface CNI plugin. As [supporting CNI plugins is required to implement the Kubernetes network model](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/), you probably already have this if you have a reasonably recent Kubernetes cluster with functional pod networking.
    * AWS EKS, Azure AKS, and IBM Cloud IKS clusters have this capability.
    * Google Cloud GKE clusters have CNI enabled when any of the following features are enabled:
       [network policy](https://cloud.google.com/kubernetes-engine/docs/how-to/network-policy),
       [intranode visibility](https://cloud.google.com/kubernetes-engine/docs/how-to/intranode-visibility),
       [workload identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity),
       [pod security policy](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies#overview),
       or [dataplane v2](https://cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2).
    * Kind has CNI enabled by default.
    * OpenShift has CNI enabled by default.

1. Install Kubernetes with the [ServiceAccount admission controller](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#serviceaccount) enabled.
    * The Kubernetes documentation highly recommends this for all Kubernetes installations
      where `ServiceAccounts` are utilized.

## Installing the CNI node agent

### Install Istio with the `istio-cni` component

In most environments, a basic Istio cluster with the `istio-cni` component enabled can be installed using the following commands:

**Tabset (gateway-install-type):**

**Tab: IstioOperator**

```bash
$ cat <<EOF > istio-cni.yaml
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
spec:
  components:
    cni:
      namespace: istio-system
      enabled: true
EOF
$ istioctl install -f istio-cni.yaml -y
```

**Tab: Helm**

```bash
$ helm install istio-cni istio/cni -n istio-system --wait
```

This will deploy an `istio-cni` DaemonSet into the cluster, which will create one Pod on every active node, deploy the Istio CNI plugin binary on each, and set up the necessary node-level configuration for the plugin.
The CNI DaemonSet runs with [`system-node-critical`](https://kubernetes.io/docs/tasks/administer-cluster/guaranteed-scheduling-critical-addon-pods/) `PriorityClass`. This is because it is the only means of actually reconfiguring pod networking to add them to the Istio mesh.

> **Tip:**
>
> You can install `istio-cni` into any Kubernetes namespace, but the namespace must allow pods with the `system-node-critical` PriorityClass to be scheduled in it. Some cloud providers (notably GKE) by default disallow the scheduling of `system-node-critical` pods in any namespace but specific ones, such as `kube-system`.
>
> You may either install `istio-cni` into `kube-system`, or (recommended) define a ResourceQuota for your GKE cluster that allows the use of `system-node-critical` pods inside `istio-system`. See [here](../../../ambient/install/platform-prerequisites/index.md#google-kubernetes-engine-gke) for more details.

Note that if installing `istiod` with the Helm chart according to the [Install with Helm](../../install/helm/index.md#installation-steps) guide, you must install `istiod` with the following extra override value, in order to disable the privileged init container injection:

```bash
$ helm install istiod istio/istiod -n istio-system --set pilot.cni.enabled=true --wait
```

### Additional configuration

In addition to the above basic configuration there are additional configuration flags that can be set:

* `values.cni.cniBinDir` and `values.cni.cniConfDir` configure the directory paths to install the plugin binary and create plugin configuration.
* `values.cni.cniConfFileName` configures the name of the plugin configuration file.
* `values.cni.chained` controls whether to configure the plugin as a chained CNI plugin.

Normally, these do not need to be changed, but some platforms may use nonstandard paths. Please check the guidelines for your specific platform, if any, [here](../../../ambient/install/platform-prerequisites/index.md).

> **Tip:**
>
> There is a time gap between a node becomes schedulable and the Istio CNI plugin becomes ready on that node.
> If an application pod starts up during this time, it is possible that traffic redirection is not properly set up and traffic would be able to bypass the Istio sidecar.
>
> This race condition is mitigated for the sidecar data plane mode by a "detect and repair" method.
> Please take a look at [race condition & mitigation](index.md#race-condition--mitigation) section to understand the implication of this mitigation, and for configuration instructions.

### Handling init container injection for revisions

When installing revisioned control planes with the CNI component enabled,
`values.pilot.cni.enabled=true` needs to be set for each installed revision, so that the sidecar injector does not attempt inject the `istio-init` init container for that revision.

```yaml
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
spec:
  revision: REVISION_NAME
  ...
  values:
    pilot:
      cni:
        enabled: true
  ...
```

The CNI plugin at version `1.x` is compatible with control plane at version `1.x-1`, `1.x`, and `1.x+1`,
which means CNI and control plane can be upgraded in any order, as long as their version difference is within one minor version.

## Operating clusters with the CNI node agent installed

### Upgrading

When upgrading Istio with [in-place upgrade](../../upgrade/in-place/index.md), the
CNI component can be upgraded together with the control plane using one `IstioOperator` resource.

When upgrading Istio with [canary upgrade](../../upgrade/canary/index.md), because the CNI component runs as a cluster singleton,
it is recommended to operate and upgrade the CNI component separately from the revisioned control plane.

The following `IstioOperator` can be used to upgrade the CNI component independently.

```yaml
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
spec:
  profile: empty # Do not include other components
  components:
    cni:
      enabled: true
  values:
    cni:
      excludeNamespaces:
        - istio-system
```

This is not a problem for Helm as the istio-cni is installed separately, and can be upgraded via Helm:

```bash
$ helm upgrade istio-cni istio/cni -n istio-system --wait
```

### Race condition & mitigation

The Istio CNI DaemonSet installs the CNI network plugin on every node.
However, a time gap exists between when the DaemonSet pod gets scheduled onto a node, and the CNI plugin is installed and ready to be used.
There is a chance that an application pod starts up during that time gap, and the `kubelet` has no knowledge of the Istio CNI plugin.
The result is that the application pod comes up without Istio traffic redirection and bypasses Istio sidecar.

To mitigate the race between an application pod and the Istio CNI DaemonSet,
an `istio-validation` init container is added as part of the sidecar injection,
which detects if traffic redirection is set up correctly, and blocks the pod starting up if not.
The CNI DaemonSet will detect and handle any pod stuck in such state; how the pod is handled is dependent on configuration described below.
This mitigation is enabled by default and can be turned off by setting `values.cni.repair.enabled` to false.

This repair capability can be further configured with different RBAC permissions to help mitigate the theoretical attack vector detailed in [`ISTIO-SECURITY-2023-005`](https://istio.io/v1.24/news/security/istio-security-2023-005/) <!-- unresolved-site-link: route=/news/security/istio-security-2023-005 -->.  By setting the below fields to true/false as required, you can select the Kubernetes RBAC permissions granted to the Istio CNI.

|Configuration                    | Roles       | Behavior on Error                                                                                                                           | Notes
|---------------------------------|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-------
|`values.cni.repair.deletePods`   | DELETE pods | Pods are deleted, when rescheduled they will have the correct configuration.                                                                  | Default in 1.20 and older
|`values.cni.repair.labelPods`    | UPDATE pods | Pods are only labeled.  User will need to take manual action to resolve.                                                                      |
|`values.cni.repair.repairPods`   | None        | Pods are dynamically reconfigured to have appropriate configuration. When the container restarts, the pod will continue normal execution.     | Default in 1.21 and newer

### Traffic redirection parameters

To redirect traffic in the application pod's network namespace to/from the Istio proxy sidecar,
the Istio CNI plugin configures the namespace's iptables.
You can adjust traffic redirection parameters using the same pod annotations as normal,
such as ports and IP ranges to be included or excluded from redirection.
See [resource annotations](https://istio.io/v1.24/docs/reference/config/annotations) <!-- unresolved-site-link: route=/docs/reference/config/annotations --> for available parameters.

### Compatibility with application init containers

The Istio CNI plugin may cause networking connectivity problems for any application init containers in sidecar data plane mode. When using Istio CNI, `kubelet`
starts a pod with the following steps:

1. The default interface CNI plugin sets up pod network interfaces and assigns pod IPs.
1. The Istio CNI plugin sets up traffic redirection to the Istio sidecar proxy within the pod.
1. All init containers execute and complete successfully.
1. The Istio sidecar proxy starts in the pod along with the pod's other containers.

Init containers execute before the sidecar proxy starts, which can result in traffic loss during their execution.
Avoid this traffic loss with one of the following settings:

1. Set the `uid` of the init container to `1337` using `runAsUser`.
  `1337` is the [`uid` used by the sidecar proxy](../../../ops/deployment/application-requirements/index.md#pod-requirements).
   Traffic sent by this `uid` is not captured by the Istio's `iptables` rule.
   Application container traffic will still be captured as usual.
1. Set the `traffic.sidecar.istio.io/excludeOutboundIPRanges` annotation to disable redirecting traffic to any
   CIDRs the init containers communicate with.
1. Set the `traffic.sidecar.istio.io/excludeOutboundPorts` annotation to disable redirecting traffic to the
   specific outbound ports the init containers use.

> **Tip:**
>
> You must use the `runAsUser 1337` workaround if [DNS proxying](../../../ops/configuration/traffic-management/dns-proxy/index.md) is enabled, and an init container sends traffic to a host name which requires DNS resolution.

> **Tip:**
>
> Some platforms (e.g. OpenShift) do not use `1337` as the sidecar `uid` and instead use a pseudo-random number, that is only known at runtime. In such cases, you can instruct the proxy to run as a predefined `uid` by leveraging the [custom injection feature](../sidecar-injection/index.md#customizing-injection), and use that same `uid` for the init container.

> **Warning:**
>
> Please use traffic capture exclusions with caution, since the IP/port exclusion annotations not only apply to init container traffic,
> but also application container traffic. i.e. application traffic sent to the configured IP/port will bypass the Istio sidecar.

### Compatibility with other CNIs

The Istio CNI plugin follows the [CNI spec](https://www.cni.dev/docs/spec/#container-network-interface-cni-specification), and should be compatible with any CNI, container runtime,
or other plugin that also follows the spec.

The Istio CNI plugin operates as a chained CNI plugin. This means its configuration is appended to the list of existing CNI plugins configurations.
See the [CNI specification reference](https://www.cni.dev/docs/spec/#section-1-network-configuration-format) for further details.

When a pod is created or deleted, the container runtime invokes each plugin in the list in order.

The Istio CNI plugin performs actions to set up the application pod's traffic redirection - in the sidecar data plane mode, this means applying `iptables` rules in the pod's network namespace
to redirect in-pod traffic to the injected Istio proxy sidecar.
