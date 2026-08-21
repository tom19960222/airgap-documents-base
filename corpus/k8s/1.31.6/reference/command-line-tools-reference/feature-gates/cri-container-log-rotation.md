---
collection: k8s
version: "1.31.6"
title: "CRIContainerLogRotation"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/cri-container-log-rotation.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enable container log rotation for CRI container runtime.
The default max size of a log file is 10MB and the default max number of
log files allowed for a container is 5.
These values can be configured in the kubelet config.
See [logging at node level](/docs/concepts/cluster-administration/logging/#logging-at-the-node-level)
for more details.
