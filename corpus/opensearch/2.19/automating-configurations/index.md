---
collection: "opensearch"
version: "2.19"
title: "Automating configurations"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_automating-configurations/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_automating-configurations/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/automating-configurations/"
canonical_url: "https://docs.opensearch.org/latest/automating-configurations/index/"
canonical_route: "/automating-configurations/"
redirect_from: ["/automating-configurations/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: false
layout: "default"
nav_exclude: true
nav_order: 1
---
# Automating configurations
**Introduced 2.13**
{: .label .label-purple }

You can automate complex OpenSearch setup and preprocessing tasks by providing templates for common use cases. For example, automating machine learning (ML) setup tasks streamlines the use of OpenSearch ML offerings.

In OpenSearch 2.12, configuration automation is limited to ML tasks.
{: .info}

OpenSearch use case templates provide a compact description of the setup process in a JSON or YAML document. These templates describe automated workflow configurations for conversational chat or query generation, AI connectors, tools, agents, and other components that prepare OpenSearch as a backend for generative models. For custom template examples, see [Sample templates](https://github.com/opensearch-project/flow-framework/tree/main/sample-templates). For OpenSearch-provided templates, see [Workflow templates](workflow-templates/index.md).

## Key features

Workflow automation provides the following benefits:

* **Use case templates**: Get started with predefined templates that outline the setup process for your general use cases.
* **Customizable workflows**: Customize the workflow templates to your specific use case.
* **Setup automation**: Easily configure AI connectors, tools, agents, and other components in a single API call.

## Overview

**Templates** implement workflow automation in OpenSearch. You can provide these templates in JSON or YAML format. You can describe one or more templates with a sequence of steps required for a particular use case. Each template consists of the following elements:

* **Metadata**: A name, description, use case category, template version, and OpenSearch version compatibility range.
* **User input**: Parameters expected from the user that are common to all automation steps across all workflows, such as an index name.
* **Workflows**: One or more workflows containing the following elements:
    * **User input**: Parameters expected from the user that are specific to the steps in this workflow.
    * **Workflow Steps**: The workflow steps described as a directed acyclic graph (DAG):
        * ***Nodes*** describe steps of the process, which may be executed in parallel. For the syntax of workflow steps, see [Workflow steps](workflow-steps/index.md).
        * ***Edges*** sequence nodes to be executed after the previous step is complete and may use the output fields of previous steps. When a node includes a key in the `previous_node_input` map referring to a previous node’s workflow step, a corresponding edge is automatically added to the template during parsing and may be omitted for the sake of simplicity.

## Next steps

- For supported APIs, see [Workflow APIs](api/index.md).
- For the workflow step syntax, see [Workflow steps](workflow-steps/index.md).
- For a complete example, see [Workflow tutorial](workflow-tutorial/index.md).
- For configurable settings, see [Workflow settings](workflow-settings/index.md).
- For information about workflow access control, see [Workflow template security](workflow-security/index.md).
