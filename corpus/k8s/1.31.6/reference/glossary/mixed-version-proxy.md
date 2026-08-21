---
collection: k8s
version: "1.31.6"
title: "Mixed Version Proxy (MVP)"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/mixed-version-proxy.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Feature to let a kube-apiserver proxy a resource request to a different peer API server.

<!--more-->

When a cluster has multiple API servers running different versions of Kubernetes, this 
feature enables resource requests to be served by the correct API server.

MVP is disabled by default and can be activated by enabling
the [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) named `UnknownVersionInteroperabilityProxy` when 
the API Server is started.
