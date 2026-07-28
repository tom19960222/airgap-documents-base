---
collection: ansible
version: "6"
title: "community.general.yaml cache – YAML formatted files."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/yaml_cache.html
fetched_at: 2026-07-27T17:14:23+00:00
---
# community.general.yaml cache – YAML formatted files.

> **Note:**
>
> This cache plugin is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.yaml`.

- [Synopsis](yaml_cache.md#synopsis)
- [Parameters](yaml_cache.md#parameters)

## [Synopsis](yaml_cache.md#id1)

- This cache uses YAML formatted, per host, files saved to the filesystem.

## [Parameters](yaml_cache.md#id2)

| Parameter | Comments |
| --- | --- |
| **_prefix**  string | User defined prefix to use when creating the files  Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   fact_caching_prefix = VALUE   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_PREFIX) |
| **_timeout**  integer | Expiration timeout in seconds for the cache plugin data. Set to 0 to never expire  Default: `86400`  Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   fact_caching_timeout = 86400   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_TIMEOUT) |
| **_uri**  string / required | Path in which the cache plugin will save the files  Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   fact_caching_connection = VALUE   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_CONNECTION) |

### Authors

- Brian Coca (@bcoca)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
