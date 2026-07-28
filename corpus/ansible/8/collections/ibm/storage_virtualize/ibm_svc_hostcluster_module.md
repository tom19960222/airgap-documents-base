---
collection: ansible
version: "8"
title: "ibm.storage_virtualize.ibm_svc_hostcluster module – This module manages host cluster on IBM Storage Virtualize family systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/storage_virtualize/ibm_svc_hostcluster_module.html
fetched_at: 2026-07-28T02:35:26+00:00
---
# ibm.storage_virtualize.ibm_svc_hostcluster module – This module manages host cluster on IBM Storage Virtualize family systems

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
> To use it in a playbook, specify: `ibm.storage_virtualize.ibm_svc_hostcluster`.

New in ibm.storage_virtualize 1.5.0

- [Synopsis](ibm_svc_hostcluster_module.md#synopsis)
- [Parameters](ibm_svc_hostcluster_module.md#parameters)
- [Notes](ibm_svc_hostcluster_module.md#notes)
- [Examples](ibm_svc_hostcluster_module.md#examples)

## [Synopsis](ibm_svc_hostcluster_module.md#id1)

- Ansible interface to manage ‘mkhostcluster’, ‘chhostcluster’ and ‘rmhostcluster’ host commands.

## [Parameters](ibm_svc_hostcluster_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **clustername**  string / required | The hostname or management IP of the Storage Virtualize system. |
| **domain**  string | Domain for the Storage Virtualize system.  Valid when hostname is used for the parameter *clustername*. |
| **log_path**  string | Path of debug log file. |
| **name**  string / required | Specifies a name or label for the new host cluster object. |
| **noownershipgroup**  boolean  *added in ibm.storage_virtualize 1.6.0* | If specified True, the host cluster object is removed from the ownership group to which it belongs.  Parameters *ownershipgroup* and *noownershipgroup* are mutually exclusive.  Applies when *state=present* to modify an existing hostcluster.  **Choices:**   - `false` - `true` |
| **ownershipgroup**  string  *added in ibm.storage_virtualize 1.6.0* | The name of the ownership group to which the host cluster object is being added.  Parameters *ownershipgroup* and *noownershipgroup* are mutually exclusive.  Applies when *state=present*. |
| **password**  string | REST API password for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **removeallhosts**  boolean | Specifies that all hosts in the host cluster and the associated host cluster object be deleted.  Applies when *state=absent*.  **Choices:**   - `false` - `true` |
| **state**  string / required | Creates (`present`) or removes (`absent`) a host cluster.  **Choices:**   - `"absent"` - `"present"` |
| **token**  string | The authentication token to verify a user on the Storage Virtualize system.  To generate a token, use the [ibm.storage_virtualize.ibm_svc_auth](ibm_svc_auth_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-auth-module) module. |
| **username**  string | REST API username for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](ibm_svc_hostcluster_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_svc_hostcluster_module.md#id4)

```yaml+jinja
- name: Define a new host cluster
  ibm.storage_virtualize.ibm_svc_hostcluster:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    name: hostcluster0
    state: present
    ownershipgroup: group1
- name: Update the ownershipgroup of a host cluster
  ibm.storage_virtualize.ibm_svc_hostcluster:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    name: hostcluster0
    state: present
    noownershipgroup: True
- name: Delete a host cluster
  ibm.storage_virtualize.ibm_svc_hostcluster:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    name: hostcluster0
    state: absent
    removeallhosts: True
```

### Authors

- Shilpi Jain (@Shilpi-J)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.storage_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.storage_virtualize)
- [Report an issue](https://github.com/ansible-collections/community.REPO_NAME/issues/new/choose)
- [Communication](index.md#communication-for-ibm-storage-virtualize)
