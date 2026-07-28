---
collection: ansible
version: "6"
title: "community.vmware.vmware_datastore_info module – Gather info about datastores available in given vCenter"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_datastore_info_module.html
fetched_at: 2026-07-27T17:21:33+00:00
---
# community.vmware.vmware_datastore_info module – Gather info about datastores available in given vCenter

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
> To use it in a playbook, specify: `community.vmware.vmware_datastore_info`.

- [Synopsis](vmware_datastore_info_module.md#synopsis)
- [Parameters](vmware_datastore_info_module.md#parameters)
- [Notes](vmware_datastore_info_module.md#notes)
- [Examples](vmware_datastore_info_module.md#examples)
- [Return Values](vmware_datastore_info_module.md#return-values)

## [Synopsis](vmware_datastore_info_module.md#id1)

- This module can be used to gather information about datastores in VMWare infrastructure.
- All values and VMware object names are case sensitive.

## [Parameters](vmware_datastore_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster**  string | Cluster to search for datastores.  If set, information of datastores belonging this clusters will be returned.  This parameter is required, if `datacenter` is not supplied. |
| **datacenter**  aliases: datacenter_name  string | Datacenter to search for datastores.  This parameter is required, if `cluster` is not supplied. |
| **gather_nfs_mount_info**  boolean | Gather mount information of NFS datastores.  Disabled per default because this slows down the execution if you have a lot of datastores.  Only valid when `schema` is `summary`.  Choices:   - `false` ← (default) - `true` |
| **gather_vmfs_mount_info**  boolean | Gather mount information of VMFS datastores.  Disabled per default because this slows down the execution if you have a lot of datastores.  Only valid when `schema` is `summary`.  Choices:   - `false` ← (default) - `true` |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **name**  string | Name of the datastore to match.  If set, information of specific datastores are returned. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **properties**  list / elements=string | Specify the properties to retrieve.  If not specified, all properties are retrieved (deeply).  Results are returned in a structure identical to the vsphere API.  Example:  properties: [  “name”,  “info.vmfs.ssd”,  “capability.vsanSparseSupported”,  “overallStatus”  ]  Only valid when `schema` is `vsphere`. |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **schema**  string | Specify the output schema desired.  The ‘summary’ output schema is the legacy output from the module  The ‘vsphere’ output schema is the vSphere API class definition which requires pyvmomi>6.7.1  Choices:   - `"summary"` ← (default) - `"vsphere"` |
| **show_tag**  boolean  added in community.vmware 1.16.0 | Tags related to Datastore are shown if set to `True`.  Choices:   - `false` ← (default) - `true` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_datastore_info_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_datastore_info_module.md#id4)

```yaml+jinja
- name: Gather info from standalone ESXi server having datacenter as 'ha-datacenter'
  community.vmware.vmware_datastore_info:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    datacenter_name: "ha-datacenter"
  delegate_to: localhost
  register: info

- name: Gather info from datacenter about specific datastore
  community.vmware.vmware_datastore_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: '{{ datacenter_name }}'
    name: datastore1
  delegate_to: localhost
  register: info

- name: Gather some info from a datastore using the vSphere API output schema
  community.vmware.vmware_datastore_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: '{{ datacenter_name }}'
    schema: vsphere
    properties:
      - name
      - info.vmfs.ssd
      - capability.vsanSparseSupported
      - overallStatus
  delegate_to: localhost
  register: info
```

## [Return Values](vmware_datastore_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **datastores**  list / elements=string | metadata about the available datastores  Returned: always  Sample: `[{"accessible": false, "capacity": 42681237504, "datastore_cluster": "datacluster0", "freeSpace": 39638269952, "maintenanceMode": "normal", "multipleHostAccess": false, "name": "datastore2", "provisioned": 12289211488, "type": "VMFS", "uncommitted": 9246243936, "url": "ds:///vmfs/volumes/5a69b18a-c03cd88c-36ae-5254001249ce/", "vmfs_blockSize": 1024, "vmfs_uuid": "5a69b18a-c03cd88c-36ae-5254001249ce", "vmfs_version": "6.81"}, {"accessible": true, "capacity": 5497558138880, "datastore_cluster": "datacluster0", "freeSpace": 4279000641536, "maintenanceMode": "normal", "multipleHostAccess": true, "name": "datastore3", "nfs_path": "/vol/datastore3", "nfs_server": "nfs_server1", "provisioned": 1708109410304, "type": "NFS", "uncommitted": 489551912960, "url": "ds:///vmfs/volumes/420b3e73-67070776/"}]` |

### Authors

- Tim Rightnour (@garbled1)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
