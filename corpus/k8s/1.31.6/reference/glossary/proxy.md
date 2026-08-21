---
collection: k8s
version: "1.31.6"
title: "Proxy"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/proxy.md
fetched_at: 2026-01-16T10:18:07+05:30
---
In computing, a proxy is a server that acts as an intermediary for a remote
service.

<!--more-->

A client interacts with the proxy; the proxy copies the client's data to the
actual server; the actual server replies to the proxy; the proxy sends the
actual server's reply to the client.

[kube-proxy](/docs/reference/command-line-tools-reference/kube-proxy/) is a
network proxy that runs on each node in your cluster, implementing part of
the Kubernetes service concept.

You can run kube-proxy as a plain userland proxy service. If your operating
system supports it, you can instead run kube-proxy in a hybrid mode that
achieves the same overall effect using less system resources.
