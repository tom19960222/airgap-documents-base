---
collection: ansible
version: "6"
title: "community.network.slxos_lldp module – Manage LLDP configuration on Extreme Networks SLX-OS network devices."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/slxos_lldp_module.html
fetched_at: 2026-07-27T17:19:45+00:00
---
# community.network.slxos_lldp module – Manage LLDP configuration on Extreme Networks SLX-OS network devices.

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
> To use it in a playbook, specify: `community.network.slxos_lldp`.

- [Synopsis](slxos_lldp_module.md#synopsis)
- [Parameters](slxos_lldp_module.md#parameters)
- [Notes](slxos_lldp_module.md#notes)
- [Examples](slxos_lldp_module.md#examples)
- [Return Values](slxos_lldp_module.md#return-values)

## [Synopsis](slxos_lldp_module.md#id1)

- This module provides declarative management of LLDP service on Extreme SLX-OS network devices.

## [Parameters](slxos_lldp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **state**  string | State of the LLDP configuration. If value is *present* lldp will be enabled else if it is *absent* it will be disabled.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](slxos_lldp_module.md#id3)

> **Note:**
>
> - Tested against SLX-OS 17s.1.02

## [Examples](slxos_lldp_module.md#id4)

```yaml+jinja
- name: Enable LLDP service
  community.network.slxos_lldp:
    state: present

- name: Disable LLDP service
  community.network.slxos_lldp:
    state: absent
```

## [Return Values](slxos_lldp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always, except for the platforms that use Netconf transport to manage the device.  Sample: `["lldp run"]` |

### Authors

- Matthew Stone (@bigmstone)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
