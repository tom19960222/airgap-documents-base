---
collection: ansible
version: "8"
title: "community.general.pids module – Retrieves process IDs list if the process is running otherwise return empty list"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/pids_module.html
fetched_at: 2026-07-28T01:49:00+00:00
---
# community.general.pids module – Retrieves process IDs list if the process is running otherwise return empty list

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](pids_module.md#ansible-collections-community-general-pids-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.pids`.

- [Synopsis](pids_module.md#synopsis)
- [Requirements](pids_module.md#requirements)
- [Parameters](pids_module.md#parameters)
- [Attributes](pids_module.md#attributes)
- [Examples](pids_module.md#examples)
- [Return Values](pids_module.md#return-values)

## [Synopsis](pids_module.md#id1)

- Retrieves a list of PIDs of given process name in Ansible controller/controlled machines.Returns an empty list if no process in that name exists.

Aliases: system.pids

## [Requirements](pids_module.md#id2)

The below requirements are needed on the host that executes this module.

- psutil(python module)

## [Parameters](pids_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ignore_case**  boolean  *added in community.general 3.0.0* | Ignore case in pattern if using the `pattern` option.  **Choices:**   - `false` ← (default) - `true` |
| **name**  string | The name of the process(es) you want to get PID(s) for. |
| **pattern**  string  *added in community.general 3.0.0* | The pattern (regular expression) to match the process(es) you want to get PID(s) for. |

## [Attributes](pids_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](pids_module.md#id5)

```yaml+jinja
# Pass the process name
- name: Getting process IDs of the process
  community.general.pids:
      name: python
  register: pids_of_python

- name: Printing the process IDs obtained
  ansible.builtin.debug:
    msg: "PIDS of python:{{pids_of_python.pids|join(',')}}"

- name: Getting process IDs of processes matching pattern
  community.general.pids:
    pattern: python(2(\.7)?|3(\.6)?)?\s+myapp\.py
  register: myapp_pids
```

## [Return Values](pids_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **pids**  list / elements=string | Process IDs of the given process  **Returned:** list of none, one, or more process IDs  **Sample:** `[100, 200]` |

### Authors

- Saranya Sridharan (@saranyasridharan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
