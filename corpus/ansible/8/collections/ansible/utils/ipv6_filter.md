---
collection: ansible
version: "8"
title: "ansible.utils.ipv6 filter – To filter only Ipv6 addresses Ipv6 filter is used."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/ipv6_filter.html
fetched_at: 2026-07-28T01:09:52+00:00
---
# ansible.utils.ipv6 filter – To filter only Ipv6 addresses Ipv6 filter is used.

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
> To use it in a playbook, specify: `ansible.utils.ipv6`.

New in ansible.utils 2.5.0

- [Synopsis](ipv6_filter.md#synopsis)
- [Keyword parameters](ipv6_filter.md#keyword-parameters)
- [Examples](ipv6_filter.md#examples)
- [Return Value](ipv6_filter.md#return-value)

## [Synopsis](ipv6_filter.md#id1)

- Sometimes you need only IPv6 addresses. To filter only Ipv6 addresses Ipv6 filter is used.

## [Keyword parameters](ipv6_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.utils.ipv6(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **query**  string | You can provide a single argument to each ipv6() filter.  Example. query type ‘ipv4’ to convert ipv6 into ipv4  **Default:** `""` |
| **value**  any / required | list of subnets or individual address or any other values input for ipv6 plugin |

## [Examples](ipv6_filter.md#id3)

```yaml+jinja
#### examples
# Ipv6 filter plugin with different queries.
- name: Set value as input list
  ansible.builtin.set_fact:
    value:
      - 192.24.2.1
      - ::ffff:192.168.32.0/120
      - ''
      - ::ffff:192.24.2.1/128
      - 192.168.32.0/24
      - fe80::100/10
      - true
- name: IPv6 filter to filter Ipv6 Address
  debug:
    msg: "{{ value|ansible.utils.ipv6 }}"

- name: convert IPv6 addresses into IPv4 addresses.
  debug:
    msg: "{{ value|ansible.utils.ipv6('ipv4') }}"

- name: filter only  IPv6 addresses.
  debug:
    msg: "{{ value|ansible.utils.ipv6('address') }}"

# PLAY [Ipv6 filter plugin with different queries.] ******************************************************************
# TASK [Set value as input list] ***************************************************************************************
# ok: [localhost] => {
#     "ansible_facts": {
#         "value": [
#             "192.24.2.1",
#             "::ffff:192.168.32.0/120",
#             "",
#             "::ffff:192.24.2.1/128",
#             "192.168.32.0/24",
#             "fe80::100/10",
#             true
#         ]
#     },
#     "changed": false
# }
#
# TASK [IPv6 filter to filter Ipv6 Address] ****************************************************************************
# ok: [localhost] => {
#     "msg": [
#         "::ffff:192.168.32.0/120",
#         "::ffff:192.24.2.1/128",
#         "fe80::100/10"
#     ]
# }
#
# TASK [convert IPv6 addresses into IPv4 addresses.] *******************************************************************
# ok: [localhost] => {
#     "msg": [
#         "192.168.32.0/24",
#         "192.24.2.1/32"
#     ]
# }
#
# TASK [filter only  IPv6 addresses] *******************************************************************
# ok: [localhost] => {
#     "msg": [
#         "::ffff:192.168.32.0",
#         "::ffff:192.24.2.1",
#         "fe80::100"
#     ]
# }
#
```

## [Return Value](ipv6_filter.md#id4)

| Key | Description |
| --- | --- |
| **data**  any | Returns values valid for a particular query.  **Returned:** success |

### Authors

- Ashwini Mhatre (@amhatre)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.utils/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.utils)
