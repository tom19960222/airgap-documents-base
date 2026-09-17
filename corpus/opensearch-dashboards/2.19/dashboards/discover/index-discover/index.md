---
collection: "opensearch-dashboards"
version: "2.19"
title: "Analyzing data"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_dashboards/discover/index-discover.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_dashboards/discover/index-discover.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/dashboards/discover/index-discover/"
canonical_url: "https://docs.opensearch.org/latest/dashboards/discover/index-discover/"
canonical_route: "/dashboards/discover/index-discover/"
redirect_from: ["/dashboards/discover/index-discover/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.1"
chart_version: ""
has_children: true
layout: "default"
nav_order: 20
---
# Analyzing data

To analyze your data in OpenSearch and visualize key metrics, you can use the **Discover** application in OpenSearch Dashboards. An example of data analysis in **Discover** is shown in the following image.

<img src="https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/dashboards/discover.png" alt="A Discover default page" width="700">

## Getting started

In this tutorial, you'll learn about using **Discover** to:

- Add data.
- Interpret and visualize data.
- Share data findings.
- Set alerts.

Before getting started, make sure you:

- Install [OpenSearch Dashboards](https://opensearch.org/downloads.html).
- Add sample data or import your own data into OpenSearch. Go to the [OpenSearch Dashboards quickstart guide](../../quickstart/index.md) to learn about adding sample datasets. Go to [Managing indexes](https://docs.opensearch.org/latest/im-plugin/index/) <!-- unresolved-cross-corpus-link: collection=opensearch route=/im-plugin/ --> to learn about importing your own data.
- Have a foundational understanding of [OpenSearch documents and indexes](https://docs.opensearch.org/latest/im-plugin/index/) <!-- unresolved-cross-corpus-link: collection=opensearch route=/im-plugin/ -->.

## Defining the search

To define a search, follow these steps:

1. On the OpenSearch Dashboards navigation menu, select **Discover**.
2. Choose the data you want to work with. In this case, choose `opensearch_dashboards_sample_data_flights` from the upper-left dropdown menu.
3. Select the <img src="https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/icons/calendar-oui.png" class="inline-icon" alt="calendar icon"/> icon to change the time range of your search and then select **Refresh**.

The resulting view is shown in the following image.

<img src="https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/dashboards/define-search.png" alt="Discover interface showing search of flight sample data for Last 7 days"  width="700">

## Analyzing document tables

In OpenSearch, a document table stores unstructured data. In a document table, each row represents a single document, and each column contains document attributes.

To examine document attributes, follow these steps:

1. From the data table's left column, choose the <img src="https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/icons/inspect-icon.png" class="inline-icon" alt="inspect icon"/> icon to open the **Document Details** window. Select the <img src="https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/icons/minimize-icon.png" class="inline-icon" alt="minimize icon"/> icon to close the **Document Details** window.
2. Examine the metadata. You can switch between the **Table** and **JSON** tabs to view the data in your preferred format.
3. Select **View surrounding documents** to view data for other log entries either preceding or following your current document or select **View single document** to view a particular log entry.

The resulting view is shown in the following image.

<img src="https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/dashboards/doc-details.png" alt="Document attributes"  width="700">

To add or delete fields in a document table, follow these steps:

1. View the data fields listed under **Available fields** and select the <img src="https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/icons/plus-icon.png" class="inline-icon" alt="plus icon"/> icon to add the desired fields to the document table. The field will be automatically added to both **Selected fields** and the document table. For this example, choose the fields `Carrier`, `AvgTicketPrice`, and `Dest`.
2. Select **Sort fields** > **Pick fields to sort by**. Drag and drop the chosen fields in the desired sort order.

The resulting view is shown in the following image.

<img src="https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/dashboards/add-data-fields.png" alt="Adding and deleting data fields"  width="700">

## Searching data

You can use the search toolbar to enter a [DQL](../../dql/index.md) or [query string](https://docs.opensearch.org/latest/query-dsl/full-text/query-string/) <!-- unresolved-cross-corpus-link: collection=opensearch route=/query-dsl/full-text/query-string/ --> query. The search toolbar is best for basic queries; for full query and filter capability, use [query domain-specific language (DSL)](https://docs.opensearch.org/latest/query-dsl/index/) <!-- unresolved-cross-corpus-link: collection=opensearch route=/query-dsl/ --> in the [Dev Tools console](../../dev-tools/index-dev/index.md).

For more information, see [Discover and Dashboard search toolbar](../../index.md#discover-and-dashboard-search-bar).

## Filtering data

Filters allow you to narrow the results of a query by specifying certain criteria. You can filter by field, value, or range. The **Add filter** pop-up suggests the available fields and operators.

To filter your data, follow these steps:

1. Under the DQL search bar, choose **Add filter**.
2. Select the desired options from the **Field**, **Operator**, and **Value** dropdown lists. For example, select `Cancelled`, `is`, and `true`.
3. Choose **Save**.
4. To remove a filter, choose the <img src="https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/icons/cross-icon.png" class="inline-icon" alt="cross icon"/> icon to the right of the filter name.

The resulting view is shown in the following image.

<img src="https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/dashboards/discover-filter.png" alt="Visualize data findings interface" width="700"/>

## Saving a search

To save your search, including the query text, filters, and current data view, follow these steps:

1. Select **Save** on the upper-right toolbar.
2. Add a title, and then choose **Save**.
3. Select **Open** on the upper-right toolbar to access your saved searches.

## Visualizing data findings

To visualize your data findings, follow these steps:

1. Select the <img src="https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/icons/inspect-icon.png" class="inline-icon" alt="inspect icon"/> icon to the right of the field you want to visualize.

   The resulting view is shown in the following image.

   <img src="https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/dashboards/visualize-discover.png" alt="Visualize data findings interface" width="700"/>

2. Select the **Visualize** button. When the **Visualize** application is launched, a visualization appears.

   The resulting view is shown in the following image.

   <img src="https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/dashboards/visualization-flight.png" alt="Data visualization of flight sample data field destination" width="700"/>

## Setting alerts

Set alerts to notify you when your data exceeds your specified thresholds. Go to [Alerting dashboards and visualizations](https://docs.opensearch.org/latest/observing-your-data/alerting/dashboards-alerting/) <!-- unresolved-cross-corpus-link: collection=opensearch route=/observing-your-data/alerting/dashboards-alerting/ --> to learn about creating and managing alerts.
