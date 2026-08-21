---
collection: k8s
version: "1.31.6"
title: "ConsistentListFromCache"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/consistent-list-from-cache.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enhance Kubernetes API server performance by serving consistent **list** requests
directly from its watch cache, improving scalability and response times.
To consistent list from cache Kubernetes requires a newer etcd version (v3.4.31+ or v3.5.13+),
that includes fixes to watch progress request feature.
If older etcd version is provided Kubernetes will automatically detect it and fallback to serving consistent reads from etcd.
Progress notifications ensure watch cache is consistent with etcd while reducing
the need for resource-intensive quorum reads from etcd.

See the Kubernetes documentation on [Semantics for **get** and **list**](/docs/reference/using-api/api-concepts/#semantics-for-get-and-list) for more details.
