---
collection: ansible
version: "8"
title: "community.network.icx_linkagg module – Manage link aggregation groups on Ruckus ICX 7000 series switches"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/icx_linkagg_module.html
fetched_at: 2026-07-28T01:56:49+00:00
---
# community.network.icx_linkagg module – Manage link aggregation groups on Ruckus ICX 7000 series switches

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
> To use it in a playbook, specify: `community.network.icx_linkagg`.

- [Synopsis](icx_linkagg_module.md#synopsis)
- [Parameters](icx_linkagg_module.md#parameters)
- [Notes](icx_linkagg_module.md#notes)
- [Examples](icx_linkagg_module.md#examples)
- [Return Values](icx_linkagg_module.md#return-values)

## [Synopsis](icx_linkagg_module.md#id1)

- This module provides declarative management of link aggregation groups on Ruckus ICX network devices.

Aliases: network.icx.icx_linkagg

## [Parameters](icx_linkagg_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregate**  list / elements=string | List of link aggregation definitions. |
| **check_running_config**  boolean | Check running configuration. This can be set as environment variable. Module will use environment variable value(default:True), unless it is overridden, by specifying it as module parameter.  **Choices:**   - `false` - `true` |
| **group**  integer | Channel-group number for the port-channel Link aggregation group. Range 1-255 or set to ‘auto’ to auto-generates a LAG ID |
| **members**  list / elements=string | List of port members or ranges of the link aggregation group. |
| **mode**  string | Mode of the link aggregation group.  **Choices:**   - `"dynamic"` - `"static"` |
| **name**  string | Name of the LAG |
| **state**  string | State of the link aggregation group.  **Choices:**   - `"present"` - `"absent"` |
| **check_running_config**  boolean | Check running configuration. This can be set as environment variable. Module will use environment variable value(default:True), unless it is overridden, by specifying it as module parameter.  **Choices:**   - `false` - `true` ← (default) |
| **group**  integer | Channel-group number for the port-channel Link aggregation group. Range 1-255 or set to ‘auto’ to auto-generates a LAG ID |
| **members**  list / elements=string | List of port members or ranges of the link aggregation group. |
| **mode**  string | Mode of the link aggregation group.  **Choices:**   - `"dynamic"` - `"static"` |
| **name**  string | Name of the LAG |
| **purge**  boolean | Purge links not defined in the *aggregate* parameter.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | State of the link aggregation group.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](icx_linkagg_module.md#id3)

> **Note:**
>
> - Tested against ICX 10.1.
> - For information on using ICX platform, see [the ICX OS Platform Options guide](user_guide/platform_icx.md).

## [Examples](icx_linkagg_module.md#id4)

```yaml+jinja
- name: Create static link aggregation group
  community.network.icx_linkagg:
    group: 10
    mode: static
    name: LAG1

- name: Create link aggregation group with auto id
  community.network.icx_linkagg:
    group: auto
    mode: dynamic
    name: LAG2

- name: Delete link aggregation group
  community.network.icx_linkagg:
    group: 10
    state: absent

- name: Set members to LAG
  community.network.icx_linkagg:
    group: 200
    mode: static
    members:
      - ethernet 1/1/1 to 1/1/6
      - ethernet 1/1/10

- name: Remove links other then LAG id 100 and 3 using purge
  community.network.icx_linkagg:
    aggregate:
      - { group: 3}
      - { group: 100}
    purge: true
```

## [Return Values](icx_linkagg_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  **Returned:** always, except for the platforms that use Netconf transport to manage the device.  **Sample:** `["lag LAG1 dynamic id 11", "ports ethernet 1/1/1 to 1/1/6", "no ports ethernet 1/1/10", "no lag LAG1 dynamic id 12"]` |

### Authors

- Ruckus Wireless (@Commscope)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
