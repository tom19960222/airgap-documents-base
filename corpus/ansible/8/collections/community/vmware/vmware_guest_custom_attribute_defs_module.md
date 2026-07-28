---
collection: ansible
version: "8"
title: "community.vmware.vmware_guest_custom_attribute_defs module – Manage custom attributes definitions for virtual machine from VMware"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_guest_custom_attribute_defs_module.html
fetched_at: 2026-07-28T02:00:09+00:00
---
# community.vmware.vmware_guest_custom_attribute_defs module – Manage custom attributes definitions for virtual machine from VMware

> **Note:**
>
> This module is part of the [community.vmware collection](https://galaxy.ansible.com/ui/repo/published/community/vmware/) (version 3.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
>
> To use it in a playbook, specify: `community.vmware.vmware_guest_custom_attribute_defs`.

- [Synopsis](vmware_guest_custom_attribute_defs_module.md#synopsis)
- [Parameters](vmware_guest_custom_attribute_defs_module.md#parameters)
- [Notes](vmware_guest_custom_attribute_defs_module.md#notes)
- [Examples](vmware_guest_custom_attribute_defs_module.md#examples)
- [Return Values](vmware_guest_custom_attribute_defs_module.md#return-values)

## [Synopsis](vmware_guest_custom_attribute_defs_module.md#id1)

- This module can be used to add and remove custom attributes definitions for the given virtual machine from VMware.

## [Parameters](vmware_guest_custom_attribute_defs_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **attribute_key**  string | Name of the custom attribute definition.  This is required parameter, if `state` is set to `present` or `absent`. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | Manage definition of custom attributes.  If set to `present` and definition not present, then custom attribute definition is created.  If set to `present` and definition is present, then no action taken.  If set to `absent` and definition is present, then custom attribute definition is removed.  If set to `absent` and definition is absent, then no action taken.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_guest_custom_attribute_defs_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_guest_custom_attribute_defs_module.md#id4)

```yaml+jinja
- name: Add VMware Attribute Definition
  community.vmware.vmware_guest_custom_attribute_defs:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    state: present
    attribute_key: custom_attr_def_1
  delegate_to: localhost
  register: defs

- name: Remove VMware Attribute Definition
  community.vmware.vmware_guest_custom_attribute_defs:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    state: absent
    attribute_key: custom_attr_def_1
  delegate_to: localhost
  register: defs
```

## [Return Values](vmware_guest_custom_attribute_defs_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **custom_attribute_defs**  list / elements=string | list of all current attribute definitions  **Returned:** always  **Sample:** `["sample_5", "sample_4"]` |

### Authors

- Jimmy Conner (@cigamit)
- Abhijeet Kasurde (@Akasurde)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
