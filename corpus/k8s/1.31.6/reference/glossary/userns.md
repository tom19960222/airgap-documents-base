---
collection: k8s
version: "1.31.6"
title: "user namespace"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/userns.md
fetched_at: 2026-01-16T10:18:07+05:30
---
A kernel feature to emulate root. Used for "rootless containers".

<!--more-->

User namespaces are a Linux kernel feature that allows a non-root user to
emulate superuser ("root") privileges,
for example in order to run containers without being a superuser outside the container.

User namespace is effective for mitigating damage of potential container break-out attacks.

In the context of user namespaces, the namespace is a Linux kernel feature, and not a
namespace in the Kubernetes sense
of the term.

<!-- TODO: https://kinvolk.io/blog/2020/12/improving-kubernetes-and-container-security-with-user-namespaces/ -->
