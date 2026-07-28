---
collection: ansible
version: "8"
title: "ansible.utils.ipv4 filter – To filter only Ipv4 addresses Ipv4 filter is used."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/ipv4_filter.html
fetched_at: 2026-07-28T01:09:51+00:00
---
# ansible.utils.ipv4 filter – To filter only Ipv4 addresses Ipv4 filter is used.

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
> To use it in a playbook, specify: `ansible.utils.ipv4`.

New in ansible.utils 2.5.0

- [Synopsis](ipv4_filter.md#synopsis)
- [Keyword parameters](ipv4_filter.md#keyword-parameters)
- [Examples](ipv4_filter.md#examples)
- [Return Value](ipv4_filter.md#return-value)

## [Synopsis](ipv4_filter.md#id1)

- Sometimes you need only IPv4 addresses. To filter only Ipv4 addresses Ipv4 filter is used.

## [Keyword parameters](ipv4_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.utils.ipv4(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **query**  string | You can provide a single argument to each ipv4() filter.  Example. query type ‘ipv6’ to convert ipv4 into ipv6  **Default:** `""` |
| **value**  any / required | list of subnets or individual address or any other values input for ipv4 plugin |

## [Examples](ipv4_filter.md#id3)

```yaml+jinja
#### examples
# Ipv4 filter plugin with different queries.
- name: Set value as input list
  ansible.builtin.set_fact:
    value:
      - 192.24.2.1
      - host.fqdn
      - ::1
      - ''
      - 192.168.32.0/24
      - fe80::100/10
      - 42540766412265424405338506004571095040/64
      - true
- name: IPv4 filter to filter Ipv4 Address
  debug:
    msg: "{{ value|ansible.utils.ipv4 }}"

- name: convert IPv4 addresses into IPv6 addresses.
  debug:
    msg: "{{ value|ansible.utils.ipv4('ipv6') }}"

- name: convert IPv4 addresses into IPv6 addresses.
  debug:
    msg: "{{ value|ansible.utils.ipv4('address') }}"

# PLAY [Ipv4 filter plugin with different queries.] ******************************************************************
# TASK [Set value as input list] ***************************************************************************************
# ok: [localhost] => {"ansible_facts": {"value": ["192.24.2.1", "host.fqdn", "::1", "", "192.168.32.0/24",
# "fe80::100/10", "42540766412265424405338506004571095040/64", true]}, "changed": false}
# TASK [IPv4 filter to filter Ipv4 Address] *******************************************************************
# ok: [localhost] => {
#     "msg": [
#         "192.24.2.1",
#         "192.168.32.0/24"
#     ]
# }
#
# TASK [convert IPv4 addresses into IPv6 addresses.] **********************************************************
# ok: [localhost] => {
#     "msg": [
#         "::ffff:192.24.2.1/128",
#         "::ffff:192.168.32.0/120"
#     ]
# }
#
# TASK [convert IPv4 addresses into IPv6 addresses.] **********************************************************
# ok: [localhost] => {
#     "msg": [
#         "192.24.2.1"
#     ]
# }
```

## [Return Value](ipv4_filter.md#id4)

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
