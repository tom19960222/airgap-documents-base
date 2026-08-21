---
collection: k8s
version: "1.31.6"
title: "PodTemplate"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/pod-template.md
fetched_at: 2026-01-16T10:18:07+05:30
---
An API object that defines a template for creating Pods.
The PodTemplate API is also embedded in API definitions for workload management, such as 
Deployment or
StatefulSets.

<!--more--> 

Pod templates allow you to define common metadata (such as labels, or a template for the name of a
new Pod) as well as to specify a pod's desired state.
[Workload management](/docs/concepts/workloads/controllers/) controllers use Pod templates
(embedded into another object, such as a Deployment or StatefulSet)
to define and manage one or more Pods.
When there can be multiple Pods based on the same template, these are called
replicas.
Although you can create a PodTemplate object directly, you rarely need to do so.
