---
collection: ceph
version: "19.2.2"
title: "Rook"
source_url: https://docs.ceph.com/en/squid/mgr/rook/
fetched_at: 2026-07-27T16:40:55+00:00
---
# Rook

Rook (<https://rook.io/>) is an orchestration tool that can run Ceph inside
a Kubernetes cluster.

The `rook` module provides integration between Ceph’s orchestrator framework
(used by modules such as `dashboard` to control cluster services) and
Rook.

Orchestrator modules only provide services to other modules, which in turn
provide user interfaces. To try out the rook module, you might like
to use the [Orchestrator CLI](../orchestrator/index.md#orchestrator-cli-module) module.

## Requirements

- Running ceph-mon and ceph-mgr services that were set up with Rook in
  Kubernetes.
- Rook 0.9 or newer.

## Configuration

Because a Rook cluster’s ceph-mgr daemon is running as a Kubernetes pod,
the `rook` module can connect to the Kubernetes API without any explicit
configuration.

## Development

If you are a developer, please see [Hacking on Ceph in Kubernetes with Rook](../../dev/kubernetes/index.md#kubernetes-dev) for instructions
on setting up a development environment to work with this.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
