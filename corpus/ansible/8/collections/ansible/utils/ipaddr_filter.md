---
collection: ansible
version: "8"
title: "ansible.utils.ipaddr filter – This filter is designed to return the input value if a query is True, else False."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/ipaddr_filter.html
fetched_at: 2026-07-28T01:09:48+00:00
---
# ansible.utils.ipaddr filter – This filter is designed to return the input value if a query is True, else False.

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
> To use it in a playbook, specify: `ansible.utils.ipaddr`.

New in ansible.utils 2.5.0

- [Synopsis](ipaddr_filter.md#synopsis)
- [Keyword parameters](ipaddr_filter.md#keyword-parameters)
- [Examples](ipaddr_filter.md#examples)
- [Return Value](ipaddr_filter.md#return-value)

## [Synopsis](ipaddr_filter.md#id1)

- This filter is designed to return the input value if a query is True, and False if a query is False
- This way it can be easily used in chained filters

## [Keyword parameters](ipaddr_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.utils.ipaddr(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **alias**  string | type of filter. example ipaddr, ipv4, ipv6, ipwrap |
| **query**  string | You can provide a single argument to each ipaddr() filter.  The filter will then treat it as a query and return values modified by that query.  Types of queries include: 1. query by name: ansible.utils.ipaddr(‘address’), ansible.utils.ipv4(‘network’); 2. query by CIDR range: ansible.utils.ipaddr(‘192.168.0.0/24’), ansible.utils.ipv6(‘2001:db8::/32’); 3. query by index number: ansible.utils.ipaddr(‘1’), ansible.utils.ipaddr(‘-1’);  **Default:** `""` |
| **value**  any / required | list of subnets or individual address or any other values input for ipaddr plugin |
| **version**  integer | Ip version 4 or 6 |

## [Examples](ipaddr_filter.md#id3)

```yaml+jinja
#### examples
# Ipaddr filter plugin with different queries.
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
- debug:
    msg: "{{ value|ansible.utils.ipaddr }}"

- name: Fetch only those elements that are host IP addresses and not network ranges
  debug:
    msg: "{{ value|ansible.utils.ipaddr('address') }}"

- name: |
    Fetch only host IP addresses with their correct CIDR prefixes (as is common with IPv6 addressing), you can use
    the ipaddr('host') filter.
  debug:
    msg: "{{ value|ansible.utils.ipaddr('host') }}"

- name: check if IP addresses or network ranges are accessible on a public Internet and return it.
  debug:
    msg: "{{ value|ansible.utils.ipaddr('public') }}"

- name: check if IP addresses or network ranges are accessible on a private Internet and return it.
  debug:
    msg: "{{ value|ansible.utils.ipaddr('private') }}"

- name: check which values are values are specifically network ranges and return it.
  debug:
    msg: "{{ value|ansible.utils.ipaddr('net') }}"

- name: check how many IP addresses can be in a certain range.
  debug:
    msg: "{{ value| ansible.utils.ipaddr('net') | ansible.utils.ipaddr('size') }}"

- name: By specifying a network range as a query, you can check if a given value is in that range.
  debug:
    msg: "{{ value|ansible.utils.ipaddr('192.0.0.0/8') }}"

# First IP address (network address)
- name: |
    If you specify a positive or negative integer as a query, ipaddr() will treat this as an index and will return
    the specific IP address from a network range, in the "host/prefix" format.
  debug:
    msg: "{{ value| ansible.utils.ipaddr('net') | ansible.utils.ipaddr('0') }}"

# Second IP address (usually the gateway host)
- debug:
    msg: "{{ value| ansible.utils.ipaddr('net') | ansible.utils.ipaddr('1') }}"

# Last IP address (the broadcast address in IPv4 networks)
- debug:
    msg: "{{ value| ansible.utils.ipaddr('net') | ansible.utils.ipaddr('-1') }}"

# PLAY [Ipaddr filter plugin with different queries.] ******************************************************************
# TASK [Set value as input list] ***************************************************************************************
# ok: [localhost] => {"ansible_facts": {"value": ["192.24.2.1", "host.fqdn", "::1", "", "192.168.32.0/24",
# "fe80::100/10", "42540766412265424405338506004571095040/64", true]}, "changed": false}
#
# TASK [debug] ********************************************************************************************************
# ok: [localhost] => {
#     "msg": [
#         "192.24.2.1",
#         "::1",
#         "192.168.32.0/24",
#         "fe80::100/10",
#         "2001:db8:32c:faad::/64"
#     ]
# }
#
# TASK [Fetch only those elements that are host IP addresses and not network ranges] ***********************************
# ok: [localhost] => {
#     "msg": [
#         "192.24.2.1",
#         "::1",
#         "fe80::100",
#         "2001:db8:32c:faad::"
#     ]
# }
#
# TASK [Fetch only host IP addresses with their correct CIDR prefixes (as is common with IPv6 addressing), you can use
# the ipaddr('host') filter.] *****************
# ok: [localhost] => {
#     "msg": [
#         "192.24.2.1/32",
#         "::1/128",
#         "fe80::100/10"
#     ]
# }
#
# TASK [check if IP addresses or network ranges are accessible on a public Internet and return it.] ********************
# ok: [localhost] => {
#     "msg": [
#         "192.24.2.1",
#         "2001:db8:32c:faad::/64"
#     ]
# }
#
# TASK [check if IP addresses or network ranges are accessible on a private Internet and return it.] *******************
# ok: [localhost] => {
#     "msg": [
#         "192.168.32.0/24",
#         "fe80::100/10"
#     ]
# }
#
# TASK [check which values are values are specifically network ranges and return it.] **********************************
# ok: [localhost] => {
#     "msg": [
#         "192.168.32.0/24",
#         "2001:db8:32c:faad::/64"
#     ]
# }
#
# TASK [check how many IP addresses can be in a certain range.] *********************************************************
# ok: [localhost] => {
#     "msg": [
#         256,
#         18446744073709551616
#     ]
# }
#
# TASK [By specifying a network range as a query, you can check if a given value is in that range.] ********************
# ok: [localhost] => {
#     "msg": [
#         "192.24.2.1",
#         "192.168.32.0/24"
#     ]
# }
#
# TASK [If you specify a positive or negative integer as a query, ipaddr() will treat this as an index and will
# return the specific IP address from a network range, in the "host/prefix" format.] ***
# ok: [localhost] => {
#     "msg": [
#         "192.168.32.0/24",
#         "2001:db8:32c:faad::/64"
#     ]
# }
#
# TASK [debug] *********************************************************************************************************
# ok: [localhost] => {
#     "msg": [
#         "192.168.32.1/24",
#         "2001:db8:32c:faad::1/64"
#     ]
# }
#
# TASK [debug] ********************************************************************************************************
# ok: [localhost] => {
#     "msg": [
#         "192.168.32.255/24",
#         "2001:db8:32c:faad:ffff:ffff:ffff:ffff/64"
#     ]
# }
```

## [Return Value](ipaddr_filter.md#id4)

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
