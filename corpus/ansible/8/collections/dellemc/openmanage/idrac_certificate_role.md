---
collection: ansible
version: "8"
title: "dellemc.openmanage.idrac_certificate role – This role allows to generate certificate signing request, import, and export certificates on iDRAC"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/idrac_certificate_role.html
fetched_at: 2026-07-28T02:05:00+00:00
---
# dellemc.openmanage.idrac_certificate role – This role allows to generate certificate signing request, import, and export certificates on iDRAC

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
> To use it in a playbook, specify: `dellemc.openmanage.idrac_certificate`.

- [Entry point `main` – This role allows to generate certificate signing request, import, and export certificates on iDRAC](idrac_certificate_role.md#entry-point-main-this-role-allows-to-generate-certificate-signing-request-import-and-export-certificates-on-idrac)

  - [Synopsis](idrac_certificate_role.md#synopsis)
  - [Parameters](idrac_certificate_role.md#parameters)

## [Entry point `main` – This role allows to generate certificate signing request, import, and export certificates on iDRAC](idrac_certificate_role.md#id1)

New in dellemc.openmanage 7.4.0

### [Synopsis](idrac_certificate_role.md#id2)

- Role to manage the iDRAC certificates - Generate CSR, Import/Export certificates, and Reset configuration - for PowerEdge servers.

### [Parameters](idrac_certificate_role.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  string | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **cert_params**  dictionary | Certificate parameters to generate signing request. |
| **common_name**  string | The common name of the certificate. |
| **country_code**  string | The country code of the country where the entity applying for certification is located. |
| **email_address**  string | The email associated with the CSR. |
| **locality_name**  string | The city or other location where the entity applying for certification is located. |
| **organization_name**  string | The name associated with an organization. |
| **organization_unit**  string | The name associated with an organizational unit. For example, department name.  **Default:** `"True"` |
| **state_name**  string | The state where the entity applying for certification is located. |
| **subject_alt_name**  list / elements=string | The alternative domain names associated with the request.  **Default:** `[]` |
| **certificate_path**  path | Absolute path of the certificate file if *command* is `import`.  Directory path with write permissions if *command* is `generate_csr` or `export`. |
| **certificate_type**  string | Type of the iDRAC certificate - `HTTPS` The Dell self-signed SSL certificate. - (CA) Certificate Authority(CA) signed SSL certificate. - `CSC` The custom signed SSL certificate. - `CLIENT_TRUST_CERTIFICATE` Client trust certificate.  **Choices:**   - `"HTTPS"` ← (default) - `"CA"` - `"CSC"` - `"CLIENT_TRUST_CERTIFICATE"` |
| **command**  string | `generate_csr`, generate CSR. This requires *cert_params* and *certificate_path*.  **Choices:**   - `"import"` - `"export"` - `"generate_csr"` ← (default) - `"reset"` |
| **hostname**  string / required | iDRAC IP Address. |
| **https_port**  integer | iDRAC port.  **Default:** `443` |
| **https_timeout**  integer | The socket level timeout in seconds.  **Default:** `30` |
| **passphrase**  string | The passphrase string if the certificate to be imported is passphrase protected. |
| **password**  string / required | iDRAC user password. |
| **reset**  boolean | To reset the iDRAC after the certificate operation.  This is applicable when *command* is `import` or `reset`.  **Choices:**   - `false` - `true` ← (default) |
| **resource_id**  string | Redfish ID of the resource. |
| **username**  string / required | iDRAC username. |
| **validate_certs**  boolean | If `false`, the SSL certificates will not be validated.  Configure `false` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `false` by default.  **Choices:**   - `false` - `true` ← (default) |
| **wait**  integer | Maximum wait time for iDRAC to start after the reset, in seconds.  This is applicable when *command* is `import` or `reset` and *reset* is `True`.  **Default:** `300` |

#### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
