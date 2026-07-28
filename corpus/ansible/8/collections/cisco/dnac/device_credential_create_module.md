---
collection: ansible
version: "8"
title: "cisco.dnac.device_credential_create module – Resource module for Device Credential Create"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/device_credential_create_module.html
fetched_at: 2026-07-28T01:21:50+00:00
---
# cisco.dnac.device_credential_create module – Resource module for Device Credential Create

> **Note:**
>
> This module is part of the [cisco.dnac collection](https://galaxy.ansible.com/ui/repo/published/cisco/dnac/) (version 6.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.dnac`.
> You need further requirements to be able to use this module,
> see [Requirements](device_credential_create_module.md#ansible-collections-cisco-dnac-device-credential-create-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.device_credential_create`.

New in cisco.dnac 3.1.0

- [Synopsis](device_credential_create_module.md#synopsis)
- [Requirements](device_credential_create_module.md#requirements)
- [Parameters](device_credential_create_module.md#parameters)
- [Notes](device_credential_create_module.md#notes)
- [See Also](device_credential_create_module.md#see-also)
- [Examples](device_credential_create_module.md#examples)
- [Return Values](device_credential_create_module.md#return-values)

## [Synopsis](device_credential_create_module.md#id1)

- Manage operation create of the resource Device Credential Create.
- API to create device credentials.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](device_credential_create_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](device_credential_create_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **settings**  dictionary | Device Credential Create’s settings. |
| **cliCredential**  list / elements=dictionary | Device Credential Create’s cliCredential. |
| **description**  string | Name or description for CLI credential. |
| **enablePassword**  string | Enable password for CLI credential. |
| **password**  string | Password for CLI credential. |
| **username**  string | User name for CLI credential. |
| **httpsRead**  list / elements=dictionary | Device Credential Create’s httpsRead. |
| **name**  string | Name or description of http read credential. |
| **password**  string | Password for http read credential. |
| **port**  integer | Port for http read credential. |
| **username**  string | User name of the http read credential. |
| **httpsWrite**  list / elements=dictionary | Device Credential Create’s httpsWrite. |
| **name**  string | Name or description of http write credential. |
| **password**  string | Password for http write credential. |
| **port**  integer | Port for http write credential. |
| **username**  string | User name of the http write credential. |
| **snmpV2cRead**  list / elements=dictionary | Device Credential Create’s snmpV2cRead. |
| **description**  string | Description for snmp v2 read. |
| **readCommunity**  string | Ready community for snmp v2 read credential. |
| **snmpV2cWrite**  list / elements=dictionary | Device Credential Create’s snmpV2cWrite. |
| **description**  string | Description for snmp v2 write. |
| **writeCommunity**  string | Write community for snmp v2 write credential. |
| **snmpV3**  list / elements=dictionary | Device Credential Create’s snmpV3. |
| **authPassword**  string | Authentication password for snmpv3 credential. |
| **authType**  string | Authentication type for snmpv3 credential. |
| **description**  string | Name or description for SNMPV3 credential. |
| **privacyPassword**  string | Privacy password for snmpv3 credential. |
| **privacyType**  string | Privacy type for snmpv3 credential. |
| **snmpMode**  string | Mode for snmpv3 credential. |
| **username**  string | User name for SNMPv3 credential. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](device_credential_create_module.md#id4)

> **Note:**
>
> - SDK Method used are network_settings.NetworkSettings.create_device_credentials,
> - Paths used are post /dna/intent/api/v1/device-credential,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](device_credential_create_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Network Settings CreateDeviceCredentials](https://developer.cisco.com/docs/dna-center/#!create-device-credentials)
> :   Complete reference of the CreateDeviceCredentials API.

## [Examples](device_credential_create_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.device_credential_create:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    settings:
      cliCredential:
      - description: string
        enablePassword: string
        password: string
        username: string
      httpsRead:
      - name: string
        password: string
        port: 0
        username: string
      httpsWrite:
      - name: string
        password: string
        port: 0
        username: string
      snmpV2cRead:
      - description: string
        readCommunity: string
      snmpV2cWrite:
      - description: string
        writeCommunity: string
      snmpV3:
      - authPassword: string
        authType: string
        description: string
        privacyPassword: string
        privacyType: string
        snmpMode: string
        username: string
```

## [Return Values](device_credential_create_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"executionId": "string", "executionStatusUrl": "string", "message": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
