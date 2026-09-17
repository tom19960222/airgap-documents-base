---
collection: istio
version: "1.24"
title: "Zipkin"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/ops/integrations/zipkin/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "How to integrate with Zipkin."
---
[Zipkin](https://zipkin.io/) is a distributed tracing system. It helps gather timing data needed to troubleshoot latency problems in service architectures. Features include both the collection and lookup of this data.

## Installation

### Option 1: Quick start

Istio provides a basic sample installation to quickly get Zipkin up and running:

```bash
$ kubectl apply -f https://raw.githubusercontent.com/istio/istio/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/addons/extras/zipkin.yaml
```

This will deploy Zipkin into your cluster. This is intended for demonstration only, and is not tuned for performance or security.

### Option 2: Customizable install

Consult the [Zipkin documentation](https://zipkin.io/) to get started. No special changes are needed for Zipkin to work with Istio.

## Usage

For information on using Zipkin, please refer to the [Zipkin task](../../../tasks/observability/distributed-tracing/zipkin/index.md).
