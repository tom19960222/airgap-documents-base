---
collection: cilium
version: "1.16.7"
title: "GAMMA Support"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/network/servicemesh/gateway-api/gamma.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="gs_gamma"></a>

# GAMMA Support

## What is GAMMA?

(From the [GAMMA page](https://gateway-api.sigs.k8s.io/mesh/gamma/)
on the Gateway API site):

The GAMMA initiative is a dedicated workstream within the Gateway API
subproject, shepherded by the GAMMA leads, rather than being a separate
subproject. GAMMA’s goal is to define how Gateway API can be used to configure
a service mesh, with the intention of making minimal changes to Gateway API and
always preserving the role-oriented nature of Gateway API. Additionally, GAMMA
strives to advocate for consistency between implementations of Gateway API by
service mesh projects, regardless of their technology stack or proxy.

In Gateway API v1.0, GAMMA supports adding extra HTTP routing to Services by
binding a HTTPRoute to a Service as a parent (as opposed to the north/south
Gateway API usage of binding a HTTPRoute to a Gateway as a parent).

This allows Cilium to intercept layer 7 traffic flowing to a parent Service and
route the traffic through the per-node Envoy proxy. Because of this, GAMMA
performs the same function as Cilium's
[Layer 7 traffic management](../l7-traffic-management.md#gs_l7_traffic_management), without the user
needing to know anything about configuring Envoy directly.

## Types of GAMMA configuration

In GAMMA, there are two types of HTTPRoutes: "producer" and "consumer" Routes.

"Producer" routes are HTTPRoutes that bind to a Service that lives in the same
namespace and have the same owner as the owner of the Service whose traffic is
being managed. So, for an application ``foo``, in the namespace ``foo``, with a
Service called ``foo-svc``, the owner of ``foo`` would create a HTTPRoute in the ``foo``
namespace that lists ``foo-svc`` as its parent. The routing then affects all traffic
coming to the ``foo`` service from the whole cluster, and is controlled by the
"producer" of the ``foo`` service - its owner.

"Consumer" routes are HTTPRoutes that bind to a Service that lives in a different
namespace than that Service. These Routes are called "consumer" Routes because
they are owned by the _consumer_ of the Service they bind to. For the ``foo`` Service
above, a Route in the ``bar`` namespace, to be used by the app in that namespace,
that binds to the ``foo-svc`` Service in the ``foo`` namespace is a _consumer_ Service
because it changes the routing for the ``bar`` service, which _consumes_ the ``foo``
Service.

Cilium currently supports only "Producer" Routes, and so HTTPRoutes must be
in the same namespace as the Service that they are binding to.

## Cilium GAMMA Support

Cilium supports GAMMA v1.0.0 for the following resources:

- [HTTPRoute](https://gateway-api.sigs.k8s.io/api-types/httproute/)
- [ReferenceGrant](https://gateway-api.sigs.k8s.io/api-types/referencegrant/)

Cilium support is limited to passing the Core conformance
tests and two out of three Extended Mesh tests. Note that GAMMA is itself
experimental as at Gateway API v1.0.0.

Cilium currently does not support "consumer" HTTPRoutes, and so does not
support the ``MeshConsumerRoute`` feature of the Mesh conformance profile.

Included file `Documentation/network/servicemesh/gateway-api/installation.rst`:

## Prerequisites

* Cilium must be configured with NodePort enabled, using
  ``nodePort.enabled=true`` or by enabling the kube-proxy replacement with
  ``kubeProxyReplacement=true``. For more information, see [kube-proxy replacement](../../kubernetes/kubeproxy-free.md#kubeproxy-free).
* Cilium must be configured with the L7 proxy enabled using ``l7Proxy=true``
  (enabled by default).
* The below CRDs from Gateway API v1.1.0 ``must`` be pre-installed.
  Please refer to this [docs](https://gateway-api.sigs.k8s.io/guides/?h=crds#getting-started-with-gateway-api)
  for installation steps. Alternatively, the below snippet could be used.

    - [GatewayClass](https://gateway-api.sigs.k8s.io/api-types/gatewayclass/)
    - [Gateway](https://gateway-api.sigs.k8s.io/api-types/gateway/)
    - [HTTPRoute](https://gateway-api.sigs.k8s.io/api-types/httproute/)
    - [GRPCRoute](https://gateway-api.sigs.k8s.io/api-types/grpcroute/)
    - [ReferenceGrant](https://gateway-api.sigs.k8s.io/api-types/referencegrant/)
    - [TLSRoute (experimental)](https://gateway-api.sigs.k8s.io/references/spec/#gateway.networking.k8s.io%2fv1alpha2.TLSRoute/)

.. admonition:: warning
   :class: attention

   An issue in Gateway API requires Cilium having the experimental CRDs to
   be installed in order to use Gateway API. The issue is being tracked
   [here](https://github.com/kubernetes-sigs/gateway-api/issues/3080).

   To install the experimental CRDs, please refer to
   the [Gateway API documentation](https://gateway-api.sigs.k8s.io/guides/#install-experimental-channel).

```shell-session
$ kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.1.0/config/crd/standard/gateway.networking.k8s.io_gatewayclasses.yaml
$ kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.1.0/config/crd/standard/gateway.networking.k8s.io_gateways.yaml
$ kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.1.0/config/crd/standard/gateway.networking.k8s.io_httproutes.yaml
$ kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.1.0/config/crd/standard/gateway.networking.k8s.io_referencegrants.yaml
$ kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.1.0/config/crd/standard/gateway.networking.k8s.io_grpcroutes.yaml
$ kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/v1.1.0/config/crd/experimental/gateway.networking.k8s.io_tlsroutes.yaml
```

* By default, the Gateway API controller creates a service of LoadBalancer type,
  so your environment will need to support this. Alternatively, since Cilium 1.16+,
  you can directly expose the Cilium L7 proxy on the [host network](gateway-api.md#gs_gateway_host_network_mode).

## Installation

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
> See [Cilium CLI upgrade notes](../../../operations/upgrade.md#upgrade_cilium_cli_helm_mode) for more details.

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

.. tabs::

   .. group-tab:: Helm

       Cilium Gateway API Controller can be enabled with helm flag ``gatewayAPI.enabled``
       set as true. Please refer to [k8s_install_helm](../../../installation/k8s-install-helm.md#k8s_install_helm) for a fresh installation.

       .. parsed-literal::

           $ helm upgrade cilium |CHART_RELEASE| \\
               --namespace kube-system \\
               --reuse-values \\
               --set kubeProxyReplacement=true \\
               --set gatewayAPI.enabled=true

           $ kubectl -n kube-system rollout restart deployment/cilium-operator
           $ kubectl -n kube-system rollout restart ds/cilium

       Next you can check the status of the Cilium agent and operator:

       .. code-block:: shell-session

           $ cilium status

   .. group-tab:: Cilium CLI

       Cilium Gateway API Controller can be enabled with the below command

       .. parsed-literal::

           $ cilium install |CHART_VERSION| \\
               --set kubeProxyReplacement=true \\
               --set gatewayAPI.enabled=true

       Next you can check the status of the Cilium agent and operator:

       .. code-block:: shell-session

           $ cilium status
