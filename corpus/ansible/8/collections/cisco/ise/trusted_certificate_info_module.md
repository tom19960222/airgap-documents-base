---
collection: ansible
version: "8"
title: "cisco.ise.trusted_certificate_info module – Information module for Trusted Certificate"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ise/trusted_certificate_info_module.html
fetched_at: 2026-07-28T01:31:38+00:00
---
# cisco.ise.trusted_certificate_info module – Information module for Trusted Certificate

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
> see [Requirements](trusted_certificate_info_module.md#ansible-collections-cisco-ise-trusted-certificate-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.trusted_certificate_info`.

New in cisco.ise 1.0.0

- [Synopsis](trusted_certificate_info_module.md#synopsis)
- [Requirements](trusted_certificate_info_module.md#requirements)
- [Parameters](trusted_certificate_info_module.md#parameters)
- [Notes](trusted_certificate_info_module.md#notes)
- [See Also](trusted_certificate_info_module.md#see-also)
- [Examples](trusted_certificate_info_module.md#examples)
- [Return Values](trusted_certificate_info_module.md#return-values)

## [Synopsis](trusted_certificate_info_module.md#id1)

- Get all Trusted Certificate.
- Get Trusted Certificate by id.
- This API can displays details of a Trust Certificate based on a given ID.
- This API supports Filtering, Sorting and Pagination.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](trusted_certificate_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.1.1
- python >= 3.5

## [Parameters](trusted_certificate_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **filter**  list / elements=string | Filter query parameter. .. Container \*\*Simple filtering\*\* should be available through the filter query string parameter. The structure of a filter is a triplet of field operator and value separated with dots. More than one filter can be sent. The logical operator common to ALL filter criteria will be by default AND, and can be changed by using the \*”filterType=or”\* query string parameter.  Each resource Data model description should specify if an attribute is a filtered field.  The ‘EQ’ operator describes ‘Equals’.  The ‘NEQ’ operator describes ‘Not Equals’.  The ‘GT’ operator describes ‘Greater Than’.  The ‘LT’ operator describes ‘Less Than’.  The ‘STARTSW’ operator describes ‘Starts With’.  The ‘NSTARTSW’ operator describes ‘Not Starts With’.  The ‘ENDSW’ operator describes ‘Ends With’.  The ‘NENDSW’ operator describes ‘Not Ends With’.  The ‘CONTAINS’ operator describes ‘Contains’.  The ‘NCONTAINS’ operator describes ‘Not Contains’. |
| **filterType**  string | FilterType query parameter. The logical operator common to ALL filter criteria will be by default AND, and can be changed by using the parameter. |
| **id**  string | Id path parameter. ID of the trust certificate. |
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
| **page**  integer | Page query parameter. Page number. |
| **size**  integer | Size query parameter. Number of objects returned per page. |
| **sort**  string | Sort query parameter. Sort type - asc or desc. |
| **sortBy**  string | SortBy query parameter. Sort column by which objects needs to be sorted. |

## [Notes](trusted_certificate_info_module.md#id4)

> **Note:**
>
> - SDK Method used are certificates.Certificates.get_trusted_certificate_by_id, certificates.Certificates.get_trusted_certificates_generator,
> - Paths used are get /api/v1/certs/trusted-certificate, get /api/v1/certs/trusted-certificate/{id},
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [See Also](trusted_certificate_info_module.md#id5)

> **See also:**
>
> [Cisco ISE documentation for Certificates](https://developer.cisco.com/docs/identity-services-engine/v1/#!certificate-openapi)
> :   Complete reference of the Certificates API.

## [Examples](trusted_certificate_info_module.md#id6)

```yaml+jinja
- name: Get all Trusted Certificate
  cisco.ise.trusted_certificate_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    page: 0
    size: 0
    sort: string
    sortBy: string
    filter: []
    filterType: string
  register: result

- name: Get Trusted Certificate by id
  cisco.ise.trusted_certificate_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    id: string
  register: result
```

## [Return Values](trusted_certificate_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"authenticateBeforeCRLReceived": "string", "automaticCRLUpdate": "string", "automaticCRLUpdatePeriod": "string", "automaticCRLUpdateUnits": "string", "crlDistributionUrl": "string", "crlDownloadFailureRetries": "string", "crlDownloadFailureRetriesUnits": "string", "description": "string", "downloadCRL": "string", "enableOCSPValidation": "string", "enableServerIdentityCheck": "string", "expirationDate": "string", "friendlyName": "string", "id": "string", "ignoreCRLExpiration": "string", "internalCA": true, "isReferredInPolicy": true, "issuedBy": "string", "issuedTo": "string", "keySize": "string", "link": {"href": "string", "rel": "string", "type": "string"}, "nonAutomaticCRLUpdatePeriod": "string", "nonAutomaticCRLUpdateUnits": "string", "rejectIfNoStatusFromOCSP": "string", "rejectIfUnreachableFromOCSP": "string", "selectedOCSPService": "string", "serialNumberDecimalFormat": "string", "sha256Fingerprint": "string", "signatureAlgorithm": "string", "status": "string", "subject": "string", "trustedFor": "string", "validFrom": "string"}` |
| **ise_responses**  list / elements=dictionary  *added in cisco.ise 1.1.0* | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `"[\n  {\n    \"authenticateBeforeCRLReceived\": \"string\",\n    \"automaticCRLUpdate\": \"string\",\n    \"automaticCRLUpdatePeriod\": \"string\",\n    \"automaticCRLUpdateUnits\": \"string\",\n    \"crlDistributionUrl\": \"string\",\n    \"crlDownloadFailureRetries\": \"string\",\n    \"crlDownloadFailureRetriesUnits\": \"string\",\n    \"description\": \"string\",\n    \"downloadCRL\": \"string\",\n    \"enableOCSPValidation\": \"string\",\n    \"enableServerIdentityCheck\": \"string\",\n    \"expirationDate\": \"string\",\n    \"friendlyName\": \"string\",\n    \"id\": \"string\",\n    \"ignoreCRLExpiration\": \"string\",\n    \"internalCA\": true,\n    \"isReferredInPolicy\": true,\n    \"issuedBy\": \"string\",\n    \"issuedTo\": \"string\",\n    \"keySize\": \"string\",\n    \"link\": {\n      \"href\": \"string\",\n      \"rel\": \"string\",\n      \"type\": \"string\"\n    },\n    \"nonAutomaticCRLUpdatePeriod\": \"string\",\n    \"nonAutomaticCRLUpdateUnits\": \"string\",\n    \"rejectIfNoStatusFromOCSP\": \"string\",\n    \"rejectIfUnreachableFromOCSP\": \"string\",\n    \"selectedOCSPService\": \"string\",\n    \"serialNumberDecimalFormat\": \"string\",\n    \"sha256Fingerprint\": \"string\",\n    \"signatureAlgorithm\": \"string\",\n    \"status\": \"string\",\n    \"subject\": \"string\",\n    \"trustedFor\": \"string\",\n    \"validFrom\": \"string\"\n  }\n]\n"` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
- [Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
