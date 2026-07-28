---
collection: ansible
version: "8"
title: "chocolatey.chocolatey.win_chocolatey_facts module – Create a facts collection for Chocolatey"
source_url: https://docs.ansible.com/projects/ansible/8/collections/chocolatey/chocolatey/win_chocolatey_facts_module.html
fetched_at: 2026-07-28T01:18:37+00:00
---
# chocolatey.chocolatey.win_chocolatey_facts module – Create a facts collection for Chocolatey

> **Note:**
>
> This module is part of the [chocolatey.chocolatey collection](https://galaxy.ansible.com/ui/repo/published/chocolatey/chocolatey/) (version 1.5.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install chocolatey.chocolatey`.
>
> To use it in a playbook, specify: `chocolatey.chocolatey.win_chocolatey_facts`.

New in chocolatey.chocolatey 0.2.8

- [Synopsis](win_chocolatey_facts_module.md#synopsis)
- [Parameters](win_chocolatey_facts_module.md#parameters)
- [Notes](win_chocolatey_facts_module.md#notes)
- [See Also](win_chocolatey_facts_module.md#see-also)
- [Examples](win_chocolatey_facts_module.md#examples)
- [Returned Facts](win_chocolatey_facts_module.md#returned-facts)

## [Synopsis](win_chocolatey_facts_module.md#id1)

- This module shows information from Chocolatey, such as installed packages, outdated packages, configuration, feature and sources.

## [Parameters](win_chocolatey_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **filter**  aliases: gather_subset  list / elements=string  *added in chocolatey.chocolatey 1.5.0* | If supplied, restrict the facts collected to the given subset. Possible values: `all`, `config`, `feature`, `outdated`, `packages`, `sources`.  You can provide a list of values to specify a larger subset.  **Default:** `["all"]` |

## [Notes](win_chocolatey_facts_module.md#id3)

> **Note:**
>
> - Chocolatey must be installed beforehand, use [chocolatey.chocolatey.win_chocolatey](win_chocolatey_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-module) to do this.

## [See Also](win_chocolatey_facts_module.md#id4)

> **See also:**
>
> [chocolatey.chocolatey.win_chocolatey](win_chocolatey_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-module)
> :   Manage packages using chocolatey.
>
> [chocolatey.chocolatey.win_chocolatey_config](win_chocolatey_config_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-config-module)
> :   Manages Chocolatey config settings.
>
> [chocolatey.chocolatey.win_chocolatey_feature](win_chocolatey_feature_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-feature-module)
> :   Manages Chocolatey features.
>
> [chocolatey.chocolatey.win_chocolatey_source](win_chocolatey_source_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-source-module)
> :   Manages Chocolatey sources.

## [Examples](win_chocolatey_facts_module.md#id5)

```yaml+jinja
- name: Gather facts from chocolatey
  win_chocolatey_facts:

- name: Displays the Configuration
  debug:
    var: ansible_chocolatey.config

- name: Displays the Feature
  debug:
    var: ansible_chocolatey.feature

- name: Displays the Sources
  debug:
    var: ansible_chocolatey.sources

- name: Displays the Packages
  debug:
    var: ansible_chocolatey.packages

- name: Displays the Outdated packages
  debug:
    var: ansible_chocolatey.outdated

- name: Gather all facts from chocolatey, except outdated packages
  win_chocolatey_facts:
    filter:
    - 'config'
    - 'feature'
    - 'packages'
    - 'sources'

- name: Displays the collected facts from chocolatey without the outdated packages
  debug:
    var: ansible_chocolatey

- name: Clear existing facts from chocolatey
  ansible.builtin.meta: clear_facts

- name: Gather config and feature facts only from chocolatey
  win_chocolatey_facts:
    filter:
    - 'config'
    - 'feature'

- name: Displays the collected config and feature facts from chocolatey
  debug:
    var: ansible_chocolatey
```

## [Returned Facts](win_chocolatey_facts_module.md#id6)

Facts returned by this module are added/updated in the `hostvars` host facts and can be referenced by name just like any other host fact. They do not need to be registered in order to use them.

| Key | Description |
| --- | --- |
| **ansible_chocolatey**  complex | Detailed information about the Chocolatey installation  **Returned:** always |
| **config**  dictionary | Detailed information about stored the configurations  **Returned:** always (except when filter is set to exclude config)  **Sample:** `{"commandExecutionTimeoutSeconds": 2700, "containsLegacyPackageInstalls": true}` |
| **feature**  dictionary | Detailed information about enabled and disabled features  **Returned:** always (except when filter is set to exclude feature)  **Sample:** `{"allowEmptyCheckums": false, "autoUninstaller": true, "failOnAutoUninstaller": false}` |
| **filter**  list / elements=string  *added in chocolatey.chocolatey 1.5.0* | The list of subsets that were gathered  **Returned:** always  **Sample:** `["all"]` |
| **outdated**  complex  *added in chocolatey.chocolatey 1.3.0* | List of packages for which an update is available  **Returned:** always (except when filter is set to exclude outdated) |
| **available_version**  string | Available version of the package  **Returned:** always  **Sample:** `"7.2.4"` |
| **current_version**  string | Current version of the package  **Returned:** always  **Sample:** `"7.2.3"` |
| **package**  string | Name of the package  **Returned:** always  **Sample:** `"vscodepowershell-core\","` |
| **pinned**  boolean | Is the version of the package pinned to suppress upgrades  **Returned:** always  **Sample:** `false` |
| **packages**  complex | List of installed Packages  **Returned:** always (except when filter is set to exclude packages) |
| **package**  string | Name of the package  **Returned:** always  **Sample:** `"vscode"` |
| **version**  string | Version of the package  **Returned:** always  **Sample:** `"1.27.2"` |
| **sources**  complex | List of Chocolatey sources  **Returned:** always (except when filter is set to exclude sources) |
| **admin_only**  boolean | Is the source visible to Administrators only  **Returned:** always  **Sample:** `false` |
| **allow_self_service**  boolean | Is the source allowed to be used with self-service  **Returned:** always  **Sample:** `false` |
| **bypass_proxy**  boolean | Can the source explicitly bypass configured proxies  **Returned:** always  **Sample:** `true` |
| **certificate**  string | Pth to a PFX certificate for X509 authenticated feeds  **Returned:** always  **Sample:** `"C:\\chocolatey\\cert.pfx"` |
| **disabled**  boolean | Is the source disabled  **Returned:** always  **Sample:** `false` |
| **name**  string | Name of the source  **Returned:** always  **Sample:** `"chocolatey"` |
| **priority**  integer | The priority order of this source, lower is better, 0 is no priority  **Returned:** always  **Sample:** `0` |
| **source**  string | The source, can be a folder/file or an url  **Returned:** always  **Sample:** `"https://community.chocolatey.org/api/v2/"` |
| **source_username**  string | Username used to access authenticated feeds  **Returned:** always  **Sample:** `"username"` |

### Authors

- Simon Bärlocher (@sbaerlocher)
- ITIGO AG (@itigoag)
- Rain Sallow (@vexx32)
- Josh King (@windos)

### Collection links

- [Issue Tracker](https://github.com/chocolatey/chocolatey-ansible/issues)
- [Repository (Sources)](https://github.com/chocolatey/chocolatey-ansible)
