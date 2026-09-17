---
collection: "opensearch"
version: "2.19"
title: "Download and install the Reporting CLI tool"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_reporting/rep-cli-install.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_reporting/rep-cli-install.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/reporting/rep-cli-install/"
canonical_url: "https://docs.opensearch.org/latest/reporting/rep-cli-install/"
canonical_route: "/reporting/rep-cli-install/"
redirect_from: ["/dashboards/reporting-cli/rep-cli-install/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Reporting"
layout: "default"
nav_order: 10
parent: "Reporting using the CLI"
---
# Download and install the Reporting CLI tool

You can download and install the Reporting CLI tool from either the npm software registry or the OpenSearch.org [Artifacts](https://opensearch.org/artifacts) hub. Refer to the following sections for instructions.

To learn more about the npm software registry, see the [npm](https://docs.npmjs.com/about-npm) documentation.

## Downloading and installing the Reporting CLI from npm

To download and install the Reporting CLI from npm, run the following command to initiate installation:

```
npm i @opensearch-project/reporting-cli
```

## Downloading and installing the Reporting CLI from OpenSearch.org

You can download the `opensearch-reporting-cli` tool from the OpenSearch.org [Artifacts](https://artifacts.opensearch.org/reporting-cli/opensearch-reporting-cli-1.0.0.tgz) hub.

Next, run the following command to install the .tar archive:

```
npm install -g opensearch-reporting-cli-1.0.0.tgz
```

To provide better security for artifacts, we recommend that you verify signatures by downloading the [Reporting CLI signature file](https://artifacts.opensearch.org/reporting-cli/opensearch-reporting-cli-1.0.0.tgz.sig).
{: .important }

To learn more about verifying signatures, see [How to verify signatures for downloadable artifacts](https://opensearch.org/verify-signatures.html).
