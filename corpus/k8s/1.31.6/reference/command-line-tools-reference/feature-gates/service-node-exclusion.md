---
collection: k8s
version: "1.31.6"
title: "ServiceNodeExclusion"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/service-node-exclusion.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enable the exclusion of nodes from load balancers created by a cloud provider.
A node is eligible for exclusion if labelled with "`node.kubernetes.io/exclude-from-external-load-balancers`".
