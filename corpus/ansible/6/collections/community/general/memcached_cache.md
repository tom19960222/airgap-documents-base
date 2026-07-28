---
collection: ansible
version: "6"
title: "community.general.memcached cache – Use memcached DB for cache"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/memcached_cache.html
fetched_at: 2026-07-27T17:14:21+00:00
---
# community.general.memcached cache – Use memcached DB for cache

> **Note:**
>
> This cache plugin is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this cache plugin,
> see [Requirements](memcached_cache.md#ansible-collections-community-general-memcached-cache-requirements) for details.
>
> To use it in a playbook, specify: `community.general.memcached`.

- [Synopsis](memcached_cache.md#synopsis)
- [Requirements](memcached_cache.md#requirements)
- [Parameters](memcached_cache.md#parameters)

## [Synopsis](memcached_cache.md#id1)

- This cache uses JSON formatted, per host records saved in memcached.

## [Requirements](memcached_cache.md#id2)

The below requirements are needed on the local controller node that executes this cache.

- memcache (python lib)

## [Parameters](memcached_cache.md#id3)

| Parameter | Comments |
| --- | --- |
| **_prefix**  string | User defined prefix to use when creating the DB entries  Default: `"ansible_facts"`  Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   fact_caching_prefix = ansible_facts   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_PREFIX) |
| **_timeout**  integer | Expiration timeout in seconds for the cache plugin data. Set to 0 to never expire  Default: `86400`  Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   fact_caching_timeout = 86400   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_TIMEOUT) |
| **_uri**  list / elements=string | List of connection information for the memcached DBs  Default: `["127.0.0.1:11211"]`  Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   fact_caching_connection = 127.0.0.1:11211   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_CONNECTION) |

### Authors

- Unknown

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
