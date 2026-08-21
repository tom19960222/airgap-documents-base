---
collection: k8s
version: "1.31.6"
title: "Storage Class"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/storage-class.md
fetched_at: 2026-01-16T10:18:07+05:30
---
A StorageClass provides a way for administrators to describe different available storage types.

<!--more--> 

StorageClasses can map to quality-of-service levels, backup policies, or to arbitrary policies determined by cluster administrators. Each StorageClass contains the fields `provisioner`, `parameters`, and `reclaimPolicy`, which are used when a Persistent Volume belonging to the class needs to be dynamically provisioned. Users can request a particular class using the name of a StorageClass object.
