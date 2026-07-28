---
collection: ansible
version: "8"
title: "ibm.storage_virtualize.ibm_svc_host module – This module manages hosts on IBM Storage Virtualize family systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/storage_virtualize/ibm_svc_host_module.html
fetched_at: 2026-07-28T02:35:25+00:00
---
# ibm.storage_virtualize.ibm_svc_host module – This module manages hosts on IBM Storage Virtualize family systems

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
> To use it in a playbook, specify: `ibm.storage_virtualize.ibm_svc_host`.

New in ibm.storage_virtualize 1.0.0

- [Synopsis](ibm_svc_host_module.md#synopsis)
- [Parameters](ibm_svc_host_module.md#parameters)
- [Notes](ibm_svc_host_module.md#notes)
- [Examples](ibm_svc_host_module.md#examples)

## [Synopsis](ibm_svc_host_module.md#id1)

- Ansible interface to manage ‘mkhost’, ‘chhost’, and ‘rmhost’ host commands.

## [Parameters](ibm_svc_host_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **clustername**  string / required | The hostname or management IP of the Storage Virtualize system. |
| **domain**  string | Domain for the Storage Virtualize system.  Valid when hostname is used for the parameter *clustername*. |
| **fcwwpn**  string | List of Initiator WWPNs to be added to the host. The complete list of WWPNs must be provided.  The parameters *fcwwpn* and *iscsiname* are mutually exclusive.  Required when *state=present*, to create or modify a Fibre Channel (FC) host. |
| **hostcluster**  string  *added in ibm.storage_virtualize 1.5.0* | Specifies the name of the host cluster to which the host object is to be added. A host cluster must exist before a host object can be added to it.  Parameters *hostcluster* and *nohostcluster* are mutually exclusive.  Valid when *state=present*, to create or modify a host. |
| **iogrp**  string | Specifies a set of one or more input/output (I/O) groups from which the host can access the volumes. Once specified, this parameter cannot be modified.  Valid when *state=present*, to create a host. |
| **iscsiname**  string | List of Initiator IQNs to be added to the host. IQNs are separated by comma. The complete list of IQNs must be provided.  The parameters *fcwwpn* and *iscsiname* are mutually exclusive.  Valid when *state=present*, to create host. |
| **log_path**  string | Path of debug log file. |
| **name**  string / required | Specifies a name or label for the new host object. |
| **nohostcluster**  boolean  *added in ibm.storage_virtualize 1.5.0* | If specified as `True`, host object is removed from the host cluster.  Parameters *hostcluster* and *nohostcluster* are mutually exclusive.  Valid when *state=present*, to modify an existing host.  **Choices:**   - `false` - `true` |
| **nopartition**  boolean  *added in ibm.storage_virtualize 2.1.0* | If specified as `True`, the host object is removed from the storage partition.  Parameters *partition* and *nopartition* are mutually exclusive.  Valid when *state=present*, to modify an existing host.  Supported from Storage Virtualize family systems 8.6.1.0 or later.  **Choices:**   - `false` - `true` |
| **nqn**  string  *added in ibm.storage_virtualize 1.12.0* | List of initiator NQNs to be added to the host. Each NQN is separated by a comma. The complete list of NQNs must be provided.  Required when *protocol=rdmanvme*, to create.  Valid when *state=present*, to create or modify a host. |
| **old_name**  string  *added in ibm.storage_virtualize 1.9.0* | Specifies the old name of the host while renaming.  Valid when *state=present*, to rename an existing host. |
| **partition**  string  *added in ibm.storage_virtualize 2.1.0* | Specifies the storage partition to be associated with the host.  Valid when *state=present*, to create or modify a host.  Supported from Storage Virtualize family systems 8.6.1.0 or later. |
| **password**  string | REST API password for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **portset**  string  *added in ibm.storage_virtualize 1.12.0* | Specifies the portset to be associated with the host.  Valid when *state=present*, to create or modify a host. |
| **protocol**  string | Specifies the protocol used by the host to communicate with the storage system. Only ‘scsi’ protocol is supported.  Valid when *state=present*, to create a host.  **Choices:**   - `"scsi"` - `"rdmanvme"` |
| **site**  string | Specifies the site name of the host.  Valid when *state=present*, to create or modify a host. |
| **state**  string / required | Creates or updates (`present`) or removes (`absent`) a host.  **Choices:**   - `"absent"` - `"present"` |
| **token**  string  *added in ibm.storage_virtualize 1.5.0* | The authentication token to verify a user on the Storage Virtualize system.  To generate a token, use the [ibm.storage_virtualize.ibm_svc_auth](ibm_svc_auth_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-auth-module) module. |
| **type**  string | Specifies the type of host.  Valid when *state=present*, to create or modify a host. |
| **username**  string | REST API username for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](ibm_svc_host_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_svc_host_module.md#id4)

```yaml+jinja
- name: Define a new iSCSI host
  ibm.storage_virtualize.ibm_svc_host:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    name: host4test
    state: present
    iscsiname: iqn.1994-05.com.redhat:2e358e438b8a
    iogrp: 0:1:2:3
    protocol: scsi
    type: generic
    site: site-name
    portset: portset0
- name: Add a host to an existing host cluster
  ibm.storage_virtualize.ibm_svc_host:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    name: host4test
    state: present
    hostcluster: hostcluster0
- name: Define a new FC host
  ibm.storage_virtualize.ibm_svc_host:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    name: host4test
    state: present
    fcwwpn: 100000109B570216:1000001AA0570266
    iogrp: 0:1:2:3
    protocol: scsi
    type: generic
    site: site-name
- name: Rename an existing host
  ibm.storage_virtualize.ibm_svc_host:
    clustername: "{{ clustername }}"
    domain: "{{ domain }}"
    username: "{{ username }}"
    password: "{{ password }}"
    old_name: "host4test"
    name: "new_host_name"
    state: "present"
- name: Create an iSCSI host
  ibm.storage_virtualize.ibm_svc_host:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    name: host_name
    iscsiname: iqn.1994-05.com.redhat:2e358e438b8a,iqn.localhost.hostid.7f000001
    state: present
- name: Delete a host
  ibm.storage_virtualize.ibm_svc_host:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    name: new_host_name
    state: absent
```

### Authors

- Sreshtant Bohidar (@Sreshtant-Bohidar)
- Rohit Kumar (@rohitk-github)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.storage_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.storage_virtualize)
- [Report an issue](https://github.com/ansible-collections/community.REPO_NAME/issues/new/choose)
- [Communication](index.md#communication-for-ibm-storage-virtualize)
