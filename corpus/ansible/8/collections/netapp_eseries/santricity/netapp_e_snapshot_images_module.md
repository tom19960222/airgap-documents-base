---
collection: ansible
version: "8"
title: "netapp_eseries.santricity.netapp_e_snapshot_images module – NetApp E-Series create and delete snapshot images"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp_eseries/santricity/netapp_e_snapshot_images_module.html
fetched_at: 2026-07-28T02:44:37+00:00
---
# netapp_eseries.santricity.netapp_e_snapshot_images module – NetApp E-Series create and delete snapshot images

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
> To use it in a playbook, specify: `netapp_eseries.santricity.netapp_e_snapshot_images`.

New in netapp_eseries.santricity 2.2

- [Synopsis](netapp_e_snapshot_images_module.md#synopsis)
- [Parameters](netapp_e_snapshot_images_module.md#parameters)
- [Examples](netapp_e_snapshot_images_module.md#examples)
- [Return Values](netapp_e_snapshot_images_module.md#return-values)

## [Synopsis](netapp_e_snapshot_images_module.md#id1)

- Create and delete snapshots images on snapshot groups for NetApp E-series storage arrays.
- Only the oldest snapshot image can be deleted so consistency is preserved.
- Related: Snapshot volumes are created from snapshot images.

## [Parameters](netapp_e_snapshot_images_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_password**  string / required | The password to authenticate with the SANtricity WebServices Proxy or embedded REST API. |
| **api_url**  string / required | The url to the SANtricity WebServices Proxy or embedded REST API. |
| **api_username**  string / required | The username to authenticate with the SANtricity WebServices Proxy or embedded REST API. |
| **snapshot_group**  string / required | The name of the snapshot group in which you want to create a snapshot image. |
| **ssid**  string | Storage system identifier |
| **state**  string / required | Whether a new snapshot image should be created or oldest be deleted.  **Choices:**   - `"create"` - `"remove"` |
| **validate_certs**  boolean | Should https certificates be validated?  **Choices:**   - `false` - `true` ← (default) |

## [Examples](netapp_e_snapshot_images_module.md#id3)

```yaml+jinja
- name: Create Snapshot
  netapp_e_snapshot_images:
    ssid: "{{ ssid }}"
    api_url: "{{ netapp_api_url }}"
    api_username: "{{ netapp_api_username }}"
    api_password: "{{ netapp_api_password }}"
    validate_certs: "{{ validate_certs }}"
    snapshot_group: "3300000060080E5000299C24000005B656D9F394"
    state: 'create'
```

## [Return Values](netapp_e_snapshot_images_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **image_id**  string | ID of snapshot image  **Returned:** state == created  **Sample:** `"3400000060080E5000299B640063074057BC5C5E "` |
| **msg**  string | State of operation  **Returned:** always  **Sample:** `"Created snapshot image"` |

### Authors

- Kevin Hulquest (@hulquest)

### Collection links

- [Issue Tracker](https://github.com/netappeseries/santricity/issues)
- [Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
