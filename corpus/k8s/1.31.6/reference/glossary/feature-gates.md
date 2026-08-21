---
collection: k8s
version: "1.31.6"
title: "Feature gate"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/feature-gates.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Feature gates are a set of keys (opaque string values) that you can use to control which
Kubernetes features are enabled in your cluster.

<!--more-->

You can turn these features on or off using the `--feature-gates` command line flag on each Kubernetes component.
Each Kubernetes component lets you enable or disable a set of feature gates that are relevant to that component.
The Kubernetes documentation lists all current 
[feature gates](/docs/reference/command-line-tools-reference/feature-gates/) and what they control.
