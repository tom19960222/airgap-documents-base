---
collection: ansible
version: "8"
title: "ansible.builtin.combine filter – combine two dictionaries"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/combine_filter.html
fetched_at: 2026-07-28T01:04:50+00:00
---
# ansible.builtin.combine filter – combine two dictionaries

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `combine`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.combine` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](combine_filter.md#synopsis)
- [Input](combine_filter.md#input)
- [Positional parameters](combine_filter.md#positional-parameters)
- [Keyword parameters](combine_filter.md#keyword-parameters)
- [Notes](combine_filter.md#notes)
- [Examples](combine_filter.md#examples)
- [Return Value](combine_filter.md#return-value)

## [Synopsis](combine_filter.md#id1)

- Create a dictionary (hash/associative array) as a result of merging existing dictionaries.

## [Input](combine_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.combine`.

| Parameter | Comments |
| --- | --- |
| **Input**  dictionary / required | First dictionary to combine. |

## [Positional parameters](combine_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | ansible.builtin.combine(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **_dicts**  list / elements=dictionary / required | The list of dictionaries to combine. |

## [Keyword parameters](combine_filter.md#id4)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.builtin.combine(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **list_merge**  string | Behavior when encountering list elements.  **Choices:**   - `"append"`:   append newer entries to the older ones - `"append_rp"`:   append newer entries to the older ones, overwrite duplicates - `"keep"`:   discard newer entries - `"prepend"`:   insert newer entries in front of the older ones - `"prepend_rp"`:   insert newer entries in front of the older ones, discard duplicates - `"replace"` (default):   overwrite older entries with newer ones |
| **recursive**  boolean | If `True`, merge elements recursively.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](combine_filter.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `input | ansible.builtin.combine(positional1, positional2, key1=value1, key2=value2)`

## [Examples](combine_filter.md#id6)

```yaml+jinja
# ab => {'a':1, 'b':3, 'c': 4}
ab: {{ {'a':1, 'b':2} | ansible.builtin.combine({'b':3, 'c':4}) }}

many: "{{ dict1 | ansible.builtin.combine(dict2, dict3, dict4) }}"

# defaults => {'a':{'b':3, 'c':4}, 'd': 5}
# customization => {'a':{'c':20}}
# final => {'a':{'b':3, 'c':20}, 'd': 5}
final: "{{ defaults | ansible.builtin.combine(customization, recursive=true) }}"
```

## [Return Value](combine_filter.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  dictionary | Resulting merge of supplied dictionaries.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
