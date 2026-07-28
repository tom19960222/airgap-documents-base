---
collection: ansible
version: "6"
title: "cisco.dnac.pnp_device_import module – Resource module for Pnp Device Import"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/pnp_device_import_module.html
fetched_at: 2026-07-27T16:53:14+00:00
---
# cisco.dnac.pnp_device_import module – Resource module for Pnp Device Import

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
> see [Requirements](pnp_device_import_module.md#ansible-collections-cisco-dnac-pnp-device-import-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.pnp_device_import`.

New in cisco.dnac 3.1.0

- [Synopsis](pnp_device_import_module.md#synopsis)
- [Requirements](pnp_device_import_module.md#requirements)
- [Parameters](pnp_device_import_module.md#parameters)
- [Notes](pnp_device_import_module.md#notes)
- [See Also](pnp_device_import_module.md#see-also)
- [Examples](pnp_device_import_module.md#examples)
- [Return Values](pnp_device_import_module.md#return-values)

## [Synopsis](pnp_device_import_module.md#id1)

- Manage operation create of the resource Pnp Device Import.
- Add devices to PnP in bulk.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](pnp_device_import_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](pnp_device_import_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **payload**  list / elements=dictionary | Pnp Device Import’s payload. |
| **_id**  string | Pnp Device Import’s _id. |
| **deviceInfo**  dictionary | Pnp Device Import’s deviceInfo. |
| **aaaCredentials**  dictionary | Pnp Device Import’s aaaCredentials. |
| **password**  string | Pnp Device Import’s password. |
| **username**  string | Pnp Device Import’s username. |
| **addedOn**  integer | Pnp Device Import’s addedOn. |
| **addnMacAddrs**  list / elements=string | Pnp Device Import’s addnMacAddrs. |
| **agentType**  string | Pnp Device Import’s agentType. |
| **authenticatedSudiSerialNo**  string | Pnp Device Import’s authenticatedSudiSerialNo. |
| **authStatus**  string | Pnp Device Import’s authStatus. |
| **capabilitiesSupported**  list / elements=string | Pnp Device Import’s capabilitiesSupported. |
| **cmState**  string | Pnp Device Import’s cmState. |
| **description**  string | Pnp Device Import’s description. |
| **deviceSudiSerialNos**  list / elements=string | Pnp Device Import’s deviceSudiSerialNos. |
| **deviceType**  string | Pnp Device Import’s deviceType. |
| **featuresSupported**  list / elements=string | Pnp Device Import’s featuresSupported. |
| **fileSystemList**  list / elements=dictionary | Pnp Device Import’s fileSystemList. |
| **freespace**  integer | Pnp Device Import’s freespace. |
| **name**  string | Pnp Device Import’s name. |
| **readable**  boolean | Readable flag.  Choices:   - `false` - `true` |
| **size**  integer | Pnp Device Import’s size. |
| **type**  string | Pnp Device Import’s type. |
| **writeable**  boolean | Writeable flag.  Choices:   - `false` - `true` |
| **firstContact**  integer | Pnp Device Import’s firstContact. |
| **hostname**  string | Pnp Device Import’s hostname. |
| **httpHeaders**  list / elements=dictionary | Pnp Device Import’s httpHeaders. |
| **key**  string | Pnp Device Import’s key. |
| **value**  string | Pnp Device Import’s value. |
| **imageFile**  string | Pnp Device Import’s imageFile. |
| **imageVersion**  string | Pnp Device Import’s imageVersion. |
| **ipInterfaces**  list / elements=dictionary | Pnp Device Import’s ipInterfaces. |
| **ipv4Address**  dictionary | Pnp Device Import’s ipv4Address. |
| **ipv6AddressList**  list / elements=dictionary | Pnp Device Import’s ipv6AddressList. |
| **macAddress**  string | Pnp Device Import’s macAddress. |
| **name**  string | Pnp Device Import’s name. |
| **status**  string | Pnp Device Import’s status. |
| **lastContact**  integer | Pnp Device Import’s lastContact. |
| **lastSyncTime**  integer | Pnp Device Import’s lastSyncTime. |
| **lastUpdateOn**  integer | Pnp Device Import’s lastUpdateOn. |
| **location**  dictionary | Pnp Device Import’s location. |
| **address**  string | Pnp Device Import’s address. |
| **altitude**  string | Pnp Device Import’s altitude. |
| **latitude**  string | Pnp Device Import’s latitude. |
| **longitude**  string | Pnp Device Import’s longitude. |
| **siteId**  string | Pnp Device Import’s siteId. |
| **macAddress**  string | Pnp Device Import’s macAddress. |
| **mode**  string | Pnp Device Import’s mode. |
| **name**  string | Pnp Device Import’s name. |
| **neighborLinks**  list / elements=dictionary | Pnp Device Import’s neighborLinks. |
| **localInterfaceName**  string | Pnp Device Import’s localInterfaceName. |
| **localMacAddress**  string | Pnp Device Import’s localMacAddress. |
| **localShortInterfaceName**  string | Pnp Device Import’s localShortInterfaceName. |
| **remoteDeviceName**  string | Pnp Device Import’s remoteDeviceName. |
| **remoteInterfaceName**  string | Pnp Device Import’s remoteInterfaceName. |
| **remoteMacAddress**  string | Pnp Device Import’s remoteMacAddress. |
| **remotePlatform**  string | Pnp Device Import’s remotePlatform. |
| **remoteShortInterfaceName**  string | Pnp Device Import’s remoteShortInterfaceName. |
| **remoteVersion**  string | Pnp Device Import’s remoteVersion. |
| **onbState**  string | Pnp Device Import’s onbState. |
| **pid**  string | Pnp Device Import’s pid. |
| **pnpProfileList**  list / elements=dictionary | Pnp Device Import’s pnpProfileList. |
| **createdBy**  string | Pnp Device Import’s createdBy. |
| **discoveryCreated**  boolean | DiscoveryCreated flag.  Choices:   - `false` - `true` |
| **primaryEndpoint**  dictionary | Pnp Device Import’s primaryEndpoint. |
| **certificate**  string | Pnp Device Import’s certificate. |
| **fqdn**  string | Pnp Device Import’s fqdn. |
| **ipv4Address**  dictionary | Pnp Device Import’s ipv4Address. |
| **ipv6Address**  dictionary | Pnp Device Import’s ipv6Address. |
| **port**  integer | Pnp Device Import’s port. |
| **protocol**  string | Pnp Device Import’s protocol. |
| **profileName**  string | Pnp Device Import’s profileName. |
| **secondaryEndpoint**  dictionary | Pnp Device Import’s secondaryEndpoint. |
| **certificate**  string | Pnp Device Import’s certificate. |
| **fqdn**  string | Pnp Device Import’s fqdn. |
| **ipv4Address**  dictionary | Pnp Device Import’s ipv4Address. |
| **ipv6Address**  dictionary | Pnp Device Import’s ipv6Address. |
| **port**  integer | Pnp Device Import’s port. |
| **protocol**  string | Pnp Device Import’s protocol. |
| **populateInventory**  boolean | PopulateInventory flag.  Choices:   - `false` - `true` |
| **preWorkflowCliOuputs**  list / elements=dictionary | Pnp Device Import’s preWorkflowCliOuputs. |
| **cli**  string | Pnp Device Import’s cli. |
| **cliOutput**  string | Pnp Device Import’s cliOutput. |
| **projectId**  string | Pnp Device Import’s projectId. |
| **projectName**  string | Pnp Device Import’s projectName. |
| **reloadRequested**  boolean | ReloadRequested flag.  Choices:   - `false` - `true` |
| **serialNumber**  string | Pnp Device Import’s serialNumber. |
| **smartAccountId**  string | Pnp Device Import’s smartAccountId. |
| **source**  string | Pnp Device Import’s source. |
| **stack**  boolean | Stack flag.  Choices:   - `false` - `true` |
| **stackInfo**  dictionary | Pnp Device Import’s stackInfo. |
| **isFullRing**  boolean | IsFullRing flag.  Choices:   - `false` - `true` |
| **stackMemberList**  list / elements=dictionary | Pnp Device Import’s stackMemberList. |
| **hardwareVersion**  string | Pnp Device Import’s hardwareVersion. |
| **licenseLevel**  string | Pnp Device Import’s licenseLevel. |
| **licenseType**  string | Pnp Device Import’s licenseType. |
| **macAddress**  string | Pnp Device Import’s macAddress. |
| **pid**  string | Pnp Device Import’s pid. |
| **priority**  integer | Pnp Device Import’s priority. |
| **role**  string | Pnp Device Import’s role. |
| **serialNumber**  string | Pnp Device Import’s serialNumber. |
| **softwareVersion**  string | Pnp Device Import’s softwareVersion. |
| **stackNumber**  integer | Pnp Device Import’s stackNumber. |
| **state**  string | Pnp Device Import’s state. |
| **sudiSerialNumber**  string | Pnp Device Import’s sudiSerialNumber. |
| **stackRingProtocol**  string | Pnp Device Import’s stackRingProtocol. |
| **supportsStackWorkflows**  boolean | SupportsStackWorkflows flag.  Choices:   - `false` - `true` |
| **totalMemberCount**  integer | Pnp Device Import’s totalMemberCount. |
| **validLicenseLevels**  list / elements=string | Pnp Device Import’s validLicenseLevels. |
| **state**  string | Pnp Device Import’s state. |
| **sudiRequired**  boolean | SudiRequired flag.  Choices:   - `false` - `true` |
| **tags**  dictionary | Pnp Device Import’s tags. |
| **userSudiSerialNos**  list / elements=string | Pnp Device Import’s userSudiSerialNos. |
| **virtualAccountId**  string | Pnp Device Import’s virtualAccountId. |
| **workflowId**  string | Pnp Device Import’s workflowId. |
| **workflowName**  string | Pnp Device Import’s workflowName. |
| **runSummaryList**  list / elements=dictionary | Pnp Device Import’s runSummaryList. |
| **details**  string | Pnp Device Import’s details. |
| **errorFlag**  boolean | ErrorFlag flag.  Choices:   - `false` - `true` |
| **historyTaskInfo**  dictionary | Pnp Device Import’s historyTaskInfo. |
| **addnDetails**  list / elements=dictionary | Pnp Device Import’s addnDetails. |
| **key**  string | Pnp Device Import’s key. |
| **value**  string | Pnp Device Import’s value. |
| **name**  string | Pnp Device Import’s name. |
| **timeTaken**  integer | Pnp Device Import’s timeTaken. |
| **type**  string | Pnp Device Import’s type. |
| **workItemList**  list / elements=dictionary | Pnp Device Import’s workItemList. |
| **command**  string | Pnp Device Import’s command. |
| **endTime**  integer | Pnp Device Import’s endTime. |
| **outputStr**  string | Pnp Device Import’s outputStr. |
| **startTime**  integer | Pnp Device Import’s startTime. |
| **state**  string | Pnp Device Import’s state. |
| **timeTaken**  integer | Pnp Device Import’s timeTaken. |
| **timestamp**  integer | Pnp Device Import’s timestamp. |
| **systemResetWorkflow**  dictionary | Pnp Device Import’s systemResetWorkflow. |
| **_id**  string | Pnp Device Import’s _id. |
| **addedOn**  integer | Pnp Device Import’s addedOn. |
| **addToInventory**  boolean | AddToInventory flag.  Choices:   - `false` - `true` |
| **configId**  string | Pnp Device Import’s configId. |
| **currTaskIdx**  integer | Pnp Device Import’s currTaskIdx. |
| **description**  string | Pnp Device Import’s description. |
| **endTime**  integer | Pnp Device Import’s endTime. |
| **execTime**  integer | Pnp Device Import’s execTime. |
| **imageId**  string | Pnp Device Import’s imageId. |
| **instanceType**  string | Pnp Device Import’s instanceType. |
| **lastupdateOn**  integer | Pnp Device Import’s lastupdateOn. |
| **name**  string | Pnp Device Import’s name. |
| **startTime**  integer | Pnp Device Import’s startTime. |
| **state**  string | Pnp Device Import’s state. |
| **tasks**  list / elements=dictionary | Pnp Device Import’s tasks. |
| **currWorkItemIdx**  integer | Pnp Device Import’s currWorkItemIdx. |
| **endTime**  integer | Pnp Device Import’s endTime. |
| **name**  string | Pnp Device Import’s name. |
| **startTime**  integer | Pnp Device Import’s startTime. |
| **state**  string | Pnp Device Import’s state. |
| **taskSeqNo**  integer | Pnp Device Import’s taskSeqNo. |
| **timeTaken**  integer | Pnp Device Import’s timeTaken. |
| **type**  string | Pnp Device Import’s type. |
| **workItemList**  list / elements=dictionary | Pnp Device Import’s workItemList. |
| **command**  string | Pnp Device Import’s command. |
| **endTime**  integer | Pnp Device Import’s endTime. |
| **outputStr**  string | Pnp Device Import’s outputStr. |
| **startTime**  integer | Pnp Device Import’s startTime. |
| **state**  string | Pnp Device Import’s state. |
| **timeTaken**  integer | Pnp Device Import’s timeTaken. |
| **tenantId**  string | Pnp Device Import’s tenantId. |
| **type**  string | Pnp Device Import’s type. |
| **useState**  string | Pnp Device Import’s useState. |
| **version**  integer | Pnp Device Import’s version. |
| **systemWorkflow**  dictionary | Pnp Device Import’s systemWorkflow. |
| **_id**  string | Pnp Device Import’s _id. |
| **addedOn**  integer | Pnp Device Import’s addedOn. |
| **addToInventory**  boolean | AddToInventory flag.  Choices:   - `false` - `true` |
| **configId**  string | Pnp Device Import’s configId. |
| **currTaskIdx**  integer | Pnp Device Import’s currTaskIdx. |
| **description**  string | Pnp Device Import’s description. |
| **endTime**  integer | Pnp Device Import’s endTime. |
| **execTime**  integer | Pnp Device Import’s execTime. |
| **imageId**  string | Pnp Device Import’s imageId. |
| **instanceType**  string | Pnp Device Import’s instanceType. |
| **lastupdateOn**  integer | Pnp Device Import’s lastupdateOn. |
| **name**  string | Pnp Device Import’s name. |
| **startTime**  integer | Pnp Device Import’s startTime. |
| **state**  string | Pnp Device Import’s state. |
| **tasks**  list / elements=dictionary | Pnp Device Import’s tasks. |
| **currWorkItemIdx**  integer | Pnp Device Import’s currWorkItemIdx. |
| **endTime**  integer | Pnp Device Import’s endTime. |
| **name**  string | Pnp Device Import’s name. |
| **startTime**  integer | Pnp Device Import’s startTime. |
| **state**  string | Pnp Device Import’s state. |
| **taskSeqNo**  integer | Pnp Device Import’s taskSeqNo. |
| **timeTaken**  integer | Pnp Device Import’s timeTaken. |
| **type**  string | Pnp Device Import’s type. |
| **workItemList**  list / elements=dictionary | Pnp Device Import’s workItemList. |
| **command**  string | Pnp Device Import’s command. |
| **endTime**  integer | Pnp Device Import’s endTime. |
| **outputStr**  string | Pnp Device Import’s outputStr. |
| **startTime**  integer | Pnp Device Import’s startTime. |
| **state**  string | Pnp Device Import’s state. |
| **timeTaken**  integer | Pnp Device Import’s timeTaken. |
| **tenantId**  string | Pnp Device Import’s tenantId. |
| **type**  string | Pnp Device Import’s type. |
| **useState**  string | Pnp Device Import’s useState. |
| **version**  integer | Pnp Device Import’s version. |
| **tenantId**  string | Pnp Device Import’s tenantId. |
| **version**  integer | Pnp Device Import’s version. |
| **workflow**  dictionary | Pnp Device Import’s workflow. |
| **_id**  string | Pnp Device Import’s _id. |
| **addedOn**  integer | Pnp Device Import’s addedOn. |
| **addToInventory**  boolean | AddToInventory flag.  Choices:   - `false` - `true` |
| **configId**  string | Pnp Device Import’s configId. |
| **currTaskIdx**  integer | Pnp Device Import’s currTaskIdx. |
| **description**  string | Pnp Device Import’s description. |
| **endTime**  integer | Pnp Device Import’s endTime. |
| **execTime**  integer | Pnp Device Import’s execTime. |
| **imageId**  string | Pnp Device Import’s imageId. |
| **instanceType**  string | Pnp Device Import’s instanceType. |
| **lastupdateOn**  integer | Pnp Device Import’s lastupdateOn. |
| **name**  string | Pnp Device Import’s name. |
| **startTime**  integer | Pnp Device Import’s startTime. |
| **state**  string | Pnp Device Import’s state. |
| **tasks**  list / elements=dictionary | Pnp Device Import’s tasks. |
| **currWorkItemIdx**  integer | Pnp Device Import’s currWorkItemIdx. |
| **endTime**  integer | Pnp Device Import’s endTime. |
| **name**  string | Pnp Device Import’s name. |
| **startTime**  integer | Pnp Device Import’s startTime. |
| **state**  string | Pnp Device Import’s state. |
| **taskSeqNo**  integer | Pnp Device Import’s taskSeqNo. |
| **timeTaken**  integer | Pnp Device Import’s timeTaken. |
| **type**  string | Pnp Device Import’s type. |
| **workItemList**  list / elements=dictionary | Pnp Device Import’s workItemList. |
| **command**  string | Pnp Device Import’s command. |
| **endTime**  integer | Pnp Device Import’s endTime. |
| **outputStr**  string | Pnp Device Import’s outputStr. |
| **startTime**  integer | Pnp Device Import’s startTime. |
| **state**  string | Pnp Device Import’s state. |
| **timeTaken**  integer | Pnp Device Import’s timeTaken. |
| **tenantId**  string | Pnp Device Import’s tenantId. |
| **type**  string | Pnp Device Import’s type. |
| **useState**  string | Pnp Device Import’s useState. |
| **version**  integer | Pnp Device Import’s version. |
| **workflowParameters**  dictionary | Pnp Device Import’s workflowParameters. |
| **configList**  list / elements=dictionary | Pnp Device Import’s configList. |
| **configId**  string | Pnp Device Import’s configId. |
| **configParameters**  list / elements=dictionary | Pnp Device Import’s configParameters. |
| **key**  string | Pnp Device Import’s key. |
| **value**  string | Pnp Device Import’s value. |
| **licenseLevel**  string | Pnp Device Import’s licenseLevel. |
| **licenseType**  string | Pnp Device Import’s licenseType. |
| **topOfStackSerialNumber**  string | Pnp Device Import’s topOfStackSerialNumber. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](pnp_device_import_module.md#id4)

> **Note:**
>
> - SDK Method used are device_onboarding_pnp.DeviceOnboardingPnp.import_devices_in_bulk,
> - Paths used are post /dna/intent/api/v1/onboarding/pnp-device/import,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](pnp_device_import_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Device Onboarding (PnP) ImportDevicesInBulk](https://developer.cisco.com/docs/dna-center/#!import-devices-in-bulk)
> :   Complete reference of the ImportDevicesInBulk API.

## [Examples](pnp_device_import_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.pnp_device_import:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    payload:
    - _id: string
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
          validLicenseLevels:
          - string
        state: string
        sudiRequired: true
        tags: {}
        userSudiSerialNos:
        - string
        virtualAccountId: string
        workflowId: string
        workflowName: string
      runSummaryList:
      - details: string
        errorFlag: true
        historyTaskInfo:
          addnDetails:
          - key: string
            value: string
          name: string
          timeTaken: 0
          type: string
          workItemList:
          - command: string
            endTime: 0
            outputStr: string
            startTime: 0
            state: string
            timeTaken: 0
        timestamp: 0
      systemResetWorkflow:
        _id: string
        addToInventory: true
        addedOn: 0
        configId: string
        currTaskIdx: 0
        description: string
        endTime: 0
        execTime: 0
        imageId: string
        instanceType: string
        lastupdateOn: 0
        name: string
        startTime: 0
        state: string
        tasks:
        - currWorkItemIdx: 0
          endTime: 0
          name: string
          startTime: 0
          state: string
          taskSeqNo: 0
          timeTaken: 0
          type: string
          workItemList:
          - command: string
            endTime: 0
            outputStr: string
            startTime: 0
            state: string
            timeTaken: 0
        tenantId: string
        type: string
        useState: string
        version: 0
      systemWorkflow:
        _id: string
        addToInventory: true
        addedOn: 0
        configId: string
        currTaskIdx: 0
        description: string
        endTime: 0
        execTime: 0
        imageId: string
        instanceType: string
        lastupdateOn: 0
        name: string
        startTime: 0
        state: string
        tasks:
        - currWorkItemIdx: 0
          endTime: 0
          name: string
          startTime: 0
          state: string
          taskSeqNo: 0
          timeTaken: 0
          type: string
          workItemList:
          - command: string
            endTime: 0
            outputStr: string
            startTime: 0
            state: string
            timeTaken: 0
        tenantId: string
        type: string
        useState: string
        version: 0
      tenantId: string
      version: 0
      workflow:
        _id: string
        addToInventory: true
        addedOn: 0
        configId: string
        currTaskIdx: 0
        description: string
        endTime: 0
        execTime: 0
        imageId: string
        instanceType: string
        lastupdateOn: 0
        name: string
        startTime: 0
        state: string
        tasks:
        - currWorkItemIdx: 0
          endTime: 0
          name: string
          startTime: 0
          state: string
          taskSeqNo: 0
          timeTaken: 0
          type: string
          workItemList:
          - command: string
            endTime: 0
            outputStr: string
            startTime: 0
            state: string
            timeTaken: 0
        tenantId: string
        type: string
        useState: string
        version: 0
      workflowParameters:
        configList:
        - configId: string
          configParameters:
          - key: string
            value: string
        licenseLevel: string
        licenseType: string
        topOfStackSerialNumber: string
```

## [Return Values](pnp_device_import_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"failureList": [{"id": "string", "index": 0, "msg": "string", "serialNum": "string"}], "successList": [{"_id": "string", "dayZeroConfig": {"config": "string"}, "dayZeroConfigPreview": {}, "deviceInfo": {"aaaCredentials": {"password": "string", "username": "string"}, "addedOn": 0, "addnMacAddrs": ["string"], "agentType": "string", "authStatus": "string", "authenticatedMicNumber": "string", "authenticatedSudiSerialNo": "string", "capabilitiesSupported": ["string"], "cmState": "string", "description": "string", "deviceSudiSerialNos": ["string"], "deviceType": "string", "featuresSupported": ["string"], "fileSystemList": [{"freespace": 0, "name": "string", "readable": true, "size": 0, "type": "string", "writeable": true}], "firstContact": 0, "hostname": "string", "httpHeaders": [{"key": "string", "value": "string"}], "imageFile": "string", "imageVersion": "string", "ipInterfaces": [{"ipv4Address": {}, "ipv6AddressList": [{}], "macAddress": "string", "name": "string", "status": "string"}], "lastContact": 0, "lastSyncTime": 0, "lastUpdateOn": 0, "location": {"address": "string", "altitude": "string", "latitude": "string", "longitude": "string", "siteId": "string"}, "macAddress": "string", "mode": "string", "name": "string", "neighborLinks": [{"localInterfaceName": "string", "localMacAddress": "string", "localShortInterfaceName": "string", "remoteDeviceName": "string", "remoteInterfaceName": "string", "remoteMacAddress": "string", "remotePlatform": "string", "remoteShortInterfaceName": "string", "remoteVersion": "string"}], "onbState": "string", "pid": "string", "pnpProfileList": [{"createdBy": "string", "discoveryCreated": true, "primaryEndpoint": {"certificate": "string", "fqdn": "string", "ipv4Address": {}, "ipv6Address": {}, "port": 0, "protocol": "string"}, "profileName": "string", "secondaryEndpoint": {"certificate": "string", "fqdn": "string", "ipv4Address": {}, "ipv6Address": {}, "port": 0, "protocol": "string"}}], "populateInventory": true, "preWorkflowCliOuputs": [{"cli": "string", "cliOutput": "string"}], "projectId": "string", "projectName": "string", "reloadRequested": true, "serialNumber": "string", "siteId": "string", "siteName": "string", "smartAccountId": "string", "source": "string", "stack": true, "stackInfo": {"isFullRing": true, "stackMemberList": [{"hardwareVersion": "string", "licenseLevel": "string", "licenseType": "string", "macAddress": "string", "pid": "string", "priority": 0, "role": "string", "serialNumber": "string", "softwareVersion": "string", "stackNumber": 0, "state": "string", "sudiSerialNumber": "string"}], "stackRingProtocol": "string", "supportsStackWorkflows": true, "totalMemberCount": 0, "validLicenseLevels": ["string"]}, "state": "string", "sudiRequired": true, "tags": {}, "userMicNumbers": ["string"], "userSudiSerialNos": ["string"], "virtualAccountId": "string", "workflowId": "string", "workflowName": "string"}, "runSummaryList": [{"details": "string", "errorFlag": true, "historyTaskInfo": {"addnDetails": [{"key": "string", "value": "string"}], "name": "string", "timeTaken": 0, "type": "string", "workItemList": [{"command": "string", "endTime": 0, "outputStr": "string", "startTime": 0, "state": "string", "timeTaken": 0}]}, "timestamp": 0}], "systemResetWorkflow": {"_id": "string", "addToInventory": true, "addedOn": 0, "configId": "string", "currTaskIdx": 0, "description": "string", "endTime": 0, "execTime": 0, "imageId": "string", "instanceType": "string", "lastupdateOn": 0, "name": "string", "startTime": 0, "state": "string", "tasks": [{"currWorkItemIdx": 0, "endTime": 0, "name": "string", "startTime": 0, "state": "string", "taskSeqNo": 0, "timeTaken": 0, "type": "string", "workItemList": [{"command": "string", "endTime": 0, "outputStr": "string", "startTime": 0, "state": "string", "timeTaken": 0}]}], "tenantId": "string", "type": "string", "useState": "string", "version": 0}, "systemWorkflow": {"_id": "string", "addToInventory": true, "addedOn": 0, "configId": "string", "currTaskIdx": 0, "description": "string", "endTime": 0, "execTime": 0, "imageId": "string", "instanceType": "string", "lastupdateOn": 0, "name": "string", "startTime": 0, "state": "string", "tasks": [{"currWorkItemIdx": 0, "endTime": 0, "name": "string", "startTime": 0, "state": "string", "taskSeqNo": 0, "timeTaken": 0, "type": "string", "workItemList": [{"command": "string", "endTime": 0, "outputStr": "string", "startTime": 0, "state": "string", "timeTaken": 0}]}], "tenantId": "string", "type": "string", "useState": "string", "version": 0}, "tenantId": "string", "version": 0, "workflow": {"_id": "string", "addToInventory": true, "addedOn": 0, "configId": "string", "currTaskIdx": 0, "description": "string", "endTime": 0, "execTime": 0, "imageId": "string", "instanceType": "string", "lastupdateOn": 0, "name": "string", "startTime": 0, "state": "string", "tasks": [{"currWorkItemIdx": 0, "endTime": 0, "name": "string", "startTime": 0, "state": "string", "taskSeqNo": 0, "timeTaken": 0, "type": "string", "workItemList": [{"command": "string", "endTime": 0, "outputStr": "string", "startTime": 0, "state": "string", "timeTaken": 0}]}], "tenantId": "string", "type": "string", "useState": "string", "version": 0}, "workflowParameters": {"configList": [{"configId": "string", "configParameters": [{"key": "string", "value": "string"}]}], "licenseLevel": "string", "licenseType": "string", "topOfStackSerialNumber": "string"}}]}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
