---
collection: ansible
version: "6"
title: "community.general.logstash_plugin module – Manage Logstash plugins"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/logstash_plugin_module.html
fetched_at: 2026-07-27T17:10:36+00:00
---
# community.general.logstash_plugin module – Manage Logstash plugins

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
> To use it in a playbook, specify: `community.general.logstash_plugin`.

- [Synopsis](logstash_plugin_module.md#synopsis)
- [Parameters](logstash_plugin_module.md#parameters)
- [Examples](logstash_plugin_module.md#examples)

## [Synopsis](logstash_plugin_module.md#id1)

- Manages Logstash plugins.

## [Parameters](logstash_plugin_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  string / required | Install plugin with that name. |
| **plugin_bin**  path | Specify logstash-plugin to use for plugin management.  Default: `"/usr/share/logstash/bin/logstash-plugin"` |
| **proxy_host**  string | Proxy host to use during plugin installation. |
| **proxy_port**  string | Proxy port to use during plugin installation. |
| **state**  string | Apply plugin state.  Choices:   - `"present"` ← (default) - `"absent"` |
| **version**  string | Specify plugin Version of the plugin to install. If plugin exists with previous version, it will NOT be updated. |

## [Examples](logstash_plugin_module.md#id3)

```yaml+jinja
- name: Install Logstash beats input plugin
  community.general.logstash_plugin:
    state: present
    name: logstash-input-beats

- name: Install specific version of a plugin
  community.general.logstash_plugin:
    state: present
    name: logstash-input-syslog
    version: '3.2.0'

- name: Uninstall Logstash plugin
  community.general.logstash_plugin:
    state: absent
    name: logstash-filter-multiline

- name: Install Logstash plugin with alternate heap size
  community.general.logstash_plugin:
    state: present
    name: logstash-input-beats
  environment:
    LS_JAVA_OPTS: "-Xms256m -Xmx256m"
```

### Authors

- Loic Blot (@nerzhul)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
