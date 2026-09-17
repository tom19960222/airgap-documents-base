---
collection: istio
version: "1.24"
title: "Jaeger"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/ops/integrations/jaeger/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "How to integrate with Jaeger."
---
[Jaeger](https://www.jaegertracing.io/) is an open source end to end distributed tracing system,
allowing users to monitor and troubleshoot transactions in complex distributed systems.

## Installation

### Option 1: Quick start

Istio provides a basic sample installation to quickly get Jaeger up and running:

```bash
$ kubectl apply -f https://raw.githubusercontent.com/istio/istio/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/addons/jaeger.yaml
```

This will deploy Jaeger into your cluster. This is intended for demonstration only,
and is not tuned for performance or security.

### Option 2: Customizable install

Consult the [Jaeger documentation](https://www.jaegertracing.io/) to get started.
No special changes are needed for Jaeger to work with Istio.

## Usage

For information on using Jaeger, please refer to the
[Jaeger task](../../../tasks/observability/distributed-tracing/jaeger/index.md).
