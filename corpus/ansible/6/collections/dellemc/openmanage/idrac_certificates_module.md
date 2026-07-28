---
collection: ansible
version: "6"
title: "dellemc.openmanage.idrac_certificates module – Configure certificates for iDRAC"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/idrac_certificates_module.html
fetched_at: 2026-07-27T17:25:10+00:00
---
# dellemc.openmanage.idrac_certificates module – Configure certificates for iDRAC

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
> see [Requirements](idrac_certificates_module.md#ansible-collections-dellemc-openmanage-idrac-certificates-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.idrac_certificates`.

New in dellemc.openmanage 5.5.0

- [Synopsis](idrac_certificates_module.md#synopsis)
- [Requirements](idrac_certificates_module.md#requirements)
- [Parameters](idrac_certificates_module.md#parameters)
- [Notes](idrac_certificates_module.md#notes)
- [Examples](idrac_certificates_module.md#examples)
- [Return Values](idrac_certificates_module.md#return-values)

## [Synopsis](idrac_certificates_module.md#id1)

- This module allows to generate certificate signing request, import, and export certificates on iDRAC.

## [Requirements](idrac_certificates_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](idrac_certificates_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **cert_params**  dictionary | Certificate parameters to generate signing request. |
| **common_name**  string / required | The common name of the certificate. |
| **country_code**  string / required | The country code of the country where the entity applying for certification is located. |
| **email_address**  string / required | The email associated with the CSR. |
| **locality_name**  string / required | The city or other location where the entity applying for certification is located. |
| **organization_name**  string / required | The name associated with an organization. |
| **organization_unit**  string / required | The name associated with an organizational unit. For example department name. |
| **state_name**  string / required | The state where the entity applying for certification is located. |
| **subject_alt_name**  list / elements=string | The alternative domain names associated with the request.  Default: `[]` |
| **certificate_path**  path | Absolute path of the certificate file if *command* is `import`.  Directory path with write permissions if *command* is `generate_csr` or `export`. |
| **certificate_type**  string | Type of the iDRAC certificate.  `HTTPS` The Dell self-signed SSL certificate.  `CA` Certificate Authority(CA) signed SSL certificate.  `CSC` The custom signed SSL certificate.  `CLIENT_TRUST_CERTIFICATE` Client trust certificate.  Choices:   - `"HTTPS"` ← (default) - `"CA"` - `"CSC"` - `"CLIENT_TRUST_CERTIFICATE"` |
| **command**  string | `generate_csr`, generate CSR. This requires *cert_params* and *certificate_path*. This is applicable only for `HTTPS`  `import`, import the certificate file. This requires *certificate_path*.  `export`, export the certificate. This requires *certificate_path*.  `reset`, reset the certificate to default settings. This is applicable only for `HTTPS`.  Choices:   - `"import"` - `"export"` - `"generate_csr"` ← (default) - `"reset"` |
| **idrac_ip**  string / required | iDRAC IP Address. |
| **idrac_password**  aliases: idrac_pwd  string / required | iDRAC user password. |
| **idrac_port**  integer | iDRAC port.  Default: `443` |
| **idrac_user**  string / required | iDRAC username. |
| **passphrase**  string | The passphrase string if the certificate to be imported is passphrase protected. |
| **reset**  boolean | To reset the iDRAC after the certificate operation.  This is applicable when *command* is `import` or `reset`.  Choices:   - `false` - `true` ← (default) |
| **resource_id**  string | Redfish ID of the resource. |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |
| **wait**  integer | Maximum wait time for iDRAC to start after the reset, in seconds.  This is applicable when *command* is `import` or `reset` and *reset* is `True`.  Default: `300` |

## [Notes](idrac_certificates_module.md#id4)

> **Note:**
>
> - The certificate operations are supported on iDRAC firmware 5.10.10.00 and above.
> - Run this module from a system that has direct access to Dell iDRAC.
> - This module supports `check_mode`.

## [Examples](idrac_certificates_module.md#id5)

```yaml+jinja
---
- name: Generate HTTPS certificate signing request
  dellemc.openmanage.idrac_certificates:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    command: "generate_csr"
    certificate_type: "HTTPS"
    certificate_path: "/home/omam/mycerts"
    cert_params:
      common_name: "sample.domain.com"
      organization_unit: "OrgUnit"
      locality_name: "Bangalore"
      state_name: "Karnataka"
      country_code: "IN"
      email_address: "admin@domain.com"
      organization_name: "OrgName"
      subject_alt_name:
        - 192.198.2.1

- name: Import a HTTPS certificate.
  dellemc.openmanage.idrac_certificates:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    command: "import"
    certificate_type: "HTTPS"
    certificate_path: "/path/to/cert.pem"

- name: Export a HTTPS certificate.
  dellemc.openmanage.idrac_certificates:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    command: "export"
    certificate_type: "HTTPS"
    certificate_path: "/home/omam/mycert_dir"

- name: Import a CSC certificate.
  dellemc.openmanage.idrac_certificates:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    command: "import"
    certificate_type: "CSC"
    certificate_path: "/path/to/cert.pem"

- name: Export a Client trust certificate.
  dellemc.openmanage.idrac_certificates:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    command: "export"
    certificate_type: "CLIENT_TRUST_CERTIFICATE"
    certificate_path: "/home/omam/mycert_dir"
```

## [Return Values](idrac_certificates_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **certificate_path**  string | The csr or exported certificate file path  Returned: when *command* is `export` or `generate_csr`  Sample: `"/home/ansible/myfiles/cert.pem"` |
| **error_info**  dictionary | Details of the HTTP Error.  Returned: on HTTP error  Sample: `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Status of the certificate configuration operation.  Returned: always  Sample: `"Successfully performed the operation generate_csr."` |

### Authors

- Jagadeesh N V(@jagadeeshnv)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
