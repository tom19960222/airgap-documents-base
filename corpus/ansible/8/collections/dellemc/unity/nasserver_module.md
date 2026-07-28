---
collection: ansible
version: "8"
title: "dellemc.unity.nasserver module – Manage NAS servers on Unity storage system"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/unity/nasserver_module.html
fetched_at: 2026-07-28T02:05:25+00:00
---
# dellemc.unity.nasserver module – Manage NAS servers on Unity storage system

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
> see [Requirements](nasserver_module.md#ansible-collections-dellemc-unity-nasserver-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.unity.nasserver`.

New in dellemc.unity 1.1.0

- [Synopsis](nasserver_module.md#synopsis)
- [Requirements](nasserver_module.md#requirements)
- [Parameters](nasserver_module.md#parameters)
- [Notes](nasserver_module.md#notes)
- [Examples](nasserver_module.md#examples)
- [Return Values](nasserver_module.md#return-values)

## [Synopsis](nasserver_module.md#id1)

- Managing NAS servers on Unity storage system includes get, modification to the NAS servers.

Aliases: dellemc_unity_nasserver

## [Requirements](nasserver_module.md#id2)

The below requirements are needed on the host that executes this module.

- A Dell Unity Storage device version 5.1 or later.
- Ansible-core 2.13 or later.
- Python 3.9, 3.10 or 3.11.
- Storops Python SDK 1.2.11.

## [Parameters](nasserver_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allow_unmapped_user**  boolean | This flag is used to mandatorily disable access in case of any user mapping failure.  If `true`, then enable access in case of any user mapping failure.  If `false`, then disable access in case of any user mapping failure.  It can be mentioned during modification of the NAS server.  **Choices:**   - `false` - `true` |
| **current_unix_directory_service**  string | This is the directory service used for querying identity information for UNIX (such as UIDs, GIDs, net groups).  It can be mentioned during modification of the NAS server.  **Choices:**   - `"NONE"` - `"NIS"` - `"LOCAL"` - `"LDAP"` - `"LOCAL_THEN_NIS"` - `"LOCAL_THEN_LDAP"` |
| **default_unix_user**  string | Default Unix user name used for granting access in the case of Windows to Unix user mapping failure.  It can be mentioned during modification of the NAS server. |
| **default_windows_user**  string | Default windows user name used for granting access in the case of Unix to Windows user mapping failure.  It can be mentioned during modification of the NAS server. |
| **enable_windows_to_unix_username_mapping**  boolean | This parameter indicates whether a Unix to/from Windows user name mapping is enabled.  It can be mentioned during modification of the NAS server.  **Choices:**   - `false` - `true` |
| **is_backup_only**  boolean | It specifies whether the NAS server is used as backup only.  It can be mentioned during modification of the NAS server.  **Choices:**   - `false` - `true` |
| **is_multiprotocol_enabled**  boolean | This parameter indicates whether multiprotocol sharing mode is enabled.  It can be mentioned during modification of the NAS server.  **Choices:**   - `false` - `true` |
| **is_packet_reflect_enabled**  boolean | If the packet has to be reflected, then this parameter has to be set to `true`.  It can be mentioned during modification of the NAS server.  **Choices:**   - `false` - `true` |
| **is_replication_destination**  boolean | It specifies whether the NAS server is a replication destination.  It can be mentioned during modification of the NAS server.  **Choices:**   - `false` - `true` |
| **nas_server_id**  string | The ID of the NAS server.  Either *nas_server_name* or *nas_server_id* is required to perform the task.  The parameters *nas_server_name* and *nas_server_id* are mutually exclusive. |
| **nas_server_name**  string | The Name of the NAS server.  Either *nas_server_name* or *nas_server_id* is required to perform the task.  The parameters *nas_server_name* and *nas_server_id* are mutually exclusive. |
| **nas_server_new_name**  string | The new name of the NAS server.  It can be mentioned during modification of the NAS server. |
| **password**  string / required | The password of the Unity management server. |
| **port**  integer | Port number through which communication happens with Unity management server.  **Default:** `443` |
| **replication_params**  dictionary | Settings required for enabling replication. |
| **destination_nas_server_name**  string | Name of the destination nas server.  Default value will be source nas server name prefixed by ‘DR_’. |
| **destination_pool_id**  string | Id of pool to allocate destination Luns.  Mutually exclusive with *destination_pool_name*. |
| **destination_pool_name**  string | Name of pool to allocate destination Luns.  Mutually exclusive with *destination_pool_id*. |
| **destination_sp**  string | Storage process of destination nas server  **Choices:**   - `"SPA"` - `"SPB"` |
| **is_backup**  boolean | Indicates if the destination nas server is backup.  **Choices:**   - `false` - `true` |
| **new_replication_name**  string | Replication name to rename the session to. |
| **remote_system**  dictionary | Details of remote system to which the replication is being configured.  The *remote_system* option should be specified if the *replication_type* is `remote`. |
| **remote_system_host**  string / required | IP or FQDN for remote Unity unisphere Host. |
| **remote_system_password**  string / required | Password of remote Unity unisphere Host. |
| **remote_system_port**  integer | Port at which remote Unity unisphere is hosted.  **Default:** `443` |
| **remote_system_username**  string / required | User name of remote Unity unisphere Host. |
| **remote_system_verifycert**  boolean | Boolean variable to specify whether or not to validate SSL certificate of remote Unity unisphere Host.  `true` - Indicates that the SSL certificate should be verified.  `false` - Indicates that the SSL certificate should not be verified.  **Choices:**   - `false` - `true` ← (default) |
| **replication_mode**  string | The replication mode.  This is mandatory to enable replication.  **Choices:**   - `"asynchronous"` - `"manual"` |
| **replication_name**  string | User defined name for replication session. |
| **replication_type**  string | Type of replication.  **Choices:**   - `"local"` - `"remote"` |
| **rpo**  integer | Maximum time to wait before the system syncs the source and destination LUNs.  The *rpo* option should be specified if the *replication_mode* is `asynchronous`.  The value should be in range of `5` to `1440`. |
| **replication_reuse_resource**  boolean | This parameter indicates if existing NAS Server is to be used for replication.  **Choices:**   - `false` - `true` |
| **replication_state**  string | State of the replication.  **Choices:**   - `"enable"` - `"disable"` |
| **state**  string / required | Define the state of NAS server on the array.  The value present indicates that NAS server should exist on the system after the task is executed.  In this release deletion of NAS server is not supported. Hence, if state is set to `absent` for any existing NAS server then error will be thrown.  For any non-existing NAS server, if state is set to `absent` then it will return None.  **Choices:**   - `"present"` - `"absent"` |
| **unispherehost**  string / required | IP or FQDN of the Unity management server. |
| **username**  string / required | The username of the Unity management server. |
| **validate_certs**  aliases: verifycert  boolean | Boolean variable to specify whether or not to validate SSL certificate.  `true` - Indicates that the SSL certificate should be verified.  `false` - Indicates that the SSL certificate should not be verified.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](nasserver_module.md#id4)

> **Note:**
>
> - The *check_mode* is not supported.
> - The modules present in this collection named as ‘dellemc.unity’ are built to support the Dell Unity storage platform.

## [Examples](nasserver_module.md#id5)

```yaml+jinja
- name: Get Details of NAS Server
  dellemc.unity.nasserver:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    nas_server_name: "{{nas_server_name}}"
    state: "present"

- name: Modify Details of NAS Server
  dellemc.unity.nasserver:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    nas_server_name: "{{nas_server_name}}"
    nas_server_new_name: "updated_sample_nas_server"
    is_replication_destination: false
    is_backup_only: false
    is_multiprotocol_enabled: true
    allow_unmapped_user: true
    default_unix_user: "default_unix_sample_user"
    default_windows_user: "default_windows_sample_user"
    enable_windows_to_unix_username_mapping: true
    current_unix_directory_service: "LDAP"
    is_packet_reflect_enabled: true
    state: "present"

- name: Enable replication for NAS Server on Local System
  dellemc.unity.nasserver:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    nas_server_id: "nas_10"
    replication_reuse_resource: false
    replication_params:
      replication_name: "test_replication"
      destination_nas_server_name: "destination_nas"
      replication_mode: "asynchronous"
      rpo: 60
      replication_type: "local"
      destination_pool_name: "Pool_Ansible_Neo_DND"
      destination_sp: "SPA"
      is_backup: true
    replication_state: "enable"
    state: "present"

- name: Enable replication for NAS Server on Remote System
  dellemc.unity.nasserver:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    nas_server_name: "dummy_nas"
    replication_reuse_resource: false
    replication_params:
      replication_name: "test_replication"
      destination_nas_server_name: "destination_nas"
      replication_mode: "asynchronous"
      rpo: 60
      replication_type: "remote"
      remote_system:
        remote_system_host: '10.10.10.10'
        remote_system_verifycert: false
        remote_system_username: 'test1'
        remote_system_password: 'test1!'
      destination_pool_name: "fastVP_pool"
      destination_sp: "SPA"
      is_backup: true
    replication_state: "enable"
    state: "present"

- name: Enable replication for NAS Server on Remote System in existing NAS Server
  dellemc.unity.nasserver:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    nas_server_name: "dummy_nas"
    replication_reuse_resource: true
    replication_params:
      destination_nas_server_name: "destination_nas"
      replication_mode: "asynchronous"
      rpo: 60
      replication_type: "remote"
      replication_name: "test_replication"
      remote_system:
        remote_system_host: '10.10.10.10'
        remote_system_verifycert: false
        remote_system_username: 'test1'
        remote_system_password: 'test1!'
      destination_pool_name: "fastVP_pool"
    replication_state: "enable"
    state: "present"

- name: Modify replication on the nasserver
  dellemc.unity.nasserver:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    nas_server_name: "dummy_nas"
    replication_params:
        replication_name: "test_repl"
        new_replication_name: "test_repl_updated"
        replication_mode: "asynchronous"
        rpo: 50
    replication_state: "enable"
    state: "present"

- name: Disable replication on the nasserver
  dellemc.unity.nasserver:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    nas_server_name: "dummy_nas"
    replication_state: "disable"
    state: "present"

- name: Disable replication by specifying replication_name on the nasserver
  dellemc.unity.nasserver:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    nas_server_name: "dummy_nas"
    replication_params:
        replication_name: "test_replication"
    replication_state: "disable"
    state: "present"
```

## [Return Values](nasserver_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether or not the resource has changed.  **Returned:** always  **Sample:** `true` |
| **nas_server_details**  dictionary | The NAS server details.  **Returned:** When NAS server exists.  **Sample:** `{"allow_unmapped_user": null, "cifs_server": {"UnityCifsServerList": [{"UnityCifsServer": {"hash": 8761756885270, "id": "cifs_34"}}]}, "current_sp": {"UnityStorageProcessor": {"hash": 8761756885273, "id": "spb"}}, "current_unix_directory_service": "NasServerUnixDirectoryServiceEnum.NIS", "default_unix_user": null, "default_windows_user": null, "existed": true, "file_dns_server": {"UnityFileDnsServer": {"hash": 8761756885441, "id": "dns_12"}}, "file_interface": {"UnityFileInterfaceList": [{"UnityFileInterface": {"hash": 8761756889908, "id": "if_37"}}]}, "filesystems": null, "hash": 8761757005084, "health": {"UnityHealth": {"hash": 8761756867588}}, "home_sp": {"UnityStorageProcessor": {"hash": 8761756867618, "id": "spb"}}, "id": "nas_10", "is_backup_only": false, "is_multi_protocol_enabled": false, "is_packet_reflect_enabled": false, "is_replication_destination": false, "is_replication_enabled": true, "is_windows_to_unix_username_mapping_enabled": null, "name": "dummy_nas", "pool": {"UnityPool": {"hash": 8761756885360, "id": "pool_7"}}, "preferred_interface_settings": {"UnityPreferredInterfaceSettings": {"hash": 8761756885438, "id": "preferred_if_10"}}, "replication_type": "ReplicationTypeEnum.REMOTE", "size_allocated": 3489660928, "tenant": null, "virus_checker": {"UnityVirusChecker": {"hash": 8761756885426, "id": "cava_10"}}}` |
| **allow_unmapped_user**  boolean | Enable/disable access status in case of any user mapping failure.  **Returned:** success |
| **current_unix_directory_service**  string | Directory service used for querying identity information for UNIX (such as UIDs, GIDs, net groups).  **Returned:** success |
| **default_unix_user**  string | Default Unix user name used for granting access in the case of Windows to Unix user mapping failure.  **Returned:** success |
| **default_windows_user**  string | Default windows user name used for granting access in the case of Unix to Windows user mapping failure.  **Returned:** success |
| **id**  string | ID of the NAS server.  **Returned:** success |
| **is_backup_only**  boolean | Whether the NAS server is used as backup only.  **Returned:** success |
| **is_multi_protocol_enabled**  boolean | Indicates whether multiprotocol sharing mode is enabled.  **Returned:** success |
| **is_packet_reflect_enabled**  boolean | If the packet reflect has to be enabled.  **Returned:** success |
| **is_replication_destination**  boolean | If the NAS server is a replication destination then true.  **Returned:** success |
| **is_windows_to_unix_username_mapping_enabled**  boolean | Indicates whether a Unix to/from Windows user name mapping is enabled.  **Returned:** success |
| **name**  string | Name of the NAS server.  **Returned:** success |

### Authors

- P Srinivas Rao (@srinivas-rao5)

### Collection links

- [Issue Tracker](https://www.dell.com/community/Automation/bd-p/Automation)
- [Repository (Sources)](https://github.com/dell/ansible-unity/tree/1.7.1)
