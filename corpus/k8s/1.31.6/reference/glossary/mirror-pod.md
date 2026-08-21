---
collection: k8s
version: "1.31.6"
title: "Mirror Pod"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/mirror-pod.md
fetched_at: 2026-01-16T10:18:07+05:30
---
A pod object that a kubelet uses
 to represent a static pod

<!--more--> 

When the kubelet finds a static pod in its configuration, it automatically tries to
create a Pod object on the Kubernetes API server for it. This means that the pod
will be visible on the API server, but cannot be controlled from there.

(For example, removing a mirror pod will not stop the kubelet daemon from running it).
