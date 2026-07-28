---
collection: ansible
version: "8"
title: "ansible.builtin.dict2items filter – Convert a dictionary into an itemized list of dictionaries"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/dict2items_filter.html
fetched_at: 2026-07-28T01:04:42+00:00
---
# ansible.builtin.dict2items filter – Convert a dictionary into an itemized list of dictionaries

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `dict2items`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.dict2items` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](dict2items_filter.md#synopsis)
- [Input](dict2items_filter.md#input)
- [Positional parameters](dict2items_filter.md#positional-parameters)
- [See Also](dict2items_filter.md#see-also)
- [Examples](dict2items_filter.md#examples)
- [Return Value](dict2items_filter.md#return-value)

## [Synopsis](dict2items_filter.md#id1)

- Takes a dictionary and transforms it into a list of dictionaries, with each having a `key` and `value` keys that correspond to the keys and values of the original.

## [Input](dict2items_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.dict2items`.

| Parameter | Comments |
| --- | --- |
| **Input**  dictionary / required | The dictionary to transform |

## [Positional parameters](dict2items_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | ansible.builtin.dict2items(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **key_name**  string  *added in Ansible 2.8* | The name of the property on the item representing the dictionary’s keys.  **Default:** `"key"` |
| **value_name**  string  *added in Ansible 2.8* | The name of the property on the item representing the dictionary’s values.  **Default:** `"value"` |

## [See Also](dict2items_filter.md#id4)

> **See also:**
>
> [ansible.builtin.items2dict](items2dict_filter.md#ansible-collections-ansible-builtin-items2dict-filter) filter plugin
> :   Consolidate a list of itemized dictionaries into a dictionary.

## [Examples](dict2items_filter.md#id5)

```yaml+jinja
# items => [ { "key": "a", "value": 1 }, { "key": "b", "value": 2 } ]
items: "{{ {'a': 1, 'b': 2}| dict2items}}"

vars:
  files:
    users: /etc/passwd
    groups: /etc/group
  files_dicts: "{{ files | dict2items(key_name='file', value_name='path') }}"
```

## [Return Value](dict2items_filter.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=dictionary | A list of dictionaries.  **Returned:** success |

### Authors

- Ansible core team

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
