---
collection: ansible
version: "8"
title: "community.general.consul_kv lookup – Fetch metadata from a Consul key value store."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/consul_kv_lookup.html
fetched_at: 2026-07-28T01:52:43+00:00
---
# community.general.consul_kv lookup – Fetch metadata from a Consul key value store.

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
> see [Requirements](consul_kv_lookup.md#ansible-collections-community-general-consul-kv-lookup-requirements) for details.
>
> To use it in a playbook, specify: `community.general.consul_kv`.

- [Synopsis](consul_kv_lookup.md#synopsis)
- [Requirements](consul_kv_lookup.md#requirements)
- [Keyword parameters](consul_kv_lookup.md#keyword-parameters)
- [Examples](consul_kv_lookup.md#examples)
- [Return Value](consul_kv_lookup.md#return-value)

## [Synopsis](consul_kv_lookup.md#id1)

- Lookup metadata for a playbook from the key value store in a Consul cluster. Values can be easily set in the kv store with simple rest commands
- `curl -X PUT -d 'some-value' http://localhost:8500/v1/kv/ansible/somedata`

## [Requirements](consul_kv_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- python-consul python library <https://python-consul.readthedocs.io/en/latest/#installation>

## [Keyword parameters](consul_kv_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.general.consul_kv', key1=value1, key2=value2, ...)` and `query('community.general.consul_kv', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **_raw**  list / elements=string | List of key(s) to retrieve. |
| **client_cert**  string | The client cert to verify the ssl connection.  **Configuration:**   - INI entry:  ```YAML+Jinja   [lookup_consul]   client_cert = VALUE   ``` - Environment variable: [`ANSIBLE_CONSUL_CLIENT_CERT`](../../environment_variables.md#envvar-ANSIBLE_CONSUL_CLIENT_CERT) |
| **datacenter**  string | Retrieve the key from a consul datacenter other than the default for the consul host. |
| **host**  string | The target to connect to, must be a resolvable address.  Will be determined from [`ANSIBLE_CONSUL_URL`](../../environment_variables.md#envvar-ANSIBLE_CONSUL_URL) if that is set.  **Default:** `"localhost"`  **Configuration:**   - INI entry:  ```YAML+Jinja   [lookup_consul]   host = localhost   ``` |
| **index**  string | If the key has a value with the specified index then this is returned allowing access to historical values. |
| **port**  string | The port of the target host to connect to.  If you use [`ANSIBLE_CONSUL_URL`](../../environment_variables.md#envvar-ANSIBLE_CONSUL_URL) this value will be used from there.  **Default:** `8500` |
| **recurse**  boolean | If true, will retrieve all the values that have the given key as prefix.  **Choices:**   - `false` ← (default) - `true` |
| **scheme**  string | Whether to use http or https.  If you use [`ANSIBLE_CONSUL_URL`](../../environment_variables.md#envvar-ANSIBLE_CONSUL_URL) this value will be used from there.  **Default:** `"http"` |
| **token**  string | The acl token to allow access to restricted values. |
| **url**  string  *added in community.general 1.0.0* | The target to connect to.  Should look like this: `https://my.consul.server:8500`.  **Configuration:**   - INI entry:  ```YAML+Jinja   [lookup_consul]   url = VALUE   ``` - Environment variable: [`ANSIBLE_CONSUL_URL`](../../environment_variables.md#envvar-ANSIBLE_CONSUL_URL) |
| **validate_certs**  string | Whether to verify the ssl connection or not.  **Default:** `true`  **Configuration:**   - INI entry:  ```YAML+Jinja   [lookup_consul]   validate_certs = true   ``` - Environment variable: [`ANSIBLE_CONSUL_VALIDATE_CERTS`](../../environment_variables.md#envvar-ANSIBLE_CONSUL_VALIDATE_CERTS) |

## [Examples](consul_kv_lookup.md#id4)

```yaml+jinja
- ansible.builtin.debug:
    msg: 'key contains {{item}}'
  with_community.general.consul_kv:
    - 'key/to/retrieve'

- name: Parameters can be provided after the key be more specific about what to retrieve
  ansible.builtin.debug:
    msg: 'key contains {{item}}'
  with_community.general.consul_kv:
    - 'key/to recurse=true token=E6C060A9-26FB-407A-B83E-12DDAFCB4D98'

- name: retrieving a KV from a remote cluster on non default port
  ansible.builtin.debug:
    msg: "{{ lookup('community.general.consul_kv', 'my/key', host='10.10.10.10', port='2000') }}"
```

## [Return Value](consul_kv_lookup.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  dictionary | Value(s) stored in consul.  **Returned:** success |

### Authors

- Unknown

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
