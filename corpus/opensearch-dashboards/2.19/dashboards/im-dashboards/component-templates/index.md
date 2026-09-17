---
collection: "opensearch-dashboards"
version: "2.19"
title: "Component templates"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_dashboards/im-dashboards/component-templates.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_dashboards/im-dashboards/component-templates.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/dashboards/im-dashboards/component-templates/"
canonical_url: "https://docs.opensearch.org/latest/dashboards/im-dashboards/component-templates/"
canonical_route: "/dashboards/im-dashboards/component-templates/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.1"
chart_version: ""
layout: "default"
nav_order: 50
parent: "Index Management"
---
# Component templates
Introduced 2.7
{: .label .label-purple }

Component templates allow you to create a single index pattern that matches multiple indexes. This pattern can include wildcards or regular expressions, enabling you to apply the same setting or mapping to multiple indexes simultaneously.

Using them with [index templates](https://docs.opensearch.org/latest/im-plugin/index-templates/) <!-- unresolved-cross-corpus-link: collection=opensearch route=/im-plugin/index-templates/ --> can provide a powerful tool for managing large volumes of data. You can create an index template that defines the basic structure and settings of your indexes and then use the component templates to apply the settings to all indexes that match a specific pattern or set of criteria.

You can create component templates using the Index Management UI. The UI maximizes ease of use for common indexing and data stream administrative operations such as create, read, update, delete (CRUD) and mapping indexes; CRUD and mapping aliases; reindexing; and open/close, shrink, and split indexes, along with the monitoring of actions and logging of audit records.

The following GIF demonstrates creating a component template.

![Component template demo](https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/admin-ui-index/component.gif)

## Prerequisites

This tutorial is intended for admin users who [manage OpenSearch clusters](https://docs.opensearch.org/latest/tuning-your-cluster/cluster/) <!-- unresolved-cross-corpus-link: collection=opensearch route=/tuning-your-cluster/cluster/ --> and are familiar with [index management in OpenSearch Dashboards](../index.md).

## Key terms

It's helpful to understand the following terms before starting this tutorial:

- *Component template* refers to a reusable building block with settings, mappings, and aliases that can be attached to an index template.
- *Index template* refers to a predefined structure used to organize and store data in a database or search index.

## Creating component templates using the Index Management UI

You can use predefined OpenSearch Dashboards component templates or customize your own, either by creating original templates or by modifying existing templates. Predefined component templates include preconfigured charts, tables, and graphs and are a good starting point for users who are new to OpenSearch Dashboards. Alternatively, customized template components provide you with options for tailoring reports and visualizations that meet your specific requirements and preferences.

To create template components using the UI, follow these steps:

1. On the OpenSearch Dashboards main page, select **Index Management** in the navigation menu.
1. In the Index Management window, select **Templates** > **Component templates**.
1. Select **Create** and then define the component template settings.
1. To configure aliases, settings, and mappings, toggle **Use configuration**, as shown in the following image.

    ![Component template use configuration](https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/admin-ui-index/component_use_config.png)

1. Enter details in the aliases, settings, and mappings fields.
1. Select **Create component template**.

When you create component templates, those templates apply only to new index templates that you create and not to existing index templates.
{: .note }

## Associating component templates with index templates

To associate a component template with an index template, follow these steps:

1. In the **Index Management** navigation menu, select **Templates**.
1. In the Templates window, select **Create template**.
1. Select **Component template** as the method for defining your template.
1. In the **Component template** pane, select **Associate component template**, as shown in the following image.

    ![Component template associate configuration](https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/admin-ui-index/associate_component.png)

1. In the **Associate component template** pop-up window, select the component templates that you want to associate with your index template.
1. Select **Associate**.
1. Select **Preview template** to view the template settings.
1. Select **Create template**.
