---
collection: ansible
version: "6"
title: "cisco.dnac.authentication_import_certificate module – Resource module for Authentication Import Certificate"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/authentication_import_certificate_module.html
fetched_at: 2026-07-27T16:51:01+00:00
---
# cisco.dnac.authentication_import_certificate module – Resource module for Authentication Import Certificate

> **Note:**
>
> This module is part of the [cisco.dnac collection](https://galaxy.ansible.com/cisco/dnac) (version 6.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.dnac`.
> You need further requirements to be able to use this module,
> see [Requirements](authentication_import_certificate_module.md#ansible-collections-cisco-dnac-authentication-import-certificate-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.authentication_import_certificate`.

New in cisco.dnac 3.1.0

- [Synopsis](authentication_import_certificate_module.md#synopsis)
- [Requirements](authentication_import_certificate_module.md#requirements)
- [Parameters](authentication_import_certificate_module.md#parameters)
- [Notes](authentication_import_certificate_module.md#notes)
- [See Also](authentication_import_certificate_module.md#see-also)
- [Examples](authentication_import_certificate_module.md#examples)
- [Return Values](authentication_import_certificate_module.md#return-values)

## [Synopsis](authentication_import_certificate_module.md#id1)

- Manage operation create of the resource Authentication Import Certificate.
- This method is used to upload a certificate.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](authentication_import_certificate_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](authentication_import_certificate_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **certFilePath**  string | Cert file absolute path. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **listOfUsers**  list / elements=string | ListOfUsers query parameter. |
| **pkFilePath**  string | Pk file absolute path. |
| **pkPassword**  string | PkPassword query parameter. Private Key Passsword. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](authentication_import_certificate_module.md#id4)

> **Note:**
>
> - SDK Method used are authentication_management.AuthenticationManagement.import_certificate,
> - Paths used are post /dna/intent/api/v1/certificate,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](authentication_import_certificate_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Authentication Management ImportCertificate](https://developer.cisco.com/docs/dna-center/#!import-certificate)
> :   Complete reference of the ImportCertificate API.

## [Examples](authentication_import_certificate_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.authentication_import_certificate:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    certFilePath: /tmp/uploads/Test-242.pem
    listOfUsers: []
    pkFilePath: /tmp/uploads/Test-242.key
    pkPassword: string
```

## [Return Values](authentication_import_certificate_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"response": {"taskId": "string", "url": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
