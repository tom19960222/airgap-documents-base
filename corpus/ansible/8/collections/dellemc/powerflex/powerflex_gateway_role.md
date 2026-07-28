---
collection: ansible
version: "8"
title: "dellemc.powerflex.powerflex_gateway role – Role to manage the installation and uninstallation of PowerFlex gateway"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/powerflex/powerflex_gateway_role.html
fetched_at: 2026-07-28T02:05:18+00:00
---
# dellemc.powerflex.powerflex_gateway role – Role to manage the installation and uninstallation of PowerFlex gateway

> **Note:**
>
> This role is part of the [dellemc.powerflex collection](https://galaxy.ansible.com/ui/repo/published/dellemc/powerflex/) (version 1.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it use: `ansible-galaxy collection install dellemc.powerflex`.
>
> To use it in a playbook, specify: `dellemc.powerflex.powerflex_gateway`.

- [Entry point `main` – Role to manage the installation and uninstallation of PowerFlex gateway](powerflex_gateway_role.md#entry-point-main-role-to-manage-the-installation-and-uninstallation-of-powerflex-gateway)

  - [Synopsis](powerflex_gateway_role.md#synopsis)
  - [Parameters](powerflex_gateway_role.md#parameters)

## [Entry point `main` – Role to manage the installation and uninstallation of PowerFlex gateway](powerflex_gateway_role.md#id1)

### [Synopsis](powerflex_gateway_role.md#id2)

- Role to manage the installation and uninstallation of PowerFlex gateway.

### [Parameters](powerflex_gateway_role.md#id3)

| Parameter | Comments |
| --- | --- |
| **powerflex_common_file_install_location**  path | Location of installation, compatible installation software package based on the operating system of the node.  The files can be downloaded from the Dell Product support page for the PowerFlex software.  **Default:** `"/var/tmp"` |
| **powerflex_gateway_admin_password**  string / required | Admin password for the PowerFlex gateway. |
| **powerflex_gateway_http_port**  integer | PowerFlex gateway HTTP port.  **Default:** `80` |
| **powerflex_gateway_https_port**  integer | PowerFlex gateway HTTPS port.  **Default:** `443` |
| **powerflex_gateway_is_redundant**  boolean | Is the gateway redundant (will install keepalived)  **Choices:**   - `false` ← (default) - `true` |
| **powerflex_gateway_skip_java**  boolean | Specifies whether to install java or not.  **Choices:**   - `false` ← (default) - `true` |
| **powerflex_gateway_state**  string | State of the PowerFlex gateway.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **powerflex_gateway_virtual_interface**  string | Virtual interface of PowerFlex gateway. |
| **powerflex_gateway_virtual_ip**  string | Virtual IP address of PowerFlex gateway. |

#### Collection links

- [Issue Tracker](https://www.dell.com/community/Automation/bd-p/Automation)
- [Repository (Sources)](https://github.com/dell/ansible-powerflex/tree/1.9.0)
