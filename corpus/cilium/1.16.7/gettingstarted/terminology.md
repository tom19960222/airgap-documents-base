---
collection: cilium
version: "1.16.7"
title: "Terminology"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/gettingstarted/terminology.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

# Terminology

<a id="label"></a>
<a id="labels"></a>

## Labels

Labels are a generic, flexible and highly scalable way of addressing a large
set of resources as they allow for arbitrary grouping and creation of sets.
Whenever something needs to be described, addressed or selected, it is done
based on labels:

- `Endpoints` are assigned labels as derived from the container runtime,
  orchestration system, or other sources.
- `Network policies` select pairs of `endpoints` which are allowed to
  communicate based on labels. The policies themselves are identified by labels
  as well.

### What is a Label?

A label is a pair of strings consisting of a ``key`` and ``value``. A label can
be formatted as a single string with the format ``key=value``. The key portion
is mandatory and must be unique. This is typically achieved by using the
reverse domain name notion, e.g. ``io.cilium.mykey=myvalue``. The value portion
is optional and can be omitted, e.g. ``io.cilium.mykey``.

Key names should typically consist of the character set ``[a-z0-9-.]``.

When using labels to select resources, both the key and the value must match,
e.g. when a policy should be applied to all endpoints with the label
``my.corp.foo`` then the label ``my.corp.foo=bar`` will not match the
selector.

### Label Source

