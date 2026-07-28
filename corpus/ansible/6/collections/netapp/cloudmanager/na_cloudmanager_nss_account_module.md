---
collection: ansible
version: "6"
title: "netapp.cloudmanager.na_cloudmanager_nss_account module – NetApp Cloud Manager nss account"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/cloudmanager/na_cloudmanager_nss_account_module.html
fetched_at: 2026-07-28T00:11:39+00:00
---
# netapp.cloudmanager.na_cloudmanager_nss_account module – NetApp Cloud Manager nss account

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
> To use it in a playbook, specify: `netapp.cloudmanager.na_cloudmanager_nss_account`.

New in netapp.cloudmanager 21.3.0

- [Synopsis](na_cloudmanager_nss_account_module.md#synopsis)
- [Parameters](na_cloudmanager_nss_account_module.md#parameters)
- [Notes](na_cloudmanager_nss_account_module.md#notes)
- [Examples](na_cloudmanager_nss_account_module.md#examples)

## [Synopsis](na_cloudmanager_nss_account_module.md#id1)

- Create and Delete nss account.

## [Parameters](na_cloudmanager_nss_account_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **client_id**  string / required | The connector ID of the Cloud Manager Connector. |
| **environment**  string  added in netapp.cloudmanager 21.8.0 | The environment for NetApp Cloud Manager API operations.  Choices:   - `"prod"` ← (default) - `"stage"` |
| **feature_flags**  dictionary  added in netapp.cloudmanager 21.11.0 | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **name**  string | The name of the NSS account. |
| **password**  string | The NSS password. |
| **public_id**  string | The ID of the NSS account. |
| **refresh_token**  string | The refresh token for NetApp Cloud Manager API operations. |
| **sa_client_id**  string | The service account secret client ID for NetApp Cloud Manager API operations. |
| **sa_secret_key**  string | The service account secret key for NetApp Cloud Manager API operations. |
| **state**  string | Whether the specified nss account should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **username**  string / required | The NSS username. |
| **vsa_list**  list / elements=string | The working environment list. |

## [Notes](na_cloudmanager_nss_account_module.md#id3)

> **Note:**
>
> - Support check_mode.
> - The modules prefixed with na_cloudmanager are built to manage CloudManager and CVO deployments in AWS/GCP/Azure clouds.
> - If sa_client_id and sa_secret_key are provided, service account will be used in operations. refresh_token will be ignored.

## [Examples](na_cloudmanager_nss_account_module.md#id4)

```yaml+jinja
- name: Create nss account
  netapp.cloudmanager.na_cloudmanager_nss_account:
    state: present
    name: test_cloud
    username: test_cloud
    password: password
    client_id: your_client_id
    refresh_token: your_refresh_token
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.cloudmanager)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.cloudmanager)
