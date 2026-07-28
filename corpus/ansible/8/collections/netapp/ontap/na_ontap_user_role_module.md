---
collection: ansible
version: "8"
title: "netapp.ontap.na_ontap_user_role module – NetApp ONTAP user role configuration and management"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/ontap/na_ontap_user_role_module.html
fetched_at: 2026-07-28T02:43:32+00:00
---
# netapp.ontap.na_ontap_user_role module – NetApp ONTAP user role configuration and management

> **Note:**
>
> This module is part of the [netapp.ontap collection](https://galaxy.ansible.com/ui/repo/published/netapp/ontap/) (version 22.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.ontap`.
> You need further requirements to be able to use this module,
> see [Requirements](na_ontap_user_role_module.md#ansible-collections-netapp-ontap-na-ontap-user-role-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_user_role`.

New in netapp.ontap 2.6.0

- [Synopsis](na_ontap_user_role_module.md#synopsis)
- [Requirements](na_ontap_user_role_module.md#requirements)
- [Parameters](na_ontap_user_role_module.md#parameters)
- [Notes](na_ontap_user_role_module.md#notes)
- [Examples](na_ontap_user_role_module.md#examples)

## [Synopsis](na_ontap_user_role_module.md#id1)

- Create or destroy user roles

## [Requirements](na_ontap_user_role_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_user_role_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_level**  string | The access level of the role.  Use `privileges` for rest-role access choices.  **Choices:**   - `"none"` - `"readonly"` - `"all"` ← (default) |
| **cert_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **command_directory_name**  string | The command or command directory to which the role has an access.  Required with ZAPI.  Supported with REST from ONTAP 9.11.1 or later. |
| **feature_flags**  dictionary  *added in netapp.ontap 20.5.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_ontap_version**  string  *added in netapp.ontap 21.23.0* | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  **Choices:**   - `false` ← (default) - `true` |
| **key_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client key file. |
| **name**  string / required | The name of the role to manage. |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **privileges**  list / elements=dictionary  *added in netapp.ontap 21.23.0* | Privileges to give the user roles  REST only |
| **access**  string | The access level of the role.  For command/command directory path, the only supported enum values are ‘none’,’readonly’ and ‘all’.  Options ‘read_create’, ‘read_modify’ and ‘read_create_modify’ are supported only with REST and requires ONTAP 9.11.1 or later versions.  **Choices:**   - `"none"` - `"readonly"` - `"all"` ← (default) - `"read_create"` - `"read_modify"` - `"read_create_modify"` |
| **path**  string / required | The api or command to which the role has an access.  command or command directory path is supported from ONTAP 9.11.1 or later versions.  Only rest roles are supported for earlier versions. |
| **query**  string | A query for the role. The query must apply to the specified command or directory name.  Query is only supported on 9.11.1+ |
| **query**  string  *added in netapp.ontap 2.8.0* | A query for the role. The query must apply to the specified command or directory name.  Use double quotes “” for modifying a existing query to none.  Supported with REST from ONTAP 9.11.1 or later. |
| **state**  string | Whether the specified user role should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  **Default:** `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **vserver**  string | The name of the vserver to use.  Required with ZAPI. |

## [Notes](na_ontap_user_role_module.md#id4)

> **Note:**
>
> - supports ZAPI and REST. REST requires ONTAP 9.7 or later.
> - supports check mode.
> - when trying to add a command to a role, ONTAP will affect other related commands too.
> - for example, ‘volume modify’ will affect ‘volume create’ and ‘volume show’, always provide all the related commands.
> - REST supports both role and rest-role from ONTAP 9.11.1 or later versions and only rest-role for earlier versions.
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_user_role_module.md#id5)

```yaml+jinja
- name: Create User Role Zapi
  netapp.ontap.na_ontap_user_role:
    state: present
    name: ansibleRole
    command_directory_name: volume
    access_level: none
    query: show
    vserver: ansibleVServer
    use_rest: never
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Modify User Role Zapi
  netapp.ontap.na_ontap_user_role:
    state: present
    name: ansibleRole
    command_directory_name: volume
    access_level: none
    query: ""
    vserver: ansibleVServer
    use_rest: never
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Create user role REST in ONTAP 9.11.1.
  netapp.ontap.na_ontap_user_role:
    state: present
    privileges:
      - path: /api/cluster/jobs
    vserver: ansibleSVM
    name: carchi-test-role
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Modify user role REST in ONTAP 9.11.1.
  netapp.ontap.na_ontap_user_role:
    state: present
    privileges:
      - path: /api/cluster/jobs
        access: readonly
      - path: /api/storage/volumes
        access: readonly
    vserver: ansibleSVM
    name: carchi-test-role
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
