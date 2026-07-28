---
collection: ansible
version: "8"
title: "ansible.netcommon.type5_pw filter – The type5_pw filter plugin."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/netcommon/type5_pw_filter.html
fetched_at: 2026-07-28T01:09:21+00:00
---
# ansible.netcommon.type5_pw filter – The type5_pw filter plugin.

> **Note:**
>
> This filter plugin is part of the [ansible.netcommon collection](https://galaxy.ansible.com/ui/repo/published/ansible/netcommon/) (version 5.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.netcommon`.
>
> To use it in a playbook, specify: `ansible.netcommon.type5_pw`.

New in ansible.netcommon 1.0.0

- [Synopsis](type5_pw_filter.md#synopsis)
- [Keyword parameters](type5_pw_filter.md#keyword-parameters)
- [Notes](type5_pw_filter.md#notes)
- [Examples](type5_pw_filter.md#examples)

## [Synopsis](type5_pw_filter.md#id1)

- Filter plugin to produce cisco type5 hashed password.
- Using the parameters below - `xml_data | ansible.netcommon.type5_pw(template.yml`)

## [Keyword parameters](type5_pw_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.netcommon.type5_pw(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **password**  string / required | The password to be hashed. |
| **salt**  string | Mention the salt to hash the password. |

## [Notes](type5_pw_filter.md#id3)

> **Note:**
>
> - The filter plugin generates cisco type5 hashed password.

## [Examples](type5_pw_filter.md#id4)

```yaml+jinja
# Using type5_pw

- name: Set some facts
  ansible.builtin.set_fact:
    password: "cisco@123"

- name: Filter type5_pw invocation
  ansible.builtin.debug:
    msg: "{{ password | ansible.netcommon.type5_pw(salt='avs') }}"

# Task Output
# -----------
#
# TASK [Set some facts]
# ok: [host] => changed=false
#   ansible_facts:
#     password: cisco@123

# TASK [Filter type5_pw invocation]
# ok: [host] =>
#   msg: $1$avs$uSTOEMh65qzvpb9yBMpzd/
```

### Authors

- Ken Celenza (@itdependsnetworks)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
