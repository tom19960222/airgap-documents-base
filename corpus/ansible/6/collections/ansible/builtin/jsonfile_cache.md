---
collection: ansible
version: "6"
title: "ansible.builtin.jsonfile cache – JSON formatted files."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/jsonfile_cache.html
fetched_at: 2026-07-27T16:44:13+00:00
---
# ansible.builtin.jsonfile cache – JSON formatted files.

> **Note:**
>
> This cache plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `jsonfile` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same cache plugin name.

- [Synopsis](jsonfile_cache.md#synopsis)
- [Parameters](jsonfile_cache.md#parameters)

## [Synopsis](jsonfile_cache.md#id1)

- This cache uses JSON formatted, per host, files saved to the filesystem.

## [Parameters](jsonfile_cache.md#id2)

| Parameter | Comments |
| --- | --- |
| **_prefix**  string | User defined prefix to use when creating the JSON files  Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   fact_caching_prefix = VALUE   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_PREFIX) |
| **_timeout**  integer | Expiration timeout for the cache plugin data  Default: `86400`  Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   fact_caching_timeout = 86400   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_TIMEOUT) |
| **_uri**  path / required | Path in which the cache plugin will save the JSON files  Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   fact_caching_connection = VALUE   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_CONNECTION) |

### Authors

- Ansible Core (@ansible-core)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
