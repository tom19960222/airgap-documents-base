---
collection: ansible
version: "8"
title: "ansible.netcommon.hash_salt filter – The hash_salt filter plugin."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/netcommon/hash_salt_filter.html
fetched_at: 2026-07-28T01:09:19+00:00
---
# ansible.netcommon.hash_salt filter – The hash_salt filter plugin.

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
> To use it in a playbook, specify: `ansible.netcommon.hash_salt`.

New in ansible.netcommon 1.0.0

- [Synopsis](hash_salt_filter.md#synopsis)
- [Keyword parameters](hash_salt_filter.md#keyword-parameters)
- [Notes](hash_salt_filter.md#notes)
- [Examples](hash_salt_filter.md#examples)

## [Synopsis](hash_salt_filter.md#id1)

- The filter plugin produces the salt from a hashed password.
- Using the parameters below - `password | ansible.netcommon.hash_salt(template.yml`)

## [Keyword parameters](hash_salt_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.netcommon.hash_salt(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **password**  string / required | This source data on which hash_salt invokes.  For example `password | ansible.netcommon.hash_salt`, in this case `password` represents the hashed password. |

## [Notes](hash_salt_filter.md#id3)

> **Note:**
>
> - The filter plugin produces the salt from a hashed password.

## [Examples](hash_salt_filter.md#id4)

```yaml+jinja
# Using hash_salt

# playbook

- name: Set the facts
  ansible.builtin.set_fact:
    password: "$1$avs$uSTOEMh65ADDBREAKqzvpb9yBMpzd/"

- name: Invoke hash_salt
  ansible.builtin.debug:
    msg: "{{ password | ansible.netcommon.hash_salt() }}"

# Task Output
# -----------
#
# TASK [Set the facts]
# ok: [host] => changed=false
#   ansible_facts:
#     password: $1$avs$uSTOEMh65ADDBREAKqzvpb9yBMpzd/

# TASK [Invoke hash_salt]
# ok: [host] =>
#   msg: avs
```

### Authors

- Ken Celenza (@itdependsnetworks)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
