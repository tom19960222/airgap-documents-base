---
collection: "opensearch"
version: "2.19"
title: "Simple Schema for Observability"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_observing-your-data/ss4o.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_observing-your-data/ss4o.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/observing-your-data/ss4o/"
canonical_url: "https://docs.opensearch.org/latest/observing-your-data/ss4o/"
canonical_route: "/observing-your-data/ss4o/"
redirect_from: ["/observing-your-data/ssfo/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 120
---
# Simple Schema for Observability
Introduced 2.6
{: .label .label-purple }

[Observability](../index.md) is a collection of plugins and applications that let you visualize data-driven events by using Piped Processing Language (PPL) to explore and query data stored in OpenSearch. [Simple Schema for Observability](https://github.com/opensearch-project/opensearch-catalog/tree/main/docs/schema/observability), which uses the schema convention `ss4o`, is a standardization for conforming to a common and unified observability schema. With the schema in place, Observability tools can ingest, automatically extract, and aggregate data and create custom dashboards, making it easier to understand the system at a higher level.

The Simple Schema for Observability is inspired by both [OpenTelemetry](https://opentelemetry.io/docs/) and the Elastic Common Schema (ECS) and uses Amazon Elastic Container Service ([Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_cwe_events.html)) event logs and OpenTelemetry (OTel) metadata.

Alerts will be supported in a future release.
{: .note }

## Use cases

Use cases for the Simple Schema for Observability include:

* Ingesting observability data from different data types.
* Moving from proprietary configurations that are non-transferable to a consolidated, sharable observability solution that allows users to ingest and display an analysis of any type of telemetry data from any type of provider.
* Conforming dashboards to the schema to align with the data structure so that you can design and organize the dashboard components and visualizations in a way that effectively represents your data.

Data Prepper conforms to the schema for metrics and will gradually support traces and logs. Data Prepper's [trace mapping](https://docs.opensearch.org/latest/data-prepper/common-use-cases/trace-analytics/) <!-- unresolved-jekyll-link: route=/data-prepper/common-use-cases/trace-analytics/ --> currently provides `service-map` data in a different way than `ss4o` traces. To make the trace mapping compatible with Observability, it will be integrated with the `ss4o` traces schema and will introduce `service-map` as an enriched field.
{: .note }

## Traces and metrics

Schema definitions for traces and metrics are defined and supported by the Observability plugin. These schema definitions include:

- The index structure (mapping).
- The [index naming conventions](https://github.com/opensearch-project/observability/issues/1405).
- A JSON schema for enforcement and validation of the structure.
- The [integration](https://github.com/opensearch-project/OpenSearch-Dashboards/issues/3412) feature for adding preconfigured dashboards and assets.
