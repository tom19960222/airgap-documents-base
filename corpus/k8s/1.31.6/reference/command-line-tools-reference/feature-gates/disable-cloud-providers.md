---
collection: k8s
version: "1.31.6"
title: "DisableCloudProviders"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/disable-cloud-providers.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enabling this feature gate deactivated functionality in `kube-apiserver`,
`kube-controller-manager` and `kubelet` that related to the `--cloud-provider`
command line argument.

In Kubernetes v1.31 and later, the only valid values for `--cloud-provider`
are the empty string (no cloud provider integration), or "external"
(integration via a separate cloud-controller-manager).
