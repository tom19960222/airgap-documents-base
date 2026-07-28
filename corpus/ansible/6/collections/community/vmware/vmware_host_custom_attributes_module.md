---
collection: ansible
version: "6"
title: "community.vmware.vmware_host_custom_attributes module – Manage custom attributes from VMware for the given ESXi host"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_host_custom_attributes_module.html
fetched_at: 2026-07-27T17:22:15+00:00
---
# community.vmware.vmware_host_custom_attributes module – Manage custom attributes from VMware for the given ESXi host

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
> To use it in a playbook, specify: `community.vmware.vmware_host_custom_attributes`.

New in community.vmware 1.11.0

- [Synopsis](vmware_host_custom_attributes_module.md#synopsis)
- [Parameters](vmware_host_custom_attributes_module.md#parameters)
- [Notes](vmware_host_custom_attributes_module.md#notes)
- [Examples](vmware_host_custom_attributes_module.md#examples)
- [Return Values](vmware_host_custom_attributes_module.md#return-values)

## [Synopsis](vmware_host_custom_attributes_module.md#id1)

- This module can be used to add, remove and update custom attributes for the given ESXi host.

## [Parameters](vmware_host_custom_attributes_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **attributes**  list / elements=dictionary | A list of name and value of custom attributes that needs to be manage.  Value of custom attribute is not required and will be ignored, if `state` is set to `absent`.  Default: `[]` |
| **name**  string / required | Name of the attribute. |
| **value**  string | Value of the attribute.  Default: `""` |
| **esxi_hostname**  string / required | Name of the ESXi host to work with.  This is a required parameter |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | The action to take.  If set to `present`, then custom attribute is added or updated.  If set to `absent`, then custom attribute is removed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_host_custom_attributes_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_host_custom_attributes_module.md#id4)

```yaml+jinja
- name: Add ESXi host custom attributes
  community.vmware.vmware_host_custom_attributes:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: host1
    state: present
    attributes:
      - name: MyAttribute
        value: MyValue
  delegate_to: localhost
  register: attributes

- name: Remove ESXi host Attribute
  community.vmware.vmware_host_custom_attributes:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: host1
    state: absent
    attributes:
      - name: MyAttribute
  delegate_to: localhost
  register: attributes
```

## [Return Values](vmware_host_custom_attributes_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **custom_attributes**  dictionary | metadata about the ESXi host attributes  Returned: changed  Sample: `{"mycustom": "my_custom_value", "mycustom_2": "my_custom_value_2", "sample_1": "sample_1_value", "sample_2": "sample_2_value", "sample_3": "sample_3_value"}` |

### Authors

- Hunter Christain (@exp-hc)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
