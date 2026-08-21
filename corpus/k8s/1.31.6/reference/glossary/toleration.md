---
collection: k8s
version: "1.31.6"
title: "Toleration"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/toleration.md
fetched_at: 2026-01-16T10:18:07+05:30
---
A core object consisting of three required properties: key, value, and effect. Tolerations enable the scheduling of pods on nodes or node groups that have matching taints.

<!--more-->

Tolerations and taints work together to ensure that pods are not scheduled onto inappropriate nodes. One or more tolerations are applied to a pod. A toleration indicates that the pod is allowed (but not required) to be scheduled on nodes or node groups with matching taints.
