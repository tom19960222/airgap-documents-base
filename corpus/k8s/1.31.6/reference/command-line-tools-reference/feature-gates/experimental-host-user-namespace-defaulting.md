---
collection: k8s
version: "1.31.6"
title: "ExperimentalHostUserNamespaceDefaulting"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/experimental-host-user-namespace-defaulting.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enabling the defaulting user
namespace to host. This is for containers that are using other host namespaces,
host mounts, or containers that are privileged or using specific non-namespaced
capabilities (e.g. `MKNODE`, `SYS_MODULE` etc.). This should only be enabled
if user namespace remapping is enabled in the Docker daemon.
