---
collection: ansible
version: "8"
title: "dellemc.openmanage.idrac_reset role – Role to reset and restart iDRAC"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/idrac_reset_role.html
fetched_at: 2026-07-28T02:05:04+00:00
---
# dellemc.openmanage.idrac_reset role – Role to reset and restart iDRAC

> **Note:**
>
> This role is part of the [dellemc.openmanage collection](https://galaxy.ansible.com/ui/repo/published/dellemc/openmanage/) (version 7.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it use: `ansible-galaxy collection install dellemc.openmanage`.
>
> To use it in a playbook, specify: `dellemc.openmanage.idrac_reset`.

- [Entry point `main` – Role to reset and restart iDRAC](idrac_reset_role.md#entry-point-main-role-to-reset-and-restart-idrac)

  - [Synopsis](idrac_reset_role.md#synopsis)
  - [Parameters](idrac_reset_role.md#parameters)

## [Entry point `main` – Role to reset and restart iDRAC](idrac_reset_role.md#id1)

New in dellemc.openmanage 7.6.0

### [Synopsis](idrac_reset_role.md#id2)

- Role to reset and restart iDRAC (iDRAC8 and iDRAC9 only) for Dell PowerEdge servers.

### [Parameters](idrac_reset_role.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **force_reset**  boolean | Force restart the idrac without checking the idrac lifecycle controller status.  **Choices:**   - `false` ← (default) - `true` |
| **hostname**  string / required | iDRAC IP Address or hostname. |
| **https_port**  integer | iDRAC port.  **Default:** `443` |
| **https_timeout**  integer | The HTTPS socket level timeout in seconds.  **Default:** `30` |
| **password**  string / required | iDRAC user password. |
| **reset_to_default**  string | Reset the iDRAC to factory default settings.  If this value is not set, then the default behaviour is to restart the iDRAC.  `All`This action will reset your iDRAC to the factory defaults. SupportAssist settings including registration information will be permanently removed. Username and password will reset to default credentials.  `ResetAllWithRootDefaults`This action will reset your iDRAC to the factory defaults. SupportAssist settings including registration information will be permanently removed. Default username will reset to root and password to the shipping value (root/shipping value).  `Default`This action will reset your iDRAC to the factory defaults. SupportAssist settings including registration information will be permanently removed. User and network settings will be preserved.  Note: Supported only for iDRAC9.  **Choices:**   - `"All"` - `"ResetAllWithRootDefaults"` - `"Default"` |
| **username**  string / required | iDRAC username with admin privileges. |
| **validate_certs**  boolean | If `false`, the SSL certificates will not be validated.  Configure `false` only on personally controlled sites where self-signed certificates are used.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_idrac**  boolean | Wait for the iDRAC to restart and LC status to be ready.  When *reset_to_default* is `All`, the IP address of iDRAC might not be accessible because of the change in network settings.  When *reset_to_default* is `ResetAllWithRootDefaults`, the IP address of iDRAC might not be accessible because of the change in network settings.  **Choices:**   - `false` - `true` ← (default) |

#### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
