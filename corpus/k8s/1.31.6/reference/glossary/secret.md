---
collection: k8s
version: "1.31.6"
title: "Secret"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/secret.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Stores sensitive information, such as passwords, OAuth tokens, and SSH keys.

<!--more-->

Secrets give you more control over how sensitive information is used and reduces
the risk of accidental exposure. Secret values are encoded as base64 strings and
are stored unencrypted by default, but can be configured to be
[encrypted at rest](/docs/tasks/administer-cluster/encrypt-data/#ensure-all-secrets-are-encrypted).

A Pod can reference the Secret in
a variety of ways, such as in a volume mount or as an environment variable.
Secrets are designed for confidential data and
[ConfigMaps](/docs/tasks/configure-pod-container/configure-pod-configmap/) are
designed for non-confidential data.
