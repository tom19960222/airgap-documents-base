---
collection: k8s
version: "1.31.6"
title: "Taint"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/taint.md
fetched_at: 2026-01-16T10:18:07+05:30
---
A core object consisting of three required properties: key, value, and effect. Taints prevent the scheduling of Pods on nodes or node groups.

<!--more-->

Taints and tolerations work together to ensure that pods are not scheduled onto inappropriate nodes. One or more taints are applied to a node. A node should only schedule a Pod with the matching tolerations for the configured taints.
