---
collection: ansible
version: "8"
title: "community.vmware.vmware_content_library_manager module – Create, update and delete VMware content library"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_content_library_manager_module.html
fetched_at: 2026-07-28T01:59:44+00:00
---
# community.vmware.vmware_content_library_manager module – Create, update and delete VMware content library

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
> see [Requirements](vmware_content_library_manager_module.md#ansible-collections-community-vmware-vmware-content-library-manager-module-requirements) for details.
>
> To use it in a playbook, specify: `community.vmware.vmware_content_library_manager`.

- [Synopsis](vmware_content_library_manager_module.md#synopsis)
- [Requirements](vmware_content_library_manager_module.md#requirements)
- [Parameters](vmware_content_library_manager_module.md#parameters)
- [Examples](vmware_content_library_manager_module.md#examples)
- [Return Values](vmware_content_library_manager_module.md#return-values)

## [Synopsis](vmware_content_library_manager_module.md#id1)

- Module to manage VMware content Library
- Content Library feature is introduced in vSphere 6.0 version, so this module is not supported in the earlier versions of vSphere.
- All variables and VMware object names are case sensitive.

## [Requirements](vmware_content_library_manager_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere Automation SDK

## [Parameters](vmware_content_library_manager_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **datastore_name**  aliases: datastore  string | Name of the datastore on which backing content library is created.  This is required only if *state* is set to `present`.  This parameter is ignored, when *state* is set to `absent`.  Currently only datastore backing creation is supported. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **library_description**  string | The content library description.  This is required only if *state* is set to `present`.  This parameter is ignored, when *state* is set to `absent`.  Process of updating content library only allows description change. |
| **library_name**  string / required | The name of VMware content library to manage. |
| **library_type**  string | The content library type.  This is required only if *state* is set to `present`.  This parameter is ignored, when *state* is set to `absent`.  **Choices:**   - `"local"` ← (default) - `"subscribed"` |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **port**  integer | The port number of the vSphere vCenter.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  **Default:** `443` |
| **protocol**  string | The connection to protocol.  **Choices:**   - `"http"` - `"https"` ← (default) |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead. |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **ssl_thumbprint**  string | The SHA1 SSL thumbprint of the subscribed content library to subscribe to.  This is required only if *library_type* is set to `subscribed` and the library is https.  This parameter is ignored, when *state* is set to `absent`.  The information can be extracted using openssl using the following example: `echo | openssl s_client -connect test-library.com:443 |& openssl x509 -fingerprint -noout`  **Default:** `""` |
| **state**  string | The state of content library.  If set to `present` and library does not exists, then content library is created.  If set to `present` and library exists, then content library is updated.  If set to `absent` and library exists, then content library is deleted.  If set to `absent` and library does not exists, no action is taken.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **subscription_url**  string | The url of the content library to subscribe to.  This is required only if *library_type* is set to `subscribed`.  This parameter is ignored, when *state* is set to `absent`.  **Default:** `""` |
| **update_on_demand**  boolean | Whether to download all content on demand.  If set to `true`, all content will be downloaded on demand.  If set to `false` content will be downloaded ahead of time.  This is required only if *library_type* is set to `subscribed`.  This parameter is ignored, when *state* is set to `absent`.  **Choices:**   - `false` ← (default) - `true` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid.  Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Examples](vmware_content_library_manager_module.md#id4)

```yaml+jinja
- name: Create Local Content Library
  community.vmware.vmware_content_library_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    library_name: test-content-lib
    library_description: 'Library with Datastore Backing'
    library_type: local
    datastore_name: datastore
    state: present
  delegate_to: localhost

- name: Create Subscribed Content Library
  community.vmware.vmware_content_library_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    library_name: test-content-lib
    library_description: 'Subscribed Library with Datastore Backing'
    library_type: subscribed
    datastore_name: datastore
    subscription_url: 'https://library.url'
    ssl_thumbprint: 'aa:bb:cc:dd:ee:ff:gg:hh:ii:jj:kk:ll:mm:nn:oo:pp:qq:rr:ss:tt'
    update_on_demand: true
    state: present
  delegate_to: localhost

- name: Update Content Library
  community.vmware.vmware_content_library_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    library_name: test-content-lib
    library_description: 'Library with Datastore Backing'
    state: present
  delegate_to: localhost

- name: Delete Content Library
  community.vmware.vmware_content_library_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    library_name: test-content-lib
    state: absent
  delegate_to: localhost
```

## [Return Values](vmware_content_library_manager_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **content_library_info**  dictionary | library creation success and library_id  **Returned:** on success  **Sample:** `{"library_description": "Test description", "library_id": "d0b92fa9-7039-4f29-8e9c-0debfcb22b72", "library_type": "LOCAL", "msg": "Content Library 'demo-local-lib-4' created."}` |

### Authors

- Pavan Bidkar (@pgbidkar)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
