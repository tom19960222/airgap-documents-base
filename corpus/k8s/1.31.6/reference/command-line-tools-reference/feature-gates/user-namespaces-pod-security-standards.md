---
collection: k8s
version: "1.31.6"
title: "UserNamespacesPodSecurityStandards"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/user-namespaces-pod-security-standards.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enable Pod Security Standards policies relaxation for pods
that run with namespaces. You must set the value of this feature gate consistently across all nodes in
your cluster, and you must also enable `UserNamespacesSupport` to use this feature.
