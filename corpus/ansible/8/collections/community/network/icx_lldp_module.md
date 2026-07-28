---
collection: ansible
version: "8"
title: "community.network.icx_lldp module – Manage LLDP configuration on Ruckus ICX 7000 series switches"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/icx_lldp_module.html
fetched_at: 2026-07-28T01:56:50+00:00
---
# community.network.icx_lldp module – Manage LLDP configuration on Ruckus ICX 7000 series switches

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
> To use it in a playbook, specify: `community.network.icx_lldp`.

- [Synopsis](icx_lldp_module.md#synopsis)
- [Parameters](icx_lldp_module.md#parameters)
- [Notes](icx_lldp_module.md#notes)
- [Examples](icx_lldp_module.md#examples)
- [Return Values](icx_lldp_module.md#return-values)

## [Synopsis](icx_lldp_module.md#id1)

- This module provides declarative management of LLDP service on ICX network devices.

Aliases: network.icx.icx_lldp

## [Parameters](icx_lldp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **check_running_config**  boolean | Check running configuration. This can be set as environment variable. Module will use environment variable value(default:True), unless it is overridden, by specifying it as module parameter.  **Choices:**   - `false` - `true` ← (default) |
| **interfaces**  list / elements=string | specify interfaces |
| **name**  list / elements=string | List of ethernet ports to enable lldp. To add a range of ports use ‘to’ keyword. See the example. |
| **state**  string | State of lldp configuration for interfaces  **Choices:**   - `"present"` - `"absent"` - `"enabled"` - `"disabled"` |
| **state**  string | Enables the receipt and transmission of Link Layer Discovery Protocol (LLDP) globally.  **Choices:**   - `"present"` - `"absent"` - `"enabled"` - `"disabled"` |

## [Notes](icx_lldp_module.md#id3)

> **Note:**
>
> - Tested against ICX 10.1.
> - For information on using ICX platform, see [the ICX OS Platform Options guide](user_guide/platform_icx.md).

## [Examples](icx_lldp_module.md#id4)

```yaml+jinja
- name: Disable LLDP
  community.network.icx_lldp:
    state: absent

- name: Enable LLDP
  community.network.icx_lldp:
    state: present

- name: Disable LLDP on ports 1/1/1 - 1/1/10, 1/1/20
  community.network.icx_lldp:
    interfaces:
     - name:
        - ethernet 1/1/1 to 1/1/10
        - ethernet 1/1/20
       state: absent
    state: present

- name: Enable LLDP on ports 1/1/5 - 1/1/10
  community.network.icx_lldp:
    interfaces:
      - name:
        - ethernet 1/1/1 to 1/1/10
```

## [Return Values](icx_lldp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  **Returned:** always, except for the platforms that use Netconf transport to manage the device.  **Sample:** `["lldp run", "no lldp run"]` |

### Authors

- Ruckus Wireless (@Commscope)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
