---
collection: ansible
version: "8"
title: "ansible.windows.win_acl module – Set file/directory/registry permissions for a system user or group"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/windows/win_acl_module.html
fetched_at: 2026-07-28T01:10:28+00:00
---
# ansible.windows.win_acl module – Set file/directory/registry permissions for a system user or group

> **Note:**
>
> This module is part of the [ansible.windows collection](https://galaxy.ansible.com/ui/repo/published/ansible/windows/) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.windows`.
>
> To use it in a playbook, specify: `ansible.windows.win_acl`.

- [Synopsis](win_acl_module.md#synopsis)
- [Parameters](win_acl_module.md#parameters)
- [Notes](win_acl_module.md#notes)
- [See Also](win_acl_module.md#see-also)
- [Examples](win_acl_module.md#examples)

## [Synopsis](win_acl_module.md#id1)

- Add or remove rights/permissions for a given user or group for the specified file, folder, registry key or AppPool identifies.

## [Parameters](win_acl_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **follow**  boolean  *added in ansible.windows 1.12.0* | Follow the symlinks and junctions to apply the ACLs to the target instead of the link.  **Choices:**   - `false` ← (default) - `true` |
| **inherit**  string | Inherit flags on the ACL rules.  Can be specified as a comma separated list, e.g. `ContainerInherit`, `ObjectInherit`.  For more information on the choices see MSDN InheritanceFlags enumeration at <https://msdn.microsoft.com/en-us/library/system.security.accesscontrol.inheritanceflags.aspx>.  Defaults to `ContainerInherit, ObjectInherit` for Directories.  **Choices:**   - `"ContainerInherit"` - `"ObjectInherit"` |
| **path**  string / required | The path to the file or directory. |
| **propagation**  string | Propagation flag on the ACL rules.  For more information on the choices see MSDN PropagationFlags enumeration at <https://msdn.microsoft.com/en-us/library/system.security.accesscontrol.propagationflags.aspx>.  **Choices:**   - `"InheritOnly"` - `"None"` ← (default) - `"NoPropagateInherit"` |
| **rights**  string / required | The rights/permissions that are to be allowed/denied for the specified user or group for the item at `path`.  If `path` is a file or directory, rights can be any right under MSDN FileSystemRights <https://msdn.microsoft.com/en-us/library/system.security.accesscontrol.filesystemrights.aspx>.  If `path` is a registry key, rights can be any right under MSDN RegistryRights <https://msdn.microsoft.com/en-us/library/system.security.accesscontrol.registryrights.aspx>. |
| **state**  string | Specify whether to add `present` or remove `absent` the specified access rule.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **type**  string / required | Specify whether to allow or deny the rights specified.  **Choices:**   - `"allow"` - `"deny"` |
| **user**  string / required | User or Group to add specified rights to act on src file/folder or registry key. |

## [Notes](win_acl_module.md#id3)

> **Note:**
>
> - If adding ACL’s for AppPool identities, the Windows Feature “Web-Scripting-Tools” must be enabled.

## [See Also](win_acl_module.md#id4)

> **See also:**
>
> [ansible.windows.win_acl_inheritance](win_acl_inheritance_module.md#ansible-collections-ansible-windows-win-acl-inheritance-module)
> :   Change ACL inheritance.
>
> [ansible.windows.win_file](win_file_module.md#ansible-collections-ansible-windows-win-file-module)
> :   Creates, touches or removes files or directories.
>
> [ansible.windows.win_owner](win_owner_module.md#ansible-collections-ansible-windows-win-owner-module)
> :   Set owner.
>
> [ansible.windows.win_stat](win_stat_module.md#ansible-collections-ansible-windows-win-stat-module)
> :   Get information about Windows files.

## [Examples](win_acl_module.md#id5)

```yaml+jinja
- name: Restrict write and execute access to User Fed-Phil
  ansible.windows.win_acl:
    user: Fed-Phil
    path: C:\Important\Executable.exe
    type: deny
    rights: ExecuteFile,Write

- name: Add IIS_IUSRS allow rights
  ansible.windows.win_acl:
    path: C:\inetpub\wwwroot\MySite
    user: IIS_IUSRS
    rights: FullControl
    type: allow
    state: present
    inherit: ContainerInherit, ObjectInherit
    propagation: 'None'

- name: Set registry key right
  ansible.windows.win_acl:
    path: HKCU:\Bovine\Key
    user: BUILTIN\Users
    rights: EnumerateSubKeys
    type: allow
    state: present
    inherit: ContainerInherit, ObjectInherit
    propagation: 'None'

- name: Remove FullControl AccessRule for IIS_IUSRS
  ansible.windows.win_acl:
    path: C:\inetpub\wwwroot\MySite
    user: IIS_IUSRS
    rights: FullControl
    type: allow
    state: absent
    inherit: ContainerInherit, ObjectInherit
    propagation: 'None'

- name: Deny Intern
  ansible.windows.win_acl:
    path: C:\Administrator\Documents
    user: Intern
    rights: Read,Write,Modify,FullControl,Delete
    type: deny
    state: present
```

### Authors

- Phil Schwartz (@schwartzmx)
- Trond Hindenes (@trondhindenes)
- Hans-Joachim Kliemeck (@h0nIg)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
- [Communication](index.md#communication-for-ansible-windows)
