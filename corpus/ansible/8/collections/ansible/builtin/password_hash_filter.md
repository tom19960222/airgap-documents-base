---
collection: ansible
version: "8"
title: "ansible.builtin.password_hash filter – convert input password into password_hash"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/password_hash_filter.html
fetched_at: 2026-07-28T01:04:57+00:00
---
# ansible.builtin.password_hash filter – convert input password into password_hash

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `password_hash`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.password_hash` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](password_hash_filter.md#synopsis)
- [Input](password_hash_filter.md#input)
- [Keyword parameters](password_hash_filter.md#keyword-parameters)
- [Notes](password_hash_filter.md#notes)
- [Examples](password_hash_filter.md#examples)
- [Return Value](password_hash_filter.md#return-value)

## [Synopsis](password_hash_filter.md#id1)

- Returns a password_hash of a secret.

## [Input](password_hash_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.password_hash`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | Secret to hash. |

## [Keyword parameters](password_hash_filter.md#id3)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.builtin.password_hash(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **hashtype**  string | Hashing algorithm to use.  **Choices:**   - `"md5"` - `"blowfish"` - `"sha256"` - `"sha512"` ← (default) |
| **ident**  string | Algorithm identifier. |
| **rounds**  integer | Number of encryption rounds, default varies by algorithm used. |
| **salt**  integer | Secret string that is used for the hashing, if none is provided a random one can be generated. |

## [Notes](password_hash_filter.md#id4)

> **Note:**
>
> - Algorithms available might be restricted by the system.

## [Examples](password_hash_filter.md#id5)

```yaml+jinja
# pwdhash => "$6$/bQCntzQ7VrgVcFa$VaMkmevkY1dqrx8neaenUDlVU.6L/.ojRbrnI4ID.yBHU6XON1cB422scCiXfUL5wRucMdLgJU0Fn38uoeBni/"
pwdhash: "{{ 'testing' | password_hash }}"
```

## [Return Value](password_hash_filter.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  string | The resulting password hash.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
