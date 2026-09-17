---
collection: cilium
version: "1.16.7"
title: "Overview of Network Policy"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/security/policy/index.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="network_policy"></a>
<a id="network-policies"></a>
<a id="network-policy"></a>

# Overview of Network Policy

This page documents the policy language used to configure network policies
in Cilium. Security policies can be specified and imported via the following
mechanisms:

* Using Kubernetes `NetworkPolicy`, `CiliumNetworkPolicy` and `CiliumClusterwideNetworkPolicy`
  resources. See the section [k8s_policy](../../network/kubernetes/policy.md#k8s_policy) for more details. In this mode,
  Kubernetes will automatically distribute the policies to all agents.

* Directly imported into the agent via CLI or [api_ref](../../api.md#api_ref) of the agent. This
  method does not automatically distribute policies to all agents. It is in the
  responsibility of the user to import the policy in all required agents.

.. toctree::
   :maxdepth: 2
   :glob:

   intro
   language
   kubernetes
   lifecycle
   troubleshooting
   caveats
