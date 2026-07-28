---
collection: ansible
version: "8"
title: "dellemc.unity.nfsserver module – Manage NFS server on Unity storage system"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/unity/nfsserver_module.html
fetched_at: 2026-07-28T02:05:27+00:00
---
# dellemc.unity.nfsserver module – Manage NFS server on Unity storage system

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
> see [Requirements](nfsserver_module.md#ansible-collections-dellemc-unity-nfsserver-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.unity.nfsserver`.

New in dellemc.unity 1.4.0

- [Synopsis](nfsserver_module.md#synopsis)
- [Requirements](nfsserver_module.md#requirements)
- [Parameters](nfsserver_module.md#parameters)
- [Notes](nfsserver_module.md#notes)
- [Examples](nfsserver_module.md#examples)
- [Return Values](nfsserver_module.md#return-values)

## [Synopsis](nfsserver_module.md#id1)

- Managing the NFS server on the Unity storage system includes creating NFS server, getting NFS server details and deleting NFS server attributes.

## [Requirements](nfsserver_module.md#id2)

The below requirements are needed on the host that executes this module.

- A Dell Unity Storage device version 5.1 or later.
- Ansible-core 2.13 or later.
- Python 3.9, 3.10 or 3.11.
- Storops Python SDK 1.2.11.

## [Parameters](nfsserver_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **host_name**  string | Host name of the NFS server. |
| **is_extended_credentials_enabled**  boolean | Indicates whether support for more than 16 unix groups in a Unix credential.  **Choices:**   - `false` - `true` |
| **is_secure_enabled**  boolean | Indicates whether the secure NFS is enabled.  **Choices:**   - `false` - `true` |
| **kerberos_domain_controller_password**  string | Kerberos Domain Controller administrator password. |
| **kerberos_domain_controller_type**  string | Type of Kerberos Domain Controller used for secure NFS service.  **Choices:**   - `"CUSTOM"` - `"UNIX"` - `"WINDOWS"` |
| **kerberos_domain_controller_username**  string | Kerberos Domain Controller administrator username. |
| **nas_server_id**  string | ID of the NAS server on which NFS server will be hosted. |
| **nas_server_name**  string | Name of the NAS server on which NFS server will be hosted. |
| **nfs_server_id**  string | ID of the NFS server. |
| **nfs_v4_enabled**  boolean | Indicates whether the NFSv4 is enabled on the NAS server.  **Choices:**   - `false` - `true` |
| **password**  string / required | The password of the Unity management server. |
| **port**  integer | Port number through which communication happens with Unity management server.  **Default:** `443` |
| **remove_spn_from_kerberos**  boolean | Indicates whether to remove the SPN from Kerberos Domain Controller.  **Choices:**   - `false` - `true` ← (default) |
| **state**  string / required | Define whether the NFS server should exist or not.  **Choices:**   - `"absent"` - `"present"` |
| **unispherehost**  string / required | IP or FQDN of the Unity management server. |
| **username**  string / required | The username of the Unity management server. |
| **validate_certs**  aliases: verifycert  boolean | Boolean variable to specify whether or not to validate SSL certificate.  `true` - Indicates that the SSL certificate should be verified.  `false` - Indicates that the SSL certificate should not be verified.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](nfsserver_module.md#id4)

> **Note:**
>
> - The *check_mode* is supported.
> - Modify operation for NFS Server is not supported.
> - When *kerberos_domain_controller_type* is `UNIX`, *kdc_type* in *nfs_server_details* output is displayed as `null`.
> - The modules present in this collection named as ‘dellemc.unity’ are built to support the Dell Unity storage platform.

## [Examples](nfsserver_module.md#id5)

```yaml+jinja
- name: Create NFS server with kdctype as Windows
  dellemc.unity.nfsserver:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    nas_server_name: "dummy_nas"
    host_name: "dummy_nas23"
    is_secure_enabled: true
    kerberos_domain_controller_type: "WINDOWS"
    kerberos_domain_controller_username: "administrator"
    kerberos_domain_controller_password: "Password123!"
    is_extended_credentials_enabled: true
    nfs_v4_enabled: true
    state: "present"

- name: Create NFS server with kdctype as Unix
  dellemc.unity.nfsserver:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    nas_server_name: "dummy_nas"
    host_name: "dummy_nas23"
    is_secure_enabled: true
    kerberos_domain_controller_type: "UNIX"
    is_extended_credentials_enabled: true
    nfs_v4_enabled: true
    state: "present"

- name: Get NFS server details
  dellemc.unity.nfsserver:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    nas_server_name: "dummy_nas"
    state: "present"

- name: Delete NFS server
  dellemc.unity.nfsserver:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    nas_server_name: "dummy_nas"
    kerberos_domain_controller_username: "administrator"
    kerberos_domain_controller_password: "Password123!"
    unjoin_server_account: false
    state: "absent"
```

## [Return Values](nfsserver_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether or not the resource has changed.  **Returned:** always  **Sample:** `true` |
| **nfs_server_details**  dictionary | Details of the NFS server.  **Returned:** When NFS server exists  **Sample:** `{"credentials_cache_ttl": "0:15:00", "existed": true, "file_interfaces": {"UnityFileInterfaceList": [{"UnityFileInterface": {"hash": 8778980109421, "id": "if_37"}}]}, "hash": 8778980109388, "host_name": "dummy_nas23.pie.lab.emc.com", "id": "nfs_51", "is_extended_credentials_enabled": true, "is_secure_enabled": true, "kdc_type": "KdcTypeEnum.WINDOWS", "nas_server": {"UnityNasServer": {"hash": 8778980109412}}, "nfs_v4_enabled": true, "servicee_principal_name": null}` |
| **credentials_cache_ttl**  string | Credential cache refresh timeout. Resolution is in minutes. Default value is 15 minutes.  **Returned:** success |
| **existed**  boolean | Indicates if NFS Server exists.  **Returned:** success |
| **host_name**  string | Host name of the NFS server.  **Returned:** success |
| **id**  string | Unique identifier of the NFS Server instance.  **Returned:** success |
| **is_extended_credentials_enabled**  boolean | Indicates whether the NFS server supports more than 16 Unix groups in a Unix credential.  **Returned:** success |
| **is_secure_enabled**  boolean | Indicates whether secure NFS is enabled on the NFS server.  **Returned:** success |
| **kdc_type**  string | Type of Kerberos Domain Controller used for secure NFS service.  **Returned:** success |
| **nfs_v4_enabled**  boolean | Indicates whether NFSv4 is enabled on the NAS server.  **Returned:** success |
| **servicee_principal_name**  string | The Service Principal Name (SPN) for the NFS Server.  **Returned:** success |

### Authors

- Meenakshi Dembi (@dembim)

### Collection links

- [Issue Tracker](https://www.dell.com/community/Automation/bd-p/Automation)
- [Repository (Sources)](https://github.com/dell/ansible-unity/tree/1.7.1)
