---
collection: ansible
version: "8"
title: "ansible.builtin.b64encode filter – Encode a string as base64"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/b64encode_filter.html
fetched_at: 2026-07-28T01:05:04+00:00
---
# ansible.builtin.b64encode filter – Encode a string as base64

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `b64encode`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.b64encode` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](b64encode_filter.md#synopsis)
- [Input](b64encode_filter.md#input)
- [Examples](b64encode_filter.md#examples)
- [Return Value](b64encode_filter.md#return-value)

## [Synopsis](b64encode_filter.md#id1)

- Base64 encoding function.

## [Input](b64encode_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.b64encode`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | A string to encode. |

## [Examples](b64encode_filter.md#id3)

```yaml+jinja
# b64 encode a string
b64lola: "{{ 'lola'|b64encode }}"

# b64 encode the content of 'stuff' variable
b64stuff: "{{ stuff|b64encode }}"
```

## [Return Value](b64encode_filter.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  string | A base64 encoded string.  **Returned:** success |

### Authors

- ansible core team

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
