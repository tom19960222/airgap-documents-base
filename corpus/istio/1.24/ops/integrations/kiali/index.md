---
collection: istio
version: "1.24"
title: "Kiali"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/ops/integrations/kiali/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Information on how to integrate with Kiali."
---
[Kiali](https://kiali.io/) is an observability console for Istio with service mesh configuration and validation capabilities.
It helps you understand the structure and health of your service mesh by monitoring traffic flow to infer the topology and report errors.
Kiali provides detailed metrics and a basic [Grafana](../grafana/index.md) integration, which can be used for advanced queries.
Distributed tracing is provided by integration with [Jaeger](../jaeger/index.md).

## Installation

### Option 1: Quick start

Istio provides a basic sample installation to quickly get Kiali up and running:

```bash
$ kubectl apply -f https://raw.githubusercontent.com/istio/istio/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/addons/kiali.yaml
```

This will deploy Kiali into your cluster. This is intended for demonstration only, and is not tuned for performance or security.

> **Idea:**
>
> If you use this sample YAML and plan to publicly expose the resulting Kiali
> installation, be sure to change the `signing_key` in Kiali's ConfigMap when using an
> authentication strategy other than `anonymous`.

### Option 2: Customizable install

The Kiali project offers its own [quick start guide](https://kiali.io/docs/installation/quick-start)
and [customizable installation methods](https://kiali.io/docs/installation/installation-guide).
We recommend production users follow those instructions to ensure they stay up to date with the latest versions and best practices.

## Usage

For more information about using Kiali, see the [Visualizing Your Mesh](../../../tasks/observability/kiali/index.md) task.
