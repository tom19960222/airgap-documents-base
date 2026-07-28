---
collection: ansible
version: "8"
title: "ansible.builtin.b64decode filter – Decode a base64 string"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/b64decode_filter.html
fetched_at: 2026-07-28T01:05:05+00:00
---
# ansible.builtin.b64decode filter – Decode a base64 string

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `b64decode`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.b64decode` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](b64decode_filter.md#synopsis)
- [Input](b64decode_filter.md#input)
- [Examples](b64decode_filter.md#examples)
- [Return Value](b64decode_filter.md#return-value)

## [Synopsis](b64decode_filter.md#id1)

- Base64 decoding function.
- The return value is a string.
- Trying to store a binary blob in a string most likely corrupts the binary. To base64 decode a binary blob, use the ``base64`` command and pipe the encoded data through standard input. For example, in the ansible.builtin.shell`` module, ``cmd=”base64 –decode > myfile.bin” stdin=”{{ encoded }}”``.

## [Input](b64decode_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.b64decode`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | A base64 string to decode. |

## [Examples](b64decode_filter.md#id3)

```yaml+jinja
# b64 decode a string
lola: "{{ 'bG9sYQ==' | b64decode }}"

# b64 decode the content of 'b64stuff' variable
stuff: "{{ b64stuff | b64encode }}"
```

## [Return Value](b64decode_filter.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  string | The contents of the base64 encoded string.  **Returned:** success |

### Authors

- ansible core team

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
