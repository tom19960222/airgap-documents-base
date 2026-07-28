---
collection: ansible
version: "6"
title: "community.general.pritunl_user_info module – List Pritunl Users using the Pritunl API"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/pritunl_user_info_module.html
fetched_at: 2026-07-27T17:12:02+00:00
---
# community.general.pritunl_user_info module – List Pritunl Users using the Pritunl API

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.pritunl_user_info`.

New in community.general 2.3.0

- [Synopsis](pritunl_user_info_module.md#synopsis)
- [Parameters](pritunl_user_info_module.md#parameters)
- [Examples](pritunl_user_info_module.md#examples)
- [Return Values](pritunl_user_info_module.md#return-values)

## [Synopsis](pritunl_user_info_module.md#id1)

- A module to list Pritunl users using the Pritunl API.

## [Parameters](pritunl_user_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **organization**  aliases: org  string / required | The name of the organization the user is part of. |
| **pritunl_api_secret**  string / required | API Secret found in Administrators > USERNAME > API Secret. |
| **pritunl_api_token**  string / required | API Token of a Pritunl admin user.  It needs to be enabled in Administrators > USERNAME > Enable Token Authentication. |
| **pritunl_url**  string / required | URL and port of the Pritunl server on which the API is enabled. |
| **user_name**  string | Name of the user to filter on Pritunl. |
| **user_type**  string | Type of the user *user_name*.  Choices:   - `"client"` ← (default) - `"server"` |
| **validate_certs**  boolean | If certificates should be validated or not.  This should never be set to `false`, except if you are very sure that your connection to the server can not be subject to a Man In The Middle attack.  Choices:   - `false` - `true` ← (default) |

## [Examples](pritunl_user_info_module.md#id3)

```yaml+jinja
- name: List all existing users part of the organization MyOrg
  community.general.pritunl_user_info:
    state: list
    organization: MyOrg

- name: Search for the user named Florian part of the organization MyOrg
  community.general.pritunl_user_info:
    state: list
    organization: MyOrg
    user_name: Florian
```

## [Return Values](pritunl_user_info_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **users**  list / elements=dictionary | List of Pritunl users.  Returned: success  Sample: `[{"audit": false, "auth_type": "google", "bypass_secondary": false, "client_to_client": false, "disabled": false, "dns_mapping": null, "dns_servers": null, "dns_suffix": null, "email": "foo@bar.com", "gravatar": true, "groups": ["foo", "bar"], "id": "5d070dafe63q3b2e6s472c3b", "name": "foo@acme.com", "network_links": [], "organization": "58070daee6sf342e6e4s2c36", "organization_name": "Acme", "otp_auth": true, "otp_secret": "35H5EJA3XB2$4CWG", "pin": false, "port_forwarding": [], "servers": []}]` |

### Authors

- Florian Dambrine (@Lowess)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
