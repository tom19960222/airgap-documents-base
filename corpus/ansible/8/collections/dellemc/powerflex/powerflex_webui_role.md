---
collection: ansible
version: "8"
title: "dellemc.powerflex.powerflex_webui role – Role to manage the installation and uninstallation of Powerflex web UI."
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/powerflex/powerflex_webui_role.html
fetched_at: 2026-07-28T02:05:19+00:00
---
# dellemc.powerflex.powerflex_webui role – Role to manage the installation and uninstallation of Powerflex web UI.

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
> To use it in a playbook, specify: `dellemc.powerflex.powerflex_webui`.

- [Entry point `main` – Role to manage the installation and uninstallation of Powerflex web UI.](powerflex_webui_role.md#entry-point-main-role-to-manage-the-installation-and-uninstallation-of-powerflex-web-ui)

  - [Synopsis](powerflex_webui_role.md#synopsis)
  - [Parameters](powerflex_webui_role.md#parameters)

## [Entry point `main` – Role to manage the installation and uninstallation of Powerflex web UI.](powerflex_webui_role.md#id1)

### [Synopsis](powerflex_webui_role.md#id2)

- Role to manage the installation and uninstallation of Powerflex web UI.

### [Parameters](powerflex_webui_role.md#id3)

| Parameter | Comments |
| --- | --- |
| **hostname**  string / required | IP or FQDN of the PowerFlex gateway. |
| **password**  string / required | The password of the PowerFlex gateway. |
| **port**  integer | Port of the PowerFlex gateway.  **Default:** `443` |
| **powerflex_common_file_install_location**  path | Location of installation, compatible installation software package based on the operating system of the node.  The files can be downloaded from the Dell Product support page for PowerFlex software.  **Default:** `"/var/tmp"` |
| **powerflex_webui_skip_java**  boolean | Specifies whether to install java or not.  **Choices:**   - `false` ← (default) - `true` |
| **powerflex_webui_state**  string | Specifies the state of the web UI.  present will install the web UI if not already installed.  absent will uninstall the web UI if installed.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **timeout**  integer | Time after which connection will get terminated.  **Default:** `120` |
| **username**  string / required | The username of the PowerFlex gateway. |
| **validate_certs**  boolean | If `false`, the SSL certificates will not be validated.  Configure `false` only on personally controlled sites where self-signed certificates are used.  **Choices:**   - `false` ← (default) - `true` |

#### Collection links

- [Issue Tracker](https://www.dell.com/community/Automation/bd-p/Automation)
- [Repository (Sources)](https://github.com/dell/ansible-powerflex/tree/1.9.0)
