---
collection: k8s
version: "1.31.6"
title: "IngressClassNamespacedParams"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/ingress-class-namespaced-params.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Allow namespace-scoped parameters reference in
`IngressClass` resource. This feature adds two fields - `Scope` and `Namespace`
to `IngressClass.spec.parameters`.
