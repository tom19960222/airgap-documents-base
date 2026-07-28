---
collection: ansible
version: "8"
title: "dellemc.unity.cifsserver module – Manage CIFS server on Unity storage system"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/unity/cifsserver_module.html
fetched_at: 2026-07-28T02:05:20+00:00
---
# dellemc.unity.cifsserver module – Manage CIFS server on Unity storage system

> **Note:**
>
> This module is part of the [dellemc.unity collection](https://galaxy.ansible.com/ui/repo/published/dellemc/unity/) (version 1.7.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.unity`.
> You need further requirements to be able to use this module,
> see [Requirements](cifsserver_module.md#ansible-collections-dellemc-unity-cifsserver-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.unity.cifsserver`.

New in dellemc.unity 1.4.0

- [Synopsis](cifsserver_module.md#synopsis)
- [Requirements](cifsserver_module.md#requirements)
- [Parameters](cifsserver_module.md#parameters)
- [Notes](cifsserver_module.md#notes)
- [Examples](cifsserver_module.md#examples)
- [Return Values](cifsserver_module.md#return-values)

## [Synopsis](cifsserver_module.md#id1)

- Managing the CIFS server on the Unity storage system includes creating CIFS server, getting CIFS server details and deleting CIFS server.

## [Requirements](cifsserver_module.md#id2)

The below requirements are needed on the host that executes this module.

- A Dell Unity Storage device version 5.1 or later.
- Ansible-core 2.13 or later.
- Python 3.9, 3.10 or 3.11.
- Storops Python SDK 1.2.11.

## [Parameters](cifsserver_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cifs_server_id**  string | The ID of the CIFS server. |
| **cifs_server_name**  string | The name of the CIFS server. |
| **domain**  string | The domain name where the SMB server is registered in Active Directory. |
| **domain_password**  string | Active Directory domain password. |
| **domain_username**  string | Active Directory domain user name. |
| **interfaces**  list / elements=string | List of file IP interfaces that service CIFS protocol of SMB server. |
| **local_password**  string | Standalone SMB server administrator password. |
| **nas_server_id**  string | ID of the NAS server on which CIFS server will be hosted. |
| **nas_server_name**  string | Name of the NAS server on which CIFS server will be hosted. |
| **netbios_name**  string | The computer name of the SMB server in Windows network. |
| **password**  string / required | The password of the Unity management server. |
| **port**  integer | Port number through which communication happens with Unity management server.  **Default:** `443` |
| **state**  string / required | Define whether the CIFS server should exist or not.  **Choices:**   - `"absent"` - `"present"` |
| **unispherehost**  string / required | IP or FQDN of the Unity management server. |
| **unjoin_cifs_server_account**  boolean | Keep SMB server account unjoined in Active Directory after deletion.  `false` specifies keep SMB server account joined after deletion.  `true` specifies unjoin SMB server account from Active Directory before deletion.  **Choices:**   - `false` - `true` |
| **username**  string / required | The username of the Unity management server. |
| **validate_certs**  aliases: verifycert  boolean | Boolean variable to specify whether or not to validate SSL certificate.  `true` - Indicates that the SSL certificate should be verified.  `false` - Indicates that the SSL certificate should not be verified.  **Choices:**   - `false` - `true` ← (default) |
| **workgroup**  string | Standalone SMB server workgroup. |

## [Notes](cifsserver_module.md#id4)

> **Note:**
>
> - The *check_mode* is supported.
> - The modules present in this collection named as ‘dellemc.unity’ are built to support the Dell Unity storage platform.

## [Examples](cifsserver_module.md#id5)

```yaml+jinja
- name: Create CIFS server belonging to Active Directory
  dellemc.unity.cifsserver:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    nas_server_name: "test_nas1"
    cifs_server_name: "test_cifs"
    domain: "ad_domain"
    domain_username: "domain_username"
    domain_password: "domain_password"
    state: "present"

- name: Get CIFS server details using CIFS server ID
  dellemc.unity.cifsserver:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    cifs_server_id: "cifs_37"
    state: "present"

- name: Get CIFS server details using NAS server name
  dellemc.unity.cifsserver:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    nas_server_name: "test_nas1"
    state: "present"

- name: Delete CIFS server
  dellemc.unity.cifsserver:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    cifs_server_id: "cifs_37"
    unjoin_cifs_server_account: true
    domain_username: "domain_username"
    domain_password: "domain_password"
    state: "absent"

- name: Create standalone CIFS server
  dellemc.unity.cifsserver:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    netbios_name: "ANSIBLE_CIFS"
    workgroup: "ansible"
    local_password: "Password123!"
    nas_server_name: "test_nas1"
    state: "present"

- name: Get CIFS server details using netbios name
  dellemc.unity.cifsserver:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    netbios_name: "ANSIBLE_CIFS"
    state: "present"

- name: Delete standalone CIFS server
  dellemc.unity.cifsserver:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    cifs_server_id: "cifs_40"
    state: "absent"
```

## [Return Values](cifsserver_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether or not the resource has changed.  **Returned:** always  **Sample:** `true` |
| **cifs_server_details**  dictionary | Details of the CIFS server.  **Returned:** When CIFS server exists  **Sample:** `{"description": null, "domain": "xxx.xxx.xxx.com", "existed": true, "file_interfaces": {"UnityFileInterfaceList": [{"UnityFileInterface": {"hash": -9223363258905013637, "id": "if_43"}}]}, "hash": -9223363258905010379, "health": {"UnityHealth": {"hash": 8777949765559}}, "id": "cifs_40", "is_standalone": false, "last_used_organizational_unit": "ou=Computers,ou=Dell NAS servers", "name": "ansible_cifs", "nas_server": {"UnityNasServer": {"hash": 8777949765531, "id": "nas_18"}}, "netbios_name": "ANSIBLE_CIFS", "smb_multi_channel_supported": true, "smb_protocol_versions": ["1.0", "2.0", "2.1", "3.0"], "smbca_supported": true, "workgroup": null}` |
| **description**  string | Description of the SMB server.  **Returned:** success |
| **domain**  string | Domain name where SMB server is registered in Active Directory.  **Returned:** success |
| **file_interfaces**  dictionary | The file interfaces associated with the NAS server.  **Returned:** success |
| **UnityFileInterfaceList**  list / elements=string | List of file interfaces associated with the NAS server.  **Returned:** success |
| **UnityFileInterface**  dictionary | Details of file interface associated with the NAS server.  **Returned:** success |
| **id**  string | Unique identifier of the file interface.  **Returned:** success |
| **id**  string | Unique identifier of the CIFS server instance.  **Returned:** success |
| **is_standalone**  boolean | Indicates whether the SMB server is standalone.  **Returned:** success |
| **name**  string | User-specified name for the SMB server.  **Returned:** success |
| **nasServer**  dictionary | Information about the NAS server in the storage system.  **Returned:** success |
| **UnityNasServer**  dictionary | Information about the NAS server in the storage system.  **Returned:** success |
| **id**  string | Unique identifier of the NAS server instance.  **Returned:** success |
| **netbios_name**  string | Computer Name of the SMB server in windows network.  **Returned:** success |
| **smb_multi_channel_supported**  boolean | Indicates whether the SMB 3.0+ multichannel feature is supported.  **Returned:** success |
| **smb_protocol_versions**  list / elements=string | Supported SMB protocols, such as 1.0, 2.0, 2.1, 3.0, and so on.  **Returned:** success |
| **smbca_supported**  boolean | Indicates whether the SMB server supports continuous availability.  **Returned:** success |
| **workgroup**  string | Windows network workgroup for the SMB server.  **Returned:** success |

### Authors

- Akash Shendge (@shenda1)

### Collection links

- [Issue Tracker](https://www.dell.com/community/Automation/bd-p/Automation)
- [Repository (Sources)](https://github.com/dell/ansible-unity/tree/1.7.1)
