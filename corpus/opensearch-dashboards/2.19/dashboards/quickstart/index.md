---
collection: "opensearch-dashboards"
version: "2.19"
title: "OpenSearch Dashboards quickstart guide"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_dashboards/quickstart.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_dashboards/quickstart.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/dashboards/quickstart/"
canonical_url: "https://docs.opensearch.org/latest/dashboards/getting-started/index/"
canonical_route: "/dashboards/getting-started/"
redirect_from: ["/dashboards/get-started/quickstart-dashboards/","/dashboards/quickstart-dashboards/","/dashboards/browser-compatibility/","/dashboards/getting-started/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.1"
chart_version: ""
has_children: false
layout: "default"
nav_order: 2
---
# OpenSearch Dashboards quickstart guide

This quickstart guide provides tutorials on using OpenSearch Dashboards applications and tools. You can use these tutorials, either in your own environment or on [OpenSearch Playground](https://playground.opensearch.org/app/home#/), to learn the following fundamental concepts:

- **Adding sample data:** Use preloaded visualizations, dashboards, and other tools to explore OpenSearch Dashboards before adding your own data.
- **Using the Discover application:** Analyze your data to gain insights.
- **Using the Dashboards application:** Create and store data visualizations.
- **Customizing the appearance theme:** Quickly change the OpenSearch Dashboards appearance theme from the home page.

The OpenSearch Dashboards default view is shown in the following image.

<img src="https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/dashboards/home-page-nav.png" alt="OpenSearch Dashboards interface default view" width="700">

## Docking the navigation menu

To dock or undock the navigation menu, select the <img src="https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/icons/menu-icon.png" class="inline-icon" alt="menu icon"/> icon on the upper-left toolbar and then select **Dock navigation** or **Undock navigation** on the lower left of the menu. A docked navigation menu is shown in the preceding image.

Before continuing with the following tutorials, make sure you've installed OpenSearch and OpenSearch Dashboards. For information about installation and configuration, see [Install and configure OpenSearch](https://docs.opensearch.org/latest/install-and-configure/install-opensearch/index/) <!-- unresolved-cross-corpus-link: collection=opensearch route=/install-and-configure/install-opensearch/ --> and [Install and configure OpenSearch Dashboards](https://docs.opensearch.org/latest/install-and-configure/install-dashboards/index/) <!-- unresolved-cross-corpus-link: collection=opensearch route=/install-and-configure/install-dashboards/ -->.
{: .note}

## Adding sample data

The following tutorials use the [**Sample flight data**](https://playground.opensearch.org/app/home#/tutorial_directory) dataset.
{: .note}

To add sample data, follow these steps:

1. On the OpenSearch Dashboards **Home** page, choose **Add sample data**. Alternatively, choose **Add data** on the upper-right toolbar.
2. On the **Add sample data** page, choose the dataset(s) you want to add to Dashboards. The following image shows the available sample datasets.

<img src="https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/dashboards/add-sample.png" alt="Adding sample data window" width="700">

## Using the Discover application

With [**Discover**](../discover/index-discover/index.md), you can:

- Choose data for analysis, set a time range for that data, search it using [Dashboards Query Language (DQL)](../dql/index.md), and filter the results.
- Analyze your data by querying and filtering, viewing results in a table, and examining documents.
- Create histograms to display the distribution of your data.

Follow these steps to use the Discover tool:

1. From the OpenSearch Dashboards navigation menu, choose **Discover**.
2. On the **Discover** page, choose the index pattern `opensearch_dashboards_sample_data_flights` from the dropdown menu on the upper left.
3. Select the <img src="https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/icons/calendar-oui.png" class="inline-icon" alt="calendar icon"/> icon to change the [time filter](../discover/time-filter/index.md) from the default of **Last 15 minutes** to **Last 7 days**.
4. In the DQL search bar, enter `FlightDelay:true AND DestCountry: US AND FlightDelayMin >= 60` and select **Update**. Results are shown for US-bound flights delayed by 60 minutes or more.
5. Filter data by selecting **Add filter** from the DQL search bar and then selecting a **Field**, **Operator**, and **Value** from the dropdown lists in the **Edit Filter** pop-up window. For example, select `FlightDelayType`, **is**, and **Weather Delay**.

The resulting view is shown in the following image.

<img src="https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/dashboards/opensearch-dashboards-discover.png" alt="Discover output of steps 1 through 6" width="700">

## Using the Dashboards application

With [**Dashboards**](../dashboard/index.md), you can:

- Display data in a single view.
- Build dynamic dashboards.
- Create and share reports.
- Embed analytics to differentiate your applications.

The **Dashboards** application creates and stores visualizations generated from your data. Follow these steps to use the application:

1. On the OpenSearch Dashboards **Home** page, choose **Dashboards**. A list of dashboards generated from the sample data appears.
2. In the search toolbar, search for and select **[Flights] Global Flight Dashboard**. You'll see a dashboard preloaded with visualizations, including charts, maps, and data tables.
3. To add other panels to the dashboard, select the **Edit** button and then choose **Add** from the toolbar. The **Add panels** window opens.
4. In the search toolbar in the **Add panels** window, search for and select the existing panel **[Flights] Delay Buckets**. A pop-up message confirms that you've added the panel.
5. Select close `x` to exit the **Add panels** window.
6. The newly added panel is now displayed as the last panel on the dashboard.

The resulting view is shown in the following image.

<img src="https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/dashboards/add-dash-panel.png" alt="Add panel view" width="700">

For information about using a specific data visualization type, such as VisBuilder, go to [Building data visualizations](../visualize/viz-index/index.md). For information about using dashboards and visualizations in **Observability**, go to [Observability](https://docs.opensearch.org/latest/observing-your-data/) <!-- unresolved-cross-corpus-link: collection=opensearch route=/observing-your-data/ -->.
{: .note}

### Interacting with data using dashboards

Interactive dashboards allow you to analyze data in more depth and filter it in several ways. With **Dashboards**, you can use dashboard-level filters to directly interact with data.

Using the **[Flights] Global Flight Dashboard** dashboard, follow these steps to further analyze and filter the sample flight data:

1. On the **[Flights] Airline Carrier** panel, choose **OpenSearch-Air**. The dashboard updates automatically, adding the filter `Carrier: OpenSearch-Air` on the upper-left filter bar. The following GIF illustrates this step.
2. Choose **Save** to save the dashboard.

![Filter data demo](https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/dashboards/airline-carrier.gif)

Alternatively, you can use the dashboard toolbar to apply filters by following these steps:

1. In the dashboard toolbar, choose **Add filter**.
2. From the **Field**, **Operator**, and **Value** dropdown lists, choose **Carrier**, **is**, and **OpenSearch-Air**, respectively.
3. Choose **Save**. The dashboard updates automatically.

The resulting view is shown in the following image.

<img src="https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/dashboards/filter-data-dash.png" alt="Dashboards tutorial panel view" width="700">

## Customizing the appearance theme
Introduced 2.14
{: .label .label-purple }

Light mode is the default OpenSearch Dashboards appearance theme. You can customize the appearance theme to suit your preferences. The available options include light mode, dark mode, and your browser's settings.

### Enabling the appearance theme setting

The appearance theme setting is enabled or disabled through **Advanced Settings** and requires admin permissions.

### Changing the appearance theme settings

Admins can change the appearance theme for all users of their OpenSearch Dashboards instance through **Advanced Settings**:

1. Navigate to **Management** > **Dashboards Management** > **Advanced Settings**.
2. Scroll to the **Appearance** section and toggle `theme:darkMode` on or off.
3. Select the **Save changes** button and then the **Reload** button. The updated theme is applied immediately.

<img src="https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/dashboards/dark-mode.png" alt="Dark mode view" width="700">

## Next steps

- Go to [Building data visualizations](../visualize/viz-index/index.md) to learn more about data visualizations.
- Go to [Creating dashboards](index.md) to learn more about creating dashboards.
- Go to [Analyzing data](../discover/index-discover/index.md) to learn more about using Dashboards to analyze data.
- Go to [Ingest APIs](https://docs.opensearch.org/latest/api-reference/ingest-apis/index/) <!-- unresolved-cross-corpus-link: collection=opensearch route=/api-reference/ingest-apis/ --> and [Ingest pipelines](https://docs.opensearch.org/latest/ingest-pipelines/) <!-- unresolved-cross-corpus-link: collection=opensearch route=/ingest-pipelines/ --> to learn more about data ingestion using OpenSearch.
