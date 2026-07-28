---
collection: ansible
version: "8"
title: "community.general.pritunl_user module – Manage Pritunl Users using the Pritunl API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/pritunl_user_module.html
fetched_at: 2026-07-28T01:49:11+00:00
---
# community.general.pritunl_user module – Manage Pritunl Users using the Pritunl API

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.pritunl_user`.

New in community.general 2.3.0

- [Synopsis](pritunl_user_module.md#synopsis)
- [Parameters](pritunl_user_module.md#parameters)
- [Attributes](pritunl_user_module.md#attributes)
- [Examples](pritunl_user_module.md#examples)
- [Return Values](pritunl_user_module.md#return-values)

## [Synopsis](pritunl_user_module.md#id1)

- A module to manage Pritunl users using the Pritunl API.

Aliases: net_tools.pritunl.pritunl_user

## [Parameters](pritunl_user_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **organization**  aliases: org  string / required | The name of the organization the user is part of. |
| **pritunl_api_secret**  string / required | API Secret found in Administrators > USERNAME > API Secret. |
| **pritunl_api_token**  string / required | API Token of a Pritunl admin user.  It needs to be enabled in Administrators > USERNAME > Enable Token Authentication. |
| **pritunl_url**  string / required | URL and port of the Pritunl server on which the API is enabled. |
| **state**  string | If `present`, the module adds user `user_name` to the Pritunl `organization`. If `absent`, removes the user `user_name` from the Pritunl `organization`.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **user_disabled**  boolean | Enable/Disable the user `user_name`.  **Choices:**   - `false` - `true` |
| **user_email**  string | Email address associated with the user `user_name`. |
| **user_gravatar**  boolean | Enable/Disable Gravatar usage for the user `user_name`.  **Choices:**   - `false` - `true` |
| **user_groups**  list / elements=string | List of groups associated with the user `user_name`. |
| **user_mac_addresses**  list / elements=string  *added in community.general 5.0.0* | Allowed MAC addresses for the user `user_name`. |
| **user_name**  string / required | Name of the user to create or delete from Pritunl. |
| **user_type**  string | Type of the user `user_name`.  **Choices:**   - `"client"` ← (default) - `"server"` |
| **validate_certs**  boolean | If certificates should be validated or not.  This should never be set to `false`, except if you are very sure that your connection to the server can not be subject to a Man In The Middle attack.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](pritunl_user_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](pritunl_user_module.md#id4)

```yaml+jinja
- name: Create the user Foo with email address foo@bar.com in MyOrg
  community.general.pritunl_user:
    state: present
    organization: MyOrg
    user_name: Foo
    user_email: foo@bar.com
    user_mac_addresses:
      - "00:00:00:00:00:99"

- name: Disable the user Foo but keep it in Pritunl
  community.general.pritunl_user:
    state: present
    organization: MyOrg
    user_name: Foo
    user_email: foo@bar.com
    user_disabled: true

- name: Make sure the user Foo is not part of MyOrg anymore
  community.general.pritunl_user:
    state: absent
    organization: MyOrg
    user_name: Foo
```

## [Return Values](pritunl_user_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **response**  dictionary | JSON representation of Pritunl Users.  **Returned:** success  **Sample:** `{"audit": false, "auth_type": "google", "bypass_secondary": false, "client_to_client": false, "disabled": false, "dns_mapping": null, "dns_servers": null, "dns_suffix": null, "email": "foo@bar.com", "gravatar": true, "groups": ["foo", "bar"], "id": "5d070dafe63q3b2e6s472c3b", "name": "foo@acme.com", "network_links": [], "organization": "58070daee6sf342e6e4s2c36", "organization_name": "Acme", "otp_auth": true, "otp_secret": "35H5EJA3XB2$4CWG", "pin": false, "port_forwarding": [], "servers": []}` |

### Authors

- Florian Dambrine (@Lowess)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
