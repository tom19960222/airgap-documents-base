---
collection: ceph
version: "19.2.2"
title: "Tracing Services"
source_url: https://docs.ceph.com/en/squid/cephadm/services/tracing/
fetched_at: 2026-07-27T16:39:25+00:00
---
# Tracing Services

## Jaeger Tracing

Ceph uses Jaeger as the tracing backend. in order to use tracing, we need to deploy those services.

Further details on tracing in ceph:

[Ceph Tracing documentation](https://docs.ceph.com/en/latest/jaegertracing/#jaeger-distributed-tracing/)

## Deployment

Jaeger services consist of 3 services:

1. Jaeger Agent
2. Jaeger Collector
3. Jaeger Query

Jaeger requires a database for the traces. we use ElasticSearch (version 6) by default.

To deploy jaeger tracing service, when not using your own ElasticSearch:

1. Deploy jaeger services, with a new elasticsearch container:

   > ```
   > ceph orch apply jaeger
   > ```
2. Deploy jaeger services, with existing elasticsearch cluster and existing jaeger query (deploy agents and collectors):

   > ```
   > ceph orch apply jaeger --without-query --es_nodes=ip:port,..
   > ```

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
