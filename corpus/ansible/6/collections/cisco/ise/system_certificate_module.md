---
collection: ansible
version: "6"
title: "cisco.ise.system_certificate module – Resource module for System Certificate"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ise/system_certificate_module.html
fetched_at: 2026-07-27T16:59:50+00:00
---
# cisco.ise.system_certificate module – Resource module for System Certificate

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
> see [Requirements](system_certificate_module.md#ansible-collections-cisco-ise-system-certificate-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.system_certificate`.

New in cisco.ise 1.0.0

- [Synopsis](system_certificate_module.md#synopsis)
- [Requirements](system_certificate_module.md#requirements)
- [Parameters](system_certificate_module.md#parameters)
- [Notes](system_certificate_module.md#notes)
- [See Also](system_certificate_module.md#see-also)
- [Examples](system_certificate_module.md#examples)
- [Return Values](system_certificate_module.md#return-values)

## [Synopsis](system_certificate_module.md#id1)

- Manage operations update and delete of the resource System Certificate.
- This API deletes a System Certificate of a particular node based on given HostName and ID.
- Update a System Certificate.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](system_certificate_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.0.8
- python >= 3.5

## [Parameters](system_certificate_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **admin**  boolean | Use certificate to authenticate the Cisco ISE Admin Portal.  Choices:   - `false` - `true` |
| **allowPortalTagTransferForSameSubject**  boolean | Allow overwriting the portal tag from matching certificate of same subject.  Choices:   - `false` - `true` |
| **allowReplacementOfPortalGroupTag**  boolean | Allow Replacement of Portal Group Tag (required).  Choices:   - `false` - `true` |
| **allowRoleTransferForSameSubject**  boolean | Allow transfer of roles for certificate with matching subject.  Choices:   - `false` - `true` |
| **allowWildcardDelete**  boolean | If the given certificate to be deleted is a wildcard certificate, corresponding certificate gets deleted on rest of the nodes in the deployment as well.  Choices:   - `false` - `true` |
| **description**  string | Description of System Certificate. |
| **eap**  boolean | Use certificate for EAP protocols that use SSL/TLS tunneling.  Choices:   - `false` - `true` |
| **expirationTTLPeriod**  integer | System Certificate’s expirationTTLPeriod. |
| **expirationTTLUnits**  string | System Certificate’s expirationTTLUnits. |
| **hostName**  string | HostName path parameter. Name of Host whose certificate needs to be updated. |
| **id**  string | Id path parameter. ID of the System Certificate to be updated. |
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
| **portal**  boolean | Use for portal.  Choices:   - `false` - `true` |
| **portalGroupTag**  string | Set Group tag. |
| **pxgrid**  boolean | Use certificate for the pxGrid Controller.  Choices:   - `false` - `true` |
| **radius**  boolean | Use certificate for the RADSec server.  Choices:   - `false` - `true` |
| **renewSelfSignedCertificate**  boolean | Renew Self-signed Certificate.  Choices:   - `false` - `true` |
| **saml**  boolean | Use certificate for SAML Signing.  Choices:   - `false` - `true` |

## [Notes](system_certificate_module.md#id4)

> **Note:**
>
> - SDK Method used are certificates.Certificates.delete_system_certificate_by_id, certificates.Certificates.update_system_certificate,
> - Paths used are delete /api/v1/certs/system-certificate/{hostName}/{id}, put /api/v1/certs/system-certificate/{hostName}/{id},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [See Also](system_certificate_module.md#id5)

> **See also:**
>
> [Cisco ISE documentation for Certificates](https://developer.cisco.com/docs/identity-services-engine/v1/#!certificate-openapi)
> :   Complete reference of the Certificates API.

## [Examples](system_certificate_module.md#id6)

```yaml+jinja
- name: Update by id
  cisco.ise.system_certificate:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    admin: true
    allowPortalTagTransferForSameSubject: true
    allowReplacementOfPortalGroupTag: true
    allowRoleTransferForSameSubject: true
    description: string
    eap: true
    expirationTTLPeriod: 0
    expirationTTLUnits: string
    hostName: string
    id: string
    ims: true
    name: string
    portal: true
    portalGroupTag: string
    pxgrid: true
    radius: true
    renewSelfSignedCertificate: true
    saml: true

- name: Delete by id
  cisco.ise.system_certificate:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    allowWildcardDelete: true
    hostName: string
    id: string
```

## [Return Values](system_certificate_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"expirationDate": "string", "friendlyName": "string", "groupTag": "string", "id": "string", "issuedBy": "string", "issuedTo": "string", "keySize": 0, "link": {"href": "string", "rel": "string", "type": "string"}, "portalsUsingTheTag": "string", "selfSigned": true, "serialNumberDecimalFormat": "string", "sha256Fingerprint": "string", "signatureAlgorithm": "string", "usedBy": "string", "validFrom": "string"}` |
| **ise_update_response**  dictionary  added in cisco.ise 1.1.0 | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"response": {"id": "string", "link": {"href": "string", "rel": "string", "type": "string"}, "message": "string", "status": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
[Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
