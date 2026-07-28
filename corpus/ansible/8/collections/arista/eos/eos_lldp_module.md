---
collection: ansible
version: "8"
title: "arista.eos.eos_lldp module – Manage LLDP configuration on Arista EOS network devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/arista/eos/eos_lldp_module.html
fetched_at: 2026-07-28T01:11:06+00:00
---
# arista.eos.eos_lldp module – Manage LLDP configuration on Arista EOS network devices

> **Note:**
>
> This module is part of the [arista.eos collection](https://galaxy.ansible.com/ui/repo/published/arista/eos/) (version 6.2.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install arista.eos`.
>
> To use it in a playbook, specify: `arista.eos.eos_lldp`.

New in arista.eos 1.0.0

- [Synopsis](eos_lldp_module.md#synopsis)
- [Parameters](eos_lldp_module.md#parameters)
- [Notes](eos_lldp_module.md#notes)
- [Examples](eos_lldp_module.md#examples)
- [Return Values](eos_lldp_module.md#return-values)

## [Synopsis](eos_lldp_module.md#id1)

- This module provides declarative management of LLDP service on Arista EOS network devices.

Aliases: lldp

## [Parameters](eos_lldp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **state**  string | State of the LLDP configuration. If value is *present* lldp will be enabled else if it is *absent* it will be disabled.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"enabled"` - `"disabled"` |

## [Notes](eos_lldp_module.md#id3)

> **Note:**
>
> - Tested against Arista EOS 4.24.6F

## [Examples](eos_lldp_module.md#id4)

```yaml+jinja
- name: Enable LLDP service
  arista.eos.eos_lldp:
    state: present

- name: Disable LLDP service
  arista.eos.eos_lldp:
    state: absent
```

## [Return Values](eos_lldp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  **Returned:** always, except for the platforms that use Netconf transport to manage the device.  **Sample:** `["lldp run"]` |

### Authors

- Ganesh Nalawade (@ganeshrn)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/arista.eos)
