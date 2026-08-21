---
collection: k8s
version: "1.31.6"
title: "StreamingProxyRedirects"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/streaming-proxy-redirects.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Instructs the API server to intercept (and follow) redirects from the
backend (kubelet) for streaming requests. Examples of streaming requests include the `exec`,
`attach` and `port-forward` requests.
