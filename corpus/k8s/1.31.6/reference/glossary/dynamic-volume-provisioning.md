---
collection: k8s
version: "1.31.6"
title: "Dynamic Volume Provisioning"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/dynamic-volume-provisioning.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Allows users to request automatic creation of storage  Volumes.

<!--more--> 

Dynamic provisioning eliminates the need for cluster administrators to pre-provision storage. Instead, it automatically provisions storage by user request. Dynamic volume provisioning is based on an API object, StorageClass, referring to a Volume Plugin that provisions a Volume and the set of parameters to pass to the Volume Plugin.
