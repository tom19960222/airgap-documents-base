---
collection: k8s
version: "1.31.6"
title: "SeccompDefault"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/seccomp-default.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enables the use of `RuntimeDefault` as the default seccomp profile
for all workloads.
The seccomp profile is specified in the `securityContext` of a Pod and/or a Container.
