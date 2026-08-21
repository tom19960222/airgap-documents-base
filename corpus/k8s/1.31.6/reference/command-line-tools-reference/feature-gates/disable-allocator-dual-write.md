---
collection: k8s
version: "1.31.6"
title: "DisableAllocatorDualWrite"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/disable-allocator-dual-write.md
fetched_at: 2026-01-16T10:18:07+05:30
---
You can enable the `MultiCIDRServiceAllocator` feature gate. The API server supports migration
from the old bitmap ClusterIP allocators to the new IPAddress allocators.

The API server performs a dual-write on both allocators. This feature gate disables the dual write
on the new Cluster IP allocators; you can enable this feature gate if you have completed the
relevant stage of the migration.
