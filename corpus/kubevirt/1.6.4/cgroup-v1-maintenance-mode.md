---
collection: kubevirt
version: "1.6.4"
title: "Cgroup v1 is moving to maintenance mode"
source_url: https://github.com/kubevirt/kubevirt/blob/ac5324e8f6e7cda1cfe92542df3ceb0cd0d8e68f/docs/cgroup-v1-maintenance-mode.md
fetched_at: 2026-03-16T09:25:18Z
---
# Cgroup v1 is moving to maintenance mode

## Introduction

The containerized world, including many technologies like Kubernetes, systemd and Kubevirt,
were originally designed to run on cgroup v1.

At this point, cgroup v2 is the default cgroup manager for most distributions and is widely adopted.

Kubernetes had moved cgroup support to maintenance mode in 1.31, and Kubevirt is following this path.

For more info, please look at the Kubernetes blog-post on the subject:
https://kubernetes.io/blog/2024/08/14/kubernetes-1-31-moving-cgroup-v1-support-maintenance-mode/

## What does this mean?

Quoting from Kubernetes' blog-post:

> When cgroup v1 is placed into maintenance mode in Kubernetes, it means that:
>
> Feature Freeze: No new features will be added to cgroup v1 support.
> Security Fixes: Critical security fixes will still be provided.
> Best-Effort Bug Fixes: Major bugs may be fixed if feasible, but some issues might remain unresolved.

Kubevirt will follow the same principles.
