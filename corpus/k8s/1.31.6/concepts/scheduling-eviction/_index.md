---
collection: k8s
version: "1.31.6"
title: "Scheduling, Preemption and Eviction"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/concepts/scheduling-eviction/_index.md
fetched_at: 2026-01-16T10:18:07+05:30
---
In Kubernetes, scheduling refers to making sure that Pods
are matched to Nodes so that the
kubelet can run them. Preemption
is the process of terminating Pods with lower Priority
so that Pods with higher Priority can schedule on Nodes. Eviction is the process
of terminating one or more Pods on Nodes.

## Scheduling

* [Kubernetes Scheduler](/docs/concepts/scheduling-eviction/kube-scheduler/)
* [Assigning Pods to Nodes](/docs/concepts/scheduling-eviction/assign-pod-node/)
* [Pod Overhead](/docs/concepts/scheduling-eviction/pod-overhead/)
* [Pod Topology Spread Constraints](/docs/concepts/scheduling-eviction/topology-spread-constraints/)
* [Taints and Tolerations](/docs/concepts/scheduling-eviction/taint-and-toleration/)
* [Scheduling Framework](/docs/concepts/scheduling-eviction/scheduling-framework)
* [Dynamic Resource Allocation](/docs/concepts/scheduling-eviction/dynamic-resource-allocation)
* [Scheduler Performance Tuning](/docs/concepts/scheduling-eviction/scheduler-perf-tuning/)
* [Resource Bin Packing for Extended Resources](/docs/concepts/scheduling-eviction/resource-bin-packing/)
* [Pod Scheduling Readiness](/docs/concepts/scheduling-eviction/pod-scheduling-readiness/)
* [Descheduler](https://github.com/kubernetes-sigs/descheduler#descheduler-for-kubernetes)

## Pod Disruption

[Pod disruption](/docs/concepts/workloads/pods/disruptions/) is the process by which 
Pods on Nodes are terminated either voluntarily or involuntarily. 

 

Voluntary disruptions are started intentionally by application owners or cluster 
administrators. Involuntary disruptions are unintentional and can be triggered by 
unavoidable issues like Nodes running out of resources, or by accidental deletions.

* [Pod Priority and Preemption](/docs/concepts/scheduling-eviction/pod-priority-preemption/)
* [Node-pressure Eviction](/docs/concepts/scheduling-eviction/node-pressure-eviction/)
* [API-initiated Eviction](/docs/concepts/scheduling-eviction/api-eviction/)
