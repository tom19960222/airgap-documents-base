---
collection: ansible
version: "8"
title: "cisco.ise.trusted_certificate module – Resource module for Trusted Certificate"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ise/trusted_certificate_module.html
fetched_at: 2026-07-28T01:31:36+00:00
---
# cisco.ise.trusted_certificate module – Resource module for Trusted Certificate

> **Note:**
>
> This module is part of the [cisco.ise collection](https://galaxy.ansible.com/ui/repo/published/cisco/ise/) (version 2.6.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ise`.
> You need further requirements to be able to use this module,
> see [Requirements](trusted_certificate_module.md#ansible-collections-cisco-ise-trusted-certificate-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.trusted_certificate`.

New in cisco.ise 1.0.0

- [Synopsis](trusted_certificate_module.md#synopsis)
- [Requirements](trusted_certificate_module.md#requirements)
- [Parameters](trusted_certificate_module.md#parameters)
- [Notes](trusted_certificate_module.md#notes)
- [See Also](trusted_certificate_module.md#see-also)
- [Examples](trusted_certificate_module.md#examples)
- [Return Values](trusted_certificate_module.md#return-values)

## [Synopsis](trusted_certificate_module.md#id1)

- Manage operations update and delete of the resource Trusted Certificate.
- This API deletes a Trust Certificate from Trusted Certificate Store based on a given ID.
- Update a trusted certificate present in Cisco ISE trust store.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](trusted_certificate_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.1.1
- python >= 3.5

## [Parameters](trusted_certificate_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **authenticateBeforeCRLReceived**  boolean | Switch to enable or disable CRL verification if CRL is not received.  **Choices:**   - `false` - `true` |
| **automaticCRLUpdate**  boolean | Switch to enable or disable automatic CRL update.  **Choices:**   - `false` - `true` |
| **automaticCRLUpdatePeriod**  integer | Automatic CRL update period. |
| **automaticCRLUpdateUnits**  string | Unit of time for automatic CRL update. |
| **crlDistributionUrl**  string | CRL Distribution URL. |
| **crlDownloadFailureRetries**  integer | If CRL download fails, wait time before retry. |
| **crlDownloadFailureRetriesUnits**  string | Unit of time before retry if CRL download fails. |
| **description**  string | Description for trust certificate. |
| **downloadCRL**  boolean | Switch to enable or disable download of CRL.  **Choices:**   - `false` - `true` |
| **enableOCSPValidation**  boolean | Switch to enable or disable OCSP Validation.  **Choices:**   - `false` - `true` |
| **enableServerIdentityCheck**  boolean | Switch to enable or disable verification if HTTPS or LDAP server certificate name fits the configured server URL.  **Choices:**   - `false` - `true` |
| **id**  string | Id path parameter. ID of the trust certificate. |
| **ignoreCRLExpiration**  boolean | Switch to enable or disable ignore CRL expiration.  **Choices:**   - `false` - `true` |
| **ise_debug**  boolean | Flag for Identity Services Engine SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **ise_hostname**  string / required | The Identity Services Engine hostname. |
| **ise_password**  string / required | The Identity Services Engine password to authenticate. |
| **ise_single_request_timeout**  integer  *added in cisco.ise 3.0.0* | Timeout (in seconds) for RESTful HTTP requests.  **Default:** `60` |
| **ise_username**  string / required | The Identity Services Engine username to authenticate. |
| **ise_uses_api_gateway**  boolean  *added in cisco.ise 1.1.0* | Flag that informs the SDK whether to use the Identity Services Engine’s API Gateway to send requests.  If it is true, it uses the ISE’s API Gateway and sends requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}.  If it is false, it sends the requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}:{{port}}, where the port value depends on the Service used (ERS, Mnt, UI, PxGrid).  **Choices:**   - `false` - `true` ← (default) |
| **ise_uses_csrf_token**  boolean  *added in cisco.ise 3.0.0* | Flag that informs the SDK whether we send the CSRF token to ISE’s ERS APIs.  If it is True, the SDK assumes that your ISE CSRF Check is enabled.  If it is True, it assumes you need the SDK to manage the CSRF token automatically for you.  **Choices:**   - `false` ← (default) - `true` |
| **ise_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **ise_version**  string | Informs the SDK which version of Identity Services Engine to use.  **Default:** `"3.1_Patch_1"` |
| **ise_wait_on_rate_limit**  boolean | Flag for Identity Services Engine SDK to enable automatic rate-limit handling.  **Choices:**   - `false` - `true` ← (default) |
| **name**  string | Friendly name of the certificate. |
| **nonAutomaticCRLUpdatePeriod**  integer | Non automatic CRL update period. |
| **nonAutomaticCRLUpdateUnits**  string | Unit of time of non automatic CRL update. |
| **rejectIfNoStatusFromOCSP**  boolean | Switch to reject certificate if there is no status from OCSP.  **Choices:**   - `false` - `true` |
| **rejectIfUnreachableFromOCSP**  boolean | Switch to reject certificate if unreachable from OCSP.  **Choices:**   - `false` - `true` |
| **selectedOCSPService**  string | Name of selected OCSP Service. |
| **status**  string | Trusted Certificate’s status. |
| **trustForCertificateBasedAdminAuth**  boolean | Trust for Certificate based Admin authentication.  **Choices:**   - `false` - `true` |
| **trustForCiscoServicesAuth**  boolean | Trust for authentication of Cisco Services.  **Choices:**   - `false` - `true` |
| **trustForClientAuth**  boolean | Trust for client authentication and Syslog.  **Choices:**   - `false` - `true` |
| **trustForIseAuth**  boolean | Trust for authentication within Cisco ISE.  **Choices:**   - `false` - `true` |

## [Notes](trusted_certificate_module.md#id4)

> **Note:**
>
> - SDK Method used are certificates.Certificates.delete_trusted_certificate_by_id, certificates.Certificates.update_trusted_certificate,
> - Paths used are delete /api/v1/certs/trusted-certificate/{id}, put /api/v1/certs/trusted-certificate/{id},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [See Also](trusted_certificate_module.md#id5)

> **See also:**
>
> [Cisco ISE documentation for Certificates](https://developer.cisco.com/docs/identity-services-engine/v1/#!certificate-openapi)
> :   Complete reference of the Certificates API.

## [Examples](trusted_certificate_module.md#id6)

```yaml+jinja
- name: Update by id
  cisco.ise.trusted_certificate:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    authenticateBeforeCRLReceived: true
    automaticCRLUpdate: true
    automaticCRLUpdatePeriod: 0
    automaticCRLUpdateUnits: string
    crlDistributionUrl: string
    crlDownloadFailureRetries: 0
    crlDownloadFailureRetriesUnits: string
    description: string
    downloadCRL: true
    enableOCSPValidation: true
    enableServerIdentityCheck: true
    id: string
    ignoreCRLExpiration: true
    name: string
    nonAutomaticCRLUpdatePeriod: 0
    nonAutomaticCRLUpdateUnits: string
    rejectIfNoStatusFromOCSP: true
    rejectIfUnreachableFromOCSP: true
    selectedOCSPService: string
    status: string
    trustForCertificateBasedAdminAuth: true
    trustForCiscoServicesAuth: true
    trustForClientAuth: true
    trustForIseAuth: true

- name: Delete by id
  cisco.ise.trusted_certificate:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string
```

## [Return Values](trusted_certificate_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"authenticateBeforeCRLReceived": "string", "automaticCRLUpdate": "string", "automaticCRLUpdatePeriod": "string", "automaticCRLUpdateUnits": "string", "crlDistributionUrl": "string", "crlDownloadFailureRetries": "string", "crlDownloadFailureRetriesUnits": "string", "description": "string", "downloadCRL": "string", "enableOCSPValidation": "string", "enableServerIdentityCheck": "string", "expirationDate": "string", "friendlyName": "string", "id": "string", "ignoreCRLExpiration": "string", "internalCA": true, "isReferredInPolicy": true, "issuedBy": "string", "issuedTo": "string", "keySize": "string", "link": {"href": "string", "rel": "string", "type": "string"}, "nonAutomaticCRLUpdatePeriod": "string", "nonAutomaticCRLUpdateUnits": "string", "rejectIfNoStatusFromOCSP": "string", "rejectIfUnreachableFromOCSP": "string", "selectedOCSPService": "string", "serialNumberDecimalFormat": "string", "sha256Fingerprint": "string", "signatureAlgorithm": "string", "status": "string", "subject": "string", "trustedFor": "string", "validFrom": "string"}` |
| **ise_update_response**  dictionary  *added in cisco.ise 1.1.0* | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"response": {"id": "string", "link": {"href": "string", "rel": "string", "type": "string"}, "message": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
- [Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
