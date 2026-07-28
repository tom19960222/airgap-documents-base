---
collection: ansible
version: "6"
title: "vmware.vmware_rest.content_subscribedlibrary module – Creates a new subscribed library"
source_url: https://docs.ansible.com/projects/ansible/6/collections/vmware/vmware_rest/content_subscribedlibrary_module.html
fetched_at: 2026-07-28T00:22:04+00:00
---
# vmware.vmware_rest.content_subscribedlibrary module – Creates a new subscribed library

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
> see [Requirements](content_subscribedlibrary_module.md#ansible-collections-vmware-vmware-rest-content-subscribedlibrary-module-requirements) for details.
>
> To use it in a playbook, specify: `vmware.vmware_rest.content_subscribedlibrary`.

New in vmware.vmware_rest 2.0.0

- [Synopsis](content_subscribedlibrary_module.md#synopsis)
- [Requirements](content_subscribedlibrary_module.md#requirements)
- [Parameters](content_subscribedlibrary_module.md#parameters)
- [Notes](content_subscribedlibrary_module.md#notes)
- [Examples](content_subscribedlibrary_module.md#examples)
- [Return Values](content_subscribedlibrary_module.md#return-values)

## [Synopsis](content_subscribedlibrary_module.md#id1)

- Creates a new subscribed library. <p> Once created, the subscribed library will be empty. If the [{@link](mailto:{%40link) LibraryModel#subscriptionInfo} property is set, the Content Library Service will attempt to synchronize to the remote source. This is an asynchronous operation so the content of the published library may not immediately appear.

## [Requirements](content_subscribedlibrary_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp

## [Parameters](content_subscribedlibrary_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **client_token**  string | Unique token generated on the client for each creation request. The token should be a universally unique identifier (UUID), for example: `b8a2a2e3-2314-43cd-a871-6ede0f429751`. This token can be used to guarantee idempotent creation. |
| **creation_time**  string | The date and time when this library was created. |
| **description**  string | A human-readable description for this library. |
| **id**  string | An identifier which uniquely identifies this `library_model`. |
| **last_modified_time**  string | The date and time when this library was last updated. This field is updated automatically when the library properties are changed. This field is not affected by adding, removing, or modifying a library item or its content within the library. Tagging the library or syncing the subscribed library does not alter this field. |
| **last_sync_time**  string | The date and time when this library was last synchronized. This field applies only to subscribed libraries. It is updated every time a synchronization is triggered on the library. The value is not set for a local library. |
| **library_id**  string | Identifier of the subscribed library whose content should be evicted. Required with *state=[‘absent’, ‘evict’, ‘present’, ‘sync’]* |
| **name**  string | The name of the library. A Library is identified by a human-readable name. Library names cannot be undefined or an empty string. Names do not have to be unique. |
| **optimization_info**  dictionary | Defines various optimizations and optimization parameters applied to this library.  Valid attributes are:  - `optimize_remote_publishing` (bool): If set to `True` then library would be optimized for remote publishing. Turn it on if remote publishing is dominant use case for this library. Remote publishing means here that publisher and subscribers are not the part of the same `vcenter` SSO domain. Any optimizations could be done as result of turning on this optimization during library creation. For example, library content could be stored in different format but optimizations are not limited to just storage format. Note, that value of this toggle could be set only during creation of the library and you would need to migrate your library in case you need to change this value (optimize the library for different use case). ([‘present’]) |
| **publish_info**  dictionary | Defines how this library is published so that it can be subscribed to by a remote subscribed library. The `publish_info` defines where and how the metadata for this local library is accessible. A local library is only published publically if `publish_info.published` is `True`.  Valid attributes are:  - `authentication_method` (str): The `authentication_method` indicates how a subscribed library should authenticate to the published library endpoint. ([‘present’])    - Accepted values:      - BASIC     - NONE - `published` (bool): Whether the local library is published. ([‘present’]) - `publish_url` (str): The URL to which the library metadata is published by the Content Library Service. This value can be used to set the `subscription_info.subscriptionurl` property when creating a subscribed library. ([‘present’]) - `user_name` (str): The username to require for authentication. ([‘present’]) - `password` (str): The new password to require for authentication. ([‘present’]) - `current_password` (str): The current password to verify. This field is available starting in vSphere 6.7. ([‘present’]) - `persist_json_enabled` (bool): Whether library and library item metadata are persisted in the storage backing as JSON files. This flag only applies if the local library is published. Enabling JSON persistence allows you to synchronize a subscribed library manually instead of over HTTP. You copy the local library content and metadata to another storage backing manually and then create a subscribed library referencing the location of the library JSON file in the `subscription_info.subscriptionurl`. When the subscribed library’s storage backing matches the subscription URL, files do not need to be copied to the subscribed library. For a library backed by a datastore, the library JSON file will be stored at the path contentlib-{library_id}/lib.json on the datastore. For a library backed by a remote file system, the library JSON file will be stored at {library_id}/lib.json in the remote file system path. ([‘present’]) |
| **server_guid**  string | The unique identifier of the vCenter server where the library exists. |
| **session_timeout**  float  added in vmware.vmware_rest 2.1.0 | Timeout settings for client session.  The maximal number of seconds for the whole operation including connection establishment, request sending and response.  The default value is 300s. |
| **state**  string | Choices:   - `"absent"` - `"evict"` - `"present"` ← (default) - `"probe"` - `"sync"` |
| **storage_backings**  list / elements=dictionary | The list of default storage backings which are available for this library. A storage backing defines a default storage location which can be used to store files for library items in this library. Some library items, for instance, virtual machine template items, support files that may be distributed across various storage backings. One or more item files may or may not be located on the default storage backing. Multiple default storage locations are not currently supported but may become supported in future releases.  Valid attributes are:  - `type` (str): The `type` specifies the type of the storage backing. ([‘present’])    - Accepted values:      - DATASTORE     - OTHER - `datastore_id` (str): Identifier of the datastore used to store the content in the library. ([‘present’]) - `storage_uri` (str): URI identifying the location used to store the content in the library. The following URI formats are supported: vSphere 6.5 <ul> <li>nfs://server/path?version=4 (for vCenter Server Appliance only) - Specifies an NFS Version 4 server.</li> <li>nfs://server/path (for vCenter Server Appliance only) - Specifies an NFS Version 3 server. The <nfs://server:/path> format is also supported.</li> <li>smb://server/path - Specifies an SMB server or Windows share.</li> </ul> vSphere 6.0 Update 1 <ul> <li>nfs://server:/path (for vCenter Server Appliance only)</li> <li>file://unc-server/path (for vCenter Server for Windows only)</li> <li>file:///mount/point (for vCenter Server Appliance only) - Local file URIs are supported only when the path is a local mount point for an NFS file system. Use of file URIs is strongly discouraged. Instead, use an NFS URI to specify the remote file system.</li> </ul> vSphere 6.0 <ul> <li>nfs://server:/path (for vCenter Server Appliance only)</li> <li>file://unc-server/path (for vCenter Server for Windows only)</li> <li>file:///path - Local file URIs are supported but strongly discouraged because it may interfere with the performance of vCenter Server.</li> </ul> ([‘present’]) |
| **subscription_info**  dictionary | Defines the subscription behavior for this Library. The `subscription_info` defines how this subscribed library synchronizes to a remote source. Setting the value will determine the remote source to which the library synchronizes, and how. Changing the subscription will result in synchronizing to a new source. If the new source differs from the old one, the old library items and data will be lost. Setting `subscription_info.automaticSyncEnabled` to false will halt subscription but will not remove existing cached data.  Valid attributes are:  - `authentication_method` (str): Indicate how the subscribed library should authenticate with the published library endpoint. ([‘present’, ‘probe’])    - Accepted values:      - BASIC     - NONE - `automatic_sync_enabled` (bool): Whether the library should participate in automatic library synchronization. In order for automatic synchronization to happen, the global `configuration_model.automatic_sync_enabled` option must also be true. The subscription is still active even when automatic synchronization is turned off, but synchronization is only activated with an explicit call to [vmware.vmware_rest.content_subscribedlibrary](content_subscribedlibrary_module.md#ansible-collections-vmware-vmware-rest-content-subscribedlibrary-module) with `state=sync` or vmware.vmware_rest.content_library_item with `state=sync`. In other words, manual synchronization is still available even when automatic synchronization is disabled. ([‘present’, ‘probe’]) - `on_demand` (bool): Indicates whether a library item’s content will be synchronized only on demand. If this is set to `True`, then the library item’s metadata will be synchronized but the item’s content (its files) will not be synchronized. The Content Library Service will synchronize the content upon request only. This can cause the first use of the content to have a noticeable delay. Items without synchronized content can be forcefully synchronized in advance using the vmware.vmware_rest.content_library_item with `state=sync` call with `force_sync_content` set to true. Once content has been synchronized, the content can removed with the vmware.vmware_rest.content_library_item with `state=sync` call. If this value is set to `False`, all content will be synchronized in advance. ([‘present’, ‘probe’]) - `password` (str): The password to use when authenticating. The password must be set when using a password-based authentication method; empty strings are not allowed. ([‘present’, ‘probe’]) - `ssl_thumbprint` (str): An optional SHA-1 hash of the SSL certificate for the remote endpoint. If this value is defined the SSL certificate will be verified by comparing it to the SSL thumbprint. The SSL certificate must verify against the thumbprint. When specified, the standard certificate chain validation behavior is not used. The certificate chain is validated normally if this value is not set. ([‘present’, ‘probe’]) - `subscription_url` (str): The URL of the endpoint where the metadata for the remotely published library is being served. This URL can be the `publish_info.publish_url` of the published library (for example, <https://server/path/lib.json>). If the source content comes from a published library with `publish_info.persist_json_enabled`, the subscription URL can be a URL pointing to the library JSON file on a datastore or remote file system. The supported formats are: vSphere 6.5 <ul> <li>ds:///vmfs/volumes/{uuid}/mylibrary/lib.json (for datastore)</li> <li>nfs://server/path/mylibrary/lib.json (for NFSv3 server on vCenter Server Appliance)</li> <li>nfs://server/path/mylibrary/lib.json?version=4 (for NFSv4 server on vCenter Server Appliance) </li> <li>smb://server/path/mylibrary/lib.json (for SMB server)</li> </ul> vSphere 6.0 <ul> <li>file://server/mylibrary/lib.json (for UNC server on vCenter Server for Windows)</li> <li>file:///path/mylibrary/lib.json (for local file system)</li> </ul> When you specify a DS subscription URL, the datastore must be on the same vCenter Server as the subscribed library. When you specify an NFS or SMB subscription URL, the `storage_backings.storage_uri` of the subscribed library must be on the same remote file server and should share a common parent path with the subscription URL. ([‘present’, ‘probe’]) - `user_name` (str): The username to use when authenticating. The username must be set when using a password-based authentication method. Empty strings are allowed for usernames. ([‘present’, ‘probe’]) - `source_info` (dict): Information about the source published library. This field will be set for a subscribed library which is associated with a subscription of the published library. ([‘present’, ‘probe’])    - Accepted keys:      - source_library (string): Identifier of the published library.     - subscription (string): Identifier of the subscription associated with the subscribed library. |
| **type**  string | The `library_type` defines the type of a Library. The type of a library can be used to determine which additional services can be performed with a library.  Choices:   - `"LOCAL"` - `"SUBSCRIBED"` |
| **vcenter_hostname**  string / required | The hostname or IP address of the vSphere vCenter  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **vcenter_password**  string / required | The vSphere vCenter password  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **vcenter_rest_log_file**  string | You can use this optional parameter to set the location of a log file.  This file will be used to record the HTTP REST interaction.  The file will be stored on the host that run the module.  If the value is not specified in the task, the value of  environment variable `VMWARE_REST_LOG_FILE` will be used instead. |
| **vcenter_username**  string / required | The vSphere vCenter username  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **vcenter_validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |
| **version**  string | A version number which is updated on metadata changes. This value allows clients to detect concurrent updates and prevent accidental clobbering of data. This value represents a number which is incremented every time library properties, such as name or description, are changed. It is not incremented by changes to a library item within the library, including adding or removing items. It is also not affected by tagging the library. |

## [Notes](content_subscribedlibrary_module.md#id4)

> **Note:**
>
> - Tested on vSphere 7.0.2

## [Examples](content_subscribedlibrary_module.md#id5)

```yaml+jinja
- name: Build a list of subscribed libraries
  vmware.vmware_rest.content_subscribedlibrary_info:
  register: result

- name: Delete all the subscribed libraries
  vmware.vmware_rest.content_subscribedlibrary:
    library_id: '{{ item.id }}'
    state: absent
  with_items: '{{ result.value }}'

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

- name: Create subscribed library
  vmware.vmware_rest.content_subscribedlibrary:
    name: sub_lib
    subscription_info:
      subscription_url: '{{ nfs_lib.value.publish_info.publish_url }}'
      authentication_method: NONE
      automatic_sync_enabled: false
      on_demand: true
    storage_backings:
    - datastore_id: "{{ lookup('vmware.vmware_rest.datastore_moid', '/my_dc/datastore/rw_datastore')\
        \ }}"
      type: DATASTORE
  register: sub_lib

- name: Create subscribed library (again)
  vmware.vmware_rest.content_subscribedlibrary:
    name: sub_lib
    subscription_info:
      subscription_url: '{{ nfs_lib.value.publish_info.publish_url }}'
      authentication_method: NONE
      automatic_sync_enabled: false
      on_demand: true
    storage_backings:
    - datastore_id: "{{ lookup('vmware.vmware_rest.datastore_moid', '/my_dc/datastore/rw_datastore')\
        \ }}"
      type: DATASTORE
  register: result

- name: Clean up the cache
  vmware.vmware_rest.content_subscribedlibrary:
    name: sub_lib
    library_id: '{{ sub_lib.id }}'
    state: evict

- name: Trigger a library sync
  vmware.vmware_rest.content_subscribedlibrary:
    name: sub_lib
    library_id: '{{ sub_lib.id }}'
    state: sync
```

## [Return Values](content_subscribedlibrary_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Delete all the subscribed libraries  Returned: On success  Sample: `"All items completed"` |
| **results**  list / elements=string | Delete all the subscribed libraries  Returned: On success  Sample: `[{"_ansible_item_label": {"creation_time": "2022-06-23T22:38:29.995Z", "description": "", "id": "41bd5c47-e658-4876-bab2-03758f25a3e9", "last_modified_time": "2022-06-23T22:38:29.995Z", "last_sync_time": "2022-06-23T22:38:32.305Z", "name": "sub_lib", "server_guid": "b138c531-cd80-43f5-842d-657d9ddc98f8", "storage_backings": [{"datastore_id": "datastore-1200", "type": "DATASTORE"}], "subscription_info": {"authentication_method": "NONE", "automatic_sync_enabled": 0, "on_demand": 1, "subscription_url": "https://vcenter.test:443/cls/vcsp/lib/c9b8f7da-d5ac-4076-86b9-39ee107d7da3/lib.json"}, "type": "SUBSCRIBED", "version": "4"}, "_ansible_no_log": null, "ansible_loop_var": "item", "changed": 1, "failed": 0, "invocation": {"module_args": {"client_token": null, "creation_time": null, "description": null, "id": null, "last_modified_time": null, "last_sync_time": null, "library_id": "41bd5c47-e658-4876-bab2-03758f25a3e9", "name": null, "optimization_info": null, "publish_info": null, "server_guid": null, "session_timeout": null, "state": "absent", "storage_backings": null, "subscription_info": null, "type": null, "vcenter_hostname": "vcenter.test", "vcenter_password": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER", "vcenter_rest_log_file": null, "vcenter_username": "administrator@vsphere.local", "vcenter_validate_certs": 0, "version": null}}, "item": {"creation_time": "2022-06-23T22:38:29.995Z", "description": "", "id": "41bd5c47-e658-4876-bab2-03758f25a3e9", "last_modified_time": "2022-06-23T22:38:29.995Z", "last_sync_time": "2022-06-23T22:38:32.305Z", "name": "sub_lib", "server_guid": "b138c531-cd80-43f5-842d-657d9ddc98f8", "storage_backings": [{"datastore_id": "datastore-1200", "type": "DATASTORE"}], "subscription_info": {"authentication_method": "NONE", "automatic_sync_enabled": 0, "on_demand": 1, "subscription_url": "https://vcenter.test:443/cls/vcsp/lib/c9b8f7da-d5ac-4076-86b9-39ee107d7da3/lib.json"}, "type": "SUBSCRIBED", "version": "4"}, "value": {}}]` |

### Authors

- Ansible Cloud Team (@ansible-collections)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/vmware.vmware_rest/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/vmware.vmware_rest)
[Repository (Sources)](https://github.com/ansible-collections/vmware.vmware_rest.git)
