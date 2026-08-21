---
collection: k8s
version: "1.31.6"
title: "LocalStorageCapacityIsolationFSQuotaMonitoring"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/local-storage-capacity-isolation-fs-quota-monitoring.md
fetched_at: 2026-01-16T10:18:07+05:30
---
When `LocalStorageCapacityIsolation` 
is enabled for 
[local ephemeral storage](/docs/concepts/configuration/manage-resources-containers/), 
the backing filesystem for [emptyDir volumes](/docs/concepts/storage/volumes/#emptydir) supports project quotas,
and `UserNamespacesSupport` is enabled, 
project quotas are used to monitor `emptyDir` volume storage consumption rather than using filesystem walk, ensuring better performance and accuracy.
