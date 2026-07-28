---
collection: ansible
version: "6"
title: "community.vmware.vmware_datastore_cluster module – Manage VMware vSphere datastore clusters"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_datastore_cluster_module.html
fetched_at: 2026-07-27T17:21:32+00:00
---
# community.vmware.vmware_datastore_cluster module – Manage VMware vSphere datastore clusters

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
> To use it in a playbook, specify: `community.vmware.vmware_datastore_cluster`.

- [Synopsis](vmware_datastore_cluster_module.md#synopsis)
- [Parameters](vmware_datastore_cluster_module.md#parameters)
- [Notes](vmware_datastore_cluster_module.md#notes)
- [Examples](vmware_datastore_cluster_module.md#examples)
- [Return Values](vmware_datastore_cluster_module.md#return-values)

## [Synopsis](vmware_datastore_cluster_module.md#id1)

- This module can be used to add and delete datastore cluster in given VMware environment.
- All parameters and VMware object values are case sensitive.

## [Parameters](vmware_datastore_cluster_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **automation_level**  string | Run SDRS automated or manually.  Choices:   - `"automated"` - `"manual"` ← (default) |
| **datacenter_name**  aliases: datacenter  string | The name of the datacenter.  You must specify either a `datacenter_name` or a `folder`.  Mutually exclusive with `folder` parameter. |
| **datastore_cluster_name**  string / required | The name of the datastore cluster. |
| **enable_io_loadbalance**  boolean | Whether or not storage DRS takes into account storage I/O workload when making load balancing and initial placement recommendations.  Choices:   - `false` ← (default) - `true` |
| **enable_sdrs**  boolean | Whether or not storage DRS is enabled.  Choices:   - `false` ← (default) - `true` |
| **folder**  string | Destination folder, absolute path to place datastore cluster in.  The folder should include the datacenter.  This parameter is case sensitive.  You must specify either a `folder` or a `datacenter_name`.  Examples:  folder: /datacenter1/datastore  folder: datacenter1/datastore  folder: /datacenter1/datastore/folder1  folder: datacenter1/datastore/folder1  folder: /folder1/datacenter1/datastore  folder: folder1/datacenter1/datastore  folder: /folder1/datacenter1/datastore/folder2 |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **keep_vmdks_together**  boolean | Specifies whether or not each VM in this datastore cluster should have its virtual disks on the same datastore by default.  Choices:   - `false` - `true` ← (default) |
| **loadbalance_interval**  integer | Specify the interval in minutes that storage DRS runs to load balance among datastores.  Default: `480` |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | If the datastore cluster should be present or absent.  Choices:   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_datastore_cluster_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_datastore_cluster_module.md#id4)

```yaml+jinja
- name: Create datastore cluster and enable SDRS
  community.vmware.vmware_datastore_cluster:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: '{{ datacenter_name }}'
    datastore_cluster_name: '{{ datastore_cluster_name }}'
    enable_sdrs: True
    state: present
  delegate_to: localhost

- name: Create datastore cluster using folder
  community.vmware.vmware_datastore_cluster:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    folder: '/{{ datacenter_name }}/datastore/ds_folder'
    datastore_cluster_name: '{{ datastore_cluster_name }}'
    state: present
  delegate_to: localhost

- name: Delete datastore cluster
  community.vmware.vmware_datastore_cluster:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: '{{ datacenter_name }}'
    datastore_cluster_name: '{{ datastore_cluster_name }}'
    state: absent
  delegate_to: localhost
```

## [Return Values](vmware_datastore_cluster_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  string | information about datastore cluster operation  Returned: always  Sample: `"Datastore cluster 'DSC2' created successfully."` |

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
