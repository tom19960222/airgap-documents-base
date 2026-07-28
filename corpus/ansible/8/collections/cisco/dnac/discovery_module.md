---
collection: ansible
version: "8"
title: "cisco.dnac.discovery module – Resource module for Discovery"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/discovery_module.html
fetched_at: 2026-07-28T01:22:06+00:00
---
# cisco.dnac.discovery module – Resource module for Discovery

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
> see [Requirements](discovery_module.md#ansible-collections-cisco-dnac-discovery-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.discovery`.

New in cisco.dnac 3.1.0

- [Synopsis](discovery_module.md#synopsis)
- [Requirements](discovery_module.md#requirements)
- [Parameters](discovery_module.md#parameters)
- [Notes](discovery_module.md#notes)
- [See Also](discovery_module.md#see-also)
- [Examples](discovery_module.md#examples)
- [Return Values](discovery_module.md#return-values)

## [Synopsis](discovery_module.md#id6)

- Manage operations create, update and delete of the resource Discovery.
- Initiates discovery with the given parameters.
- Stops all the discoveries and removes them.
- Stops the discovery for the given Discovery ID and removes it. Discovery ID can be obtained using the “Get Discoveries by range” API.
- Stops or starts an existing discovery.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](discovery_module.md#id7)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](discovery_module.md#id8)

| Parameter | Comments |
| --- | --- |
| **attributeInfo**  dictionary | Discovery’s attributeInfo. |
| **cdpLevel**  integer | Discovery’s cdpLevel. |
| **deviceIds**  string | Discovery’s deviceIds. |
| **discoveryCondition**  string | Discovery’s discoveryCondition. |
| **discoveryStatus**  string | Discovery’s discoveryStatus. |
| **discoveryType**  string | Discovery’s discoveryType. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **enablePasswordList**  string | Discovery’s enablePasswordList. |
| **globalCredentialIdList**  list / elements=string | Discovery’s globalCredentialIdList. |
| **httpReadCredential**  dictionary | Discovery’s httpReadCredential. |
| **comments**  string | Discovery’s comments. |
| **credentialType**  string | Discovery’s credentialType. |
| **description**  string | Discovery’s description. |
| **id**  string | Discovery’s id. |
| **instanceTenantId**  string | Discovery’s instanceTenantId. |
| **instanceUuid**  string | Discovery’s instanceUuid. |
| **password**  string | Discovery’s password. |
| **port**  integer | Discovery’s port. |
| **secure**  boolean | Secure flag.  **Choices:**   - `false` - `true` |
| **username**  string | Discovery’s username. |
| **httpWriteCredential**  dictionary | Discovery’s httpWriteCredential. |
| **comments**  string | Discovery’s comments. |
| **credentialType**  string | Discovery’s credentialType. |
| **description**  string | Discovery’s description. |
| **id**  string | Discovery’s id. |
| **instanceTenantId**  string | Discovery’s instanceTenantId. |
| **instanceUuid**  string | Discovery’s instanceUuid. |
| **password**  string | Discovery’s password. |
| **port**  integer | Discovery’s port. |
| **secure**  boolean | Secure flag.  **Choices:**   - `false` - `true` |
| **username**  string | Discovery’s username. |
| **id**  string | Discovery’s id. |
| **ipAddressList**  string | Discovery’s ipAddressList. |
| **ipFilterList**  string | Discovery’s ipFilterList. |
| **isAutoCdp**  boolean | IsAutoCdp flag.  **Choices:**   - `false` - `true` |
| **lldpLevel**  integer | Discovery’s lldpLevel. |
| **name**  string | Discovery’s name. |
| **netconfPort**  string | Discovery’s netconfPort. |
| **numDevices**  integer | Discovery’s numDevices. |
| **parentDiscoveryId**  string | Discovery’s parentDiscoveryId. |
| **passwordList**  string | Discovery’s passwordList. |
| **preferredMgmtIPMethod**  string | Discovery’s preferredMgmtIPMethod. |
| **protocolOrder**  string | Discovery’s protocolOrder. |
| **retry**  integer | Number of times to try establishing connection to device. |
| **retryCount**  integer | Discovery’s retryCount. |
| **snmpAuthPassphrase**  string | Discovery’s snmpAuthPassphrase. |
| **snmpAuthProtocol**  string | Discovery’s snmpAuthProtocol. |
| **snmpMode**  string | Discovery’s snmpMode. |
| **snmpPrivPassphrase**  string | Discovery’s snmpPrivPassphrase. |
| **snmpPrivProtocol**  string | Discovery’s snmpPrivProtocol. |
| **snmpROCommunity**  string | Snmp RO community of the devices to be discovered. |
| **snmpRoCommunity**  string | Discovery’s snmpRoCommunity. |
| **snmpROCommunityDesc**  string | Description for Snmp RO community. |
| **snmpRoCommunityDesc**  string | Discovery’s snmpRoCommunityDesc. |
| **snmpRWCommunity**  string | Snmp RW community of the devices to be discovered. |
| **snmpRwCommunity**  string | Discovery’s snmpRwCommunity. |
| **snmpRWCommunityDesc**  string | Description for Snmp RW community. |
| **snmpRwCommunityDesc**  string | Discovery’s snmpRwCommunityDesc. |
| **snmpUserName**  string | Discovery’s snmpUserName. |
| **snmpVersion**  string | Version of SNMP. V2 or v3. |
| **timeOut**  integer | Discovery’s timeOut. |
| **timeout**  integer | Time to wait for device response in seconds. |
| **updateMgmtIp**  boolean | UpdateMgmtIp flag.  **Choices:**   - `false` - `true` |
| **userNameList**  string | Discovery’s userNameList. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](discovery_module.md#id9)

> **Note:**
>
> - SDK Method used are discovery.Discovery.delete_discovery_by_id, discovery.Discovery.start_discovery, discovery.Discovery.updates_discovery_by_id,
> - Paths used are post /dna/intent/api/v1/discovery, delete /dna/intent/api/v1/discovery, delete /dna/intent/api/v1/discovery/{id}, put /dna/intent/api/v1/discovery,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](discovery_module.md#id10)

> **See also:**
>
> [Cisco DNA Center documentation for Discovery StartDiscovery](https://developer.cisco.com/docs/dna-center/#!start-discovery)
> :   Complete reference of the StartDiscovery API.
>
> [Cisco DNA Center documentation for Discovery DeleteAllDiscovery](https://developer.cisco.com/docs/dna-center/#!delete-all-discovery)
> :   Complete reference of the DeleteAllDiscovery API.
>
> [Cisco DNA Center documentation for Discovery DeleteDiscoveryById](https://developer.cisco.com/docs/dna-center/#!delete-discovery-by-id)
> :   Complete reference of the DeleteDiscoveryById API.
>
> [Cisco DNA Center documentation for Discovery UpdatesAnExistingDiscoveryBySpecifiedId](https://developer.cisco.com/docs/dna-center/#!updates-an-existing-discovery-by-specified-id)
> :   Complete reference of the UpdatesAnExistingDiscoveryBySpecifiedId API.

## [Examples](discovery_module.md#id11)

```yaml+jinja
- name: Delete all
  cisco.dnac.discovery:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent

- name: Update all
  cisco.dnac.discovery:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    attributeInfo: {}
    cdpLevel: 0
    deviceIds: string
    discoveryCondition: string
    discoveryStatus: string
    discoveryType: string
    enablePasswordList: string
    globalCredentialIdList:
    - string
    httpReadCredential:
      comments: string
      credentialType: string
      description: string
      id: string
      instanceTenantId: string
      instanceUuid: string
      password: string
      port: 0
      secure: true
      username: string
    httpWriteCredential:
      comments: string
      credentialType: string
      description: string
      id: string
      instanceTenantId: string
      instanceUuid: string
      password: string
      port: 0
      secure: true
      username: string
    id: string
    ipAddressList: string
    ipFilterList: string
    isAutoCdp: true
    lldpLevel: 0
    name: string
    netconfPort: string
    numDevices: 0
    parentDiscoveryId: string
    passwordList: string
    preferredMgmtIPMethod: string
    protocolOrder: string
    retryCount: 0
    snmpAuthPassphrase: string
    snmpAuthProtocol: string
    snmpMode: string
    snmpPrivPassphrase: string
    snmpPrivProtocol: string
    snmpRoCommunity: string
    snmpRoCommunityDesc: string
    snmpRwCommunity: string
    snmpRwCommunityDesc: string
    snmpUserName: string
    timeOut: 0
    updateMgmtIp: true
    userNameList: string

- name: Create
  cisco.dnac.discovery:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    cdpLevel: 0
    discoveryType: string
    enablePasswordList:
    - string
    globalCredentialIdList:
    - string
    httpReadCredential:
      password: string
      port: 0
      secure: true
      username: string
    httpWriteCredential:
      password: string
      port: 0
      secure: true
      username: string
    ipAddressList: string
    ipFilterList:
    - string
    lldpLevel: 0
    name: string
    netconfPort: string
    passwordList:
    - string
    preferredMgmtIPMethod: string
    protocolOrder: string
    retry: 0
    snmpAuthPassphrase: string
    snmpAuthProtocol: string
    snmpMode: string
    snmpPrivPassphrase: string
    snmpPrivProtocol: string
    snmpROCommunity: string
    snmpROCommunityDesc: string
    snmpRWCommunity: string
    snmpRWCommunityDesc: string
    snmpUserName: string
    snmpVersion: string
    timeout: 0
    userNameList:
    - string

- name: Delete by id
  cisco.dnac.discovery:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    id: string
```

## [Return Values](discovery_module.md#id12)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": {"taskId": "string", "url": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
