---
collection: ansible
version: "6"
title: "cisco.dnac.device_credential_info module – Information module for Device Credential"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/device_credential_info_module.html
fetched_at: 2026-07-27T16:51:27+00:00
---
# cisco.dnac.device_credential_info module – Information module for Device Credential

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
> see [Requirements](device_credential_info_module.md#ansible-collections-cisco-dnac-device-credential-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.device_credential_info`.

New in cisco.dnac 3.1.0

- [Synopsis](device_credential_info_module.md#synopsis)
- [Requirements](device_credential_info_module.md#requirements)
- [Parameters](device_credential_info_module.md#parameters)
- [Notes](device_credential_info_module.md#notes)
- [See Also](device_credential_info_module.md#see-also)
- [Examples](device_credential_info_module.md#examples)
- [Return Values](device_credential_info_module.md#return-values)

## [Synopsis](device_credential_info_module.md#id1)

- Get all Device Credential.
- API to get device credential details.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](device_credential_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](device_credential_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **headers**  dictionary | Additional headers. |
| **siteId**  string | SiteId query parameter. Site id to retrieve the credential details associated with the site. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](device_credential_info_module.md#id4)

> **Note:**
>
> - SDK Method used are network_settings.NetworkSettings.get_device_credential_details,
> - Paths used are get /dna/intent/api/v1/device-credential,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](device_credential_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Network Settings GetDeviceCredentialDetails](https://developer.cisco.com/docs/dna-center/#!get-device-credential-details)
> :   Complete reference of the GetDeviceCredentialDetails API.

## [Examples](device_credential_info_module.md#id6)

```yaml+jinja
- name: Get all Device Credential
  cisco.dnac.device_credential_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    siteId: string
  register: result
```

## [Return Values](device_credential_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"cli": [{"comments": "string", "credentialType": "string", "description": "string", "enablePassword": "string", "id": "string", "instanceTenantId": "string", "instanceUuid": "string", "password": "string", "username": "string"}], "http_read": [{"comments": "string", "credentialType": "string", "description": "string", "id": "string", "instanceTenantId": "string", "instanceUuid": "string", "password": "string", "port": "string", "secure": "string", "username": "string"}], "http_write": [{"comments": "string", "credentialType": "string", "description": "string", "id": "string", "instanceTenantId": "string", "instanceUuid": "string", "password": "string", "port": "string", "secure": "string", "username": "string"}], "snmp_v2_read": [{"comments": "string", "credentialType": "string", "description": "string", "id": "string", "instanceTenantId": "string", "instanceUuid": "string", "readCommunity": "string"}], "snmp_v2_write": [{"comments": "string", "credentialType": "string", "description": "string", "id": "string", "instanceTenantId": "string", "instanceUuid": "string", "writeCommunity": "string"}], "snmp_v3": [{"authPassword": "string", "authType": "string", "comments": "string", "credentialType": "string", "description": "string", "id": "string", "instanceTenantId": "string", "instanceUuid": "string", "privacyPassword": "string", "privacyType": "string", "snmpMode": "string", "username": "string"}]}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
