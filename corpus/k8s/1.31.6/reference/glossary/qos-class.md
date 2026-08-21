---
collection: k8s
version: "1.31.6"
title: "QoS Class"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/qos-class.md
fetched_at: 2026-01-16T10:18:07+05:30
---
QoS Class (Quality of Service Class) provides a way for Kubernetes to classify Pods within the cluster into several classes and make decisions about scheduling and eviction.

<!--more--> 
QoS Class of a Pod is set at creation time  based on its compute resources requests and limits settings. QoS classes are used to make decisions about Pods scheduling and eviction.
Kubernetes can assign one of the following  QoS classes to a Pod: `Guaranteed`, `Burstable` or `BestEffort`.
