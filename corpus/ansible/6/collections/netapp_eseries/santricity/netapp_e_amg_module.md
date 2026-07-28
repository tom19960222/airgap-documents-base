---
collection: ansible
version: "6"
title: "netapp_eseries.santricity.netapp_e_amg module – NetApp E-Series create, remove, and update asynchronous mirror groups"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp_eseries/santricity/netapp_e_amg_module.html
fetched_at: 2026-07-28T00:14:11+00:00
---
# netapp_eseries.santricity.netapp_e_amg module – NetApp E-Series create, remove, and update asynchronous mirror groups

> **Note:**
>
> This module is part of the [netapp_eseries.santricity collection](https://galaxy.ansible.com/netapp_eseries/santricity) (version 1.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp_eseries.santricity`.
>
> To use it in a playbook, specify: `netapp_eseries.santricity.netapp_e_amg`.

New in netapp_eseries.santricity 2.2

- [Synopsis](netapp_e_amg_module.md#synopsis)
- [Parameters](netapp_e_amg_module.md#parameters)
- [Notes](netapp_e_amg_module.md#notes)
- [Examples](netapp_e_amg_module.md#examples)
- [Return Values](netapp_e_amg_module.md#return-values)

## [Synopsis](netapp_e_amg_module.md#id1)

- Allows for the creation, removal and updating of Asynchronous Mirror Groups for NetApp E-series storage arrays

## [Parameters](netapp_e_amg_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_password**  string / required | The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the SANtricity Web Services Proxy or Embedded Web Services API. Example <https://prod-1.wahoo.acme.com/devmgr/v2> |
| **api_username**  string / required | The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **interfaceType**  string | The intended protocol to use if both Fibre and iSCSI are available.  Choices:   - `"iscsi"` - `"fibre"` |
| **manualSync**  boolean | Setting this to true will cause other synchronization values to be ignored  Choices:   - `false` ← (default) - `true` |
| **name**  string / required | The name of the async array you wish to target, or create.  If `state` is present and the name isn’t found, it will attempt to create. |
| **new_name**  string | New async array name |
| **recoveryWarnThresholdMinutes**  integer | Recovery point warning threshold (minutes). The user will be warned when the age of the last good failures point exceeds this value  Default: `20` |
| **repoUtilizationWarnThreshold**  integer | Recovery point warning threshold  Default: `80` |
| **secondaryArrayId**  string / required | The ID of the secondary array to be used in mirroring process |
| **ssid**  string | The ID of the array to manage. This value must be unique for each array.  Default: `"1"` |
| **state**  string / required | A `state` of present will either create or update the async mirror group.  A `state` of absent will remove the async mirror group.  Choices:   - `"absent"` - `"present"` |
| **syncIntervalMinutes**  integer | The synchronization interval in minutes  Default: `10` |
| **syncWarnThresholdMinutes**  integer | The threshold (in minutes) for notifying the user that periodic synchronization has taken too long to complete.  Default: `10` |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |

## [Notes](netapp_e_amg_module.md#id3)

> **Note:**
>
> - The E-Series Ansible modules require either an instance of the Web Services Proxy (WSP), to be available to manage the storage-system, or an E-Series storage-system that supports the Embedded Web Services API.
> - Embedded Web Services is currently available on the E2800, E5700, EF570, and newer hardware models.
> - **ERROR while parsing**: While parsing M() at index 1: Module name “netapp_e_storage_system” is not a FQCN may be utilized for configuring the systems managed by a WSP instance.

## [Examples](netapp_e_amg_module.md#id4)

```yaml+jinja
- name: AMG removal
  na_eseries_amg:
    state: absent
    ssid: "{{ ssid }}"
    secondaryArrayId: "{{amg_secondaryArrayId}}"
    api_url: "{{ netapp_api_url }}"
    api_username: "{{ netapp_api_username }}"
    api_password: "{{ netapp_api_password }}"
    new_name: "{{amg_array_name}}"
    name: "{{amg_name}}"
  when: amg_create

- name: AMG create
  netapp_e_amg:
    state: present
    ssid: "{{ ssid }}"
    secondaryArrayId: "{{amg_secondaryArrayId}}"
    api_url: "{{ netapp_api_url }}"
    api_username: "{{ netapp_api_username }}"
    api_password: "{{ netapp_api_password }}"
    new_name: "{{amg_array_name}}"
    name: "{{amg_name}}"
  when: amg_create
```

## [Return Values](netapp_e_amg_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Successful creation  Returned: success  Sample: `"{\"changed\": true, \"connectionType\": \"fc\", \"groupRef\": \"3700000060080E5000299C24000006E857AC7EEC\", \"groupState\": \"optimal\", \"id\": \"3700000060080E5000299C24000006E857AC7EEC\", \"label\": \"amg_made_by_ansible\", \"localRole\": \"primary\", \"mirrorChannelRemoteTarget\": \"9000000060080E5000299C24005B06E557AC7EEC\", \"orphanGroup\": false, \"recoveryPointAgeAlertThresholdMinutes\": 20, \"remoteRole\": \"secondary\", \"remoteTarget\": {\"nodeName\": {\"ioInterfaceType\": \"fc\", \"iscsiNodeName\": null, \"remoteNodeWWN\": \"20040080E5299F1C\"}, \"remoteRef\": \"9000000060080E5000299C24005B06E557AC7EEC\", \"scsiinitiatorTargetBaseProperties\": {\"ioInterfaceType\": \"fc\", \"iscsiinitiatorTargetBaseParameters\": null}}, \"remoteTargetId\": \"ansible2\", \"remoteTargetName\": \"Ansible2\", \"remoteTargetWwn\": \"60080E5000299F880000000056A25D56\", \"repositoryUtilizationWarnThreshold\": 80, \"roleChangeProgress\": \"none\", \"syncActivity\": \"idle\", \"syncCompletionTimeAlertThresholdMinutes\": 10, \"syncIntervalMinutes\": 10, \"worldWideName\": \"60080E5000299C24000006E857AC7EEC\"}"` |

### Authors

- Kevin Hulquest (@hulquest)

### Collection links

[Issue Tracker](https://github.com/netappeseries/santricity/issues)
[Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
