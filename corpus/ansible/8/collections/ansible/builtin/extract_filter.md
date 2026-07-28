---
collection: ansible
version: "8"
title: "ansible.builtin.extract filter – extract a value based on an index or key"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/extract_filter.html
fetched_at: 2026-07-28T01:08:03+00:00
---
# ansible.builtin.extract filter – extract a value based on an index or key

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `extract`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.extract` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](extract_filter.md#synopsis)
- [Input](extract_filter.md#input)
- [Positional parameters](extract_filter.md#positional-parameters)
- [Keyword parameters](extract_filter.md#keyword-parameters)
- [Notes](extract_filter.md#notes)
- [Examples](extract_filter.md#examples)
- [Return Value](extract_filter.md#return-value)

## [Synopsis](extract_filter.md#id1)

- Extract a value from a list or dictionary based on an index/key.
- User must ensure that index or key used matches the type of container.
- Equivalent of using `list[index]` and `dictionary[key]` but useful as a filter to combine with `map`.

## [Input](extract_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.extract`.

| Parameter | Comments |
| --- | --- |
| **Input**  any / required | Index or key to extract. |

## [Positional parameters](extract_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | ansible.builtin.extract(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **morekeys**  list / elements=dictionary / required | Indicies or keys to extract from the initial result (subkeys/subindices). |

## [Keyword parameters](extract_filter.md#id4)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.builtin.extract(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **contianer**  any / required | Dictionary or list from which to extract a value. |

## [Notes](extract_filter.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `input | ansible.builtin.extract(positional1, positional2, key1=value1, key2=value2)`

## [Examples](extract_filter.md#id6)

```yaml+jinja
# extracted => 'b', same as ['a', 'b', 'c'][1]
extracted: "{{ 1 | extract(['a', 'b', 'c']) }}"

# extracted_key => '2', same as {'a': 1, 'b': 2, 'c': 3}['b']
extracted_key: "{{ 'b' | extract({'a': 1, 'b': 2, 'c': 3}) }}"

# extracted_key_r => '2', same as [{'a': 1, 'b': 2, 'c': 3}, {'x': 9, 'y': 10}][0]['b']
extracted_key_r: "{{ 0 | extract([{'a': 1, 'b': 2, 'c': 3}, {'x': 9, 'y': 10}], morekeys='b') }}"
```

## [Return Value](extract_filter.md#id7)

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
