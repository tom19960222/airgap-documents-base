---
collection: ansible
version: "8"
title: "community.vmware.vmware_category module – Manage VMware categories"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_category_module.html
fetched_at: 2026-07-28T01:59:34+00:00
---
# community.vmware.vmware_category module – Manage VMware categories

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
> see [Requirements](vmware_category_module.md#ansible-collections-community-vmware-vmware-category-module-requirements) for details.
>
> To use it in a playbook, specify: `community.vmware.vmware_category`.

- [Synopsis](vmware_category_module.md#synopsis)
- [Requirements](vmware_category_module.md#requirements)
- [Parameters](vmware_category_module.md#parameters)
- [Examples](vmware_category_module.md#examples)
- [Return Values](vmware_category_module.md#return-values)

## [Synopsis](vmware_category_module.md#id1)

- This module can be used to create / delete / update VMware categories.
- Tag feature is introduced in vSphere 6 version, so this module is not supported in the earlier versions of vSphere.
- All variables and VMware object names are case sensitive.

## [Requirements](vmware_category_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere Automation SDK

## [Parameters](vmware_category_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **associable_object_types**  list / elements=string | List of object types that can be associated with the given category.  **Choices:**   - `"All objects"` - `"Cluster"` - `"Content Library"` - `"Datacenter"` - `"Datastore"` - `"Datastore Cluster"` - `"Distributed Port Group"` - `"Distributed Switch"` - `"Folder"` - `"Host"` - `"Library item"` - `"Network"` - `"Host Network"` - `"Opaque Network"` - `"Resource Pool"` - `"vApp"` - `"Virtual Machine"` |
| **category_cardinality**  string | The category cardinality.  This parameter is ignored, when updating existing category.  **Choices:**   - `"multiple"` ← (default) - `"single"` |
| **category_description**  string | The category description.  This is required only if `state` is set to `present`.  This parameter is ignored, when `state` is set to `absent`.  **Default:** `""` |
| **category_name**  string / required | The name of category to manage. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **new_category_name**  string | The new name for an existing category.  This value is used while updating an existing category. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **port**  integer | The port number of the vSphere vCenter.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  **Default:** `443` |
| **protocol**  string | The connection to protocol.  **Choices:**   - `"http"` - `"https"` ← (default) |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead. |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | The state of category.  If set to `present` and category does not exists, then category is created.  If set to `present` and category exists, then category is updated.  If set to `absent` and category exists, then category is deleted.  If set to `absent` and category does not exists, no action is taken.  Process of updating category only allows name, description change.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid.  Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Examples](vmware_category_module.md#id4)

```yaml+jinja
- name: Create a category
  community.vmware.vmware_category:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    category_name: Sample_Cat_0001
    category_description: Sample Description
    category_cardinality: 'multiple'
    state: present

- name: Rename category
  community.vmware.vmware_category:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    category_name: Sample_Category_0001
    new_category_name: Sample_Category_0002
    state: present

- name: Update category description
  community.vmware.vmware_category:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    category_name: Sample_Category_0001
    category_description: Some fancy description
    state: present

- name: Delete category
  community.vmware.vmware_category:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    category_name: Sample_Category_0002
    state: absent

- name: Create category with 2 associable object types
  community.vmware.vmware_category:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    category_name: 'Sample_Category_0003'
    category_description: 'sample description'
    associable_object_types:
    - Datastore
    - Cluster
    state: present
```

## [Return Values](vmware_category_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **category_results**  dictionary | dictionary of category metadata  **Returned:** on success  **Sample:** `{"category_id": "urn:vmomi:InventoryServiceCategory:d7120bda-9fa5-4f92-9d71-aa1acff2e5a8:GLOBAL", "msg": "Category NewCat_0001 updated."}` |

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
