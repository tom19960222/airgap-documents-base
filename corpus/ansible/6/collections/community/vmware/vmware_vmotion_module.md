---
collection: ansible
version: "6"
title: "community.vmware.vmware_vmotion module – Move a virtual machine using vMotion, and/or its vmdks using storage vMotion."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_vmotion_module.html
fetched_at: 2026-07-27T17:23:00+00:00
---
# community.vmware.vmware_vmotion module – Move a virtual machine using vMotion, and/or its vmdks using storage vMotion.

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
> To use it in a playbook, specify: `community.vmware.vmware_vmotion`.

- [Synopsis](vmware_vmotion_module.md#synopsis)
- [Parameters](vmware_vmotion_module.md#parameters)
- [Notes](vmware_vmotion_module.md#notes)
- [Examples](vmware_vmotion_module.md#examples)
- [Return Values](vmware_vmotion_module.md#return-values)

## [Synopsis](vmware_vmotion_module.md#id1)

- Using VMware vCenter, move a virtual machine using vMotion to a different host, and/or its vmdks to another datastore using storage vMotion.

## [Parameters](vmware_vmotion_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **destination_cluster**  string  added in community.vmware 2.5.0 | Name of the destination cluster the virtual machine should be running on.  Only works if drs is enabled for this cluster. |
| **destination_datacenter**  string  added in community.vmware 1.11.0 | Name of the destination datacenter the datastore is located on.  Optional, required only when datastores are shared across datacenters. |
| **destination_datastore**  aliases: datastore  string | Name of the destination datastore the virtual machine’s vmdk should be moved on. |
| **destination_datastore_cluster**  string  added in community.vmware 2.5.0 | Name of the destination datastore cluster (storage pod) the virtual machine’s vmdk should be moved on.  Only works if drs is enabled for the cluster the vm is running / should run. |
| **destination_host**  aliases: destination  string | Name of the destination host the virtual machine should be running on.  Version 2.6 onwards, this parameter is not a required parameter, unlike the previous versions. |
| **destination_resourcepool**  aliases: resource_pool  string | Name of the destination resource pool where the virtual machine should be running.  Resource pool is required if vmotion is done between hosts which are part of different clusters or datacenters.  if not passed, resource_pool object will be retrived from host_obj parent. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **moid**  string | Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.  This is required if `vm_name` or `vm_uuid` is not supplied. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **use_instance_uuid**  boolean | Whether to use the VMware instance UUID rather than the BIOS UUID.  Choices:   - `false` ← (default) - `true` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |
| **vm_name**  aliases: vm  string | Name of the VM to perform a vMotion on.  This is required parameter, if `vm_uuid` is not set.  Version 2.6 onwards, this parameter is not a required parameter, unlike the previous versions. |
| **vm_uuid**  aliases: uuid  string | UUID of the virtual machine to perform a vMotion operation on.  This is a required parameter, if `vm_name` or `moid` is not set. |

## [Notes](vmware_vmotion_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_vmotion_module.md#id4)

```yaml+jinja
- name: Perform vMotion of virtual machine
  community.vmware.vmware_vmotion:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    vm_name: 'vm_name_as_per_vcenter'
    destination_host: 'destination_host_as_per_vcenter'
  delegate_to: localhost

- name: Perform vMotion of virtual machine
  community.vmware.vmware_vmotion:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    moid: vm-42
    destination_host: 'destination_host_as_per_vcenter'
  delegate_to: localhost

- name: Perform vMotion of virtual machine to resource_pool
  community.vmware.vmware_vmotion:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    moid: vm-42
    destination_host: 'destination_host_as_per_vcenter'
    destination_resourcepool: 'destination_resourcepool_as_per_vcenter'
  delegate_to: localhost

- name: Perform storage vMotion of virtual machine
  community.vmware.vmware_vmotion:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    vm_name: 'vm_name_as_per_vcenter'
    destination_datastore: 'destination_datastore_as_per_vcenter'
  delegate_to: localhost

- name: Perform storage vMotion and host vMotion of virtual machine
  community.vmware.vmware_vmotion:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    vm_name: 'vm_name_as_per_vcenter'
    destination_host: 'destination_host_as_per_vcenter'
    destination_datastore: 'destination_datastore_as_per_vcenter'
  delegate_to: localhost

- name: Perform storage vMotion to a Storage Cluster and vMotion to a Cluster of virtual machine
  community.vmware.vmware_vmotion:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    vm_name: 'vm_name_as_per_vcenter'
    destination_cluster: 'destination_cluster_as_per_vcenter'
    destination_datastore_cluster: 'destination_datastore_cluster_as_per_vcenter'
  delegate_to: localhost
```

## [Return Values](vmware_vmotion_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **datastore**  string | List the datastore the virtual machine is on.  Only returned if there is asked for a Storage vMotion (Datastore or Datastore Cluster).  Returned: changed or success  Sample: `"datastore1"` |
| **running_host**  string | List the host the virtual machine is registered to.  Only returned if there is asked for a vMotion (Cluster or Host).  Returned: changed or success  Sample: `"host1.example.com"` |

### Authors

- Bede Carroll (@bedecarroll)
- Olivier Boukili (@oboukili)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
