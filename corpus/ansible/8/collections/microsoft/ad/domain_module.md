---
collection: ansible
version: "8"
title: "microsoft.ad.domain module – Ensures the existence of a Windows domain"
source_url: https://docs.ansible.com/projects/ansible/8/collections/microsoft/ad/domain_module.html
fetched_at: 2026-07-28T02:40:49+00:00
---
# microsoft.ad.domain module – Ensures the existence of a Windows domain

> **Note:**
>
> This module is part of the [microsoft.ad collection](https://galaxy.ansible.com/ui/repo/published/microsoft/ad/) (version 1.4.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install microsoft.ad`.
>
> To use it in a playbook, specify: `microsoft.ad.domain`.

- [Synopsis](domain_module.md#synopsis)
- [Parameters](domain_module.md#parameters)
- [Attributes](domain_module.md#attributes)
- [See Also](domain_module.md#see-also)
- [Examples](domain_module.md#examples)
- [Return Values](domain_module.md#return-values)

## [Synopsis](domain_module.md#id1)

- Ensure that the domain named by *dns_domain_name* exists and is reachable.
- If the domain is not reachable, the domain is created in a new forest on the target Windows Server 2012+ host.
- This module may require subsequent use of the [ansible.windows.win_reboot](../../ansible/windows/win_reboot_module.md#ansible-collections-ansible-windows-win-reboot-module) action if changes are made.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](domain_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **create_dns_delegation**  boolean | Whether to create a DNS delegation that references the new DNS server that you install along with the domain controller.  Valid for Active Directory-integrated DNS only.  The default is computed automatically based on the environment.  **Choices:**   - `false` - `true` |
| **database_path**  path | The path to a directory on a fixed disk of the Windows host where the domain database will be created.  If not set then the default path is `%SYSTEMROOT%\NTDS`. |
| **dns_domain_name**  string / required | The DNS name of the domain which should exist and be reachable or reside on the target Windows host. |
| **domain_mode**  string | Specifies the domain functional level of the first domain in the creation of a new forest.  The domain functional level cannot be lower than the forest functional level, but it can be higher.  The default is automatically computed and set.  Current known modes are `Win2003`, `Win2008`, `Win2008R2`, `Win2012`, `Win2012R2`, or `WinThreshold`. |
| **domain_netbios_name**  string | The NetBIOS name for the root domain in the new forest.  For NetBIOS names to be valid for use with this parameter they must be single label names of 15 characters or less, if not it will fail.  If this parameter is not set, then the default is automatically computed from the value of the *domain_name* parameter. |
| **forest_mode**  string | Specifies the forest functional level for the new forest.  The default forest functional level in Windows Server is typically the same as the version you are running.  Current known modes are `Win2003`, `Win2008`, `Win2008R2`, `Win2012`, `Win2012R2`, or `WinThreshold`. |
| **install_dns**  boolean | Whether to install the DNS service when creating the domain controller.  **Choices:**   - `false` - `true` ← (default) |
| **log_path**  path | Specifies the fully qualified, non-UNC path to a directory on a fixed disk of the local computer where the log file for this operation is written.  If not set then the default path is `%SYSTEMROOT%\NTDS`. |
| **reboot**  boolean | If `true`, this will reboot the host if a reboot was required to configure the domain.  If `false`, this will not reboot the host if a reboot was required and instead sets the *reboot_required* return value to `true`.  Multiple reboots may occur if the host required a reboot before the domain promotion.  This cannot be used with async mode.  To use this parameter, ensure the fully qualified module name is used in the task or the *collections* keyword includes this collection.  **Choices:**   - `false` ← (default) - `true` |
| **safe_mode_password**  string / required | Safe mode password for the domain controller. |
| **sysvol_path**  path | The path to a directory on a fixed disk of the Windows host where the Sysvol file will be created.  If not set then the default path is `%SYSTEMROOT%\SYSVOL`. |

## [Attributes](domain_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action** | **Support:** **full** | Indicates this has a corresponding action plugin so some parts of the options can be executed on the controller |
| **async** | **Support:** **partial**  Supported for all scenarios except with *reboot=True*. | Supports being used with the `async` keyword |
| **bypass_host_loop** | **Support:** **none** | Forces a ‘global’ task that does not execute per host, this bypasses per host templating and serial, throttle and other loop considerations  Conditionals will work as if `run_once` is being used, variables used will be from the first available host  This action will not work normally outside of lockstep strategies |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platform:** **windows** | Target OS/families that can be operated against |

## [See Also](domain_module.md#id4)

> **See also:**
>
> [microsoft.ad.domain_controller](domain_controller_module.md#ansible-collections-microsoft-ad-domain-controller-module)
> :   Manage domain controller/member server state for a Windows host.
>
> [microsoft.ad.group](group_module.md#ansible-collections-microsoft-ad-group-module)
> :   Manage Active Directory group objects.
>
> [microsoft.ad.membership](membership_module.md#ansible-collections-microsoft-ad-membership-module)
> :   Manage domain/workgroup membership for a Windows host.
>
> [microsoft.ad.user](user_module.md#ansible-collections-microsoft-ad-user-module)
> :   Manage Active Directory users.
>
> [microsoft.ad.computer](computer_module.md#ansible-collections-microsoft-ad-computer-module)
> :   Manage Active Directory computer objects.
>
> [Migration guide](docsite/guide_migration.md#ansible-collections-microsoft-ad-docsite-guide-migration-migrated-modules-win-domain)
> :   This module replaces `ansible.windows.win_domain`. See the migration guide for details.
>
> [ansible.windows.win_domain](../../ansible/windows/win_domain_module.md#ansible-collections-ansible-windows-win-domain-module)
> :   Ensures the existence of a Windows domain.

## [Examples](domain_module.md#id5)

```yaml+jinja
- name: Create new domain in a new forest on the target host and reboot
  microsoft.ad.domain:
    dns_domain_name: ansible.vagrant
    safe_mode_password: password123!
    reboot: true

- name: Create new Windows domain in a new forest with specific parameters and reboot in post task
  microsoft.ad.domain:
    create_dns_delegation: false
    database_path: C:\Windows\NTDS
    dns_domain_name: ansible.vagrant
    domain_mode: Win2012R2
    domain_netbios_name: ANSIBLE
    forest_mode: Win2012R2
    safe_mode_password: password123!
    sysvol_path: C:\Windows\SYSVOL
  register: domain_install

- name: Reboot host if install requires it
  ansible.windows.win_reboot:
  when: domain_install.reboot_required
```

## [Return Values](domain_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **reboot_required**  boolean | True if changes were made that require a reboot.  **Returned:** always  **Sample:** `true` |

### Authors

- Matt Davis (@nitzmahone)
- Jordan Borean (@jborean93)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/microsoft.ad/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/microsoft.ad)
- [Report an issue](https://github.com/ansible-collections/microsoft.ad/issues/new/choose)
- [Communication](index.md#communication-for-microsoft-ad)
