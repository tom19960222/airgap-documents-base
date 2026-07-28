---
collection: ansible
version: "8"
title: "dellemc.openmanage.redfish_firmware role – Update a component firmware using the image file available on the local or remote system"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/redfish_firmware_role.html
fetched_at: 2026-07-28T02:05:06+00:00
---
# dellemc.openmanage.redfish_firmware role – Update a component firmware using the image file available on the local or remote system

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
> To use it in a playbook, specify: `dellemc.openmanage.redfish_firmware`.

- [Entry point `main` – Update a component firmware using the image file available on the local or remote system](redfish_firmware_role.md#entry-point-main-update-a-component-firmware-using-the-image-file-available-on-the-local-or-remote-system)

  - [Synopsis](redfish_firmware_role.md#synopsis)
  - [Parameters](redfish_firmware_role.md#parameters)

## [Entry point `main` – Update a component firmware using the image file available on the local or remote system](redfish_firmware_role.md#id1)

New in dellemc.openmanage 7.5.0

### [Synopsis](redfish_firmware_role.md#id2)

- This module allows the firmware update of only one component at a time. If the module is run for more than one component, an error message is returned.
- Depending on the component, the firmware update is applied after an automatic or manual reboot.

### [Parameters](redfish_firmware_role.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **hostname**  string / required | iDRAC IP Address or hostname. |
| **http_timeout**  integer | The socket level timeout in seconds.  **Default:** `30` |
| **https_port**  integer | iDRAC port.  **Default:** `443` |
| **image_uri**  string / required | Firmware Image location URI or local path.  For example- <http://%3Cweb_address%3E/components.exe> or /home/firmware_repo/component.exe. |
| **job_wait**  boolean | Provides the option to wait for job completion.  **Choices:**   - `false` - `true` ← (default) |
| **job_wait_timeout**  integer | The maximum wait time of *job_wait* in seconds. The job is tracked only for this duration.  This option is applicable when *job_wait* is `True`.  **Default:** `3600` |
| **password**  string / required | iDRAC user password. |
| **transfer_protocol**  string | Protocol used to transfer the firmware image file. Applicable for URI based update.  **Choices:**   - `"CIFS"` - `"FTP"` - `"HTTP"` ← (default) - `"HTTPS"` - `"NSF"` - `"OEM"` - `"SCP"` - `"SFTP"` - `"TFTP"` |
| **username**  string / required | iDRAC username with admin privileges. |
| **validate_certs**  boolean | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version 5.0.0, *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

#### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
