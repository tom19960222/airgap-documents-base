---
collection: k8s
version: "1.31.6"
title: "BalanceAttachedNodeVolumes"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/balance-attached-node-volumes.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Include volume count on node to be considered for
balanced resource allocation while scheduling. A node which has closer CPU,
memory utilization, and volume count is favored by the scheduler while making decisions.
