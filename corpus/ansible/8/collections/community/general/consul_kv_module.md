---
collection: ansible
version: "8"
title: "community.general.consul_kv module – Manipulate entries in the key/value store of a consul cluster"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/consul_kv_module.html
fetched_at: 2026-07-28T01:45:12+00:00
---
# community.general.consul_kv module – Manipulate entries in the key/value store of a consul cluster

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](consul_kv_module.md#ansible-collections-community-general-consul-kv-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.consul_kv`.

- [Synopsis](consul_kv_module.md#synopsis)
- [Requirements](consul_kv_module.md#requirements)
- [Parameters](consul_kv_module.md#parameters)
- [Attributes](consul_kv_module.md#attributes)
- [Examples](consul_kv_module.md#examples)

## [Synopsis](consul_kv_module.md#id1)

- Allows the retrieval, addition, modification and deletion of key/value entries in a consul cluster via the agent. The entire contents of the record, including the indices, flags and session are returned as `value`.
- If the `key` represents a prefix then note that when a value is removed, the existing value if any is returned as part of the results.
- See <http://www.consul.io/docs/agent/http.html#kv> for more details.

Aliases: clustering.consul.consul_kv

## [Requirements](consul_kv_module.md#id2)

The below requirements are needed on the host that executes this module.

- python-consul
- requests

## [Parameters](consul_kv_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cas**  string | Used when acquiring a lock with a session. If the `cas` is `0`, then Consul will only put the key if it does not already exist. If the `cas` value is non-zero, then the key is only set if the index matches the ModifyIndex of that key. |
| **flags**  string | Opaque positive integer value that can be passed when setting a value. |
| **host**  string | Host of the consul agent.  **Default:** `"localhost"` |
| **key**  string / required | The key at which the value should be stored. |
| **port**  integer | The port on which the consul agent is running.  **Default:** `8500` |
| **recurse**  boolean | If the key represents a prefix, each entry with the prefix can be retrieved by setting this to `true`.  **Choices:**   - `false` - `true` |
| **retrieve**  boolean | If the `state` is `present` and `value` is set, perform a read after setting the value and return this value.  **Choices:**   - `false` - `true` ← (default) |
| **scheme**  string | The protocol scheme on which the consul agent is running.  **Default:** `"http"` |
| **session**  string | The session that should be used to acquire or release a lock associated with a key/value pair. |
| **state**  string | The action to take with the supplied key and value. If the state is `present` and `value` is set, the key contents will be set to the value supplied and `changed` will be set to `true` only if the value was different to the current contents. If the state is `present` and `value` is not set, the existing value associated to the key will be returned. The state `absent` will remove the key/value pair, again `changed` will be set to `true` only if the key actually existed prior to the removal. An attempt can be made to obtain or free the lock associated with a key/value pair with the states `acquire` or `release` respectively. a valid session must be supplied to make the attempt changed will be true if the attempt is successful, false otherwise.  **Choices:**   - `"absent"` - `"acquire"` - `"present"` ← (default) - `"release"` |
| **token**  string | The token key identifying an ACL rule set that controls access to the key value pair |
| **validate_certs**  boolean | Whether to verify the tls certificate of the consul agent.  **Choices:**   - `false` - `true` ← (default) |
| **value**  string | The value should be associated with the given key, required if `state` is `present`. |

## [Attributes](consul_kv_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](consul_kv_module.md#id5)

```yaml+jinja
# If the key does not exist, the value associated to the "data" property in `retrieved_key` will be `None`
# If the key value is empty string, `retrieved_key["data"]["Value"]` will be `None`
- name: Retrieve a value from the key/value store
  community.general.consul_kv:
    key: somekey
  register: retrieved_key

- name: Add or update the value associated with a key in the key/value store
  community.general.consul_kv:
    key: somekey
    value: somevalue

- name: Remove a key from the store
  community.general.consul_kv:
    key: somekey
    state: absent

- name: Add a node to an arbitrary group via consul inventory (see consul.ini)
  community.general.consul_kv:
    key: ansible/groups/dc1/somenode
    value: top_secret

- name: Register a key/value pair with an associated session
  community.general.consul_kv:
    key: stg/node/server_birthday
    value: 20160509
    session: "{{ sessionid }}"
    state: acquire
```

### Authors

- Steve Gargan (@sgargan)
- Colin Nolan (@colin-nolan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
