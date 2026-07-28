---
collection: ansible
version: "8"
title: "purestorage.flashblade.purefb_fs module – Manage filesystemon Pure Storage FlashBlade`"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flashblade/purefb_fs_module.html
fetched_at: 2026-07-28T02:51:58+00:00
---
# purestorage.flashblade.purefb_fs module – Manage filesystemon Pure Storage FlashBlade`

> **Note:**
>
> This module is part of the [purestorage.flashblade collection](https://galaxy.ansible.com/ui/repo/published/purestorage/flashblade/) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flashblade`.
> You need further requirements to be able to use this module,
> see [Requirements](purefb_fs_module.md#ansible-collections-purestorage-flashblade-purefb-fs-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_fs`.

New in purestorage.flashblade 1.0.0

- [Synopsis](purefb_fs_module.md#synopsis)
- [Requirements](purefb_fs_module.md#requirements)
- [Parameters](purefb_fs_module.md#parameters)
- [Notes](purefb_fs_module.md#notes)
- [Examples](purefb_fs_module.md#examples)

## [Synopsis](purefb_fs_module.md#id1)

- This module manages filesystems on Pure Storage FlashBlade.

## [Requirements](purefb_fs_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_fs_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_control**  string | The access control style that is utilized for client actions such as setting file and directory ACLs.  Only available from Purity//FB 3.1.1  **Choices:**   - `"nfs"` - `"smb"` - `"shared"` ← (default) - `"independent"` - `"mode-bits"` |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **client_policy**  string  *added in purestorage.flashblade 1.12.0* | Name of SMB client policy to assign to filesystem  Only valid with REST 2.10 or higher  Remove policy with empty string |
| **delete_link**  boolean | Define if the filesystem can be deleted even if it has a replica link  **Choices:**   - `false` ← (default) - `true` |
| **discard_snaps**  boolean | Allow a filesystem to be demoted.  **Choices:**   - `false` ← (default) - `true` |
| **eradicate**  boolean | Define whether to eradicate the filesystem on delete or leave in trash.  **Choices:**   - `false` ← (default) - `true` |
| **export_policy**  string  *added in purestorage.flashblade 1.9.0* | Name of NFS export policy to assign to filesystem  Overrides *nfs_rules*  Only valid for Purity//FB 3.3.0 or higher |
| **fastremove**  boolean | Define whether the fast remove directory is enabled for the filesystem.  **Choices:**   - `false` ← (default) - `true` |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **group_quota**  string | Default quota in M, G, T or P units for a group under this file system. |
| **hard_limit**  boolean | Define whether the capacity for a filesystem is a hard limit.  CAUTION This will cause the filesystem to go Read-Only if the capacity has already exceeded the logical size of the filesystem.  **Choices:**   - `false` ← (default) - `true` |
| **http**  boolean | Define whether to HTTP/HTTPS protocol is enabled for the filesystem.  **Choices:**   - `false` ← (default) - `true` |
| **name**  string / required | Filesystem Name. |
| **nfs_rules**  string | Define the NFS rules in operation.  If not set at filesystem creation time it defaults to *\*(rw,no_root_squash*)  Supported binary options are ro/rw, secure/insecure, fileid_32bit/no_fileid_32bit, root_squash/no_root_squash, all_squash/no_all_squash and atime/noatime  Supported non-binary options are anonuid=#, anongid=#, sec=(sys|krb5)  Superceeded by *export_policy* if provided |
| **nfsv3**  boolean | Define whether to NFSv3 protocol is enabled for the filesystem.  **Choices:**   - `false` - `true` ← (default) |
| **nfsv4**  boolean | Define whether to NFSv4.1 protocol is enabled for the filesystem.  **Choices:**   - `false` - `true` ← (default) |
| **policy**  string | Filesystem policy to assign to or remove from a filesystem. |
| **policy_state**  string | Add or delete a policy from a filesystem  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **promote**  boolean | Promote/demote a filesystem.  Can only demote the file-system if it is in a replica-link relationship.  **Choices:**   - `false` - `true` |
| **safeguard_acls**  boolean | Safeguards ACLs on a filesystem.  Performs different roles depending on the filesystem protocol enabled.  See Purity//FB documentation for detailed description.  Only available from Purity//FB 3.1.1  **Choices:**   - `false` - `true` ← (default) |
| **share_policy**  string  *added in purestorage.flashblade 1.12.0* | Name of SMB share policy to assign to filesystem  Only valid with REST 2.10 or higher  Remove policy with empty string |
| **size**  string | Volume size in M, G, T or P units. See examples.  If size is not set at filesystem creation time the filesystem size becomes unlimited. |
| **smb**  boolean | Define whether to SMB protocol is enabled for the filesystem.  **Choices:**   - `false` ← (default) - `true` |
| **smb_aclmode**  string | Specify the ACL mode for the SMB protocol.  Deprecated from Purity//FB 3.1.1. Use *access_control* instead.  **Choices:**   - `"shared"` ← (default) - `"native"` |
| **snapshot**  boolean | Define whether a snapshot directory is enabled for the filesystem.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | Create, delete or modifies a filesystem.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **user_quota**  string | Default quota in M, G, T or P units for a user under this file system. |
| **writable**  boolean | Define if a filesystem is writeable.  **Choices:**   - `false` - `true` |

## [Notes](purefb_fs_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_fs_module.md#id5)

```yaml+jinja
- name: Create new filesystem named foo
  purestorage.flashblade.purefb_fs:
    name: foo
    size: 1T
    state: present
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Delete filesystem named foo
  purestorage.flashblade.purefb_fs:
    name: foo
    state: absent
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Recover filesystem named foo
  purestorage.flashblade.purefb_fs:
    name: foo
    state: present
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Eradicate filesystem named foo
  purestorage.flashblade.purefb_fs:
    name: foo
    state: absent
    eradicate: true
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Promote filesystem named foo ready for failover
  purestorage.flashblade.purefb_fs:
    name: foo
    promote: true
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Demote filesystem named foo after failover
  purestorage.flashblade.purefb_fs:
    name: foo
    promote: false
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Modify attributes of an existing filesystem named foo
  purestorage.flashblade.purefb_fs:
    name: foo
    size: 2T
    nfsv3 : false
    nfsv4 : true
    user_quota: 10K
    group_quota: 25M
    nfs_rules: '10.21.200.0/24(ro)'
    snapshot: true
    fastremove: true
    hard_limit: true
    smb: true
    state: present
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
