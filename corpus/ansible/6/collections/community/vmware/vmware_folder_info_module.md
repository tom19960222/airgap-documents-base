---
collection: ansible
version: "6"
title: "community.vmware.vmware_folder_info module – Provides information about folders in a datacenter"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_folder_info_module.html
fetched_at: 2026-07-27T17:21:48+00:00
---
# community.vmware.vmware_folder_info module – Provides information about folders in a datacenter

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
> To use it in a playbook, specify: `community.vmware.vmware_folder_info`.

- [Synopsis](vmware_folder_info_module.md#synopsis)
- [Parameters](vmware_folder_info_module.md#parameters)
- [Notes](vmware_folder_info_module.md#notes)
- [Examples](vmware_folder_info_module.md#examples)
- [Return Values](vmware_folder_info_module.md#return-values)

## [Synopsis](vmware_folder_info_module.md#id1)

- The module can be used to gather a hierarchical view of the folders that exist within a datacenter

## [Parameters](vmware_folder_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **datacenter**  aliases: datacenter_name  string / required | Name of the datacenter. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_folder_info_module.md#id3)

> **Note:**
>
> - `flat_folder_info` added in VMware collection 1.4.0.
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_folder_info_module.md#id4)

```yaml+jinja
- name: Provide information about vCenter folders
  community.vmware.vmware_folder_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: datacenter_name
  delegate_to: localhost
  register: vcenter_folder_info

- name: Get information about folders
  community.vmware.vmware_folder_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: 'Asia-Datacenter1'
  register: r

- name: Set Managed object ID for the given folder
  ansible.builtin.set_fact:
    folder_mo_id: "{{ (r.flat_folder_info | selectattr('path', 'equalto', '/Asia-Datacenter1/vm/tier1/tier2') | map(attribute='moid'))[0] }}"
```

## [Return Values](vmware_folder_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **flat_folder_info**  list / elements=string | list of dict about folders in flat structure  Returned: success  Sample: `[{"moid": "group-v3", "path": "/Asia-Datacenter1/vm"}, {"moid": "group-v44", "path": "/Asia-Datacenter1/vm/tier1"}, {"moid": "group-v45", "path": "/Asia-Datacenter1/vm/tier1/tier2"}]` |
| **folder_info**  dictionary | dict about folders  Returned: success  Sample: `{"datastoreFolders": {"moid": "group-v10", "path": "/DC01/datastore", "subfolders": {"Local Datastores": {"path": "/DC01/datastore/Local Datastores", "subfolders": {}}}}, "hostFolders": {"moid": "group-v21", "path": "/DC01/host", "subfolders": {}}, "networkFolders": {"moid": "group-v31", "path": "/DC01/network", "subfolders": {}}, "vmFolders": {"moid": "group-v41", "path": "/DC01/vm", "subfolders": {"Core Infrastructure Servers": {"moid": "group-v42", "path": "/DC01/vm/Core Infrastructure Servers", "subfolders": {"Staging Network Services": {"moid": "group-v43", "path": "/DC01/vm/Core Infrastructure Servers/Staging Network Services", "subfolders": {}}, "VMware": {"moid": "group-v44", "path": "/DC01/vm/Core Infrastructure Servers/VMware", "subfolders": {}}}}}}}` |

### Authors

- David Hewitt (@davidmhewitt)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
