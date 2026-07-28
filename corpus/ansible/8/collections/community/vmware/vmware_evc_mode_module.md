---
collection: ansible
version: "8"
title: "community.vmware.vmware_evc_mode module – Enable/Disable EVC mode on vCenter"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_evc_mode_module.html
fetched_at: 2026-07-28T02:00:02+00:00
---
# community.vmware.vmware_evc_mode module – Enable/Disable EVC mode on vCenter

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
> To use it in a playbook, specify: `community.vmware.vmware_evc_mode`.

- [Synopsis](vmware_evc_mode_module.md#synopsis)
- [Parameters](vmware_evc_mode_module.md#parameters)
- [Notes](vmware_evc_mode_module.md#notes)
- [Examples](vmware_evc_mode_module.md#examples)
- [Return Values](vmware_evc_mode_module.md#return-values)

## [Synopsis](vmware_evc_mode_module.md#id1)

- This module can be used to enable/disable EVC mode on vCenter.

## [Parameters](vmware_evc_mode_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster_name**  aliases: cluster  string / required | The name of the cluster to enable or disable EVC mode on. |
| **datacenter_name**  aliases: datacenter  string / required | The name of the datacenter the cluster belongs to that you want to enable or disable EVC mode on. |
| **evc_mode**  string | Required for `state=present`.  The EVC mode to enable or disable on the cluster. (intel-broadwell, intel-nehalem, intel-merom, etc.). |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | Add or remove EVC mode.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_evc_mode_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_evc_mode_module.md#id4)

```yaml+jinja
- name: Enable EVC Mode
  community.vmware.vmware_evc_mode:
     hostname: "{{ groups['vcsa'][0] }}"
     username: "{{ vcenter_username }}"
     password: "{{ site_password }}"
     datacenter_name: "{{ datacenter_name }}"
     cluster_name: "{{ cluster_name }}"
     evc_mode: "intel-broadwell"
     state: present
  delegate_to: localhost
  register: enable_evc

- name: Disable EVC Mode
  community.vmware.vmware_evc_mode:
     hostname: "{{ groups['vcsa'][0] }}"
     username: "{{ vcenter_username }}"
     password: "{{ site_password }}"
     datacenter_name: "{{ datacenter_name }}"
     cluster_name: "{{ cluster_name }}"
     state: absent
  delegate_to: localhost
  register: disable_evc
```

## [Return Values](vmware_evc_mode_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  string | information about performed operation  **Returned:** always  **Sample:** `"EVC Mode for 'intel-broadwell' has been enabled."` |

### Authors

- Michael Tipton (@castawayegr)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
