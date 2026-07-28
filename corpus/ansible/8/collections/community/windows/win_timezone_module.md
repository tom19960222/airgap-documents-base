---
collection: ansible
version: "8"
title: "community.windows.win_timezone module – Sets Windows machine timezone"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_timezone_module.html
fetched_at: 2026-07-28T02:02:31+00:00
---
# community.windows.win_timezone module – Sets Windows machine timezone

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/ui/repo/published/community/windows/) (version 1.13.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_timezone`.

- [Synopsis](win_timezone_module.md#synopsis)
- [Parameters](win_timezone_module.md#parameters)
- [Notes](win_timezone_module.md#notes)
- [See Also](win_timezone_module.md#see-also)
- [Examples](win_timezone_module.md#examples)
- [Return Values](win_timezone_module.md#return-values)

## [Synopsis](win_timezone_module.md#id1)

- Sets machine time to the specified timezone.

## [Parameters](win_timezone_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **timezone**  string / required | Timezone to set to.  Example: Central Standard Time  To disable Daylight Saving time, add the suffix `_dstoff` on timezones that support this. |

## [Notes](win_timezone_module.md#id3)

> **Note:**
>
> - The module will check if the provided timezone is supported on the machine.
> - A list of possible timezones is available from `tzutil.exe /l` and from <https://msdn.microsoft.com/en-us/library/ms912391.aspx>
> - If running on Server 2008 the hotfix <https://support.microsoft.com/en-us/help/2556308/tzutil-command-line-tool-is-added-to-windows-vista-and-to-windows-server-2008> needs to be installed to be able to run this module.

## [See Also](win_timezone_module.md#id4)

> **See also:**
>
> [community.windows.win_region](win_region_module.md#ansible-collections-community-windows-win-region-module)
> :   Set the region and format settings.

## [Examples](win_timezone_module.md#id5)

```yaml+jinja
- name: Set timezone to 'Romance Standard Time' (GMT+01:00)
  community.windows.win_timezone:
    timezone: Romance Standard Time

- name: Set timezone to 'GMT Standard Time' (GMT)
  community.windows.win_timezone:
    timezone: GMT Standard Time

- name: Set timezone to 'Central Standard Time' (GMT-06:00)
  community.windows.win_timezone:
    timezone: Central Standard Time

- name: Set timezime to Pacific Standard time and disable Daylight Saving time adjustments
  community.windows.win_timezone:
    timezone: Pacific Standard Time_dstoff
```

## [Return Values](win_timezone_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **previous_timezone**  string | The previous timezone if it was changed, otherwise the existing timezone.  **Returned:** success  **Sample:** `"Central Standard Time"` |
| **timezone**  string | The current timezone (possibly changed).  **Returned:** success  **Sample:** `"Central Standard Time"` |

### Authors

- Phil Schwartz (@schwartzmx)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
