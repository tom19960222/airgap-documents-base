---
collection: k8s
version: "1.31.6"
title: "DisableKubeletCloudCredentialProviders"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/disable-kubelet-cloud-credential-providers.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enabling the feature gate deactivated the legacy in-tree functionality within the
kubelet, that allowed the kubelet to to authenticate to a cloud provider container registry
for container image pulls.
