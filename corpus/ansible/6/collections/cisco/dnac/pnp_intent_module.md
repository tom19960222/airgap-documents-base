---
collection: ansible
version: "6"
title: "cisco.dnac.pnp_intent module – Resource module for Site and PnP related functions"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/pnp_intent_module.html
fetched_at: 2026-07-27T16:53:18+00:00
---
# cisco.dnac.pnp_intent module – Resource module for Site and PnP related functions

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
> see [Requirements](pnp_intent_module.md#ansible-collections-cisco-dnac-pnp-intent-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.pnp_intent`.

New in cisco.dnac 6.6.0

- [Synopsis](pnp_intent_module.md#synopsis)
- [Requirements](pnp_intent_module.md#requirements)
- [Parameters](pnp_intent_module.md#parameters)
- [Notes](pnp_intent_module.md#notes)
- [Examples](pnp_intent_module.md#examples)
- [Return Values](pnp_intent_module.md#return-values)

## [Synopsis](pnp_intent_module.md#id1)

- Manage operations add device, claim device and unclaim device of Onboarding Configuration(PnP) resource
- API to add device to pnp inventory and claim it to a site.
- API to delete device from the pnp inventory.

## [Requirements](pnp_intent_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk == 2.4.5
- python >= 3.5

## [Parameters](pnp_intent_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary / required | List of details of device being managed. |
| **deviceInfo**  dictionary | Pnp Device’s deviceInfo. |
| **aaaCredentials**  dictionary | Pnp Device’s aaaCredentials. |
| **password**  string | Pnp Device’s password. |
| **username**  string | Pnp Device’s username. |
| **addedOn**  integer | Pnp Device’s addedOn. |
| **addnMacAddrs**  list / elements=string | Pnp Device’s addnMacAddrs. |
| **agentType**  string | Pnp Device’s agentType. |
| **authenticatedSudiSerialNo**  string | Pnp Device’s authenticatedSudiSerialNo. |
| **authStatus**  string | Pnp Device’s authStatus. |
| **capabilitiesSupported**  list / elements=string | Pnp Device’s capabilitiesSupported. |
| **cmState**  string | Pnp Device’s cmState. |
| **description**  string | Pnp Device’s description. |
| **deviceSudiSerialNos**  list / elements=string | Pnp Device’s deviceSudiSerialNos. |
| **deviceType**  string | Pnp Device’s deviceType. |
| **featuresSupported**  list / elements=string | Pnp Device’s featuresSupported. |
| **fileSystemList**  list / elements=dictionary | Pnp Device’s fileSystemList. |
| **freespace**  integer | Pnp Device’s freespace. |
| **name**  string | Pnp Device’s name. |
| **readable**  boolean | Readable flag.  Choices:   - `false` - `true` |
| **size**  integer | Pnp Device’s size. |
| **type**  string | Pnp Device’s type. |
| **writeable**  boolean | Writeable flag.  Choices:   - `false` - `true` |
| **firstContact**  integer | Pnp Device’s firstContact. |
| **hostname**  string | Pnp Device’s hostname. |
| **httpHeaders**  list / elements=dictionary | Pnp Device’s httpHeaders. |
| **key**  string | Pnp Device’s key. |
| **value**  string | Pnp Device’s value. |
| **imageFile**  string | Pnp Device’s imageFile. |
| **imageVersion**  string | Pnp Device’s imageVersion. |
| **ipInterfaces**  list / elements=dictionary | Pnp Device’s ipInterfaces. |
| **ipv4Address**  dictionary | Pnp Device’s ipv4Address. |
| **ipv6AddressList**  list / elements=dictionary | Pnp Device’s ipv6AddressList. |
| **macAddress**  string | Pnp Device’s macAddress. |
| **name**  string | Pnp Device’s name. |
| **status**  string | Pnp Device’s status. |
| **lastContact**  integer | Pnp Device’s lastContact. |
| **lastSyncTime**  integer | Pnp Device’s lastSyncTime. |
| **lastUpdateOn**  integer | Pnp Device’s lastUpdateOn. |
| **location**  dictionary | Pnp Device’s location. |
| **address**  string | Pnp Device’s address. |
| **altitude**  string | Pnp Device’s altitude. |
| **latitude**  string | Pnp Device’s latitude. |
| **longitude**  string | Pnp Device’s longitude. |
| **siteId**  string | Pnp Device’s siteId. |
| **macAddress**  string | Pnp Device’s macAddress. |
| **mode**  string | Pnp Device’s mode. |
| **name**  string | Pnp Device’s name. |
| **neighborLinks**  list / elements=dictionary | Pnp Device’s neighborLinks. |
| **localInterfaceName**  string | Pnp Device’s localInterfaceName. |
| **localMacAddress**  string | Pnp Device’s localMacAddress. |
| **localShortInterfaceName**  string | Pnp Device’s localShortInterfaceName. |
| **remoteDeviceName**  string | Pnp Device’s remoteDeviceName. |
| **remoteInterfaceName**  string | Pnp Device’s remoteInterfaceName. |
| **remoteMacAddress**  string | Pnp Device’s remoteMacAddress. |
| **remotePlatform**  string | Pnp Device’s remotePlatform. |
| **remoteShortInterfaceName**  string | Pnp Device’s remoteShortInterfaceName. |
| **remoteVersion**  string | Pnp Device’s remoteVersion. |
| **onbState**  string | Pnp Device’s onbState. |
| **pid**  string | Pnp Device’s pid. |
| **pnpProfileList**  list / elements=dictionary | Pnp Device’s pnpProfileList. |
| **createdBy**  string | Pnp Device’s createdBy. |
| **discoveryCreated**  boolean | DiscoveryCreated flag.  Choices:   - `false` - `true` |
| **primaryEndpoint**  dictionary | Pnp Device’s primaryEndpoint. |
| **certificate**  string | Pnp Device’s certificate. |
| **fqdn**  string | Pnp Device’s fqdn. |
| **ipv4Address**  dictionary | Pnp Device’s ipv4Address. |
| **ipv6Address**  dictionary | Pnp Device’s ipv6Address. |
| **port**  integer | Pnp Device’s port. |
| **protocol**  string | Pnp Device’s protocol. |
| **profileName**  string | Pnp Device’s profileName. |
| **secondaryEndpoint**  dictionary | Pnp Device’s secondaryEndpoint. |
| **certificate**  string | Pnp Device’s certificate. |
| **fqdn**  string | Pnp Device’s fqdn. |
| **ipv4Address**  dictionary | Pnp Device’s ipv4Address. |
| **ipv6Address**  dictionary | Pnp Device’s ipv6Address. |
| **port**  integer | Pnp Device’s port. |
| **protocol**  string | Pnp Device’s protocol. |
| **populateInventory**  boolean | PopulateInventory flag.  Choices:   - `false` - `true` |
| **preWorkflowCliOuputs**  list / elements=dictionary | Pnp Device’s preWorkflowCliOuputs. |
| **cli**  string | Pnp Device’s cli. |
| **cliOutput**  string | Pnp Device’s cliOutput. |
| **projectId**  string | Pnp Device’s projectId. |
| **projectName**  string | Pnp Device’s projectName. |
| **reloadRequested**  boolean | ReloadRequested flag.  Choices:   - `false` - `true` |
| **serialNumber**  string | Pnp Device’s serialNumber. |
| **smartAccountId**  string | Pnp Device’s smartAccountId. |
| **source**  string | Pnp Device’s source. |
| **stack**  boolean | Stack flag.  Choices:   - `false` - `true` |
| **stackInfo**  dictionary | Pnp Device’s stackInfo. |
| **isFullRing**  boolean | IsFullRing flag.  Choices:   - `false` - `true` |
| **stackMemberList**  list / elements=dictionary | Pnp Device’s stackMemberList. |
| **hardwareVersion**  string | Pnp Device’s hardwareVersion. |
| **licenseLevel**  string | Pnp Device’s licenseLevel. |
| **licenseType**  string | Pnp Device’s licenseType. |
| **macAddress**  string | Pnp Device’s macAddress. |
| **pid**  string | Pnp Device’s pid. |
| **priority**  integer | Pnp Device’s priority. |
| **role**  string | Pnp Device’s role. |
| **serialNumber**  string | Pnp Device’s serialNumber. |
| **softwareVersion**  string | Pnp Device’s softwareVersion. |
| **stackNumber**  integer | Pnp Device’s stackNumber. |
| **state**  string | Pnp Device’s state. |
| **sudiSerialNumber**  string | Pnp Device’s sudiSerialNumber. |
| **stackRingProtocol**  string | Pnp Device’s stackRingProtocol. |
| **supportsStackWorkflows**  boolean | SupportsStackWorkflows flag.  Choices:   - `false` - `true` |
| **totalMemberCount**  integer | Pnp Device’s totalMemberCount. |
| **validLicenseLevels**  string | Pnp Device’s validLicenseLevels. |
| **state**  string | Pnp Device’s state. |
| **sudiRequired**  boolean | SudiRequired flag.  Choices:   - `false` - `true` |
| **tags**  dictionary | Pnp Device’s tags. |
| **userSudiSerialNos**  list / elements=string | Pnp Device’s userSudiSerialNos. |
| **virtualAccountId**  string | Pnp Device’s virtualAccountId. |
| **workflowId**  string | Pnp Device’s workflowId. |
| **workflowName**  string | Pnp Device’s workflowName. |
| **golden_image**  boolean | Is the image to be condifgured tagged as golden image  Choices:   - `false` - `true` |
| **image_name**  string | Name of image to be configured on the device |
| **site_name**  string | Name of the site for which device will be claimed. |
| **template_name**  string | Name of template to be configured on the device. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_log**  boolean | Flag for logging playbook execution details. If set to true the log file will be created at the location of the execution with the name dnac.log  Choices:   - `false` ← (default) - `true` |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  string | The Cisco DNA Center port.  Default: `"443"` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.2.3.3"` |
| **state**  string | The state of DNAC after module completion.  Choices:   - `"merged"` ← (default) - `"deleted"` |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](pnp_intent_module.md#id4)

> **Note:**
>
> - SDK Method used are device_onboarding_pnp.DeviceOnboardingPnp.add_device, device_onboarding_pnp.DeviceOnboardingPnp.claim_a_device_to_a_site, device_onboarding_pnp.DeviceOnboardingPnp.delete_device_by_id_from_pnp,
> - Paths used are post /dna/intent/api/v1/onboarding/pnp-device post /dna/intent/api/v1/onboarding/pnp-device/site-claim post /dna/intent/api/v1/onboarding/pnp-device/{id}
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [Examples](pnp_intent_module.md#id5)

```yaml+jinja
- name: Add a new device and claim the device
  cisco.dnac.pnp_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    state: merged
    config:
        template_name: string
        image_name: string
        site_name: string
        deviceInfo:
        aaaCredentials:
          password: string
          username: string
        addedOn: 0
        addnMacAddrs:
        - string
        agentType: string
        authStatus: string
        authenticatedSudiSerialNo: string
        capabilitiesSupported:
        - string
        cmState: string
        description: string
        deviceSudiSerialNos:
        - string
        deviceType: string
        featuresSupported:
        - string
        fileSystemList:
        - freespace: 0
          name: string
          readable: true
          size: 0
          type: string
          writeable: true
        firstContact: 0
        hostname: string
        httpHeaders:
        - key: string
          value: string
        imageFile: string
        imageVersion: string
        ipInterfaces:
        - ipv4Address: {}
          ipv6AddressList:
          - {}
          macAddress: string
          name: string
          status: string
        lastContact: 0
        lastSyncTime: 0
        lastUpdateOn: 0
        location:
          address: string
          altitude: string
          latitude: string
          longitude: string
          siteId: string
        macAddress: string
        mode: string
        name: string
        neighborLinks:
        - localInterfaceName: string
          localMacAddress: string
          localShortInterfaceName: string
          remoteDeviceName: string
          remoteInterfaceName: string
          remoteMacAddress: string
          remotePlatform: string
          remoteShortInterfaceName: string
          remoteVersion: string
        onbState: string
        pid: string
        pnpProfileList:
        - createdBy: string
          discoveryCreated: true
          primaryEndpoint:
            certificate: string
            fqdn: string
            ipv4Address: {}
            ipv6Address: {}
            port: 0
            protocol: string
          profileName: string
          secondaryEndpoint:
            certificate: string
            fqdn: string
            ipv4Address: {}
            ipv6Address: {}
            port: 0
            protocol: string
        populateInventory: true
        preWorkflowCliOuputs:
        - cli: string
          cliOutput: string
        projectId: string
        projectName: string
        reloadRequested: true
        serialNumber: string
        smartAccountId: string
        source: string
        stack: true
        stackInfo:
          isFullRing: true
          stackMemberList:
          - hardwareVersion: string
            licenseLevel: string
            licenseType: string
            macAddress: string
            pid: string
            priority: 0
            role: string
            serialNumber: string
            softwareVersion: string
            stackNumber: 0
            state: string
            sudiSerialNumber: string
          stackRingProtocol: string
          supportsStackWorkflows: true
          totalMemberCount: 0
          validLicenseLevels: string
        state: string
        sudiRequired: true
        tags: {}
        userSudiSerialNos:
        - string
        virtualAccountId: string
        workflowId: string
        workflowName: string
```

## [Return Values](pnp_intent_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **response_1**  dictionary | A dictionary with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `"{\n  \"response\":\n    {\n      \"response\": String,\n      \"version\": String\n    },\n  \"msg\": String\n}\n"` |
| **response_2**  list / elements=string | A list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `["{\n  \"response\": []", "\n  \"msg\": String\n}\n"]` |
| **response_3**  dictionary | A string with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `"{\n  \"response\": String,\n  \"msg\": String\n}\n"` |

### Authors

- Madhan Sankaranarayanan (@madhansansel) Rishita Chowdhary (@rishitachowdhary)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
