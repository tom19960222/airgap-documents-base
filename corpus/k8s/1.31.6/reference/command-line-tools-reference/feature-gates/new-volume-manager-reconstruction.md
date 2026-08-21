---
collection: k8s
version: "1.31.6"
title: "NewVolumeManagerReconstruction"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/new-volume-manager-reconstruction.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enables improved discovery of mounted volumes during kubelet
startup. Since the associated code had been significantly refactored, Kubernetes versions 1.25 to 1.29
allowed you to opt-out in case the kubelet got stuck at the startup, or did not unmount volumes
from terminated Pods.

This refactoring was behind the `SELinuxMountReadWriteOncePod`  feature gate in Kubernetes
releases 1.25 and 1.26.
