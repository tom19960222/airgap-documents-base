---
collection: ansible
version: "8"
title: "community.vmware.vmware_custom_attribute_manager module – Manage custom attributes from VMware for the given vSphere object"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_custom_attribute_manager_module.html
fetched_at: 2026-07-28T01:59:45+00:00
---
# community.vmware.vmware_custom_attribute_manager module – Manage custom attributes from VMware for the given vSphere object

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
> To use it in a playbook, specify: `community.vmware.vmware_custom_attribute_manager`.

New in community.vmware 3.2.0

- [Synopsis](vmware_custom_attribute_manager_module.md#synopsis)
- [Parameters](vmware_custom_attribute_manager_module.md#parameters)
- [Notes](vmware_custom_attribute_manager_module.md#notes)
- [Examples](vmware_custom_attribute_manager_module.md#examples)

## [Synopsis](vmware_custom_attribute_manager_module.md#id1)

- This module can be used to add, remove and update custom attributes for the given vSphere object.

## [Parameters](vmware_custom_attribute_manager_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **custom_attributes**  list / elements=dictionary / required | A list of name and value of custom attributes that needs to be manage.  Value of custom attribute is not required and will be ignored, if `state` is set to `absent`. |
| **name**  string / required | Name of the attribute. |
| **value**  string | Value of the attribute.  **Default:** `""` |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **object_name**  string / required | Name of the vSphere object to work with. |
| **object_type**  string / required | Type of the object the custom attribute is associated with.  **Choices:**   - `"Cluster"` - `"Datacenter"` - `"Datastore"` - `"DistributedVirtualPortgroup"` - `"DistributedVirtualSwitch"` - `"Folder"` - `"HostSystem"` - `"ResourcePool"` - `"VirtualMachine"` |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | If set to `present`, the custom attribute is set to the given value.  If set to `absent`, the custom attribute is cleared. The given value is ignored in this case.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_custom_attribute_manager_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_custom_attribute_manager_module.md#id4)

```yaml+jinja
- name: Add virtual machine custom attributes
  community.vmware.vmware_custom_attribute_manager:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    object_name: vm1
    object_type: VirtualMachine
    state: present
    custom_attributes:
      - name: MyAttribute
        value: MyValue
  delegate_to: localhost

- name: Add multiple virtual machine custom attributes
  community.vmware.vmware_custom_attribute_manager:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    object_name: vm1
    object_type: VirtualMachine
    state: present
    custom_attributes:
      - name: MyAttribute
        value: MyValue
      - name: MyAttribute2
        value: MyValue2
  delegate_to: localhost

- name: Remove virtual machine Attribute
  community.vmware.vmware_custom_attribute_manager:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    object_name: vm1
    object_type: VirtualMachine
    state: absent
    custom_attributes:
      - name: MyAttribute
  delegate_to: localhost
  register: attributes
```

### Authors

- Mario Lenz (@mariolenz)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
