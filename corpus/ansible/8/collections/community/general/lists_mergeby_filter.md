---
collection: ansible
version: "8"
title: "community.general.lists_mergeby filter – Merge two or more lists of dictionaries by a given attribute"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/lists_mergeby_filter.html
fetched_at: 2026-07-28T01:52:21+00:00
---
# community.general.lists_mergeby filter – Merge two or more lists of dictionaries by a given attribute

> **Note:**
>
> This filter plugin is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.lists_mergeby`.

New in community.general 2.0.0

- [Synopsis](lists_mergeby_filter.md#synopsis)
- [Input](lists_mergeby_filter.md#input)
- [Positional parameters](lists_mergeby_filter.md#positional-parameters)
- [Keyword parameters](lists_mergeby_filter.md#keyword-parameters)
- [Notes](lists_mergeby_filter.md#notes)
- [Examples](lists_mergeby_filter.md#examples)
- [Return Value](lists_mergeby_filter.md#return-value)

## [Synopsis](lists_mergeby_filter.md#id1)

- Merge two or more lists by attribute `index`. Optional parameters `recursive` and `list_merge` control the merging of the lists in values. The function merge_hash from ansible.utils.vars is used. To learn details on how to use the parameters `recursive` and `list_merge` see Ansible User’s Guide chapter “Using filters to manipulate data” section “Combining hashes/dictionaries”.

## [Input](lists_mergeby_filter.md#id2)

This describes the input of the filter, the value before `| community.general.lists_mergeby`.

| Parameter | Comments |
| --- | --- |
| **Input**  list / elements=dictionary / required | A list of dictionaries. |

## [Positional parameters](lists_mergeby_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | community.general.lists_mergeby(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **another_list**  list / elements=dictionary | Another list of dictionaries. This parameter can be specified multiple times. |
| **index**  string / required | The dictionary key that must be present in every dictionary in every list that is used to merge the lists. |

## [Keyword parameters](lists_mergeby_filter.md#id4)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | community.general.lists_mergeby(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **list_merge**  string | Modifies the behaviour when the dictionaries (hashes) to merge contain arrays/lists.  **Choices:**   - `"replace"` ← (default) - `"keep"` - `"append"` - `"prepend"` - `"append_rp"` - `"prepend_rp"` |
| **recursive**  boolean | Should the combine recursively merge nested dictionaries (hashes).  **Note:** It does not depend on the value of the `hash_behaviour` setting in `ansible.cfg`.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](lists_mergeby_filter.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `input | community.general.lists_mergeby(positional1, positional2, key1=value1, key2=value2)`

## [Examples](lists_mergeby_filter.md#id6)

```yaml+jinja
- name: Merge two lists
  ansible.builtin.debug:
    msg: >-
      {{ list1 | community.general.lists_mergeby(
                    list2,
                    'index',
                    recursive=True,
                    list_merge='append'
                 ) }}"
  vars:
    list1:
      - index: a
        value: 123
      - index: b
        value: 42
    list2:
      - index: a
        foo: bar
      - index: c
        foo: baz
  # Produces the following list of dictionaries:
  #   {
  #     "index": "a",
  #     "foo": "bar",
  #     "value": 123
  #   },
  #   {
  #     "index": "b",
  #     "value": 42
  #   },
  #   {
  #     "index": "c",
  #     "foo": "baz"
  #   }
```

## [Return Value](lists_mergeby_filter.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=dictionary | The merged list.  **Returned:** success |

### Authors

- Vladimir Botka (@vbotka)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
