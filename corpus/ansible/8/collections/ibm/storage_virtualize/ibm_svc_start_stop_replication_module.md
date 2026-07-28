---
collection: ansible
version: "8"
title: "ibm.storage_virtualize.ibm_svc_start_stop_replication module – This module starts or stops remote copies on IBM Storage Virtualize family systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/storage_virtualize/ibm_svc_start_stop_replication_module.html
fetched_at: 2026-07-28T02:35:43+00:00
---
# ibm.storage_virtualize.ibm_svc_start_stop_replication module – This module starts or stops remote copies on IBM Storage Virtualize family systems

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
> To use it in a playbook, specify: `ibm.storage_virtualize.ibm_svc_start_stop_replication`.

New in ibm.storage_virtualize 1.3.0

- [Synopsis](ibm_svc_start_stop_replication_module.md#synopsis)
- [Parameters](ibm_svc_start_stop_replication_module.md#parameters)
- [Notes](ibm_svc_start_stop_replication_module.md#notes)
- [Examples](ibm_svc_start_stop_replication_module.md#examples)

## [Synopsis](ibm_svc_start_stop_replication_module.md#id1)

- Ansible interface to manage remote copy related commands.

## [Parameters](ibm_svc_start_stop_replication_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access**  boolean | Instructs the system to allow write access to a consistent secondary volume.  Applies when *state=stopped*.  **Choices:**   - `false` ← (default) - `true` |
| **clean**  boolean | Specifies that the volume that is to become a secondary is clean.  Applies when *state=started*.  **Choices:**   - `false` ← (default) - `true` |
| **clustername**  string / required | The hostname or management IP of the Storage Virtualize system. |
| **domain**  string | Domain for the Storage Virtualize system.  Valid when hostname is used for the parameter *clustername*. |
| **force**  boolean | Specifies that the system must process the copy operation even if it causes a temporary loss of consistency during synchronization.  Applies when *state=started*.  **Choices:**   - `false` - `true` |
| **isgroup**  boolean | Specifies that a consistency group has to be started or stopped.  **Choices:**   - `false` ← (default) - `true` |
| **log_path**  string | Path of debug log file. |
| **name**  string | Specifies a name to assign to the new remote copy relationship or group, or to operate on the existing remote copy. |
| **password**  string | REST API password for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **primary**  string | Specifies the copy direction by defining which disk becomes the primary (source).  Applies when *state=started*.  **Choices:**   - `"master"` - `"aux"` |
| **state**  string / required | Starts (`started`) or stops (`stopped`) a remote copy relationship.  **Choices:**   - `"started"` - `"stopped"` |
| **token**  string  *added in ibm.storage_virtualize 1.5.0* | The authentication token to verify a user on the Storage Virtualize system.  To generate a token, use the ibm_svc_auth module. |
| **username**  string | REST API username for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](ibm_svc_start_stop_replication_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_svc_start_stop_replication_module.md#id4)

```yaml+jinja
- name: Start remote copy
  ibm.storage_virtualize.ibm_svc_start_stop_replication:
    name: sample_rcopy
    clustername: "{{clustername}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/ansible.log
    state: started
    clean: true
- name: Stop remote copy
  ibm.storage_virtualize.ibm_svc_start_stop_replication:
    name: sample_rcopy
    clustername: "{{clustername}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/ansible.log
    state: stopped
```

### Authors

- rohit(@rohitk-github)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.storage_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.storage_virtualize)
- [Report an issue](https://github.com/ansible-collections/community.REPO_NAME/issues/new/choose)
- [Communication](index.md#communication-for-ibm-storage-virtualize)
