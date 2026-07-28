---
collection: ansible
version: "8"
title: "ansible.utils.ipcut filter – This filter is designed to get 1st or last few bits of IP address."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/ipcut_filter.html
fetched_at: 2026-07-28T01:09:49+00:00
---
# ansible.utils.ipcut filter – This filter is designed to get 1st or last few bits of IP address.

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
> To use it in a playbook, specify: `ansible.utils.ipcut`.

New in ansible.utils 2.11.0

- [Synopsis](ipcut_filter.md#synopsis)
- [Keyword parameters](ipcut_filter.md#keyword-parameters)
- [Examples](ipcut_filter.md#examples)
- [Return Value](ipcut_filter.md#return-value)

## [Synopsis](ipcut_filter.md#id1)

- This filter is designed to fetch 1st or last few bits of Ip address.

## [Keyword parameters](ipcut_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.utils.ipcut(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **amount**  integer | integer for arithmetic. Example -1,2,3 |
| **value**  string / required | list of subnets or individual address or any other values input for ip_cut plugin |

## [Examples](ipcut_filter.md#id3)

```yaml+jinja
#### examples
- name: Get first 64 bits of Ipv6 address
  debug:
    msg: "{{ '1234:4321:abcd:dcba::17' | ansible.utils.ipcut(64) }}"

- name: Get last 80 bits of Ipv6 address
  debug:
    msg: "{{ '1234:4321:abcd:dcba::17' | ansible.utils.ipcut(-80) }}"
# PLAY [IPCUT filter plugin examples] ************************************************************************************************

# TASK [Get first X bits of Ipv6 address] ********************************************************************************************
# ok: [localhost] => {
#     "msg": "1234:4321:abcd:dcba"
# }

# TASK [Get last X bits of Ipv6 address] *********************************************************************************************
# ok: [localhost] => {
#     "msg": "dcba:0:0:0:17"
# }

# PLAY RECAP *************************************************************************************************************************
# localhost                  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## [Return Value](ipcut_filter.md#id4)

| Key | Description |
| --- | --- |
| **data**  string | Returns result of portion of IP.  **Returned:** success |

### Authors

- Ashwini Mhatre (@amhatre)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.utils/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.utils)
