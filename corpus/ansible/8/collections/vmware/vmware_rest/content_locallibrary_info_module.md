---
collection: ansible
version: "8"
title: "vmware.vmware_rest.content_locallibrary_info module – Returns a given local library."
source_url: https://docs.ansible.com/projects/ansible/8/collections/vmware/vmware_rest/content_locallibrary_info_module.html
fetched_at: 2026-07-28T02:57:45+00:00
---
# vmware.vmware_rest.content_locallibrary_info module – Returns a given local library.

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
> see [Requirements](content_locallibrary_info_module.md#ansible-collections-vmware-vmware-rest-content-locallibrary-info-module-requirements) for details.
>
> To use it in a playbook, specify: `vmware.vmware_rest.content_locallibrary_info`.

New in vmware.vmware_rest 2.0.0

- [Synopsis](content_locallibrary_info_module.md#synopsis)
- [Requirements](content_locallibrary_info_module.md#requirements)
- [Parameters](content_locallibrary_info_module.md#parameters)
- [Notes](content_locallibrary_info_module.md#notes)
- [Examples](content_locallibrary_info_module.md#examples)
- [Return Values](content_locallibrary_info_module.md#return-values)

## [Synopsis](content_locallibrary_info_module.md#id1)

- Returns a given local library.

## [Requirements](content_locallibrary_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp

## [Parameters](content_locallibrary_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **library_id**  string | Identifier of the local library to return. Required with *state=[‘get’]* |
| **session_timeout**  float  *added in vmware.vmware_rest 2.1.0* | Timeout settings for client session.  The maximal number of seconds for the whole operation including connection establishment, request sending and response.  The default value is 300s. |
| **vcenter_hostname**  string / required | The hostname or IP address of the vSphere vCenter  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **vcenter_password**  string / required | The vSphere vCenter password  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **vcenter_rest_log_file**  string | You can use this optional parameter to set the location of a log file.  This file will be used to record the HTTP REST interaction.  The file will be stored on the host that run the module.  If the value is not specified in the task, the value of  environment variable `VMWARE_REST_LOG_FILE` will be used instead. |
| **vcenter_username**  string / required | The vSphere vCenter username  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **vcenter_validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](content_locallibrary_info_module.md#id4)

> **Note:**
>
> - Tested on vSphere 7.0.2

## [Examples](content_locallibrary_info_module.md#id5)

```yaml+jinja
- name: List Local Content Library
  vmware.vmware_rest.content_locallibrary_info:
  register: my_content_library

- name: List all Local Content Library
  vmware.vmware_rest.content_locallibrary_info:
  register: all_content_libraries

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

- name: Retrieve the local content library information based upon id check mode
  vmware.vmware_rest.content_locallibrary_info:
    library_id: '{{ ds_lib.id }}'
  register: result
  check_mode: true
```

## [Return Values](content_locallibrary_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **value**  list / elements=string | List all Local Content Library  **Returned:** On success  **Sample:** `[{"creation_time": "2022-11-23T20:02:22.940Z", "description": "automated", "id": "a66d5c73-57f8-4a3a-9361-292a55f68516", "last_modified_time": "2022-11-23T20:02:22.940Z", "name": "my_library_on_nfs", "publish_info": {"authentication_method": "NONE", "persist_json_enabled": 0, "publish_url": "https://vcenter.test:443/cls/vcsp/lib/a66d5c73-57f8-4a3a-9361-292a55f68516/lib.json", "published": 1, "user_name": "vcsp"}, "server_guid": "52fb0b5e-ffc3-465b-bf4f-e4e6d5423cf5", "storage_backings": [{"storage_uri": "nfs://datastore.test/srv/share/content-library", "type": "OTHER"}], "type": "LOCAL", "version": "2"}, {"creation_time": "2022-11-23T20:02:25.134Z", "description": "automated", "id": "3393956a-43ed-4e7f-bd96-eb39bd604445", "last_modified_time": "2022-11-23T20:02:25.134Z", "name": "my_library_on_nfs_0", "publish_info": {"authentication_method": "NONE", "persist_json_enabled": 0, "publish_url": "https://vcenter.test:443/cls/vcsp/lib/3393956a-43ed-4e7f-bd96-eb39bd604445/lib.json", "published": 1, "user_name": "vcsp"}, "server_guid": "52fb0b5e-ffc3-465b-bf4f-e4e6d5423cf5", "storage_backings": [{"storage_uri": "nfs://datastore.test/srv/share/content-library", "type": "OTHER"}], "type": "LOCAL", "version": "2"}, {"creation_time": "2022-11-23T20:02:26.342Z", "description": "automated", "id": "87f66f86-c046-45a7-9563-d59ea220babf", "last_modified_time": "2022-11-23T20:02:26.342Z", "name": "my_library_on_nfs_1", "publish_info": {"authentication_method": "NONE", "persist_json_enabled": 0, "publish_url": "https://vcenter.test:443/cls/vcsp/lib/87f66f86-c046-45a7-9563-d59ea220babf/lib.json", "published": 1, "user_name": "vcsp"}, "server_guid": "52fb0b5e-ffc3-465b-bf4f-e4e6d5423cf5", "storage_backings": [{"storage_uri": "nfs://datastore.test/srv/share/content-library", "type": "OTHER"}], "type": "LOCAL", "version": "2"}, {"creation_time": "2022-11-23T20:02:27.504Z", "description": "automated", "id": "f6c590c4-ae6d-4ad0-9362-378196e98a3c", "last_modified_time": "2022-11-23T20:02:27.504Z", "name": "my_library_on_nfs_2", "publish_info": {"authentication_method": "NONE", "persist_json_enabled": 0, "publish_url": "https://vcenter.test:443/cls/vcsp/lib/f6c590c4-ae6d-4ad0-9362-378196e98a3c/lib.json", "published": 1, "user_name": "vcsp"}, "server_guid": "52fb0b5e-ffc3-465b-bf4f-e4e6d5423cf5", "storage_backings": [{"storage_uri": "nfs://datastore.test/srv/share/content-library", "type": "OTHER"}], "type": "LOCAL", "version": "2"}, {"creation_time": "2022-11-23T20:02:28.821Z", "description": "automated", "id": "e8917499-2a4c-4b70-b39b-ae0caaef89c3", "last_modified_time": "2022-11-23T20:02:28.821Z", "name": "my_library_on_nfs_3", "publish_info": {"authentication_method": "NONE", "persist_json_enabled": 0, "publish_url": "https://vcenter.test:443/cls/vcsp/lib/e8917499-2a4c-4b70-b39b-ae0caaef89c3/lib.json", "published": 1, "user_name": "vcsp"}, "server_guid": "52fb0b5e-ffc3-465b-bf4f-e4e6d5423cf5", "storage_backings": [{"storage_uri": "nfs://datastore.test/srv/share/content-library", "type": "OTHER"}], "type": "LOCAL", "version": "2"}, {"creation_time": "2022-11-23T20:02:30.085Z", "description": "automated", "id": "630ebdfe-8913-45d3-aaa8-9c2fdecbb76b", "last_modified_time": "2022-11-23T20:02:30.085Z", "name": "my_library_on_nfs_4", "publish_info": {"authentication_method": "NONE", "persist_json_enabled": 0, "publish_url": "https://vcenter.test:443/cls/vcsp/lib/630ebdfe-8913-45d3-aaa8-9c2fdecbb76b/lib.json", "published": 1, "user_name": "vcsp"}, "server_guid": "52fb0b5e-ffc3-465b-bf4f-e4e6d5423cf5", "storage_backings": [{"storage_uri": "nfs://datastore.test/srv/share/content-library", "type": "OTHER"}], "type": "LOCAL", "version": "2"}, {"creation_time": "2022-11-23T20:02:31.482Z", "description": "automated", "id": "a046e2e5-bd55-4d04-9443-750a2ab35a6d", "last_modified_time": "2022-11-23T20:02:31.482Z", "name": "my_library_on_nfs_5", "publish_info": {"authentication_method": "NONE", "persist_json_enabled": 0, "publish_url": "https://vcenter.test:443/cls/vcsp/lib/a046e2e5-bd55-4d04-9443-750a2ab35a6d/lib.json", "published": 1, "user_name": "vcsp"}, "server_guid": "52fb0b5e-ffc3-465b-bf4f-e4e6d5423cf5", "storage_backings": [{"storage_uri": "nfs://datastore.test/srv/share/content-library", "type": "OTHER"}], "type": "LOCAL", "version": "2"}, {"creation_time": "2022-11-23T20:02:32.846Z", "description": "automated", "id": "b94383b1-7877-4dbd-8c33-51abc39451ff", "last_modified_time": "2022-11-23T20:02:32.846Z", "name": "my_library_on_nfs_6", "publish_info": {"authentication_method": "NONE", "persist_json_enabled": 0, "publish_url": "https://vcenter.test:443/cls/vcsp/lib/b94383b1-7877-4dbd-8c33-51abc39451ff/lib.json", "published": 1, "user_name": "vcsp"}, "server_guid": "52fb0b5e-ffc3-465b-bf4f-e4e6d5423cf5", "storage_backings": [{"storage_uri": "nfs://datastore.test/srv/share/content-library", "type": "OTHER"}], "type": "LOCAL", "version": "2"}, {"creation_time": "2022-11-23T20:02:34.218Z", "description": "automated", "id": "8e3efb68-cb84-4ce0-a65a-6c94cc6e6e00", "last_modified_time": "2022-11-23T20:02:34.218Z", "name": "my_library_on_nfs_7", "publish_info": {"authentication_method": "NONE", "persist_json_enabled": 0, "publish_url": "https://vcenter.test:443/cls/vcsp/lib/8e3efb68-cb84-4ce0-a65a-6c94cc6e6e00/lib.json", "published": 1, "user_name": "vcsp"}, "server_guid": "52fb0b5e-ffc3-465b-bf4f-e4e6d5423cf5", "storage_backings": [{"storage_uri": "nfs://datastore.test/srv/share/content-library", "type": "OTHER"}], "type": "LOCAL", "version": "2"}, {"creation_time": "2022-11-23T20:02:35.922Z", "description": "automated", "id": "0b12c0b3-6c6d-448d-9033-e054a70183e7", "last_modified_time": "2022-11-23T20:02:35.922Z", "name": "my_library_on_nfs_8", "publish_info": {"authentication_method": "NONE", "persist_json_enabled": 0, "publish_url": "https://vcenter.test:443/cls/vcsp/lib/0b12c0b3-6c6d-448d-9033-e054a70183e7/lib.json", "published": 1, "user_name": "vcsp"}, "server_guid": "52fb0b5e-ffc3-465b-bf4f-e4e6d5423cf5", "storage_backings": [{"storage_uri": "nfs://datastore.test/srv/share/content-library", "type": "OTHER"}], "type": "LOCAL", "version": "2"}, {"creation_time": "2022-11-23T20:02:37.796Z", "description": "automated", "id": "46454797-bbe0-415a-9fe9-3cf2f74a14db", "last_modified_time": "2022-11-23T20:02:37.796Z", "name": "my_library_on_nfs_9", "publish_info": {"authentication_method": "NONE", "persist_json_enabled": 0, "publish_url": "https://vcenter.test:443/cls/vcsp/lib/46454797-bbe0-415a-9fe9-3cf2f74a14db/lib.json", "published": 1, "user_name": "vcsp"}, "server_guid": "52fb0b5e-ffc3-465b-bf4f-e4e6d5423cf5", "storage_backings": [{"storage_uri": "nfs://datastore.test/srv/share/content-library", "type": "OTHER"}], "type": "LOCAL", "version": "2"}, {"creation_time": "2022-11-23T20:02:38.976Z", "description": "automated", "id": "209926aa-e3fe-46a5-95f2-501e82a5139b", "last_modified_time": "2022-11-23T20:02:38.976Z", "name": "my_library_on_nfs_10", "publish_info": {"authentication_method": "NONE", "persist_json_enabled": 0, "publish_url": "https://vcenter.test:443/cls/vcsp/lib/209926aa-e3fe-46a5-95f2-501e82a5139b/lib.json", "published": 1, "user_name": "vcsp"}, "server_guid": "52fb0b5e-ffc3-465b-bf4f-e4e6d5423cf5", "storage_backings": [{"storage_uri": "nfs://datastore.test/srv/share/content-library", "type": "OTHER"}], "type": "LOCAL", "version": "2"}]` |

### Authors

- Ansible Cloud Team (@ansible-collections)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vmware.vmware_rest/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/vmware.vmware_rest)
- [Repository (Sources)](https://github.com/ansible-collections/vmware.vmware_rest.git)
