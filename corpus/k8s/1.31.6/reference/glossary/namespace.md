---
collection: k8s
version: "1.31.6"
title: "Namespace"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/namespace.md
fetched_at: 2026-01-16T10:18:07+05:30
---
An abstraction used by Kubernetes to support isolation of groups of resources within a single cluster.

<!--more--> 

Namespaces are used to organize objects in a cluster and provide a way to divide cluster resources. Names of resources need to be unique within a namespace, but not across namespaces. Namespace-based scoping is applicable only for namespaced objects _(e.g. Deployments, Services, etc)_ and not for cluster-wide objects _(e.g. StorageClass, Nodes, PersistentVolumes, etc)_.
