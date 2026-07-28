---
collection: ansible
version: "8"
title: "ibm.storage_virtualize.ibm_sv_manage_syslog_server module – This module manages syslog server on IBM Storage Virtualize family systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/storage_virtualize/ibm_sv_manage_syslog_server_module.html
fetched_at: 2026-07-28T02:35:21+00:00
---
# ibm.storage_virtualize.ibm_sv_manage_syslog_server module – This module manages syslog server on IBM Storage Virtualize family systems

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
> To use it in a playbook, specify: `ibm.storage_virtualize.ibm_sv_manage_syslog_server`.

New in ibm.storage_virtualize 2.1.0

- [Synopsis](ibm_sv_manage_syslog_server_module.md#synopsis)
- [Parameters](ibm_sv_manage_syslog_server_module.md#parameters)
- [Notes](ibm_sv_manage_syslog_server_module.md#notes)
- [Examples](ibm_sv_manage_syslog_server_module.md#examples)

## [Synopsis](ibm_sv_manage_syslog_server_module.md#id1)

- This Ansible module provides the interface to manage syslog servers through ‘mksyslogserver’, ‘chsyslogserver’ and ‘rmsyslogserver’ Storage Virtualize commands.

## [Parameters](ibm_sv_manage_syslog_server_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **audit**  string | Specifies whether the server receives CLI audit logs. The default value is off.  **Choices:**   - `"off"` - `"on"` |
| **cadf**  string | Specifies that Cloud Auditing Data Federation (CADF) data reporting be turned on or off. The parameters *facility* and I (cadf) are mutually exclusive.  **Choices:**   - `"off"` - `"on"` |
| **clustername**  string / required | The hostname or management IP of the Storage Virtualize system. |
| **domain**  string | Domain for the Storage Virtualize system.  Valid when hostname is used for the parameter *clustername*. |
| **error**  string | Specifies whether the server receives error notifications. If specified as on, error notifications are sent to the syslog server. The default value is on.  **Choices:**   - `"off"` - `"on"` |
| **facility**  integer | Specifies the facility number used in syslog messages. This number identifies the origin of the message to the receiving server. The default value is 0. The parameters *facility* and I (cadf) are mutually exclusive. |
| **info**  string | Specifies whether the server receives information notifications. If specified as on, information notifications are sent to the syslog server. The default value is on.  **Choices:**   - `"off"` - `"on"` |
| **ip**  string | Specifies the Internet Protocol (IP) address or domain name of the syslog server. If a domain name is specified, a DNS server must be configured on the system. |
| **log_path**  string | Path of debug log file. |
| **login**  string | Specifies whether the server receives authentication logs. The default value is off.  **Choices:**   - `"off"` - `"on"` |
| **name**  string / required | Specifies the name of a syslog server. |
| **old_name**  string | Specifies the old name of a syslog server to rename.  Valid when *state=present*, to rename the existing syslog server. |
| **password**  string | REST API password for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **port**  integer | Specifies the communication port that is used by this server. The parameter *protocol* must be specified while specifying this parameter. The default value is 514 for udp and 6514 for tcp. |
| **protocol**  string | Specifies the communication protocol that is used by this server. The default value is udp.  **Choices:**   - `"tcp"` - `"udp"` |
| **state**  string / required | Creates, updates (`present`) or deletes (`absent`) a syslog server.  **Choices:**   - `"present"` - `"absent"` |
| **token**  string | The authentication token to verify a user on the Storage Virtualize system.  To generate a token, use the [ibm.storage_virtualize.ibm_svc_auth](ibm_svc_auth_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-auth-module) module. |
| **username**  string | REST API username for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  **Choices:**   - `false` ← (default) - `true` |
| **warning**  string | Specifies whether the server receives warning notifications. If specified as on, warning notifications are sent to the syslog server. The default value is on.  **Choices:**   - `"off"` - `"on"` |

## [Notes](ibm_sv_manage_syslog_server_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_sv_manage_syslog_server_module.md#id4)

```yaml+jinja
- name: Create syslog server
  ibm.storage_virtualize.ibm_sv_manage_syslog_server:
   clustername: '{{clustername}}'
   username: '{{username}}'
   password: '{{password}}'
   name: server1
   ip: 1.2.3.4
   state: present
- name: Modify the server details
  ibm.storage_virtualize.ibm_sv_manage_syslog_server:
   clustername: '{{clustername}}'
   username: '{{username}}'
   password: '{{password}}'
   name: server1
   info: off
   state: present
- name: Delete the syslog server
  ibm.storage_virtualize.ibm_sv_manage_syslog_server:
   clustername: '{{clustername}}'
   username: '{{username}}'
   password: '{{password}}'
   name: server1
   state: absent
```

### Authors

- Shilpi Jain (@Shilpi-J)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.storage_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.storage_virtualize)
- [Report an issue](https://github.com/ansible-collections/community.REPO_NAME/issues/new/choose)
- [Communication](index.md#communication-for-ibm-storage-virtualize)
