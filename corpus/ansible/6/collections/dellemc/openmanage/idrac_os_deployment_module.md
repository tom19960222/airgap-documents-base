---
collection: ansible
version: "6"
title: "dellemc.openmanage.idrac_os_deployment module – Boot to a network ISO image"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/idrac_os_deployment_module.html
fetched_at: 2026-07-27T17:25:16+00:00
---
# dellemc.openmanage.idrac_os_deployment module – Boot to a network ISO image

> **Note:**
>
> This module is part of the [dellemc.openmanage collection](https://galaxy.ansible.com/dellemc/openmanage) (version 5.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.openmanage`.
> You need further requirements to be able to use this module,
> see [Requirements](idrac_os_deployment_module.md#ansible-collections-dellemc-openmanage-idrac-os-deployment-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.idrac_os_deployment`.

New in dellemc.openmanage 2.1.0

- [Synopsis](idrac_os_deployment_module.md#synopsis)
- [Requirements](idrac_os_deployment_module.md#requirements)
- [Parameters](idrac_os_deployment_module.md#parameters)
- [Notes](idrac_os_deployment_module.md#notes)
- [Examples](idrac_os_deployment_module.md#examples)
- [Return Values](idrac_os_deployment_module.md#return-values)

## [Synopsis](idrac_os_deployment_module.md#id1)

- Boot to a network ISO image.

## [Requirements](idrac_os_deployment_module.md#id2)

The below requirements are needed on the host that executes this module.

- omsdk >= 1.2.488
- python >= 3.8.6

## [Parameters](idrac_os_deployment_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **expose_duration**  integer | It is the time taken in minutes for the ISO image file to be exposed as a local CD-ROM device to the host server. When the time expires, the ISO image gets automatically detached.  Default: `1080` |
| **idrac_ip**  string / required | iDRAC IP Address. |
| **idrac_password**  aliases: idrac_pwd  string / required | iDRAC user password. |
| **idrac_port**  integer | iDRAC port.  Default: `443` |
| **idrac_user**  string / required | iDRAC username. |
| **iso_image**  string / required | Network ISO name. |
| **share_name**  string / required | CIFS or NFS Network share. |
| **share_password**  aliases: share_pwd  string | Network share user password. This option is mandatory for CIFS Network Share. |
| **share_user**  string | Network share user in the format [‘user@domain](mailto:'user%40domain)’ or ‘domain\\user’ if user is part of a domain else ‘user’. This option is mandatory for CIFS Network Share. |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |

## [Notes](idrac_os_deployment_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to DellEMC iDRAC.
> - This module does not support `check_mode`.

## [Examples](idrac_os_deployment_module.md#id5)

```yaml+jinja
---
- name: Boot to Network ISO
  dellemc.openmanage.idrac_os_deployment:
      idrac_ip: "192.168.0.1"
      idrac_user: "user_name"
      idrac_password: "user_password"
      ca_path: "/path/to/ca_cert.pem"
      share_name: "192.168.0.0:/nfsfileshare"
      iso_image:  "unattended_os_image.iso"
      expose_duration: 180
```

## [Return Values](idrac_os_deployment_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **boot_status**  dictionary | Details of the boot to network ISO image operation.  Returned: always  Sample: `{"DeleteOnCompletion": "false", "InstanceID": "DCIM_OSDConcreteJob:1", "JobName": "BootToNetworkISO", "JobStatus": "Success", "Message": "The command was successful.", "MessageID": "OSD1", "Name": "BootToNetworkISO", "Status": "Success", "file": "192.168.0.0:/nfsfileshare/unattended_os_image.iso", "retval": true}` |
| **msg**  string | Over all device information status.  Returned: on error  Sample: `"Failed to boot to network iso"` |

### Authors

- Felix Stephen (@felixs88)
- Jagadeesh N V (@jagadeeshnv)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
