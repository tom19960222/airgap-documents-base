---
collection: k8s
version: "1.31.6"
title: "CRI-O"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/cri-o.md
fetched_at: 2026-01-16T10:18:07+05:30
---
A tool that lets you use OCI container runtimes with Kubernetes CRI.

<!--more-->

CRI-O is an implementation of the cri
to enable using container
runtimes that are compatible with the Open Container Initiative (OCI)
[runtime spec](https://www.github.com/opencontainers/runtime-spec).

Deploying CRI-O allows Kubernetes to use any OCI-compliant runtime as the container
runtime for running Pods, and to fetch
OCI container images from remote registries.
