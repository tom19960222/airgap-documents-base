---
collection: ansible
version: "8"
title: "community.grafana.grafana_user module – Manage Grafana User"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/grafana/grafana_user_module.html
fetched_at: 2026-07-28T01:53:18+00:00
---
# community.grafana.grafana_user module – Manage Grafana User

> **Note:**
>
> This module is part of the [community.grafana collection](https://galaxy.ansible.com/ui/repo/published/community/grafana/) (version 1.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.grafana`.
>
> To use it in a playbook, specify: `community.grafana.grafana_user`.

New in community.grafana 1.0.0

- [Synopsis](grafana_user_module.md#synopsis)
- [Parameters](grafana_user_module.md#parameters)
- [Notes](grafana_user_module.md#notes)
- [Examples](grafana_user_module.md#examples)
- [Return Values](grafana_user_module.md#return-values)

## [Synopsis](grafana_user_module.md#id1)

- Create/update/delete Grafana User through the users and admin API.
- Tested with Grafana v6.4.3
- Password update is not supported at the time

## [Parameters](grafana_user_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **client_cert**  path | PEM formatted certificate chain file to be used for SSL client authentication.  This file can also include the key as well, and if the key is included, *client_key* is not required |
| **client_key**  path | PEM formatted file that contains your private key to be used for SSL client authentication.  If *client_cert* contains both the certificate and key, this option is not required. |
| **email**  string | The email of the Grafana User. |
| **is_admin**  boolean | The Grafana User is an admin.  **Choices:**   - `false` ← (default) - `true` |
| **login**  string / required | The login of the Grafana User. |
| **name**  string | The name of the Grafana User. |
| **password**  string | The password of the Grafana User.  At the moment, this field is not updated yet. |
| **state**  string | State if the user should be present in Grafana or not  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **url**  aliases: grafana_url  string / required | The Grafana URL. |
| **url_password**  aliases: grafana_password  string | The Grafana password for API authentication.  **Default:** `"admin"` |
| **url_username**  aliases: grafana_user  string | The Grafana user for API authentication.  **Default:** `"admin"` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` - `true` ← (default) |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](grafana_user_module.md#id3)

> **Note:**
>
> - Unlike other modules from the collection, this module does not support `grafana_api_key` authentication type. The Grafana API endpoint for users management requires basic auth and admin privileges.

## [Examples](grafana_user_module.md#id4)

```yaml+jinja
---
- name: Create or update a Grafana user
  community.grafana.grafana_user:
    url: "https://grafana.example.com"
    url_username: admin
    url_password: changeme
    name: "Bruce Wayne"
    email: batman@gotham.city
    login: batman
    password: robin
    is_admin: true
    state: present

- name: Delete a Grafana user
  community.grafana.grafana_user:
    url: "https://grafana.example.com"
    url_username: admin
    url_password: changeme
    login: batman
    state: absent
```

## [Return Values](grafana_user_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **user**  complex | Information about the User  **Returned:** when state present |
| **email**  string | The User email address  **Returned:** always  **Sample:** `"['foo.bar@example.com']"` |
| **id**  integer | The User id  **Returned:** always  **Sample:** `[42]` |
| **isDisabled**  boolean | The Grafana account status  **Returned:** always  **Sample:** `[false]` |
| **isExternal**  boolean | The Grafana account information on external user provider  **Returned:** always  **Sample:** `[false]` |
| **isGrafanaAdmin**  boolean | The Grafana user permission for admin  **Returned:** always  **Sample:** `[false]` |
| **login**  string | The User login  **Returned:** always  **Sample:** `"['batman']"` |
| **orgId**  integer | The organization id that the team is part of.  **Returned:** always  **Sample:** `[1]` |
| **theme**  string | The Grafana theme  **Returned:** always  **Sample:** `"['light']"` |

### Authors

- Antoine Tanzilli (@Tailzip)
- Hong Viet LE (@pomverte)
- Julien Alexandre (@jual)
- Marc Cyprien (@LeFameux)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.grafana/issues)
- [Homepage](https://github.com/ansible-collections/grafana)
- [Repository (Sources)](https://github.com/ansible-collections/community.grafana.git)
