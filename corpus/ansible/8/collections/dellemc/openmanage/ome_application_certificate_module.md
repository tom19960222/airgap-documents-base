---
collection: ansible
version: "8"
title: "dellemc.openmanage.ome_application_certificate module – This module allows to generate a CSR and upload the certificate"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/ome_application_certificate_module.html
fetched_at: 2026-07-28T02:04:18+00:00
---
# dellemc.openmanage.ome_application_certificate module – This module allows to generate a CSR and upload the certificate

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
> see [Requirements](ome_application_certificate_module.md#ansible-collections-dellemc-openmanage-ome-application-certificate-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_application_certificate`.

New in dellemc.openmanage 2.1.0

- [Synopsis](ome_application_certificate_module.md#synopsis)
- [Requirements](ome_application_certificate_module.md#requirements)
- [Parameters](ome_application_certificate_module.md#parameters)
- [Notes](ome_application_certificate_module.md#notes)
- [Examples](ome_application_certificate_module.md#examples)
- [Return Values](ome_application_certificate_module.md#return-values)

## [Synopsis](ome_application_certificate_module.md#id1)

- This module allows the generation a new certificate signing request (CSR) and to upload the certificate on OpenManage Enterprise.

## [Requirements](ome_application_certificate_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_application_certificate_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **business_name**  string | Name of the business that issued the certificate. This option is applicable for `generate_csr`. |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **command**  string | `generate_csr` allows the generation of a CSR and `upload` uploads the certificate.  **Choices:**   - `"generate_csr"` ← (default) - `"upload"` |
| **country**  string | Country in which the issuer resides. This option is applicable for `generate_csr`. |
| **country_state**  string | State in which the issuer resides. This option is applicable for `generate_csr`. |
| **department_name**  string | Name of the department that issued the certificate. This option is applicable for `generate_csr`. |
| **distinguished_name**  string | Name of the certificate issuer. This option is applicable for `generate_csr`. |
| **email**  string | Email associated with the issuer. This option is applicable for `generate_csr`. |
| **hostname**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular IP address or hostname. |
| **locality**  string | Local address of the issuer of the certificate. This option is applicable for `generate_csr`. |
| **password**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise or OpenManage Enterprise Modular HTTPS port.  **Default:** `443` |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **upload_file**  string | Local path of the certificate file to be uploaded. This option is applicable for `upload`. Once the certificate is uploaded, OpenManage Enterprise cannot be accessed for a few seconds. |
| **username**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ome_application_certificate_module.md#id4)

> **Note:**
>
> - If a certificate is uploaded, which is identical to an already existing certificate, it is accepted by the module.
> - This module does not support `check_mode`.

## [Examples](ome_application_certificate_module.md#id5)

```yaml+jinja
---
- name: Generate a certificate signing request
  dellemc.openmanage.ome_application_certificate:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: "generate_csr"
    distinguished_name: "hostname.com"
    department_name: "Remote Access Group"
    business_name: "Dell Inc."
    locality: "Round Rock"
    country_state: "Texas"
    country: "US"
    email: "support@dell.com"

- name: Upload the certificate
  dellemc.openmanage.ome_application_certificate:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: "upload"
    upload_file: "/path/certificate.cer"
```

## [Return Values](ome_application_certificate_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **csr_status**  dictionary | Details of the generated certificate.  **Returned:** on success  **Sample:** `{"CertificateData": "-----BEGIN CERTIFICATE REQUEST-----GHFSUEKLELE af3u4h2rkdkfjasczjfefhkrr/frjrfrjfrxnvzklf/nbcvxmzvndlskmcvbmzkdk kafhaksksvklhfdjtrhhffgeth/tashdrfstkm@kdjFGD/sdlefrujjfvvsfeikdf yeufghdkatbavfdomehtdnske/tahndfavdtdfgeikjlagmdfbandfvfcrfgdtwxc qwgfrteyupojmnsbajdkdbfs/ujdfgthedsygtamnsuhakmanfuarweyuiwruefjr etwuwurefefgfgurkjkdmbvfmvfvfk==-----END CERTIFICATE REQUEST-----"}` |
| **error_info**  dictionary | Details of the HTTP error.  **Returned:** on HTTP error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to upload the certificate because the certificate file provided is invalid.", "MessageArgs": [], "MessageId": "CSEC9002", "RelatedProperties": [], "Resolution": "Make sure the CA certificate and private key are correct and retry the operation.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Overall status of the certificate signing request.  **Returned:** always  **Sample:** `"Successfully generated certificate signing request."` |

### Authors

- Felix Stephen (@felixs88)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
