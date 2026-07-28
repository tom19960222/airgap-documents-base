---
collection: ansible
version: "8"
title: "grafana.grafana.cloud_plugin module – Manage Grafana Cloud Plugins"
source_url: https://docs.ansible.com/projects/ansible/8/collections/grafana/grafana/cloud_plugin_module.html
fetched_at: 2026-07-28T02:33:51+00:00
---
# grafana.grafana.cloud_plugin module – Manage Grafana Cloud Plugins

> **Note:**
>
> This module is part of the [grafana.grafana collection](https://galaxy.ansible.com/ui/repo/published/grafana/grafana/) (version 2.2.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install grafana.grafana`.
> You need further requirements to be able to use this module,
> see [Requirements](cloud_plugin_module.md#ansible-collections-grafana-grafana-cloud-plugin-module-requirements) for details.
>
> To use it in a playbook, specify: `grafana.grafana.cloud_plugin`.

New in grafana.grafana 0.0.1

- [Synopsis](cloud_plugin_module.md#synopsis)
- [Requirements](cloud_plugin_module.md#requirements)
- [Parameters](cloud_plugin_module.md#parameters)
- [Notes](cloud_plugin_module.md#notes)
- [Examples](cloud_plugin_module.md#examples)
- [Return Values](cloud_plugin_module.md#return-values)

## [Synopsis](cloud_plugin_module.md#id1)

- Create, Update and delete Grafana Cloud stacks using Ansible.

## [Requirements](cloud_plugin_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests >= 1.0.0

## [Parameters](cloud_plugin_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cloud_api_key**  string / required | Cloud API Key to authenticate with Grafana Cloud. |
| **name**  string / required | Name of the plugin, e.g. grafana-github-datasource. |
| **stack_slug**  string / required | Name of the Grafana Cloud stack to which the plugin will be added. |
| **state**  string | State for the Grafana Cloud Plugin.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **version**  string | Version of the plugin to install.  **Default:** `"latest"` |

## [Notes](cloud_plugin_module.md#id4)

> **Note:**
>
> - Does not support `check_mode`.

## [Examples](cloud_plugin_module.md#id5)

```yaml+jinja
- name: Create/Update a plugin
  grafana.grafana.cloud_plugin:
    name: grafana-github-datasource
    version: 1.0.14
    stack_slug: "{{ stack_slug }}"
    cloud_api_key: "{{ grafana_cloud_api_key }}"
    state: present

- name: Delete a Grafana Cloud stack
  grafana.grafana.cloud_plugin:
    name: grafana-github-datasource
    stack_slug: "{{ stack_slug }}"
    cloud_api_key: "{{ grafana_cloud_api_key }}"
    state: absent
```

## [Return Values](cloud_plugin_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **current_version**  string | Current version of the plugin.  **Returned:** On success  **Sample:** `"1.0.14"` |
| **latest_version**  string | Latest version available for the plugin.  **Returned:** On success  **Sample:** `"1.0.15"` |
| **pluginId**  integer | Id for the Plugin.  **Returned:** On success  **Sample:** `663` |
| **pluginName**  string | Name of the plugin.  **Returned:** On success  **Sample:** `"GitHub"` |
| **pluginSlug**  string | Slug for the Plugin.  **Returned:** On success  **Sample:** `"grafana-github-datasource"` |

### Authors

- Ishan Jain (@ishanjainn)

### Collection links

- [Issue Tracker](https://github.com/grafana/grafana-ansible-collection/issues)
- [Repository (Sources)](https://github.com/grafana/grafana-ansible-collection)
