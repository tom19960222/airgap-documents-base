---
collection: ansible
version: "6"
title: "vmware.vmware_rest.content_locallibrary_info module – Returns a given local library."
source_url: https://docs.ansible.com/projects/ansible/6/collections/vmware/vmware_rest/content_locallibrary_info_module.html
fetched_at: 2026-07-28T00:22:03+00:00
---
# vmware.vmware_rest.content_locallibrary_info module – Returns a given local library.

> **Note:**
>
> This module is part of the [vmware.vmware_rest collection](https://galaxy.ansible.com/vmware/vmware_rest) (version 2.2.0).
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
| **session_timeout**  float  added in vmware.vmware_rest 2.1.0 | Timeout settings for client session.  The maximal number of seconds for the whole operation including connection establishment, request sending and response.  The default value is 300s. |
| **vcenter_hostname**  string / required | The hostname or IP address of the vSphere vCenter  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **vcenter_password**  string / required | The vSphere vCenter password  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **vcenter_rest_log_file**  string | You can use this optional parameter to set the location of a log file.  This file will be used to record the HTTP REST interaction.  The file will be stored on the host that run the module.  If the value is not specified in the task, the value of  environment variable `VMWARE_REST_LOG_FILE` will be used instead. |
| **vcenter_username**  string / required | The vSphere vCenter username  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **vcenter_validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Notes](content_locallibrary_info_module.md#id4)

> **Note:**
>
> - Tested on vSphere 7.0.2

## [Examples](content_locallibrary_info_module.md#id5)

```yaml+jinja
- name: Build a list of local libraries
  vmware.vmware_rest.content_locallibrary_info:
  register: result
  retries: 100
  delay: 3
  until: result is not failed

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
    - datastore_id: "{{ lookup('vmware.vmware_rest.datastore_moid', '/my_dc/datastore/rw_datastore')\
        \ }}"
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
| **value**  list / elements=string | List all Local Content Library  Returned: On success  Sample: `[{"creation_time": "2022-06-23T22:35:23.573Z", "description": "automated", "id": "53a679e5-a7dc-4d50-ad6e-759f697b6143", "last_modified_time": "2022-06-23T22:35:23.573Z", "name": "my_library_on_nfs_3", "publish_info": {"authentication_method": "NONE", "persist_json_enabled": 0, "publish_url": "https://vcenter.test:443/cls/vcsp/lib/53a679e5-a7dc-4d50-ad6e-759f697b6143/lib.json", "published": 1, "user_name": "vcsp"}, "server_guid": "b138c531-cd80-43f5-842d-657d9ddc98f8", "storage_backings": [{"storage_uri": "nfs://datastore.test/srv/share/content-library", "type": "OTHER"}], "type": "LOCAL", "version": "2"}, {"creation_time": "2022-06-23T22:35:24.545Z", "description": "automated", "id": "b8380086-243a-400d-9a9f-8259f83d0148", "last_modified_time": "2022-06-23T22:35:24.545Z", "name": "my_library_on_nfs_4", "publish_info": {"authentication_method": "NONE", "persist_json_enabled": 0, "publish_url": "https://vcenter.test:443/cls/vcsp/lib/b8380086-243a-400d-9a9f-8259f83d0148/lib.json", "published": 1, "user_name": "vcsp"}, "server_guid": "b138c531-cd80-43f5-842d-657d9ddc98f8", "storage_backings": [{"storage_uri": "nfs://datastore.test/srv/share/content-library", "type": "OTHER"}], "type": "LOCAL", "version": "2"}, {"creation_time": "2022-06-23T22:35:25.464Z", "description": "automated", "id": "1bad9ede-140b-4c62-bc6b-df506eb27292", "last_modified_time": "2022-06-23T22:35:25.464Z", "name": "my_library_on_nfs_5", "publish_info": {"authentication_method": "NONE", "persist_json_enabled": 0, "publish_url": "https://vcenter.test:443/cls/vcsp/lib/1bad9ede-140b-4c62-bc6b-df506eb27292/lib.json", "published": 1, "user_name": "vcsp"}, "server_guid": "b138c531-cd80-43f5-842d-657d9ddc98f8", "storage_backings": [{"storage_uri": "nfs://datastore.test/srv/share/content-library", "type": "OTHER"}], "type": "LOCAL", "version": "2"}, {"creation_time": "2022-06-23T22:35:26.405Z", "description": "automated", "id": "a2d5c986-e376-4648-95f1-661efff3f851", "last_modified_time": "2022-06-23T22:35:26.405Z", "name": "my_library_on_nfs_6", "publish_info": {"authentication_method": "NONE", "persist_json_enabled": 0, "publish_url": "https://vcenter.test:443/cls/vcsp/lib/a2d5c986-e376-4648-95f1-661efff3f851/lib.json", "published": 1, "user_name": "vcsp"}, "server_guid": "b138c531-cd80-43f5-842d-657d9ddc98f8", "storage_backings": [{"storage_uri": "nfs://datastore.test/srv/share/content-library", "type": "OTHER"}], "type": "LOCAL", "version": "2"}, {"creation_time": "2022-06-23T22:35:27.357Z", "description": "automated", "id": "45f33229-1232-4d7d-9cb3-69d7888bbb07", "last_modified_time": "2022-06-23T22:35:27.357Z", "name": "my_library_on_nfs_7", "publish_info": {"authentication_method": "NONE", "persist_json_enabled": 0, "publish_url": "https://vcenter.test:443/cls/vcsp/lib/45f33229-1232-4d7d-9cb3-69d7888bbb07/lib.json", "published": 1, "user_name": "vcsp"}, "server_guid": "b138c531-cd80-43f5-842d-657d9ddc98f8", "storage_backings": [{"storage_uri": "nfs://datastore.test/srv/share/content-library", "type": "OTHER"}], "type": "LOCAL", "version": "2"}, {"creation_time": "2022-06-23T22:35:28.377Z", "description": "automated", "id": "8723c432-c706-4dfb-9f56-dadd3b95f299", "last_modified_time": "2022-06-23T22:35:28.377Z", "name": "my_library_on_nfs_8", "publish_info": {"authentication_method": "NONE", "persist_json_enabled": 0, "publish_url": "https://vcenter.test:443/cls/vcsp/lib/8723c432-c706-4dfb-9f56-dadd3b95f299/lib.json", "published": 1, "user_name": "vcsp"}, "server_guid": "b138c531-cd80-43f5-842d-657d9ddc98f8", "storage_backings": [{"storage_uri": "nfs://datastore.test/srv/share/content-library", "type": "OTHER"}], "type": "LOCAL", "version": "2"}, {"creation_time": "2022-06-23T22:35:29.397Z", "description": "automated", "id": "bae6e392-12e7-4868-b18f-f487307bf752", "last_modified_time": "2022-06-23T22:35:29.397Z", "name": "my_library_on_nfs_9", "publish_info": {"authentication_method": "NONE", "persist_json_enabled": 0, "publish_url": "https://vcenter.test:443/cls/vcsp/lib/bae6e392-12e7-4868-b18f-f487307bf752/lib.json", "published": 1, "user_name": "vcsp"}, "server_guid": "b138c531-cd80-43f5-842d-657d9ddc98f8", "storage_backings": [{"storage_uri": "nfs://datastore.test/srv/share/content-library", "type": "OTHER"}], "type": "LOCAL", "version": "2"}, {"creation_time": "2022-06-23T22:35:30.412Z", "description": "automated", "id": "61ea41a8-9443-4a64-9181-f9a046012197", "last_modified_time": "2022-06-23T22:35:30.412Z", "name": "my_library_on_nfs_10", "publish_info": {"authentication_method": "NONE", "persist_json_enabled": 0, "publish_url": "https://vcenter.test:443/cls/vcsp/lib/61ea41a8-9443-4a64-9181-f9a046012197/lib.json", "published": 1, "user_name": "vcsp"}, "server_guid": "b138c531-cd80-43f5-842d-657d9ddc98f8", "storage_backings": [{"storage_uri": "nfs://datastore.test/srv/share/content-library", "type": "OTHER"}], "type": "LOCAL", "version": "2"}, {"creation_time": "2022-06-23T22:35:19.438Z", "description": "automated", "id": "c9b8f7da-d5ac-4076-86b9-39ee107d7da3", "last_modified_time": "2022-06-23T22:35:19.438Z", "name": "my_library_on_nfs", "publish_info": {"authentication_method": "NONE", "persist_json_enabled": 0, "publish_url": "https://vcenter.test:443/cls/vcsp/lib/c9b8f7da-d5ac-4076-86b9-39ee107d7da3/lib.json", "published": 1, "user_name": "vcsp"}, "server_guid": "b138c531-cd80-43f5-842d-657d9ddc98f8", "storage_backings": [{"storage_uri": "nfs://datastore.test/srv/share/content-library", "type": "OTHER"}], "type": "LOCAL", "version": "2"}, {"creation_time": "2022-06-23T22:35:20.801Z", "description": "automated", "id": "99517bfa-7f2c-4e01-83e5-ed1bbb13c3e6", "last_modified_time": "2022-06-23T22:35:20.801Z", "name": "my_library_on_nfs_0", "publish_info": {"authentication_method": "NONE", "persist_json_enabled": 0, "publish_url": "https://vcenter.test:443/cls/vcsp/lib/99517bfa-7f2c-4e01-83e5-ed1bbb13c3e6/lib.json", "published": 1, "user_name": "vcsp"}, "server_guid": "b138c531-cd80-43f5-842d-657d9ddc98f8", "storage_backings": [{"storage_uri": "nfs://datastore.test/srv/share/content-library", "type": "OTHER"}], "type": "LOCAL", "version": "2"}, {"creation_time": "2022-06-23T22:35:21.697Z", "description": "automated", "id": "0926be51-049a-476b-8537-e4b3d0a572a9", "last_modified_time": "2022-06-23T22:35:21.697Z", "name": "my_library_on_nfs_1", "publish_info": {"authentication_method": "NONE", "persist_json_enabled": 0, "publish_url": "https://vcenter.test:443/cls/vcsp/lib/0926be51-049a-476b-8537-e4b3d0a572a9/lib.json", "published": 1, "user_name": "vcsp"}, "server_guid": "b138c531-cd80-43f5-842d-657d9ddc98f8", "storage_backings": [{"storage_uri": "nfs://datastore.test/srv/share/content-library", "type": "OTHER"}], "type": "LOCAL", "version": "2"}, {"creation_time": "2022-06-23T22:35:22.620Z", "description": "automated", "id": "7c970cd1-1526-4903-8295-64e28ecc6bad", "last_modified_time": "2022-06-23T22:35:22.620Z", "name": "my_library_on_nfs_2", "publish_info": {"authentication_method": "NONE", "persist_json_enabled": 0, "publish_url": "https://vcenter.test:443/cls/vcsp/lib/7c970cd1-1526-4903-8295-64e28ecc6bad/lib.json", "published": 1, "user_name": "vcsp"}, "server_guid": "b138c531-cd80-43f5-842d-657d9ddc98f8", "storage_backings": [{"storage_uri": "nfs://datastore.test/srv/share/content-library", "type": "OTHER"}], "type": "LOCAL", "version": "2"}]` |

### Authors

- Ansible Cloud Team (@ansible-collections)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/vmware.vmware_rest/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/vmware.vmware_rest)
[Repository (Sources)](https://github.com/ansible-collections/vmware.vmware_rest.git)
