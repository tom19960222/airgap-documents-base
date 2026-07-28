---
collection: ansible
version: "8"
title: "netapp_eseries.santricity.netapp_e_volume_copy module – NetApp E-Series create volume copy pairs"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp_eseries/santricity/netapp_e_volume_copy_module.html
fetched_at: 2026-07-28T02:44:41+00:00
---
# netapp_eseries.santricity.netapp_e_volume_copy module – NetApp E-Series create volume copy pairs

> **Note:**
>
> This module is part of the [netapp_eseries.santricity collection](https://galaxy.ansible.com/ui/repo/published/netapp_eseries/santricity/) (version 1.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp_eseries.santricity`.
>
> To use it in a playbook, specify: `netapp_eseries.santricity.netapp_e_volume_copy`.

New in netapp_eseries.santricity 2.2

- [Synopsis](netapp_e_volume_copy_module.md#synopsis)
- [Parameters](netapp_e_volume_copy_module.md#parameters)
- [Notes](netapp_e_volume_copy_module.md#notes)
- [Examples](netapp_e_volume_copy_module.md#examples)
- [Return Values](netapp_e_volume_copy_module.md#return-values)

## [Synopsis](netapp_e_volume_copy_module.md#id1)

- Create and delete snapshots images on volume groups for NetApp E-series storage arrays.

## [Parameters](netapp_e_volume_copy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_password**  string / required | The password to authenticate with the SANtricity WebServices Proxy or embedded REST API. |
| **api_url**  string / required | The url to the SANtricity WebServices Proxy or embedded REST API, for example `https://prod-1.wahoo.acme.com/devmgr/v2`. |
| **api_username**  string / required | The username to authenticate with the SANtricity WebServices Proxy or embedded REST API. |
| **copy_priority**  integer | Copy priority level  **Default:** `0` |
| **create_copy_pair_if_does_not_exist**  boolean | Defines if a copy pair will be created if it does not exist.  If set to True destination_volume_id and source_volume_id are required.  **Choices:**   - `false` - `true` ← (default) |
| **destination_volume_id**  string | The id of the volume copy destination.  If used, must be paired with source_volume_id  Mutually exclusive with volume_copy_pair_id, and search_volume_id |
| **onlineCopy**  boolean | Whether copy should be online  **Choices:**   - `false` ← (default) - `true` |
| **search_volume_id**  string | Searches for all valid potential target and source volumes that could be used in a copy_pair  Mutually exclusive with volume_copy_pair_id, destination_volume_id and source_volume_id |
| **source_volume_id**  string | The id of the volume copy source.  If used, must be paired with destination_volume_id  Mutually exclusive with volume_copy_pair_id, and search_volume_id |
| **ssid**  string | Storage system identifier  **Default:** `"1"` |
| **start_stop_copy**  string | starts a re-copy or stops a copy in progress  Note: If you stop the initial file copy before it it done the copy pair will be destroyed  Requires volume_copy_pair_id  **Choices:**   - `"start"` - `"stop"` |
| **state**  string / required | Whether the specified volume copy pair should exist or not.  **Choices:**   - `"present"` - `"absent"` |
| **targetWriteProtected**  boolean | Whether target should be write protected  **Choices:**   - `false` - `true` ← (default) |
| **validate_certs**  boolean | Should https certificates be validated?  **Choices:**   - `false` - `true` ← (default) |
| **volume_copy_pair_id**  string | The id of a given volume copy pair  Mutually exclusive with destination_volume_id, source_volume_id, and search_volume_id  Can use to delete or check presence of volume pairs  Must specify this or (destination_volume_id and source_volume_id) |

## [Notes](netapp_e_volume_copy_module.md#id3)

> **Note:**
>
> - The E-Series Ansible modules require either an instance of the Web Services Proxy (WSP), to be available to manage the storage-system, or an E-Series storage-system that supports the Embedded Web Services API.
> - Embedded Web Services is currently available on the E2800, E5700, EF570, and newer hardware models.
> - **ERROR while parsing**: While parsing “M(netapp_e_storage_system)” at index 1: Module name “netapp_e_storage_system” is not a FQCN may be utilized for configuring the systems managed by a WSP instance.

## [Examples](netapp_e_volume_copy_module.md#id4)

```yaml+jinja
---
msg:
    description: Success message
    returned: success
    type: str
    sample: Json facts for the volume copy that was created.
```

## [Return Values](netapp_e_volume_copy_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Success message  **Returned:** success  **Sample:** `"Created Volume Copy Pair with ID"` |

### Authors

- Kevin Hulquest (@hulquest)

### Collection links

- [Issue Tracker](https://github.com/netappeseries/santricity/issues)
- [Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
