---
collection: ansible
version: "6"
title: "community.general.redis cache – Use Redis DB for cache"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/redis_cache.html
fetched_at: 2026-07-27T17:14:23+00:00
---
# community.general.redis cache – Use Redis DB for cache

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
> see [Requirements](redis_cache.md#ansible-collections-community-general-redis-cache-requirements) for details.
>
> To use it in a playbook, specify: `community.general.redis`.

- [Synopsis](redis_cache.md#synopsis)
- [Requirements](redis_cache.md#requirements)
- [Parameters](redis_cache.md#parameters)

## [Synopsis](redis_cache.md#id1)

- This cache uses JSON formatted, per host records saved in Redis.

## [Requirements](redis_cache.md#id2)

The below requirements are needed on the local controller node that executes this cache.

- redis>=2.4.5 (python lib)

## [Parameters](redis_cache.md#id3)

| Parameter | Comments |
| --- | --- |
| **_keyset_name**  string  added in community.general 1.3.0 | User defined name for cache keyset name.  Default: `"ansible_cache_keys"`  Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   fact_caching_redis_keyset_name = ansible_cache_keys   ``` - Environment variable: [`ANSIBLE_CACHE_REDIS_KEYSET_NAME`](../../environment_variables.md#envvar-ANSIBLE_CACHE_REDIS_KEYSET_NAME) |
| **_prefix**  string | User defined prefix to use when creating the DB entries  Default: `"ansible_facts"`  Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   fact_caching_prefix = ansible_facts   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_PREFIX) |
| **_sentinel_service_name**  string  added in community.general 1.3.0 | The redis sentinel service name (or referenced as cluster name).  Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   fact_caching_redis_sentinel = VALUE   ``` - Environment variable: [`ANSIBLE_CACHE_REDIS_SENTINEL`](../../environment_variables.md#envvar-ANSIBLE_CACHE_REDIS_SENTINEL) |
| **_timeout**  integer | Expiration timeout in seconds for the cache plugin data. Set to 0 to never expire  Default: `86400`  Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   fact_caching_timeout = 86400   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_TIMEOUT) |
| **_uri**  string / required | A colon separated string of connection information for Redis.  The format is `host:port:db:password`, for example `localhost:6379:0:changeme`.  To use encryption in transit, prefix the connection with `tls://`, as in `tls://localhost:6379:0:changeme`.  To use redis sentinel, use separator `;`, for example `localhost:26379;localhost:26379;0:changeme`. Requires redis>=2.9.0.  Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   fact_caching_connection = VALUE   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_CONNECTION) |

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
