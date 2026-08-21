---
collection: k8s
version: "1.31.6"
title: "Device Plugin"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/device-plugin.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Device plugins run on worker
Nodes and provide
Pods  with access to resources,
such as local hardware, that require vendor-specific initialization or setup
steps.

<!--more-->

Device plugins advertise resources to the
kubelet, so that workload
Pods can access hardware features that relate to the Node where that Pod is running.
You can deploy a device plugin as a daemonset,
or install the device plugin software directly on each target Node.

See
[Device Plugins](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/)
for more information.
