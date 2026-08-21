---
collection: k8s
version: "1.31.6"
title: "Node-pressure eviction"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/node-pressure-eviction.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Node-pressure eviction is the process by which the kubelet proactively terminates
pods to reclaim resources on nodes.

<!--more-->

The kubelet monitors resources like CPU, memory, disk space, and filesystem 
inodes on your cluster's nodes. When one or more of these resources reach
specific consumption levels, the kubelet can proactively fail one or more pods
on the node to reclaim resources and prevent starvation. 

Node-pressure eviction is not the same as [API-initiated eviction](/docs/concepts/scheduling-eviction/api-eviction/).
