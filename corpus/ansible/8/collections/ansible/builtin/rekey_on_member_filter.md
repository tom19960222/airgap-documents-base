---
collection: ansible
version: "8"
title: "ansible.builtin.rekey_on_member filter – Rekey a list of dicts into a dict using a member"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/rekey_on_member_filter.html
fetched_at: 2026-07-28T01:08:15+00:00
---
# ansible.builtin.rekey_on_member filter – Rekey a list of dicts into a dict using a member

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `rekey_on_member`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.rekey_on_member` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

New in ansible-core 2.13

- [Synopsis](rekey_on_member_filter.md#synopsis)
- [Input](rekey_on_member_filter.md#input)
- [Positional parameters](rekey_on_member_filter.md#positional-parameters)
- [Keyword parameters](rekey_on_member_filter.md#keyword-parameters)
- [Notes](rekey_on_member_filter.md#notes)
- [Examples](rekey_on_member_filter.md#examples)
- [Return Value](rekey_on_member_filter.md#return-value)

## [Synopsis](rekey_on_member_filter.md#id1)

- Iterate over several iterables in parallel, producing tuples with an item from each one.

## [Input](rekey_on_member_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.rekey_on_member`.

| Parameter | Comments |
| --- | --- |
| **Input**  dictionary / required | Original dictionary. |

## [Positional parameters](rekey_on_member_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | ansible.builtin.rekey_on_member(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **duplicates**  string | How to handle duplicates.  **Choices:**   - `"overwrite"` - `"error"` ← (default) |

## [Keyword parameters](rekey_on_member_filter.md#id4)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.builtin.rekey_on_member(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **_key**  string / required | The key to rekey. |

## [Notes](rekey_on_member_filter.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `input | ansible.builtin.rekey_on_member(positional1, positional2, key1=value1, key2=value2)`

## [Examples](rekey_on_member_filter.md#id6)

```yaml+jinja
# mydict => {'eigrp': {'state': 'enabled', 'proto': 'eigrp'}, 'ospf': {'state': 'enabled', 'proto': 'ospf'}}
 mydict: '{{ [{"proto": "eigrp", "state": "enabled"}, {"proto": "ospf", "state": "enabled"}] | rekey_on_member("proto") }}'
```

## [Return Value](rekey_on_member_filter.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  dictionary | The resulting dictionary.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
