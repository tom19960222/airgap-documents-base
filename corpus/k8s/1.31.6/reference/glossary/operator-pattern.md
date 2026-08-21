---
collection: k8s
version: "1.31.6"
title: "Operator pattern"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/operator-pattern.md
fetched_at: 2026-01-16T10:18:07+05:30
---
The [operator pattern](/docs/concepts/extend-kubernetes/operator/) is a system
design that links a controller to one or more custom
resources.

<!--more-->

You can extend Kubernetes by adding controllers to your cluster, beyond the built-in
controllers that come as part of Kubernetes itself.

If a running application acts as a controller and has API access to carry out tasks
against a custom resource that's defined in the control plane, that's an example of
the Operator pattern.
