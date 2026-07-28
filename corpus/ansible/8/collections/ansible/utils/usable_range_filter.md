---
collection: ansible
version: "8"
title: "ansible.utils.usable_range filter – Expand the usable IP addresses"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/usable_range_filter.html
fetched_at: 2026-07-28T01:10:04+00:00
---
# ansible.utils.usable_range filter – Expand the usable IP addresses

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
> To use it in a playbook, specify: `ansible.utils.usable_range`.

New in ansible.utils 2.3.0

- [Synopsis](usable_range_filter.md#synopsis)
- [Keyword parameters](usable_range_filter.md#keyword-parameters)
- [Examples](usable_range_filter.md#examples)
- [Return Value](usable_range_filter.md#return-value)

## [Synopsis](usable_range_filter.md#id1)

- For a given IP address (IPv4 or IPv6) in CIDR form, the plugin generates a list of usable IP addresses belonging to the network.

## [Keyword parameters](usable_range_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.utils.usable_range(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **ip**  string / required | A string that represents an IP address of network in CIDR form  For example: `10.0.0.0/24` or `2001:db8:abcd:0012::0/124` |

## [Examples](usable_range_filter.md#id3)

```yaml+jinja
#### Simple examples

- name: Expand and produce list of usable IP addresses in 10.0.0.0/28
  ansible.builtin.set_fact:
    data: "{{ '10.0.0.0/28' | ansible.utils.usable_range }}"

# TASK [Expand and produce list of usable IP addresses in 10.0.0.0/28] ************************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": {
#             "number_of_ips": 16,
#             "usable_ips": [
#                 "10.0.0.0",
#                 "10.0.0.1",
#                 "10.0.0.2",
#                 "10.0.0.3",
#                 "10.0.0.4",
#                 "10.0.0.5",
#                 "10.0.0.6",
#                 "10.0.0.7",
#                 "10.0.0.8",
#                 "10.0.0.9",
#                 "10.0.0.10",
#                 "10.0.0.11",
#                 "10.0.0.12",
#                 "10.0.0.13",
#                 "10.0.0.14",
#                 "10.0.0.15"
#             ]
#         }
#     },
#     "changed": false
# }

- name: Expand and produce list of usable IP addresses in 2001:db8:abcd:0012::0/126
  ansible.builtin.set_fact:
    data1: "{{ '2001:db8:abcd:0012::0/126' | ansible.utils.usable_range }}"

# TASK [Expand and produce list of usable IP addresses in 2001:db8:abcd:0012::0/126] ***
# ok: [localhost] => {
#     "ansible_facts": {
#         "data1": {
#             "number_of_ips": 4,
#             "usable_ips": [
#                 "2001:db8:abcd:12::",
#                 "2001:db8:abcd:12::1",
#                 "2001:db8:abcd:12::2",
#                 "2001:db8:abcd:12::3"
#             ]
#         }
#     },
#     "changed": false
# }

- name: Expand and produce list of usable IP addresses in 10.1.1.1
  ansible.builtin.set_fact:
    data: "{{ '10.1.1.1' | ansible.utils.usable_range }}"

# TASK [Expand and produce list of usable IP addresses in 10.1.1.1] ***************************
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": {
#             "number_of_ips": 1,
#             "usable_ips": [
#                 "10.1.1.1"
#             ]
#         }
#     },
#     "changed": false
# }

#### Simple Use-case (looping through the list result)

- name: Expand and produce list of usable IP addresses in 127.0.0.0/28
  ansible.builtin.set_fact:
    data1: "{{ '127.0.0.0/28' | ansible.utils.usable_range }}"

- name: Ping all but first IP addresses from the generated list
  shell: "ping -c 1 {{ item }}"
  loop: "{{ data1.usable_ips[1:] }}"

# TASK [Expand and produce list of usable IP addresses in 127.0.0.0/28] ******************************
# ok: [localhost]

# TASK [Ping all but first IP addresses from the generated list] *************************************
# changed: [localhost] => (item=127.0.0.1)
# changed: [localhost] => (item=127.0.0.2)
# changed: [localhost] => (item=127.0.0.3)
# changed: [localhost] => (item=127.0.0.4)
# changed: [localhost] => (item=127.0.0.5)
# changed: [localhost] => (item=127.0.0.6)
# changed: [localhost] => (item=127.0.0.7)
# changed: [localhost] => (item=127.0.0.8)
# changed: [localhost] => (item=127.0.0.9)
# changed: [localhost] => (item=127.0.0.10)
# changed: [localhost] => (item=127.0.0.11)
# changed: [localhost] => (item=127.0.0.12)
# changed: [localhost] => (item=127.0.0.13)
# changed: [localhost] => (item=127.0.0.14)
# changed: [localhost] => (item=127.0.0.15)
```

## [Return Value](usable_range_filter.md#id4)

| Key | Description |
| --- | --- |
| **data**  string | Total number of usable IP addresses under the key `number_of_ips`  List of usable IP addresses under the key `usable_ips`  **Returned:** success |

### Authors

- Priyam Sahoo (@priyamsahoo)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.utils/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.utils)
