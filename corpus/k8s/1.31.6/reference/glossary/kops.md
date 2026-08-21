---
collection: k8s
version: "1.31.6"
title: "kOps (Kubernetes Operations)"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/kops.md
fetched_at: 2026-01-16T10:18:07+05:30
---
`kOps` will not only help you create, destroy, upgrade and maintain production-grade, highly available, Kubernetes cluster, but it will also provision the necessary cloud infrastructure.

<!--more--> 

> **Note:**
>
> AWS (Amazon Web Services) is currently officially supported, with DigitalOcean, GCE and OpenStack in beta support, and Azure in alpha.

`kOps` is an automated provisioning system:
  * Fully automated installation
  * Uses DNS to identify clusters
  * Self-healing: everything runs in Auto-Scaling Groups
  * Multiple OS support (Amazon Linux, Debian, Flatcar, RHEL, Rocky and Ubuntu)
  * High-Availability support
  * Can directly provision, or generate terraform manifests
