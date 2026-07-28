---
collection: ansible
version: "8"
title: "ibm.storage_virtualize.ibm_sv_manage_fcportsetmember module – This module manages addition or removal of ports to or from the Fibre Channel(FC) portsets on IBM Storage Virtualize family systems."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/storage_virtualize/ibm_sv_manage_fcportsetmember_module.html
fetched_at: 2026-07-28T02:35:15+00:00
---
# ibm.storage_virtualize.ibm_sv_manage_fcportsetmember module – This module manages addition or removal of ports to or from the Fibre Channel(FC) portsets on IBM Storage Virtualize family systems.

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
> To use it in a playbook, specify: `ibm.storage_virtualize.ibm_sv_manage_fcportsetmember`.

New in ibm.storage_virtualize 1.12.0

- [Synopsis](ibm_sv_manage_fcportsetmember_module.md#synopsis)
- [Parameters](ibm_sv_manage_fcportsetmember_module.md#parameters)
- [Notes](ibm_sv_manage_fcportsetmember_module.md#notes)
- [Examples](ibm_sv_manage_fcportsetmember_module.md#examples)

## [Synopsis](ibm_sv_manage_fcportsetmember_module.md#id1)

- Ansible interface to manage ‘addfcportsetmember’ and ‘rmfcportsetmember’ commands.

## [Parameters](ibm_sv_manage_fcportsetmember_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **clustername**  string / required | The hostname or management IP of the Storage Virtualize system. |
| **domain**  string | Domain for the Storage Virtualize system.  Valid when hostname is used for the parameter *clustername*. |
| **fcportid**  string / required | Specifies the Fibre Channel I/O port ID of the port.  The value can be a decimal number 1 to the maximum number of FC I/O ports. |
| **log_path**  string | Path of debug log file. |
| **name**  string / required | Specifies the name of the FC portset. |
| **password**  string | REST API password for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **state**  string / required | Add (`present`) or Remove (`absent`) the FC port ID to or from the FC portset  **Choices:**   - `"present"` - `"absent"` |
| **token**  string | The authentication token to verify a user on the Storage Virtualize system.  To generate a token, use the [ibm.storage_virtualize.ibm_svc_auth](ibm_svc_auth_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-auth-module) module. |
| **username**  string | REST API username for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](ibm_sv_manage_fcportsetmember_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_sv_manage_fcportsetmember_module.md#id4)

```yaml+jinja
- name: Add port ID to the portset
  ibm.storage_virtualize.ibm_sv_manage_fcportsetmember:
   clustername: "{{cluster}}"
   username: "{{username}}"
   password: "{{password}}"
   name: portset1
   fcportid: 3
   state: present
- name: Remove port ID from portset
  ibm.storage_virtualize.ibm_sv_manage_fcportsetmember:
   clustername: "{{cluster}}"
   username: "{{username}}"
   password: "{{password}}"
   name: portset1
   fcportid: 3
   state: absent
```

### Authors

- Sudheesh S (@sudheesh-reddy)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.storage_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.storage_virtualize)
- [Report an issue](https://github.com/ansible-collections/community.REPO_NAME/issues/new/choose)
- [Communication](index.md#communication-for-ibm-storage-virtualize)
