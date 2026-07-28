---
collection: ansible
version: "8"
title: "ansible.builtin.hash filter – hash of input data"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/hash_filter.html
fetched_at: 2026-07-28T01:04:57+00:00
---
# ansible.builtin.hash filter – hash of input data

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `hash`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.hash` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](hash_filter.md#synopsis)
- [Input](hash_filter.md#input)
- [Keyword parameters](hash_filter.md#keyword-parameters)
- [Examples](hash_filter.md#examples)
- [Return Value](hash_filter.md#return-value)

## [Synopsis](hash_filter.md#id1)

- Returns a configurable hash of the input data. Uses [SHA-1](https://en.wikipedia.org/wiki/SHA-1) by default.

## [Input](hash_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.hash`.

| Parameter | Comments |
| --- | --- |
| **Input**  any / required | Data to checksum. |

## [Keyword parameters](hash_filter.md#id3)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.builtin.hash(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **hashtype**  string | Type of algorithm to produce the hash.  The list of available choices depends on the installed Python’s hashlib.  **Default:** `"sha1"` |

## [Examples](hash_filter.md#id4)

```yaml+jinja
# sha1_hash => "109f4b3c50d7b0df729d299bc6f8e9ef9066971f"
sha1_hash: {{ 'test2' | hash('sha1') }}
# md5 => "5a105e8b9d40e1329780d62ea2265d8a"
md5: {{ 'test2' | hash('md5') }}
```

## [Return Value](hash_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  string | The checksum of the input, as configured in *hashtype*.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
