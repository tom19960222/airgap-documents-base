---
collection: istio
version: "1.24"
title: "Workload"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/glossary/workload.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
A binary deployed by [operators](index.md#operator) to deliver some function of a service mesh application.
Workloads have names, namespaces, and unique ids. These properties are available in policy and telemetry configuration
using the following [attributes](index.md#attribute):

* `source.workload.name`, `source.workload.namespace`, `source.workload.uid`
* `destination.workload.name`, `destination.workload.namespace`, `destination.workload.uid`

In Kubernetes, a workload typically corresponds to a Kubernetes deployment,
while a [workload instance](index.md#workload-instance) corresponds to an individual [pod](index.md#pod) managed
by the deployment.
