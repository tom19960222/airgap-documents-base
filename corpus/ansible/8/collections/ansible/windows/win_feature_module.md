---
collection: ansible
version: "8"
title: "ansible.windows.win_feature module – Installs and uninstalls Windows Features on Windows Server"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/windows/win_feature_module.html
fetched_at: 2026-07-28T01:10:36+00:00
---
# ansible.windows.win_feature module – Installs and uninstalls Windows Features on Windows Server

> **Note:**
>
> This module is part of the [ansible.windows collection](https://galaxy.ansible.com/ui/repo/published/ansible/windows/) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.windows`.
>
> To use it in a playbook, specify: `ansible.windows.win_feature`.

- [Synopsis](win_feature_module.md#synopsis)
- [Parameters](win_feature_module.md#parameters)
- [See Also](win_feature_module.md#see-also)
- [Examples](win_feature_module.md#examples)
- [Return Values](win_feature_module.md#return-values)

## [Synopsis](win_feature_module.md#id1)

- Installs or uninstalls Windows Roles or Features on Windows Server.
- This module uses the Add/Remove-WindowsFeature Cmdlets on Windows 2008 R2 and Install/Uninstall-WindowsFeature Cmdlets on Windows 2012, which are not available on client os machines.

## [Parameters](win_feature_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **include_management_tools**  boolean | Adds the corresponding management tools to the specified feature.  Not supported in Windows 2008 R2 and will be ignored.  **Choices:**   - `false` ← (default) - `true` |
| **include_sub_features**  boolean | Adds all subfeatures of the specified feature.  **Choices:**   - `false` ← (default) - `true` |
| **name**  list / elements=string / required | Names of roles or features to install as a single feature or a comma-separated list of features.  To list all available features use the PowerShell command `Get-WindowsFeature`. |
| **source**  string | Specify a source to install the feature from.  Not supported in Windows 2008 R2 and will be ignored.  Can either be `{driveletter}:\sources\sxs` or `\\{IP}\share\sources\sxs`. |
| **state**  string | State of the features or roles on the system.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [See Also](win_feature_module.md#id3)

> **See also:**
>
> [chocolatey.chocolatey.win_chocolatey](../../chocolatey/chocolatey/win_chocolatey_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-module)
> :   Manage packages using chocolatey.
>
> [ansible.windows.win_package](win_package_module.md#ansible-collections-ansible-windows-win-package-module)
> :   Installs/uninstalls an installable package.

## [Examples](win_feature_module.md#id4)

```yaml+jinja
- name: Install IIS (Web-Server only)
  ansible.windows.win_feature:
    name: Web-Server
    state: present

- name: Install IIS (Web-Server and Web-Common-Http)
  ansible.windows.win_feature:
    name:
    - Web-Server
    - Web-Common-Http
    state: present

- name: Install NET-Framework-Core from file
  ansible.windows.win_feature:
    name: NET-Framework-Core
    source: C:\Temp\iso\sources\sxs
    state: present

- name: Install IIS Web-Server with sub features and management tools
  ansible.windows.win_feature:
    name: Web-Server
    state: present
    include_sub_features: true
    include_management_tools: true
  register: win_feature

- name: Reboot if installing Web-Server feature requires it
  ansible.windows.win_reboot:
  when: win_feature.reboot_required
```

## [Return Values](win_feature_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **exitcode**  string | The stringified exit code from the feature installation/removal command.  **Returned:** always  **Sample:** `"Success"` |
| **feature_result**  complex | List of features that were installed or removed.  **Returned:** success |
| **display_name**  string | Feature display name.  **Returned:** always  **Sample:** `"Telnet Client"` |
| **id**  integer | A list of KB article IDs that apply to the update.  **Returned:** always  **Sample:** `44` |
| **message**  list / elements=string | Any messages returned from the feature subsystem that occurred during installation or removal of this feature.  **Returned:** always  **Sample:** `[]` |
| **reboot_required**  boolean | True when the target server requires a reboot as a result of installing or removing this feature.  **Returned:** always  **Sample:** `true` |
| **restart_needed**  boolean | DEPRECATED in Ansible 2.4 (refer to `reboot_required` instead). True when the target server requires a reboot as a result of installing or removing this feature.  **Returned:** always  **Sample:** `true` |
| **skip_reason**  string | The reason a feature installation or removal was skipped.  **Returned:** always  **Sample:** `"NotSkipped"` |
| **success**  boolean | If the feature installation or removal was successful.  **Returned:** always  **Sample:** `true` |
| **reboot_required**  boolean | True when the target server indicates a reboot is required (no further updates can be installed until after a reboot).  This my be true even if not change had occurred as the value is derived from the server state.  **Returned:** success  **Sample:** `true` |

### Authors

- Paul Durivage (@angstwad)
- Trond Hindenes (@trondhindenes)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
- [Communication](index.md#communication-for-ansible-windows)
