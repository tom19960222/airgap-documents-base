---
collection: ansible
version: "8"
title: "ansible.netcommon.comp_type5 filter – The comp_type5 filter plugin."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/netcommon/comp_type5_filter.html
fetched_at: 2026-07-28T01:09:19+00:00
---
# ansible.netcommon.comp_type5 filter – The comp_type5 filter plugin.

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
> To use it in a playbook, specify: `ansible.netcommon.comp_type5`.

New in ansible.netcommon 1.0.0

- [Synopsis](comp_type5_filter.md#synopsis)
- [Keyword parameters](comp_type5_filter.md#keyword-parameters)
- [Notes](comp_type5_filter.md#notes)
- [Examples](comp_type5_filter.md#examples)

## [Synopsis](comp_type5_filter.md#id1)

- The filter confirms configuration idempotency on use of type5_pw.

## [Keyword parameters](comp_type5_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.netcommon.comp_type5(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **encrypted_password**  string / required | The encrypted text. |
| **return_original**  boolean | Return the original text.  **Choices:**   - `false` - `true` |
| **unencrypted_password**  string / required | The unencrypted text. |

## [Notes](comp_type5_filter.md#id3)

> **Note:**
>
> - The filter confirms configuration idempotency on use of type5_pw.
> - Can be used to validate password post hashing username cisco secret 5 {{ ansible_ssh_pass | ansible.netcommon.comp_type5(encrypted, True) }}

## [Examples](comp_type5_filter.md#id4)

```yaml+jinja
# Using comp_type5

# playbook

- name: Set the facts
  ansible.builtin.set_fact:
    unencrypted_password: "cisco@123"
    encrypted_password: "$1$avs$uSTOEMh65ADDBREAKqzvpb9yBMpzd/"

- name: Invoke comp_type5
  ansible.builtin.debug:
    msg: "{{ unencrypted_password | ansible.netcommon.comp_type5(encrypted_password, False) }}"

# Task Output
# -----------
#
# TASK [Set the facts]
# ok: [35.155.113.92] => changed=false
#   ansible_facts:
#     encrypted_password: $1$avs$uSTOEMh65ADDBREAKqzvpb9yBMpzd/
#     unencrypted_password: cisco@123

# TASK [Invoke comp_type5]
# ok: [35.155.113.92] =>
#   msg: true
```

### Authors

- Ken Celenza (@itdependsnetworks)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
