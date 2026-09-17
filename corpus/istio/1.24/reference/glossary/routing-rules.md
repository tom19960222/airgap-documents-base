---
collection: istio
version: "1.24"
title: "Routing Rules"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/glossary/routing-rules.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
Routing rules, which you configure in a [virtual service](../../concepts/traffic-management/index.md#virtual-services),
define the paths that requests follow within the service mesh. With routing rules, you can define
conditions to route traffic addressed to the virtual service's host to specific
destination workloads. Routing rules let you control traffic for tasks
like A/B testing, canary rollouts, and staged rollouts with percentage-based traffic splits.
