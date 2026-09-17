---
collection: "opensearch-dashboards"
version: "2.19"
title: "Getting started with workspaces"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_dashboards/workspace/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_dashboards/workspace/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/dashboards/workspace/"
canonical_url: "https://docs.opensearch.org/latest/dashboards/workspace/index/"
canonical_route: "/dashboards/workspace/"
redirect_from: ["/dashboards/workspace/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.1"
chart_version: ""
layout: "default"
nav_order: 0
parent: "Workspace for OpenSearch Dashboards"
---
# Getting started with workspaces
Introduced 2.18
{: .label .label-purple }

OpenSearch Dashboards 2.18 introduces an enhanced home page that provides a comprehensive view of all your workspaces.

The new home page includes the following features:

1. A **Create workspace** button for [OpenSearch Dashboard admins](workspace-acl/index.md#configuring-dashboard-administrators) to navigate to the [create workspace](create-workspace/index.md) page.
2. Workspace access time information and a link to the workspace overview page.
3. A use case information icon that displays information about the workspace's purpose.
4. A **View all workspaces** button that navigates to the [workspace management](manage-workspace/index.md#navigating-the-workspaces-list) page.
5. Links to the latest OpenSearch documentation through the **Learn more from documentation** button and to [OpenSearch Playground](https://playground.opensearch.org/app/home#/) through the **Explore live demo environment at playground.opensearch.org** button.

The navigation logic ensures a seamless user experience by directing you to the appropriate page based on your workspace access level:

- If a you have a default workspace configured, you are directed to the workspace overview page.
- If a you have only one workspace, you are directed to the overview page of that workspace.
- If a you have multiple workspaces, you are directed to the new home page.
- If a you have no workspaces, you are directed to the new home page.
