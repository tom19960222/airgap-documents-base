---
collection: ansible
version: "8"
title: "community.general.udm_share module – Manage samba shares on a univention corporate server"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/udm_share_module.html
fetched_at: 2026-07-28T01:51:02+00:00
---
# community.general.udm_share module – Manage samba shares on a univention corporate server

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.udm_share`.

- [Synopsis](udm_share_module.md#synopsis)
- [Parameters](udm_share_module.md#parameters)
- [Attributes](udm_share_module.md#attributes)
- [Examples](udm_share_module.md#examples)

## [Synopsis](udm_share_module.md#id1)

- This module allows to manage samba shares on a univention corporate server (UCS). It uses the python API of the UCS to create a new object or edit it.

Aliases: cloud.univention.udm_share

## [Parameters](udm_share_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **directorymode**  string | Permissions for the share’s root directory.  **Default:** `"00755"` |
| **group**  string | Directory owner group of the share’s root directory.  **Default:** `"0"` |
| **host**  string | Host FQDN (server which provides the share), for example `{{ ansible_fqdn }}`. Required if `state=present`. |
| **name**  string / required | Name |
| **nfs_hosts**  list / elements=string | Only allow access for this host, IP address or network.  **Default:** `[]` |
| **nfsCustomSettings**  aliases: nfs_custom_settings  list / elements=string | Option name in exports file.  **Default:** `[]` |
| **ou**  string / required | Organisational unit, inside the LDAP Base DN. |
| **owner**  string | Directory owner of the share’s root directory.  **Default:** `"0"` |
| **path**  path | Directory on the providing server, for example `/home`. Required if `state=present`. |
| **root_squash**  boolean | Modify user ID for root user (root squashing).  **Choices:**   - `false` - `true` ← (default) |
| **sambaBlockingLocks**  aliases: samba_blocking_locks  boolean | Blocking locks.  **Choices:**   - `false` - `true` ← (default) |
| **sambaBlockSize**  aliases: samba_block_size  string | Blocking size. |
| **sambaBrowseable**  aliases: samba_browsable  boolean | Show in Windows network environment.  **Choices:**   - `false` - `true` ← (default) |
| **sambaCreateMode**  aliases: samba_create_mode  string | File mode.  **Default:** `"0744"` |
| **sambaCscPolicy**  aliases: samba_csc_policy  string | Client-side caching policy.  **Default:** `"manual"` |
| **sambaCustomSettings**  aliases: samba_custom_settings  list / elements=dictionary | Option name in smb.conf and its value.  **Default:** `[]` |
| **sambaDirectoryMode**  aliases: samba_directory_mode  string | Directory mode.  **Default:** `"0755"` |
| **sambaDirectorySecurityMode**  aliases: samba_directory_security_mode  string | Directory security mode.  **Default:** `"0777"` |
| **sambaDosFilemode**  aliases: samba_dos_filemode  boolean | Users with write access may modify permissions.  **Choices:**   - `false` ← (default) - `true` |
| **sambaFakeOplocks**  aliases: samba_fake_oplocks  boolean | Fake oplocks.  **Choices:**   - `false` ← (default) - `true` |
| **sambaForceCreateMode**  aliases: samba_force_create_mode  boolean | Force file mode.  **Choices:**   - `false` ← (default) - `true` |
| **sambaForceDirectoryMode**  aliases: samba_force_directory_mode  boolean | Force directory mode.  **Choices:**   - `false` ← (default) - `true` |
| **sambaForceDirectorySecurityMode**  aliases: samba_force_directory_security_mode  boolean | Force directory security mode.  **Choices:**   - `false` ← (default) - `true` |
| **sambaForceGroup**  aliases: samba_force_group  string | Force group. |
| **sambaForceSecurityMode**  aliases: samba_force_security_mode  boolean | Force security mode.  **Choices:**   - `false` ← (default) - `true` |
| **sambaForceUser**  aliases: samba_force_user  string | Force user. |
| **sambaHideFiles**  aliases: samba_hide_files  string | Hide files. |
| **sambaHideUnreadable**  aliases: samba_hide_unreadable  boolean | Hide unreadable files/directories.  **Choices:**   - `false` ← (default) - `true` |
| **sambaHostsAllow**  aliases: samba_hosts_allow  list / elements=string | Allowed host/network.  **Default:** `[]` |
| **sambaHostsDeny**  aliases: samba_hosts_deny  list / elements=string | Denied host/network.  **Default:** `[]` |
| **sambaInheritAcls**  aliases: samba_inherit_acls  boolean | Inherit ACLs.  **Choices:**   - `false` - `true` ← (default) |
| **sambaInheritOwner**  aliases: samba_inherit_owner  boolean | Create files/directories with the owner of the parent directory.  **Choices:**   - `false` ← (default) - `true` |
| **sambaInheritPermissions**  aliases: samba_inherit_permissions  boolean | Create files/directories with permissions of the parent directory.  **Choices:**   - `false` ← (default) - `true` |
| **sambaInvalidUsers**  aliases: samba_invalid_users  string | Invalid users or groups. |
| **sambaLevel2Oplocks**  aliases: samba_level_2_oplocks  boolean | Level 2 oplocks.  **Choices:**   - `false` - `true` ← (default) |
| **sambaLocking**  aliases: samba_locking  boolean | Locking.  **Choices:**   - `false` - `true` ← (default) |
| **sambaMSDFSRoot**  aliases: samba_msdfs_root  boolean | MSDFS root.  **Choices:**   - `false` ← (default) - `true` |
| **sambaName**  aliases: samba_name  string | Windows name. Required if `state=present`. |
| **sambaNtAclSupport**  aliases: samba_nt_acl_support  boolean | NT ACL support.  **Choices:**   - `false` - `true` ← (default) |
| **sambaOplocks**  aliases: samba_oplocks  boolean | Oplocks.  **Choices:**   - `false` - `true` ← (default) |
| **sambaPostexec**  aliases: samba_postexec  string | Postexec script. |
| **sambaPreexec**  aliases: samba_preexec  string | Preexec script. |
| **sambaPublic**  aliases: samba_public  boolean | Allow anonymous read-only access with a guest user.  **Choices:**   - `false` ← (default) - `true` |
| **sambaSecurityMode**  aliases: samba_security_mode  string | Security mode.  **Default:** `"0777"` |
| **sambaStrictLocking**  aliases: samba_strict_locking  string | Strict locking.  **Default:** `"Auto"` |
| **sambaValidUsers**  aliases: samba_valid_users  string | Valid users or groups. |
| **sambaVFSObjects**  aliases: samba_vfs_objects  string | VFS objects. |
| **sambaWriteable**  aliases: samba_writeable  boolean | Samba write access.  **Choices:**   - `false` - `true` ← (default) |
| **sambaWriteList**  aliases: samba_write_list  string | Restrict write access to these users/groups. |
| **state**  string | Whether the share is present or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **subtree_checking**  boolean | Subtree checking.  **Choices:**   - `false` - `true` ← (default) |
| **sync**  string | NFS synchronisation.  **Default:** `"sync"` |
| **writeable**  boolean | NFS write access.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](udm_share_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **partial** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](udm_share_module.md#id4)

```yaml+jinja
- name: Create a share named home on the server ucs.example.com with the path /home
  community.general.udm_share:
    name: home
    path: /home
    host: ucs.example.com
    sambaName: Home
```

### Authors

- Tobias Rüetschi (@keachi)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
