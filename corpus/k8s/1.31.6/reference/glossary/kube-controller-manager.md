---
collection: k8s
version: "1.31.6"
title: "kube-controller-manager"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/kube-controller-manager.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Control plane component that runs controller processes.

<!--more-->

Logically, each controller is a separate process, but to reduce complexity, they are all compiled into a single binary and run in a single process.
