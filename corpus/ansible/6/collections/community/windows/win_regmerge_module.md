---
collection: ansible
version: "6"
title: "community.windows.win_regmerge module – Merges the contents of a registry file into the Windows registry"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_regmerge_module.html
fetched_at: 2026-07-27T17:23:52+00:00
---
# community.windows.win_regmerge module – Merges the contents of a registry file into the Windows registry

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
> To use it in a playbook, specify: `community.windows.win_regmerge`.

- [Synopsis](win_regmerge_module.md#synopsis)
- [Parameters](win_regmerge_module.md#parameters)
- [Notes](win_regmerge_module.md#notes)
- [See Also](win_regmerge_module.md#see-also)
- [Examples](win_regmerge_module.md#examples)
- [Return Values](win_regmerge_module.md#return-values)

## [Synopsis](win_regmerge_module.md#id1)

- Wraps the reg.exe command to import the contents of a registry file.
- Suitable for use with registry files created using [ansible.windows.win_template](../../ansible/windows/win_template_module.md#ansible-collections-ansible-windows-win-template-module).
- Windows registry files have a specific format and must be constructed correctly with carriage return and line feed line endings otherwise they will not be merged.
- Exported registry files often start with a Byte Order Mark which must be removed if the file is to templated using [ansible.windows.win_template](../../ansible/windows/win_template_module.md#ansible-collections-ansible-windows-win-template-module).
- Registry file format is described at <https://support.microsoft.com/en-us/kb/310516>
- See also [ansible.windows.win_template](../../ansible/windows/win_template_module.md#ansible-collections-ansible-windows-win-template-module), [ansible.windows.win_regedit](../../ansible/windows/win_regedit_module.md#ansible-collections-ansible-windows-win-regedit-module)

## [Parameters](win_regmerge_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **compare_key**  string | The parent key to use when comparing the contents of the registry to the contents of the file. Needs to be in HKLM or HKCU part of registry. Use a PS-Drive style path for example HKLM:\SOFTWARE not HKEY_LOCAL_MACHINE\SOFTWARE If not supplied, or the registry key is not found, no comparison will be made, and the module will report changed. |
| **path**  path / required | The full path including file name to the registry file on the remote machine to be merged |

## [Notes](win_regmerge_module.md#id3)

> **Note:**
>
> - Organise your registry files so that they contain a single root registry key if you want to use the compare_to functionality.
> - This module does not force registry settings to be in the state described in the file. If registry settings have been modified externally the module will merge the contents of the file but continue to report differences on subsequent runs.
> - To force registry change, use [ansible.windows.win_regedit](../../ansible/windows/win_regedit_module.md#ansible-collections-ansible-windows-win-regedit-module) with `state=absent` before using `community.windows.win_regmerge`.

## [See Also](win_regmerge_module.md#id4)

> **See also:**
>
> [ansible.windows.win_reg_stat](../../ansible/windows/win_reg_stat_module.md#ansible-collections-ansible-windows-win-reg-stat-module)
> :   Get information about Windows registry keys.
>
> [ansible.windows.win_regedit](../../ansible/windows/win_regedit_module.md#ansible-collections-ansible-windows-win-regedit-module)
> :   Add, change, or remove registry keys and values.

## [Examples](win_regmerge_module.md#id5)

```yaml+jinja
- name: Merge in a registry file without comparing to current registry
  community.windows.win_regmerge:
    path: C:\autodeploy\myCompany-settings.reg

- name: Compare and merge registry file
  community.windows.win_regmerge:
    path: C:\autodeploy\myCompany-settings.reg
    compare_to: HKLM:\SOFTWARE\myCompany
```

## [Return Values](win_regmerge_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **compare_to_key_found**  boolean | whether the parent registry key has been found for comparison  Returned: when comparison key not found in registry  Sample: `false` |
| **compared**  boolean | whether a comparison has taken place between the registry and the file  Returned: when a comparison key has been supplied and comparison has been attempted  Sample: `true` |
| **difference_count**  integer | number of differences between the registry and the file  Returned: changed  Sample: `1` |

### Authors

- Jon Hawkesworth (@jhawkesworth)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
