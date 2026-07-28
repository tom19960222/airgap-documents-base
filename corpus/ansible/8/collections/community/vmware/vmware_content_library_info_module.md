---
collection: ansible
version: "8"
title: "community.vmware.vmware_content_library_info module – Gather information about VMWare Content Library"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_content_library_info_module.html
fetched_at: 2026-07-28T01:59:43+00:00
---
# community.vmware.vmware_content_library_info module – Gather information about VMWare Content Library

> **Note:**
>
> This module is part of the [community.vmware collection](https://galaxy.ansible.com/ui/repo/published/community/vmware/) (version 3.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
> You need further requirements to be able to use this module,
> see [Requirements](vmware_content_library_info_module.md#ansible-collections-community-vmware-vmware-content-library-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.vmware.vmware_content_library_info`.

- [Synopsis](vmware_content_library_info_module.md#synopsis)
- [Requirements](vmware_content_library_info_module.md#requirements)
- [Parameters](vmware_content_library_info_module.md#parameters)
- [Examples](vmware_content_library_info_module.md#examples)
- [Return Values](vmware_content_library_info_module.md#return-values)

## [Synopsis](vmware_content_library_info_module.md#id1)

- Module to list the content libraries.
- Module to get information about specific content library.
- Content Library feature is introduced in vSphere 6.0 version, so this module is not supported in the earlier versions of vSphere.
- All variables and VMware object names are case sensitive.

## [Requirements](vmware_content_library_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere Automation SDK

## [Parameters](vmware_content_library_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **hostname**  string | The hostname or IP address of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **library_id**  string | content library id for which details needs to be fetched. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **port**  integer | The port number of the vSphere vCenter.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  **Default:** `443` |
| **protocol**  string | The connection to protocol.  **Choices:**   - `"http"` - `"https"` ← (default) |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead. |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid.  Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Examples](vmware_content_library_info_module.md#id4)

```yaml+jinja
- name: Get List of Content Libraries
  community.vmware.vmware_content_library_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
  delegate_to: localhost

- name: Get information about content library
  community.vmware.vmware_content_library_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    library_id: '13b0f060-f4d3-4f84-b61f-0fe1b0c0a5a8'
  delegate_to: localhost
```

## [Return Values](vmware_content_library_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **content_lib_details**  list / elements=string | list of content library metadata  **Returned:** on success  **Sample:** `[{"library_creation_time": "2019-07-02T11:50:52.242000", "library_description": "new description", "library_id": "13b0f060-f4d3-4f84-b61f-0fe1b0c0a5a8", "library_name": "demo-local-lib", "library_publish_info": {"authentication_method": "NONE", "persist_json_enabled": false, "publish_url": null, "published": false, "user_name": null}, "library_server_guid": "0fd5813b-aac7-4b92-9fb7-f18f16565613", "library_type": "LOCAL", "library_version": "3"}]` |
| **content_libs**  list / elements=string | list of content libraries  **Returned:** on success  **Sample:** `["ded9c4d5-0dcd-4837-b1d8-af7398511e33", "36b72549-14ed-4b5f-94cb-6213fecacc02"]` |

### Authors

- Pavan Bidkar (@pgbidkar)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
