---
collection: ansible
version: "8"
title: "community.general.etcd lookup – get info from an etcd server"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/etcd_lookup.html
fetched_at: 2026-07-28T01:52:48+00:00
---
# community.general.etcd lookup – get info from an etcd server

> **Note:**
>
> This lookup plugin is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.etcd`.

- [Synopsis](etcd_lookup.md#synopsis)
- [Terms](etcd_lookup.md#terms)
- [Keyword parameters](etcd_lookup.md#keyword-parameters)
- [Notes](etcd_lookup.md#notes)
- [See Also](etcd_lookup.md#see-also)
- [Examples](etcd_lookup.md#examples)
- [Return Value](etcd_lookup.md#return-value)

## [Synopsis](etcd_lookup.md#id1)

- Retrieves data from an etcd server

## [Terms](etcd_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  list / elements=string / required | the list of keys to lookup on the etcd server |

## [Keyword parameters](etcd_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.general.etcd', key1=value1, key2=value2, ...)` and `query('community.general.etcd', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **url**  string | Environment variable with the URL for the etcd server  **Default:** `"http://127.0.0.1:4001"`  **Configuration:**   - Environment variable: [`ANSIBLE_ETCD_URL`](../../environment_variables.md#envvar-ANSIBLE_ETCD_URL) |
| **validate_certs**  boolean | toggle checking that the ssl certificates are valid, you normally only want to turn this off with self-signed certs.  **Choices:**   - `false` - `true` ← (default) |
| **version**  string | Environment variable with the etcd protocol version  **Default:** `"v1"`  **Configuration:**   - Environment variable: [`ANSIBLE_ETCD_VERSION`](../../environment_variables.md#envvar-ANSIBLE_ETCD_VERSION) |

## [Notes](etcd_lookup.md#id4)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('community.general.etcd', term1, term2, key1=value1, key2=value2)` and `query('community.general.etcd', term1, term2, key1=value1, key2=value2)`

## [See Also](etcd_lookup.md#id5)

> **See also:**
>
> [community.general.etcd3](etcd3_module.md#ansible-collections-community-general-etcd3-module)
> :   Set or delete key value pairs from an etcd3 cluster.
>
> [community.general.etcd3](etcd3_lookup.md#ansible-collections-community-general-etcd3-lookup) lookup plugin
> :   Get key values from etcd3 server.

## [Examples](etcd_lookup.md#id6)

```yaml+jinja
- name: "a value from a locally running etcd"
  ansible.builtin.debug:
    msg: "{{ lookup('community.general.etcd', 'foo/bar') }}"

- name: "values from multiple folders on a locally running etcd"
  ansible.builtin.debug:
    msg: "{{ lookup('community.general.etcd', 'foo', 'bar', 'baz') }}"

- name: "since Ansible 2.5 you can set server options inline"
  ansible.builtin.debug:
    msg: "{{ lookup('community.general.etcd', 'foo', version='v2', url='http://192.168.0.27:4001') }}"
```

## [Return Value](etcd_lookup.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | list of values associated with input keys  **Returned:** success |

### Authors

- Jan-Piet Mens (@jpmens)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