A label can be derived from various sources. For example, an [endpoint](terminology.md#endpoint) will
derive the labels associated to the container by the local container runtime as
well as the labels associated with the pod as provided by Kubernetes. As these
two label namespaces are not aware of each other, this may result in
conflicting label keys.

To resolve this potential conflict, Cilium prefixes all label keys with
``source:`` to indicate the source of the label when importing labels, e.g.
``k8s:role=frontend``, ``container:user=joe``, ``k8s:role=backend``. This means
that when you run a Docker container using ``docker run [...] -l foo=bar``, the
label ``container:foo=bar`` will appear on the Cilium endpoint representing the
container. Similarly, a Kubernetes pod started with the label ``foo: bar``
will be represented with a Cilium endpoint associated with the label
``k8s:foo=bar``. A unique name is allocated for each potential source. The
following label sources are currently supported:

- ``container:`` for labels derived from the local container runtime
- ``k8s:`` for labels derived from Kubernetes
- ``reserved:`` for special reserved labels, see [reserved_labels](terminology.md#reserved_labels).
- ``unspec:`` for labels with unspecified source

When using labels to identify other resources, the source can be included to
limit matching of labels to a particular type. If no source is provided, the
label source defaults to ``any:`` which will match all labels regardless of
their source. If a source is provided, the source of the selecting and matching
labels need to match.

<a id="endpoint"></a>
<a id="endpoints"></a>

## Endpoint

Cilium makes application containers available on the network by assigning them
IP addresses. Multiple application containers can share the same IP address; a
typical example for this model is a Kubernetes Pod. All application containers
which share a common address are grouped together in what Cilium refers to as
an endpoint.

Allocating individual IP addresses enables the use of the entire Layer 4 port
range by each endpoint. This essentially allows multiple application containers
running on the same cluster node to all bind to well known ports such as ``80``
without causing any conflicts.

The default behavior of Cilium is to assign both an IPv6 and IPv4 address to
every endpoint. However, this behavior can be configured to only allocate an
IPv6 address with the ``--enable-ipv4=false`` option. If both an IPv6 and IPv4
address are assigned, either address can be used to reach the endpoint. The
same behavior will apply with regard to policy rules, load-balancing, etc. See
[address_management](../network/concepts/ipam/index.md#address_management) for more details.

### Identification

For identification purposes, Cilium assigns an internal endpoint id to all
endpoints on a cluster node. The endpoint id is unique within the context of
an individual cluster node.

<a id="endpoint-id"></a>

### Endpoint Metadata

An endpoint automatically derives metadata from the application containers
associated with the endpoint. The metadata can then be used to identify the
endpoint for security/policy, load-balancing and routing purposes.

The source of the metadata will depend on the orchestration system and
container runtime in use. The following metadata retrieval mechanisms are
currently supported:

| System | Description |
| --- | --- |
| Kubernetes | Pod labels (via k8s API) |
| containerd (Docker) | Container labels (via Docker API) |

Metadata is attached to endpoints in the form of `labels`.

The following example launches a container with the label ``app=benchmark``
which is then associated with the endpoint. The label is prefixed with
``container:`` to indicate that the label was derived from the container
runtime.

```shell-session
$ docker run --net cilium -d -l app=benchmark tgraf/netperf
aaff7190f47d071325e7af06577f672beff64ccc91d2b53c42262635c063cf1c
$ cilium-dbg endpoint list
ENDPOINT   POLICY        IDENTITY   LABELS (source:key[=value])   IPv6                   IPv4            STATUS
           ENFORCEMENT
62006      Disabled      257        container:app=benchmark       f00d::a00:20f:0:f236   10.15.116.202   ready
```

An endpoint can have metadata associated from multiple sources. A typical
example is a Kubernetes cluster which uses containerd as the container runtime.
Endpoints will derive Kubernetes pod labels (prefixed with the ``k8s:`` source
prefix) and containerd labels (prefixed with ``container:`` source prefix).

<a id="identity"></a>

## Identity

All `endpoints` are assigned an identity. The identity is what is used to enforce
basic connectivity between endpoints. In traditional networking terminology,
this would be equivalent to Layer 3 enforcement.

An identity is identified by `labels` and is given a cluster wide unique
identifier. The endpoint is assigned the identity which matches the endpoint's
`security relevant labels`, i.e. all endpoints which share the same set of
`security relevant labels` will share the same identity. This concept allows to
scale policy enforcement to a massive number of endpoints as many individual
endpoints will typically share the same set of security `labels` as applications
are scaled.

### What is an Identity?

The identity of an endpoint is derived based on the `labels` associated with
the pod or container which are derived to the [endpoint](terminology.md#endpoint). When a pod or
container is started, Cilium will create an [endpoint](terminology.md#endpoint) based on the event
received by the container runtime to represent the pod or container on the
network. As a next step, Cilium will resolve the identity of the [endpoint](terminology.md#endpoint)
created. Whenever the `labels` of the pod or container change, the identity is
reconfirmed and automatically modified as required.

<a id="security-relevant-labels"></a>

### Security Relevant Labels

Not all `labels` associated with a container or pod are meaningful when
deriving the `identity`. Labels may be used to store metadata such as the
timestamp when a container was launched. Cilium requires to know which labels
are meaningful and are subject to being considered when deriving the identity.
For this purpose, the user is required to specify a list of string prefixes of
meaningful labels. The standard behavior is to include all labels which start
with the prefix ``id.``, e.g.  ``id.service1``, ``id.service2``,
``id.groupA.service44``. The list of meaningful label prefixes can be specified
when starting the agent.

<a id="reserved_labels"></a>

### Special Identities

All endpoints which are managed by Cilium will be assigned an identity. In
order to allow communication to network endpoints which are not managed by
Cilium, special identities exist to represent those. Special reserved
identities are prefixed with the string ``reserved:``.

| Identity | Numeric ID | Description |
| --- | --- | --- |
| ``reserved:unknown`` | 0 | The identity could not be derived. |
| ``reserved:host`` <br> | 1 <br> | The local host. Any traffic that originates from <br> or is designated to one of the local host IPs. |
| ``reserved:world`` | 2 | Any network endpoint outside of the cluster |
| ``reserved:unmanaged`` <br> <br> | 3 <br> <br> | An endpoint that is not managed by Cilium, e.g. <br> a Kubernetes pod that was launched before Cilium <br> was installed. |
| ``reserved:health`` <br> | 4 <br> | This is health checking traffic generated by <br> Cilium agents. |
| ``reserved:init`` <br> <br> <br> <br> <br> <br> <br> <br> <br> | 5 <br> <br> <br> <br> <br> <br> <br> <br> <br> | An endpoint for which the identity has not yet <br> been resolved is assigned the init identity. <br> This represents the phase of an endpoint in which <br> some of the metadata required to derive the <br> security identity is still missing. This is <br> typically the case in the bootstrapping phase. <br> <br> The init identity is only allocated if the labels <br> of the endpoint are not known at creation time. <br> This can be the case for the Docker plugin. |
| ``reserved:remote-node`` <br> <br> <br> | 6 <br> <br> <br> | The collection of all remote cluster hosts. <br> Any traffic that originates from or is designated <br> to one of the IPs of any host in any connected <br> cluster other than the local node. |
| ``reserved:kube-apiserver`` <br> | 7 <br> | Remote node(s) which have backend(s) serving the <br> kube-apiserver running. |
| ``reserved:ingress`` <br> | 8 <br> | Given to the IPs used as the source address for <br> connections from Ingress proxies. |

### Well-known Identities

The following is a list of well-known identities which Cilium is aware of
automatically and will hand out a security identity without requiring to
contact any external dependencies such as the kvstore. The purpose of this is
to allow bootstrapping Cilium and enable network connectivity with policy
enforcement in the cluster for essential services without depending on any
dependencies.

| Deployment | Namespace | ServiceAccount | Cluster Name | Numeric ID | Labels |
| --- | --- | --- | --- | --- | --- |
| kube-dns | kube-system | kube-dns | <cilium-cluster> | 102 | ``k8s-app=kube-dns`` |
| kube-dns (EKS) | kube-system | kube-dns | <cilium-cluster> | 103 | ``k8s-app=kube-dns``, ``eks.amazonaws.com/component=kube-dns`` |
| core-dns | kube-system | coredns | <cilium-cluster> | 104 | ``k8s-app=kube-dns`` |
| core-dns (EKS) | kube-system | coredns | <cilium-cluster> | 106 | ``k8s-app=kube-dns``, ``eks.amazonaws.com/component=coredns`` |
| cilium-operator | <cilium-namespace> | cilium-operator | <cilium-cluster> | 105 | ``name=cilium-operator``, ``io.cilium/app=operator`` |

*Note*: if ``cilium-cluster`` is not defined with the ``cluster-name`` option,
the default value will be set to "``default``".

### Identity Management in the Cluster

Identities are valid in the entire cluster which means that if several pods or
containers are started on several cluster nodes, all of them will resolve and
share a single identity if they share the identity relevant labels. This
requires coordination between cluster nodes.

![](https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/images/identity_store.png)

The operation to resolve an endpoint identity is performed with the help of the
distributed key-value store which allows to perform atomic operations in the
form *generate a new unique identifier if the following value has not been seen
before*. This allows each cluster node to create the identity relevant subset
of labels and then query the key-value store to derive the identity. Depending
on whether the set of labels has been queried before, either a new identity
will be created, or the identity of the initial query will be returned.

<a id="node"></a>

## Node

Cilium refers to a node as an individual member of a cluster. Each node must be
running the ``cilium-agent`` and will operate in a mostly autonomous manner.
Synchronization of state between Cilium agents running on different nodes is
kept to a minimum for simplicity and scale. It occurs exclusively via the
Key-Value store or with packet metadata.

### Node Address

Cilium will automatically detect the node's IPv4 and IPv6 address. The detected
node address is printed out when the ``cilium-agent`` starts:

:

```
Local node-name: worker0
Node-IPv6: f00d::ac10:14:0:1
External-Node IPv4: 172.16.0.20
Internal-Node IPv4: 10.200.28.238
```
