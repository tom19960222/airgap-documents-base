---
collection: ansible
version: "8"
title: "ansible.utils.ipv6 test – Test if something is an IPv6 address or network"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/ipv6_test.html
fetched_at: 2026-07-28T01:10:14+00:00
---
# ansible.utils.ipv6 test – Test if something is an IPv6 address or network

> **Note:**
>
> This test plugin is part of the [ansible.utils collection](https://galaxy.ansible.com/ui/repo/published/ansible/utils/) (version 2.12.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.utils`.
>
> To use it in a playbook, specify: `ansible.utils.ipv6`.

New in ansible.utils 2.2.0

- [Synopsis](ipv6_test.md#synopsis)
- [Keyword parameters](ipv6_test.md#keyword-parameters)
- [Examples](ipv6_test.md#examples)
- [Return Value](ipv6_test.md#return-value)

## [Synopsis](ipv6_test.md#id1)

- This plugin checks if the provided value is a valid host or network IP address with IPv6 addressing scheme

## [Keyword parameters](ipv6_test.md#id2)

This describes keyword parameters of the test. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `input is ansible.utils.ipv6(key1=value1, key2=value2, ...)` and `input is not ansible.utils.ipv6(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **ip**  string / required | A string that represents the value against which the test is going to be performed  For example: `10.1.1.1`, `10.0.0.0/8`, or `fe80::216:3eff:fee4:16f3` |

## [Examples](ipv6_test.md#id3)

```yaml+jinja
#### Simple examples

- name: Check if fe80::216:3eff:fee4:16f3 is a valid IPv6 address
  ansible.builtin.set_fact:
    data: "{{ 'fe80::216:3eff:fee4:16f3' is ansible.utils.ipv6 }}"

# TASK [Check if fe80::216:3eff:fee4:16f3 is a valid IPv6 address] *************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }

- name: Check if 2001:db8:a::/64 is a valid IPv6 address
  ansible.builtin.set_fact:
    data: "{{ '2001:db8:a::/64' is ansible.utils.ipv6 }}"

# TASK [Check if 2001:db8:a::/64 is a valid IPv6 address] **********************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }

- name: Check if 192.169.1.250 is not a valid IPv6 address
  ansible.builtin.set_fact:
    data: "{{ '192.169.1.250' is not ansible.utils.ipv6 }}"

# TASK [Check if 192.169.1.250 is not a valid IPv6 address] ********************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": true
#     },
#     "changed": false
# }
```

## [Return Value](ipv6_test.md#id4)

| Key | Description |
| --- | --- |
| **data**  string | If jinja test satisfies plugin expression `true`  If jinja test does not satisfy plugin expression `false`  **Returned:** success |

### Authors

- Priyam Sahoo (@priyamsahoo)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.utils/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.utils)
