---
collection: ansible
version: "6"
title: "community.windows.win_power_plan module – Changes the power plan of a Windows system"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_power_plan_module.html
fetched_at: 2026-07-27T17:23:41+00:00
---
# community.windows.win_power_plan module – Changes the power plan of a Windows system

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/community/windows) (version 1.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_power_plan`.

- [Synopsis](win_power_plan_module.md#synopsis)
- [Parameters](win_power_plan_module.md#parameters)
- [Examples](win_power_plan_module.md#examples)
- [Return Values](win_power_plan_module.md#return-values)

## [Synopsis](win_power_plan_module.md#id1)

- This module will change the power plan of a Windows system to the defined string.
- Windows defaults to `balanced` which will cause CPU throttling. In some cases it can be preferable to change the mode to `high performance` to increase CPU performance.
- One of *name* or *guid* must be provided.

## [Parameters](win_power_plan_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **guid**  string  added in community.windows 1.9.0 | String value that indicates the desired power plan by guid.  The power plan must already be present on the system.  For out of box guids see <https://docs.microsoft.com/en-us/windows/win32/power/power-policy-settings>. |
| **name**  string | String value that indicates the desired power plan by name.  The power plan must already be present on the system.  Commonly there will be options for `balanced` and `high performance`. |

## [Examples](win_power_plan_module.md#id3)

```yaml+jinja
- name: Change power plan to high performance
  community.windows.win_power_plan:
    name: high performance

- name: Change power plan to high performance
  community.windows.win_power_plan:
    guid: 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c
```

## [Return Values](win_power_plan_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **all_available_plans**  dictionary | The name and enabled state of all power plans.  Returned: always  Sample: `{"Balanced": true, "High performance": false, "Power saver": false}` |
| **power_plan_enabled**  boolean | State of the intended power plan.  Returned: success  Sample: `true` |
| **power_plan_name**  string | Value of the intended power plan.  Returned: always  Sample: `"balanced"` |

### Authors

- Noah Sparks (@nwsparks)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
