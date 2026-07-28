---
collection: ansible
version: "8"
title: "dellemc.openmanage.ome_template_identity_pool module – Attach or detach an identity pool to a requested template on OpenManage Enterprise"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/ome_template_identity_pool_module.html
fetched_at: 2026-07-28T02:04:50+00:00
---
# dellemc.openmanage.ome_template_identity_pool module – Attach or detach an identity pool to a requested template on OpenManage Enterprise

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
> see [Requirements](ome_template_identity_pool_module.md#ansible-collections-dellemc-openmanage-ome-template-identity-pool-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_template_identity_pool`.

New in dellemc.openmanage 2.0.0

- [Synopsis](ome_template_identity_pool_module.md#synopsis)
- [Requirements](ome_template_identity_pool_module.md#requirements)
- [Parameters](ome_template_identity_pool_module.md#parameters)
- [Notes](ome_template_identity_pool_module.md#notes)
- [Examples](ome_template_identity_pool_module.md#examples)
- [Return Values](ome_template_identity_pool_module.md#return-values)

## [Synopsis](ome_template_identity_pool_module.md#id1)

- This module allows to- - Attach an identity pool to a requested template on OpenManage Enterprise. - Detach an identity pool from a requested template on OpenManage Enterprise.

## [Requirements](ome_template_identity_pool_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_template_identity_pool_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **hostname**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular IP address or hostname. |
| **identity_pool_name**  string | Name of the identity pool. - To attach an identity pool to a template, provide the name of the identity pool. - This option is not applicable when detaching an identity pool from a template. |
| **password**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise or OpenManage Enterprise Modular HTTPS port.  **Default:** `443` |
| **template_name**  string / required | Name of the template to which an identity pool is attached or detached. |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **username**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ome_template_identity_pool_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to Dell OpenManage Enterprise.
> - This module supports `check_mode`.

## [Examples](ome_template_identity_pool_module.md#id5)

```yaml+jinja
---
- name: Attach an identity pool to a template
  dellemc.openmanage.ome_template_identity_pool:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    template_name: template_name
    identity_pool_name: identity_pool_name

- name: Detach an identity pool from a template
  dellemc.openmanage.ome_template_identity_pool:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    template_name: template_name
```

## [Return Values](ome_template_identity_pool_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  **Returned:** on HTTP error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Overall identity pool status of the attach or detach operation.  **Returned:** always  **Sample:** `"Successfully attached identity pool to template."` |

### Authors

- Felix Stephen (@felixs88)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
