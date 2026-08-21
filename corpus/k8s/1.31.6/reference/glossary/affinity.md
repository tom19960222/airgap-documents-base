---
collection: k8s
version: "1.31.6"
title: "Affinity"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/affinity.md
fetched_at: 2026-01-16T10:18:07+05:30
---
In Kubernetes, _affinity_ is a set of rules that give hints to the scheduler about where to place pods.

<!--more-->
There are two kinds of affinity:
* [node affinity](/docs/concepts/scheduling-eviction/assign-pod-node/#node-affinity)
* [pod-to-pod affinity](/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity)

The rules are defined using the Kubernetes labels,
and selectors specified in pods, 
and they can be either required or preferred, depending on how strictly you want the scheduler to enforce them.
