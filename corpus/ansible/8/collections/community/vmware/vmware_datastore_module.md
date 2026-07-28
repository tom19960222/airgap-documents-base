---
collection: ansible
version: "8"
title: "community.vmware.vmware_datastore module – Configure Datastores"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_datastore_module.html
fetched_at: 2026-07-28T01:59:47+00:00
---
# community.vmware.vmware_datastore module – Configure Datastores

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
> To use it in a playbook, specify: `community.vmware.vmware_datastore`.

New in community.vmware 3.0.0

- [Synopsis](vmware_datastore_module.md#synopsis)
- [Parameters](vmware_datastore_module.md#parameters)
- [Notes](vmware_datastore_module.md#notes)
- [Examples](vmware_datastore_module.md#examples)
- [Return Values](vmware_datastore_module.md#return-values)

## [Synopsis](vmware_datastore_module.md#id1)

- Configure Storage I/O Control Settings of a Datastore.

## [Parameters](vmware_datastore_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **congestion_threshold_manual**  integer | Storage I/O congestion threshold in ms.  Only use `congestion_threshold_percentage` or `congestion_threshold_manual`.  Only valid when `storage_io_control` is `enable_io_statistics`. |
| **congestion_threshold_percentage**  integer | Storage I/O congestion threshold in percentage of peak throughput.  A value between 50% and 100%.  Recommended: 90%  Only use `congestion_threshold_percentage` or `congestion_threshold_manual`.  Only valid when `storage_io_control` is `enable_io_statistics`.  **Default:** `90` |
| **datacenter**  aliases: datacenter_name  string | Datacenter to search for the datastores. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **name**  string / required | Name of the datastore. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **statistic_collection**  boolean | Include I/O statistics for SDRS.  Only valid when `storage_io_control` is `enable_io_statistics` or `enable_statistics`.  **Choices:**   - `false` - `true` ← (default) |
| **storage_io_control**  string / required | Specify datastore typ.  **Choices:**   - `"enable_io_statistics"` - `"enable_statistics"` - `"disable"` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_datastore_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_datastore_module.md#id4)

```yaml+jinja
- name: Configure Storage I/O Control of an mounted datastore
  community.vmware.vmware_datastore_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: '{{ datacenter_name }}'
    name: datastore1
    storage_io_control: 'enable_io_statistics'
    congestion_threshold_manual: 30
    statistic_collection: true
  delegate_to: localhost
  register: info
```

## [Return Values](vmware_datastore_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  string | Information about datastore operation.  **Returned:** always  **Sample:** `"Datastore configured successfully."` |

### Authors

- Nina Loser (@Nina2244)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
