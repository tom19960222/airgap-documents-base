---
collection: k8s
version: "1.31.6"
title: "Pod Disruption"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/pod-disruption.md
fetched_at: 2026-01-16T10:18:07+05:30
---
[Pod disruption](/docs/concepts/workloads/pods/disruptions/) is the process by which 
Pods on Nodes are terminated either voluntarily or involuntarily. 

<!--more--> 

Voluntary disruptions are started intentionally by application owners or cluster 
administrators. Involuntary disruptions are unintentional and can be triggered by 
unavoidable issues like Nodes running out of resources, or by accidental deletions.
