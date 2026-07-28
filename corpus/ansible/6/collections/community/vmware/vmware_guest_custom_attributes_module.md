---
collection: ansible
version: "6"
title: "community.vmware.vmware_guest_custom_attributes module – Manage custom attributes from VMware for the given virtual machine"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_guest_custom_attributes_module.html
fetched_at: 2026-07-27T17:21:53+00:00
---
# community.vmware.vmware_guest_custom_attributes module – Manage custom attributes from VMware for the given virtual machine

> **Note:**
>
> This module is part of the [community.vmware collection](https://galaxy.ansible.com/community/vmware) (version 2.10.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
>
> To use it in a playbook, specify: `community.vmware.vmware_guest_custom_attributes`.

- [Synopsis](vmware_guest_custom_attributes_module.md#synopsis)
- [Parameters](vmware_guest_custom_attributes_module.md#parameters)
- [Notes](vmware_guest_custom_attributes_module.md#notes)
- [Examples](vmware_guest_custom_attributes_module.md#examples)
- [Return Values](vmware_guest_custom_attributes_module.md#return-values)

## [Synopsis](vmware_guest_custom_attributes_module.md#id1)

- This module can be used to add, remove and update custom attributes for the given virtual machine.

## [Parameters](vmware_guest_custom_attributes_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **attributes**  list / elements=dictionary | A list of name and value of custom attributes that needs to be manage.  Value of custom attribute is not required and will be ignored, if `state` is set to `absent`.  Default: `[]` |
| **name**  string / required | Name of the attribute. |
| **value**  string | Value of the attribute.  Default: `""` |
| **datacenter**  string | Datacenter name where the virtual machine is located in. |
| **folder**  string | Absolute path to find an existing guest.  This is required parameter, if `name` is supplied and multiple virtual machines with same name are found. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **moid**  string | Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.  This is required if `name` or `uuid` is not supplied. |
| **name**  string | Name of the virtual machine to work with.  This is required parameter, if `uuid` or `moid` is not supplied. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | The action to take.  If set to `present`, then custom attribute is added or updated.  If set to `absent`, then custom attribute is removed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **use_instance_uuid**  boolean | Whether to use the VMware instance UUID rather than the BIOS UUID.  Choices:   - `false` ← (default) - `true` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **uuid**  string | UUID of the virtual machine to manage if known. This is VMware’s unique identifier.  This is required parameter, if `name` or `moid` is not supplied. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_guest_custom_attributes_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_guest_custom_attributes_module.md#id4)

```yaml+jinja
- name: Add virtual machine custom attributes
  community.vmware.vmware_guest_custom_attributes:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    uuid: 421e4592-c069-924d-ce20-7e7533fab926
    state: present
    attributes:
      - name: MyAttribute
        value: MyValue
  delegate_to: localhost
  register: attributes

- name: Add multiple virtual machine custom attributes
  community.vmware.vmware_guest_custom_attributes:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    uuid: 421e4592-c069-924d-ce20-7e7533fab926
    state: present
    attributes:
      - name: MyAttribute
        value: MyValue
      - name: MyAttribute2
        value: MyValue2
  delegate_to: localhost
  register: attributes

- name: Remove virtual machine Attribute
  community.vmware.vmware_guest_custom_attributes:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    uuid: 421e4592-c069-924d-ce20-7e7533fab926
    state: absent
    attributes:
      - name: MyAttribute
  delegate_to: localhost
  register: attributes

- name: Remove virtual machine Attribute using Virtual Machine MoID
  community.vmware.vmware_guest_custom_attributes:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    moid: vm-42
    state: absent
    attributes:
      - name: MyAttribute
  delegate_to: localhost
  register: attributes
```

## [Return Values](vmware_guest_custom_attributes_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **custom_attributes**  dictionary | metadata about the virtual machine attributes  Returned: always  Sample: `{"mycustom": "my_custom_value", "mycustom_2": "my_custom_value_2", "sample_1": "sample_1_value", "sample_2": "sample_2_value", "sample_3": "sample_3_value"}` |

### Authors

- Jimmy Conner (@cigamit)
- Abhijeet Kasurde (@Akasurde)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
