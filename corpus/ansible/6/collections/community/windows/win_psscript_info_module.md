---
collection: ansible
version: "6"
title: "community.windows.win_psscript_info module – Gather information about installed PowerShell Scripts"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_psscript_info_module.html
fetched_at: 2026-07-27T17:23:47+00:00
---
# community.windows.win_psscript_info module – Gather information about installed PowerShell Scripts

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
> see [Requirements](win_psscript_info_module.md#ansible-collections-community-windows-win-psscript-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.windows.win_psscript_info`.

- [Synopsis](win_psscript_info_module.md#synopsis)
- [Requirements](win_psscript_info_module.md#requirements)
- [Parameters](win_psscript_info_module.md#parameters)
- [See Also](win_psscript_info_module.md#see-also)
- [Examples](win_psscript_info_module.md#examples)
- [Return Values](win_psscript_info_module.md#return-values)

## [Synopsis](win_psscript_info_module.md#id1)

- Gather information about PowerShell Scripts installed via PowerShellGet.

## [Requirements](win_psscript_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- `PowerShellGet` module

## [Parameters](win_psscript_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **name**  string | The name of the script.  Supports any wildcard pattern supported by `Get-InstalledScript`.  If omitted then all scripts will returned.  Default: `"*"` |
| **repository**  string | The name of the PSRepository the scripts were installed from.  This acts as a filter against the scripts that would be returned based on the *name* option.  Only scripts installed from a registered repository will be returned.  If the repository was re-registered after script installation with a new `SourceLocation`, this will not match. |

## [See Also](win_psscript_info_module.md#id4)

> **See also:**
>
> [community.windows.win_psrepository_info](win_psrepository_info_module.md#ansible-collections-community-windows-win-psrepository-info-module)
> :   Gather information about PSRepositories.
>
> [community.windows.win_psmodule_info](win_psmodule_info_module.md#ansible-collections-community-windows-win-psmodule-info-module)
> :   Gather information about PowerShell Modules.

## [Examples](win_psscript_info_module.md#id5)

```yaml+jinja
- name: Get info about all script on the system
  community.windows.win_psscript_info:

- name: Get info about the Test-RPC script
  community.windows.win_psscript_info:
    name: Test-RPC

- name: Get info about test scripts
  community.windows.win_psscript_info:
    name: Test*

- name: Get info about all scripts installed from the PSGallery repository
  community.windows.win_psscript_info:
    repository: PSGallery
  register: gallery_scripts

- name: Update all scripts retrieved from above example
  community.windows.win_psscript:
    name: "{{ item }}"
    state: latest
  loop: "{{ gallery_scripts.scripts | map(attribute=name) }}"

- name: Get info about all scripts on the system
  community.windows.win_psscript_info:
  register: all_scripts

- name: Find scripts installed from a repository that isn't registered now
  set_fact:
    missing_repository_scripts: "{{
      all_scripts
      | json_query('scripts[?repository!=null && repository==repository_source_location].{name: name, version: version, repository: repository}')
      | list
    }}"

- debug:
    var: missing_repository_scripts
```

## [Return Values](win_psscript_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **scripts**  list / elements=dictionary | A list of installed scripts (or an empty list is there are none).  Returned: always |
| **additional_metadata**  dictionary | Additional metadata included with the script or during publishing of the script.  Many of the fields here are surfaced at the top level with some standardization. The values here may differ slightly as a result.  The field names here vary widely in case, and are not normalized or converted to snake_case.  Returned: success |
| **author**  string | The author of the script.  Returned: success  Sample: `"Ryan Ries"` |
| **company_name**  string | The company name of the script.  Returned: success  Sample: `"Microsoft Corporation"` |
| **copyright**  string | The copyright of the script.  Returned: success  Sample: `"Jordan Borean 2017"` |
| **dependencies**  list / elements=string | The script’s dependencies.  Returned: success |
| **description**  string | The description of the script.  Returned: success  Sample: `"This scripts tests network connectivity."` |
| **icon_uri**  string | The address of the icon of the script.  Returned: success  Sample: `"https://raw.githubusercontent.com/scripter/script/main/logo.png"` |
| **installed_date**  string | The date the script was installed.  Returned: success  Sample: `"2018-02-14T17:55:34.9620740-05:00"` |
| **installed_location**  string | The path where the script is installed.  Returned: success  Sample: `"C:\\Program Files\\WindowsPowerShell\\Scripts"` |
| **license_uri**  string | The address of the license for the script.  Returned: success  Sample: `"https://raw.githubusercontent.com/scripter/script/main/LICENSE"` |
| **name**  string | The name of the script.  Returned: success  Sample: `"Test-RPC"` |
| **package_management_provider**  string | This is the PowerShellGet package management provider used to install the script.  Returned: success  Sample: `"NuGet"` |
| **power_shell_get_format_version**  string | The version of the PowerShellGet specification format.  Returned: success  Sample: `"2.0"` |
| **project_uri**  string | The address of the script’s project.  Returned: success  Sample: `"https://github.com/scripter/script"` |
| **published_date**  string | The date the script was published.  Returned: success  Sample: `"2017-03-15T04:18:09.0000000"` |
| **release_notes**  string | The script’s release notes. This is a free text field and no specific format should be assumed.  Returned: success  Sample: `"## 1.5.5\n- Add optional param for detailed info\n\n## 1.4.7\n- Bug fix for deadlock when getting parameters in an event\n\n## 1.1.4\n- Bug fix when installing package from private feeds\n"` |
| **repository**  string | The PSRepository where the script was installed from.  This value is not historical. It depends on the PSRepositories that are registered now for the current user.  The `repository_source_location` must match the current source location of a registered repository to get a repository name.  If there is no match, then this value will match `repository_source_location`.  Returned: success  Sample: `"PSGallery"` |
| **repository_source_location**  string | The source location of the repository where the script was installed from.  Returned: success  Sample: `"https://www.powershellgallery.com/api/v2"` |
| **tags**  list / elements=string | The tags defined in the script’s `AdditionalMetadata`.  Returned: success  Sample: `["networking", "serialization", "git", "dsc"]` |
| **updated_date**  string | The date the script was last updated.  Returned: success  Sample: `"2019-12-31T09:20:02.0000000"` |
| **version**  string | The script version.  Returned: success  Sample: `"1.2.3"` |

### Authors

- Brian Scholer (@briantist)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
