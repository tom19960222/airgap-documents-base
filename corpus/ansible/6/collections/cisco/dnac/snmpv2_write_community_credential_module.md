---
collection: ansible
version: "6"
title: "cisco.dnac.snmpv2_write_community_credential module – Resource module for Snmpv2 Write Community Credential"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/snmpv2_write_community_credential_module.html
fetched_at: 2026-07-27T16:54:20+00:00
---
# cisco.dnac.snmpv2_write_community_credential module – Resource module for Snmpv2 Write Community Credential

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
> see [Requirements](snmpv2_write_community_credential_module.md#ansible-collections-cisco-dnac-snmpv2-write-community-credential-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.snmpv2_write_community_credential`.

New in cisco.dnac 3.1.0

- [Synopsis](snmpv2_write_community_credential_module.md#synopsis)
- [Requirements](snmpv2_write_community_credential_module.md#requirements)
- [Parameters](snmpv2_write_community_credential_module.md#parameters)
- [Notes](snmpv2_write_community_credential_module.md#notes)
- [See Also](snmpv2_write_community_credential_module.md#see-also)
- [Examples](snmpv2_write_community_credential_module.md#examples)
- [Return Values](snmpv2_write_community_credential_module.md#return-values)

## [Synopsis](snmpv2_write_community_credential_module.md#id1)

- Manage operations create and update of the resource Snmpv2 Write Community Credential.
- Adds global SNMP write community.
- Updates global SNMP write community.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](snmpv2_write_community_credential_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](snmpv2_write_community_credential_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **comments**  string | Comments to identify the credential. |
| **credentialType**  string | Credential type to identify the application that uses the credential. |
| **description**  string | Name/Description of the credential. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **instanceUuid**  string | Snmpv2 Write Community Credential’s instanceUuid. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |
| **writeCommunity**  string | SNMP write community. NO!$DATA!$ for no value change. |

## [Notes](snmpv2_write_community_credential_module.md#id4)

> **Note:**
>
> - SDK Method used are discovery.Discovery.create_snmp_write_community, discovery.Discovery.update_snmp_write_community,
> - Paths used are post /dna/intent/api/v1/global-credential/snmpv2-write-community, put /dna/intent/api/v1/global-credential/snmpv2-write-community,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](snmpv2_write_community_credential_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Discovery CreateSNMPWriteCommunity](https://developer.cisco.com/docs/dna-center/#!create-snmp-write-community)
> :   Complete reference of the CreateSNMPWriteCommunity API.
>
> [Cisco DNA Center documentation for Discovery UpdateSNMPWriteCommunity](https://developer.cisco.com/docs/dna-center/#!update-snmp-write-community)
> :   Complete reference of the UpdateSNMPWriteCommunity API.

## [Examples](snmpv2_write_community_credential_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.snmpv2_write_community_credential:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    comments: string
    credentialType: string
    description: string
    writeCommunity: string

- name: Update all
  cisco.dnac.snmpv2_write_community_credential:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    comments: string
    credentialType: string
    description: string
    instanceUuid: string
    writeCommunity: string
```

## [Return Values](snmpv2_write_community_credential_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"response": {"taskId": "string", "url": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
