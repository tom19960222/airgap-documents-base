---
collection: ansible
version: "6"
title: "community.windows.win_psmodule_info module – Gather information about PowerShell Modules"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_psmodule_info_module.html
fetched_at: 2026-07-27T17:23:44+00:00
---
# community.windows.win_psmodule_info module – Gather information about PowerShell Modules

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
> see [Requirements](win_psmodule_info_module.md#ansible-collections-community-windows-win-psmodule-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.windows.win_psmodule_info`.

- [Synopsis](win_psmodule_info_module.md#synopsis)
- [Requirements](win_psmodule_info_module.md#requirements)
- [Parameters](win_psmodule_info_module.md#parameters)
- [See Also](win_psmodule_info_module.md#see-also)
- [Examples](win_psmodule_info_module.md#examples)
- [Return Values](win_psmodule_info_module.md#return-values)

## [Synopsis](win_psmodule_info_module.md#id1)

- Gather information about PowerShell Modules including information from PowerShellGet.

## [Requirements](win_psmodule_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- `PowerShellGet` module

## [Parameters](win_psmodule_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **name**  string | The name of the module to retrieve.  Supports any wildcard pattern supported by `Get-Module`.  If omitted then all modules will returned.  Default: `"*"` |
| **repository**  string | The name of the PSRepository the modules were installed from.  This acts as a filter against the modules that would be returned based on the *name* option.  Modules that were not installed from a repository will not be returned if this option is set.  Only modules installed from a registered repository will be returned.  If the repository was re-registered after module installation with a new `SourceLocation`, this will not match. |

## [See Also](win_psmodule_info_module.md#id4)

> **See also:**
>
> [community.windows.win_psrepository_info](win_psrepository_info_module.md#ansible-collections-community-windows-win-psrepository-info-module)
> :   Gather information about PSRepositories.
>
> [community.windows.win_psscript_info](win_psscript_info_module.md#ansible-collections-community-windows-win-psscript-info-module)
> :   Gather information about installed PowerShell Scripts.

## [Examples](win_psmodule_info_module.md#id5)

```yaml+jinja
- name: Get info about all modules on the system
  community.windows.win_psmodule_info:

- name: Get info about the ScheduledTasks module
  community.windows.win_psmodule_info:
    name: ScheduledTasks

- name: Get info about networking modules
  community.windows.win_psmodule_info:
    name: Net*

- name: Get info about all modules installed from the PSGallery repository
  community.windows.win_psmodule_info:
    repository: PSGallery
  register: gallery_modules

- name: Update all modules retrieved from above example
  community.windows.win_psmodule:
    name: "{{ item }}"
    state: latest
  loop: "{{ gallery_modules.modules | map(attribute=name) }}"

- name: Get info about all modules on the system
  community.windows.win_psmodule_info:
  register: all_modules

- name: Find modules installed from a repository that isn't registered now
  set_fact:
    missing_repository_modules: "{{
      all_modules
      | json_query('modules[?repository!=null && repository==repository_source_location].{name: name, version: version, repository: repository}')
      | list
    }}"

- debug:
    var: missing_repository_modules
```

## [Return Values](win_psmodule_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **modules**  list / elements=dictionary | A list of modules (or an empty list is there are none).  Returned: always |
| **access_mode**  string | The module’s access mode. See <https://docs.microsoft.com/en-us/dotnet/api/system.management.automation.moduleaccessmode>  Returned: success  Sample: `"ReadWrite"` |
| **author**  string | The author of the module.  Returned: success  Sample: `"Warren Frame"` |
| **clr_version**  string | The CLR version of the module.  Returned: success  Sample: `"4.0"` |
| **company_name**  string | The company name of the module.  Returned: success  Sample: `"Microsoft Corporation"` |
| **compatible_ps_editions**  list / elements=string | The PS Editions the module is compatible with.  Returned: success  Sample: `["Desktop"]` |
| **copyright**  string | The copyright of the module.  Returned: success  Sample: `"(c) 2016 Warren F. All rights reserved."` |
| **dependencies**  list / elements=string | The modules required by this module.  Returned: success |
| **description**  string | The description of the module.  Returned: success  Sample: `"Provides cmdlets to work with local users and local groups"` |
| **dot_net_framework_version**  string | The .Net Framework version of the module.  Returned: success  Sample: `"4.6.1"` |
| **exported_aliases**  list / elements=string | The aliases exported from the module.  Returned: success  Sample: `["glu", "slu"]` |
| **exported_cmdlets**  list / elements=string | The cmdlets exported from the module.  Returned: success  Sample: `["Get-Certificate", "Get-PfxData"]` |
| **exported_commands**  list / elements=string | All of the commands exported from the module. Includes functions, cmdlets, and aliases.  Returned: success  Sample: `["glu", "Get-LocalUser"]` |
| **exported_dsc_resources**  list / elements=string | The DSC resources exported from the module.  Returned: success  Sample: `["xWebAppPool", "xWebSite"]` |
| **exported_format_files**  list / elements=path | The format files exported from the module.  Returned: success  Sample: `["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules\\DnsClient\\DnsCmdlets.Format.ps1xml", "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules\\DnsClient\\DnsConfig.Format.ps1xml", "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules\\DnsClient\\DnsClientPSProvider.Format.ps1xml"]` |
| **exported_functions**  list / elements=string | The functions exported from the module.  Returned: success  Sample: `["New-VirtualDisk", "New-Volume"]` |
| **exported_type_files**  list / elements=path | The type files exported from the module.  Returned: success  Sample: `["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules\\DnsClient\\DnsCmdlets.Types.ps1xml", "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules\\DnsClient\\DnsConfig.Types.ps1xml", "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules\\DnsClient\\DnsClientPSProvider.Types.ps1xml"]` |
| **exported_variables**  list / elements=string | The variables exported from the module.  Returned: success  Sample: `["GitPromptScriptBlock"]` |
| **exported_workflows**  list / elements=string | The workflows exported from the module.  Returned: success |
| **file_list**  list / elements=path | The files included in the module.  Returned: success  Sample: `["C:\\Program Files\\WindowsPowerShell\\Modules\\PowerShellGet\\1.6.0\\PSModule.psm1", "C:\\Program Files\\WindowsPowerShell\\Modules\\PowerShellGet\\1.6.0\\PSGet.Format.ps1xml", "C:\\Program Files\\WindowsPowerShell\\Modules\\PowerShellGet\\1.6.0\\PSGet.Resource.psd1"]` |
| **guid**  string | The GUID of the module.  Returned: success  Sample: `"74c9fd30-734b-4c89-a8ae-7727ad21d1d5"` |
| **help_info_uri**  string | The help info address of the module.  Returned: success  Sample: `"https://go.microsoft.com/fwlink/?linkid=390823"` |
| **icon_uri**  string | The address of the icon of the module.  Returned: success  Sample: `"https://raw.githubusercontent.com/powershell/psscriptanalyzer/master/logo.png"` |
| **installed_date**  string | The date the module was installed.  Returned: success  Sample: `"2018-02-14T17:55:34.9620740-05:00"` |
| **installed_location**  string | The path where the module is installed.  This should have the same value as `module_base` but only has a value when the module was installed via PowerShellGet.  Returned: success  Sample: `"C:\\Program Files\\WindowsPowerShell\\Modules\\posh-git\\0.7.1"` |
| **license_uri**  string | The address of the license for the module.  Returned: success  Sample: `"https://github.com/PowerShell/xPendingReboot/blob/master/LICENSE"` |
| **log_pipeline_execution_details**  boolean | Determines whether pipeline execution detail events should be logged.  Returned: success |
| **module_base**  string | The path that contains the module’s files.  Returned: success  Sample: `"C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules\\PKI"` |
| **module_list**  list / elements=dictionary | A list of modules packaged with this module.  This value is not often returned and the modules are not automatically processed.  Returned: success |
| **guid**  string | The GUID of the module.  Returned: success  Sample: `"82fdb72c-ecc5-4dfd-b9d5-83cf6eb9067f"` |
| **maximum_version**  string | The maximum version of the module.  Returned: success  Sample: `"2.9"` |
| **name**  string | The name of the module.  This may also be a path to the module file.  Returned: success  Sample: `".\\WindowsUpdateLog.psm1"` |
| **required_version**  string | The exact version of the module required.  Returned: success  Sample: `"3.1.4"` |
| **version**  string | The minimum version of the module.  Returned: success  Sample: `"2.0"` |
| **module_type**  string | The module’s type. See <https://docs.microsoft.com/en-us/dotnet/api/system.management.automation.moduletype>  Returned: success  Sample: `"Script"` |
| **name**  string | The name of the module.  Returned: success  Sample: `"PSReadLine"` |
| **nested_modules**  list / elements=dictionary | A list of modules nested with and loaded into the scope of this module.  This list contains full module objects, so each item can have all of the properties listed here, including `nested_modules`.  Returned: success |
| **package_management_provider**  string | If the module was installed from PowerShellGet, this is the package management provider used.  Returned: success  Sample: `"NuGet"` |
| **path**  string | The path to the module.  Returned: success  Sample: `"C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules\\PKI\\PKI.psd1"` |
| **power_shell_host_name**  string | The name of the PowerShell host that the module requires.  Returned: success  Sample: `"Windows PowerShell ISE Host"` |
| **power_shell_host_version**  string | The version of the PowerShell host that the module requires.  Returned: success  Sample: `"1.1"` |
| **power_shell_version**  string | The minimum version of PowerShell that the module requires.  Returned: success  Sample: `"5.1"` |
| **prefix**  string | The default prefix applied to `Verb-Noun` commands exported from the module, resulting in `Verb-PrefixNoun` names.  Returned: success |
| **private_data**  dictionary | Arbitrary private data used by the module. This is typically defined in the module manifest.  This module limits the depth of the data returned for module types other than `Script` and `Manifest`.  The `PSData` is commonly supplied and provides metadata for PowerShellGet but those fields are surfaced in top-level properties as well.  Returned: success  Sample: `{"PSData": {"LicenseUri": "https://example.com/module/LICENSE", "ProjectUri": "https://example.com/module/", "ReleaseNotes": "v2 - Fixed some bugs\nv1 - First release\n", "Tags": ["networking", "serialization"]}}` |
| **procoessor_architecture**  string | The module’s processor architecture. See <https://docs.microsoft.com/en-us/dotnet/api/system.reflection.processorarchitecture>  Returned: success  Sample: `"Amd64"` |
| **project_uri**  string | The address of the module’s project.  Returned: success  Sample: `"https://github.com/psake/psake"` |
| **published_date**  string | The date the module was published.  Returned: success  Sample: `"2017-03-15T04:18:09.0000000"` |
| **release_notes**  string | The module’s release notes. This is a free text field and no specific format should be assumed.  Returned: success  Sample: `` "## 1.4.6\n- Update `HelpInfoUri` to point to the latest content\n\n## 1.4.5\n- Bug fix for deadlock when getting parameters in an event\n\n## 1.4.4\n- Bug fix when installing modules from private feeds\n" `` |
| **repository**  string | The PSRepository where the module was installed from.  This value is not historical. It depends on the PSRepositories that are registered now for the current user.  The `repository_source_location` must match the current source location of a registered repository to get a repository name.  If there is no match, then this value will match `repository_source_location`.  Returned: success  Sample: `"PSGallery"` |
| **repository_source_location**  string | The source location of the repository where the module was installed from.  Returned: success  Sample: `"https://www.powershellgallery.com/api/v2"` |
| **required_assemblies**  string | A list of assemblies that the module requires.  The values may be a simple name or a full path.  Returned: success  Sample: `"['Microsoft.Management.Infrastructure.CimCmdlets.dll', 'Microsoft.Management.Infrastructure.Dll']"` |
| **required_modules**  list / elements=dictionary | A list of modules required by this module.  This list contains full module objects, so each item can have all of the properties listed here, including `required_modules`.  These module objects may not contain full information however, so you may see different results than if you had directly queried the module.  Returned: success |
| **root_module**  string | The root module as defined in the manifest.  This may be a module name, filename, or full path.  Returned: success  Sample: `"WindowsErrorReporting.psm1"` |
| **scripts**  list / elements=string | A list of scripts (`.ps1` files) that run in the caller’s session state when the module is imported.  This value comes from the `ScriptsToProcess` field in the module’s manifest.  Returned: success  Sample: `["PrepareEnvironment.ps1", "InitializeData.ps1"]` |
| **tags**  list / elements=string | The tags defined in the module’s `PSData` metadata.  Returned: success  Sample: `["networking", "serialization", "git", "dsc"]` |
| **updated_date**  string | The date the module was last updated.  Returned: success  Sample: `"2019-12-31T09:20:02.0000000"` |
| **version**  string | The module version.  Returned: success  Sample: `"1.2.3"` |

### Authors

- Brian Scholer (@briantist)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
