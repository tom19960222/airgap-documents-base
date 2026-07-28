---
collection: ansible
version: "6"
title: "community.windows.win_region module – Set the region and format settings"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_region_module.html
fetched_at: 2026-07-27T17:23:51+00:00
---
# community.windows.win_region module – Set the region and format settings

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
> To use it in a playbook, specify: `community.windows.win_region`.

- [Synopsis](win_region_module.md#synopsis)
- [Parameters](win_region_module.md#parameters)
- [See Also](win_region_module.md#see-also)
- [Examples](win_region_module.md#examples)
- [Return Values](win_region_module.md#return-values)

## [Synopsis](win_region_module.md#id1)

- Set the location settings of a Windows Server.
- Set the format settings of a Windows Server.
- Set the unicode language settings of a Windows Server.
- Copy across these settings to the default profile.

## [Parameters](win_region_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **copy_settings**  boolean | This will copy the current format and location values to new user profiles and the welcome screen. This will only run if `location`, `format` or `unicode_language` has resulted in a change. If this process runs then it will always result in a change.  Choices:   - `false` ← (default) - `true` |
| **format**  string | The language format to set for the current user, see <https://msdn.microsoft.com/en-us/library/system.globalization.cultureinfo.aspx> for a list of culture names to use.  This needs to be set if `location` or `unicode_language` is not set. |
| **location**  string | The location to set for the current user, see <https://msdn.microsoft.com/en-us/library/dd374073.aspx> for a list of GeoIDs you can use and what location it relates to.  This needs to be set if `format` or `unicode_language` is not set. |
| **unicode_language**  string | The unicode language format to set for all users, see <https://msdn.microsoft.com/en-us/library/system.globalization.cultureinfo.aspx> for a list of culture names to use.  This needs to be set if `location` or `format` is not set. After setting this value a reboot is required for it to take effect. |

## [See Also](win_region_module.md#id3)

> **See also:**
>
> [community.windows.win_timezone](win_timezone_module.md#ansible-collections-community-windows-win-timezone-module)
> :   Sets Windows machine timezone.

## [Examples](win_region_module.md#id4)

```yaml+jinja
- name: Set the region format to English United States
  community.windows.win_region:
    format: en-US

- name: Set the region format to English Australia and copy settings to new profiles
  community.windows.win_region:
    format: en-AU
    copy_settings: yes

- name: Set the location to United States
  community.windows.win_region:
    location: 244

# Reboot when region settings change
- name: Set the unicode language to English Great Britain, reboot if required
  community.windows.win_region:
    unicode_language: en-GB
  register: result

- ansible.windows.win_reboot:
  when: result.restart_required

# Reboot when format, location or unicode has changed
- name: Set format, location and unicode to English Australia and copy settings, reboot if required
  community.windows.win_region:
    location: 12
    format: en-AU
    unicode_language: en-AU
  register: result

- ansible.windows.win_reboot:
  when: result.restart_required
```

## [Return Values](win_region_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **restart_required**  boolean | Whether a reboot is required for the change to take effect.  Returned: success  Sample: `true` |

### Authors

- Jordan Borean (@jborean93)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
