---
collection: ansible
version: "6"
title: "netapp.storagegrid.na_sg_org_user module – NetApp StorageGRID manage users within a tenancy."
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/storagegrid/na_sg_org_user_module.html
fetched_at: 2026-07-28T00:13:47+00:00
---
# netapp.storagegrid.na_sg_org_user module – NetApp StorageGRID manage users within a tenancy.

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
> To use it in a playbook, specify: `netapp.storagegrid.na_sg_org_user`.

New in netapp.storagegrid 20.6.0

- [Synopsis](na_sg_org_user_module.md#synopsis)
- [Parameters](na_sg_org_user_module.md#parameters)
- [Notes](na_sg_org_user_module.md#notes)
- [Examples](na_sg_org_user_module.md#examples)
- [Return Values](na_sg_org_user_module.md#return-values)

## [Synopsis](na_sg_org_user_module.md#id1)

- Create, Update, Delete Users within a NetApp StorageGRID tenant.

## [Parameters](na_sg_org_user_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_url**  string / required | The url to the StorageGRID Admin Node REST API. |
| **auth_token**  string / required | The authorization token for the API request |
| **disable**  boolean | Disable the user from signing in. Does not apply to federated users.  Choices:   - `false` - `true` |
| **full_name**  string | Full Name of the user.  Required for create operation |
| **member_of**  list / elements=string | List of unique_groups that the user is a member of. |
| **password**  string | Set a password for a local user. Does not apply to federated users.  Requires root privilege. |
| **state**  string | Whether the specified user should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **unique_name**  string / required | Unique Name for the user. Must begin with `user/` or `federated-user/`.  Required for create, modify or delete operation. |
| **update_password**  string | Choose when to update the password.  When set to `always`, the password will always be updated.  When set to `on_create`, the password will only be set upon a new user creation.  Choices:   - `"on_create"` ← (default) - `"always"` |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |

## [Notes](na_sg_org_user_module.md#id3)

> **Note:**
>
> - The modules prefixed with `na_sg` are built to manage NetApp StorageGRID.

## [Examples](na_sg_org_user_module.md#id4)

```yaml+jinja
- name: create a tenant user
  netapp.storagegrid.na_sg_org_user:
    api_url: "https://<storagegrid-endpoint-url>"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
    state: present
    full_name: ansibleuser1
    unique_name: user/ansibleuser1
    member_of: "group/ansiblegroup1"
    disable: false
```

## [Return Values](na_sg_org_user_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resp**  dictionary | Returns information about the StorageGRID tenant user.  Returned: always  Sample: `{"accountId": "0", "disable": false, "federated": false, "fullName": "Example User", "id": "00000000-0000-0000-0000-000000000000", "memberOf": ["00000000-0000-0000-0000-000000000000"], "uniqueName": "user/Example", "userURN": "urn:sgws:identity::0:user/Example"}` |

### Authors

- NetApp Ansible Team (@joshedmonds)

### Collection links

[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.storagegrid)
