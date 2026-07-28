---
collection: ansible
version: "8"
title: "vmware.vmware_rest.content_library_item_info module – Returns the { @ link ItemModel} with the given identifier."
source_url: https://docs.ansible.com/projects/ansible/8/collections/vmware/vmware_rest/content_library_item_info_module.html
fetched_at: 2026-07-28T02:57:44+00:00
---
# vmware.vmware_rest.content_library_item_info module – Returns the [{@link](mailto:{%40link) ItemModel} with the given identifier.

> **Note:**
>
> This module is part of the [vmware.vmware_rest collection](https://galaxy.ansible.com/ui/repo/published/vmware/vmware_rest/) (version 2.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vmware.vmware_rest`.
> You need further requirements to be able to use this module,
> see [Requirements](content_library_item_info_module.md#ansible-collections-vmware-vmware-rest-content-library-item-info-module-requirements) for details.
>
> To use it in a playbook, specify: `vmware.vmware_rest.content_library_item_info`.

New in vmware.vmware_rest 2.0.0

- [Synopsis](content_library_item_info_module.md#synopsis)
- [Requirements](content_library_item_info_module.md#requirements)
- [Parameters](content_library_item_info_module.md#parameters)
- [Notes](content_library_item_info_module.md#notes)
- [Examples](content_library_item_info_module.md#examples)
- [Return Values](content_library_item_info_module.md#return-values)

## [Synopsis](content_library_item_info_module.md#id1)

- Returns the [{@link](mailto:{%40link) ItemModel} with the given identifier.

## [Requirements](content_library_item_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp

## [Parameters](content_library_item_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **library_id**  string | Identifier of the library whose items should be returned. Required with *state=[‘list’]* |
| **library_item_id**  string | Identifier of the library item to return. Required with *state=[‘get’]* |
| **session_timeout**  float  *added in vmware.vmware_rest 2.1.0* | Timeout settings for client session.  The maximal number of seconds for the whole operation including connection establishment, request sending and response.  The default value is 300s. |
| **vcenter_hostname**  string / required | The hostname or IP address of the vSphere vCenter  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **vcenter_password**  string / required | The vSphere vCenter password  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **vcenter_rest_log_file**  string | You can use this optional parameter to set the location of a log file.  This file will be used to record the HTTP REST interaction.  The file will be stored on the host that run the module.  If the value is not specified in the task, the value of  environment variable `VMWARE_REST_LOG_FILE` will be used instead. |
| **vcenter_username**  string / required | The vSphere vCenter username  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **vcenter_validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](content_library_item_info_module.md#id4)

> **Note:**
>
> - Tested on vSphere 7.0.2

## [Examples](content_library_item_info_module.md#id5)

```yaml+jinja
- name: Create a content library pointing on a NFS share
  vmware.vmware_rest.content_locallibrary:
    name: my_library_on_nfs
    description: automated
    publish_info:
      published: true
      authentication_method: NONE
    storage_backings:
    - storage_uri: nfs://datastore.test/srv/share/content-library
      type: OTHER
    state: present
  register: nfs_lib

- name: Get the list of items of the NFS library
  vmware.vmware_rest.content_library_item_info:
    library_id: '{{ nfs_lib.id }}'
  register: lib_items

- name: Get the list of items of the NFS library
  vmware.vmware_rest.content_library_item_info:
    library_id: '{{ nfs_lib.id }}'
  register: result

- name: Create a new local content library
  vmware.vmware_rest.content_locallibrary:
    name: local_library_001
    description: automated
    publish_info:
      published: true
      authentication_method: NONE
    storage_backings:
    - datastore_id: "{{ lookup('vmware.vmware_rest.datastore_moid', '/my_dc/datastore/rw_datastore') }}"
      type: DATASTORE
    state: present
  register: ds_lib

- name: Get the (empty) list of items of the library
  vmware.vmware_rest.content_library_item_info:
    library_id: '{{ ds_lib.id }}'
  register: result

- name: Create subscribed library
  vmware.vmware_rest.content_subscribedlibrary:
    name: sub_lib
    subscription_info:
      subscription_url: '{{ nfs_lib.value.publish_info.publish_url }}'
      authentication_method: NONE
      automatic_sync_enabled: false
      on_demand: true
    storage_backings:
    - datastore_id: "{{ lookup('vmware.vmware_rest.datastore_moid', '/my_dc/datastore/rw_datastore') }}"
      type: DATASTORE
  register: sub_lib

- name: Ensure the OVF is here
  vmware.vmware_rest.content_library_item_info:
    library_id: '{{ sub_lib.id }}'
  register: result

- name: Create a content library based on a DataStore
  vmware.vmware_rest.content_locallibrary:
    name: my_library_on_datastore
    description: automated
    publish_info:
      published: true
      authentication_method: NONE
    storage_backings:
    - datastore_id: "{{ lookup('vmware.vmware_rest.datastore_moid', '/my_dc/datastore/local') }}"
      type: DATASTORE
    state: present
  register: nfs_lib
```

## [Return Values](content_library_item_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **value**  list / elements=string | Ensure the OVF is here  **Returned:** On success  **Sample:** `[{"cached": 0, "content_version": "2", "creation_time": "2022-11-23T20:06:05.707Z", "description": "an OVF example", "id": "f6618d6b-301b-4202-aa9c-12eb0c7536b1", "last_modified_time": "2022-11-23T20:06:06.062Z", "last_sync_time": "2022-11-23T20:06:06.061Z", "library_id": "8b4e355e-a463-44f1-9b04-d0786a49cc7d", "metadata_version": "1", "name": "golden_image", "security_compliance": 1, "size": 0, "source_id": "636ef270-b556-4972-924f-0d21b0f3bfce", "type": "ovf", "version": "1"}]` |

### Authors

- Ansible Cloud Team (@ansible-collections)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vmware.vmware_rest/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/vmware.vmware_rest)
- [Repository (Sources)](https://github.com/ansible-collections/vmware.vmware_rest.git)
