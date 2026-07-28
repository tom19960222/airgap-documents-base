---
collection: ansible
version: "6"
title: "cisco.ise.system_certificate_import module – Resource module for System Certificate Import"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ise/system_certificate_import_module.html
fetched_at: 2026-07-27T16:59:52+00:00
---
# cisco.ise.system_certificate_import module – Resource module for System Certificate Import

> **Note:**
>
> This module is part of the [cisco.ise collection](https://galaxy.ansible.com/cisco/ise) (version 2.5.9).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ise`.
> You need further requirements to be able to use this module,
> see [Requirements](system_certificate_import_module.md#ansible-collections-cisco-ise-system-certificate-import-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.system_certificate_import`.

New in cisco.ise 1.0.0

- [Synopsis](system_certificate_import_module.md#synopsis)
- [Requirements](system_certificate_import_module.md#requirements)
- [Parameters](system_certificate_import_module.md#parameters)
- [Notes](system_certificate_import_module.md#notes)
- [See Also](system_certificate_import_module.md#see-also)
- [Examples](system_certificate_import_module.md#examples)
- [Return Values](system_certificate_import_module.md#return-values)

## [Synopsis](system_certificate_import_module.md#id1)

- Manage operation create of the resource System Certificate Import.
- Import an X509 certificate as a system certificate.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](system_certificate_import_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.0.8
- python >= 3.5

## [Parameters](system_certificate_import_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **admin**  boolean | Use certificate to authenticate the Cisco ISE Admin Portal.  Choices:   - `false` - `true` |
| **allowExtendedValidity**  boolean | Allow import of certificates with validity greater than 398 days (required).  Choices:   - `false` - `true` |
| **allowOutOfDateCert**  boolean | Allow out of date certificates (required).  Choices:   - `false` - `true` |
| **allowPortalTagTransferForSameSubject**  boolean | Allow overwriting the portal tag from matching certificate of same subject.  Choices:   - `false` - `true` |
| **allowReplacementOfCertificates**  boolean | Allow Replacement of certificates (required).  Choices:   - `false` - `true` |
| **allowReplacementOfPortalGroupTag**  boolean | Allow Replacement of Portal Group Tag (required).  Choices:   - `false` - `true` |
| **allowRoleTransferForSameSubject**  boolean | Allow transfer of roles for certificate with matching subject.  Choices:   - `false` - `true` |
| **allowSHA1Certificates**  boolean | Allow SHA1 based certificates (required).  Choices:   - `false` - `true` |
| **allowWildCardCertificates**  boolean | Allow Wildcard certificates.  Choices:   - `false` - `true` |
| **data**  string | Certificate Content (required). |
| **eap**  boolean | Use certificate for EAP protocols that use SSL/TLS tunneling.  Choices:   - `false` - `true` |
| **ims**  boolean | Use certificate for the Cisco ISE Messaging Service.  Choices:   - `false` - `true` |
| **ise_debug**  boolean | Flag for Identity Services Engine SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **ise_hostname**  string / required | The Identity Services Engine hostname. |
| **ise_password**  string / required | The Identity Services Engine password to authenticate. |
| **ise_username**  string / required | The Identity Services Engine username to authenticate. |
| **ise_uses_api_gateway**  boolean  added in cisco.ise 1.1.0 | Flag that informs the SDK whether to use the Identity Services Engine’s API Gateway to send requests.  If it is true, it uses the ISE’s API Gateway and sends requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}.  If it is false, it sends the requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}:{{port}}, where the port value depends on the Service used (ERS, Mnt, UI, PxGrid).  Choices:   - `false` - `true` ← (default) |
| **ise_uses_csrf_token**  boolean  added in cisco.ise 3.0.0 | Flag that informs the SDK whether we send the CSRF token to ISE’s ERS APIs.  If it is True, the SDK assumes that your ISE CSRF Check is enabled.  If it is True, it assumes you need the SDK to manage the CSRF token automatically for you.  Choices:   - `false` ← (default) - `true` |
| **ise_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **ise_version**  string | Informs the SDK which version of Identity Services Engine to use.  Default: `"3.1_Patch_1"` |
| **ise_wait_on_rate_limit**  boolean | Flag for Identity Services Engine SDK to enable automatic rate-limit handling.  Choices:   - `false` - `true` ← (default) |
| **name**  string | Name of the certificate. |
| **password**  string | Certificate Password (required). |
| **portal**  boolean | Use for portal.  Choices:   - `false` - `true` |
| **portalGroupTag**  string | Set Group tag. |
| **privateKeyData**  string | Private Key data (required). |
| **pxgrid**  boolean | Use certificate for the pxGrid Controller.  Choices:   - `false` - `true` |
| **radius**  boolean | Use certificate for the RADSec server.  Choices:   - `false` - `true` |
| **saml**  boolean | Use certificate for SAML Signing.  Choices:   - `false` - `true` |
| **validateCertificateExtensions**  boolean | Validate certificate extensions.  Choices:   - `false` - `true` |

## [Notes](system_certificate_import_module.md#id4)

> **Note:**
>
> - SDK Method used are certificates.Certificates.import_system_certificate,
> - Paths used are post /api/v1/certs/system-certificate/import,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [See Also](system_certificate_import_module.md#id5)

> **See also:**
>
> [Cisco ISE documentation for Certificates](https://developer.cisco.com/docs/identity-services-engine/v1/#!certificate-openapi)
> :   Complete reference of the Certificates API.

## [Examples](system_certificate_import_module.md#id6)

```yaml+jinja
- name: Create
  cisco.ise.system_certificate_import:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    admin: true
    allowExtendedValidity: true
    allowOutOfDateCert: true
    allowPortalTagTransferForSameSubject: true
    allowReplacementOfCertificates: true
    allowReplacementOfPortalGroupTag: true
    allowRoleTransferForSameSubject: true
    allowSHA1Certificates: true
    allowWildCardCertificates: true
    data: string
    eap: true
    ims: true
    name: string
    password: string
    portal: true
    portalGroupTag: string
    privateKeyData: string
    pxgrid: true
    radius: true
    saml: true
    validateCertificateExtensions: true
```

## [Return Values](system_certificate_import_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"response": {"id": "string", "message": "string", "status": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
[Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
