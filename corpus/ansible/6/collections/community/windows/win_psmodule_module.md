---
collection: ansible
version: "6"
title: "community.windows.win_psmodule module – Adds or removes a Windows PowerShell module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_psmodule_module.html
fetched_at: 2026-07-27T17:23:43+00:00
---
# community.windows.win_psmodule module – Adds or removes a Windows PowerShell module

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
> To use it in a playbook, specify: `community.windows.win_psmodule`.

- [Synopsis](win_psmodule_module.md#synopsis)
- [Parameters](win_psmodule_module.md#parameters)
- [Notes](win_psmodule_module.md#notes)
- [See Also](win_psmodule_module.md#see-also)
- [Examples](win_psmodule_module.md#examples)
- [Return Values](win_psmodule_module.md#return-values)

## [Synopsis](win_psmodule_module.md#id1)

- This module helps to install Windows PowerShell modules and register custom modules repository on Windows-based systems.

## [Parameters](win_psmodule_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **accept_license**  boolean  added in community.windows 1.11.0 | Accepts the module’s license.  Required for modules that require license acceptance, since interactively answering the prompt is not possible.  Corresponds to the `-AcceptLicense` parameter of `Install-Module`.  Installation of a module or a dependency that requires license acceptance cannot be detected in check mode, but will cause a failure at runtime unless *accept_license=true*.  Choices:   - `false` ← (default) - `true` |
| **allow_clobber**  boolean | If `yes` allows install modules that contains commands those have the same names as commands that already exists.  Choices:   - `false` ← (default) - `true` |
| **allow_prerelease**  boolean | If `yes` installs modules marked as prereleases.  It doesn’t work with the parameters `minimum_version` and/or `maximum_version`.  It doesn’t work with the `state` set to absent.  Choices:   - `false` ← (default) - `true` |
| **maximum_version**  string | The maximum version of the PowerShell module that has to be installed. |
| **minimum_version**  string | The minimum version of the PowerShell module that has to be installed. |
| **name**  string / required | Name of the Windows PowerShell module that has to be installed. |
| **password**  string  added in community.windows 1.10.0 | Password to authenticate against private repository. |
| **repository**  string | Name of the custom repository to use. |
| **required_version**  string | The exact version of the PowerShell module that has to be installed. |
| **skip_publisher_check**  boolean | If `yes`, allows you to install a different version of a module that already exists on your computer in the case when a different one is not digitally signed by a trusted publisher and the newest existing module is digitally signed by a trusted publisher.  Choices:   - `false` ← (default) - `true` |
| **state**  string | If `present` a new module is installed.  If `absent` a module is removed.  If `latest` a module is updated to the newest version.  Choices:   - `"absent"` - `"latest"` - `"present"` ← (default) |
| **url**  string | URL of the custom repository to register.  DEPRECATED, will be removed in a major release after `2021-07-01`, please use the [community.windows.win_psrepository](win_psrepository_module.md#ansible-collections-community-windows-win-psrepository-module) module instead. |
| **username**  string  added in community.windows 1.10.0 | Username to authenticate against private repository. |

## [Notes](win_psmodule_module.md#id3)

> **Note:**
>
> - PowerShell modules needed - PowerShellGet >= 1.6.0 - PackageManagement >= 1.1.7
> - PowerShell package provider needed - NuGet >= 2.8.5.201
> - On PowerShell 5.x required modules and a package provider will be updated under the first run of the win_psmodule module.
> - On PowerShell 3.x and 4.x you have to install them before using the win_psmodule.

## [See Also](win_psmodule_module.md#id4)

> **See also:**
>
> [community.windows.win_psrepository](win_psrepository_module.md#ansible-collections-community-windows-win-psrepository-module)
> :   Adds, removes or updates a Windows PowerShell repository.

## [Examples](win_psmodule_module.md#id5)

```yaml+jinja
---
- name: Add a PowerShell module
  community.windows.win_psmodule:
    name: PowerShellModule
    state: present

- name: Add an exact version of PowerShell module
  community.windows.win_psmodule:
    name: PowerShellModule
    required_version: "4.0.2"
    state: present

- name: Install or update an existing PowerShell module to the newest version
  community.windows.win_psmodule:
    name: PowerShellModule
    state: latest

- name: Install newer version of built-in Windows module
  community.windows.win_psmodule:
    name: Pester
    skip_publisher_check: yes
    state: present

- name: Add a PowerShell module and register a repository
  community.windows.win_psmodule:
    name: MyCustomModule
    repository: MyRepository
    state: present

- name: Add a PowerShell module from a specific repository
  community.windows.win_psmodule:
    name: PowerShellModule
    repository: MyRepository
    state: present

- name: Add a PowerShell module from a specific repository with credentials
  win_psmodule:
    name: PowerShellModule
    repository: MyRepository
    username: repo_username
    password: repo_password
    state: present

- name: Remove a PowerShell module
  community.windows.win_psmodule:
    name: PowerShellModule
    state: absent
```

## [Return Values](win_psmodule_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **nuget_changed**  boolean | True when Nuget package provider is installed.  Returned: always  Sample: `true` |
| **output**  string | A message describing the task result.  Returned: always  Sample: `"Module PowerShellCookbook installed"` |
| **repository_changed**  boolean | True when a custom repository is installed or removed.  Returned: always  Sample: `true` |

### Authors

- Wojciech Sciesinski (@it-praktyk)
- Daniele Lazzari (@dlazz)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
