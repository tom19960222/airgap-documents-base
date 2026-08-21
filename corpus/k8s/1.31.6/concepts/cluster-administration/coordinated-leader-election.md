---
collection: k8s
version: "1.31.6"
title: "Coordinated Leader Election"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/concepts/cluster-administration/coordinated-leader-election.md
fetched_at: 2026-01-16T10:18:07+05:30
---
<!-- overview -->

(Feature gate: CoordinatedLeaderElection)

Kubernetes 1.31 includes an alpha feature that allows control plane components to
deterministically select a leader via _coordinated leader election_.
This is useful to satisfy Kubernetes version skew constraints during cluster upgrades.
Currently, the only builtin selection strategy is `OldestEmulationVersion`,
preferring the leader with the lowest emulation version, followed by binary
version, followed by creation timestamp.

## Enabling coordinated leader election

Ensure that `CoordinatedLeaderElection` [feature
gate](/docs/reference/command-line-tools-reference/feature-gates/) is enabled
when you start the API Server: and that the `coordination.k8s.io/v1alpha1` API group is
enabled.

This can be done by setting flags `--feature-gates="CoordinatedLeaderElection=true"` and
`--runtime-config="coordination.k8s.io/v1alpha1=true"`.

## Component configuration
Provided that you have enabled the `CoordinatedLeaderElection` feature gate _and_  
have the `coordination.k8s.io/v1alpha1` API group enabled, compatible control plane  
components automatically use the LeaseCandidate and Lease APIs to elect a leader  
as needed.  

For Kubernetes 1.31, two control plane components  
(kube-controller-manager and kube-scheduler) automatically use coordinated  
leader election when the feature gate and API group are enabled.
