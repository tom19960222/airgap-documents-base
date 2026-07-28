---
collection: ansible
version: "8"
title: "microsoft.ad.domain_controller module – Manage domain controller/member server state for a Windows host"
source_url: https://docs.ansible.com/projects/ansible/8/collections/microsoft/ad/domain_controller_module.html
fetched_at: 2026-07-28T02:40:50+00:00
---
# microsoft.ad.domain_controller module – Manage domain controller/member server state for a Windows host

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
> To use it in a playbook, specify: `microsoft.ad.domain_controller`.

- [Synopsis](domain_controller_module.md#synopsis)
- [Parameters](domain_controller_module.md#parameters)
- [Attributes](domain_controller_module.md#attributes)
- [Notes](domain_controller_module.md#notes)
- [See Also](domain_controller_module.md#see-also)
- [Examples](domain_controller_module.md#examples)
- [Return Values](domain_controller_module.md#return-values)

## [Synopsis](domain_controller_module.md#id1)

- Ensure that a Windows Server 2012+ host is configured as a domain controller or demoted to member server.
- This module may require subsequent use of the [ansible.windows.win_reboot](../../ansible/windows/win_reboot_module.md#ansible-collections-ansible-windows-win-reboot-module) action if changes are made.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](domain_controller_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **database_path**  path | The path to a directory on a fixed disk of the Windows host where the domain database will be created..  If not set then the default path is `%SYSTEMROOT%\NTDS`. |
| **dns_domain_name**  string | When *state=domain_controller*, the DNS name of the domain for which the targeted Windows host should be a DC. |
| **domain_admin_password**  string / required | Password for the specified *domain_admin_user*. |
| **domain_admin_user**  string / required | Username of a domain admin for the target domain (necessary to promote or demote a domain controller). |
| **domain_log_path**  path | Specified the fully qualified, non-UNC path to a directory on a fixed disk of the local computer that will contain the domain log files. |
| **install_dns**  boolean | Whether to install the DNS service when creating the domain controller.  If not specified then the `-InstallDns` option is not supplied to `Install-ADDSDomainController` command, see [Install-ADDSDomainController](https://learn.microsoft.com/en-us/powershell/module/addsdeployment/install-addsdomaincontroller).  **Choices:**   - `false` - `true` |
| **install_media_path**  path | The path to a directory on a fixed disk of the Windows host where the Install From Media `IFC` data will be used.  See the [Install using IFM guide](https://social.technet.microsoft.com/wiki/contents/articles/8630.active-directory-step-by-step-guide-to-install-an-additional-domain-controller-using-ifm.aspx) for more information. |
| **local_admin_password**  string | Password to be assigned to the local `Administrator` user (required when *state=member_server*). |
| **read_only**  boolean | Whether to install the domain controller as a read only replica for an existing domain.  **Choices:**   - `false` ← (default) - `true` |
| **reboot**  boolean | If `true`, this will reboot the host if a reboot was required to configure the server.  If `false`, this will not reboot the host if a reboot was required and instead sets the *reboot_required* return value to `true`.  Multiple reboots may occur if the host required a reboot before the domain promotion.  This cannot be used with async mode.  To use this parameter, ensure the fully qualified module name is used in the task or the *collections* keyword includes this collection.  **Choices:**   - `false` ← (default) - `true` |
| **safe_mode_password**  string | Safe mode password for the domain controller (required when *state=domain_controller*). |
| **site_name**  string | Specifies the name of an existing site where you can place the new domain controller.  This option is required when *read_only=true*. |
| **state**  string / required | Whether the target host should be a domain controller or a member server.  **Choices:**   - `"domain_controller"` - `"member_server"` |
| **sysvol_path**  path | The path to a directory on a fixed disk of the Windows host where the Sysvol folder will be created.  If not set then the default path is `%SYSTEMROOT%\SYSVOL`. |

## [Attributes](domain_controller_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action** | **Support:** **full** | Indicates this has a corresponding action plugin so some parts of the options can be executed on the controller |
| **async** | **Support:** **partial**  Supported for all scenarios except with *reboot=True*. | Supports being used with the `async` keyword |
| **bypass_host_loop** | **Support:** **none** | Forces a ‘global’ task that does not execute per host, this bypasses per host templating and serial, throttle and other loop considerations  Conditionals will work as if `run_once` is being used, variables used will be from the first available host  This action will not work normally outside of lockstep strategies |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platform:** **windows** | Target OS/families that can be operated against |

## [Notes](domain_controller_module.md#id4)

> **Note:**
>
> - It is highly recommended to set *reboot=true* to have Ansible manage the host reboot phase as the actions done by this module puts the host in a state where it may not be possible for Ansible to reconnect in a subsequent task without a reboot.

## [See Also](domain_controller_module.md#id5)

> **See also:**
>
> [microsoft.ad.computer](computer_module.md#ansible-collections-microsoft-ad-computer-module)
> :   Manage Active Directory computer objects.
>
> [microsoft.ad.domain](domain_module.md#ansible-collections-microsoft-ad-domain-module)
> :   Ensures the existence of a Windows domain.
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
> [Migration guide](docsite/guide_migration.md#ansible-collections-microsoft-ad-docsite-guide-migration-migrated-modules-win-domain-controller)
> :   This module replaces `ansible.windows.win_domain_controller`. See the migration guide for details.
>
> [ansible.windows.win_domain_controller](../../ansible/windows/win_domain_controller_module.md#ansible-collections-ansible-windows-win-domain-controller-module)
> :   Manage domain controller/member server state for a Windows host.

## [Examples](domain_controller_module.md#id6)

```yaml+jinja
- name: Ensure a server is a domain controller
  microsoft.ad.domain_controller:
    dns_domain_name: ansible.vagrant
    domain_admin_user: testguy@ansible.vagrant
    domain_admin_password: password123!
    safe_mode_password: password123!
    state: domain_controller
    reboot: true

- name: Ensure a server is not a domain controller
  microsoft.ad.domain_controller:
    domain_admin_user: testguy@ansible.vagrant
    domain_admin_password: password123!
    local_admin_password: password123!
    state: member_server
    reboot: true

- name: Promote server as a read only domain controller
  microsoft.ad.domain_controller:
    dns_domain_name: ansible.vagrant
    domain_admin_user: testguy@ansible.vagrant
    domain_admin_password: password123!
    safe_mode_password: password123!
    state: domain_controller
    read_only: yes
    site_name: London
    reboot: true

# This scenario is not recommended, use reboot: true when possible
- name: Promote server with custom paths with manual reboot task
  microsoft.ad.domain_controller:
    dns_domain_name: ansible.vagrant
    domain_admin_user: testguy@ansible.vagrant
    domain_admin_password: password123!
    safe_mode_password: password123!
    state: domain_controller
    sysvol_path: D:\SYSVOL
    database_path: D:\NTDS
    domain_log_path: D:\NTDS
  register: dc_promotion

- name: Reboot after promotion
  microsoft.ad.win_reboot:
  when: dc_promotion.reboot_required
```

## [Return Values](domain_controller_module.md#id7)

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
