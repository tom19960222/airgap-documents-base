---
collection: ansible
version: "8"
title: "ansible.builtin.checksum filter – checksum of input data"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/checksum_filter.html
fetched_at: 2026-07-28T01:07:58+00:00
---
# ansible.builtin.checksum filter – checksum of input data

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `checksum`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.checksum` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](checksum_filter.md#synopsis)
- [Input](checksum_filter.md#input)
- [Examples](checksum_filter.md#examples)
- [Return Value](checksum_filter.md#return-value)

## [Synopsis](checksum_filter.md#id1)

- Returns a checksum ([SHA-1](https://en.wikipedia.org/wiki/SHA-1)) hash of the input data.

## [Input](checksum_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.checksum`.

| Parameter | Comments |
| --- | --- |
| **Input**  any / required | Data to checksum. |

## [Examples](checksum_filter.md#id3)

```yaml+jinja
# csum => "109f4b3c50d7b0df729d299bc6f8e9ef9066971f"
csum: "{{ 'test2' | checksum }}"
```

## [Return Value](checksum_filter.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  string | The checksum (SHA-1) of the input.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
