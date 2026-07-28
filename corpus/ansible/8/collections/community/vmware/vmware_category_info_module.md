---
collection: ansible
version: "8"
title: "community.vmware.vmware_category_info module – Gather info about VMware tag categories"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_category_info_module.html
fetched_at: 2026-07-28T01:59:35+00:00
---
# community.vmware.vmware_category_info module – Gather info about VMware tag categories

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
> see [Requirements](vmware_category_info_module.md#ansible-collections-community-vmware-vmware-category-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.vmware.vmware_category_info`.

- [Synopsis](vmware_category_info_module.md#synopsis)
- [Requirements](vmware_category_info_module.md#requirements)
- [Parameters](vmware_category_info_module.md#parameters)
- [Examples](vmware_category_info_module.md#examples)
- [Return Values](vmware_category_info_module.md#return-values)

## [Synopsis](vmware_category_info_module.md#id1)

- This module can be used to gather information about VMware tag categories.
- Tag feature is introduced in vSphere 6 version, so this module is not supported in earlier versions of vSphere.
- All variables and VMware object names are case sensitive.

## [Requirements](vmware_category_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere Automation SDK

## [Parameters](vmware_category_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **hostname**  string | The hostname or IP address of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **port**  integer | The port number of the vSphere vCenter.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  **Default:** `443` |
| **protocol**  string | The connection to protocol.  **Choices:**   - `"http"` - `"https"` ← (default) |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead. |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid.  Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Examples](vmware_category_info_module.md#id4)

```yaml+jinja
- name: Gather info about tag categories
  community.vmware.vmware_category_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
  delegate_to: localhost
  register: all_tag_category_info

- name: Gather category id from given tag category
  community.vmware.vmware_category_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
  delegate_to: localhost
  register: tag_category_results

- set_fact:
    category_id: "{{ item.category_id }}"
  loop: "{{ tag_category_results.tag_category_info|json_query(query) }}"
  vars:
    query: "[?category_name==`Category0001`]"
- debug: var=category_id
```

## [Return Values](vmware_category_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **tag_category_info**  list / elements=string | metadata of tag categories  **Returned:** always  **Sample:** `[{"category_associable_types": [], "category_cardinality": "MULTIPLE", "category_description": "awesome description", "category_id": "urn:vmomi:InventoryServiceCategory:e785088d-6981-4b1c-9fb8-1100c3e1f742:GLOBAL", "category_name": "Category0001", "category_used_by": []}, {"category_associable_types": ["VirtualMachine"], "category_cardinality": "SINGLE", "category_description": "another awesome description", "category_id": "urn:vmomi:InventoryServiceCategory:ae5b7c6c-e622-4671-9b96-76e93adb70f2:GLOBAL", "category_name": "template_tag", "category_used_by": []}]` |

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
