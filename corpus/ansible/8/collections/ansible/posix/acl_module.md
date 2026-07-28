---
collection: ansible
version: "8"
title: "ansible.posix.acl module – Set and retrieve file ACL information."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/posix/acl_module.html
fetched_at: 2026-07-28T01:09:24+00:00
---
# ansible.posix.acl module – Set and retrieve file ACL information.

> **Note:**
>
> This module is part of the [ansible.posix collection](https://galaxy.ansible.com/ui/repo/published/ansible/posix/) (version 1.5.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.posix`.
>
> To use it in a playbook, specify: `ansible.posix.acl`.

New in ansible.posix 1.0.0

- [Synopsis](acl_module.md#synopsis)
- [Parameters](acl_module.md#parameters)
- [Notes](acl_module.md#notes)
- [Examples](acl_module.md#examples)
- [Return Values](acl_module.md#return-values)

## [Synopsis](acl_module.md#id1)

- Set and retrieve file ACL information.

## [Parameters](acl_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **default**  boolean | If the target is a directory, setting this to `true` will make it the default ACL for entities created inside the directory.  Setting `default` to `true` causes an error if the path is a file.  **Choices:**   - `false` ← (default) - `true` |
| **entity**  string | The actual user or group that the ACL applies to when matching entity types user or group are selected.  **Default:** `""` |
| **entry**  string | DEPRECATED.  The ACL to set or remove.  This must always be quoted in the form of `<etype>:<qualifier>:<perms>`.  The qualifier may be empty for some types, but the type and perms are always required.  `-` can be used as placeholder when you do not care about permissions.  This is now superseded by entity, type and permissions fields. |
| **etype**  string | The entity type of the ACL to apply, see `setfacl` documentation for more info.  **Choices:**   - `"group"` - `"mask"` - `"other"` - `"user"` |
| **follow**  boolean | Whether to follow symlinks on the path if a symlink is encountered.  **Choices:**   - `false` - `true` ← (default) |
| **path**  aliases: name  path / required | The full path of the file or object. |
| **permissions**  string | The permissions to apply/remove can be any combination of `r`, `w`, `x`  (read, write and execute respectively), and `X` (execute permission if the file is a directory or already has execute permission for some user) |
| **recalculate_mask**  string | Select if and when to recalculate the effective right masks of the files.  See `setfacl` documentation for more info.  Incompatible with `state=query`.  **Choices:**   - `"default"` ← (default) - `"mask"` - `"no_mask"` |
| **recursive**  aliases: recurse  boolean | Recursively sets the specified ACL.  Incompatible with `state=query`.  Alias `recurse` added in version 1.3.0.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | Define whether the ACL should be present or not.  The `query` state gets the current ACL without changing it, for use in `register` operations.  **Choices:**   - `"absent"` - `"present"` - `"query"` ← (default) |
| **use_nfsv4_acls**  boolean | Use NFSv4 ACLs instead of POSIX ACLs.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](acl_module.md#id3)

> **Note:**
>
> - The `acl` module requires that ACLs are enabled on the target filesystem and that the `setfacl` and `getfacl` binaries are installed.
> - As of Ansible 2.0, this module only supports Linux distributions.
> - As of Ansible 2.3, the *name* option has been changed to *path* as default, but *name* still works as well.

## [Examples](acl_module.md#id4)

```yaml+jinja
- name: Grant user Joe read access to a file
  ansible.posix.acl:
    path: /etc/foo.conf
    entity: joe
    etype: user
    permissions: r
    state: present

- name: Removes the ACL for Joe on a specific file
  ansible.posix.acl:
    path: /etc/foo.conf
    entity: joe
    etype: user
    state: absent

- name: Sets default ACL for joe on /etc/foo.d/
  ansible.posix.acl:
    path: /etc/foo.d/
    entity: joe
    etype: user
    permissions: rw
    default: true
    state: present

- name: Same as previous but using entry shorthand
  ansible.posix.acl:
    path: /etc/foo.d/
    entry: default:user:joe:rw-
    state: present

- name: Obtain the ACL for a specific file
  ansible.posix.acl:
    path: /etc/foo.conf
  register: acl_info
```

## [Return Values](acl_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **acl**  list / elements=string | Current ACL on provided path (after changes, if any)  **Returned:** success  **Sample:** `["user::rwx", "group::rwx", "other::rwx"]` |

### Authors

- Brian Coca (@bcoca)
- Jérémie Astori (@astorije)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.posix)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.posix)
