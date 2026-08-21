---
collection: k8s
version: "1.31.6"
title: "ZeroLimitedNominalConcurrencyShares"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/zero-limited-nominal-concurrency-shares.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Allow [priority & fairness](/docs/concepts/cluster-administration/flow-control/)
in the API server to use a zero value for the `nominalConcurrencyShares` field of
the `limited` section of a priority level.
