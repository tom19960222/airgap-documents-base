---
collection: ansible
version: "8"
title: "ansible.windows.win_updates module – Download and install Windows updates"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/windows/win_updates_module.html
fetched_at: 2026-07-28T01:10:52+00:00
---
# ansible.windows.win_updates module – Download and install Windows updates

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
> To use it in a playbook, specify: `ansible.windows.win_updates`.

- [Synopsis](win_updates_module.md#synopsis)
- [Parameters](win_updates_module.md#parameters)
- [Notes](win_updates_module.md#notes)
- [See Also](win_updates_module.md#see-also)
- [Examples](win_updates_module.md#examples)
- [Return Values](win_updates_module.md#return-values)

## [Synopsis](win_updates_module.md#id1)

- Searches, downloads, and installs Windows updates synchronously by automating the Windows Update client.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](win_updates_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **_output_path**  string | Internal use only. |
| **_wait**  boolean | Internal use only.  **Choices:**   - `false` ← (default) - `true` |
| **accept_list**  aliases: whitelist  list / elements=string | A list of update titles or KB numbers that can be used to specify which updates are to be searched or installed.  If an available update does not match one of the entries, then it is skipped and not installed.  Each entry can either be the KB article or Update title as a regex according to the PowerShell regex rules.  The accept list is only validated on updates that were found based on *category_names*. It will not force the module to install an update if it was not in the category specified.  The alias `whitelist` is deprecated and will be removed in a release after `2023-06-01`. |
| **category_names**  list / elements=string | A scalar or list of categories to install updates from. To get the list of categories, run the module with `state=searched`. The category must be the full category string, but is case insensitive.  Some possible categories are Application, Connectors, Critical Updates, Definition Updates, Developer Kits, Feature Packs, Guidance, Security Updates, Service Packs, Tools, Update Rollups, Updates, and Upgrades.  Since `v1.7.0` the value `*` will match all categories.  **Default:** `["CriticalUpdates", "SecurityUpdates", "UpdateRollups"]` |
| **log_path**  path | If set, `win_updates` will append update progress to the specified file. The directory must already exist. |
| **reboot**  boolean | Ansible will automatically reboot the remote host if it is required and continue to install updates after the reboot.  This can be used instead of using a [ansible.windows.win_reboot](win_reboot_module.md#ansible-collections-ansible-windows-win-reboot-module) task after this one and ensures all updates for that category is installed in one go.  Async does not work when `reboot=true`.  **Choices:**   - `false` ← (default) - `true` |
| **reboot_timeout**  integer | The time in seconds to wait until the host is back online from a reboot.  This is only used if `reboot=true` and a reboot is required.  **Default:** `1200` |
| **reject_list**  aliases: blacklist  list / elements=string | A list of update titles or KB numbers that can be used to specify which updates are to be excluded from installation.  If an available update does match one of the entries, then it is skipped and not installed.  Each entry can either be the KB article or Update title as a regex according to the PowerShell regex rules.  The alias `blacklist` is deprecated and will be removed in a release after `2023-06-01`. |
| **server_selection**  string | Defines the Windows Update source catalog.  `default` Use the default search source. For many systems default is set to the Microsoft Windows Update catalog. Systems participating in Windows Server Update Services (WSUS) or similar corporate update server environments may default to those managed update sources instead of the Windows Update catalog.  `managed_server` Use a managed server catalog. For environments utilizing Windows Server Update Services (WSUS) or similar corporate update servers, this option selects the defined corporate update source.  `windows_update` Use the Microsoft Windows Update catalog.  **Choices:**   - `"default"` ← (default) - `"managed_server"` - `"windows_update"` |
| **skip_optional**  boolean  *added in ansible.windows 1.8.0* | Skip optional updates where the update has BrowseOnly set by Microsoft.  Microsoft documents show that BrowseOnly means that the update should not be installed automatically and appear as optional updates.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | Controls whether found updates are downloaded or installed or listed  This module also supports Ansible check mode, which has the same effect as setting state=searched  **Choices:**   - `"installed"` ← (default) - `"searched"` - `"downloaded"` |
| **use_scheduled_task**  boolean | This option is deprecated and no longer does anything since `v1.7.0` of this collection.  The option will be removed in a release after `2023-06-01`.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](win_updates_module.md#id3)

> **Note:**
>
> - [ansible.windows.win_updates](win_updates_module.md#ansible-collections-ansible-windows-win-updates-module) must be run by a user with membership in the local Administrators group.
> - [ansible.windows.win_updates](win_updates_module.md#ansible-collections-ansible-windows-win-updates-module) will use the default update service configured for the machine (Windows Update, Microsoft Update, WSUS, etc).
> - By default [ansible.windows.win_updates](win_updates_module.md#ansible-collections-ansible-windows-win-updates-module) does not manage reboots, but will signal when a reboot is required with the *reboot_required* return value. *reboot* can be used to reboot the host if required in the one task.
> - [ansible.windows.win_updates](win_updates_module.md#ansible-collections-ansible-windows-win-updates-module) can take a significant amount of time to complete (hours, in some cases). Performance depends on many factors, including OS version, number of updates, system load, and update server load.
> - Beware that just after [ansible.windows.win_updates](win_updates_module.md#ansible-collections-ansible-windows-win-updates-module) reboots the system, the Windows system may not have settled yet and some base services could be in limbo. This can result in unexpected behavior. Check the examples for ways to mitigate this.
> - More information about PowerShell and how it handles RegEx strings can be found at <https://technet.microsoft.com/en-us/library/2007.11.powershell.aspx>.
> - The current module doesn’t support Systems Center Configuration Manager (SCCM). See <https://github.com/ansible-collections/ansible.windows/issues/194>

## [See Also](win_updates_module.md#id4)

> **See also:**
>
> [chocolatey.chocolatey.win_chocolatey](../../chocolatey/chocolatey/win_chocolatey_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-module)
> :   Manage packages using chocolatey.
>
> [ansible.windows.win_feature](win_feature_module.md#ansible-collections-ansible-windows-win-feature-module)
> :   Installs and uninstalls Windows Features on Windows Server.
>
> [community.windows.win_hotfix](../../community/windows/win_hotfix_module.md#ansible-collections-community-windows-win-hotfix-module)
> :   Install and uninstalls Windows hotfixes.
>
> [ansible.windows.win_package](win_package_module.md#ansible-collections-ansible-windows-win-package-module)
> :   Installs/uninstalls an installable package.

## [Examples](win_updates_module.md#id5)

```yaml+jinja
- name: Install all updates and reboot as many times as needed
  ansible.windows.win_updates:
    category_names: '*'
    reboot: true

- name: Install all security, critical, and rollup updates without a scheduled task
  ansible.windows.win_updates:
    category_names:
      - SecurityUpdates
      - CriticalUpdates
      - UpdateRollups

- name: Search-only, return list of found updates (if any), log to C:\ansible_wu.txt
  ansible.windows.win_updates:
    category_names: SecurityUpdates
    state: searched
    log_path: C:\ansible_wu.txt

- name: Install all security updates with automatic reboots
  ansible.windows.win_updates:
    category_names:
    - SecurityUpdates
    reboot: true

- name: Install only particular updates based on the KB numbers
  ansible.windows.win_updates:
    category_names:
    - SecurityUpdates
    accept_list:
    - KB4056892
    - KB4073117

- name: Exclude updates based on the update title
  ansible.windows.win_updates:
    category_names:
    - SecurityUpdates
    - CriticalUpdates
    reject_list:
    - Windows Malicious Software Removal Tool for Windows
    - \d{4}-\d{2} Cumulative Update for Windows Server 2016

# Optionally, you can increase the reboot_timeout to survive long updates during reboot
- name: Ensure we wait long enough for the updates to be applied during reboot
  ansible.windows.win_updates:
    reboot: true
    reboot_timeout: 3600

# Search and download Windows updates
- name: Search and download Windows updates without installing them
  ansible.windows.win_updates:
    state: downloaded
```

## [Return Values](win_updates_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **failed_update_count**  integer | The number of updates that failed to install.  **Returned:** always  **Sample:** `0` |
| **filtered_updates**  dictionary | Updates that were found but were filtered based on *blacklist*, *whitelist* or *category_names*. The return value is in the same form as *updates*, along with *filtered_reason*.  **Returned:** success  **Sample:** `"see the updates return value"` |
| **filtered_reason**  string | The reason why this update was filtered.  This value has been deprecated since `1.7.0`, use `filtered_reasons` which contain a list of all the reasons why the update is filtered.  **Returned:** always  **Sample:** `"skip_hidden"` |
| **filtered_reasons**  list / elements=string  *added in ansible.windows 1.7.0* | A list of reasons why the update has been filtered.  Can be `accept_list`, `reject_list`, `hidden`, `category_names`, or `skip_optional`.  **Returned:** success  **Sample:** `["category_names", "accept_list"]` |
| **found_update_count**  integer | The number of updates found needing to be applied.  **Returned:** success  **Sample:** `3` |
| **installed_update_count**  integer | The number of updates successfully installed or downloaded.  **Returned:** success  **Sample:** `2` |
| **reboot_required**  boolean | True when the target server requires a reboot to complete updates (no further updates can be installed until after a reboot).  **Returned:** success  **Sample:** `true` |
| **rebooted**  boolean  *added in ansible.windows 1.14.0* | Set to `true` when the target Windows host has been rebooted by `win_updates`.  **Returned:** success  **Sample:** `false` |
| **updates**  dictionary | Updates that were found/installed.  The key for each update is the `id` of the update.  **Returned:** success |
| **categories**  list / elements=string | A list of category strings for this update.  **Returned:** always  **Sample:** `["Critical Updates", "Windows Server 2012 R2"]` |
| **downloaded**  boolean  *added in ansible.windows 1.7.0* | Was the update downloaded.  **Returned:** always  **Sample:** `true` |
| **failure_hresult_code**  boolean | The HRESULT code from a failed update.  **Returned:** on install or download failure  **Sample:** `2147942402` |
| **failure_msg**  string  *added in ansible.windows 1.7.0* | The error message with more details on the failure.  **Returned:** on install or download failure and not running with async  **Sample:** `"Operation did not complete because there is no logged-on interactive user (WU_E_NO_INTERACTIVE_USER 0x80240020)"` |
| **id**  string | Internal Windows Update GUID.  **Returned:** always  **Sample:** `"fb95c1c8-de23-4089-ae29-fd3351d55421"` |
| **installed**  boolean | Was the update successfully installed.  **Returned:** always  **Sample:** `true` |
| **kb**  list / elements=string | A list of KB article IDs that apply to the update.  **Returned:** always  **Sample:** `["3004365"]` |
| **title**  string | Display name.  **Returned:** always  **Sample:** `"Security Update for Windows Server 2012 R2 (KB3004365)"` |

### Authors

- Matt Davis (@nitzmahone)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
- [Communication](index.md#communication-for-ansible-windows)
