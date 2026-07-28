---
collection: ansible
version: "6"
title: "netapp_eseries.santricity.netapp_e_amg_sync module – NetApp E-Series conduct synchronization actions on asynchronous mirror groups."
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp_eseries/santricity/netapp_e_amg_sync_module.html
fetched_at: 2026-07-28T00:14:12+00:00
---
# netapp_eseries.santricity.netapp_e_amg_sync module – NetApp E-Series conduct synchronization actions on asynchronous mirror groups.

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
> To use it in a playbook, specify: `netapp_eseries.santricity.netapp_e_amg_sync`.

New in netapp_eseries.santricity 2.2

- [Synopsis](netapp_e_amg_sync_module.md#synopsis)
- [Parameters](netapp_e_amg_sync_module.md#parameters)
- [Examples](netapp_e_amg_sync_module.md#examples)
- [Return Values](netapp_e_amg_sync_module.md#return-values)

## [Synopsis](netapp_e_amg_sync_module.md#id1)

- Allows for the initialization, suspension and resumption of an asynchronous mirror group’s synchronization for NetApp E-series storage arrays.

## [Parameters](netapp_e_amg_sync_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_password**  string / required | The password to authenticate with the SANtricity WebServices Proxy or embedded REST API. |
| **api_url**  string / required | The url to the SANtricity WebServices Proxy or embedded REST API. |
| **api_username**  string / required | The username to authenticate with the SANtricity WebServices Proxy or embedded REST API. |
| **delete_recovery_point**  boolean | Indicates whether the failures point can be deleted on the secondary if necessary to achieve the synchronization.  If true, and if the amount of unsynchronized data exceeds the CoW repository capacity on the secondary for any member volume, the last failures point will be deleted and synchronization will continue.  If false, the synchronization will be suspended if the amount of unsynchronized data exceeds the CoW Repository capacity on the secondary and the failures point will be preserved.  NOTE: This only has impact for newly launched syncs.  Choices:   - `false` ← (default) - `true` |
| **name**  string / required | The name of the async mirror group you wish to target |
| **ssid**  string | The ID of the storage array containing the AMG you wish to target |
| **state**  string / required | The synchronization action you’d like to take.  If `running` then it will begin syncing if there is no active sync or will resume a suspended sync. If there is already a sync in progress, it will return with an OK status.  If `suspended` it will suspend any ongoing sync action, but return OK if there is no active sync or if the sync is already suspended  Choices:   - `"running"` - `"suspended"` |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |

## [Examples](netapp_e_amg_sync_module.md#id3)

```yaml+jinja
- name: start AMG async
  netapp_e_amg_sync:
    name: "{{ amg_sync_name }}"
    state: running
    ssid: "{{ ssid }}"
    api_url: "{{ netapp_api_url }}"
    api_username: "{{ netapp_api_username }}"
    api_password: "{{ netapp_api_password }}"
```

## [Return Values](netapp_e_amg_sync_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **json**  string | The object attributes of the AMG.  Returned: success  Sample: `"{'changed': False, 'connectionType': 'fc', 'groupRef': '3700000060080E5000299C24000006EF57ACAC70', 'groupState': 'optimal', 'id': '3700000060080E5000299C24000006EF57ACAC70', 'label': 'made_with_ansible', 'localRole': 'primary', 'mirrorChannelRemoteTarget': '9000000060080E5000299C24005B06E557AC7EEC', 'orphanGroup': False, 'recoveryPointAgeAlertThresholdMinutes': 20, 'remoteRole': 'secondary', 'remoteTarget': {'nodeName': {'ioInterfaceType': 'fc', 'iscsiNodeName': None, 'remoteNodeWWN': '20040080E5299F1C'}, 'remoteRef': '9000000060080E5000299C24005B06E557AC7EEC', 'scsiinitiatorTargetBaseProperties': {'ioInterfaceType': 'fc', 'iscsiinitiatorTargetBaseParameters': None}}, 'remoteTargetId': 'ansible2', 'remoteTargetName': 'Ansible2', 'remoteTargetWwn': '60080E5000299F880000000056A25D56', 'repositoryUtilizationWarnThreshold': 80, 'roleChangeProgress': 'none', 'syncActivity': 'idle', 'syncCompletionTimeAlertThresholdMinutes': 10, 'syncIntervalMinutes': 10, 'worldWideName': '60080E5000299C24000006EF57ACAC70'}"` |

### Authors

- Kevin Hulquest (@hulquest)

### Collection links

[Issue Tracker](https://github.com/netappeseries/santricity/issues)
[Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
