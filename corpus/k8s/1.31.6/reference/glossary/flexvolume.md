---
collection: k8s
version: "1.31.6"
title: "FlexVolume"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/flexvolume.md
fetched_at: 2026-01-16T10:18:07+05:30
---
FlexVolume is a deprecated interface for creating out-of-tree volume plugins. The Container Storage Interface is a newer interface that addresses several problems with FlexVolume.

<!--more--> 

FlexVolumes enable users to write their own drivers and add support for their volumes in Kubernetes. FlexVolume driver binaries and dependencies must be installed on host machines. This requires root access. The Storage SIG suggests implementing a CSI driver if possible since it addresses the limitations with FlexVolumes.

* [FlexVolume in the Kubernetes documentation](/docs/concepts/storage/volumes/#flexvolume)
* [More information on FlexVolumes](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-storage/flexvolume.md)
* [Volume Plugin FAQ for Storage Vendors](https://github.com/kubernetes/community/blob/master/sig-storage/volume-plugin-faq.md)
