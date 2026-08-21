---
collection: k8s
version: "1.31.6"
title: "Container Storage Interface (CSI)"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/csi.md
fetched_at: 2026-01-16T10:18:07+05:30
---
The Container Storage Interface (CSI) defines a standard interface to expose storage systems to containers.

<!--more--> 

CSI allows vendors to create custom storage plugins for Kubernetes without adding them to the Kubernetes repository (out-of-tree plugins). To use a CSI driver from a storage provider, you must first [deploy it to your cluster](https://kubernetes-csi.github.io/docs/deploying.html). You will then be able to create a Storage Class that uses that CSI driver.

* [CSI in the Kubernetes documentation](/docs/concepts/storage/volumes/#csi)
* [List of available CSI drivers](https://kubernetes-csi.github.io/docs/drivers.html)
