---
collection: "opensearch-dashboards"
version: "2.19"
title: "Query and visualize Amazon S3 data"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_dashboards/management/query-data-source.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_dashboards/management/query-data-source.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/dashboards/management/query-data-source/"
canonical_url: "https://docs.opensearch.org/latest/dashboards/management/query-data-source/"
canonical_route: "/dashboards/management/query-data-source/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.1"
chart_version: ""
grand_parent: "Data sources"
has_children: false
layout: "default"
nav_order: 10
parent: "Connecting Amazon S3 to OpenSearch"
---
# Query and visualize Amazon S3 data
Introduced 2.11
{: .label .label-purple }

This tutorial guides you through using the **Query data** use case for querying and visualizing your Amazon Simple Storage Service (Amazon S3) data using OpenSearch Dashboards.

## Prerequisites

You must be using the `opensearch-security` plugin and have the appropriate role permissions. Contact your IT administrator to assign you the necessary permissions.

## Get started with querying

To get started, follow these steps:

1. On the **Manage data sources** page, select your data source from the list.
2. On the data source's detail page, select the **Query data** card. This option takes you to the **Observability** > **Logs** page.
3. Select the **Event Explorer** button. This option creates and saves frequently searched queries and visualizations using [Piped Processing Language (PPL)](https://docs.opensearch.org/latest/search-plugins/sql/ppl/index/) <!-- unresolved-cross-corpus-link: collection=opensearch route=/search-plugins/sql/ppl/ --> or [SQL](https://docs.opensearch.org/latest/search-plugins/sql/index/) <!-- unresolved-cross-corpus-link: collection=opensearch route=/search-plugins/sql/ -->, which connects to Spark SQL.
4. Select the Amazon S3 data source from the dropdown menu in the upper-left corner.
5. Enter the query in the **Enter PPL query** field. Note that the default language is SQL. To change the language, select PPL from the dropdown menu.
6. Select the **Search** button. The **Query Processing** message is shown, confirming that your query is being processed.
7. View the results, which are listed in a table on the **Events** tab. On this page, details such as available fields, source, and time are shown in a table format.
8. (Optional) Create data visualizations.

## Create visualizations of your Amazon S3 data

To create visualizations, follow these steps:

1. On the **Explorer** page, select the **Visualizations** tab.
2. Select **Index data to visualize**. This option currently only creates [acceleration indexes](../accelerate-external-data/index.md), which give you views of the data visualizations from the **Visualizations** tab. To create a visualization of your Amazon S3 data, go to **Discover**. See the [Discover documentation](../../discover/index-discover/index.md) for information and a tutorial.

## Use Query Workbench with your Amazon S3 data source

[Query Workbench](../../query-workbench/index.md) runs on-demand SQL queries, translates SQL into its REST equivalent, and views and saves results as text, JSON, JDBC, or CSV.

To use Query Workbench with your Amazon S3 data, follow these steps:

1. From the OpenSearch Dashboards main menu, select **OpenSearch Plugins** > **Query Workbench**.
2. From the **Data Sources** dropdown menu in the upper-left corner, choose your Amazon S3 data source. Your data begins loading the databases that are part of your data source.
3. View the databases listed in the left-side navigation menu and select a database to view its details. Any information about acceleration indexes is listed under **Acceleration index destination**.
4. Choose the **Describe Index** button to learn more about how data is stored in that particular index.
5. Choose the **Drop index** button to delete and clear both the OpenSearch index and the Amazon S3 Spark job that refreshes the data.
6. Enter your SQL query and select **Run**.

## Next steps

- Learn about [accelerating the query performance of your external data sources](../accelerate-external-data/index.md).
