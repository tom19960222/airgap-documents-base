---
collection: ansible
version: "6"
title: "community.windows.win_psrepository_info module – Gather information about PSRepositories"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_psrepository_info_module.html
fetched_at: 2026-07-27T17:23:46+00:00
---
# community.windows.win_psrepository_info module – Gather information about PSRepositories

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
> see [Requirements](win_psrepository_info_module.md#ansible-collections-community-windows-win-psrepository-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.windows.win_psrepository_info`.

- [Synopsis](win_psrepository_info_module.md#synopsis)
- [Requirements](win_psrepository_info_module.md#requirements)
- [Parameters](win_psrepository_info_module.md#parameters)
- [See Also](win_psrepository_info_module.md#see-also)
- [Examples](win_psrepository_info_module.md#examples)
- [Return Values](win_psrepository_info_module.md#return-values)

## [Synopsis](win_psrepository_info_module.md#id1)

- Gather information about all or a specific PSRepository.

## [Requirements](win_psrepository_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- `PowerShellGet` module

## [Parameters](win_psrepository_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **name**  string | The name of the repository to retrieve.  Supports any wildcard pattern supported by `Get-PSRepository`.  If omitted then all repositories will returned.  Default: `"*"` |

## [See Also](win_psrepository_info_module.md#id4)

> **See also:**
>
> [community.windows.win_psrepository](win_psrepository_module.md#ansible-collections-community-windows-win-psrepository-module)
> :   Adds, removes or updates a Windows PowerShell repository.

## [Examples](win_psrepository_info_module.md#id5)

```yaml+jinja
- name: Get info for a single repository
  community.windows.win_psrepository_info:
    name: PSGallery
  register: repo_info

- name: Find all repositories that start with 'MyCompany'
  community.windows.win_psrepository_info:
    name: MyCompany*

- name: Get info for all repositories
  community.windows.win_psrepository_info:
  register: repo_info

- name: Remove all repositories that don't have a publish_location set
  community.windows.win_psrepository:
    name: "{{ item }}"
    state: absent
  loop: "{{ repo_info.repositories | rejectattr('publish_location', 'none') | list }}"
```

## [Return Values](win_psrepository_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **repositories**  list / elements=dictionary | A list of repositories (or an empty list is there are none).  Returned: always |
| **installation_policy**  string | The installation policy of the repository. The sample values are the only possible values.  Returned: success  Sample: `"['Trusted', 'Untrusted']"` |
| **name**  string | The name of the repository.  Returned: success  Sample: `"PSGallery"` |
| **package_management_provider**  string | The name of the package management provider for this repository.  Returned: success  Sample: `"NuGet"` |
| **provider_options**  dictionary | Provider-specific options for this repository.  Returned: success |
| **publish_location**  string | The location used to publish modules.  Returned: success  Sample: `"https://www.powershellgallery.com/api/v2/package/"` |
| **registered**  boolean | Whether the module is registered. Should always be `True`  Returned: success |
| **script_publish_location**  string | The location used to publish scripts.  Returned: success  Sample: `"https://www.powershellgallery.com/api/v2/package/"` |
| **script_source_location**  string | The location used to find and retrieve scripts.  Returned: success  Sample: `"https://www.powershellgallery.com/api/v2/items/psscript"` |
| **source_location**  string | The location used to find and retrieve modules. This should always have a value.  Returned: success  Sample: `"https://www.powershellgallery.com/api/v2"` |
| **trusted**  boolean | A boolean flag reflecting the value of `installation_policy` as to whether the repository is trusted.  Returned: success |

### Authors

- Brian Scholer (@briantist)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
