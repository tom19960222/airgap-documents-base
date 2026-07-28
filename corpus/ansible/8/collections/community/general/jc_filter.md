---
collection: ansible
version: "8"
title: "community.general.jc filter – Convert output of many shell commands and file-types to JSON"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/jc_filter.html
fetched_at: 2026-07-28T01:52:20+00:00
---
# community.general.jc filter – Convert output of many shell commands and file-types to JSON

> **Note:**
>
> This filter plugin is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this filter plugin,
> see [Requirements](jc_filter.md#ansible-collections-community-general-jc-filter-requirements) for details.
>
> To use it in a playbook, specify: `community.general.jc`.

New in community.general 1.1.0

- [Synopsis](jc_filter.md#synopsis)
- [Requirements](jc_filter.md#requirements)
- [Input](jc_filter.md#input)
- [Positional parameters](jc_filter.md#positional-parameters)
- [Keyword parameters](jc_filter.md#keyword-parameters)
- [Notes](jc_filter.md#notes)
- [Examples](jc_filter.md#examples)
- [Return Value](jc_filter.md#return-value)

## [Synopsis](jc_filter.md#id1)

- Convert output of many shell commands and file-types to JSON.
- Uses the [jc library](https://github.com/kellyjonbrazil/jc).

## [Requirements](jc_filter.md#id2)

The below requirements are needed on the local controller node that executes this filter.

- jc installed as a Python library (<https://pypi.org/project/jc/>)

## [Input](jc_filter.md#id3)

This describes the input of the filter, the value before `| community.general.jc`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | The data to convert. |

## [Positional parameters](jc_filter.md#id4)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | community.general.jc(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **parser**  string / required | The correct parser for the input data.  For example `ifconfig`.  Note: use underscores instead of dashes (if any) in the parser module name.  See <https://github.com/kellyjonbrazil/jc#parsers> for the latest list of parsers. |

## [Keyword parameters](jc_filter.md#id5)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | community.general.jc(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **quiet**  boolean | Set to `false` to not suppress warnings.  **Choices:**   - `false` - `true` ← (default) |
| **raw**  boolean | Set to `true` to return pre-processed JSON.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](jc_filter.md#id6)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `input | community.general.jc(positional1, positional2, key1=value1, key2=value2)`

## [Examples](jc_filter.md#id7)

```yaml+jinja
- name: Install the prereqs of the jc filter (jc Python package) on the Ansible controller
  delegate_to: localhost
  ansible.builtin.pip:
    name: jc
    state: present

- name: Run command
  ansible.builtin.command: uname -a
  register: result

- name: Convert command's result to JSON
  ansible.builtin.debug:
    msg: "{{ result.stdout | community.general.jc('uname') }}"
  # Possible output:
  #
  # "msg": {
  #   "hardware_platform": "x86_64",
  #   "kernel_name": "Linux",
  #   "kernel_release": "4.15.0-112-generic",
  #   "kernel_version": "#113-Ubuntu SMP Thu Jul 9 23:41:39 UTC 2020",
  #   "machine": "x86_64",
  #   "node_name": "kbrazil-ubuntu",
  #   "operating_system": "GNU/Linux",
  #   "processor": "x86_64"
  # }
```

## [Return Value](jc_filter.md#id8)

| Key | Description |
| --- | --- |
| **Return value**  any | The processed output.  **Returned:** success |

### Authors

- Kelly Brazil (@kellyjonbrazil)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
