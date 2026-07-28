---
collection: ansible
version: "6"
title: "community.windows.win_psrepository_copy module – Copies registered PSRepositories to other user profiles"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_psrepository_copy_module.html
fetched_at: 2026-07-27T17:23:45+00:00
---
# community.windows.win_psrepository_copy module – Copies registered PSRepositories to other user profiles

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
> To use it in a playbook, specify: `community.windows.win_psrepository_copy`.

New in community.windows 1.3.0

- [Synopsis](win_psrepository_copy_module.md#synopsis)
- [Parameters](win_psrepository_copy_module.md#parameters)
- [Notes](win_psrepository_copy_module.md#notes)
- [See Also](win_psrepository_copy_module.md#see-also)
- [Examples](win_psrepository_copy_module.md#examples)

## [Synopsis](win_psrepository_copy_module.md#id1)

- Copies specified registered PSRepositories to other user profiles on the system.
- Can include the `Default` profile so that new users start with the selected repositories.
- Can include special service accounts like the local SYSTEM user, LocalService, NetworkService.

## [Parameters](win_psrepository_copy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **exclude**  list / elements=string | The names of repositories to exclude.  Names are interpreted as wildcards.  If a name matches both an include (*name*) and *exclude*, it will be excluded. |
| **exclude_profiles**  list / elements=string | The names of user profiles to exclude.  If a profile matches both an include (*profiles*) and *exclude_profiles*, it will be excluded.  By default, the service account profiles are excluded.  To explcitly exclude nothing, set *exclude_profiles=[]*.  Default: `["systemprofile", "LocalService", "NetworkService"]` |
| **name**  list / elements=string | The names of repositories to copy.  Names are interpreted as wildcards.  Default: `["*"]` |
| **profiles**  list / elements=string | The names of user profiles to populate with repositories.  Names are interpreted as wildcards.  The `Default` profile can also be matched.  The `Public` and `All Users` profiles cannot be targeted, as PSRepositories are not loaded from them.  Default: `["*"]` |
| **source**  path | The full path to the source repositories XML file.  Defaults to the repositories registered to the current user.  Default: `"%LOCALAPPDATA%\\Microsoft\\Windows\\PowerShell\\PowerShellGet\\PSRepositories.xml"` |

## [Notes](win_psrepository_copy_module.md#id3)

> **Note:**
>
> - Does not require the `PowerShellGet` module or any other external dependencies.
> - User profiles are loaded from the registry. If a given path does not exist (like if the profile directory was deleted), it is silently skipped.
> - If setting service account profiles, you may need `become=yes`. See examples.
> - When PowerShellGet first sets up a repositories file, it always adds `PSGallery`, however if this module creates a new repos file and your selected repositories don’t include `PSGallery`, it won’t be in your destination.
> - The values searched in *profiles* (and *exclude_profiles*) are profile names, not necessarily user names. This can happen when the profile path is deliberately changed or when domain user names conflict with users from the local computer or another domain. In this case the second+ user may have the domain name or local computer name appended, like `JoeUser.Contoso` vs. `JoeUser`. If you intend to filter user profiles, ensure your filters catch the right names.
> - In the case of the service accounts, the specific profiles are `systemprofile` (for the `SYSTEM` user), and `LocalService` or `NetworkService` for those accounts respectively.
> - Repositories with credentials (requiring authentication) or proxy information will copy, but the credentials and proxy details will not as that information is not stored with repository.

## [See Also](win_psrepository_copy_module.md#id4)

> **See also:**
>
> [community.windows.win_psrepository](win_psrepository_module.md#ansible-collections-community-windows-win-psrepository-module)
> :   Adds, removes or updates a Windows PowerShell repository.
>
> [community.windows.win_psrepository_info](win_psrepository_info_module.md#ansible-collections-community-windows-win-psrepository-info-module)
> :   Gather information about PSRepositories.

## [Examples](win_psrepository_copy_module.md#id5)

```yaml+jinja
- name: Copy the current user's PSRepositories to all non-service account profiles and Default profile
  community.windows.win_psrepository_copy:

- name: Copy the current user's PSRepositories to all profiles and Default profile
  community.windows.win_psrepository_copy:
    exclude_profiles: []

- name: Copy the current user's PSRepositories to all profiles beginning with A, B, or C
  community.windows.win_psrepository_copy:
    profiles:
      - 'A*'
      - 'B*'
      - 'C*'

- name: Copy the current user's PSRepositories to all profiles beginning B except Brian and Brianna
  community.windows.win_psrepository_copy:
    profiles: 'B*'
    exclude_profiles:
      - Brian
      - Brianna

- name: Copy a specific set of repositories to profiles beginning with 'svc' with exceptions
  community.windows.win_psrepository_copy:
    name:
      - CompanyRepo1
      - CompanyRepo2
      - PSGallery
    profiles: 'svc*'
    exclude_profiles: 'svc-restricted'

- name: Copy repos matching a pattern with exceptions
  community.windows.win_psrepository_copy:
    name: 'CompanyRepo*'
    exclude: 'CompanyRepo*-Beta'

- name: Copy repositories from a custom XML file on the target host
  community.windows.win_psrepository_copy:
    source: 'C:\data\CustomRepostories.xml'

### A sample workflow of seeding a system with a custom repository

# A playbook that does initial host setup or builds system images

- name: Register custom respository
  community.windows.win_psrepository:
    name: PrivateRepo
    source_location: https://example.com/nuget/feed/etc
    installation_policy: trusted

- name: Ensure all current and new users have this repository registered
  community.windows.win_psrepository_copy:
    name: PrivateRepo

# In another playbook, run by other users (who may have been created later)

- name: Install a module
  community.windows.win_psmodule:
    name: CompanyModule
    repository: PrivateRepo
    state: present
```

### Authors

- Brian Scholer (@briantist)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
