---
collection: k8s
version: "1.31.6"
title: "EventedPLEG"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/evented-pleg.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enable support for the kubelet to receive container life cycle events from the
container runtime via
an extension to CRI.
(PLEG is an abbreviation for “Pod lifecycle event generator”).
For this feature to be useful, you also need to enable support for container lifecycle events
in each container runtime running in your cluster. If the container runtime does not announce
support for container lifecycle events then the kubelet automatically switches to the legacy
generic PLEG mechanism, even if you have this feature gate enabled.
