---
collection: k8s
version: "1.31.6"
title: "RetryGenerateName"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/retry-generate-name.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enables retrying of object creation when the
API server
is expected to generate a [name](/docs/concepts/overview/working-with-objects/names/#names).

When this feature is enabled, requests using `generateName` are retried automatically in case the
control plane detects a name conflict with an existing object, up to a limit of 8 total attempts.
