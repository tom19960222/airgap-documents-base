---
collection: ansible
version: "6"
title: "community.windows.win_rds_cap module – Manage Connection Authorization Policies (CAP) on a Remote Desktop Gateway server"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_rds_cap_module.html
fetched_at: 2026-07-27T17:23:49+00:00
---
# community.windows.win_rds_cap module – Manage Connection Authorization Policies (CAP) on a Remote Desktop Gateway server

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
> see [Requirements](win_rds_cap_module.md#ansible-collections-community-windows-win-rds-cap-module-requirements) for details.
>
> To use it in a playbook, specify: `community.windows.win_rds_cap`.

- [Synopsis](win_rds_cap_module.md#synopsis)
- [Requirements](win_rds_cap_module.md#requirements)
- [Parameters](win_rds_cap_module.md#parameters)
- [See Also](win_rds_cap_module.md#see-also)
- [Examples](win_rds_cap_module.md#examples)

## [Synopsis](win_rds_cap_module.md#id1)

- Creates, removes and configures a Remote Desktop connection authorization policy (RD CAP).
- A RD CAP allows you to specify the users who can connect to a Remote Desktop Gateway server.

## [Requirements](win_rds_cap_module.md#id2)

The below requirements are needed on the host that executes this module.

- Windows Server 2008R2 (6.1) or higher.
- The Windows Feature “RDS-Gateway” must be enabled.

## [Parameters](win_rds_cap_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allow_only_sdrts_servers**  boolean | Specifies whether connections are allowed only to Remote Desktop Session Host servers that enforce Remote Desktop Gateway redirection policy.  Choices:   - `false` - `true` |
| **auth_method**  string | Specifies how the RD Gateway server authenticates users.  When a new CAP is created, the default value is `password`.  Choices:   - `"both"` - `"none"` - `"password"` - `"smartcard"` |
| **computer_groups**  list / elements=string | A list of computer groups that is allowed to connect to the Remote Gateway server. |
| **idle_timeout**  integer | Specifies the time interval, in minutes, after which an idle session is disconnected.  A value of zero disables idle timeout. |
| **name**  string / required | Name of the connection authorization policy. |
| **order**  integer | Evaluation order of the policy.  The CAP in which *order* is set to a value of ‘1’ is evaluated first.  By default, a newly created CAP will take the first position.  If the given value exceed the total number of existing policies, the policy will take the last position but the evaluation order will be capped to this number. |
| **redirect_clipboard**  boolean | Allow clipboard redirection.  Choices:   - `false` - `true` |
| **redirect_drives**  boolean | Allow disk drive redirection.  Choices:   - `false` - `true` |
| **redirect_pnp**  boolean | Allow Plug and Play devices redirection.  Choices:   - `false` - `true` |
| **redirect_printers**  boolean | Allow printers redirection.  Choices:   - `false` - `true` |
| **redirect_serial**  boolean | Allow serial port redirection.  Choices:   - `false` - `true` |
| **session_timeout**  integer | The maximum time, in minutes, that a session can be idle.  A value of zero disables session timeout. |
| **session_timeout_action**  string | The action the server takes when a session times out.  `disconnect`: disconnect the session.  `reauth`: silently reauthenticate and reauthorize the session.  Choices:   - `"disconnect"` ← (default) - `"reauth"` |
| **state**  string | The state of connection authorization policy.  If `absent` will ensure the policy is removed.  If `present` will ensure the policy is configured and exists.  If `enabled` will ensure the policy is configured, exists and enabled.  If `disabled` will ensure the policy is configured, exists, but disabled.  Choices:   - `"absent"` - `"enabled"` - `"disabled"` - `"present"` ← (default) |
| **user_groups**  list / elements=string | A list of user groups that is allowed to connect to the Remote Gateway server.  Required when a new CAP is created. |

## [See Also](win_rds_cap_module.md#id4)

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

## [Examples](win_rds_cap_module.md#id5)

```yaml+jinja
- name: Create a new RDS CAP with a 30 minutes timeout and clipboard redirection enabled
  community.windows.win_rds_cap:
    name: My CAP
    user_groups:
      - BUILTIN\users
    session_timeout: 30
    session_timeout_action: disconnect
    allow_only_sdrts_servers: yes
    redirect_clipboard: yes
    redirect_drives: no
    redirect_printers: no
    redirect_serial: no
    redirect_pnp: no
    state: enabled
```

### Authors

- Kevin Subileau (@ksubileau)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
