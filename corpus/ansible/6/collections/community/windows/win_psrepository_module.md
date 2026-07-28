---
collection: ansible
version: "6"
title: "community.windows.win_psrepository module – Adds, removes or updates a Windows PowerShell repository."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_psrepository_module.html
fetched_at: 2026-07-27T17:23:44+00:00
---
# community.windows.win_psrepository module – Adds, removes or updates a Windows PowerShell repository.

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
> see [Requirements](win_psrepository_module.md#ansible-collections-community-windows-win-psrepository-module-requirements) for details.
>
> To use it in a playbook, specify: `community.windows.win_psrepository`.

- [Synopsis](win_psrepository_module.md#synopsis)
- [Requirements](win_psrepository_module.md#requirements)
- [Parameters](win_psrepository_module.md#parameters)
- [Notes](win_psrepository_module.md#notes)
- [See Also](win_psrepository_module.md#see-also)
- [Examples](win_psrepository_module.md#examples)

## [Synopsis](win_psrepository_module.md#id1)

- This module helps to add, remove and update Windows PowerShell repository on Windows-based systems.

## [Requirements](win_psrepository_module.md#id2)

The below requirements are needed on the host that executes this module.

- PowerShell Module [PowerShellGet >= 1.6.0](https://www.powershellgallery.com/packages/PowerShellGet/)
- PowerShell Module [PackageManagement >= 1.1.7](https://www.powershellgallery.com/packages/PackageManagement/)
- PowerShell Package Provider `NuGet` >= 2.8.5.201

## [Parameters](win_psrepository_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **force**  boolean | If `True`, any differences from the desired state will result in the repository being unregistered, and then re-registered.  *force* has no effect when *state=absent*. See notes for additional context.  Choices:   - `false` ← (default) - `true` |
| **installation_policy**  string | Sets the `InstallationPolicy` of a repository.  Will default to `trusted` when creating a new repository or used with *force=True*.  Choices:   - `"trusted"` - `"untrusted"` |
| **name**  string / required | Name of the repository to work with. |
| **password**  string  added in community.windows 1.10.0 | Password to authenticate against private repository. |
| **proxy**  string  added in community.windows 1.1.0 | Proxy to use for repository. |
| **publish_location**  string | Specifies the URI for publishing modules to this repository. |
| **script_publish_location**  string | Specifies the URI for publishing scripts to this repository. |
| **script_source_location**  string | Specifies the URI for discovering and installing scripts from this repository. |
| **source_location**  aliases: source  string | Specifies the URI for discovering and installing modules from this repository.  A URI can be a NuGet server feed (most common situation), HTTP, HTTPS, FTP or file location.  Required when registering a new repository or using *force=True*. |
| **state**  string | If `present` a new repository is added or updated.  If `absent` a repository is removed.  Choices:   - `"absent"` - `"present"` ← (default) |
| **username**  string  added in community.windows 1.10.0 | Username to authenticate against private repository. |

## [Notes](win_psrepository_module.md#id4)

> **Note:**
>
> - See the examples on how to update the NuGet package provider.
> - You can not use `win_psrepository` to re-register (add) removed PSGallery, use the command `Register-PSRepository -Default` instead.
> - When registering or setting *source_location*, PowerShellGet will transform the location according to internal rules, such as following HTTP/S redirects.
> - This can result in a `CHANGED` status on each run as the values will never match and will be “reset” each time.
> - To work around that, find the true destination value with [community.windows.win_psrepository_info](win_psrepository_info_module.md#ansible-collections-community-windows-win-psrepository-info-module) or `Get-PSRepository` and update the playbook to match.
> - When updating an existing repository, all options except *name* are optional. Only supplied options will be updated. Use *force=True* to exactly match.
> - *script_location*, *publish_location*, and *script_publish_location* are optional but once set can only be cleared with *force=True*.
> - Using *force=True* will unregister and re-register the repository if there are any changes, so that it exactly matches the options specified.

## [See Also](win_psrepository_module.md#id5)

> **See also:**
>
> [community.windows.win_psrepository_info](win_psrepository_info_module.md#ansible-collections-community-windows-win-psrepository-info-module)
> :   Gather information about PSRepositories.
>
> [community.windows.win_psmodule](win_psmodule_module.md#ansible-collections-community-windows-win-psmodule-module)
> :   Adds or removes a Windows PowerShell module.

## [Examples](win_psrepository_module.md#id6)

```yaml+jinja
---
- name: Ensure the required NuGet package provider version is installed
  ansible.windows.win_shell: Find-PackageProvider -Name Nuget -ForceBootstrap -IncludeDependencies -Force

- name: Register a PowerShell repository
  community.windows.win_psrepository:
    name: MyRepository
    source_location: https://myrepo.com
    state: present

- name: Remove a PowerShell repository
  community.windows.win_psrepository:
    name: MyRepository
    state: absent

- name: Add an untrusted repository
  community.windows.win_psrepository:
    name: MyRepository
    installation_policy: untrusted

- name: Add a repository with different locations
  community.windows.win_psrepository:
    name: NewRepo
    source_location: https://myrepo.example/module/feed
    script_source_location: https://myrepo.example/script/feed
    publish_location: https://myrepo.example/api/module/publish
    script_publish_location: https://myrepo.example/api/script/publish

- name: Update only two properties on the above repository
  community.windows.win_psrepository:
    name: NewRepo
    installation_policy: untrusted
    script_publish_location: https://scriptprocessor.example/publish

- name: Clear script locations from the above repository by re-registering it
  community.windows.win_psrepository:
    name: NewRepo
    installation_policy: untrusted
    source_location: https://myrepo.example/module/feed
    publish_location: https://myrepo.example/api/module/publish
    force: True

- name: Register a PowerShell repository with credentials
  community.windows.win_psrepository:
    name: MyRepository
    source_location: https://myrepo.com
    state: present
    username: repo_username
    password: repo_password
```

### Authors

- Wojciech Sciesinski (@it-praktyk)
- Brian Scholer (@briantist)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
