---
collection: "opensearch-dashboards"
version: "2.19"
title: "Data sources"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_dashboards/management/data-sources.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_dashboards/management/data-sources.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/dashboards/management/data-sources/"
canonical_url: "https://docs.opensearch.org/latest/dashboards/management/data-sources/"
canonical_route: "/dashboards/management/data-sources/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.1"
chart_version: ""
has_children: true
layout: "default"
nav_order: 110
---
# Data sources

OpenSearch data sources are the applications that OpenSearch can connect to and ingest data from. Once your data sources have been connected and your data has been ingested, it can be indexed, searched, and analyzed using [REST APIs](https://docs.opensearch.org/latest/api-reference/index/) <!-- unresolved-cross-corpus-link: collection=opensearch route=/api-reference/ --> or the OpenSearch Dashboards UI.

This documentation focuses on using the OpenSeach Dashboards interface to connect and manage your data sources. For information about using an API to connect data sources, see the developer resources linked under [Next steps](#next-steps).

## Prerequisites

The first step in connecting your data sources to OpenSearch is to install OpenSearch and OpenSearch Dashboards on your system. Refer to the [installation instructions](https://docs.opensearch.org/latest/install-and-configure/index/) <!-- unresolved-cross-corpus-link: collection=opensearch route=/install-and-configure/ --> for information.

Once you have installed OpenSearch and OpenSearch Dashboards, you can use Dashboards to connect your data sources to OpenSearch and then use Dashboards to manage data sources, create index patterns based on those data sources, run queries against a specific data source, and combine visualizations in one dashboard.

Configuration of the [YAML files](https://docs.opensearch.org/latest/install-and-configure/configuring-opensearch/#configuration-file) <!-- unresolved-cross-corpus-link: collection=opensearch route=/install-and-configure/configuring-opensearch/ --> and installation of the `dashboards-observability` and `opensearch-sql` plugins is necessary. For more information, see [OpenSearch plugins](https://docs.opensearch.org/latest/install-and-configure/plugins/) <!-- unresolved-cross-corpus-link: collection=opensearch route=/install-and-configure/plugins/ -->.

To securely store and encrypt data source connections in OpenSearch, you must add the following configuration to the `opensearch.yml` file on all the nodes:

`plugins.query.datasources.encryption.masterkey: "YOUR_GENERATED_MASTER_KEY_HERE"`

The key must be 16, 24, or 32 characters. You can use the following command to generate a 24-character key:

`openssl rand -hex 12`

Generating 12 bytes results in a hexadecimal string that is 12 * 2 = 24 characters.
{: .note}

## Permissions

To work with data sources in OpenSearch Dashboards, you must be assigned the correct cluster-level [data source permissions](https://docs.opensearch.org/latest/security/access-control/permissions#data-source-permissions) <!-- unresolved-cross-corpus-link: collection=opensearch route=/security/access-control/permissions/ -->.

## Types of data streams

To configure data sources through OpenSearch Dashboards, go to **Management** > **Dashboards Management** > **Data sources**. This flow can be used for OpenSearch data stream connections. See [Configuring and using multiple data sources](../multi-data-sources/index.md).

Alternatively, if you are running OpenSearch Dashboards 2.16 or later, go to **Management** > **Data sources**. This flow can be used to connect Amazon Simple Storage Service (Amazon S3) and Prometheus. See [Connecting Amazon S3 to OpenSearch](../s3-data-source/index.md) and [Connecting Prometheus to OpenSearch](../connect-prometheus/index.md) for more information.

## Next steps

- Learn about [managing index patterns](../index-patterns/index.md) through OpenSearch Dashboards.
- Learn about [indexing data using Index Management](../../im-dashboards/index.md) through OpenSearch Dashboards.
- Learn about how to connect [multiple data sources](../multi-data-sources/index.md).
- Learn about how to connect [OpenSearch and Amazon S3](../s3-data-source/index.md) and [OpenSearch and Prometheus](../connect-prometheus/index.md) using the OpenSearch Dashboards interface.
- Learn about the [Integrations](https://docs.opensearch.org/latest/integrations/index/) <!-- unresolved-cross-corpus-link: collection=opensearch route=/integrations/ --> plugin, which gives you the flexibility to use various data ingestion methods and connect data to OpenSearch Dashboards.
