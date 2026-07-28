---
collection: ansible
version: "6"
title: "community.vmware.vmware_host_datastore module – Manage a datastore on ESXi host"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_host_datastore_module.html
fetched_at: 2026-07-27T17:22:15+00:00
---
# community.vmware.vmware_host_datastore module – Manage a datastore on ESXi host

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
> To use it in a playbook, specify: `community.vmware.vmware_host_datastore`.

- [Synopsis](vmware_host_datastore_module.md#synopsis)
- [Parameters](vmware_host_datastore_module.md#parameters)
- [Notes](vmware_host_datastore_module.md#notes)
- [Examples](vmware_host_datastore_module.md#examples)

## [Synopsis](vmware_host_datastore_module.md#id1)

- This module can be used to mount/umount datastore on ESXi host.
- This module only supports NFS (NFS v3 or NFS v4.1) and VMFS datastores.
- For VMFS datastore, available device must already be connected on ESXi host.
- All parameters and VMware object names are case sensitive.

## [Parameters](vmware_host_datastore_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auto_expand**  boolean  added in community.vmware 1.13.0 | Expand a datastore capacity to full if it has free capacity.  This parameter can’t be extend using another datastore.  A use case example in *auto_expand*, it can be used to expand a datastore capacity after increasing LUN volume.  Choices:   - `false` - `true` ← (default) |
| **datastore_name**  string / required | Name of the datastore to add/remove. |
| **datastore_type**  string | Type of the datastore to configure (nfs/nfs41/vmfs).  Choices:   - `"nfs"` - `"nfs41"` - `"vmfs"` |
| **esxi_hostname**  string | ESXi hostname to manage the datastore.  Required when used with a vcenter |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **nfs_path**  string | Resource path on NFS host.  Required if datastore type is set to `nfs`/`nfs41` and state is set to `present`, else unused. |
| **nfs_ro**  boolean | ReadOnly or ReadWrite mount.  Unused if datastore type is not set to `nfs`/`nfs41` and state is not set to `present`.  Choices:   - `false` ← (default) - `true` |
| **nfs_server**  string | NFS host serving nfs datastore.  Required if datastore type is set to `nfs`/`nfs41` and state is set to `present`, else unused.  Two or more servers can be defined if datastore type is set to `nfs41` |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | present: Mount datastore on host if datastore is absent else do nothing.  absent: Umount datastore if datastore is present else do nothing.  Choices:   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |
| **vmfs_device_name**  string | Name of the device to be used as VMFS datastore.  Required for VMFS datastore type and state is set to `present`, else unused. |
| **vmfs_version**  integer | VMFS version to use for datastore creation.  Unused if datastore type is not set to `vmfs` and state is not set to `present`. |

## [Notes](vmware_host_datastore_module.md#id3)

> **Note:**
>
> - Kerberos authentication with NFS v4.1 isn’t implemented
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_host_datastore_module.md#id4)

```yaml+jinja
- name: Mount VMFS datastores to ESXi
  community.vmware.vmware_host_datastore:
      hostname: '{{ vcenter_hostname }}'
      username: '{{ vcenter_username }}'
      password: '{{ vcenter_password }}'
      datastore_name: '{{ item.name }}'
      datastore_type: '{{ item.type }}'
      vmfs_device_name: 'naa.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
      vmfs_version: 6
      esxi_hostname: '{{ inventory_hostname }}'
      state: present
  delegate_to: localhost

- name: Mount NFS datastores to ESXi
  community.vmware.vmware_host_datastore:
      hostname: '{{ vcenter_hostname }}'
      username: '{{ vcenter_username }}'
      password: '{{ vcenter_password }}'
      datastore_name: '{{ item.name }}'
      datastore_type: '{{ item.type }}'
      nfs_server: '{{ item.server }}'
      nfs_path: '{{ item.path }}'
      nfs_ro: no
      esxi_hostname: '{{ inventory_hostname }}'
      state: present
  delegate_to: localhost
  loop:
      - { 'name': 'NasDS_vol01', 'server': 'nas01', 'path': '/mnt/vol01', 'type': 'nfs'}
      - { 'name': 'NasDS_vol02', 'server': 'nas01', 'path': '/mnt/vol02', 'type': 'nfs'}

- name: Mount NFS v4.1 datastores to ESXi
  community.vmware.vmware_host_datastore:
      hostname: '{{ vcenter_hostname }}'
      username: '{{ vcenter_username }}'
      password: '{{ vcenter_password }}'
      datastore_name: '{{ item.name }}'
      datastore_type: '{{ item.type }}'
      nfs_server: '{{ item.server }}'
      nfs_path: '{{ item.path }}'
      nfs_ro: no
      esxi_hostname: '{{ inventory_hostname }}'
      state: present
  delegate_to: localhost
  loop:
      - { 'name': 'NasDS_vol03', 'server': 'nas01,nas02', 'path': '/mnt/vol01', 'type': 'nfs41'}
      - { 'name': 'NasDS_vol04', 'server': 'nas01,nas02', 'path': '/mnt/vol02', 'type': 'nfs41'}

- name: Remove/Umount Datastores from a ESXi
  community.vmware.vmware_host_datastore:
      hostname: '{{ esxi_hostname }}'
      username: '{{ esxi_username }}'
      password: '{{ esxi_password }}'
      datastore_name: NasDS_vol01
      state: absent
  delegate_to: localhost
```

### Authors

- Ludovic Rivallain (@lrivallain)
- Christian Kotte (@ckotte)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
