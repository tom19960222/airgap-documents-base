---
collection: k8s
version: "1.31.6"
title: "kube-proxy"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/kube-proxy.md
fetched_at: 2026-01-16T10:18:07+05:30
---
kube-proxy is a network proxy that runs on each
node in your cluster,
implementing part of the Kubernetes
service concept.

<!--more-->

[kube-proxy](/docs/reference/command-line-tools-reference/kube-proxy/)
maintains network rules on nodes. These network rules allow network
communication to your Pods from network sessions inside or outside of
your cluster.

kube-proxy uses the operating system packet filtering layer if there is one
and it's available. Otherwise, kube-proxy forwards the traffic itself.
