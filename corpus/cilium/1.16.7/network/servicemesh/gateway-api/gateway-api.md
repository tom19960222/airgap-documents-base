---
collection: cilium
version: "1.16.7"
title: "Gateway API Support"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/network/servicemesh/gateway-api/gateway-api.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="gs_gateway_api"></a>

# Gateway API Support

## What is Gateway API?

Gateway API is a Kubernetes SIG-Network subproject to design a successor for
the Ingress object. It is a set of resources that model service networking in
Kubernetes, and is designed to be role-oriented, portable, expressive, and
extensible.

See the [Gateway API site](https://gateway-api.sigs.k8s.io/) for more details.

## Cilium Gateway API Support

Cilium supports Gateway API v1.1.0 for below resources, all the Core conformance
tests are passed.

- [GatewayClass](https://gateway-api.sigs.k8s.io/api-types/gatewayclass/)
- [Gateway](https://gateway-api.sigs.k8s.io/api-types/gateway/)
- [HTTPRoute](https://gateway-api.sigs.k8s.io/api-types/httproute/)
- [GRPCRoute](https://gateway-api.sigs.k8s.io/api-types/grpcroute/)
- [TLSRoute (experimental)](https://gateway-api.sigs.k8s.io/references/spec/#gateway.networking.k8s.io/v1alpha2.TLSRoute)
- [ReferenceGrant](https://gateway-api.sigs.k8s.io/api-types/referencegrant/)

.. admonition:: Video
   :class: attention

    If you'd like more insights on Cilium's Gateway API support, check out [eCHO episode 58: Cilium Service Mesh and Ingress](https://www.youtube.com/watch?v=60epwCxO8G4&index=80&t=2024s).

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

Included file `Documentation/network/servicemesh/ingress-reference.rst`:

## Reference

### How Cilium Ingress and Gateway API differ from other Ingress controllers

One of the biggest differences between Cilium's Ingress and Gateway API support
and other Ingress controllers is how closely tied the implementation is to the
CNI. For Cilium, Ingress and Gateway API are part of the networking stack,
and so behave in a different way to other Ingress or Gateway API controllers
(even other Ingress or Gateway API controllers running in a Cilium cluster).

Other Ingress or Gateway API controllers are generally installed as a Deployment
or Daemonset in the cluster, and exposed via a Loadbalancer Service or similar (which Cilium
can, of course, enable).

Cilium's Ingress and Gateway API config is exposed with a Loadbalancer or NodePort
service, or optionally can be exposed on the Host network also. But in all of
these cases, when traffic arrives at the Service's port, eBPF code intercepts
the traffic and transparently forwards it to Envoy (using the TPROXY kernel facility).

This affects things like client IP visibility, which works differently for Cilium's
Ingress and Gateway API support to other Ingress controllers.

It also allows Cilium's Network Policy engine to apply CiliumNetworkPolicy to
traffic bound for and traffic coming from an Ingress.

### Cilium's ingress config and CiliumNetworkPolicy

Ingress and Gateway API traffic bound to backend services via Cilium passes through a
per-node Envoy proxy.

The per-node Envoy proxy has special code that allows it to interact with the
eBPF policy engine, and do policy lookups on traffic. This allows Envoy to be
a Network Policy enforcement point, both for Ingress (and Gateway API) traffic,
and also for east-west traffic via GAMMA or L7 Traffic Management.

However, for ingress config, there's also an additional step. Traffic that arrives at
Envoy *for Ingress or Gateway API* is assigned the special ``ingress`` identity
in Cilium's Policy engine.

Traffic coming from outside the cluster is usually assigned the ``world`` identity
(unless there are IP CIDR policies in the cluster). This means that there are
actually *two* logical Policy enforcement points in Cilium Ingress - before traffic
arrives at the ``ingress`` identity, and after, when it is about to exit the
per-node Envoy.

![](/images/ingress-policy.png)

This means that, when applying Network Policy to a cluster, it's important to
ensure that both steps are allowed, and that traffic is allowed from ``world`` to
``ingress``, and from ``ingress`` to identities in the cluster (like the
``productpage`` identity in the image above).

Please see the [gs_ingress_and_network_policy](../ingress-and-network-policy.md#gs_ingress_and_network_policy) for more details for Ingress,
although the same principles also apply for Gateway API.

### Source IP Visibility

> **Note:**
> By default, source IP visibility for Cilium ingress config, both Ingress
> and Gateway API, should *just work* on most installations. Read this section
> for more information on requirements and relevant settings.

Having a backend be able to deduce what IP address the actual request came from
is important for most applications.

By default, Cilium's Envoy instances are configured to append the visible source
address of incoming HTTP connections to the ``X-Forwarded-For`` header, using the
usual rules. That is, by default Cilium sets the number of trusted hops to ``0``,
indicating that Envoy should use the address the connection is opened from, rather
than a value inside the ``X-Forwarded-For`` list. Increasing this count will
have Envoy use the ``n`` th value from the list, counting from the right.

Envoy will also set the ``X-Envoy-External-Address`` header to the trusted client
address, whatever that turns out to be, based on ``X-Forwarded-For``.

> **Note:**
> Backends using Cilium ingress (whether via Ingress or Gateway API) should
> just see the ``X-Forwarded-For`` and ``X-Envoy-External-Address`` headers (which
> are handled transparently by many HTTP libraries).

#### ``externalTrafficPolicy`` for Loadbalancer or NodePort Services

Cilium's ingress support (both for Ingress and Gateway API) often uses a Loadbalancer
or NodePort Service to expose the Envoy Daemonset.

In these cases, the Service object has one field that is particularly relevant
to Client IP visibility - the ``externalTrafficPolicy`` field.

It has two relevant settings:

- ``Local``: Nodes will only route traffic to Pods running on the local node,
  *without masquerading the source IP*. Because of this, in clusters that use
  ``kube-proxy``, this is the only way to ensure source IP visibility. Part of
  the contract for ``externalTrafficPolicy`` local is also that the node will
  open a port (the ``healthCheckNodePort``, automatically set by Kubernetes when
  ``externalTrafficPolicy: Local`` is set), and requests to
  ``http://<nodeIP>:<healthCheckNodePort>/healthz`` will return 200 on nodes that
  have local pods running, and non-200 on nodes that don't. Cilium implements this
  for general Loadbalancer Services, but it's a bit different for Cilium ingress
  config (both Ingress and Gateway API).
- ``Cluster``: Node will route to all endpoints across the cluster evenly. This
  has a couple of other effects: Firstly, upstream loadbalancers will expect to
  be able to send traffic to any node and have it end up at a backend Pod, and
  the node *may* masquerade the source IP. This means that in many cases,
  ``externalTrafficPolicy: Cluster`` may mean that the backend pod does *not* see
  the source IP.

In Cilium's case, all ingress traffic bound for a Service that exposes Envoy is
*always* going to the local node, and is *always* forwarded to Envoy using the
Linux Kernel TPROXY function, which transparently forwards packets to the backend.

This means that for Cilium ingress config, for both Ingress and Gateway API, things
work a little differently in both ``externalTrafficPolicy`` cases.

> **Note:**
> In *both* ``externalTrafficPolicy`` cases, traffic will arrive at any node
> in the cluster, and be forwarded to *Envoy* **while keeping the source IP intact**.

Also, for any Services that exposes Cilium's Envoy, Cilium will ensure that
when ``externalTrafficPolicy: Local`` is set, every node in the cluster will
pass the ``healthCheckNodePort`` check, so that external load balancers will
forward correctly.

However, for Cilium's ingress config, both Ingress and Gateway API, **it is not
necessary** to configure ``externalTrafficPolicy: Local`` to keep the source IP
visible to the backend pod (via the ``X-Forwarded-For`` and ``X-Envoy-External-Address``
fields).

#### TLS Passthrough and source IP visibility

Both Ingress and Gateway API support TLS Passthrough configuration (via annotation
for Ingress, and the TLSRoute resource for Gateway API). This configuration allows
multiple TLS Passthrough backends to share the same TLS port on a loadbalancer,
with Envoy inspecting the Server Name Indicator (SNI) field of the TLS handshake,
and using that to forward the TLS stream to a backend.

However, this poses problems for source IP visibility, because Envoy is doing a
TCP Proxy of the TLS stream.

What happens is that the TLS traffic arrives at Envoy, terminating a TCP stream,
Envoy inspects the client hello to find the SNI, picks a backend to forward to,
then starts a new TCP stream and forwards the TLS traffic inside the downstream
(outside)  packets to the upstream (the backend).

Because it's a new TCP stream, as far as the backends are concerned, the source
IP is Envoy (which is often the Node IP, depending on your Cilium config).

> **Note:**
> When doing TLS Passthrough, backends will see Cilium Envoy's IP address
> as the source of the forwarded TLS streams.

<a id="gs_gateway_host_network_mode"></a>
Included file `Documentation/network/servicemesh/gateway-api/host-network-mode.rst`:

.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

### Host network mode

> **Note:**
> Supported since Cilium 1.16+

Host network mode allows you to expose the Cilium Gateway API Gateway directly
on the host network.
This is useful in cases where a LoadBalancer Service is unavailable, such
as in development environments or environments with cluster-external
loadbalancers.

> **Note:**
> * Enabling the Cilium Gateway API host network mode automatically disables the LoadBalancer type Service mode. They are mutually exclusive.
> * The listener is exposed on all interfaces (``0.0.0.0`` for IPv4 and/or ``::`` for IPv6).

Host network mode can be enabled via Helm:

```yaml
gatewayAPI:
  enabled: true
  hostNetwork:
    enabled: true
```

Once enabled, the host network port for a ``Gateway`` can be specified via
``spec.listeners.port``. The port must be unique per ``Gateway``
resource and you should choose a port number higher than ``1023`` (see
[Bind to privileged port](host-network-mode.md#bind-to-privileged-port)).

> **Warning:**
> Be aware that misconfiguration might result in port clashes. Configure unique ports that are still available on all Cilium Nodes where Gateway API listeners are exposed.

#### Bind to privileged port

By default, the Cilium L7 Envoy process does not have any Linux capabilities
out-of-the-box and is therefore not allowed to listen on privileged ports.

If you choose a port equal to or lower than ``1023``, ensure that the Helm value
``envoy.securityContext.capabilities.keepCapNetBindService=true`` is configured
and to add the capability ``NET_BIND_SERVICE`` to the respective
[Cilium Envoy container via Helm values](../../../security/network/proxy/envoy.md#envoy):

* Standalone DaemonSet mode: ``envoy.securityContext.capabilities.envoy``
* Embedded mode: ``securityContext.capabilities.ciliumAgent``

Configure the following Helm values to allow privileged port bindings in host
network mode:

.. tabs::

   .. group-tab:: Standalone DaemonSet mode

     .. code-block:: yaml

         gatewayAPI:
           enabled: true
           hostNetwork:
             enabled: true
         envoy:
           enabled: true
           securityContext:
             capabilities:
               keepCapNetBindService: true
               envoy:
               # Add NET_BIND_SERVICE to the list (keep the others!)
               - NET_BIND_SERVICE

   .. group-tab:: Embedded mode

     .. code-block:: yaml

         gatewayAPI:
           enabled: true
           hostNetwork:
             enabled: true
         envoy:
           securityContext:
             capabilities:
               keepCapNetBindService: true
         securityContext:
           capabilities:
             ciliumAgent:
             # Add NET_BIND_SERVICE to the list (keep the others!)
             - NET_BIND_SERVICE

#### Deploy Gateway API listeners on subset of nodes

The Cilium Gateway API Envoy listener can be exposed on a specific subset of
nodes. This only works in combination with the host network mode and can be
configured via a node label selector in the Helm values:

```yaml
gatewayAPI:
  enabled: true
  hostNetwork:
    enabled: true
    nodes:
      matchLabels:
        role: infra
        component: gateway-api
```

This will deploy the Gateway API Envoy listener only on the Cilium Nodes
matching the configured labels. An empty selector selects all nodes and
continues to expose the functionality on all Cilium nodes.

## Examples

Please refer to one of the below examples on how to use and leverage
Cilium's Gateway API features:

.. toctree::
   :maxdepth: 1
   :glob:

   http
   https
   splitting
   header

More examples can be found in the [upstream repository](https://github.com/kubernetes-sigs/gateway-api/tree/v1.1.0/examples/standard).

## Troubleshooting

Included file `Documentation/network/servicemesh/gateway-api/troubleshooting.rst`:

This page guides you through the different mechanics of Gateway API and how to troubleshoot them.

Be sure to follow the Generic and Setup Verification steps from the [Troubleshooting Ingress & Service Mesh page](../../../operations/troubleshooting.md#troubleshooting_servicemesh).

### Checking resources

1. Check the Gateway resource

```shell-session
$ kubectl get gateway -A
NAMESPACE                   NAME                 CLASS    ADDRESS          PROGRAMMED   AGE
website                     http-gateway         cilium   172.21.255.202   True         5h
webshop                     tls-gateway          cilium   172.21.255.203   True         5h
```

    The preceding command returns an overview of all the Gateways in the cluster. Check the following:

    * Is the Gateway programmed?

        A programmed Gateway means that Cilium prepared a configuration for it.

      * If the ``Programmed true`` indicator is missing, make sure that Gateway API is enabled in the Cilium configuration.

    * Does the gateway have an address?

    You can check the service with ``kubectl get service``.
    If the gateway has an address, it means that a LoadBalancer service is assigned to the gateway.
    If no IP appears, you might be missing a LoadBalancer implementation.

    * Is the class ``cilium``?

    Cilium only programs Gateways with the class ``cilium``.

    * If the Gateway API resource type (``Gateway``, ``HTTPRoute``, etc.) is not found, make sure that the Gateway API CRDs are installed.

    You can use ``kubectl describe gateway`` to investigate issues more thoroughly.

```shell-session
$ kubectl describe gateway <name>

  Conditions:
    Message:               Gateway successfully scheduled
    Reason:                Accepted
    Status:                True
    Type:                  Accepted
    Message:               Gateway successfully reconciled
    Reason:                Programmed
    Status:                True
    Type:                  Programmed
    [...]
  Listeners:
    Attached Routes:  2
    Conditions:
      Message:               Listener Ready
      Reason:                Programmed
      Status:                True
      Type:                  Programmed
      Message:               Listener Accepted
      Reason:                Accepted
      Status:                True
      [...]
```

    You can see the general status of the gateway as well as the status of the configured listeners.

    Listener status displays the number of routes successfully attached to the listener.

    You can see status conditions for both gateway and listener:

      * ``Accepted``: the Gateway configuration was accepted.
      * ``Programmed``: the Gateway configuration was programmed into Envoy.
      * ``ResolvedRefs``: all referenced secrets were found and have permission for use.

    If any of these conditions are set to false, the ``Message`` and ``Reason`` fields give more information.

1. Check the HTTPRoute resource

  When the Gateway is functional, you can check the routes to verify if they are configured correctly.
  The way to check route status is similar to checking the status of a gateway resource.

  While these instructions are written for HTTPRoute, they also apply to other route types.

```shell-session
$ kubectl get httproute -A
NAMESPACE                 NAME              HOSTNAMES         AGE
website                   homepage          www.example.org   17m
webshop                   catalog-service                     17m
webshop                   cart-service                        17m
```

  To get more information, enter ``kubectl describe httproute <name>``.

```shell-session
$ kubectl describe httproute <name>
Status:
  Parents:
    Conditions:
      Last Transition Time:  2023-06-05T15:11:53Z
      Message:               Accepted HTTPRoute
      Observed Generation:   1
      Reason:                Accepted
      Status:                True
      Type:                  Accepted
      Last Transition Time:  2023-06-05T15:11:53Z
      Message:               Service reference is valid
      Observed Generation:   1
      Reason:                ResolvedRefs
      Status:                True
      Type:                  ResolvedRefs
    Controller Name:         io.cilium/gateway-controller
    Parent Ref:
      Group:  gateway.networking.k8s.io
      Kind:   Gateway
      Name:   same-namespace
```

  Status lists the conditions that are relevant for the specific ``HTTPRoute``.
  Conditions are listed by parent reference to the gateway. If you linked the route to multiple gateways, multiple entries appear.
  Conditions include ``Reason``, ``Type``, ``Status`` and ``Message``. ``Type`` indicates the condition type, and ``Status`` indicates with a boolean whether the condition type is met. Optionally, ``Message`` gives you more information about the condition.

  Notice the following condition types:

  * ``Accepted``: The HTTPRoute configuration was correct and accepted.
  * ``ResolvedRefs``: The referenced services were found and are valid references.

  If any of these are set to false, you can get more information by looking at the ``Message`` and ``Reason`` fields.

1. Check Cilium Operator logs

  The Cilium Operator logs may contain further debugging information. For example, if the required Custom Resource Definitions (CRDs) are not installed, an error will be logged:

```shell-session
$ kubectl logs -n kube-system deployments/cilium-operator | grep gateway
level=error msg="Required GatewayAPI resources are not found, please
refer to docs for installation instructions" error="customresourcedefinitions.apiextensions.k8s.io \"gatewayclasses.gateway.networking.k8s.io\" not found
customresourcedefinitions.apiextensions.k8s.io \"gateways.gateway.networking.k8s.io\" not found
customresourcedefinitions.apiextensions.k8s.io \"httproutes.gateway.networking.k8s.io\" not found
customresourcedefinitions.apiextensions.k8s.io \"referencegrants.gateway.networking.k8s.io\" not found
customresourcedefinitions.apiextensions.k8s.io \"grpcroutes.gateway.networking.k8s.io\" not found
customresourcedefinitions.apiextensions.k8s.io \"tlsroutes.gateway.networking.k8s.io\" not found" subsys=gateway-api
```

### Common mistakes

Included file `Documentation/network/servicemesh/gateway-api/mistakes-warning.rst`:

> **Warning:**
> Gateway API is a recent addition to Kubernetes, and the Cilium project has not yet received much user feedback.
> If you encounter an issue that is not yet listed in this section, consider opening a PR to add your issue to the list.

* The backend service does not exist.

    To verify whether the backend service was found, run ``kubectl describe httproute <name>`` and inspect the ``conditions`` field:

```shell-session
Parents:
  Conditions:
    Last Transition Time:  2023-06-06T13:55:10Z
    Message:               Service "backend" not found
    Observed Generation:   1
    Reason:                BackendNotFound
    Status:                False
    Type:                  ResolvedRefs
    Last Transition Time:  2023-06-06T13:55:10Z
    Message:               Accepted HTTPRoute
    Observed Generation:   1
    Reason:                Accepted
    Status:                True
    Type:                  Accepted
  Controller Name:         io.cilium/gateway-controller
```

* The gateway specified under ``parentRefs`` does not exist.

    To verify whether the gateway was found, run ``kubectl describe httproute <name>`` and inspect the ``conditions`` field:

```shell-session
Parents:
  Conditions:
    Last Transition Time:  2023-06-06T13:56:40Z
    Message:               Gateway.gateway.networking.k8s.io "my-gatewai" not found
    Observed Generation:   2
      Reason:                InvalidHTTPRoute
      Status:                False
      Type:                  Accepted
```

### Underlying mechanics: a high level overview

A Cilium deployment has two parts that handle Gateway API resources: the Cilium agent and the Cilium operator.

The Cilium operator watches all Gateway API resources and verifies whether the resources are valid.
If resources are valid, the operator marks them as accepted. That starts the process of translation into Cilium Envoy Configuration resources.

The Cilium agent then picks up the Cilium Envoy Configuration resources.

The Cilium agent uses the resources to supply the configuration to the built in Envoy or the Envoy DaemonSet. Envoy handles traffic.
