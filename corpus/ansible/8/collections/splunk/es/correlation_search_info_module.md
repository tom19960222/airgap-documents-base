---
collection: ansible
version: "8"
title: "splunk.es.correlation_search_info module – Manage Splunk Enterprise Security Correlation Searches"
source_url: https://docs.ansible.com/projects/ansible/8/collections/splunk/es/correlation_search_info_module.html
fetched_at: 2026-07-28T02:53:48+00:00
---
# splunk.es.correlation_search_info module – Manage Splunk Enterprise Security Correlation Searches

> **Note:**
>
> This module is part of the [splunk.es collection](https://galaxy.ansible.com/ui/repo/published/splunk/es/) (version 2.1.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install splunk.es`.
>
> To use it in a playbook, specify: `splunk.es.correlation_search_info`.

New in splunk.es 1.0.0

- [Synopsis](correlation_search_info_module.md#synopsis)
- [Parameters](correlation_search_info_module.md#parameters)
- [Examples](correlation_search_info_module.md#examples)

## [Synopsis](correlation_search_info_module.md#id1)

- This module allows for the query of Splunk Enterprise Security Correlation Searches

Aliases: splunk_correlation_search_info

## [Parameters](correlation_search_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  string | Name of coorelation search |

## [Examples](correlation_search_info_module.md#id3)

```yaml+jinja
- name: Example usage of splunk.es.correlation_search_info
  splunk.es.correlation_search_info:
    name: "Name of correlation search"
  register: scorrelation_search_info

- name: debug display information gathered
  debug:
    var: scorrelation_search_info
```

### Authors

- Ansible Security Automation Team (@maxamillion) <<https://github.com/ansible-security>>

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/splunk.es/issues)
- [Repository (Sources)](https://github.com/ansible-collections/splunk.es)
