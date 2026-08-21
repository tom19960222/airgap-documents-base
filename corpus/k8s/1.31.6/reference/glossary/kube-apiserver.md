---
collection: k8s
version: "1.31.6"
title: "API server"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/kube-apiserver.md
fetched_at: 2026-01-16T10:18:07+05:30
---
The API server is a component of the Kubernetes
control plane that exposes the Kubernetes API.
The API server is the front end for the Kubernetes control plane.

<!--more-->

The main implementation of a Kubernetes API server is [kube-apiserver](/docs/reference/generated/kube-apiserver/).
kube-apiserver is designed to scale horizontally&mdash;that is, it scales by deploying more instances.
You can run several instances of kube-apiserver and balance traffic between those instances.
