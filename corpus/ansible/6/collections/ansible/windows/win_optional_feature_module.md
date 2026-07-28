---
collection: ansible
version: "6"
title: "ansible.windows.win_optional_feature module – Manage optional Windows features"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/windows/win_optional_feature_module.html
fetched_at: 2026-07-27T16:44:58+00:00
---
# ansible.windows.win_optional_feature module – Manage optional Windows features

> **Note:**
>
> This module is part of the [ansible.windows collection](https://galaxy.ansible.com/ansible/windows) (version 1.12.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.windows`.
>
> To use it in a playbook, specify: `ansible.windows.win_optional_feature`.

- [Synopsis](win_optional_feature_module.md#synopsis)
- [Parameters](win_optional_feature_module.md#parameters)
- [See Also](win_optional_feature_module.md#see-also)
- [Examples](win_optional_feature_module.md#examples)
- [Return Values](win_optional_feature_module.md#return-values)

## [Synopsis](win_optional_feature_module.md#id1)

- Install or uninstall optional Windows features on non-Server Windows.
- This module uses the `Enable-WindowsOptionalFeature` and `Disable-WindowsOptionalFeature` cmdlets.

## [Parameters](win_optional_feature_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **include_parent**  boolean | Whether to enable the parent feature and the parent’s dependencies.  Choices:   - `false` ← (default) - `true` |
| **name**  list / elements=string / required | The name(s) of the feature to install.  This relates to `FeatureName` in the Powershell cmdlet.  To list all available features use the PowerShell command `Get-WindowsOptionalFeature`. |
| **source**  string | Specify a source to install the feature from.  Can either be `{driveletter}:\sources\sxs` or `\\{IP}\share\sources\sxs`. |
| **state**  string | Whether to ensure the feature is absent or present on the system.  Choices:   - `"absent"` - `"present"` ← (default) |

## [See Also](win_optional_feature_module.md#id3)

> **See also:**
>
> [chocolatey.chocolatey.win_chocolatey](../../chocolatey/chocolatey/win_chocolatey_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-module)
> :   Manage packages using chocolatey.
>
> [ansible.windows.win_feature](win_feature_module.md#ansible-collections-ansible-windows-win-feature-module)
> :   Installs and uninstalls Windows Features on Windows Server.
>
> [ansible.windows.win_package](win_package_module.md#ansible-collections-ansible-windows-win-package-module)
> :   Installs/uninstalls an installable package.

## [Examples](win_optional_feature_module.md#id4)

```yaml+jinja
- name: Install .Net 3.5
  ansible.windows.win_optional_feature:
    name: NetFx3
    state: present

- name: Install .Net 3.5 from source
  ansible.windows.win_optional_feature:
    name: NetFx3
    source: \\share01\win10\sources\sxs
    state: present

- name: Install Microsoft Subsystem for Linux
  ansible.windows.win_optional_feature:
    name: Microsoft-Windows-Subsystem-Linux
    state: present
  register: wsl_status

- name: Reboot if installing Linux Subsytem as feature requires it
  ansible.windows.win_reboot:
  when: wsl_status.reboot_required

- name: Install multiple features in one task
  ansible.windows.win_optional_feature:
    name:
    - NetFx3
    - Microsoft-Windows-Subsystem-Linux
    state: present
```

## [Return Values](win_optional_feature_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **reboot_required**  boolean | True when the target server requires a reboot to complete updates  Returned: success  Sample: `true` |

### Authors

- Carson Anderson (@rcanderson23)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
[Communication](index.md#communication-for-ansible-windows)
