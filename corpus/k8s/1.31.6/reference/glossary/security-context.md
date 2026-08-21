---
collection: k8s
version: "1.31.6"
title: "Security Context"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/security-context.md
fetched_at: 2026-01-16T10:18:07+05:30
---
The `securityContext` field defines privilege and access control settings for
a Pod or
container.

<!--more-->

In a `securityContext`, you can define: the user that processes run as,
the group that processes run as, and privilege settings.
You can also configure security policies (for example: SELinux, AppArmor or seccomp).

The `PodSpec.securityContext` setting applies to all containers in a Pod.
