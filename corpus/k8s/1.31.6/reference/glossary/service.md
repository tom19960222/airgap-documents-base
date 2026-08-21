---
collection: k8s
version: "1.31.6"
title: "Service"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/service.md
fetched_at: 2026-01-16T10:18:07+05:30
---
A method for exposing a network application that is running as one or more
Pods in your cluster.

<!--more-->

The set of Pods targeted by a Service is (usually) determined by a
selector. If more Pods are added or removed,
the set of Pods matching the selector will change. The Service makes sure that network traffic
can be directed to the current set of Pods for the workload.

Kubernetes Services either use IP networking (IPv4, IPv6, or both), or reference an external name in
the Domain Name System (DNS).

The Service abstraction enables other mechanisms, such as Ingress and Gateway.
