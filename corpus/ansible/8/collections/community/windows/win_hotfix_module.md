---
collection: ansible
version: "8"
title: "community.windows.win_hotfix module – Install and uninstalls Windows hotfixes"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_hotfix_module.html
fetched_at: 2026-07-28T02:01:58+00:00
---
# community.windows.win_hotfix module – Install and uninstalls Windows hotfixes

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/ui/repo/published/community/windows/) (version 1.13.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_hotfix`.

- [Synopsis](win_hotfix_module.md#synopsis)
- [Parameters](win_hotfix_module.md#parameters)
- [Notes](win_hotfix_module.md#notes)
- [See Also](win_hotfix_module.md#see-also)
- [Examples](win_hotfix_module.md#examples)
- [Return Values](win_hotfix_module.md#return-values)

## [Synopsis](win_hotfix_module.md#id1)

- Install, uninstall a Windows hotfix.

## [Parameters](win_hotfix_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **hotfix_identifier**  string | The name of the hotfix as shown in DISM, see examples for details.  This or `hotfix_kb` MUST be set when `state=absent`.  If `state=present` then the hotfix at `source` will be validated against this value, if it does not match an error will occur.  You can get the identifier by running ‘Get-WindowsPackage -Online -PackagePath path-to-cab-in-msu’ after expanding the msu file. |
| **hotfix_kb**  string | The name of the KB the hotfix relates to, see examples for details.  This or `hotfix_identifier` MUST be set when `state=absent`.  If `state=present` then the hotfix at `source` will be validated against this value, if it does not match an error will occur.  Because DISM uses the identifier as a key and doesn’t refer to a KB in all cases it is recommended to use `hotfix_identifier` instead. |
| **source**  path | The path to the downloaded hotfix .msu file.  This MUST be set if `state=present` and MUST be a .msu hotfix file. |
| **state**  string | Whether to install or uninstall the hotfix.  When `present`, `source` MUST be set.  When `absent`, `hotfix_identifier` or `hotfix_kb` MUST be set.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Notes](win_hotfix_module.md#id3)

> **Note:**
>
> - This must be run on a host that has the DISM powershell module installed and a Powershell version >= 4.
> - This module is installed by default on Windows 8 and Server 2012 and newer.
> - You can manually install this module on Windows 7 and Server 2008 R2 by installing the Windows ADK <https://developer.microsoft.com/en-us/windows/hardware/windows-assessment-deployment-kit>, see examples to see how to do it with chocolatey.
> - You can download hotfixes from <https://www.catalog.update.microsoft.com/Home.aspx>.

## [See Also](win_hotfix_module.md#id4)

> **See also:**
>
> [ansible.windows.win_package](../../ansible/windows/win_package_module.md#ansible-collections-ansible-windows-win-package-module)
> :   Installs/uninstalls an installable package.
>
> [ansible.windows.win_updates](../../ansible/windows/win_updates_module.md#ansible-collections-ansible-windows-win-updates-module)
> :   Download and install Windows updates.

## [Examples](win_hotfix_module.md#id5)

```yaml+jinja
- name: Install Windows ADK with DISM for Server 2008 R2
  chocolatey.chocolatey.win_chocolatey:
    name: windows-adk
    version: 8.100.26866.0
    state: present
    install_args: /features OptionId.DeploymentTools

- name: Install hotfix without validating the KB and Identifier
  community.windows.win_hotfix:
    source: C:\temp\windows8.1-kb3172729-x64_e8003822a7ef4705cbb65623b72fd3cec73fe222.msu
    state: present
  register: hotfix_install

- ansible.windows.win_reboot:
  when: hotfix_install.reboot_required

- name: Install hotfix validating KB
  community.windows.win_hotfix:
    hotfix_kb: KB3172729
    source: C:\temp\windows8.1-kb3172729-x64_e8003822a7ef4705cbb65623b72fd3cec73fe222.msu
    state: present
  register: hotfix_install

- ansible.windows.win_reboot:
  when: hotfix_install.reboot_required

- name: Install hotfix validating Identifier
  community.windows.win_hotfix:
    hotfix_identifier: Package_for_KB3172729~31bf3856ad364e35~amd64~~6.3.1.0
    source: C:\temp\windows8.1-kb3172729-x64_e8003822a7ef4705cbb65623b72fd3cec73fe222.msu
    state: present
  register: hotfix_install

- ansible.windows.win_reboot:
  when: hotfix_install.reboot_required

- name: Uninstall hotfix with Identifier
  community.windows.win_hotfix:
    hotfix_identifier: Package_for_KB3172729~31bf3856ad364e35~amd64~~6.3.1.0
    state: absent
  register: hotfix_uninstall

- ansible.windows.win_reboot:
  when: hotfix_uninstall.reboot_required

- name: Uninstall hotfix with KB (not recommended)
  community.windows.win_hotfix:
    hotfix_kb: KB3172729
    state: absent
  register: hotfix_uninstall

- ansible.windows.win_reboot:
  when: hotfix_uninstall.reboot_required
```

## [Return Values](win_hotfix_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **identifier**  string | The DISM identifier for the hotfix.  **Returned:** success  **Sample:** `"Package_for_KB3172729~31bf3856ad364e35~amd64~~6.3.1.0"` |
| **identifiers**  list / elements=string  *added in community.windows 1.10.0* | The DISM identifiers for each hotfix in the msu.  **Returned:** success  **Sample:** `["Package_for_KB3172729~31bf3856ad364e35~amd64~~6.3.1.0"]` |
| **kb**  string | The KB the hotfix relates to.  **Returned:** success  **Sample:** `"KB3172729"` |
| **kbs**  list / elements=string  *added in community.windows 1.10.0* | The KB for each hotfix in the msu,  **Returned:** success  **Sample:** `["KB3172729"]` |
| **reboot_required**  string | Whether a reboot is required for the install or uninstall to finalise.  **Returned:** success  **Sample:** `"True"` |

### Authors

- Jordan Borean (@jborean93)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
