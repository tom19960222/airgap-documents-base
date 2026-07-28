---
collection: ansible
version: "6"
title: "infoblox.nios_modules.nios_next_network lookup – Return the next available network range for a network-container"
source_url: https://docs.ansible.com/projects/ansible/6/collections/infoblox/nios_modules/nios_next_network_lookup.html
fetched_at: 2026-07-27T16:43:30+00:00
---
# infoblox.nios_modules.nios_next_network lookup – Return the next available network range for a network-container

> **Note:**
>
> This lookup plugin is part of the [infoblox.nios_modules collection](https://galaxy.ansible.com/infoblox/nios_modules) (version 1.4.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install infoblox.nios_modules`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](nios_next_network_lookup.md#ansible-collections-infoblox-nios-modules-nios-next-network-lookup-requirements) for details.
>
> To use it in a playbook, specify: `infoblox.nios_modules.nios_next_network`.

New in infoblox.nios_modules 1.0.0

- [Synopsis](nios_next_network_lookup.md#synopsis)
- [Requirements](nios_next_network_lookup.md#requirements)
- [Terms](nios_next_network_lookup.md#terms)
- [Keyword parameters](nios_next_network_lookup.md#keyword-parameters)
- [Notes](nios_next_network_lookup.md#notes)
- [Examples](nios_next_network_lookup.md#examples)
- [Return Value](nios_next_network_lookup.md#return-value)

## [Synopsis](nios_next_network_lookup.md#id1)

- Uses the Infoblox WAPI API to return the next available network addresses for a given network CIDR

## [Requirements](nios_next_network_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- infoblox_client

## [Terms](nios_next_network_lookup.md#id3)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | The CIDR network to retrieve the next network from next available network within the specified container. |

## [Keyword parameters](nios_next_network_lookup.md#id4)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('infoblox.nios_modules.nios_next_network', key1=value1, key2=value2, ...)` and `query('infoblox.nios_modules.nios_next_network', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **cidr**  string / required | The CIDR of the network to retrieve the next network from next available network within the specified container. Also, Requested CIDR must be specified and greater than the parent CIDR. |
| **exclude**  list / elements=string | Network addresses returned from network-container excluding list of user’s input network range.  Default: `[""]` |
| **network_view**  string | The network view to retrieve the CIDR network from.  Default: `"default"` |
| **num**  integer | The number of network addresses to return from network-container.  Default: `1` |

## [Notes](nios_next_network_lookup.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('infoblox.nios_modules.nios_next_network', term1, term2, key1=value1, key2=value2)` and `query('infoblox.nios_modules.nios_next_network', term1, term2, key1=value1, key2=value2)`

## [Examples](nios_next_network_lookup.md#id6)

```yaml+jinja
- name: return next available network for network-container 192.168.10.0/24
  ansible.builtin.set_fact:
    networkaddr: "{{ lookup('infoblox.nios_modules.nios_next_network', '192.168.10.0/24', cidr=25,
                        provider={'host': 'nios01', 'username': 'admin', 'password': 'password'}) }}"

- name: return next available network for network-container 192.168.10.0/24 in a non-default network view
  ansible.builtin.set_fact:
    networkaddr: "{{ lookup('infoblox.nios_modules.nios_next_network', '192.168.10.0/24', cidr=25, network_view='ansible'
                        provider={'host': 'nios01', 'username': 'admin', 'password': 'password'}) }}"

- name: return the next 2 available network addresses for network-container 192.168.10.0/24
  ansible.builtin.set_fact:
    networkaddr: "{{ lookup('infoblox.nios_modules.nios_next_network', '192.168.10.0/24', cidr=25, num=2,
                        provider={'host': 'nios01', 'username': 'admin', 'password': 'password'}) }}"

- name: return the available network addresses for network-container 192.168.10.0/24 excluding network range '192.168.10.0/25'
  ansible.builtin.set_fact:
    networkaddr: "{{ lookup('infoblox.nios_modules.nios_next_network', '192.168.10.0/24', cidr=25, exclude=['192.168.10.0/25'],
                        provider={'host': 'nios01', 'username': 'admin', 'password': 'password'}) }}"
```

## [Return Value](nios_next_network_lookup.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | The list of next network addresses available  Returned: always |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/infobloxopen/infoblox-ansible/issues)
[Homepage](https://github.com/infobloxopen/infoblox-ansible)
[Repository (Sources)](https://github.com/infobloxopen/infoblox-ansible/tree/master)
