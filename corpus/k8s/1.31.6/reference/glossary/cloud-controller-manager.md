---
collection: k8s
version: "1.31.6"
title: "Cloud Controller Manager"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/cloud-controller-manager.md
fetched_at: 2026-01-16T10:18:07+05:30
---
A Kubernetes control plane component
that embeds cloud-specific control logic. The cloud controller manager lets you link your
cluster into your cloud provider's API, and separates out the components that interact
with that cloud platform from components that only interact with your cluster.

<!--more-->

By decoupling the interoperability logic between Kubernetes and the underlying cloud
infrastructure, the cloud-controller-manager component enables cloud providers to release
features at a different pace compared to the main Kubernetes project.
