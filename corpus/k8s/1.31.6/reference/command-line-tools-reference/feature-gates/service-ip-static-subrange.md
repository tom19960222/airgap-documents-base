---
collection: k8s
version: "1.31.6"
title: "ServiceIPStaticSubrange"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/service-ip-static-subrange.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enables a strategy for Services ClusterIP allocations, whereby the
ClusterIP range is subdivided. Dynamic allocated ClusterIP addresses will be allocated preferently
from the upper range allowing users to assign static ClusterIPs from the lower range with a low
risk of collision. See
[Avoiding collisions](/docs/reference/networking/virtual-ips/#avoiding-collisions)
for more details.
