---
collection: ansible
version: "6"
title: "community.general.proxmox_snap module – Snapshot management of instances in Proxmox VE cluster"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/proxmox_snap_module.html
fetched_at: 2026-07-27T17:12:10+00:00
---
# community.general.proxmox_snap module – Snapshot management of instances in Proxmox VE cluster

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](proxmox_snap_module.md#ansible-collections-community-general-proxmox-snap-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.proxmox_snap`.

New in community.general 2.0.0

- [Synopsis](proxmox_snap_module.md#synopsis)
- [Requirements](proxmox_snap_module.md#requirements)
- [Parameters](proxmox_snap_module.md#parameters)
- [Notes](proxmox_snap_module.md#notes)
- [Examples](proxmox_snap_module.md#examples)

## [Synopsis](proxmox_snap_module.md#id1)

- Allows you to create/delete/restore snapshots from instances in Proxmox VE cluster.
- Supports both KVM and LXC, OpenVZ has not been tested, as it is no longer supported on Proxmox VE.

## [Requirements](proxmox_snap_module.md#id2)

The below requirements are needed on the host that executes this module.

- proxmoxer
- python >= 2.7
- requests

## [Parameters](proxmox_snap_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_host**  string / required | Specify the target host of the Proxmox VE cluster. |
| **api_password**  string | Specify the password to authenticate with.  You can use `PROXMOX_PASSWORD` environment variable. |
| **api_token_id**  string  added in community.general 1.3.0 | Specify the token ID. |
| **api_token_secret**  string  added in community.general 1.3.0 | Specify the token secret. |
| **api_user**  string / required | Specify the user to authenticate with. |
| **description**  string | Specify the description for the snapshot. Only used on the configuration web interface.  This is saved as a comment inside the configuration file. |
| **force**  boolean | For removal from config file, even if removing disk snapshot fails.  Choices:   - `false` ← (default) - `true` |
| **hostname**  string | The instance name. |
| **snapname**  string | Name of the snapshot that has to be created/deleted/restored.  Default: `"ansible_snap"` |
| **state**  string | Indicate desired state of the instance snapshot.  The `rollback` value was added in community.general 4.8.0.  Choices:   - `"present"` ← (default) - `"absent"` - `"rollback"` |
| **timeout**  integer | Timeout for operations.  Default: `30` |
| **unbind**  boolean  added in community.general 5.7.0 | This option only applies to LXC containers.  Allows to snapshot a container even if it has configured mountpoints.  Temporarily disables all configured mountpoints, takes snapshot, and finally restores original configuration.  If running, the container will be stopped and restarted to apply config changes.  Due to restrictions in the Proxmox API this option can only be used authenticating as `root@pam` with *api_password*, API tokens do not work either.  See <https://pve.proxmox.com/pve-docs/api-viewer/#/nodes>/{node}/lxc/{vmid}/config (PUT tab) for more details.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  Choices:   - `false` ← (default) - `true` |
| **vmid**  string | The instance id.  If not set, will be fetched from PromoxAPI based on the hostname. |
| **vmstate**  boolean | Snapshot includes RAM.  Choices:   - `false` ← (default) - `true` |

## [Notes](proxmox_snap_module.md#id4)

> **Note:**
>
> - Requires proxmoxer and requests modules on host. These modules can be installed with pip.
> - Supports `check_mode`.

## [Examples](proxmox_snap_module.md#id5)

```yaml+jinja
- name: Create new container snapshot
  community.general.proxmox_snap:
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    vmid: 100
    state: present
    snapname: pre-updates

- name: Create new snapshot for a container with configured mountpoints
  community.general.proxmox_snap:
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    vmid: 100
    state: present
    unbind: true # requires root@pam+password auth, API tokens are not supported
    snapname: pre-updates

- name: Remove container snapshot
  community.general.proxmox_snap:
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    vmid: 100
    state: absent
    snapname: pre-updates

- name: Rollback container snapshot
  community.general.proxmox_snap:
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    vmid: 100
    state: rollback
    snapname: pre-updates
```

### Authors

- Jeffrey van Pelt (@Thulium-Drake)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
