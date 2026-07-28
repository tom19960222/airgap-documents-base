---
collection: ansible
version: "6"
title: "community.network.cnos_lldp module – Manage LLDP configuration on Lenovo CNOS network devices."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/cnos_lldp_module.html
fetched_at: 2026-07-27T17:18:12+00:00
---
# community.network.cnos_lldp module – Manage LLDP configuration on Lenovo CNOS network devices.

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
> To use it in a playbook, specify: `community.network.cnos_lldp`.

- [Synopsis](cnos_lldp_module.md#synopsis)
- [Parameters](cnos_lldp_module.md#parameters)
- [Notes](cnos_lldp_module.md#notes)
- [Examples](cnos_lldp_module.md#examples)
- [Return Values](cnos_lldp_module.md#return-values)

## [Synopsis](cnos_lldp_module.md#id1)

- This module provides declarative management of LLDP service on Lenovc CNOS network devices.

## [Parameters](cnos_lldp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **state**  string | State of the LLDP configuration. If value is *present* lldp will be enabled else if it is *absent* it will be disabled.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](cnos_lldp_module.md#id3)

> **Note:**
>
> - Tested against CNOS 10.9.1

## [Examples](cnos_lldp_module.md#id4)

```yaml+jinja
- name: Enable LLDP service
  community.network.cnos_lldp:
    state: present

- name: Disable LLDP service
  community.network.cnos_lldp:
    state: absent
```

## [Return Values](cnos_lldp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always, except for the platforms that use Netconf transport to manage the device.  Sample: `["lldp timer 1024", "lldp trap-interval 330"]` |

### Authors

- Anil Kumar Muraleedharan (@amuraleedhar)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
