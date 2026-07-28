---
collection: ansible
version: "8"
title: "community.general.redis lookup – fetch data from Redis"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/redis_lookup.html
fetched_at: 2026-07-28T01:52:59+00:00
---
# community.general.redis lookup – fetch data from Redis

> **Note:**
>
> This lookup plugin is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](redis_lookup.md#ansible-collections-community-general-redis-lookup-requirements) for details.
>
> To use it in a playbook, specify: `community.general.redis`.

- [Synopsis](redis_lookup.md#synopsis)
- [Requirements](redis_lookup.md#requirements)
- [Terms](redis_lookup.md#terms)
- [Keyword parameters](redis_lookup.md#keyword-parameters)
- [Notes](redis_lookup.md#notes)
- [Examples](redis_lookup.md#examples)
- [Return Value](redis_lookup.md#return-value)

## [Synopsis](redis_lookup.md#id1)

- This lookup returns a list of results from a Redis DB corresponding to a list of items given to it

## [Requirements](redis_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- redis (python library <https://github.com/andymccurdy/redis-py/>)

## [Terms](redis_lookup.md#id3)

| Parameter | Comments |
| --- | --- |
| **Terms**  string | list of keys to query |

## [Keyword parameters](redis_lookup.md#id4)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.general.redis', key1=value1, key2=value2, ...)` and `query('community.general.redis', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **host**  string | location of Redis host  **Default:** `"127.0.0.1"`  **Configuration:**   - INI entry:  ```YAML+Jinja   [lookup_redis]   host = 127.0.0.1   ``` - Environment variable: [`ANSIBLE_REDIS_HOST`](../../environment_variables.md#envvar-ANSIBLE_REDIS_HOST) |
| **port**  integer | port on which Redis is listening on  **Default:** `6379`  **Configuration:**   - INI entry:  ```YAML+Jinja   [lookup_redis]   port = 6379   ``` - Environment variable: [`ANSIBLE_REDIS_PORT`](../../environment_variables.md#envvar-ANSIBLE_REDIS_PORT) |
| **socket**  path | path to socket on which to query Redis, this option overrides host and port options when set.  **Configuration:**   - INI entry:  ```YAML+Jinja   [lookup_redis]   socket = VALUE   ``` - Environment variable: [`ANSIBLE_REDIS_SOCKET`](../../environment_variables.md#envvar-ANSIBLE_REDIS_SOCKET) |

## [Notes](redis_lookup.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('community.general.redis', term1, term2, key1=value1, key2=value2)` and `query('community.general.redis', term1, term2, key1=value1, key2=value2)`

## [Examples](redis_lookup.md#id6)

```yaml+jinja
- name: query redis for somekey (default or configured settings used)
  ansible.builtin.debug:
    msg: "{{ lookup('community.general.redis', 'somekey') }}"

- name: query redis for list of keys and non-default host and port
  ansible.builtin.debug:
    msg: "{{ lookup('community.general.redis', item, host='myredis.internal.com', port=2121) }}"
  loop: '{{list_of_redis_keys}}'

- name: use list directly
  ansible.builtin.debug:
    msg: "{{ lookup('community.general.redis', 'key1', 'key2', 'key3') }}"

- name: use list directly with a socket
  ansible.builtin.debug:
    msg: "{{ lookup('community.general.redis', 'key1', 'key2', socket='/var/tmp/redis.sock') }}"
```

## [Return Value](redis_lookup.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | value(s) stored in Redis  **Returned:** success |

### Authors

- Jan-Piet Mens (@jpmens) <jpmens(at)gmail.com>
- Ansible Core Team

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
