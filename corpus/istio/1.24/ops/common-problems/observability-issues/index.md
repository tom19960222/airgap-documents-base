---
collection: istio
version: "1.24"
title: "Observability Problems"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/ops/common-problems/observability-issues/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Dealing with telemetry collection issues."
---
## No traces appearing in Zipkin when running Istio locally on Mac

Istio is installed and everything seems to be working except there are no traces showing up in Zipkin when there
should be.

This may be caused by a known [Docker issue](https://github.com/docker/for-mac/issues/1260) where the time inside
containers may skew significantly from the time on the host machine. If this is the case,
when you select a very long date range in Zipkin you will see the traces appearing as much as several days too early.

You can also confirm this problem by comparing the date inside a Docker container to outside:

```bash
$ docker run --entrypoint date gcr.io/istio-testing/ubuntu-16-04-slave:latest
Sun Jun 11 11:44:18 UTC 2017
```

```bash
$ date -u
Thu Jun 15 02:25:42 UTC 2017
```

To fix the problem, you'll need to shutdown and then restart Docker before reinstalling Istio.

## Missing Grafana output

If you're unable to get Grafana output when connecting from a local web client to Istio remotely hosted, you
should validate the client and server date and time match.

The time of the web client (e.g. Chrome) affects the output from Grafana. A simple solution
to this problem is to verify a time synchronization service is running correctly within the
Kubernetes cluster and the web client machine also is correctly using a time synchronization
service. Some common time synchronization systems are NTP and Chrony. This is especially
problematic in engineering labs with firewalls. In these scenarios, NTP may not be configured
properly to point at the lab-based NTP services.

## Verify Istio CNI pods are running (if used)

The Istio CNI plugin performs the Istio mesh pod traffic redirection in the Kubernetes pod lifecycle’s network setup phase, thereby removing the [requirement for the `NET_ADMIN` and `NET_RAW` capabilities](../../deployment/application-requirements/index.md) for users deploying pods into the Istio mesh. The Istio CNI plugin replaces the functionality provided by the `istio-init` container.

1. Verify that the `istio-cni-node` pods are running:

```bash
$ kubectl -n kube-system get pod -l k8s-app=istio-cni-node
```

1. If `PodSecurityPolicy` is being enforced in your cluster, ensure the `istio-cni` service account can use a `PodSecurityPolicy` which [allows the `NET_ADMIN` and `NET_RAW` capabilities](../../deployment/application-requirements/index.md).
