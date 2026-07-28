---
collection: ansible
version: "6"
title: "community.windows.win_psscript module – Install and manage PowerShell scripts from a PSRepository"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_psscript_module.html
fetched_at: 2026-07-27T17:23:47+00:00
---
# community.windows.win_psscript module – Install and manage PowerShell scripts from a PSRepository

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/community/windows) (version 1.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
> You need further requirements to be able to use this module,
> see [Requirements](win_psscript_module.md#ansible-collections-community-windows-win-psscript-module-requirements) for details.
>
> To use it in a playbook, specify: `community.windows.win_psscript`.

- [Synopsis](win_psscript_module.md#synopsis)
- [Requirements](win_psscript_module.md#requirements)
- [Parameters](win_psscript_module.md#parameters)
- [Notes](win_psscript_module.md#notes)
- [See Also](win_psscript_module.md#see-also)
- [Examples](win_psscript_module.md#examples)

## [Synopsis](win_psscript_module.md#id1)

- Add or remove PowerShell scripts from registered PSRepositories.

## [Requirements](win_psscript_module.md#id2)

The below requirements are needed on the host that executes this module.

- `PowerShellGet` module v1.6.0+

## [Parameters](win_psscript_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allow_prerelease**  boolean | If `yes` installs scripts flagged as prereleases.  Choices:   - `false` ← (default) - `true` |
| **maximum_version**  string | The maximum version of the script to install.  Cannot be used when *state=latest*. |
| **minimum_version**  string | The minimum version of the script to install.  Cannot be used when *state=latest*. |
| **name**  string / required | The name of the script you want to install or remove. |
| **repository**  string | The registered name of the repository you want to install from.  Cannot be used when *state=absent*.  If ommitted, all repositories will be searched.  To register a repository, use [community.windows.win_psrepository](win_psrepository_module.md#ansible-collections-community-windows-win-psrepository-module). |
| **required_version**  string | The exact version of the script to install.  Cannot be used with *minimum_version* or *maximum_version*.  Cannot be used when *state=latest*. |
| **scope**  string | Determines whether the script is installed for only the `current_user` or for `all_users`.  Choices:   - `"current_user"` - `"all_users"` ← (default) |
| **source_password**  string | The password portion of the credential required to access the repository.  Must be used together with *source_username*. |
| **source_username**  string | The username portion of the credential required to access the repository.  Must be used together with *source_password*. |
| **state**  string | The desired state of the script. `absent` removes the script.  `latest` will ensure the most recent version available is installed.  `present` only installs if the script is missing.  Choices:   - `"present"` ← (default) - `"absent"` - `"latest"` |

## [Notes](win_psscript_module.md#id4)

> **Note:**
>
> - Unlike PowerShell modules, scripts do not support side-by-side installations of multiple versions. Installing a new version will replace the existing one.

## [See Also](win_psscript_module.md#id5)

> **See also:**
>
> [community.windows.win_psrepository](win_psrepository_module.md#ansible-collections-community-windows-win-psrepository-module)
> :   Adds, removes or updates a Windows PowerShell repository.
>
> [community.windows.win_psrepository_info](win_psrepository_info_module.md#ansible-collections-community-windows-win-psrepository-info-module)
> :   Gather information about PSRepositories.
>
> [community.windows.win_psmodule](win_psmodule_module.md#ansible-collections-community-windows-win-psmodule-module)
> :   Adds or removes a Windows PowerShell module.

## [Examples](win_psscript_module.md#id6)

```yaml+jinja
- name: Install a script from PSGallery
  community.windows.win_psscript:
    name: Test-RPC
    repository: PSGallery

- name: Find and install the latest version of a script from any repository
  community.windows.win_psscript:
    name: Get-WindowsAutoPilotInfo
    state: latest

- name: Remove a script that isn't needed
  community.windows.win_psscript:
    name: Defrag-Partition
    state: absent

- name: Install a specific version of a script for the current user
  community.windows.win_psscript:
    name: CleanOldFiles
    scope: current_user
    required_version: 3.10.2

- name: Install a script below a certain version
  community.windows.win_psscript:
    name: New-FeatureEnable
    maximum_version: 2.99.99

- name: Ensure a minimum version of a script is present
  community.windows.win_psscript:
    name: OldStandby
    minimum_version: 3.0.0

- name: Install any available version that fits a specific range
  community.windows.win_psscript:
    name: FinickyScript
    minimum_version: 2.5.1
    maximum_version: 2.6.19
```

### Authors

- Brian Scholer (@briantist)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
