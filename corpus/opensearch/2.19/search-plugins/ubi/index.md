---
collection: "opensearch"
version: "2.19"
title: "User Behavior Insights"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_search-plugins/ubi/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_search-plugins/ubi/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/search-plugins/ubi/"
canonical_url: "https://docs.opensearch.org/latest/search-plugins/ubi/index/"
canonical_route: "/search-plugins/ubi/"
redirect_from: ["/search-plugins/ubi/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
layout: "default"
nav_order: 90
---
# User Behavior Insights

**Introduced 2.15**
{: .label .label-purple }

**References UBI Specification 1.0.0**
{: .label .label-purple }

User Behavior Insights (UBI) is a plugin that captures client-side events and queries for the purposes of improving search relevance and the user experience.
It is a causal system, linking a user's query to all of their subsequent interactions with your application until they perform another search.

UBI includes the following elements:
* A machine-readable [schema](https://github.com/o19s/ubi) that faciliates interoperablity of the UBI specification.
* An OpenSearch [plugin](https://github.com/opensearch-project/user-behavior-insights) that facilitates the storage of client-side events and queries.
* A client-side JavaScript [example reference implementation](data-structures/index.md) that shows how to capture events and send them to the OpenSearch UBI plugin.

<!-- vale off -->

The UBI documentation is organized into two categories: *Explanation and reference* and *Tutorials and how-to guides*:

*Explanation and reference*

| Link | Description |
| :--------- | :------- |
| [UBI Request/Response Specification](https://github.com/o19s/ubi/) | The industry-standard schema for UBI requests and responses. The current version references UBI Specification 1.0.0.  |
| [UBI index schema](schemas/index.md) | Documentation on the individual OpenSearch query and event stores. |

*Tutorials and how-to guides*

| Link | Description |
| :--------- | :------- |
| [UBI plugin](https://github.com/opensearch-project/user-behavior-insights) | How to install and use the UBI plugin. |
| [UBI client data structures](data-structures/index.md)  | Sample JavaScript structures for populating the event store. |
| [Example UBI query DSL queries](dsl-queries/index.md)  | How to write queries for UBI data in OpenSearch query DSL. |
| [Example UBI SQL queries](sql-queries/index.md)  | How to write analytic queries for UBI data in SQL. |
| [UBI dashboard tutorial](ubi-dashboard-tutorial/index.md) | How to build a dashboard containing UBI data. |
| [Chorus Opensearch Edition](https://github.com/o19s/chorus-opensearch-edition/?tab=readme-ov-file#structured-learning-using-chorus-opensearch-edition) katas | A series of structured tutorials that teach you how to use UBI with OpenSearch through a demo e-commerce store. |

<!-- vale on -->
The documentation categories were adapted using concepts based on [Diátaxis](https://diataxis.fr/).
{: .tip }
