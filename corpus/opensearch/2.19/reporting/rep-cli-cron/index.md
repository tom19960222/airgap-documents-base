---
collection: "opensearch"
version: "2.19"
title: "Schedule reports with the cron utility"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_reporting/rep-cli-cron.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_reporting/rep-cli-cron.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/reporting/rep-cli-cron/"
canonical_url: "https://docs.opensearch.org/latest/reporting/rep-cli-cron/"
canonical_route: "/reporting/rep-cli-cron/"
redirect_from: ["/dashboards/reporting-cli/rep-cli-cron/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Reporting"
layout: "default"
nav_order: 20
parent: "Reporting using the CLI"
---
# Schedule reports with the cron utility

You can use the cron command-line utility to initiate a report request with the Reporting CLI that runs periodically at any date or time interval. Follow the cron expression syntax to specify the date and time that precedes the command that you want to initiate.

To learn about the cron expression syntax, see [Cron expression reference](../../observing-your-data/alerting/cron/index.md). To get help with cron, open the man page by running the following command:

```
man cron
```

### Prerequisites

- You need a machine with cron installed.
- You need to install the Reporting CLI. See [Downloading and installing the Reporting CLI tool](../rep-cli-install/index.md)

## Specifying the report details

Open the crontab editor by running the following command:

```
crontab -e
```
In the crontab editor, enter the report request. The following example shows a cron report that runs every day at 8:00 AM:

```
0 8 * * * opensearch-reporting-cli -u https://playground.opensearch.org/app/dashboards#/view/084aed50-6f48-11ed-a3d5-1ddbf0afc873 -e ses -s <sender_email> -r <recipient_email>
```
