---
collection: ansible
version: "6"
title: "netapp.storagegrid.na_sg_grid_account module – NetApp StorageGRID manage accounts."
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/storagegrid/na_sg_grid_account_module.html
fetched_at: 2026-07-28T00:13:35+00:00
---
# netapp.storagegrid.na_sg_grid_account module – NetApp StorageGRID manage accounts.

> **Note:**
>
> This module is part of the [netapp.storagegrid collection](https://galaxy.ansible.com/netapp/storagegrid) (version 21.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.storagegrid`.
>
> To use it in a playbook, specify: `netapp.storagegrid.na_sg_grid_account`.

New in netapp.storagegrid 20.6.0

- [Synopsis](na_sg_grid_account_module.md#synopsis)
- [Parameters](na_sg_grid_account_module.md#parameters)
- [Notes](na_sg_grid_account_module.md#notes)
- [Examples](na_sg_grid_account_module.md#examples)
- [Return Values](na_sg_grid_account_module.md#return-values)

## [Synopsis](na_sg_grid_account_module.md#id1)

- Create, Update, Delete Tenant Accounts on NetApp StorageGRID.

## [Parameters](na_sg_grid_account_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **account_id**  string | Account Id of the tenant.  May be used for modify or delete operation. |
| **allow_platform_services**  boolean | Allows tenant to use platform services features such as CloudMirror.  Choices:   - `false` - `true` |
| **api_url**  string / required | The url to the StorageGRID Admin Node REST API. |
| **auth_token**  string / required | The authorization token for the API request |
| **management**  boolean | Whether the tenant can login to the StorageGRID tenant portal.  Choices:   - `false` - `true` ← (default) |
| **name**  string | Name of the tenant.  Required for create or modify operation. |
| **password**  string | Root password for tenant account.  Requires root privilege. |
| **protocol**  string | Object Storage protocol used by the tenancy.  Required for create operation.  Choices:   - `"s3"` - `"swift"` |
| **quota_size**  integer | Quota to apply to the tenant specified in *quota_size_unit*.  If you intend to have no limits, assign `0`.  Default: `0` |
| **quota_size_unit**  string | The unit used to interpret the size parameter.  Choices:   - `"bytes"` - `"b"` - `"kb"` - `"mb"` - `"gb"` ← (default) - `"tb"` - `"pb"` - `"eb"` - `"zb"` - `"yb"` |
| **root_access_group**  string  added in netapp.storagegrid 20.11.0 | Existing federated group to have initial Root Access permissions for the tenant.  Must begin with `federated-group/` |
| **state**  string | Whether the specified account should exist or not.  Required for all operations.  Choices:   - `"present"` ← (default) - `"absent"` |
| **update_password**  string | Choose when to update the password.  When set to `always`, the password will always be updated.  When set to `on_create` the password will only be set upon a new user creation.  Choices:   - `"on_create"` ← (default) - `"always"` |
| **use_own_identity_source**  boolean | Whether the tenant account should configure its own identity source.  Choices:   - `false` - `true` |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |

## [Notes](na_sg_grid_account_module.md#id3)

> **Note:**
>
> - The modules prefixed with `na_sg` are built to manage NetApp StorageGRID.

## [Examples](na_sg_grid_account_module.md#id4)

```yaml+jinja
- name: create a tenant account
  netapp.storagegrid.na_sg_grid_account:
    api_url: "https://<storagegrid-endpoint-url>"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
    state: present
    name: storagegrid-tenant-1
    protocol: s3
    management: true
    use_own_identity_source: false
    allow_platform_services: false
    password: "tenant-password"
    quota_size: 0

- name: update a tenant account
  netapp.storagegrid.na_sg_grid_account:
    api_url: "https://<storagegrid-endpoint-url>"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
    state: present
    name: storagegrid-tenant-1
    protocol: s3
    management: true
    use_own_identity_source: false
    allow_platform_services: true
    password: "tenant-password"
    quota_size: 10240

- name: delete a tenant account
  netapp.storagegrid.na_sg_grid_account:
    api_url: "https://<storagegrid-endpoint-url>"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
    state: absent
    name: storagegrid-tenant-1
    protocol: s3
```

## [Return Values](na_sg_grid_account_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resp**  dictionary | Returns information about the StorageGRID tenant account.  Returned: success  Sample: `{"capabilities": ["management", "s3"], "id": "12345678901234567890", "name": "Example Account", "policy": {"allowPlatformServices": false, "quotaObjectBytes": 100000000000, "useAccountIdentitySource": true}}` |

### Authors

- NetApp Ansible Team (@joshedmonds)

### Collection links

[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.storagegrid)
