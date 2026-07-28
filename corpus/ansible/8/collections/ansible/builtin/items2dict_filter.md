---
collection: ansible
version: "8"
title: "ansible.builtin.items2dict filter – Consolidate a list of itemized dictionaries into a dictionary"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/items2dict_filter.html
fetched_at: 2026-07-28T01:04:43+00:00
---
# ansible.builtin.items2dict filter – Consolidate a list of itemized dictionaries into a dictionary

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `items2dict`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.items2dict` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

New in Ansible 2.7

- [Synopsis](items2dict_filter.md#synopsis)
- [Input](items2dict_filter.md#input)
- [Positional parameters](items2dict_filter.md#positional-parameters)
- [See Also](items2dict_filter.md#see-also)
- [Examples](items2dict_filter.md#examples)
- [Return Value](items2dict_filter.md#return-value)

## [Synopsis](items2dict_filter.md#id1)

- Takes a list of dicts with each having a `key` and `value` keys, and transforms the list into a dictionary, effectively as the reverse of [dict2items](dict2items_filter.md#ansible-collections-ansible-builtin-dict2items-filter).

## [Input](items2dict_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.items2dict`.

| Parameter | Comments |
| --- | --- |
| **Input**  list / elements=dictionary / required | A list of dictionaries.  Every dictionary must have keys `key` and `value`. |

## [Positional parameters](items2dict_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | ansible.builtin.items2dict(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **key_name**  string | The name of the key in the element dictionaries that holds the key to use at destination.  **Default:** `"key"` |
| **value_name**  string | The name of the key in the element dictionaries that holds the value to use at destination.  **Default:** `"value"` |

## [See Also](items2dict_filter.md#id4)

> **See also:**
>
> [ansible.builtin.dict2items](dict2items_filter.md#ansible-collections-ansible-builtin-dict2items-filter) filter plugin
> :   Convert a dictionary into an itemized list of dictionaries.

## [Examples](items2dict_filter.md#id5)

```yaml+jinja
# mydict =>  { "hi": "bye", "ciao": "ciao" }
mydict: {{ [{'key': 'hi', 'value': 'bye'}, {'key': 'ciao', 'value': 'ciao'} ]| items2dict}}

# The output is a dictionary with two key/value pairs:
#     Application: payment
#     Environment: dev
vars:
  tags:
    - key: Application
      value: payment
    - key: Environment
      value: dev
  consolidated: "{{ tags | items2dict }}"
```

## [Return Value](items2dict_filter.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  dictionary | Dictionary with the consolidated key/values.  **Returned:** success |

### Authors

- Ansible core team

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
