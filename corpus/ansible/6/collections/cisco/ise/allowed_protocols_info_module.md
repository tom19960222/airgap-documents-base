---
collection: ansible
version: "6"
title: "cisco.ise.allowed_protocols_info module – Information module for Allowed Protocols"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ise/allowed_protocols_info_module.html
fetched_at: 2026-07-27T16:56:11+00:00
---
# cisco.ise.allowed_protocols_info module – Information module for Allowed Protocols

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
> see [Requirements](allowed_protocols_info_module.md#ansible-collections-cisco-ise-allowed-protocols-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.allowed_protocols_info`.

New in cisco.ise 1.0.0

- [Synopsis](allowed_protocols_info_module.md#synopsis)
- [Requirements](allowed_protocols_info_module.md#requirements)
- [Parameters](allowed_protocols_info_module.md#parameters)
- [Notes](allowed_protocols_info_module.md#notes)
- [Examples](allowed_protocols_info_module.md#examples)
- [Return Values](allowed_protocols_info_module.md#return-values)

## [Synopsis](allowed_protocols_info_module.md#id1)

- Get all Allowed Protocols.
- Get Allowed Protocols by id.
- Get Allowed Protocols by name.
- This API allows the client to get all the allowed protocols.
- This API allows the client to get an allowed protocol by ID.
- This API allows the client to get an allowed protocol by name.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](allowed_protocols_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.0.8
- python >= 3.5

## [Parameters](allowed_protocols_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **id**  string | Id path parameter. |
| **ise_debug**  boolean | Flag for Identity Services Engine SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **ise_hostname**  string / required | The Identity Services Engine hostname. |
| **ise_password**  string / required | The Identity Services Engine password to authenticate. |
| **ise_username**  string / required | The Identity Services Engine username to authenticate. |
| **ise_uses_api_gateway**  boolean  added in cisco.ise 1.1.0 | Flag that informs the SDK whether to use the Identity Services Engine’s API Gateway to send requests.  If it is true, it uses the ISE’s API Gateway and sends requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}.  If it is false, it sends the requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}:{{port}}, where the port value depends on the Service used (ERS, Mnt, UI, PxGrid).  Choices:   - `false` - `true` ← (default) |
| **ise_uses_csrf_token**  boolean  added in cisco.ise 3.0.0 | Flag that informs the SDK whether we send the CSRF token to ISE’s ERS APIs.  If it is True, the SDK assumes that your ISE CSRF Check is enabled.  If it is True, it assumes you need the SDK to manage the CSRF token automatically for you.  Choices:   - `false` ← (default) - `true` |
| **ise_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **ise_version**  string | Informs the SDK which version of Identity Services Engine to use.  Default: `"3.1_Patch_1"` |
| **ise_wait_on_rate_limit**  boolean | Flag for Identity Services Engine SDK to enable automatic rate-limit handling.  Choices:   - `false` - `true` ← (default) |
| **name**  string | Name path parameter. |
| **page**  integer | Page query parameter. Page number. |
| **size**  integer | Size query parameter. Number of objects returned per page. |

## [Notes](allowed_protocols_info_module.md#id4)

> **Note:**
>
> - SDK Method used are allowed_protocols.AllowedProtocols.get_allowed_protocol_by_id, allowed_protocols.AllowedProtocols.get_allowed_protocol_by_name, allowed_protocols.AllowedProtocols.get_allowed_protocols_generator,
> - Paths used are get /ers/config/allowedprotocols, get /ers/config/allowedprotocols/name/{name}, get /ers/config/allowedprotocols/{id},
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [Examples](allowed_protocols_info_module.md#id5)

```yaml+jinja
- name: Get all Allowed Protocols
  cisco.ise.allowed_protocols_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    page: 1
    size: 20
  register: result

- name: Get Allowed Protocols by id
  cisco.ise.allowed_protocols_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    id: string
  register: result

- name: Get Allowed Protocols by name
  cisco.ise.allowed_protocols_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    name: string
  register: result
```

## [Return Values](allowed_protocols_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"allowChap": true, "allowEapFast": true, "allowEapMd5": true, "allowEapTls": true, "allowEapTtls": true, "allowLeap": true, "allowMsChapV1": true, "allowMsChapV2": true, "allowPapAscii": true, "allowPeap": true, "allowPreferredEapProtocol": true, "allowTeap": true, "allowWeakCiphersForEap": true, "description": "string", "eapFast": {"allowEapFastEapGtc": true, "allowEapFastEapGtcPwdChange": true, "allowEapFastEapGtcPwdChangeRetries": 0, "allowEapFastEapMsChapV2": true, "allowEapFastEapMsChapV2PwdChange": true, "allowEapFastEapMsChapV2PwdChangeRetries": 0, "allowEapFastEapTls": true, "allowEapFastEapTlsAuthOfExpiredCerts": true, "eapFastDontUsePacsAcceptClientCert": true, "eapFastDontUsePacsAllowMachineAuthentication": true, "eapFastEnableEAPChaining": true, "eapFastUsePacs": true, "eapFastUsePacsAcceptClientCert": true, "eapFastUsePacsAllowAnonymProvisioning": true, "eapFastUsePacsAllowAuthenProvisioning": true, "eapFastUsePacsAllowMachineAuthentication": true, "eapFastUsePacsAuthorizationPacTtl": 0, "eapFastUsePacsAuthorizationPacTtlUnits": "string", "eapFastUsePacsMachinePacTtl": 0, "eapFastUsePacsMachinePacTtlUnits": "string", "eapFastUsePacsReturnAccessAcceptAfterAuthenticatedProvisioning": true, "eapFastUsePacsStatelessSessionResume": true, "eapFastUsePacsTunnelPacTtl": 0, "eapFastUsePacsTunnelPacTtlUnits": "string", "eapFastUsePacsUseProactivePacUpdatePrecentage": 0}, "eapTls": {"allowEapTlsAuthOfExpiredCerts": true, "eapTlsEnableStatelessSessionResume": true, "eapTlsSessionTicketPrecentage": 0, "eapTlsSessionTicketTtl": 0, "eapTlsSessionTicketTtlUnits": "string"}, "eapTlsLBit": true, "eapTtls": {"eapTtlsChap": true, "eapTtlsEapMd5": true, "eapTtlsEapMsChapV2": true, "eapTtlsEapMsChapV2PwdChange": true, "eapTtlsEapMsChapV2PwdChangeRetries": 0, "eapTtlsMsChapV1": true, "eapTtlsMsChapV2": true, "eapTtlsPapAscii": true}, "id": "string", "link": {"href": "string", "rel": "string", "type": "string"}, "name": "string", "peap": {"allowPeapEapGtc": true, "allowPeapEapGtcPwdChange": true, "allowPeapEapGtcPwdChangeRetries": 0, "allowPeapEapMsChapV2": true, "allowPeapEapMsChapV2PwdChange": true, "allowPeapEapMsChapV2PwdChangeRetries": 0, "allowPeapEapTls": true, "allowPeapEapTlsAuthOfExpiredCerts": true, "allowPeapV0": true, "requireCryptobinding": true}, "preferredEapProtocol": "string", "processHostLookup": true, "requireMessageAuth": true, "teap": {"acceptClientCertDuringTunnelEst": true, "allowDowngradeMsk": true, "allowTeapEapMsChapV2": true, "allowTeapEapMsChapV2PwdChange": true, "allowTeapEapMsChapV2PwdChangeRetries": 0, "allowTeapEapTls": true, "allowTeapEapTlsAuthOfExpiredCerts": true, "enableEapChaining": true}}` |
| **ise_responses**  list / elements=dictionary  added in cisco.ise 1.1.0 | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `"[\n  {\n    \"id\": \"string\",\n    \"name\": \"string\",\n    \"description\": \"string\",\n    \"eapTls\": {\n      \"allowEapTlsAuthOfExpiredCerts\": true,\n      \"eapTlsEnableStatelessSessionResume\": true,\n      \"eapTlsSessionTicketTtl\": 0,\n      \"eapTlsSessionTicketTtlUnits\": \"string\",\n      \"eapTlsSessionTicketPrecentage\": 0\n    },\n    \"peap\": {\n      \"allowPeapEapMsChapV2\": true,\n      \"allowPeapEapMsChapV2PwdChange\": true,\n      \"allowPeapEapMsChapV2PwdChangeRetries\": 0,\n      \"allowPeapEapGtc\": true,\n      \"allowPeapEapGtcPwdChange\": true,\n      \"allowPeapEapGtcPwdChangeRetries\": 0,\n      \"allowPeapEapTls\": true,\n      \"allowPeapEapTlsAuthOfExpiredCerts\": true,\n      \"requireCryptobinding\": true,\n      \"allowPeapV0\": true\n    },\n    \"eapFast\": {\n      \"allowEapFastEapMsChapV2\": true,\n      \"allowEapFastEapMsChapV2PwdChange\": true,\n      \"allowEapFastEapMsChapV2PwdChangeRetries\": 0,\n      \"allowEapFastEapGtc\": true,\n      \"allowEapFastEapGtcPwdChange\": true,\n      \"allowEapFastEapGtcPwdChangeRetries\": 0,\n      \"allowEapFastEapTls\": true,\n      \"allowEapFastEapTlsAuthOfExpiredCerts\": true,\n      \"eapFastUsePacs\": true,\n      \"eapFastUsePacsTunnelPacTtl\": 0,\n      \"eapFastUsePacsTunnelPacTtlUnits\": \"string\",\n      \"eapFastUsePacsUseProactivePacUpdatePrecentage\": 0,\n      \"eapFastUsePacsAllowAnonymProvisioning\": true,\n      \"eapFastUsePacsAllowAuthenProvisioning\": true,\n      \"eapFastUsePacsReturnAccessAcceptAfterAuthenticatedProvisioning\": true,\n      \"eapFastUsePacsAcceptClientCert\": true,\n      \"eapFastUsePacsMachinePacTtl\": 0,\n      \"eapFastUsePacsMachinePacTtlUnits\": \"string\",\n      \"eapFastUsePacsAllowMachineAuthentication\": true,\n      \"eapFastUsePacsStatelessSessionResume\": true,\n      \"eapFastUsePacsAuthorizationPacTtl\": 0,\n      \"eapFastUsePacsAuthorizationPacTtlUnits\": \"string\",\n      \"eapFastDontUsePacsAcceptClientCert\": true,\n      \"eapFastDontUsePacsAllowMachineAuthentication\": true,\n      \"eapFastEnableEAPChaining\": true\n    },\n    \"eapTtls\": {\n      \"eapTtlsPapAscii\": true,\n      \"eapTtlsChap\": true,\n      \"eapTtlsMsChapV1\": true,\n      \"eapTtlsMsChapV2\": true,\n      \"eapTtlsEapMd5\": true,\n      \"eapTtlsEapMsChapV2\": true,\n      \"eapTtlsEapMsChapV2PwdChange\": true,\n      \"eapTtlsEapMsChapV2PwdChangeRetries\": 0\n    },\n    \"teap\": {\n      \"allowTeapEapMsChapV2\": true,\n      \"allowTeapEapMsChapV2PwdChange\": true,\n      \"allowTeapEapMsChapV2PwdChangeRetries\": 0,\n      \"allowTeapEapTls\": true,\n      \"allowTeapEapTlsAuthOfExpiredCerts\": true,\n      \"acceptClientCertDuringTunnelEst\": true,\n      \"enableEapChaining\": true,\n      \"allowDowngradeMsk\": true\n    },\n    \"processHostLookup\": true,\n    \"allowPapAscii\": true,\n    \"allowChap\": true,\n    \"allowMsChapV1\": true,\n    \"allowMsChapV2\": true,\n    \"allowEapMd5\": true,\n    \"allowLeap\": true,\n    \"allowEapTls\": true,\n    \"allowEapTtls\": true,\n    \"allowEapFast\": true,\n    \"allowPeap\": true,\n    \"allowTeap\": true,\n    \"allowPreferredEapProtocol\": true,\n    \"preferredEapProtocol\": \"string\",\n    \"eapTlsLBit\": true,\n    \"allowWeakCiphersForEap\": true,\n    \"requireMessageAuth\": true,\n    \"link\": {\n      \"rel\": \"string\",\n      \"href\": \"string\",\n      \"type\": \"string\"\n    }\n  }\n]\n"` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
[Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
