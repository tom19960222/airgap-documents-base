---
collection: "opensearch"
version: "2.19"
title: "Trace Analytics"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_observing-your-data/trace/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_observing-your-data/trace/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/observing-your-data/trace/"
canonical_url: "https://docs.opensearch.org/latest/observing-your-data/trace/index/"
canonical_route: "/observing-your-data/trace/"
redirect_from: ["/observability-plugin/trace/index/","/monitoring-plugins/trace/index/","/observing-your-data/trace/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_order: 40
---
# Trace Analytics

Trace Analytics provides a way to ingest and visualize [OpenTelemetry](https://opentelemetry.io/) data in OpenSearch. This data can help you find and fix performance problems in distributed applications.

A single operation, such as a user choosing a button, can trigger an extended series of events. The frontend might call a backend service, which calls another service, which queries a database, processes the data, and sends it to the original service, which sends a confirmation to the frontend.

Trace Analytics can help you visualize this flow of events and identify performance problems, as shown in the following image.

![Detailed trace view](https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/ta-trace.png)

## Trace Analytics with Jaeger data

Trace Analytics supports Jaeger trace data in the OpenSearch Observability plugin. If you use OpenSearch as the backend for Jaeger trace data, you can use the built-in Trace Analytics capabilities.

To set up your environment to use Trace Analytics, see [Analyze Jaeger trace data](trace-analytics-jaeger/index.md).
