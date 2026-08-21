---
collection: k8s
version: "1.31.6"
title: "Spec"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/spec.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Defines how each object, like Pods or Services, should be configured and its desired state.

<!--more-->
Almost every Kubernetes object includes two nested object fields that govern the object's configuration: the object spec and the object status. For objects that have a spec, you have to set this when you create the object, providing a description of the characteristics you want the resource to have: its desired state.

It varies for different objects like Pods, StatefulSets, and Services, detailing settings such as containers, volumes, replicas, ports,   
and other specifications unique to each object type. This field encapsulates what state Kubernetes should maintain for the defined   
object.
