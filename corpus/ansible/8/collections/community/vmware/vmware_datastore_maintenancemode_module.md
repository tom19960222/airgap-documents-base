---
collection: ansible
version: "8"
title: "community.vmware.vmware_datastore_maintenancemode module – Place a datastore into maintenance mode"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_datastore_maintenancemode_module.html
fetched_at: 2026-07-28T01:59:50+00:00
---
# community.vmware.vmware_datastore_maintenancemode module – Place a datastore into maintenance mode

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
> To use it in a playbook, specify: `community.vmware.vmware_datastore_maintenancemode`.

- [Synopsis](vmware_datastore_maintenancemode_module.md#synopsis)
- [Parameters](vmware_datastore_maintenancemode_module.md#parameters)
- [Notes](vmware_datastore_maintenancemode_module.md#notes)
- [Examples](vmware_datastore_maintenancemode_module.md#examples)
- [Return Values](vmware_datastore_maintenancemode_module.md#return-values)

## [Synopsis](vmware_datastore_maintenancemode_module.md#id1)

- This module can be used to manage maintenance mode of a datastore.

## [Parameters](vmware_datastore_maintenancemode_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster_name**  string | Name of the cluster where datastore is connected to.  If multiple datastores are connected to the given cluster, then all datastores will be managed by `state`.  If `datastore` or `datastore_cluster` are not set, this parameter is required. |
| **datastore**  string | Name of datastore to manage.  If `datastore_cluster` or `cluster_name` are not set, this parameter is required. |
| **datastore_cluster**  string | Name of the datastore cluster from all child datastores to be managed.  If `datastore` or `cluster_name` are not set, this parameter is required. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | If set to `present`, then enter datastore into maintenance mode.  If set to `present` and datastore is already in maintenance mode, then no action will be taken.  If set to `absent` and datastore is in maintenance mode, then exit maintenance mode.  If set to `absent` and datastore is not in maintenance mode, then no action will be taken.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_datastore_maintenancemode_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_datastore_maintenancemode_module.md#id4)

```yaml+jinja
- name: Enter datastore into Maintenance Mode
  community.vmware.vmware_datastore_maintenancemode:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datastore: '{{ datastore_name }}'
    state: present
  delegate_to: localhost

- name: Enter all datastores under cluster into Maintenance Mode
  community.vmware.vmware_datastore_maintenancemode:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: '{{ cluster_name }}'
    state: present
  delegate_to: localhost

- name: Enter all datastores under datastore cluster into Maintenance Mode
  community.vmware.vmware_datastore_maintenancemode:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datastore_cluster: '{{ datastore_cluster_name }}'
    state: present
  delegate_to: localhost

- name: Exit datastore into Maintenance Mode
  community.vmware.vmware_datastore_maintenancemode:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datastore: '{{ datastore_name }}'
    state: absent
  delegate_to: localhost
```

## [Return Values](vmware_datastore_maintenancemode_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **datastore_status**  dictionary | Action taken for datastore  **Returned:** always  **Sample:** `{"ds_226_01": "Datastore 'ds_226_01' is already in maintenance mode."}` |

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
