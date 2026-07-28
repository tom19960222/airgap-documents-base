---
collection: ansible
version: "6"
title: "ansible.windows.win_domain_membership module – Manage domain/workgroup membership for a Windows host"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/windows/win_domain_membership_module.html
fetched_at: 2026-07-27T16:44:54+00:00
---
# ansible.windows.win_domain_membership module – Manage domain/workgroup membership for a Windows host

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
> To use it in a playbook, specify: `ansible.windows.win_domain_membership`.

- [Synopsis](win_domain_membership_module.md#synopsis)
- [Parameters](win_domain_membership_module.md#parameters)
- [See Also](win_domain_membership_module.md#see-also)
- [Examples](win_domain_membership_module.md#examples)
- [Return Values](win_domain_membership_module.md#return-values)

## [Synopsis](win_domain_membership_module.md#id1)

- Manages domain membership or workgroup membership for a Windows host. Also supports hostname changes.
- This module may require subsequent use of the [ansible.windows.win_reboot](win_reboot_module.md#ansible-collections-ansible-windows-win-reboot-module) action if changes are made.

## [Parameters](win_domain_membership_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **dns_domain_name**  string | When `state` is `domain`, the DNS name of the domain to which the targeted Windows host should be joined. |
| **domain_admin_password**  string | Password for the specified `domain_admin_user`. |
| **domain_admin_user**  string / required | Username of a domain admin for the target domain (required to join or leave the domain). |
| **domain_ou_path**  string | The desired OU path for adding the computer object.  This is only used when adding the target host to a domain, if it is already a member then it is ignored. |
| **hostname**  string | The desired hostname for the Windows host. |
| **state**  string | Whether the target host should be a member of a domain or workgroup.  Choices:   - `"domain"` - `"workgroup"` |
| **workgroup_name**  string | When `state` is `workgroup`, the name of the workgroup that the Windows host should be in. |

## [See Also](win_domain_membership_module.md#id3)

> **See also:**
>
> [ansible.windows.win_domain](win_domain_module.md#ansible-collections-ansible-windows-win-domain-module)
> :   Ensures the existence of a Windows domain.
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
> [community.windows.win_domain_user](../../community/windows/win_domain_user_module.md#ansible-collections-community-windows-win-domain-user-module)
> :   Manages Windows Active Directory user accounts.
>
> [ansible.windows.win_group](win_group_module.md#ansible-collections-ansible-windows-win-group-module)
> :   Add and remove local groups.
>
> [ansible.windows.win_group_membership](win_group_membership_module.md#ansible-collections-ansible-windows-win-group-membership-module)
> :   Manage Windows local group membership.
>
> [ansible.windows.win_user](win_user_module.md#ansible-collections-ansible-windows-win-user-module)
> :   Manages local Windows user accounts.

## [Examples](win_domain_membership_module.md#id4)

```yaml+jinja
# host should be a member of domain ansible.vagrant; module will ensure the hostname is mydomainclient
# and will use the passed credentials to join domain if necessary.
# Ansible connection should use local credentials if possible.
# If a reboot is required, the second task will trigger one and wait until the host is available.
- hosts: winclient
  gather_facts: no
  tasks:
  - ansible.windows.win_domain_membership:
      dns_domain_name: ansible.vagrant
      hostname: mydomainclient
      domain_admin_user: testguy@ansible.vagrant
      domain_admin_password: password123!
      domain_ou_path: "OU=Windows,OU=Servers,DC=ansible,DC=vagrant"
      state: domain
    register: domain_state

  - ansible.windows.win_reboot:
    when: domain_state.reboot_required

# Host should be in workgroup mywg- module will use the passed credentials to clean-unjoin domain if possible.
# Ansible connection should use local credentials if possible.
# The domain admin credentials can be sourced from a vault-encrypted variable
- hosts: winclient
  gather_facts: no
  tasks:
  - ansible.windows.win_domain_membership:
      workgroup_name: mywg
      domain_admin_user: '{{ win_domain_admin_user }}'
      domain_admin_password: '{{ win_domain_admin_password }}'
      state: workgroup
```

## [Return Values](win_domain_membership_module.md#id5)

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
