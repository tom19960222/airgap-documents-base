---
collection: k8s
version: "1.31.6"
title: "SELinuxMountReadWriteOncePod"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/selinux-mount-read-write-once-pod.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Speeds up container startup by allowing kubelet to mount volumes
for a Pod directly with the correct SELinux label instead of changing each file on the volumes
recursively. The initial implementation focused on ReadWriteOncePod volumes.
