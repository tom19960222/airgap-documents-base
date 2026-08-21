---
collection: k8s
version: "1.31.6"
title: "RootCAConfigMap"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/root-ca-config-map.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Configure the `kube-controller-manager` to publish a
ConfigMap named `kube-root-ca.crt`
to every namespace. This ConfigMap contains a CA bundle used for verifying connections
to the kube-apiserver. See
[Bound Service Account Tokens](https://github.com/kubernetes/enhancements/blob/master/keps/sig-auth/1205-bound-service-account-tokens/README.md)
for more details.
