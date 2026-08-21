---
collection: k8s
version: "1.31.6"
title: "ServiceAccount"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/service-account.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Provides an identity for processes that run in a Pod.

<!--more--> 

When processes inside Pods access the cluster, they are authenticated by the API server as a particular service account, for example, `default`. When you create a Pod, if you do not specify a service account, it is automatically assigned the default service account in the same Namespace.
