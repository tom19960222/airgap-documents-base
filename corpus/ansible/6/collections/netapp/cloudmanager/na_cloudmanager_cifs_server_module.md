---
collection: ansible
version: "6"
title: "netapp.cloudmanager.na_cloudmanager_cifs_server module – NetApp Cloud Manager cifs server"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/cloudmanager/na_cloudmanager_cifs_server_module.html
fetched_at: 2026-07-27T17:55:53+00:00
---
# netapp.cloudmanager.na_cloudmanager_cifs_server module – NetApp Cloud Manager cifs server

> **Note:**
>
> This module is part of the [netapp.cloudmanager collection](https://galaxy.ansible.com/netapp/cloudmanager) (version 21.21.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.cloudmanager`.
>
> To use it in a playbook, specify: `netapp.cloudmanager.na_cloudmanager_cifs_server`.

New in netapp.cloudmanager 21.3.0

- [Synopsis](na_cloudmanager_cifs_server_module.md#synopsis)
- [Parameters](na_cloudmanager_cifs_server_module.md#parameters)
- [Notes](na_cloudmanager_cifs_server_module.md#notes)
- [Examples](na_cloudmanager_cifs_server_module.md#examples)

## [Synopsis](na_cloudmanager_cifs_server_module.md#id1)

- Create or Delete a CIFS server on the Cloud Volume ONTAP system to support CIFS volumes, based on an Active Directory or Workgroup.

## [Parameters](na_cloudmanager_cifs_server_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **client_id**  string / required | The connector ID of the Cloud Manager Connector. |
| **dns_domain**  string | The DNS domain name. For CIFS AD only. |
| **domain**  string | The active directory domain name. For CIFS AD only. |
| **environment**  string  added in netapp.cloudmanager 21.8.0 | The environment for NetApp Cloud Manager API operations.  Choices:   - `"prod"` ← (default) - `"stage"` |
| **feature_flags**  dictionary  added in netapp.cloudmanager 21.11.0 | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **ip_addresses**  list / elements=string | The DNS server IP addresses. For CIFS AD only. |
| **is_workgroup**  boolean | For CIFS workgroup operations, set to true.  Choices:   - `false` - `true` |
| **netbios**  string | The CIFS server NetBIOS name. For CIFS AD only. |
| **organizational_unit**  string | The organizational unit in which to register the CIFS server. For CIFS AD only. |
| **password**  string | The active directory admin password. For CIFS AD only. |
| **refresh_token**  string | The refresh token for NetApp Cloud Manager API operations. |
| **sa_client_id**  string | The service account secret client ID for NetApp Cloud Manager API operations. |
| **sa_secret_key**  string | The service account secret key for NetApp Cloud Manager API operations. |
| **server_name**  string | The server name. For CIFS workgroup only. |
| **state**  string | Whether the specified cifs server should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **username**  string | The active directory admin user name. For CIFS AD only. |
| **workgroup_name**  string | The workgroup name. For CIFS workgroup only. |
| **working_environment_id**  string | The public ID of the working environment where the cifs server will be created. |
| **working_environment_name**  string | The working environment name where the cifs server will be created. |

## [Notes](na_cloudmanager_cifs_server_module.md#id3)

> **Note:**
>
> - Support check_mode.
> - The modules prefixed with na_cloudmanager are built to manage CloudManager and CVO deployments in AWS/GCP/Azure clouds.
> - If sa_client_id and sa_secret_key are provided, service account will be used in operations. refresh_token will be ignored.

## [Examples](na_cloudmanager_cifs_server_module.md#id4)

```yaml+jinja
- name: Create cifs server with working_environment_id
  netapp.cloudmanager.na_cloudmanager_cifs_server:
    state: present
    working_environment_id: VsaWorkingEnvironment-abcdefgh
    client_id: your_client_id
    refresh_token: your_refresh_token
    domain: example.com
    username: admin
    password: pass
    dns_domain: example.com
    ip_addresses: ["1.0.0.0"]
    netbios: cvoname
    organizational_unit: CN=Computers
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.cloudmanager)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.cloudmanager)
