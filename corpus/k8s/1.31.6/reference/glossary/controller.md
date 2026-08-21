---
collection: k8s
version: "1.31.6"
title: "Controller"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/controller.md
fetched_at: 2026-01-16T10:18:07+05:30
---
In Kubernetes, controllers are control loops that watch the state of your
cluster, then make or request
changes where needed.
Each controller tries to move the current cluster state closer to the desired
state.

<!--more-->

Controllers watch the shared state of your cluster through the
apiserver (part of the
control-plane).

Some controllers also run inside the control plane, providing control loops that
are core to Kubernetes' operations. For example: the deployment controller, the
daemonset controller, the namespace controller, and the persistent volume
controller (and others) all run within the
kube-controller-manager.
