---
collection: k8s
version: "1.31.6"
title: "KMSv2KDF"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/kmsv2-kdf.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enables KMS v2 to generate single use data encryption keys.
See [Using a KMS Provider for data encryption](/docs/tasks/administer-cluster/kms-provider) for more details.
If the `KMSv2` feature gate is not enabled in your cluster, the value of the `KMSv2KDF` feature gate has no effect.
