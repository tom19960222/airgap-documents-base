---
collection: ansible
version: "8"
title: "community.grafana.grafana_plugin module – Manage Grafana plugins via grafana-cli"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/grafana/grafana_plugin_module.html
fetched_at: 2026-07-28T01:53:17+00:00
---
# community.grafana.grafana_plugin module – Manage Grafana plugins via grafana-cli

> **Note:**
>
> This module is part of the [community.grafana collection](https://galaxy.ansible.com/ui/repo/published/community/grafana/) (version 1.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.grafana`.
>
> To use it in a playbook, specify: `community.grafana.grafana_plugin`.

- [Synopsis](grafana_plugin_module.md#synopsis)
- [Parameters](grafana_plugin_module.md#parameters)
- [Examples](grafana_plugin_module.md#examples)
- [Return Values](grafana_plugin_module.md#return-values)

## [Synopsis](grafana_plugin_module.md#id1)

- Install and remove Grafana plugins.
- See <https://grafana.com/docs/plugins/installation/> for upstream documentation.

## [Parameters](grafana_plugin_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **grafana_plugin_url**  string | Full URL to the plugin zip file instead of downloading the file from <https://grafana.com/api/plugins>.  Requires grafana 4.6.x or later. |
| **grafana_plugins_dir**  string | Directory where the Grafana plugin will be installed.  If omitted, defaults to `/var/lib/grafana/plugins`. |
| **grafana_repo**  string | URL to the Grafana plugin repository.  If omitted, grafana-cli will use the default value: <https://grafana.com/api/plugins>. |
| **name**  string / required | Name of the plugin. |
| **state**  string | Whether the plugin should be installed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | Boolean variable to include –insecure while installing pluging  **Choices:**   - `false` ← (default) - `true` |
| **version**  string | Version of the plugin to install.  Defaults to `latest`. |

## [Examples](grafana_plugin_module.md#id3)

```yaml+jinja
---
- name: Install/update Grafana piechart panel plugin
  community.grafana.grafana_plugin:
    name: grafana-piechart-panel
    version: latest
    state: present
```

## [Return Values](grafana_plugin_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **version**  string | version of the installed/removed/updated plugin.  **Returned:** always |

### Authors

- Thierry Sallé (@seuf)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.grafana/issues)
- [Homepage](https://github.com/ansible-collections/grafana)
- [Repository (Sources)](https://github.com/ansible-collections/community.grafana.git)
