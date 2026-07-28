---
collection: ansible
version: "6"
title: "netapp_eseries.santricity.netapp_e_auth module – NetApp E-Series set or update the password for a storage array."
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp_eseries/santricity/netapp_e_auth_module.html
fetched_at: 2026-07-28T00:14:14+00:00
---
# netapp_eseries.santricity.netapp_e_auth module – NetApp E-Series set or update the password for a storage array.

> **Note:**
>
> This module is part of the [netapp_eseries.santricity collection](https://galaxy.ansible.com/netapp_eseries/santricity) (version 1.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp_eseries.santricity`.
>
> To use it in a playbook, specify: `netapp_eseries.santricity.netapp_e_auth`.

New in netapp_eseries.santricity 2.2

- [Synopsis](netapp_e_auth_module.md#synopsis)
- [Parameters](netapp_e_auth_module.md#parameters)
- [Examples](netapp_e_auth_module.md#examples)
- [Return Values](netapp_e_auth_module.md#return-values)

## [Synopsis](netapp_e_auth_module.md#id1)

- Sets or updates the password for a storage array. When the password is updated on the storage array, it must be updated on the SANtricity Web Services proxy. Note, all storage arrays do not have a Monitor or RO role.

## [Parameters](netapp_e_auth_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_password**  string | The password used to authenticate against the API  This can optionally be set via an environment variable, API_PASSWORD |
| **api_url**  string | The full API url.  Example: <http://ENDPOINT:8080/devmgr/v2>  This can optionally be set via an environment variable, API_URL |
| **api_username**  string | The username used to authenticate against the API  This can optionally be set via an environment variable, API_USERNAME |
| **current_password**  string | The current admin password. This is not required if the password hasn’t been set before. |
| **name**  string | The name of the storage array. Note that if more than one storage array with this name is detected, the task will fail and you’ll have to use the ID instead. |
| **new_password**  string / required | The password you would like to set. Cannot be more than 30 characters. |
| **set_admin**  boolean | Boolean value on whether to update the admin password. If set to false then the RO account is updated.  Choices:   - `false` ← (default) - `true` |
| **ssid**  string | the identifier of the storage array in the Web Services Proxy. |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |

## [Examples](netapp_e_auth_module.md#id3)

```yaml+jinja
- name: Test module
  netapp_e_auth:
    name: trex
    current_password: OldPasswd
    new_password: NewPasswd
    set_admin: yes
    api_url: '{{ netapp_api_url }}'
    api_username: '{{ netapp_api_username }}'
    api_password: '{{ netapp_api_password }}'
```

## [Return Values](netapp_e_auth_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Success message  Returned: success  Sample: `"Password Updated Successfully"` |

### Authors

- Kevin Hulquest (@hulquest)

### Collection links

[Issue Tracker](https://github.com/netappeseries/santricity/issues)
[Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
