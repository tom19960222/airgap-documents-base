---
collection: cilium
version: "1.16.7"
title: "Configuration"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/configuration/index.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="configuration"></a>

# Configuration

Your Cilium installation is configured by one or more Helm values -
see [helm_reference](../helm-reference.md#helm_reference). These helm values are converted to arguments
for the individual components of a Cilium installation, such as
[../cmdref/cilium-agent](../cmdref/cilium-agent.md) and [../cmdref/cilium-operator](../cmdref/cilium-operator.md), and
stored in a ConfigMap.

<a id="cilium-config-configmap"></a>

## ``cilium-config`` ConfigMap

These arguments are stored in a shared ConfigMap called ``cilium-config``
(albeit without the leading ``--``). For example, a typical installation
may look like

```shell-session
$ kubectl -n kube-system get configmap cilium-config -o yaml
data:
  agent-not-ready-taint-key: node.cilium.io/agent-not-ready
  arping-refresh-period: 30s
  auto-direct-node-routes: "false"
  (output continues)
```

<a id="making-config-changes"></a>

## Making Changes

You may change the configuration of a running installation in three ways:

1. Via ``helm upgrade``

   Do so by providing new values to Helm and applying them to the existing
   installation. By setting the value ``rollOutCiliumPods=true``, the agent
   pods will be gradually restarted.

1. Via ``cilium config set``

   The [Cilium CLI](https://github.com/cilium/cilium-cli/) has the ability
   to update individual values in the ``cilium-config`` ConfigMap. This will
   not affect running pods; pods must be deleted manually to pick up any changes.

1. Via ``CiliumNodeConfig`` objects

   Cilium also supports configuration on sets of nodes. See the
   [per-node-configuration](per-node-config.md#per-node-configuration) page for more details. Likewise, this also requires
   that pods be manually deleted for changes to take effect.

## Core Agent
.. toctree::
   :maxdepth: 1
   :glob:

   api-rate-limiting
   api-restrictions
   per-node-config
   sctp
   vlan-802.1q
   argocd-issues

## Security
.. toctree::
   :maxdepth: 1
   :glob:

   verify-image-signatures
   sbom
