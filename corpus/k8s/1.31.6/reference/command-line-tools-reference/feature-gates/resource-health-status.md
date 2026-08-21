---
collection: k8s
version: "1.31.6"
title: "ResourceHealthStatus"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/resource-health-status.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enable the `allocatedResourcesStatus` field within the `.status` for a Pod. The field
reports additional details for each container in the Pod,
with the health information for each device assigned to the Pod.
See [Device plugin and unhealthy devices](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/#device-plugin-and-unhealthy-devices) for more details.
