---
collection: ansible
version: "8"
title: "ansible.utils.ipwrap filter – This filter is designed to Wrap IPv6 addresses in [ ] brackets."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/ipwrap_filter.html
fetched_at: 2026-07-28T01:09:53+00:00
---
# ansible.utils.ipwrap filter – This filter is designed to Wrap IPv6 addresses in [ ] brackets.

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
> To use it in a playbook, specify: `ansible.utils.ipwrap`.

New in ansible.utils 2.5.0

- [Synopsis](ipwrap_filter.md#synopsis)
- [Keyword parameters](ipwrap_filter.md#keyword-parameters)
- [Examples](ipwrap_filter.md#examples)
- [Return Value](ipwrap_filter.md#return-value)

## [Synopsis](ipwrap_filter.md#id1)

- Some configuration files require IPv6 addresses to be “wrapped” in square brackets ([ ]).To accomplish that,
- you can use the ipwrap() filter.It will wrap all IPv6 addresses and leave any other strings intact.

## [Keyword parameters](ipwrap_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.utils.ipwrap(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **query**  string | You can provide a single argument to each ipwrap() filter.  The filter will then treat it as a query and return values modified by that query.  **Default:** `""` |
| **value**  any / required | list of subnets or individual address or any other values input. Example. [‘192.24.2.1’, ‘host.fqdn’, ‘::1’, ‘192.168.32.0/24’, ‘fe80::100/10’, True, ‘’, ‘42540766412265424405338506004571095040/64’] |

## [Examples](ipwrap_filter.md#id3)

```yaml+jinja
#### examples
# Ipwrap filter plugin o Wrap IPv6 addresses in [ ] brackets.
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
    msg: "{{ value|ansible.utils.ipwrap }}"

- name: |
        ipwrap() did not filter out non-IP address values, which is usually what you want when for example
        you are mixing IP addresses with hostnames. If you still want to filter out all non-IP address values,
        you can chain both filters together.
  debug:
    msg: "{{ value|ansible.utils.ipaddr|ansible.utils.ipwrap  }}"

# PLAY [Ipwrap filter plugin o Wrap IPv6 addresses in [ ] brackets.] ***************************************************
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
# TASK [debug] ************************************************************************************************
# ok: [localhost] => {
#     "msg": [
#         "192.24.2.1",
#         "host.fqdn",
#         "[::1]",
#         "",
#         "192.168.32.0/24",
#         "[fe80::100]/10",
#         "[2001:db8:32c:faad::]/64",
#         "True"
#     ]
# }
#
# TASK [ipwrap() did not filter out non-IP address values, which is usually what you want when for example
# you are mixing IP addresses with hostnames. If you still want to filter out all non-IP address values,
# you can chain both filters together.] ***
# ok: [localhost] => {
#     "msg": [
#         "192.24.2.1",
#         "[::1]",
#         "192.168.32.0/24",
#         "[fe80::100]/10",
#         "[2001:db8:32c:faad::]/64"
#     ]
# }
```

## [Return Value](ipwrap_filter.md#id4)

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
