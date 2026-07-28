---
collection: ansible
version: "6"
title: "community.vmware.vmware_guest_snapshot module – Manages virtual machines snapshots in vCenter"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_guest_snapshot_module.html
fetched_at: 2026-07-27T17:22:03+00:00
---
# community.vmware.vmware_guest_snapshot module – Manages virtual machines snapshots in vCenter

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
> To use it in a playbook, specify: `community.vmware.vmware_guest_snapshot`.

- [Synopsis](vmware_guest_snapshot_module.md#synopsis)
- [Parameters](vmware_guest_snapshot_module.md#parameters)
- [Notes](vmware_guest_snapshot_module.md#notes)
- [Examples](vmware_guest_snapshot_module.md#examples)
- [Return Values](vmware_guest_snapshot_module.md#return-values)

## [Synopsis](vmware_guest_snapshot_module.md#id1)

- This module can be used to create, delete and update snapshot(s) of the given virtual machine.
- All parameters and VMware object names are case sensitive.

## [Parameters](vmware_guest_snapshot_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **datacenter**  string / required | Destination datacenter for the deploy operation. |
| **description**  string | Define an arbitrary description to attach to snapshot.  Default: `""` |
| **folder**  string | Destination folder, absolute or relative path to find an existing guest.  This is required parameter, if `name` is supplied.  The folder should include the datacenter. ESX’s datacenter is ha-datacenter.  Examples:  folder: /ha-datacenter/vm  folder: ha-datacenter/vm  folder: /datacenter1/vm  folder: datacenter1/vm  folder: /datacenter1/vm/folder1  folder: datacenter1/vm/folder1  folder: /folder1/datacenter1/vm  folder: folder1/datacenter1/vm  folder: /folder1/datacenter1/vm/folder2 |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **memory_dump**  boolean | If set to `true`, memory dump of virtual machine is also included in snapshot.  Note that memory snapshots take time and resources, this will take longer time to create.  If virtual machine does not provide capability to take memory snapshot, then this flag is set to `false`.  Choices:   - `false` ← (default) - `true` |
| **moid**  string | Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.  This is required if `name` or `uuid` is not supplied. |
| **name**  string | Name of the virtual machine to work with.  This is required parameter, if `uuid` or `moid` is not supplied. |
| **name_match**  string | If multiple VMs matching the name, use the first or last found.  Choices:   - `"first"` ← (default) - `"last"` |
| **new_description**  string | Value to change the description of an existing snapshot to. |
| **new_snapshot_name**  string | Value to rename the existing snapshot to. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **quiesce**  boolean | If set to `true` and virtual machine is powered on, it will quiesce the file system in virtual machine.  Note that VMware Tools are required for this flag.  If virtual machine is powered off or VMware Tools are not available, then this flag is set to `false`.  If virtual machine does not provide capability to take quiesce snapshot, then this flag is set to `false`.  Choices:   - `false` ← (default) - `true` |
| **remove_children**  boolean | If set to `true` and state is set to `absent`, then entire snapshot subtree is set for removal.  Choices:   - `false` ← (default) - `true` |
| **snapshot_name**  string | Sets the snapshot name to manage.  This param is required only if state is not `remove_all` |
| **state**  string | Manage snapshot(s) attached to a specific virtual machine.  If set to `present` and snapshot absent, then will create a new snapshot with the given name.  If set to `present` and snapshot present, then no changes are made.  If set to `absent` and snapshot present, then snapshot with the given name is removed.  If set to `absent` and snapshot absent, then no changes are made.  If set to `revert` and snapshot present, then virtual machine state is reverted to the given snapshot.  If set to `revert` and snapshot absent, then no changes are made.  If set to `remove_all` and snapshot(s) present, then all snapshot(s) will be removed.  If set to `remove_all` and snapshot(s) absent, then no changes are made.  Choices:   - `"present"` ← (default) - `"absent"` - `"revert"` - `"remove_all"` |
| **use_instance_uuid**  boolean | Whether to use the VMware instance UUID rather than the BIOS UUID.  Choices:   - `false` ← (default) - `true` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **uuid**  string | UUID of the instance to manage if known, this is VMware’s BIOS UUID by default.  This is required if `name` or `moid` parameter is not supplied. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_guest_snapshot_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_guest_snapshot_module.md#id4)

```yaml+jinja
- name: Create a snapshot
  community.vmware.vmware_guest_snapshot:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    folder: "/{{ datacenter_name }}/vm/"
    name: "{{ guest_name }}"
    state: present
    snapshot_name: snap1
    description: snap1_description
  delegate_to: localhost

- name: Remove a snapshot
  community.vmware.vmware_guest_snapshot:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    folder: "/{{ datacenter_name }}/vm/"
    name: "{{ guest_name }}"
    state: absent
    snapshot_name: snap1
  delegate_to: localhost

- name: Revert to a snapshot
  community.vmware.vmware_guest_snapshot:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    folder: "/{{ datacenter_name }}/vm/"
    name: "{{ guest_name }}"
    state: revert
    snapshot_name: snap1
  delegate_to: localhost

- name: Remove all snapshots of a VM
  community.vmware.vmware_guest_snapshot:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    folder: "/{{ datacenter_name }}/vm/"
    name: "{{ guest_name }}"
    state: remove_all
  delegate_to: localhost

- name: Remove all snapshots of a VM using MoID
  community.vmware.vmware_guest_snapshot:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    folder: "/{{ datacenter_name }}/vm/"
    moid: vm-42
    state: remove_all
  delegate_to: localhost

- name: Take snapshot of a VM using quiesce and memory flag on
  community.vmware.vmware_guest_snapshot:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    folder: "/{{ datacenter_name }}/vm/"
    name: "{{ guest_name }}"
    state: present
    snapshot_name: dummy_vm_snap_0001
    quiesce: true
    memory_dump: true
  delegate_to: localhost

- name: Remove a snapshot and snapshot subtree
  community.vmware.vmware_guest_snapshot:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    folder: "/{{ datacenter_name }}/vm/"
    name: "{{ guest_name }}"
    state: absent
    remove_children: true
    snapshot_name: snap1
  delegate_to: localhost

- name: Rename a snapshot
  community.vmware.vmware_guest_snapshot:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    folder: "/{{ datacenter_name }}/vm/"
    name: "{{ guest_name }}"
    state: present
    snapshot_name: current_snap_name
    new_snapshot_name: im_renamed
    new_description: "{{ new_snapshot_description }}"
  delegate_to: localhost
```

## [Return Values](vmware_guest_snapshot_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **snapshot_results**  dictionary | metadata about the virtual machine snapshots  Returned: always  Sample: `{"current_snapshot": {"creation_time": "2019-04-09T14:40:26.617427+00:00", "description": "Snapshot 4 example", "id": 4, "name": "snapshot4", "state": "poweredOff"}, "snapshots": [{"creation_time": "2019-04-09T14:38:24.667543+00:00", "description": "Snapshot 3 example", "id": 3, "name": "snapshot3", "state": "poweredOff"}, {"creation_time": "2019-04-09T14:40:26.617427+00:00", "description": "Snapshot 4 example", "id": 4, "name": "snapshot4", "state": "poweredOff"}]}` |

### Authors

- Loic Blot (@nerzhul)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
