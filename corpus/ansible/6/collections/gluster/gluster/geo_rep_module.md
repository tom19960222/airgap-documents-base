---
collection: ansible
version: "6"
title: "gluster.gluster.geo_rep module – Manage geo-replication sessions"
source_url: https://docs.ansible.com/projects/ansible/6/collections/gluster/gluster/geo_rep_module.html
fetched_at: 2026-07-27T17:47:32+00:00
---
# gluster.gluster.geo_rep module – Manage geo-replication sessions

> **Note:**
>
> This module is part of the [gluster.gluster collection](https://galaxy.ansible.com/gluster/gluster) (version 1.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install gluster.gluster`.
>
> To use it in a playbook, specify: `gluster.gluster.geo_rep`.

- [Synopsis](geo_rep_module.md#synopsis)
- [Parameters](geo_rep_module.md#parameters)
- [Examples](geo_rep_module.md#examples)

## [Synopsis](geo_rep_module.md#id1)

- Create, stop, delete and configure geo-replication session

## [Parameters](geo_rep_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **action**  string / required | Action to be performed on geo-replication session.  Choices:   - `"create"` - `"start"` - `"stop"` - `"delete"` - `"pause"` - `"resume"` - `"config"` |
| **changelog_log_level**  string | The log level for the changelog. |
| **checkpoint**  string | Sets a checkpoint with the given option. |
| **force**  string | force the system to perform the action. |
| **georepuser**  string | Username to be used for the action being performed. |
| **gluster_log_file**  string | The path to the geo-replication glusterfs log file. |
| **gluster_log_level**  string | The log level for glusterfs processes. |
| **ignore_deletes**  string | file deletion on the master will not trigger a delete operation on the slave. |
| **log_file**  string | The path to the geo-replication log file. |
| **log_level**  string | The log level for geo-replication. |
| **log_rsync_performance**  string | for recording the rsync performance in log files. |
| **mastervol**  string | Master volume name. |
| **meta_volume_mnt**  string | The path of the meta volume mount point. |
| **rsync_command**  string | The command to use for setting synchronizing method for the files. |
| **rsync_options**  string | Additional options to rsync. |
| **slavevol**  string | Slave volume name. |
| **ssh_command**  string | The SSH command to connect to the remote machine. |
| **sync_acls**  string | Syncs acls to the Slave cluster. |
| **sync_jobs**  string | number of sync-jobs . |
| **sync_xattrs**  string | Syncs extended attributes to the Slave cluster. |
| **timeout**  string | timeout period. |
| **use_meta_volume**  string | to use meta volume in Geo-replication. |
| **use_tarssh**  string | To use tar over ssh. |
| **volume_id**  string | deletes the existing master UID for the intermediate/slave node. |

## [Examples](geo_rep_module.md#id3)

```yaml+jinja
- name: Create the geo-rep session
  gluster.gluster.geo_rep:
    action: create
    mastervol: 10.70.42.122:mastervolume
    slavevol: 10.70.43.48:slavevolume
    force: true
    georepuser: staff
- name: Starts the geo-rep session
  gluster.gluster.geo_rep:
    action: start
    mastervol: 10.70.42.122:mastervolume
    slavevol: 10.70.43.48:slavevolume
    force: true
    georepuser: staff
- name: Pause the geo-rep session
  gluster.gluster.geo_rep:
    action: pause
    mastervol: 10.70.42.122:mastervolume
    slavevol: 10.70.43.48:slavevolume
    force: true
    georepuser: staff
- name: Resume the geo-rep session
  gluster.gluster.geo_rep:
    action: resume
    mastervol: 10.70.42.122:mastervolume
    slavevol: 10.70.43.48:slavevolume
    force: true
    georepuser: staff
- name: Stop the geo-rep session
  gluster.gluster.geo_rep:
    action: stop
    mastervol: 10.70.42.122:mastervolume
    slavevol: 10.70.43.48:slavevolume
    force: true
    georepuser: staff
- name: Configures the geo-rep session
  gluster.gluster.geo_rep:
    action: config
    mastervol: 10.70.42.122:mastervolume
    slavevol: 10.70.43.48:slavevolume
    gluster_log_file: /var/log/glusterfs/geo-replication/gluster.log
    gluster_log_level: INFO
    log_file: /var/log/glusterfs/geo-replication/file.log
    log_level: INFO
    changelog_log_level: INFO
    ssh_command: SSH
    rsync_command: rsync
    use_tarssh: true
    volume_id: 6a071cfa-b150-4f0b-b1ed-96ab5d4bd671
    timeout: 60
    sync_jobs: 3
    ignore_deletes: 1
    checkpoint: now
    sync_acls: true
    sync_xattr: true
    log_rsync_performance: true
    rsync_options: --compress-level=0
    use_meta_volume: true
    meta_volume_mnt: /var/run/gluster/shared_storage/
- name: Delete the geo-rep session
  gluster.gluster.geo_rep:
    action: delete
    mastervol: 10.70.42.122:mastervolume
    slavevol: 10.70.43.48:slavevolume
    georepuser: staff
```

### Authors

- Sachidananda Urs (@sac)

### Collection links

[Issue Tracker](https://github.com/gluster/gluster-ansible-collection/issues)
[Repository (Sources)](https://github.com/gluster/gluster-ansible-collection)
