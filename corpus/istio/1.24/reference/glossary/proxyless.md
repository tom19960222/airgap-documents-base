---
collection: istio
version: "1.24"
title: "Proxyless"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/glossary/proxyless.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
Proxyless refers to a [data plane mode](index.md#data-plane-mode) that runs without proxies by instead
moving mesh functionality directly into applications.
Currently, Istio supports a [Proxyless gRPC](https://istio.io/v1.24/blog/2021/proxyless-grpc/) <!-- unresolved-site-link: route=/blog/2021/proxyless-grpc --> mode,
which enables mesh functionality in the [gRPC framework](https://grpc.io/).
