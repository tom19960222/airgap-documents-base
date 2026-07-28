---
collection: ansible
version: "8"
title: "community.vmware.vmware_host_lockdown_exceptions module – Manage Lockdown Mode Exception Users"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_host_lockdown_exceptions_module.html
fetched_at: 2026-07-28T02:00:45+00:00
---
# community.vmware.vmware_host_lockdown_exceptions module – Manage Lockdown Mode Exception Users

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
> To use it in a playbook, specify: `community.vmware.vmware_host_lockdown_exceptions`.

New in community.vmware 3.1.0

- [Synopsis](vmware_host_lockdown_exceptions_module.md#synopsis)
- [Parameters](vmware_host_lockdown_exceptions_module.md#parameters)
- [Notes](vmware_host_lockdown_exceptions_module.md#notes)
- [Examples](vmware_host_lockdown_exceptions_module.md#examples)
- [Return Values](vmware_host_lockdown_exceptions_module.md#return-values)

## [Synopsis](vmware_host_lockdown_exceptions_module.md#id1)

- This module can be used to manage Lockdown Mode Exception Users.
- All parameters and VMware objects values are case sensitive.
- Please specify `hostname` as vCenter IP or hostname only, as lockdown operations are not possible from standalone ESXi server.

## [Parameters](vmware_host_lockdown_exceptions_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster_name**  string | Name of cluster.  All host systems from given cluster used to manage exception users.  Required parameter, if `esxi_hostname` is not set. |
| **esxi_hostname**  list / elements=string | List of ESXi hostname to manage exception users.  Required parameter, if `cluster_name` is not set. |
| **exception_users**  list / elements=string / required | List of Lockdown Mode Exception Users.  To remove all Exception Users, *state=set* the empty list. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | If `present`, make sure the given users are defined as Lockdown Mode Exception Users.  If `absent`, make sure the given users are NO Lockdown Mode Exception Users.  If `set`, will replace Lockdown Mode Exception Users defined list of users.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"set"` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_host_lockdown_exceptions_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_host_lockdown_exceptions_module.md#id4)

```yaml+jinja
- name: Remove all Lockdown Mode Exception Users on a host
  community.vmware.vmware_host_lockdown:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    exception_users: []
    state: set
  delegate_to: localhost
```

## [Return Values](vmware_host_lockdown_exceptions_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **results**  dictionary | metadata about exception users of Host systems  **Returned:** always  **Sample:** `{"host_lockdown_exceptions": {"DC0_C0": {"current_exception_users": [], "desired_exception_users": [], "previous_exception_users": ["root"]}}}` |

### Authors

- Mario Lenz (@mariolenz)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
