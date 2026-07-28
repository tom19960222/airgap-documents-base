---
collection: ansible
version: "6"
title: "community.vmware.vmware_vm_storage_policy_info module – Gather information about vSphere storage profile defined storage policy information."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_vm_storage_policy_info_module.html
fetched_at: 2026-07-27T17:22:56+00:00
---
# community.vmware.vmware_vm_storage_policy_info module – Gather information about vSphere storage profile defined storage policy information.

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
> To use it in a playbook, specify: `community.vmware.vmware_vm_storage_policy_info`.

- [Synopsis](vmware_vm_storage_policy_info_module.md#synopsis)
- [Parameters](vmware_vm_storage_policy_info_module.md#parameters)
- [Notes](vmware_vm_storage_policy_info_module.md#notes)
- [Examples](vmware_vm_storage_policy_info_module.md#examples)
- [Return Values](vmware_vm_storage_policy_info_module.md#return-values)

## [Synopsis](vmware_vm_storage_policy_info_module.md#id1)

- Returns basic information on vSphere storage profiles.
- A vSphere storage profile defines storage policy information that describes storage requirements for virtual machines and storage capabilities of storage providers.

## [Parameters](vmware_vm_storage_policy_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_vm_storage_policy_info_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_vm_storage_policy_info_module.md#id4)

```yaml+jinja
- name: Get SPBM info
  community.vmware.vmware_vm_storage_policy_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
  delegate_to: localhost
  register: profiles
```

## [Return Values](vmware_vm_storage_policy_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **spbm_profiles**  list / elements=string | list of dictionary of SPBM info  Returned: success  Sample: `[{"constraints_sub_profiles": [{"rule_set_info": [{"id": "hostFailuresToTolerate", "value": 1}, {"id": "stripeWidth", "value": 1}, {"id": "forceProvisioning", "value": false}, {"id": "proportionalCapacity", "value": 0}, {"id": "cacheReservation", "value": 0}], "rule_set_name": "VSAN sub-profile"}], "description": "Storage policy used as default for vSAN datastores", "id": "aa6d5a82-1c88-45da-85d3-3d74b91a5bad", "name": "vSAN Default Storage Policy"}]` |

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
