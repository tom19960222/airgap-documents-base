---
collection: ansible
version: "8"
title: "dellemc.openmanage.idrac_os_deployment role – Role to deploy specified operating system and version on the servers"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/idrac_os_deployment_role.html
fetched_at: 2026-07-28T02:05:04+00:00
---
# dellemc.openmanage.idrac_os_deployment role – Role to deploy specified operating system and version on the servers

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
> To use it in a playbook, specify: `dellemc.openmanage.idrac_os_deployment`.

- [Entry point `main` – Role to deploy specified operating system and version on the servers](idrac_os_deployment_role.md#entry-point-main-role-to-deploy-specified-operating-system-and-version-on-the-servers)

  - [Synopsis](idrac_os_deployment_role.md#synopsis)
  - [Parameters](idrac_os_deployment_role.md#parameters)

## [Entry point `main` – Role to deploy specified operating system and version on the servers](idrac_os_deployment_role.md#id1)

New in dellemc.openmanage 7.5.0

### [Synopsis](idrac_os_deployment_role.md#id2)

- Role to deploy specified operating system and version on the servers.

### [Parameters](idrac_os_deployment_role.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **dest_os**  string | HTTP/HTTPS share based on linux/Windows.  **Choices:**   - `"linux"` ← (default) - `"windows"` |
| **destination_path**  dictionary / required | Share path to mount the ISO to iDRAC.  Share needs to have a write permission to copy the generated ISO.  CIFS, NFS, HTTP and HTTPS shares are supported. |
| **password**  string | Password of the network share destination of customized ISO. |
| **path**  path / required | Path of the network share to copy the customized ISO. |
| **username**  string | Username of the network share destination of customized ISO. |
| **eject_iso**  boolean | Eject the virtual media (ISO) after the tracking of OS deployment is finished.  **Choices:**   - `false` - `true` ← (default) |
| **hostname**  string / required | iDRAC IP Address. |
| **http_path**  string | Path to copy custom_iso in http or https share |
| **https_port**  integer | iDRAC port.  **Default:** `443` |
| **https_timeout**  integer | The socket level timeout in seconds.  **Default:** `30` |
| **kickstart_file**  path | Local path of the kickstart file.  Generation of kickstart file will be ignored if a kickstart file is provided. |
| **os_name**  string / required | The operating system name to match the jinja template of the kickstart file. |
| **os_version**  string / required | The operating system version to match the jinja template of the kickstart file.  Supported versions for RHEL are 9.x and 8.x and for ESXi is 8.x. |
| **os_wait**  boolean | Wait for the OS deployment to finish.  **Choices:**   - `false` - `true` ← (default) |
| **os_wait_time**  integer | Time in minutes to wait for the OS deployment to finish.  **Default:** `30` |
| **password**  string / required | iDRAC user password. |
| **source_iso**  dictionary / required | Network share or local path of the ISO. |
| **password**  string | Password of the network share. |
| **path**  path / required | Local path or network share path of the ISO.  CIFS, NFS, HTTP and HTTPS shares are supported. |
| **username**  string | Username of the network share. |
| **ssh_pass**  string | Password for SSH login into the target machine where the custom iso will be copied to serve from the http/https repository. |
| **ssh_user**  string | Username for SSH login into the target machine where the custom iso will be copied to serve from the http/https repository. |
| **username**  string / required | iDRAC username. |
| **validate_certs**  boolean | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  **Choices:**   - `false` - `true` ← (default) |

#### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
