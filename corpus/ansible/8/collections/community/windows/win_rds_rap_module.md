---
collection: ansible
version: "8"
title: "community.windows.win_rds_rap module – Manage Resource Authorization Policies (RAP) on a Remote Desktop Gateway server"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_rds_rap_module.html
fetched_at: 2026-07-28T02:02:20+00:00
---
# community.windows.win_rds_rap module – Manage Resource Authorization Policies (RAP) on a Remote Desktop Gateway server

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/ui/repo/published/community/windows/) (version 1.13.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
> You need further requirements to be able to use this module,
> see [Requirements](win_rds_rap_module.md#ansible-collections-community-windows-win-rds-rap-module-requirements) for details.
>
> To use it in a playbook, specify: `community.windows.win_rds_rap`.

- [Synopsis](win_rds_rap_module.md#synopsis)
- [Requirements](win_rds_rap_module.md#requirements)
- [Parameters](win_rds_rap_module.md#parameters)
- [See Also](win_rds_rap_module.md#see-also)
- [Examples](win_rds_rap_module.md#examples)

## [Synopsis](win_rds_rap_module.md#id1)

- Creates, removes and configures a Remote Desktop resource authorization policy (RD RAP).
- A RD RAP allows you to specify the network resources (computers) that users can connect to remotely through a Remote Desktop Gateway server.

## [Requirements](win_rds_rap_module.md#id2)

The below requirements are needed on the host that executes this module.

- Windows Server 2008R2 (6.1) or higher.
- The Windows Feature “RDS-Gateway” must be enabled.

## [Parameters](win_rds_rap_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allowed_ports**  list / elements=string | List of port numbers through which connections are allowed for this policy.  To allow connections through any port, specify ‘any’. |
| **computer_group**  string | The computer group name that is associated with this resource authorization policy (RAP).  This is required when *computer_group_type* is `rdg_group` or `ad_network_resource_group`. |
| **computer_group_type**  string | The computer group type:  `rdg_group`: RD Gateway-managed group  `ad_network_resource_group`: Active Directory Domain Services network resource group  `allow_any`: Allow users to connect to any network resource.  **Choices:**   - `"rdg_group"` - `"ad_network_resource_group"` - `"allow_any"` |
| **description**  string | Optional description of the resource authorization policy. |
| **name**  string / required | Name of the resource authorization policy. |
| **state**  string | The state of resource authorization policy.  If `absent` will ensure the policy is removed.  If `present` will ensure the policy is configured and exists.  If `enabled` will ensure the policy is configured, exists and enabled.  If `disabled` will ensure the policy is configured, exists, but disabled.  **Choices:**   - `"absent"` - `"disabled"` - `"enabled"` - `"present"` ← (default) |
| **user_groups**  list / elements=string | List of user groups that are associated with this resource authorization policy (RAP). A user must belong to one of these groups to access the RD Gateway server.  Required when a new RAP is created. |

## [See Also](win_rds_rap_module.md#id4)

> **See also:**
>
> [community.windows.win_rds_cap](win_rds_cap_module.md#ansible-collections-community-windows-win-rds-cap-module)
> :   Manage Connection Authorization Policies (CAP) on a Remote Desktop Gateway server.
>
> [community.windows.win_rds_rap](win_rds_rap_module.md#ansible-collections-community-windows-win-rds-rap-module)
> :   Manage Resource Authorization Policies (RAP) on a Remote Desktop Gateway server.
>
> [community.windows.win_rds_settings](win_rds_settings_module.md#ansible-collections-community-windows-win-rds-settings-module)
> :   Manage main settings of a Remote Desktop Gateway server.

## [Examples](win_rds_rap_module.md#id5)

```yaml+jinja
- name: Create a new RDS RAP
  community.windows.win_rds_rap:
    name: My RAP
    description: Allow all users to connect to any resource through ports 3389 and 3390
    user_groups:
      - BUILTIN\users
    computer_group_type: allow_any
    allowed_ports:
      - 3389
      - 3390
    state: enabled
```

### Authors

- Kevin Subileau (@ksubileau)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
