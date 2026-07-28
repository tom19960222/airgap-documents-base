---
collection: ansible
version: "8"
title: "ibm.storage_virtualize.ibm_svc_manage_ip module – This module manages IP provisioning on IBM Storage Virtualize family systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/storage_virtualize/ibm_svc_manage_ip_module.html
fetched_at: 2026-07-28T02:35:32+00:00
---
# ibm.storage_virtualize.ibm_svc_manage_ip module – This module manages IP provisioning on IBM Storage Virtualize family systems

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
> To use it in a playbook, specify: `ibm.storage_virtualize.ibm_svc_manage_ip`.

New in ibm.storage_virtualize 1.8.0

- [Synopsis](ibm_svc_manage_ip_module.md#synopsis)
- [Parameters](ibm_svc_manage_ip_module.md#parameters)
- [Notes](ibm_svc_manage_ip_module.md#notes)
- [Examples](ibm_svc_manage_ip_module.md#examples)

## [Synopsis](ibm_svc_manage_ip_module.md#id1)

- Ansible interface to manage ‘mkip’ and ‘rmip’ commands.
- This module can run on all IBM Storage Virtualize systems running on 8.4.2.0 or later.

## [Parameters](ibm_svc_manage_ip_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **clustername**  string / required | The hostname or management IP of the Storage Virtualize system. |
| **domain**  string | Domain for the Storage Virtualize system.  Valid when hostname is used for the parameter *clustername*. |
| **gateway**  string | Specifies the gateway address.  Applies when *state=present*. |
| **ip_address**  string / required | Specifies a valid ipv4/ipv6 address. |
| **log_path**  string | Path of debug log file. |
| **node**  string / required | Specifies the name of the node. |
| **password**  string | REST API password for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **port**  integer / required | Specifies a port ranging from 1 - 16 to which IP shall be assigned. |
| **portset**  string | Specifies the name of the portset object. |
| **shareip**  boolean | Specifies the flag when IP is shared between multiple portsets.  Applies when *state=present*.  **Choices:**   - `false` - `true` |
| **state**  string / required | Creates (`present`) or removes (`absent`) an IP address.  **Choices:**   - `"present"` - `"absent"` |
| **subnet_prefix**  integer | Specifies the prefix of subnet mask.  Applies when *state=present*. |
| **token**  string | The authentication token to verify a user on the Storage Virtualize system.  To generate a token, use the ibm_svc_auth module. |
| **username**  string | REST API username for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  **Choices:**   - `false` ← (default) - `true` |
| **vlan**  integer | Specifies a vlan id ranging from 1 - 4096.  Applies when *state=present*. |

## [Notes](ibm_svc_manage_ip_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_svc_manage_ip_module.md#id4)

```yaml+jinja
- name: Create IP provisioning
  ibm.storage_virtualize.ibm_svc_manage_ip:
   clustername: "{{cluster}}"
   username: "{{username}}"
   password: "{{password}}"
   log_path: /tmp/playbook.debug
   node: node1
   port: 1
   portset: portset0
   ip_address: x.x.x.x
   subnet_prefix: 20
   gateway: x.x.x.x
   vlan: 1
   shareip: true
   state: present
- name: Remove IP provisioning
  ibm.storage_virtualize.ibm_svc_manage_ip:
   clustername: "{{cluster}}"
   username: "{{username}}"
   password: "{{password}}"
   log_path: /tmp/playbook.debug
   node: node1
   port: 1
   portset: portset0
   ip_address: x.x.x.x
   state: absent
```

### Authors

- Sreshtant Bohidar(@Sreshtant-Bohidar)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.storage_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.storage_virtualize)
- [Report an issue](https://github.com/ansible-collections/community.REPO_NAME/issues/new/choose)
- [Communication](index.md#communication-for-ibm-storage-virtualize)
