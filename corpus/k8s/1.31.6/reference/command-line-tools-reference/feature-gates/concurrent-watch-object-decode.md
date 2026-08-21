---
collection: k8s
version: "1.31.6"
title: "ConcurrentWatchObjectDecode"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/concurrent-watch-object-decode.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enable concurrent watch object decoding. This is to avoid starving the API server's
watch cache when a conversion webhook is installed.
