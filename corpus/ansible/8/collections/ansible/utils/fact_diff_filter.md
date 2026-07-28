---
collection: ansible
version: "8"
title: "ansible.utils.fact_diff filter – Find the difference between currently set facts"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/fact_diff_filter.html
fetched_at: 2026-07-28T01:09:44+00:00
---
# ansible.utils.fact_diff filter – Find the difference between currently set facts

> **Note:**
>
> This filter plugin is part of the [ansible.utils collection](https://galaxy.ansible.com/ui/repo/published/ansible/utils/) (version 2.12.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.utils`.
>
> To use it in a playbook, specify: `ansible.utils.fact_diff`.

New in ansible.utils 2.12.0

- [Synopsis](fact_diff_filter.md#synopsis)
- [Keyword parameters](fact_diff_filter.md#keyword-parameters)
- [Examples](fact_diff_filter.md#examples)
- [Return Value](fact_diff_filter.md#return-value)

## [Synopsis](fact_diff_filter.md#id1)

- Compare two facts or variables and get a diff.

## [Keyword parameters](fact_diff_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.utils.fact_diff(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **after**  any / required | The second fact to be used in the comparison. |
| **before**  any / required | The first fact to be used in the comparison. |
| **plugin**  dictionary | Configure and specify the diff plugin to use  **Default:** `{}` |
| **name**  string | The diff plugin to use, in fully qualified collection name format.  **Default:** `"ansible.utils.native"` |
| **vars**  dictionary | Parameters passed to the diff plugin.  **Default:** `{}` |
| **skip_lines**  list / elements=string | Skip lines matching these regular expressions.  Matches will be removed prior to the diff.  If the provided *before* and *after* are a string, they will be split.  Each entry in each list will be cast to a string for the comparison |

## [Examples](fact_diff_filter.md#id3)

```yaml+jinja
- name: Set fact
  ansible.builtin.set_fact:
    before:
      a:
        b:
          c:
            d:
              - 0
              - 1
    after:
      a:
        b:
          c:
            d:
              - 2
              - 3

- name: Show the difference in json format
  ansible.builtin.set_fact:
    result: "{{before | ansible.utils.fact_diff(after)}}"

# TASK [Show the difference in json format] **********************************************************************************************
# ok: [localhost] => {
#     "ansible_facts": {
#         "result": [
#             "--- before",
#             "+++ after",
#             "@@ -3,8 +3,8 @@",
#             "         "b": {",
#             "             "c": {",
#             "                 "d": [",
#             "-                    0,",
#             "-                    1",
#             "+                    2,",
#             "+                    3",
#             "                 ]",
#             "             }",
#             "         }",
#             ""
#         ]
#     },
#     "changed": false
# }

- name: Set fact
  ansible.builtin.set_fact:
    before: "{{ before|ansible.utils.to_paths }}"
    after: "{{ after|ansible.utils.to_paths }}"

- name: Show the difference in path format
  ansible.builtin.set_fact:
    result: "{{before | ansible.utils.fact_diff(after)}}"

# TASK [Show the difference in path format] **********************************************************************************************
# ok: [localhost] => {
#     "ansible_facts": {
#         "result": [
#             "--- before",
#             "+++ after",
#             "@@ -1,4 +1,4 @@",
#             " {",
#             "-    "a.b.c.d[0]": 0,",
#             "-    "a.b.c.d[1]": 1",
#             "+    "a.b.c.d[0]": 2,",
#             "+    "a.b.c.d[1]": 3",
#             " }",
#             ""
#         ]
#     },
#     "changed": false
# }

- name: Set fact
  ansible.builtin.set_fact:
    before: "{{ before|to_nice_yaml }}"
    after: "{{ after|to_nice_yaml }}"

- name: Show the difference in yaml format
  ansible.builtin.set_fact:
    result: "{{before | ansible.utils.fact_diff(after)}}"

# TASK [Show the difference in yaml format] **********************************************************************************************
# ok: [localhost] => {
#     "ansible_facts": {
#         "result": [
#             "--- before",
#             "+++ after",
#             "@@ -1,2 +1,2 @@",
#             "-a.b.c.d[0]: 0",
#             "-a.b.c.d[1]: 1",
#             "+a.b.c.d[0]: 2",
#             "+a.b.c.d[1]: 3",
#             ""
#         ]
#     },
#     "changed": false
# }
```

## [Return Value](fact_diff_filter.md#id4)

| Key | Description |
| --- | --- |
| **result**  list / elements=string | Returns diff between before and after facts.  **Returned:** success |

### Authors

- Ashwini Mhatre ((@amhatre))

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.utils/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.utils)
