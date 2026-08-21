---
collection: k8s
version: "1.31.6"
title: "Persistent Volume"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/persistent-volume.md
fetched_at: 2026-01-16T10:18:07+05:30
---
An API object that represents a piece of storage in the cluster. Available as a general, pluggable resource that persists beyond the lifecycle of any individual Pod.

<!--more--> 

PersistentVolumes (PVs) provide an API that abstracts details of how storage is provided from how it is consumed.
PVs are used directly in scenarios where storage can be created ahead of time (static provisioning).
For scenarios that require on-demand storage (dynamic provisioning), PersistentVolumeClaims (PVCs) are used instead.
