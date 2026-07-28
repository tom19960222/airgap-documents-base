---
collection: ansible
version: "6"
title: "community.network.ipadm_addrprop module – Manage IP address properties on Solaris/illumos systems."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ipadm_addrprop_module.html
fetched_at: 2026-07-27T17:18:53+00:00
---
# community.network.ipadm_addrprop module – Manage IP address properties on Solaris/illumos systems.

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.ipadm_addrprop`.

- [Synopsis](ipadm_addrprop_module.md#synopsis)
- [Parameters](ipadm_addrprop_module.md#parameters)
- [Examples](ipadm_addrprop_module.md#examples)
- [Return Values](ipadm_addrprop_module.md#return-values)

## [Synopsis](ipadm_addrprop_module.md#id1)

- Modify IP address properties on Solaris/illumos systems.

## [Parameters](ipadm_addrprop_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **addrobj**  aliases: nic, interface  string / required | Specifies the address object we want to manage. |
| **property**  aliases: name  string / required | Specifies the name of the address property we want to manage. |
| **state**  string | Set or reset the property value.  Choices:   - `"present"` ← (default) - `"absent"` - `"reset"` |
| **temporary**  boolean | Specifies that the address property value is temporary. Temporary values do not persist across reboots.  Choices:   - `false` ← (default) - `true` |
| **value**  string | Specifies the value we want to set for the address property. |

## [Examples](ipadm_addrprop_module.md#id3)

```yaml+jinja
- name: Mark address on addrobj as deprecated
  community.network.ipadm_addrprop: property=deprecated value=on addrobj=e1000g0/v6

- name: Set network prefix length for addrobj
  community.network.ipadm_addrprop: addrobj=bge0/v4 name=prefixlen value=26
```

## [Return Values](ipadm_addrprop_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **addrobj**  string | address object name  Returned: always  Sample: `"bge0/v4"` |
| **property**  string | property name  Returned: always  Sample: `"deprecated"` |
| **state**  string | state of the target  Returned: always  Sample: `"present"` |
| **temporary**  boolean | specifies if operation will persist across reboots  Returned: always  Sample: `true` |
| **value**  string | property value  Returned: when value is provided  Sample: `"26"` |

### Authors

- Adam Števko (@xen0l)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
