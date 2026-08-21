---
collection: k8s
version: "1.31.6"
title: "CIDR"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/cidr.md
fetched_at: 2026-01-16T10:18:07+05:30
---
CIDR (Classless Inter-Domain Routing) is a notation for describing blocks of IP addresses and is used heavily in various networking configurations.

<!--more-->

In the context of Kubernetes, each Node is assigned a range of IP addresses through the start address and a subnet mask using CIDR. This allows Nodes to assign each Pod a unique IP address. Although originally a concept for IPv4, CIDR has also been expanded to include IPv6.
