---
collection: ansible
version: "6"
title: "dellemc.openmanage.idrac_firmware module – Firmware update from a repository on a network share (CIFS, NFS, HTTP, HTTPS, FTP)"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/idrac_firmware_module.html
fetched_at: 2026-07-27T17:25:11+00:00
---
# dellemc.openmanage.idrac_firmware module – Firmware update from a repository on a network share (CIFS, NFS, HTTP, HTTPS, FTP)

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
> see [Requirements](idrac_firmware_module.md#ansible-collections-dellemc-openmanage-idrac-firmware-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.idrac_firmware`.

New in dellemc.openmanage 2.1.0

- [Synopsis](idrac_firmware_module.md#synopsis)
- [Requirements](idrac_firmware_module.md#requirements)
- [Parameters](idrac_firmware_module.md#parameters)
- [Notes](idrac_firmware_module.md#notes)
- [Examples](idrac_firmware_module.md#examples)
- [Return Values](idrac_firmware_module.md#return-values)

## [Synopsis](idrac_firmware_module.md#id1)

- Update the Firmware by connecting to a network share (CIFS, NFS, HTTP, HTTPS, FTP) that contains a catalog of available updates.
- Network share should contain a valid repository of Update Packages (DUPs) and a catalog file describing the DUPs.
- All applicable updates contained in the repository are applied to the system.
- This feature is available only with iDRAC Enterprise License.

## [Requirements](idrac_firmware_module.md#id2)

The below requirements are needed on the host that executes this module.

- omsdk >= 1.2.488
- python >= 3.8.6

## [Parameters](idrac_firmware_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **apply_update**  boolean | If *apply_update* is set to `True`, then the packages are applied.  If *apply_update* is set to `False`, no updates are applied, and a catalog report of packages is generated and returned.  Choices:   - `false` - `true` ← (default) |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **catalog_file_name**  string | Catalog file name relative to the *share_name*.  Default: `"Catalog.xml"` |
| **idrac_ip**  string / required | iDRAC IP Address. |
| **idrac_password**  aliases: idrac_pwd  string / required | iDRAC user password. |
| **idrac_port**  integer | iDRAC port.  Default: `443` |
| **idrac_user**  string / required | iDRAC username. |
| **ignore_cert_warning**  boolean | Specifies if certificate warnings are ignored when HTTPS share is used. If `True` option is set, then the certificate warnings are ignored.  Choices:   - `false` - `true` ← (default) |
| **job_wait**  boolean | Whether to wait for job completion or not.  Choices:   - `false` - `true` ← (default) |
| **reboot**  boolean | Provides the option to apply the update packages immediately or in the next reboot.  If *reboot* is set to `True`, then the packages are applied immediately.  If *reboot* is set to `False`, then the packages are staged and applied in the next reboot.  Packages that do not require a reboot are applied immediately irrespective of I (reboot).  Choices:   - `false` ← (default) - `true` |
| **share_mnt**  string | Local mount path of the network share with read-write permission for ansible user.  This option is not applicable for HTTP, HTTPS, and FTP shares. |
| **share_name**  string / required | Network share path of update repository. CIFS, NFS, HTTP, HTTPS and FTP share types are supported. |
| **share_password**  aliases: share_pwd  string | Network share user password. This option is mandatory for CIFS Network Share. |
| **share_user**  string | Network share user in the format [‘user@domain](mailto:'user%40domain)’ or ‘domain\\user’ if user is part of a domain else ‘user’. This option is mandatory for CIFS Network Share. |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |

## [Notes](idrac_firmware_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to DellEMC iDRAC.
> - Module will report success based on the iDRAC firmware update parent job status if there are no individual component jobs present.
> - For server with iDRAC firmware 5.00.00.00 and later, if the repository contains unsupported packages, then the module will return success with a proper message.
> - This module supports `check_mode`.

## [Examples](idrac_firmware_module.md#id5)

```yaml+jinja
---
- name: Update firmware from repository on a NFS Share
  dellemc.openmanage.idrac_firmware:
       idrac_ip: "192.168.0.1"
       idrac_user: "user_name"
       idrac_password: "user_password"
       ca_path: "/path/to/ca_cert.pem"
       share_name: "192.168.0.0:/share"
       reboot: True
       job_wait: True
       apply_update: True
       catalog_file_name: "Catalog.xml"

- name: Update firmware from repository on a CIFS Share
  dellemc.openmanage.idrac_firmware:
       idrac_ip: "192.168.0.1"
       idrac_user: "user_name"
       idrac_password: "user_password"
       ca_path: "/path/to/ca_cert.pem"
       share_name: "full_cifs_path"
       share_user: "share_user"
       share_password: "share_password"
       reboot: True
       job_wait: True
       apply_update: True
       catalog_file_name: "Catalog.xml"

- name: Update firmware from repository on a HTTP
  dellemc.openmanage.idrac_firmware:
       idrac_ip: "192.168.0.1"
       idrac_user: "user_name"
       idrac_password: "user_password"
       ca_path: "/path/to/ca_cert.pem"
       share_name: "http://downloads.dell.com"
       reboot: True
       job_wait: True
       apply_update: True

- name: Update firmware from repository on a HTTPS
  dellemc.openmanage.idrac_firmware:
       idrac_ip: "192.168.0.1"
       idrac_user: "user_name"
       idrac_password: "user_password"
       ca_path: "/path/to/ca_cert.pem"
       share_name: "https://downloads.dell.com"
       reboot: True
       job_wait: True
       apply_update: True

- name: Update firmware from repository on a FTP
  dellemc.openmanage.idrac_firmware:
       idrac_ip: "192.168.0.1"
       idrac_user: "user_name"
       idrac_password: "user_password"
       ca_path: "/path/to/ca_cert.pem"
       share_name: "ftp://ftp.dell.com"
       reboot: True
       job_wait: True
       apply_update: True
```

## [Return Values](idrac_firmware_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Overall firmware update status.  Returned: always  Sample: `"Successfully updated the firmware."` |
| **update_status**  dictionary | Firmware Update job and progress details from the iDRAC.  Returned: success  Sample: `{"InstanceID": "JID_XXXXXXXXXXXX", "JobStartTime": "NA", "JobState": "Completed", "Message": "Job completed successfully.", "MessageId": "REDXXX", "Name": "Repository Update", "Status": "Success"}` |

### Authors

- Rajeev Arakkal (@rajeevarakkal)
- Felix Stephen (@felixs88)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
