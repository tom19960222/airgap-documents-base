---
collection: ansible
version: "8"
title: "dellemc.openmanage.idrac_virtual_media module – Configure the Remote File Share settings."
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/idrac_virtual_media_module.html
fetched_at: 2026-07-28T02:04:15+00:00
---
# dellemc.openmanage.idrac_virtual_media module – Configure the Remote File Share settings.

> **Note:**
>
> This module is part of the [dellemc.openmanage collection](https://galaxy.ansible.com/ui/repo/published/dellemc/openmanage/) (version 7.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.openmanage`.
> You need further requirements to be able to use this module,
> see [Requirements](idrac_virtual_media_module.md#ansible-collections-dellemc-openmanage-idrac-virtual-media-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.idrac_virtual_media`.

New in dellemc.openmanage 6.3.0

- [Synopsis](idrac_virtual_media_module.md#synopsis)
- [Requirements](idrac_virtual_media_module.md#requirements)
- [Parameters](idrac_virtual_media_module.md#parameters)
- [Notes](idrac_virtual_media_module.md#notes)
- [Examples](idrac_virtual_media_module.md#examples)
- [Return Values](idrac_virtual_media_module.md#return-values)

## [Synopsis](idrac_virtual_media_module.md#id1)

- This module allows to configure Remote File Share settings.

## [Requirements](idrac_virtual_media_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](idrac_virtual_media_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **force**  boolean | `True` ejects the image file if already connected and inserts the file provided in *image*. This is applicable when *insert* is `True`.  **Choices:**   - `false` ← (default) - `true` |
| **idrac_ip**  string / required | iDRAC IP Address. |
| **idrac_password**  aliases: idrac_pwd  string / required | iDRAC user password. |
| **idrac_port**  integer | iDRAC port.  **Default:** `443` |
| **idrac_user**  string / required | iDRAC username. |
| **resource_id**  string | Resource id of the iDRAC, if not specified manager collection id will be used. |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |
| **virtual_media**  list / elements=dictionary / required | Details of the Remote File Share. |
| **domain**  string | Domain name of network share. This option is applicable for CIFS and HTTPS share. |
| **image**  path | The path of the image file. The supported file types are .img and .iso.  The file name with .img extension is redirected as a virtual floppy and a file name with .iso extension is redirected as a virtual CDROM.  This option is required when *insert* is `True`.  The following are the examples of the share location: CIFS share: //192.168.0.1/file_path/image_name.iso, NFS share: 192.168.0.2:/file_path/image_name.img, HTTP share: <http://192.168.0.3/file_path/image_name.iso>, HTTPS share: <https://192.168.0.4/file_path/image_name.img>  CIFS share is not supported by iDRAC7 and iDRAC8.  HTTPS share with credentials is not supported by iDRAC7 and iDRAC8. |
| **index**  integer | Index of the Remote File Share. For example, to specify the Remote File Share 1, the value of *index* should be 1. If *index* is not specified, the order of *virtual_media* list will be considered. |
| **insert**  boolean / required | `True` connects the remote image file.  `False` ejects the remote image file if connected.  **Choices:**   - `false` - `true` |
| **media_type**  string | Type of the image file. This is applicable when *insert* is `True`.  **Choices:**   - `"CD"` - `"DVD"` - `"USBStick"` |
| **password**  string | Network share password. This option is applicable for CIFS and HTTPS share.  This module always reports as the changes found when *password* is provided. |
| **username**  string | Network share username. This option is applicable for CIFS and HTTPS share. |

## [Notes](idrac_virtual_media_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to Dell iDRAC.
> - This module supports `check_mode`.

## [Examples](idrac_virtual_media_module.md#id5)

```yaml+jinja
---
- name: Insert image file to Remote File Share 1 using CIFS share.
  dellemc.openmanage.idrac_virtual_media:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    virtual_media:
      - insert: true
        image: "//192.168.0.2/file_path/file.iso"
        username: "username"
        password: "password"

- name: Insert image file to Remote File Share 2 using NFS share.
  dellemc.openmanage.idrac_virtual_media:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    virtual_media:
      - index: 2
        insert: true
        image: "192.168.0.4:/file_path/file.iso"

- name: Insert image file to Remote File Share 1 and 2 using HTTP.
  dellemc.openmanage.idrac_virtual_media:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    force: true
    virtual_media:
      - index: 1
        insert: true
        image: "http://192.168.0.4/file_path/file.img"
      - index: 2
        insert: true
        image: "http://192.168.0.4/file_path/file.img"

- name: Insert image file using HTTPS.
  dellemc.openmanage.idrac_virtual_media:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    force: true
    virtual_media:
      - index: 1
        insert: true
        image: "https://192.168.0.5/file_path/file.img"
        username: username
        password: password

- name: Eject multiple virtual media.
  dellemc.openmanage.idrac_virtual_media:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    force: true
    virtual_media:
      - index: 1
        insert: false
      - index: 2
        insert: false

- name: Ejection of image file from Remote File Share 1.
  dellemc.openmanage.idrac_virtual_media:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    force: true
    virtual_media:
        insert: false

- name: Insertion and ejection of image file in single task.
  dellemc.openmanage.idrac_virtual_media:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    force: true
    virtual_media:
      - index: 1
        insert: true
        image: https://192.168.0.5/file/file.iso
        username: username
        password: password
      - index: 2
        insert: false
```

## [Return Values](idrac_virtual_media_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  **Returned:** on HTTP error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Successfully performed the virtual media operation.  **Returned:** success  **Sample:** `"Successfully performed the virtual media operation."` |

### Authors

- Felix Stephen (@felixs88)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
