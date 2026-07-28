---
collection: ansible
version: "6"
title: "community.general.elasticsearch_plugin module – Manage Elasticsearch plugins"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/elasticsearch_plugin_module.html
fetched_at: 2026-07-27T17:08:51+00:00
---
# community.general.elasticsearch_plugin module – Manage Elasticsearch plugins

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
> To use it in a playbook, specify: `community.general.elasticsearch_plugin`.

- [Synopsis](elasticsearch_plugin_module.md#synopsis)
- [Parameters](elasticsearch_plugin_module.md#parameters)
- [Examples](elasticsearch_plugin_module.md#examples)

## [Synopsis](elasticsearch_plugin_module.md#id1)

- Manages Elasticsearch plugins.

## [Parameters](elasticsearch_plugin_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **force**  boolean | Force batch mode when installing plugins. This is only necessary if a plugin requires additional permissions and console detection fails.  Choices:   - `false` ← (default) - `true` |
| **name**  string / required | Name of the plugin to install. |
| **plugin_bin**  path | Location of the plugin binary. If this file is not found, the default plugin binaries will be used.  The default changed in Ansible 2.4 to None. |
| **plugin_dir**  path | Your configured plugin directory specified in Elasticsearch  Default: `"/usr/share/elasticsearch/plugins/"` |
| **proxy_host**  string | Proxy host to use during plugin installation |
| **proxy_port**  string | Proxy port to use during plugin installation |
| **src**  string | Optionally set the source location to retrieve the plugin from. This can be a <file://> URL to install from a local file, or a remote URL. If this is not set, the plugin location is just based on the name.  The name parameter must match the descriptor in the plugin ZIP specified.  Is only used if the state would change, which is solely checked based on the name parameter. If, for example, the plugin is already installed, changing this has no effect.  For ES 1.x use url. |
| **state**  string | Desired state of a plugin.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  string | Timeout setting: 30s, 1m, 1h…  Only valid for Elasticsearch < 5.0. This option is ignored for Elasticsearch > 5.0.  Default: `"1m"` |
| **url**  string | Set exact URL to download the plugin from (Only works for ES 1.x).  For ES 2.x and higher, use src. |
| **version**  string | Version of the plugin to be installed. If plugin exists with previous version, it will NOT be updated |

## [Examples](elasticsearch_plugin_module.md#id3)

```yaml+jinja
- name: Install Elasticsearch Head plugin in Elasticsearch 2.x
  community.general.elasticsearch_plugin:
    name: mobz/elasticsearch-head
    state: present

- name: Install a specific version of Elasticsearch Head in Elasticsearch 2.x
  community.general.elasticsearch_plugin:
    name: mobz/elasticsearch-head
    version: 2.0.0

- name: Uninstall Elasticsearch head plugin in Elasticsearch 2.x
  community.general.elasticsearch_plugin:
    name: mobz/elasticsearch-head
    state: absent

- name: Install a specific plugin in Elasticsearch >= 5.0
  community.general.elasticsearch_plugin:
    name: analysis-icu
    state: present

- name: Install the ingest-geoip plugin with a forced installation
  community.general.elasticsearch_plugin:
    name: ingest-geoip
    state: present
    force: true
```

### Authors

- Mathew Davies (@ThePixelDeveloper)
- Sam Doran (@samdoran)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
