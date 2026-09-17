---
collection: "opensearch"
version: "2.19"
title: "Create and request visualization reports"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_reporting/rep-cli-create.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_reporting/rep-cli-create.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/reporting/rep-cli-create/"
canonical_url: "https://docs.opensearch.org/latest/reporting/rep-cli-create/"
canonical_route: "/reporting/rep-cli-create/"
redirect_from: ["/dashboards/reporting-cli/rep-cli-create/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Reporting"
layout: "default"
nav_order: 15
parent: "Reporting using the CLI"
---
# Create and request visualization reports

First, you need to get the URL for the visualization that you want to download as an image file or PDF.

To generate a visualization report, you need to specify the Dashboards URL.

Open the visualization for which you want to generate a report, and select **Share >  Permalinks > Generate link as Shapshot > Short URL > Copy link**, as shown in the following image.

![Copy link](https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/dashboards/dash-url.png)

You will need to add the URL with the `-u` argument when you request the report in the CLI.

#### Example: Requesting a PNG file

The following command requests a report in PNG format with basic authentication and sends the report to an email address using Amazon SES:

```
opensearch-reporting-cli -u https://localhost:5601/app/dashboards#/view/7adfa750-4c81-11e8-b3d7-01146121b73d -a basic -c admin:Test@1234 -e ses -s <email address>  -r <email address> -f png
```

#### Example: Requesting a PDF file

The following command requests a PDF file and specifies the recipient's email address:

```
opensearch-reporting-cli -u https://localhost:5601/app/dashboards#/view/7adfa750-4c81-11e8-b3d7-01146121b73d -a basic -c admin:Test@1234 -e ses -s <email address> -r <email address> -f pdf
```

Upon success, the file will be sent to the specified email address. The following image shows an example PDF report.

![PDF example](https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/dashboards/cli-pdf-report.png)

#### Example: Requesting a CSV file

The following command generates a report that contains all table content in CSV format and sends the report to an email address using Amazon SES transport:

```
opensearch-reporting-cli -u https://localhost:5601/app/dashboards#/view/7adfa750-4c81-11e8-b3d7-01146121b73d -f csv -a basic -c admin:Test@1234 -e ses -s <email address> -r <email address>
```

Upon success, the email will be sent to the specified email address with the CSV file attached.
