---
collection: ansible
version: "8"
title: "ibm.storage_virtualize.ibm_svc_manage_usergroup module – This module manages user group on IBM Storage Virtualize family systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/storage_virtualize/ibm_svc_manage_usergroup_module.html
fetched_at: 2026-07-28T02:35:39+00:00
---
# ibm.storage_virtualize.ibm_svc_manage_usergroup module – This module manages user group on IBM Storage Virtualize family systems

> **Note:**
>
> This module is part of the [ibm.storage_virtualize collection](https://galaxy.ansible.com/ui/repo/published/ibm/storage_virtualize/) (version 2.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ibm.storage_virtualize`.
>
> To use it in a playbook, specify: `ibm.storage_virtualize.ibm_svc_manage_usergroup`.

New in ibm.storage_virtualize 1.7.0

- [Synopsis](ibm_svc_manage_usergroup_module.md#synopsis)
- [Parameters](ibm_svc_manage_usergroup_module.md#parameters)
- [Notes](ibm_svc_manage_usergroup_module.md#notes)
- [Examples](ibm_svc_manage_usergroup_module.md#examples)

## [Synopsis](ibm_svc_manage_usergroup_module.md#id1)

- Ansible interface to manage ‘mkusergrp’, ‘rmusergrp’, and ‘chusergrp’ commands.

## [Parameters](ibm_svc_manage_usergroup_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **clustername**  string / required | The hostname or management IP of the Storage Virtualize system. |
| **domain**  string | Domain for the Storage Virtualize system.  Valid when hostname is used for the parameter *clustername*. |
| **log_path**  string | Path of debug log file. |
| **name**  string / required | Specifies the name of the user group. |
| **noownershipgroup**  boolean | Specifies that the usergroup is removed from the ownership group it belonged to.  Applies when *state=present*, to modify a user group.  Parameters *ownershipgroup* and *noownershipgroup* are mutually exclusive.  **Choices:**   - `false` - `true` |
| **ownershipgroup**  string | Specifies the name of the ownership group.  Applies when *state=present*.  Parameters *ownershipgroup* and *noownershipgroup* are mutually exclusive. |
| **password**  string | REST API password for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **role**  string | Specifies the role associated with all users that belong to this user group.  Required when *state=present*.  **Choices:**   - `"Monitor"` - `"CopyOperator"` - `"Service"` - `"FlashCopyAdmin"` - `"Administrator"` - `"SecurityAdmin"` - `"VasaProvider"` - `"RestrictedAdmin"` - `"3SiteAdmin"` |
| **state**  string / required | Creates or updates (`present`) or removes (`absent`) a user group.  **Choices:**   - `"present"` - `"absent"` |
| **token**  string | The authentication token to verify a user on the Storage Virtualize system.  To generate a token, use the ibm_svc_auth module. |
| **username**  string | REST API username for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](ibm_svc_manage_usergroup_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_svc_manage_usergroup_module.md#id4)

```yaml+jinja
- name: Create a user group
  ibm.storage_virtualize.ibm_svc_manage_usergroup:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    state: present
    name: user-group-name
    role: Monitor
    ownershipgroup: ownershipgroup-name
- name: Remove a user group
  ibm.storage_virtualize.ibm_svc_manage_usergroup:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    state: absent
    name: user-group-name
```

### Authors

- Sreshtant Bohidar(@Sreshtant-Bohidar)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.storage_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.storage_virtualize)
- [Report an issue](https://github.com/ansible-collections/community.REPO_NAME/issues/new/choose)
- [Communication](index.md#communication-for-ibm-storage-virtualize)
