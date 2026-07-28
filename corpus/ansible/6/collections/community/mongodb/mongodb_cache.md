---
collection: ansible
version: "6"
title: "community.mongodb.mongodb cache – Use MongoDB for caching"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/mongodb/mongodb_cache.html
fetched_at: 2026-07-27T17:16:13+00:00
---
# community.mongodb.mongodb cache – Use MongoDB for caching

> **Note:**
>
> This cache plugin is part of the [community.mongodb collection](https://galaxy.ansible.com/community/mongodb) (version 1.4.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.mongodb`.
> You need further requirements to be able to use this cache plugin,
> see [Requirements](mongodb_cache.md#ansible-collections-community-mongodb-mongodb-cache-requirements) for details.
>
> To use it in a playbook, specify: `community.mongodb.mongodb`.

New in community.mongodb 1.0.0

- [Synopsis](mongodb_cache.md#synopsis)
- [Requirements](mongodb_cache.md#requirements)
- [Parameters](mongodb_cache.md#parameters)

## [Synopsis](mongodb_cache.md#id1)

- This cache uses per host records saved in MongoDB.

## [Requirements](mongodb_cache.md#id2)

The below requirements are needed on the local controller node that executes this cache.

- pymongo>=3

## [Parameters](mongodb_cache.md#id3)

| Parameter | Comments |
| --- | --- |
| **_prefix**  string | User defined prefix to use when creating the DB entries  Default: `"ansible_facts"`  Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   fact_caching_prefix = ansible_facts   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_PREFIX) |
| **_timeout**  integer | Expiration timeout in seconds for the cache plugin data. Set to 0 to never expire  Default: `86400`  Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   fact_caching_timeout = 86400   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_TIMEOUT) |
| **_uri**  string | MongoDB Connection String URI  Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   fact_caching_connection = VALUE   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_CONNECTION) |

### Authors

- Matt Martz (@sivel)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.mongodb)
[Repository (Sources)](https://github.com/ansible-collections/community.mongodb)
