---
collection: istio
version: "1.24"
title: "Namespace Sameness"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/glossary/namespace-sameness.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
Within a multicluster mesh, [namespace sameness](https://github.com/kubernetes/community/blob/master/sig-multicluster/namespace-sameness-position-statement.md)
applies and all namespaces with a given name are considered to be the same namespace. If multiple clusters contain a
`Service` with the same namespaced name, they will be recognized as a single combined service. By default, traffic is
load-balanced across all clusters in the mesh for a given service.

Ports that match on _number_ must also have the same port _name_ to be considered as a combined `service port`.
