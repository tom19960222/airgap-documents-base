---
collection: k8s
version: "1.31.6"
title: "RemoveSelfLink"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/RemoveSelfLink.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Sets the `.metadata.selfLink` field to blank (empty string) for all
objects and collections. This field has been deprecated since the Kubernetes v1.16
release. When this feature is enabled, the `.metadata.selfLink` field remains part of
the Kubernetes API, but is always unset.
