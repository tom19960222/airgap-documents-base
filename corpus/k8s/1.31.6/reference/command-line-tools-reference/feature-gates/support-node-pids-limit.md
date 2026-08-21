---
collection: k8s
version: "1.31.6"
title: "SupportNodePidsLimit"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/support-node-pids-limit.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enable the support to limiting PIDs on the Node.  The parameter
`pid=<number>` in the `--system-reserved` and `--kube-reserved` options can be specified to
ensure that the specified number of process IDs will be reserved for the system as a whole and for
 Kubernetes system daemons respectively.
