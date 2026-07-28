---
collection: ansible
version: "8"
title: "community.network.ipadm_ifprop module – Manage IP interface properties on Solaris/illumos systems."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ipadm_ifprop_module.html
fetched_at: 2026-07-28T01:56:59+00:00
---
# community.network.ipadm_ifprop module – Manage IP interface properties on Solaris/illumos systems.

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.ipadm_ifprop`.

- [Synopsis](ipadm_ifprop_module.md#synopsis)
- [Parameters](ipadm_ifprop_module.md#parameters)
- [Examples](ipadm_ifprop_module.md#examples)
- [Return Values](ipadm_ifprop_module.md#return-values)

## [Synopsis](ipadm_ifprop_module.md#id1)

- Modify IP interface properties on Solaris/illumos systems.

Aliases: network.illumos.ipadm_ifprop

## [Parameters](ipadm_ifprop_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **interface**  aliases: nic  string / required | Specifies the IP interface we want to manage. |
| **property**  aliases: name  string / required | Specifies the name of the property we want to manage. |
| **protocol**  string / required | Specifies the protocol for which we want to manage properties. |
| **state**  string | Set or reset the property value.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"reset"` |
| **temporary**  boolean | Specifies that the property value is temporary. Temporary property values do not persist across reboots.  **Choices:**   - `false` ← (default) - `true` |
| **value**  string | Specifies the value we want to set for the property. |

## [Examples](ipadm_ifprop_module.md#id3)

```yaml+jinja
- name: Allow forwarding of IPv4 packets on network interface e1000g0
  community.network.ipadm_ifprop: protocol=ipv4 property=forwarding value=on interface=e1000g0

- name: Temporarily reset IPv4 forwarding property on network interface e1000g0
  community.network.ipadm_ifprop: protocol=ipv4 interface=e1000g0  temporary=true property=forwarding state=reset

- name: Configure IPv6 metric on network interface e1000g0
  community.network.ipadm_ifprop: protocol=ipv6 nic=e1000g0 name=metric value=100

- name: Set IPv6 MTU on network interface bge0
  community.network.ipadm_ifprop: interface=bge0 name=mtu value=1280 protocol=ipv6
```

## [Return Values](ipadm_ifprop_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **interface**  string | interface name we want to set property on  **Returned:** always  **Sample:** `"e1000g0"` |
| **property**  string | property’s name  **Returned:** always  **Sample:** `"mtu"` |
| **protocol**  string | property’s protocol  **Returned:** always  **Sample:** `"ipv4"` |
| **state**  string | state of the target  **Returned:** always  **Sample:** `"present"` |
| **value**  string | property’s value  **Returned:** when value is provided  **Sample:** `"1280"` |

### Authors

- Adam Števko (@xen0l)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
