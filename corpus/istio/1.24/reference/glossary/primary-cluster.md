---
collection: istio
version: "1.24"
title: "Primary Cluster"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/glossary/primary-cluster.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
A primary cluster is a [cluster](index.md#cluster) with a
[control plane](index.md#control-plane). A single
[mesh](index.md#service-mesh) can have more than
one primary cluster for HA or to reduce latency. Primary clusters can act as the
control plane for [remote clusters](index.md#remote-cluster).
