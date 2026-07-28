---
collection: ansible
version: "8"
title: "community.network.dladm_linkprop module – Manage link properties on Solaris/illumos systems."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/dladm_linkprop_module.html
fetched_at: 2026-07-28T01:56:26+00:00
---
# community.network.dladm_linkprop module – Manage link properties on Solaris/illumos systems.

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
> To use it in a playbook, specify: `community.network.dladm_linkprop`.

- [Synopsis](dladm_linkprop_module.md#synopsis)
- [Parameters](dladm_linkprop_module.md#parameters)
- [Examples](dladm_linkprop_module.md#examples)
- [Return Values](dladm_linkprop_module.md#return-values)

## [Synopsis](dladm_linkprop_module.md#id1)

- Set / reset link properties on Solaris/illumos systems.

Aliases: network.illumos.dladm_linkprop

## [Parameters](dladm_linkprop_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **link**  aliases: nic, interface  string / required | Link interface name. |
| **property**  aliases: name  string / required | Specifies the name of the property we want to manage. |
| **state**  string | Set or reset the property value.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"reset"` |
| **temporary**  boolean | Specifies that lin property configuration is temporary. Temporary link property configuration does not persist across reboots.  **Choices:**   - `false` ← (default) - `true` |
| **value**  string | Specifies the value we want to set for the link property. |

## [Examples](dladm_linkprop_module.md#id3)

```yaml+jinja
- name: Set 'maxbw' to 100M on e1000g1
  community.network.dladm_linkprop: name=e1000g1 property=maxbw value=100M state=present

- name: Set 'mtu' to 9000 on e1000g1
  community.network.dladm_linkprop: name=e1000g1 property=mtu value=9000

- name: Reset 'mtu' property on e1000g1
  community.network.dladm_linkprop: name=e1000g1 property=mtu state=reset
```

## [Return Values](dladm_linkprop_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **link**  string | link name  **Returned:** always  **Sample:** `"e100g0"` |
| **property**  string | property name  **Returned:** always  **Sample:** `"mtu"` |
| **state**  string | state of the target  **Returned:** always  **Sample:** `"present"` |
| **temporary**  boolean | specifies if operation will persist across reboots  **Returned:** always  **Sample:** `true` |
| **value**  string | property value  **Returned:** always  **Sample:** `"9000"` |

### Authors

- Adam Števko (@xen0l)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
