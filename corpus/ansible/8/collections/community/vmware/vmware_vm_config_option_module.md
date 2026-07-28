---
collection: ansible
version: "8"
title: "community.vmware.vmware_vm_config_option module – Return supported guest ID list and VM recommended config option for specific guest OS"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_vm_config_option_module.html
fetched_at: 2026-07-28T02:01:18+00:00
---
# community.vmware.vmware_vm_config_option module – Return supported guest ID list and VM recommended config option for specific guest OS

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
> To use it in a playbook, specify: `community.vmware.vmware_vm_config_option`.

- [Synopsis](vmware_vm_config_option_module.md#synopsis)
- [Parameters](vmware_vm_config_option_module.md#parameters)
- [Notes](vmware_vm_config_option_module.md#notes)
- [Examples](vmware_vm_config_option_module.md#examples)
- [Return Values](vmware_vm_config_option_module.md#return-values)

## [Synopsis](vmware_vm_config_option_module.md#id1)

- This module is used for getting the hardware versions supported for creation, the guest ID list supported by ESXi host for the most recent virtual hardware supported or specified hardware version, the VM recommended config options for specified guest OS ID.

## [Parameters](vmware_vm_config_option_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster_name**  string | Name of the cluster.  If `esxi_hostname` is not given, this parameter is required. |
| **datacenter**  string | The datacenter name used to get specified cluster or host.  This parameter is case sensitive.  **Default:** `"ha-datacenter"` |
| **esxi_hostname**  string | ESXi hostname.  Obtain VM configure options on this ESXi host.  If `cluster_name` is not given, this parameter is required. |
| **get_config_options**  boolean | Return the dict of VM recommended config options for guest ID specified by `guest_id` with hardware version specified by `hardware_version` or the default hardware version.  When set to True, `guest_id` must be set.  **Choices:**   - `false` ← (default) - `true` |
| **get_guest_os_ids**  boolean | Return the list of guest OS IDs supported on the specified entity.  If `hardware_version` is set, will return the corresponding guest OS ID list supported, or will return the guest OS ID list for the default hardware version.  **Choices:**   - `false` ← (default) - `true` |
| **get_hardware_versions**  boolean | Return the list of VM hardware versions supported for creation and the default hardware version on the specified entity.  **Choices:**   - `false` ← (default) - `true` |
| **guest_id**  string | The guest OS ID from the returned list when `get_guest_os_ids` is set to `true`, e.g., ‘rhel8_64Guest’.  This parameter must be set when `get_config_options` is set to `true`. |
| **hardware_version**  string | The hardware version from the returned list when `get_hardware_versions` is set to `true`, e.g., ‘vmx-19’. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_vm_config_option_module.md#id3)

> **Note:**
>
> - Known issue on vSphere 7.0 (<https://github.com/vmware/pyvmomi/issues/915>)
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_vm_config_option_module.md#id4)

```yaml+jinja
- name: Get supported guest ID list on given ESXi host for with default hardware version
  community.vmware.vmware_vm_config_option:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi_hostname }}"
    get_guest_os_ids: true
  delegate_to: localhost

- name: Get VM recommended config option for Windows 10 guest OS on given ESXi host
  community.vmware.vmware_vm_config_option:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi_hostname }}"
    get_config_options: true
    guest_id: "windows9_64Guest"
  delegate_to: localhost
```

## [Return Values](vmware_vm_config_option_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **instance**  dictionary | metadata about the VM recommended configuration  **Returned:** always  **Sample:** `"None"` |

### Authors

- Diane Wang (@Tomorrow9)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
