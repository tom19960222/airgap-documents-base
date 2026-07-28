---
collection: ansible
version: "6"
title: "infinidat.infinibox.infini_vol module – Create, Delete or Modify volumes on Infinibox"
source_url: https://docs.ansible.com/projects/ansible/6/collections/infinidat/infinibox/infini_vol_module.html
fetched_at: 2026-07-27T16:43:30+00:00
---
# infinidat.infinibox.infini_vol module – Create, Delete or Modify volumes on Infinibox

> **Note:**
>
> This module is part of the [infinidat.infinibox collection](https://galaxy.ansible.com/infinidat/infinibox) (version 1.3.12).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install infinidat.infinibox`.
> You need further requirements to be able to use this module,
> see [Requirements](infini_vol_module.md#ansible-collections-infinidat-infinibox-infini-vol-module-requirements) for details.
>
> To use it in a playbook, specify: `infinidat.infinibox.infini_vol`.

New in infinidat.infinibox 2.3.0

- [Synopsis](infini_vol_module.md#synopsis)
- [Requirements](infini_vol_module.md#requirements)
- [Parameters](infini_vol_module.md#parameters)
- [Notes](infini_vol_module.md#notes)
- [Examples](infini_vol_module.md#examples)

## [Synopsis](infini_vol_module.md#id1)

- This module creates, deletes or modifies a volume on Infinibox.

## [Requirements](infini_vol_module.md#id2)

The below requirements are needed on the host that executes this module.

- capacity
- infinisdk (<https://infinisdk.readthedocs.io/en/latest/>)
- python2 >= 2.7 or python3 >= 3.6

## [Parameters](infini_vol_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **name**  string / required | Volume Name |
| **parent_volume_name**  string | Specify a volume name. This is the volume parent for creating a snapshot. Required if volume_type is snapshot. |
| **password**  string / required | Infinibox User password. |
| **pool**  string | Pool that master volume will reside within. Required for creating a master volume, but not a snapshot. |
| **restore_volume_from_snapshot**  string | Specify true to restore a volume (parent_volume_name) from an existing snapshot specified by the name field.  State must be set to present and volume_type must be ‘snapshot’.  Default: `false` |
| **size**  string | Volume size in MB, GB or TB units. Required for creating a master volume, but not a snapshot |
| **snapshot_lock_expires_at**  string | This will cause a snapshot to be locked at the specified date-time. Uses python’s datetime format YYYY-mm-dd HH:MM:SS.ffffff, e.g. 2020-02-13 16:21:59.699700 |
| **snapshot_lock_only**  boolean | This will lock an existing snapshot but will suppress refreshing the snapshot.  Choices:   - `false` ← (default) - `true` |
| **state**  string | Creates/Modifies master volume or snapshot when present or removes when absent.  Choices:   - `"stat"` - `"present"` ← (default) - `"absent"` |
| **system**  string / required | Infinibox Hostname or IPv4 Address. |
| **thin_provision**  boolean | Whether the master volume should be thin or thick provisioned.  Choices:   - `false` - `true` ← (default) |
| **user**  string / required | Infinibox User username with sufficient priveledges ( see notes ). |
| **volume_type**  string | Specifies the volume type, regular volume or snapshot.  Choices:   - `"master"` ← (default) - `"snapshot"` |
| **write_protected**  string | Specifies if the volume should be write protected. Default will be True for snapshots, False for regular volumes.  Choices:   - `"Default"` ← (default) - `"True"` - `"False"` |

## [Notes](infini_vol_module.md#id4)

> **Note:**
>
> - This module requires infinisdk python library
> - You must set INFINIBOX_USER and INFINIBOX_PASSWORD environment variables if user and password arguments are not passed to the module directly
> - Ansible uses the infinisdk configuration file `~/.infinidat/infinisdk.ini` if no credentials are provided. See <http://infinisdk.readthedocs.io/en/latest/getting_started.html>
> - All Infinidat modules support check mode (–check). However, a dryrun that creates resources may fail if the resource dependencies are not met for a task. For example, consider a task that creates a volume in a pool. If the pool does not exist, the volume creation task will fail. It will fail even if there was a previous task in the playbook that would have created the pool but did not because the pool creation was also part of the dry run.

## [Examples](infini_vol_module.md#id5)

```yaml+jinja
- name: Create new volume named foo under pool named bar
  infini_vol:
    name: foo
    # volume_type: master  # Default
    size: 1TB
    thin_provision: yes
    pool: bar
    state: present
    user: admin
    password: secret
    system: ibox001
- name: Create snapshot named foo_snap from volume named foo
  infini_vol:
    name: foo_snap
    volume_type: snapshot
    parent_volume_name: foo
    state: present
    user: admin
    password: secret
    system: ibox001
- name: Stat snapshot, also a volume, named foo_snap
  infini_vol:
    name: foo_snap
    state: present
    user: admin
    password: secret
    system: ibox001
- name: Remove snapshot, also a volume, named foo_snap
  infini_vol:
    name: foo_snap
    state: absent
    user: admin
    password: secret
    system: ibox001
```

### Authors

- David Ohlemacher (@ohlemacher)

### Collection links

[Issue Tracker](https://www.github.com/infinidat/ansible-infinidat-collection/issues)
[Repository (Sources)](https://www.github.com/infinidat/ansible-infinidat-collection)
