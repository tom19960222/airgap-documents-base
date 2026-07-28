---
collection: ansible
version: "8"
title: "ansible.utils.network_in_usable filter – The network_in_usable filter returns whether an address passed as an argument is usable in a network."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/network_in_usable_filter.html
fetched_at: 2026-07-28T01:09:56+00:00
---
# ansible.utils.network_in_usable filter – The network_in_usable filter returns whether an address passed as an argument is usable in a network.

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
> To use it in a playbook, specify: `ansible.utils.network_in_usable`.

New in ansible.utils 2.5.0

- [Synopsis](network_in_usable_filter.md#synopsis)
- [Keyword parameters](network_in_usable_filter.md#keyword-parameters)
- [Examples](network_in_usable_filter.md#examples)
- [Return Value](network_in_usable_filter.md#return-value)

## [Synopsis](network_in_usable_filter.md#id1)

- The network_in_usable filter returns whether an address passed as an argument is usable in a network Usable addresses are addresses that can be assigned to a host.
- The network ID and the broadcast address are not usable addresses.

## [Keyword parameters](network_in_usable_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.utils.network_in_usable(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **test**  string | The address or network is usable or not. |
| **value**  string / required | The network address or range to test against. |

## [Examples](network_in_usable_filter.md#id3)

```yaml+jinja
#### examples
- name: Check ip address is usable in a network
  debug:
    msg: "{{ '192.168.0.0/24' | ansible.utils.network_in_usable( '192.168.0.1' ) }}"

- name: Check broadcast address is usable in a network
  debug:
    msg: "{{ '192.168.0.0/24' | ansible.utils.network_in_usable( '192.168.0.255' ) }}"

- name: Check in a network is part of another network.
  debug:
    msg: "{{ '192.168.0.0/16' | ansible.utils.network_in_usable( '192.168.0.255' ) }}"

# TASK [Check ip address is usable in a network] **************************************************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_network_in_usable.yaml:7
# Loading collection ansible.utils from /Users/amhatre/ansible-collections/collections/ansible_collections/ansible/utils
# ok: [localhost] => {
#     "msg": true
# }
#
# TASK [Check broadcast address is usable in a network] *******************************************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_network_in_usable.yaml:11
# Loading collection ansible.utils from /Users/amhatre/ansible-collections/collections/ansible_collections/ansible/utils
# ok: [localhost] => {
#     "msg": false
# }
#
# TASK [Check in a network is part of another network.] *******************************************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_network_in_usable.yaml:15
# Loading collection ansible.utils from /Users/amhatre/ansible-collections/collections/ansible_collections/ansible/utils
# ok: [localhost] => {
#     "msg": true
# }
```

## [Return Value](network_in_usable_filter.md#id4)

| Key | Description |
| --- | --- |
| **data**  boolean | Returns whether an address or a network passed as argument is in a network.  **Returned:** success |

### Authors

- Ashwini Mhatre (@amhatre)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.utils/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.utils)
