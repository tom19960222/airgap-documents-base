---
collection: ansible
version: "8"
title: "ansible.builtin.md5 filter – MD5 hash of input data"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/md5_filter.html
fetched_at: 2026-07-28T01:08:10+00:00
---
# ansible.builtin.md5 filter – MD5 hash of input data

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `md5`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.md5` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](md5_filter.md#synopsis)
- [Input](md5_filter.md#input)
- [Notes](md5_filter.md#notes)
- [Examples](md5_filter.md#examples)
- [Return Value](md5_filter.md#return-value)

## [Synopsis](md5_filter.md#id1)

- Returns an [MD5 hash](https://en.wikipedia.org/wiki/MD5) of the input data

## [Input](md5_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.md5`.

| Parameter | Comments |
| --- | --- |
| **Input**  any / required | data to hash |

## [Notes](md5_filter.md#id3)

> **Note:**
>
> - This requires the MD5 algorithm to be available on the system, security contexts like FIPS might prevent this.
> - MD5 has long been deemed insecure and is not recommended for security related uses.

## [Examples](md5_filter.md#id4)

```yaml+jinja
# md5hash => "ae2b1fca515949e5d54fb22b8ed95575"
md5hash: "{{ 'testing' | md5 }}"
```

## [Return Value](md5_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  string | The MD5 hash of the input.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
