---
collection: ansible
version: "6"
title: "community.vmware.vmware_tag_info module – Manage VMware tag info"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_tag_info_module.html
fetched_at: 2026-07-27T17:22:48+00:00
---
# community.vmware.vmware_tag_info module – Manage VMware tag info

> **Note:**
>
> This module is part of the [community.vmware collection](https://galaxy.ansible.com/community/vmware) (version 2.10.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
> You need further requirements to be able to use this module,
> see [Requirements](vmware_tag_info_module.md#ansible-collections-community-vmware-vmware-tag-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.vmware.vmware_tag_info`.

- [Synopsis](vmware_tag_info_module.md#synopsis)
- [Requirements](vmware_tag_info_module.md#requirements)
- [Parameters](vmware_tag_info_module.md#parameters)
- [Examples](vmware_tag_info_module.md#examples)
- [Return Values](vmware_tag_info_module.md#return-values)

## [Synopsis](vmware_tag_info_module.md#id1)

- This module can be used to collect information about VMware tags.
- Tag feature is introduced in vSphere 6 version, so this module is not supported in the earlier versions of vSphere.
- All variables and VMware object names are case sensitive.

## [Requirements](vmware_tag_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere Automation SDK

## [Parameters](vmware_tag_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **hostname**  string | The hostname or IP address of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **port**  integer | The port number of the vSphere vCenter.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Default: `443` |
| **protocol**  string | The connection to protocol.  Choices:   - `"http"` - `"https"` ← (default) |
| **proxy_host**  string  added in community.vmware 1.12.0 | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead. |
| **proxy_port**  integer  added in community.vmware 1.12.0 | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid.  Set to `False` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Examples](vmware_tag_info_module.md#id4)

```yaml+jinja
- name: Get info about tag
  community.vmware.vmware_tag_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
  delegate_to: localhost

- name: Get category id from the given tag
  community.vmware.vmware_tag_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
  delegate_to: localhost
  register: tag_details
- debug:
    msg: "{{ tag_details.tag_facts['fedora_machines']['tag_category_id'] }}"

- name: Gather tag id from the given tag
  community.vmware.vmware_tag_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
  delegate_to: localhost
  register: tag_results
- set_fact:
    tag_id: "{{ item.tag_id }}"
  loop: "{{ tag_results.tag_info|json_query(query) }}"
  vars:
    query: "[?tag_name==`tag0001`]"
- debug: var=tag_id
```

## [Return Values](vmware_tag_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **tag_facts**  dictionary | dictionary of tag metadata  Returned: on success  Sample: `{"Sample_Tag_0002": {"tag_category_id": "urn:vmomi:InventoryServiceCategory:6de17f28-7694-43ec-a783-d09c141819ae:GLOBAL", "tag_description": "Sample Description", "tag_id": "urn:vmomi:InventoryServiceTag:a141f212-0f82-4f05-8eb3-c49647c904c5:GLOBAL", "tag_used_by": []}, "fedora_machines": {"tag_category_id": "urn:vmomi:InventoryServiceCategory:baa90bae-951b-4e87-af8c-be681a1ba30c:GLOBAL", "tag_description": "", "tag_id": "urn:vmomi:InventoryServiceTag:7d27d182-3ecd-4200-9d72-410cc6398a8a:GLOBAL", "tag_used_by": []}, "ubuntu_machines": {"tag_category_id": "urn:vmomi:InventoryServiceCategory:89573410-29b4-4cac-87a4-127c084f3d50:GLOBAL", "tag_description": "", "tag_id": "urn:vmomi:InventoryServiceTag:7f3516d5-a750-4cb9-8610-6747eb39965d:GLOBAL", "tag_used_by": []}}` |
| **tag_info**  list / elements=string | list of tag metadata  Returned: on success  Sample: `[{"tag_category_id": "urn:vmomi:InventoryServiceCategory:6de17f28-7694-43ec-a783-d09c141819ae:GLOBAL", "tag_description": "Sample Description", "tag_id": "urn:vmomi:InventoryServiceTag:a141f212-0f82-4f05-8eb3-c49647c904c5:GLOBAL", "tag_name": "Sample_Tag_0002", "tag_used_by": []}, {"tag_category_id": "urn:vmomi:InventoryServiceCategory:6de17f28-7694-43ec-a783-d09c141819ae:GLOBAL", "tag_description": "", "tag_id": "urn:vmomi:InventoryServiceTag:7d27d182-3ecd-4200-9d72-410cc6398a8a:GLOBAL", "tag_name": "Sample_Tag_0002", "tag_used_by": []}, {"tag_category_id": "urn:vmomi:InventoryServiceCategory:89573410-29b4-4cac-87a4-127c084f3d50:GLOBAL", "tag_description": "", "tag_id": "urn:vmomi:InventoryServiceTag:7f3516d5-a750-4cb9-8610-6747eb39965d:GLOBAL", "tag_name": "ubuntu_machines", "tag_used_by": []}]` |

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
