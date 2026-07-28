---
collection: ansible
version: "6"
title: "ansible.windows.win_domain module – Ensures the existence of a Windows domain"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/windows/win_domain_module.html
fetched_at: 2026-07-27T16:44:54+00:00
---
# ansible.windows.win_domain module – Ensures the existence of a Windows domain

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
> To use it in a playbook, specify: `ansible.windows.win_domain`.

- [Synopsis](win_domain_module.md#synopsis)
- [Parameters](win_domain_module.md#parameters)
- [See Also](win_domain_module.md#see-also)
- [Examples](win_domain_module.md#examples)
- [Return Values](win_domain_module.md#return-values)

## [Synopsis](win_domain_module.md#id1)

- Ensure that the domain named by `dns_domain_name` exists and is reachable.
- If the domain is not reachable, the domain is created in a new forest on the target Windows Server 2012R2+ host.
- This module may require subsequent use of the [ansible.windows.win_reboot](win_reboot_module.md#ansible-collections-ansible-windows-win-reboot-module) action if changes are made.

## [Parameters](win_domain_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **create_dns_delegation**  boolean | Whether to create a DNS delegation that references the new DNS server that you install along with the domain controller.  Valid for Active Directory-integrated DNS only.  The default is computed automatically based on the environment.  Choices:   - `false` - `true` |
| **database_path**  path | The path to a directory on a fixed disk of the Windows host where the domain database will be created.  If not set then the default path is `%SYSTEMROOT%\NTDS`. |
| **dns_domain_name**  string / required | The DNS name of the domain which should exist and be reachable or reside on the target Windows host. |
| **domain_mode**  string | Specifies the domain functional level of the first domain in the creation of a new forest.  The domain functional level cannot be lower than the forest functional level, but it can be higher.  The default is automatically computed and set.  Choices:   - `"Win2003"` - `"Win2008"` - `"Win2008R2"` - `"Win2012"` - `"Win2012R2"` - `"WinThreshold"` |
| **domain_netbios_name**  string | The NetBIOS name for the root domain in the new forest.  For NetBIOS names to be valid for use with this parameter they must be single label names of 15 characters or less, if not it will fail.  If this parameter is not set, then the default is automatically computed from the value of the *domain_name* parameter. |
| **forest_mode**  string | Specifies the forest functional level for the new forest.  The default forest functional level in Windows Server is typically the same as the version you are running.  Choices:   - `"Win2003"` - `"Win2008"` - `"Win2008R2"` - `"Win2012"` - `"Win2012R2"` - `"WinThreshold"` |
| **install_dns**  boolean | Whether to install the DNS service when creating the domain controller.  Choices:   - `false` - `true` ← (default) |
| **log_path**  path | Specifies the fully qualified, non-UNC path to a directory on a fixed disk of the local computer where the log file for this operation is written.  If not set then the default path is `%SYSTEMROOT%\NTDS`. |
| **safe_mode_password**  string / required | Safe mode password for the domain controller. |
| **sysvol_path**  path | The path to a directory on a fixed disk of the Windows host where the Sysvol file will be created.  If not set then the default path is `%SYSTEMROOT%\SYSVOL`. |

## [See Also](win_domain_module.md#id3)

> **See also:**
>
> [ansible.windows.win_domain_controller](win_domain_controller_module.md#ansible-collections-ansible-windows-win-domain-controller-module)
> :   Manage domain controller/member server state for a Windows host.
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

## [Examples](win_domain_module.md#id4)

```yaml+jinja
- name: Create new domain in a new forest on the target host
  ansible.windows.win_domain:
    dns_domain_name: ansible.vagrant
    safe_mode_password: password123!

- name: Create new Windows domain in a new forest with specific parameters
  ansible.windows.win_domain:
    create_dns_delegation: no
    database_path: C:\Windows\NTDS
    dns_domain_name: ansible.vagrant
    domain_mode: Win2012R2
    domain_netbios_name: ANSIBLE
    forest_mode: Win2012R2
    safe_mode_password: password123!
    sysvol_path: C:\Windows\SYSVOL
  register: domain_install
```

## [Return Values](win_domain_module.md#id5)

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
