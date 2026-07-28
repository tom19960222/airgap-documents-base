---
collection: ansible
version: "6"
title: "community.windows.win_rds_settings module – Manage main settings of a Remote Desktop Gateway server"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_rds_settings_module.html
fetched_at: 2026-07-27T17:23:50+00:00
---
# community.windows.win_rds_settings module – Manage main settings of a Remote Desktop Gateway server

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
> see [Requirements](win_rds_settings_module.md#ansible-collections-community-windows-win-rds-settings-module-requirements) for details.
>
> To use it in a playbook, specify: `community.windows.win_rds_settings`.

- [Synopsis](win_rds_settings_module.md#synopsis)
- [Requirements](win_rds_settings_module.md#requirements)
- [Parameters](win_rds_settings_module.md#parameters)
- [See Also](win_rds_settings_module.md#see-also)
- [Examples](win_rds_settings_module.md#examples)

## [Synopsis](win_rds_settings_module.md#id1)

- Configure general settings of a Remote Desktop Gateway server.

## [Requirements](win_rds_settings_module.md#id2)

The below requirements are needed on the host that executes this module.

- Windows Server 2008R2 (6.1) or higher.
- The Windows Feature “RDS-Gateway” must be enabled.

## [Parameters](win_rds_settings_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **certificate_hash**  string | Certificate hash (thumbprint) for the Remote Desktop Gateway server. The certificate hash is the unique identifier for the certificate. |
| **enable_only_messaging_capable_clients**  boolean | If enabled, only clients that support logon messages and administrator messages can connect.  Choices:   - `false` - `true` |
| **max_connections**  integer | The maximum number of connections allowed.  If set to `0`, no new connections are allowed.  If set to `-1`, the number of connections is unlimited. |
| **ssl_bridging**  string | Specifies whether to use SSL Bridging.  `none`: no SSL bridging.  `https_http`: HTTPS-HTTP bridging.  `https_https`: HTTPS-HTTPS bridging.  Choices:   - `"https_http"` - `"https_https"` - `"none"` |

## [See Also](win_rds_settings_module.md#id4)

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

## [Examples](win_rds_settings_module.md#id5)

```yaml+jinja
- name: Configure the Remote Desktop Gateway
  community.windows.win_rds_settings:
    certificate_hash: B0D0FA8408FC67B230338FCA584D03792DA73F4C
    max_connections: 50
  notify:
    - Restart TSGateway service
```

### Authors

- Kevin Subileau (@ksubileau)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
