---
collection: k8s
version: "1.31.6"
title: "ReadOnlyAPIDataVolumes"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/readonly-apidata-volumes.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Set [`configMap`](/docs/concepts/storage/volumes/#configmap), 
[`secret`](/docs/concepts/storage/volumes/#secret), 
[`downwardAPI`](/docs/concepts/storage/volumes/#downwardapi) and 
[`projected`](/docs/concepts/storage/volumes/#projected) 
volumes to be mounted read-only.

Since Kubernetes v1.10, these volume types are always read-only and you cannot opt out.
