---
collection: ansible
version: "6"
title: "ansible.windows.win_domain_controller module – Manage domain controller/member server state for a Windows host"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/windows/win_domain_controller_module.html
fetched_at: 2026-07-27T16:44:54+00:00
---
# ansible.windows.win_domain_controller module – Manage domain controller/member server state for a Windows host

> **Note:**
>
> This module is part of the [ansible.windows collection](https://galaxy.ansible.com/ansible/windows) (version 1.12.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.windows`.
>
> To use it in a playbook, specify: `ansible.windows.win_domain_controller`.

- [Synopsis](win_domain_controller_module.md#synopsis)
- [Parameters](win_domain_controller_module.md#parameters)
- [See Also](win_domain_controller_module.md#see-also)
- [Examples](win_domain_controller_module.md#examples)
- [Return Values](win_domain_controller_module.md#return-values)

## [Synopsis](win_domain_controller_module.md#id1)

- Ensure that a Windows Server 2012+ host is configured as a domain controller or demoted to member server.
- This module may require subsequent use of the [ansible.windows.win_reboot](win_reboot_module.md#ansible-collections-ansible-windows-win-reboot-module) action if changes are made.

## [Parameters](win_domain_controller_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **database_path**  path | The path to a directory on a fixed disk of the Windows host where the domain database will be created..  If not set then the default path is `%SYSTEMROOT%\NTDS`. |
| **dns_domain_name**  string | When `state` is `domain_controller`, the DNS name of the domain for which the targeted Windows host should be a DC. |
| **domain_admin_password**  string / required | Password for the specified `domain_admin_user`. |
| **domain_admin_user**  string / required | Username of a domain admin for the target domain (necessary to promote or demote a domain controller). |
| **domain_log_path**  path | Specified the fully qualified, non-UNC path to a directory on a fixed disk of the local computer that will contain the domain log files. |
| **install_dns**  boolean | Whether to install the DNS service when creating the domain controller.  If not specified then the `-InstallDns` option is not supplied to `Install-ADDSDomainController` command, see <https://docs.microsoft.com/en-us/powershell/module/addsdeployment/install-addsdomaincontroller>.  Choices:   - `false` - `true` |
| **install_media_path**  path | The path to a directory on a fixed disk of the Windows host where the Install From Media `IFC` data will be used.  See the [Install using IFM guide](https://social.technet.microsoft.com/wiki/contents/articles/8630.active-directory-step-by-step-guide-to-install-an-additional-domain-controller-using-ifm.aspx) for more information. |
| **local_admin_password**  string | Password to be assigned to the local `Administrator` user (required when `state` is `member_server`). |
| **log_path**  string | The path to log any debug information when running the module.  This option is deprecated and should not be used, it will be removed on the major release after `2022-07-01`.  This does not relate to the `-LogPath` paramter of the install controller cmdlet. |
| **read_only**  boolean | Whether to install the domain controller as a read only replica for an existing domain.  Choices:   - `false` ← (default) - `true` |
| **safe_mode_password**  string | Safe mode password for the domain controller (required when `state` is `domain_controller`). |
| **site_name**  string | Specifies the name of an existing site where you can place the new domain controller.  This option is required when *read_only* is `yes`. |
| **state**  string / required | Whether the target host should be a domain controller or a member server.  Choices:   - `"domain_controller"` - `"member_server"` |
| **sysvol_path**  path | The path to a directory on a fixed disk of the Windows host where the Sysvol folder will be created.  If not set then the default path is `%SYSTEMROOT%\SYSVOL`. |

## [See Also](win_domain_controller_module.md#id3)

> **See also:**
>
> [ansible.windows.win_domain](win_domain_module.md#ansible-collections-ansible-windows-win-domain-module)
> :   Ensures the existence of a Windows domain.
>
> [community.windows.win_domain_computer](../../community/windows/win_domain_computer_module.md#ansible-collections-community-windows-win-domain-computer-module)
> :   Manage computers in Active Directory.
>
> [community.windows.win_domain_group](../../community/windows/win_domain_group_module.md#ansible-collections-community-windows-win-domain-group-module)
> :   Creates, modifies or removes domain groups.
>
> [ansible.windows.win_domain_membership](win_domain_membership_module.md#ansible-collections-ansible-windows-win-domain-membership-module)
> :   Manage domain/workgroup membership for a Windows host.
>
> [community.windows.win_domain_user](../../community/windows/win_domain_user_module.md#ansible-collections-community-windows-win-domain-user-module)
> :   Manages Windows Active Directory user accounts.

## [Examples](win_domain_controller_module.md#id4)

```yaml+jinja
- name: Ensure a server is a domain controller
  ansible.windows.win_domain_controller:
    dns_domain_name: ansible.vagrant
    domain_admin_user: testguy@ansible.vagrant
    domain_admin_password: password123!
    safe_mode_password: password123!
    state: domain_controller

# note that without an action wrapper, in the case where a DC is demoted,
# the task will fail with a 401 Unauthorized, because the domain credential
# becomes invalid to fetch the final output over WinRM. This requires win_async
# with credential switching (or other clever credential-switching
# mechanism to get the output and trigger the required reboot)
- name: Ensure a server is not a domain controller
  ansible.windows.win_domain_controller:
    domain_admin_user: testguy@ansible.vagrant
    domain_admin_password: password123!
    local_admin_password: password123!
    state: member_server

- name: Promote server as a read only domain controller
  ansible.windows.win_domain_controller:
    dns_domain_name: ansible.vagrant
    domain_admin_user: testguy@ansible.vagrant
    domain_admin_password: password123!
    safe_mode_password: password123!
    state: domain_controller
    read_only: yes
    site_name: London

- name: Promote server with custom paths
  ansible.windows.win_domain_controller:
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
  ansible.windows.win_reboot:
  when: dc_promotion.reboot_required
```

## [Return Values](win_domain_controller_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **reboot_required**  boolean | True if changes were made that require a reboot.  Returned: always  Sample: `true` |

### Authors

- Matt Davis (@nitzmahone)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
[Communication](index.md#communication-for-ansible-windows)
