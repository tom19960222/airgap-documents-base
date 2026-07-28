---
collection: ansible
version: "8"
title: "community.vmware.vmware_tag_manager module – Manage association of VMware tags with VMware objects"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_tag_manager_module.html
fetched_at: 2026-07-28T02:01:12+00:00
---
# community.vmware.vmware_tag_manager module – Manage association of VMware tags with VMware objects

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
> see [Requirements](vmware_tag_manager_module.md#ansible-collections-community-vmware-vmware-tag-manager-module-requirements) for details.
>
> To use it in a playbook, specify: `community.vmware.vmware_tag_manager`.

- [Synopsis](vmware_tag_manager_module.md#synopsis)
- [Requirements](vmware_tag_manager_module.md#requirements)
- [Parameters](vmware_tag_manager_module.md#parameters)
- [Examples](vmware_tag_manager_module.md#examples)
- [Return Values](vmware_tag_manager_module.md#return-values)

## [Synopsis](vmware_tag_manager_module.md#id1)

- This module can be used to assign / remove VMware tags from the given VMware objects.
- Tag feature is introduced in vSphere 6 version, so this module is not supported in the earlier versions of vSphere.
- All variables and VMware object names are case sensitive.

## [Requirements](vmware_tag_manager_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere Automation SDK

## [Parameters](vmware_tag_manager_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **hostname**  string | The hostname or IP address of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **moid**  string | Managed object ID for the given object.  Required if `object_name` is not set. |
| **object_name**  string | Name of the object to work with.  For DistributedVirtualPortgroups the format should be “switch_name:portgroup_name”  Required if `moid` is not set. |
| **object_type**  string / required | Type of object to work with.  **Choices:**   - `"VirtualMachine"` - `"Datacenter"` - `"ClusterComputeResource"` - `"HostSystem"` - `"DistributedVirtualSwitch"` - `"DistributedVirtualPortgroup"` - `"Datastore"` - `"DatastoreCluster"` - `"ResourcePool"` - `"Folder"` |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **port**  integer | The port number of the vSphere vCenter.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  **Default:** `443` |
| **protocol**  string | The connection to protocol.  **Choices:**   - `"http"` - `"https"` ← (default) |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead. |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | If `state` is set to `add` or `present` will add the tags to the existing tag list of the given object.  If `state` is set to `remove` or `absent` will remove the tags from the existing tag list of the given object.  If `state` is set to `set` will replace the tags of the given objects with the user defined list of tags.  **Choices:**   - `"present"` - `"absent"` - `"add"` ← (default) - `"remove"` - `"set"` |
| **tag_names**  list / elements=any / required | List of tag(s) to be managed.  User can also specify category name by specifying colon separated value. For example, “category_name:tag_name”.  User can also specify tag and category as dict, when tag or category contains colon. See example for more information. Added in version 2.10.  User can skip category name if you have unique tag names. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid.  Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Examples](vmware_tag_manager_module.md#id4)

```yaml+jinja
- name: Add tags to a virtual machine
  community.vmware.vmware_tag_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    tag_names:
      - Sample_Tag_0002
      - Category_0001:Sample_Tag_0003
    object_name: Fedora_VM
    object_type: VirtualMachine
    state: add
  delegate_to: localhost

- name: Specify tag and category as dict
  community.vmware.vmware_tag_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    tag_names:
      - tag: tag_0001
        category: cat_0001
      - tag: tag_0002
        category: cat_0002
    object_name: Fedora_VM
    object_type: VirtualMachine
    state: add
  delegate_to: localhost

- name: Remove a tag from a virtual machine
  community.vmware.vmware_tag_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    tag_names:
      - Sample_Tag_0002
    object_name: Fedora_VM
    object_type: VirtualMachine
    state: remove
  delegate_to: localhost

- name: Add tags to a distributed virtual switch
  community.vmware.vmware_tag_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    tag_names:
      - Sample_Tag_0003
    object_name: Switch_0001
    object_type: DistributedVirtualSwitch
    state: add
  delegate_to: localhost

- name: Add tags to a distributed virtual portgroup
  community.vmware.vmware_tag_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    tag_names:
      - Sample_Tag_0004
    object_name: Switch_0001:Portgroup_0001
    object_type: DistributedVirtualPortgroup
    state: add
  delegate_to: localhost

- name: Get information about folders
  community.vmware.vmware_folder_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: 'Asia-Datacenter1'
  delegate_to: localhost
  register: r
- name: Set Managed object ID for the given folder
  ansible.builtin.set_fact:
    folder_mo_id: "{{ (r.flat_folder_info | selectattr('path', 'equalto', '/Asia-Datacenter1/vm/tier1/tier2') | map(attribute='moid'))[0] }}"
- name: Add tags to a Folder using managed object id
  community.vmware.vmware_tag_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    tag_names:
      - Sample_Cat_0004:Sample_Tag_0004
    object_type: Folder
    moid: "{{ folder_mo_id }}"
    state: add
  delegate_to: localhost
```

## [Return Values](vmware_tag_manager_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **tag_status**  list / elements=string | metadata about tags related to object configuration  **Returned:** on success  **Sample:** `{"attached_tags": ["urn:vmomi:InventoryServiceCategory:76f69e84-f6b9-4e64-954c-fac545d2c0ba:GLOBAL:security"], "current_tags": ["urn:vmomi:InventoryServiceCategory:927f5ff8-62e6-4364-bc94-23e3bfd7dee7:GLOBAL:backup", "urn:vmomi:InventoryServiceCategory:76f69e84-f6b9-4e64-954c-fac545d2c0ba:GLOBAL:security"], "detached_tags": [], "previous_tags": ["urn:vmomi:InventoryServiceCategory:927f5ff8-62e6-4364-bc94-23e3bfd7dee7:GLOBAL:backup"]}` |

### Authors

- Abhijeet Kasurde (@Akasurde)
- Frederic Van Reet (@GBrawl)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
