---
collection: k8s
version: "1.31.6"
title: "BoundServiceAccountTokenVolume"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/bound-service-account-token-volume.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Migrate ServiceAccount volumes to use a projected volume
consisting of a ServiceAccountTokenVolumeProjection. Cluster admins can use metric
`serviceaccount_stale_tokens_total` to monitor workloads that are depending on the extended
tokens. If there are no such workloads, turn off extended tokens by starting `kube-apiserver` with
flag `--service-account-extend-token-expiration=false`.

Check [Bound Service Account Tokens](https://github.com/kubernetes/enhancements/blob/master/keps/sig-auth/1205-bound-service-account-tokens/README.md)
for more details.
