---
collection: ansible
version: "6"
title: "hpe.nimble.hpe_nimble_volume module – Manage the HPE Nimble Storage volumes"
source_url: https://docs.ansible.com/projects/ansible/6/collections/hpe/nimble/hpe_nimble_volume_module.html
fetched_at: 2026-07-27T17:50:11+00:00
---
# hpe.nimble.hpe_nimble_volume module – Manage the HPE Nimble Storage volumes

> **Note:**
>
> This module is part of the [hpe.nimble collection](https://galaxy.ansible.com/hpe/nimble) (version 1.1.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install hpe.nimble`.
> You need further requirements to be able to use this module,
> see [Requirements](hpe_nimble_volume_module.md#ansible-collections-hpe-nimble-hpe-nimble-volume-module-requirements) for details.
>
> To use it in a playbook, specify: `hpe.nimble.hpe_nimble_volume`.

New in hpe.nimble 1.0.0

- [Synopsis](hpe_nimble_volume_module.md#synopsis)
- [Requirements](hpe_nimble_volume_module.md#requirements)
- [Parameters](hpe_nimble_volume_module.md#parameters)
- [Notes](hpe_nimble_volume_module.md#notes)
- [Examples](hpe_nimble_volume_module.md#examples)

## [Synopsis](hpe_nimble_volume_module.md#id1)

- Manage the volumes on an HPE Nimble Storage group.

## [Requirements](hpe_nimble_volume_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later
- Python 3.6 or later
- HPE Nimble Storage SDK for Python
- HPE Nimble Storage arrays running NimbleOS 5.0 or later

## [Parameters](hpe_nimble_volume_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **agent_type**  string | External management agent type.  Choices:   - `"none"` - `"smis"` - `"vvol"` - `"openstack"` - `"openstackv2"` |
| **app_uuid**  string | Application identifier of volume. |
| **block_size**  integer | Size in bytes of blocks in the volume. |
| **cache_pinned**  boolean | If set to true, all the contents of this volume are kept in flash cache.  Choices:   - `false` - `true` |
| **caching**  boolean | Indicate caching the volume is enabled.  Choices:   - `false` - `true` |
| **change_name**  string | Change name of the existing source volume. |
| **clone**  boolean | Whether this volume is a clone. Use this attribute in combination with name and snapshot to create a clone by setting clone = true.  Choices:   - `false` - `true` |
| **dedupe**  boolean | Indicate whether dedupe is enabled.  Choices:   - `false` - `true` |
| **description**  string | Text description of volume. |
| **destination**  string | Name of the destination pool where the volume is moving to. |
| **encryption_cipher**  string | The encryption cipher of the volume.  Choices:   - `"none"` - `"aes_256_xts"` |
| **folder**  string | Name of the folder holding this volume. |
| **force**  boolean | Forcibly offline, reduce size or change read-only status a volume.  Choices:   - `false` - `true` |
| **force_vvol**  boolean | Forcibly move a virtual volume.  Choices:   - `false` ← (default) - `true` |
| **host**  string / required | HPE Nimble Storage IP address. |
| **iscsi_target_scope**  string | This indicates whether volume is exported under iSCSI Group Target or iSCSI volume target. This attribute is only meaningful to iSCSI system.  Choices:   - `"volume"` - `"group"` |
| **limit**  integer | Limit on the volume’s mapped usage, expressed as a percentage of the volume’s size. |
| **limit_iops**  integer | IOPS limit for this volume. |
| **limit_mbps**  integer | Throughput limit for this volume in MB/s. |
| **metadata**  dictionary | User defined key-value pairs that augment an volume’s attributes. List of key-value pairs. Keys must be unique and non-empty. When creating an object, values must be non-empty. When updating an object, an empty value causes the corresponding key to be removed. |
| **move**  boolean | Move a volume to different pool.  Choices:   - `false` - `true` |
| **multi_initiator**  boolean | For iSCSI volume target, this flag indicates whether the volume and its snapshots can be accessed from multiple initiators at the same time.  Choices:   - `false` - `true` |
| **name**  string / required | Name of the source volume. |
| **online**  boolean | Online state of volume, available for host initiators to establish connections.  Choices:   - `false` - `true` |
| **owned_by_group**  string | Name of group that currently owns the volume. |
| **parent**  string | Name of parent volume. |
| **password**  string / required | HPE Nimble Storage password. |
| **perf_policy**  string | Name of the performance policy. After creating a volume, performance policy for the volume can only be changed to another performance policy with same block size. |
| **pool**  string | Name associated with the pool in the storage pool table. |
| **read_only**  boolean | Volume is read-only.  Choices:   - `false` - `true` |
| **size**  integer | Volume size in megabytes. Size is required for creating a volume but not for cloning an existing volume. |
| **snapshot**  string | Base snapshot name. This attribute is required together with name and clone when cloning a volume with the create operation. |
| **state**  string / required | The volume operations.  Choices:   - `"present"` - `"absent"` - `"create"` - `"restore"` |
| **thinly_provisioned**  boolean | Set volume’s provisioning level to thin.  Choices:   - `false` - `true` |
| **username**  string / required | HPE Nimble Storage user name. |
| **volcoll**  string | Name of volume collection of which this volume is a member. Use this attribute in update operation to associate or dissociate volumes with or from volume collections. When associating, set this attribute to the name of the volume collection. When dissociating, set this attribute to empty string. |

## [Notes](hpe_nimble_volume_module.md#id4)

> **Note:**
>
> - This module does not support `check_mode`.

## [Examples](hpe_nimble_volume_module.md#id5)

```yaml+jinja
# If state is "create", then create a volume if not present. Fails if already present.
# if state is present, then create a volume if not present. Succeeds if it already exists.
- name: Create volume if not present
  hpe.nimble.hpe_nimble_volume:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    state: "{{ state | default('present') }}"
    size: "{{ size }}"
    limit_iops: "{{ limit_iops }}"
    limit_mbps: 5000
    force: false
    metadata: "{{ metadata }}" # metadata = {'mykey1': 'myval1', 'mykey2': 'myval2'}
    description: "{{ description }}"
    name: "{{ name }}"

- name: Changing volume "{{ name }}" to offline state
  hpe.nimble.hpe_nimble_volume:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    online: False
    state: present
    name: "{{ name }}"

- name: Changing volume "{{ name }}" to online state
  hpe.nimble.hpe_nimble_volume:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    online: True
    state: present
    name: "{{ name }}"

# Create a clone from the given snapshot name.
# If snapshot name is not provided then a snapshot is created on the source volume.
# Clone task only run if "parent" is specified. Snapshot is optional.
- name: Create or Refresh a clone
  hpe.nimble.hpe_nimble_volume:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}" # name here is the name of cloned volume
    parent: "{{ parent | mandatory }}"
    snapshot: "{{ snapshot | default(None)}}"
    state: "{{ state | default('present') }}"
  when:
    - parent is defined

- name: Destroy volume (must be offline)
  hpe.nimble.hpe_nimble_volume:
    name: "{{ name }}"
    state: absent

# If no snapshot is given, then restore volume to last snapshot. Fails if no snapshots exist.
# If snapshot is provided, then restore volume from specified snapshot.
- name: Restore volume "{{ name }}"
  hpe.nimble.hpe_nimble_volume:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    snapshot: "{{ snapshot | default(None)}}"
    state: restore

- name: Delete volume "{{ name }}" (must be offline)
  hpe.nimble.hpe_nimble_volume:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    state: absent

- name: Move volume to pool
  hpe.nimble.hpe_nimble_volume:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    move: true
    name: "{{ name }}"
    state: present
    destination: "{{ destination | mandatory }}"
```

### Authors

- HPE Nimble Storage Ansible Team (@ar-india)

### Collection links

[Issue Tracker](https://github.com/hpe-storage/nimble-ansible-modules/issues)
[Homepage](http://hpe.com/storage/nimble)
[Repository (Sources)](https://github.com/hpe-storage/nimble-ansible-modules)
