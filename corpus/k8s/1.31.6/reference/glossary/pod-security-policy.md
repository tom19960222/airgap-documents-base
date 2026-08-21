---
collection: k8s
version: "1.31.6"
title: "Pod Security Policy"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/pod-security-policy.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enables fine-grained authorization of pod creation and updates.

<!--more--> 

A cluster-level resource that controls security sensitive aspects of the Pod specification. The `PodSecurityPolicy` objects define a set of conditions that a Pod must run with in order to be accepted into the system, as well as defaults for the related fields. Pod Security Policy control is implemented as an optional admission controller.

PodSecurityPolicy was deprecated as of Kubernetes v1.21, and removed in v1.25.
As an alternative, use [Pod Security Admission](/docs/concepts/security/pod-security-admission/) or a 3rd party admission plugin.
