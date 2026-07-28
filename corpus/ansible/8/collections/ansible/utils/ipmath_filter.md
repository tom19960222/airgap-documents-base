---
collection: ansible
version: "8"
title: "ansible.utils.ipmath filter – This filter is designed to do simple IP math/arithmetic."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/ipmath_filter.html
fetched_at: 2026-07-28T01:09:50+00:00
---
# ansible.utils.ipmath filter – This filter is designed to do simple IP math/arithmetic.

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
> To use it in a playbook, specify: `ansible.utils.ipmath`.

New in ansible.utils 2.5.0

- [Synopsis](ipmath_filter.md#synopsis)
- [Keyword parameters](ipmath_filter.md#keyword-parameters)
- [Examples](ipmath_filter.md#examples)
- [Return Value](ipmath_filter.md#return-value)

## [Synopsis](ipmath_filter.md#id1)

- This filter is designed to do simple IP math/arithmetic.

## [Keyword parameters](ipmath_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.utils.ipmath(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **amount**  integer | integer for arithmetic. Example -1,2,3 |
| **value**  string / required | list of subnets or individual address or any other values input for ipaddr plugin |

## [Examples](ipmath_filter.md#id3)

```yaml+jinja
#### examples
# Ipmath filter plugin with different arthmetic.
# Get the next fifth address based on an IP address
- debug:
    msg: "{{ '192.168.1.5' | ansible.netcommon.ipmath(5) }}"

# Get the tenth previous address based on an IP address
- debug:
    msg: "{{ '192.168.1.5' | ansible.netcommon.ipmath(-10) }}"

# Get the next fifth address using CIDR notation
- debug:
    msg: "{{ '192.168.1.1/24' | ansible.netcommon.ipmath(5) }}"

# Get the previous fifth address using CIDR notation
- debug:
    msg: "{{ '192.168.1.6/24' | ansible.netcommon.ipmath(-5) }}"

# Get the previous tenth address using cidr notation
# It returns a address of the previous network range
- debug:
    msg: "{{ '192.168.2.6/24' | ansible.netcommon.ipmath(-10) }}"

# Get the next tenth address in IPv6
- debug:
    msg: "{{ '2001::1' | ansible.netcommon.ipmath(10) }}"

# Get the previous tenth address in IPv6
- debug:
    msg: "{{ '2001::5' | ansible.netcommon.ipmath(-10) }}"

# TASK [debug] **********************************************************************************************************
# ok: [localhost] => {
#     "msg": "192.168.1.10"
# }
#
# TASK [debug] **********************************************************************************************************
# ok: [localhost] => {
#     "msg": "192.168.0.251"
# }
#
# TASK [debug] **********************************************************************************************************
# ok: [localhost] => {
#     "msg": "192.168.1.6"
# }
#
# TASK [debug] **********************************************************************************************************
# ok: [localhost] => {
#     "msg": "192.168.1.1"
# }
#
# TASK [debug] **********************************************************************************************************
# ok: [localhost] => {
#     "msg": "192.168.1.252"
# }
#
# TASK [debug] **********************************************************************************************************
# ok: [localhost] => {
#     "msg": "2001::b"
# }
#
# TASK [debug] **********************************************************************************************************
# ok: [localhost] => {
#     "msg": "2000:ffff:ffff:ffff:ffff:ffff:ffff:fffb"
# }
```

## [Return Value](ipmath_filter.md#id4)

| Key | Description |
| --- | --- |
| **data**  string | Returns result of IP math/arithmetic.  **Returned:** success |

### Authors

- Ashwini Mhatre (@amhatre)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.utils/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.utils)
