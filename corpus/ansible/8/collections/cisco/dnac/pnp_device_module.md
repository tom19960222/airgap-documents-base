---
collection: ansible
version: "8"
title: "cisco.dnac.pnp_device module – Resource module for Pnp Device"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/pnp_device_module.html
fetched_at: 2026-07-28T01:23:53+00:00
---
# cisco.dnac.pnp_device module – Resource module for Pnp Device

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
> see [Requirements](pnp_device_module.md#ansible-collections-cisco-dnac-pnp-device-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.pnp_device`.

New in cisco.dnac 3.1.0

- [Synopsis](pnp_device_module.md#synopsis)
- [Requirements](pnp_device_module.md#requirements)
- [Parameters](pnp_device_module.md#parameters)
- [Notes](pnp_device_module.md#notes)
- [See Also](pnp_device_module.md#see-also)
- [Examples](pnp_device_module.md#examples)
- [Return Values](pnp_device_module.md#return-values)

## [Synopsis](pnp_device_module.md#id2)

- Manage operations create, update and delete of the resource Pnp Device.
- Adds a device to the PnP database.
- Deletes specified device from PnP database.
- Updates device details specified by device id in PnP database.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](pnp_device_module.md#id3)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](pnp_device_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **_id**  string | Pnp Device’s _id. |
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
| **readable**  boolean | Readable flag.  **Choices:**   - `false` - `true` |
| **size**  integer | Pnp Device’s size. |
| **type**  string | Pnp Device’s type. |
| **writeable**  boolean | Writeable flag.  **Choices:**   - `false` - `true` |
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
| **discoveryCreated**  boolean | DiscoveryCreated flag.  **Choices:**   - `false` - `true` |
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
| **populateInventory**  boolean | PopulateInventory flag.  **Choices:**   - `false` - `true` |
| **preWorkflowCliOuputs**  list / elements=dictionary | Pnp Device’s preWorkflowCliOuputs. |
| **cli**  string | Pnp Device’s cli. |
| **cliOutput**  string | Pnp Device’s cliOutput. |
| **projectId**  string | Pnp Device’s projectId. |
| **projectName**  string | Pnp Device’s projectName. |
| **reloadRequested**  boolean | ReloadRequested flag.  **Choices:**   - `false` - `true` |
| **serialNumber**  string | Pnp Device’s serialNumber. |
| **smartAccountId**  string | Pnp Device’s smartAccountId. |
| **source**  string | Pnp Device’s source. |
| **stack**  boolean | Stack flag.  **Choices:**   - `false` - `true` |
| **stackInfo**  dictionary | Pnp Device’s stackInfo. |
| **isFullRing**  boolean | IsFullRing flag.  **Choices:**   - `false` - `true` |
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
| **supportsStackWorkflows**  boolean | SupportsStackWorkflows flag.  **Choices:**   - `false` - `true` |
| **totalMemberCount**  integer | Pnp Device’s totalMemberCount. |
| **validLicenseLevels**  list / elements=string | Pnp Device’s validLicenseLevels. |
| **state**  string | Pnp Device’s state. |
| **sudiRequired**  boolean | SudiRequired flag.  **Choices:**   - `false` - `true` |
| **tags**  dictionary | Pnp Device’s tags. |
| **userSudiSerialNos**  list / elements=string | Pnp Device’s userSudiSerialNos. |
| **virtualAccountId**  string | Pnp Device’s virtualAccountId. |
| **workflowId**  string | Pnp Device’s workflowId. |
| **workflowName**  string | Pnp Device’s workflowName. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **id**  string | Id path parameter. |
| **runSummaryList**  list / elements=dictionary | Pnp Device’s runSummaryList. |
| **details**  string | Pnp Device’s details. |
| **errorFlag**  boolean | ErrorFlag flag.  **Choices:**   - `false` - `true` |
| **historyTaskInfo**  dictionary | Pnp Device’s historyTaskInfo. |
| **addnDetails**  list / elements=dictionary | Pnp Device’s addnDetails. |
| **key**  string | Pnp Device’s key. |
| **value**  string | Pnp Device’s value. |
| **name**  string | Pnp Device’s name. |
| **timeTaken**  integer | Pnp Device’s timeTaken. |
| **type**  string | Pnp Device’s type. |
| **workItemList**  list / elements=dictionary | Pnp Device’s workItemList. |
| **command**  string | Pnp Device’s command. |
| **endTime**  integer | Pnp Device’s endTime. |
| **outputStr**  string | Pnp Device’s outputStr. |
| **startTime**  integer | Pnp Device’s startTime. |
| **state**  string | Pnp Device’s state. |
| **timeTaken**  integer | Pnp Device’s timeTaken. |
| **timestamp**  integer | Pnp Device’s timestamp. |
| **systemResetWorkflow**  dictionary | Pnp Device’s systemResetWorkflow. |
| **_id**  string | Pnp Device’s _id. |
| **addedOn**  integer | Pnp Device’s addedOn. |
| **addToInventory**  boolean | AddToInventory flag.  **Choices:**   - `false` - `true` |
| **configId**  string | Pnp Device’s configId. |
| **currTaskIdx**  integer | Pnp Device’s currTaskIdx. |
| **description**  string | Pnp Device’s description. |
| **endTime**  integer | Pnp Device’s endTime. |
| **execTime**  integer | Pnp Device’s execTime. |
| **imageId**  string | Pnp Device’s imageId. |
| **instanceType**  string | Pnp Device’s instanceType. |
| **lastupdateOn**  integer | Pnp Device’s lastupdateOn. |
| **name**  string | Pnp Device’s name. |
| **startTime**  integer | Pnp Device’s startTime. |
| **state**  string | Pnp Device’s state. |
| **tasks**  list / elements=dictionary | Pnp Device’s tasks. |
| **currWorkItemIdx**  integer | Pnp Device’s currWorkItemIdx. |
| **endTime**  integer | Pnp Device’s endTime. |
| **name**  string | Pnp Device’s name. |
| **startTime**  integer | Pnp Device’s startTime. |
| **state**  string | Pnp Device’s state. |
| **taskSeqNo**  integer | Pnp Device’s taskSeqNo. |
| **timeTaken**  integer | Pnp Device’s timeTaken. |
| **type**  string | Pnp Device’s type. |
| **workItemList**  list / elements=dictionary | Pnp Device’s workItemList. |
| **command**  string | Pnp Device’s command. |
| **endTime**  integer | Pnp Device’s endTime. |
| **outputStr**  string | Pnp Device’s outputStr. |
| **startTime**  integer | Pnp Device’s startTime. |
| **state**  string | Pnp Device’s state. |
| **timeTaken**  integer | Pnp Device’s timeTaken. |
| **tenantId**  string | Pnp Device’s tenantId. |
| **type**  string | Pnp Device’s type. |
| **useState**  string | Pnp Device’s useState. |
| **version**  integer | Pnp Device’s version. |
| **systemWorkflow**  dictionary | Pnp Device’s systemWorkflow. |
| **_id**  string | Pnp Device’s _id. |
| **addedOn**  integer | Pnp Device’s addedOn. |
| **addToInventory**  boolean | AddToInventory flag.  **Choices:**   - `false` - `true` |
| **configId**  string | Pnp Device’s configId. |
| **currTaskIdx**  integer | Pnp Device’s currTaskIdx. |
| **description**  string | Pnp Device’s description. |
| **endTime**  integer | Pnp Device’s endTime. |
| **execTime**  integer | Pnp Device’s execTime. |
| **imageId**  string | Pnp Device’s imageId. |
| **instanceType**  string | Pnp Device’s instanceType. |
| **lastupdateOn**  integer | Pnp Device’s lastupdateOn. |
| **name**  string | Pnp Device’s name. |
| **startTime**  integer | Pnp Device’s startTime. |
| **state**  string | Pnp Device’s state. |
| **tasks**  list / elements=dictionary | Pnp Device’s tasks. |
| **currWorkItemIdx**  integer | Pnp Device’s currWorkItemIdx. |
| **endTime**  integer | Pnp Device’s endTime. |
| **name**  string | Pnp Device’s name. |
| **startTime**  integer | Pnp Device’s startTime. |
| **state**  string | Pnp Device’s state. |
| **taskSeqNo**  integer | Pnp Device’s taskSeqNo. |
| **timeTaken**  integer | Pnp Device’s timeTaken. |
| **type**  string | Pnp Device’s type. |
| **workItemList**  list / elements=dictionary | Pnp Device’s workItemList. |
| **command**  string | Pnp Device’s command. |
| **endTime**  integer | Pnp Device’s endTime. |
| **outputStr**  string | Pnp Device’s outputStr. |
| **startTime**  integer | Pnp Device’s startTime. |
| **state**  string | Pnp Device’s state. |
| **timeTaken**  integer | Pnp Device’s timeTaken. |
| **tenantId**  string | Pnp Device’s tenantId. |
| **type**  string | Pnp Device’s type. |
| **useState**  string | Pnp Device’s useState. |
| **version**  integer | Pnp Device’s version. |
| **tenantId**  string | Pnp Device’s tenantId. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |
| **version**  integer | Pnp Device’s version. |
| **workflow**  dictionary | Pnp Device’s workflow. |
| **_id**  string | Pnp Device’s _id. |
| **addedOn**  integer | Pnp Device’s addedOn. |
| **addToInventory**  boolean | AddToInventory flag.  **Choices:**   - `false` - `true` |
| **configId**  string | Pnp Device’s configId. |
| **currTaskIdx**  integer | Pnp Device’s currTaskIdx. |
| **description**  string | Pnp Device’s description. |
| **endTime**  integer | Pnp Device’s endTime. |
| **execTime**  integer | Pnp Device’s execTime. |
| **imageId**  string | Pnp Device’s imageId. |
| **instanceType**  string | Pnp Device’s instanceType. |
| **lastupdateOn**  integer | Pnp Device’s lastupdateOn. |
| **name**  string | Pnp Device’s name. |
| **startTime**  integer | Pnp Device’s startTime. |
| **state**  string | Pnp Device’s state. |
| **tasks**  list / elements=dictionary | Pnp Device’s tasks. |
| **currWorkItemIdx**  integer | Pnp Device’s currWorkItemIdx. |
| **endTime**  integer | Pnp Device’s endTime. |
| **name**  string | Pnp Device’s name. |
| **startTime**  integer | Pnp Device’s startTime. |
| **state**  string | Pnp Device’s state. |
| **taskSeqNo**  integer | Pnp Device’s taskSeqNo. |
| **timeTaken**  integer | Pnp Device’s timeTaken. |
| **type**  string | Pnp Device’s type. |
| **workItemList**  list / elements=dictionary | Pnp Device’s workItemList. |
| **command**  string | Pnp Device’s command. |
| **endTime**  integer | Pnp Device’s endTime. |
| **outputStr**  string | Pnp Device’s outputStr. |
| **startTime**  integer | Pnp Device’s startTime. |
| **state**  string | Pnp Device’s state. |
| **timeTaken**  integer | Pnp Device’s timeTaken. |
| **tenantId**  string | Pnp Device’s tenantId. |
| **type**  string | Pnp Device’s type. |
| **useState**  string | Pnp Device’s useState. |
| **version**  integer | Pnp Device’s version. |
| **workflowParameters**  dictionary | Pnp Device’s workflowParameters. |
| **configList**  list / elements=dictionary | Pnp Device’s configList. |
| **configId**  string | Pnp Device’s configId. |
| **configParameters**  list / elements=dictionary | Pnp Device’s configParameters. |
| **key**  string | Pnp Device’s key. |
| **value**  string | Pnp Device’s value. |
| **licenseLevel**  string | Pnp Device’s licenseLevel. |
| **licenseType**  string | Pnp Device’s licenseType. |
| **topOfStackSerialNumber**  string | Pnp Device’s topOfStackSerialNumber. |

## [Notes](pnp_device_module.md#id5)

> **Note:**
>
> - SDK Method used are device_onboarding_pnp.DeviceOnboardingPnp.add_device, device_onboarding_pnp.DeviceOnboardingPnp.delete_device_by_id_from_pnp, device_onboarding_pnp.DeviceOnboardingPnp.update_device,
> - Paths used are post /dna/intent/api/v1/onboarding/pnp-device, delete /dna/intent/api/v1/onboarding/pnp-device/{id}, put /dna/intent/api/v1/onboarding/pnp-device/{id},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](pnp_device_module.md#id6)

> **See also:**
>
> [Cisco DNA Center documentation for Device Onboarding (PnP) AddDevice](https://developer.cisco.com/docs/dna-center/#!add-device-2)
> :   Complete reference of the AddDevice API.
>
> [Cisco DNA Center documentation for Device Onboarding (PnP) DeleteDeviceByIdFromPnP](https://developer.cisco.com/docs/dna-center/#!delete-device-by-id-from-pn-p)
> :   Complete reference of the DeleteDeviceByIdFromPnP API.
>
> [Cisco DNA Center documentation for Device Onboarding (PnP) UpdateDevice](https://developer.cisco.com/docs/dna-center/#!update-device)
> :   Complete reference of the UpdateDevice API.

## [Examples](pnp_device_module.md#id7)

```yaml+jinja
- name: Create
  cisco.dnac.pnp_device:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    _id: string
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

- name: Update by id
  cisco.dnac.pnp_device:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    _id: string
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
    id: string
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

- name: Delete by id
  cisco.dnac.pnp_device:
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

## [Return Values](pnp_device_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"_id": "string", "dayZeroConfig": {"config": "string"}, "dayZeroConfigPreview": {}, "deviceInfo": {"aaaCredentials": {"password": "string", "username": "string"}, "addedOn": 0, "addnMacAddrs": ["string"], "agentType": "string", "authStatus": "string", "authenticatedMicNumber": "string", "authenticatedSudiSerialNo": "string", "capabilitiesSupported": ["string"], "cmState": "string", "description": "string", "deviceSudiSerialNos": ["string"], "deviceType": "string", "featuresSupported": ["string"], "fileSystemList": [{"freespace": 0, "name": "string", "readable": true, "size": 0, "type": "string", "writeable": true}], "firstContact": 0, "hostname": "string", "httpHeaders": [{"key": "string", "value": "string"}], "imageFile": "string", "imageVersion": "string", "ipInterfaces": [{"ipv4Address": {}, "ipv6AddressList": [{}], "macAddress": "string", "name": "string", "status": "string"}], "lastContact": 0, "lastSyncTime": 0, "lastUpdateOn": 0, "location": {"address": "string", "altitude": "string", "latitude": "string", "longitude": "string", "siteId": "string"}, "macAddress": "string", "mode": "string", "name": "string", "neighborLinks": [{"localInterfaceName": "string", "localMacAddress": "string", "localShortInterfaceName": "string", "remoteDeviceName": "string", "remoteInterfaceName": "string", "remoteMacAddress": "string", "remotePlatform": "string", "remoteShortInterfaceName": "string", "remoteVersion": "string"}], "onbState": "string", "pid": "string", "pnpProfileList": [{"createdBy": "string", "discoveryCreated": true, "primaryEndpoint": {"certificate": "string", "fqdn": "string", "ipv4Address": {}, "ipv6Address": {}, "port": 0, "protocol": "string"}, "profileName": "string", "secondaryEndpoint": {"certificate": "string", "fqdn": "string", "ipv4Address": {}, "ipv6Address": {}, "port": 0, "protocol": "string"}}], "populateInventory": true, "preWorkflowCliOuputs": [{"cli": "string", "cliOutput": "string"}], "projectId": "string", "projectName": "string", "reloadRequested": true, "serialNumber": "string", "siteId": "string", "siteName": "string", "smartAccountId": "string", "source": "string", "stack": true, "stackInfo": {"isFullRing": true, "stackMemberList": [{"hardwareVersion": "string", "licenseLevel": "string", "licenseType": "string", "macAddress": "string", "pid": "string", "priority": 0, "role": "string", "serialNumber": "string", "softwareVersion": "string", "stackNumber": 0, "state": "string", "sudiSerialNumber": "string"}], "stackRingProtocol": "string", "supportsStackWorkflows": true, "totalMemberCount": 0, "validLicenseLevels": ["string"]}, "state": "string", "sudiRequired": true, "tags": {}, "userMicNumbers": ["string"], "userSudiSerialNos": ["string"], "virtualAccountId": "string", "workflowId": "string", "workflowName": "string"}, "runSummaryList": [{"details": "string", "errorFlag": true, "historyTaskInfo": {"addnDetails": [{"key": "string", "value": "string"}], "name": "string", "timeTaken": 0, "type": "string", "workItemList": [{"command": "string", "endTime": 0, "outputStr": "string", "startTime": 0, "state": "string", "timeTaken": 0}]}, "timestamp": 0}], "systemResetWorkflow": {"_id": "string", "addToInventory": true, "addedOn": 0, "configId": "string", "currTaskIdx": 0, "description": "string", "endTime": 0, "execTime": 0, "imageId": "string", "instanceType": "string", "lastupdateOn": 0, "name": "string", "startTime": 0, "state": "string", "tasks": [{"currWorkItemIdx": 0, "endTime": 0, "name": "string", "startTime": 0, "state": "string", "taskSeqNo": 0, "timeTaken": 0, "type": "string", "workItemList": [{"command": "string", "endTime": 0, "outputStr": "string", "startTime": 0, "state": "string", "timeTaken": 0}]}], "tenantId": "string", "type": "string", "useState": "string", "version": 0}, "systemWorkflow": {"_id": "string", "addToInventory": true, "addedOn": 0, "configId": "string", "currTaskIdx": 0, "description": "string", "endTime": 0, "execTime": 0, "imageId": "string", "instanceType": "string", "lastupdateOn": 0, "name": "string", "startTime": 0, "state": "string", "tasks": [{"currWorkItemIdx": 0, "endTime": 0, "name": "string", "startTime": 0, "state": "string", "taskSeqNo": 0, "timeTaken": 0, "type": "string", "workItemList": [{"command": "string", "endTime": 0, "outputStr": "string", "startTime": 0, "state": "string", "timeTaken": 0}]}], "tenantId": "string", "type": "string", "useState": "string", "version": 0}, "tenantId": "string", "version": 0, "workflow": {"_id": "string", "addToInventory": true, "addedOn": 0, "configId": "string", "currTaskIdx": 0, "description": "string", "endTime": 0, "execTime": 0, "imageId": "string", "instanceType": "string", "lastupdateOn": 0, "name": "string", "startTime": 0, "state": "string", "tasks": [{"currWorkItemIdx": 0, "endTime": 0, "name": "string", "startTime": 0, "state": "string", "taskSeqNo": 0, "timeTaken": 0, "type": "string", "workItemList": [{"command": "string", "endTime": 0, "outputStr": "string", "startTime": 0, "state": "string", "timeTaken": 0}]}], "tenantId": "string", "type": "string", "useState": "string", "version": 0}, "workflowParameters": {"configList": [{"configId": "string", "configParameters": [{"key": "string", "value": "string"}]}], "licenseLevel": "string", "licenseType": "string", "topOfStackSerialNumber": "string"}}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
