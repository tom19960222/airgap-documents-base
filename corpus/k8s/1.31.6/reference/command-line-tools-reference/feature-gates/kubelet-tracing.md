---
collection: k8s
version: "1.31.6"
title: "KubeletTracing"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/kubelet-tracing.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Add support for distributed tracing in the kubelet.
When enabled, kubelet CRI interface and authenticated http servers are instrumented to generate
OpenTelemetry trace spans.
See [Traces for Kubernetes System Components](/docs/concepts/cluster-administration/system-traces) for more details.
