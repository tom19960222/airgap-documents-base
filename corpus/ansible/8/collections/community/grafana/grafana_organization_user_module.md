---
collection: ansible
version: "8"
title: "community.grafana.grafana_organization_user module – Manage Grafana Organization Users."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/grafana/grafana_organization_user_module.html
fetched_at: 2026-07-28T01:53:16+00:00
---
# community.grafana.grafana_organization_user module – Manage Grafana Organization Users.

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
> To use it in a playbook, specify: `community.grafana.grafana_organization_user`.

New in community.grafana 1.6.0

- [Synopsis](grafana_organization_user_module.md#synopsis)
- [Parameters](grafana_organization_user_module.md#parameters)
- [Examples](grafana_organization_user_module.md#examples)
- [Return Values](grafana_organization_user_module.md#return-values)

## [Synopsis](grafana_organization_user_module.md#id1)

- Add or remove users or change their roles in Grafana organizations through org API.
- The user has to exist before using this module. See <https://docs.ansible.com/ansible/latest/collections/community/grafana/grafana_user_module.html>.

## [Parameters](grafana_organization_user_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **client_cert**  path | PEM formatted certificate chain file to be used for SSL client authentication.  This file can also include the key as well, and if the key is included, *client_key* is not required |
| **client_key**  path | PEM formatted file that contains your private key to be used for SSL client authentication.  If *client_cert* contains both the certificate and key, this option is not required. |
| **login**  string / required | Username or email. |
| **org_id**  integer | Organization ID.  **Default:** `1` |
| **role**  string | User’s role in the organization.  **Choices:**   - `"viewer"` ← (default) - `"editor"` - `"admin"` |
| **state**  string | Status of a user’s organization membership.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **url**  aliases: grafana_url  string / required | The Grafana URL. |
| **url_password**  aliases: grafana_password  string | The Grafana password for API authentication.  **Default:** `"admin"` |
| **url_username**  aliases: grafana_user  string | The Grafana user for API authentication.  **Default:** `"admin"` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` - `true` ← (default) |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Examples](grafana_organization_user_module.md#id3)

```yaml+jinja
---
- name: Add user to organization
  community.grafana.grafana_organization_user:
    url: "{{ grafana_url }}"
    url_username: "{{ grafana_username }}"
    url_password: "{{ grafana_password }}"
    login: john
    role: admin

- name: Remove user from organization
  community.grafana.grafana_organization_user:
    url: "{{ grafana_url }}"
    url_username: "{{ grafana_username }}"
    url_password: "{{ grafana_password }}"
    login: john
    state: absent
```

## [Return Values](grafana_organization_user_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **user**  complex | Information about the organization user  **Returned:** when state present |
| **email**  string | The User email address  **Returned:** always  **Sample:** `"['foo.bar@example.com']"` |
| **login**  string | The User login  **Returned:** always  **Sample:** `"['batman']"` |
| **name**  string | The User name (same as login)  **Returned:** always  **Sample:** `"['batman']"` |
| **orgId**  integer | The organization id that the team is part of.  **Returned:** always  **Sample:** `[1]` |
| **role**  string | The user role in the organization  **Returned:** always  **Can only return:**   - `"Viewer"` - `"Editor"` - `"Admin"`   **Sample:** `"['Viewer']"` |

### Authors

- Aliaksandr Mianzhynski (@amenzhinsky)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.grafana/issues)
- [Homepage](https://github.com/ansible-collections/grafana)
- [Repository (Sources)](https://github.com/ansible-collections/community.grafana.git)
