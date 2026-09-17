---
collection: "opensearch"
version: "2.19"
title: "Setting up Security Analytics"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_security-analytics/sec-analytics-config/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_security-analytics/sec-analytics-config/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/security-analytics/sec-analytics-config/"
canonical_url: "https://docs.opensearch.org/latest/security-analytics/sec-analytics-config/index/"
canonical_route: "/security-analytics/sec-analytics-config/"
redirect_from: ["/security-analytics/sec-analytics-config/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_order: 10
---
# Setting up Security Analytics

Before Security Analytics can begin generating findings and sending alerts, administrators must create detectors and make log data available to the system. Once detectors are able to generate findings, you can fine-tune your alerts to focus on specific areas of interest. The following steps outline the basic workflow for setting up components in Security Analytics.

1. Create threat detectors and alerts, and ingest log data. See [Creating detectors](detectors-config/index.md) for more information.
1. Consider [creating correlation rules](correlation-config/index.md) to identify connections between events and possible threats occurring in different logs throughout your system.
1. Inspect findings generated from detector output and create any additional alerts.
1. If desired, create custom rules to better focus detectors on high-priority concerns in your system. See [Creating detection rules](../usage/rules/index.md#creating-detection-rules) for more information.

## Navigate to Security Analytics

1. To get started, select the top menu on the Dashboards home page and then select **Security Analytics**. The Overview page for Security Analytics is displayed.
1. From the options on the left side of the page, select **Detectors** to begin creating a detector.

<img src="https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/Security/secanalytics-det-nav.png" alt="Navigating to create a detector page" width="70%">
