---
collection: ansible
version: "6"
title: "community.general.kibana_plugin module – Manage Kibana plugins"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/kibana_plugin_module.html
fetched_at: 2026-07-27T17:10:26+00:00
---
# community.general.kibana_plugin module – Manage Kibana plugins

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.kibana_plugin`.

- [Synopsis](kibana_plugin_module.md#synopsis)
- [Parameters](kibana_plugin_module.md#parameters)
- [Examples](kibana_plugin_module.md#examples)
- [Return Values](kibana_plugin_module.md#return-values)

## [Synopsis](kibana_plugin_module.md#id1)

- This module can be used to manage Kibana plugins.

## [Parameters](kibana_plugin_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **allow_root**  boolean  added in community.general 2.3.0 | Whether to allow `kibana` and `kibana-plugin` to be run as root. Passes the `--allow-root` flag to these commands.  Choices:   - `false` ← (default) - `true` |
| **force**  boolean | Delete and re-install the plugin. Can be useful for plugins update.  Choices:   - `false` ← (default) - `true` |
| **name**  string / required | Name of the plugin to install. |
| **plugin_bin**  path | Location of the Kibana binary.  Default: `"/opt/kibana/bin/kibana"` |
| **plugin_dir**  path | Your configured plugin directory specified in Kibana.  Default: `"/opt/kibana/installedPlugins/"` |
| **state**  string | Desired state of a plugin.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  string | Timeout setting: 30s, 1m, 1h etc.  Default: `"1m"` |
| **url**  string | Set exact URL to download the plugin from.  For local file, prefix its absolute path with <file://> |
| **version**  string | Version of the plugin to be installed.  If plugin exists with previous version, plugin will NOT be updated unless `force` is set to yes. |

## [Examples](kibana_plugin_module.md#id3)

```yaml+jinja
- name: Install Elasticsearch head plugin
  community.general.kibana_plugin:
    state: present
    name: elasticsearch/marvel

- name: Install specific version of a plugin
  community.general.kibana_plugin:
    state: present
    name: elasticsearch/marvel
    version: '2.3.3'

- name: Uninstall Elasticsearch head plugin
  community.general.kibana_plugin:
    state: absent
    name: elasticsearch/marvel
```

## [Return Values](kibana_plugin_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cmd**  string | the launched command during plugin management (install / remove)  Returned: success |
| **name**  string | the plugin name to install or remove  Returned: success |
| **state**  string | the state for the managed plugin  Returned: success |
| **stderr**  string | the command stderr  Returned: success |
| **stdout**  string | the command stdout  Returned: success |
| **timeout**  string | the timeout for plugin download  Returned: success |
| **url**  string | the url from where the plugin is installed from  Returned: success |

### Authors

- Thierno IB. BARRY (@barryib)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
