---
collection: ansible
version: "8"
title: "community.general.pritunl_org_info module – List Pritunl Organizations using the Pritunl API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/pritunl_org_info_module.html
fetched_at: 2026-07-28T01:49:10+00:00
---
# community.general.pritunl_org_info module – List Pritunl Organizations using the Pritunl API

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
> To use it in a playbook, specify: `community.general.pritunl_org_info`.

New in community.general 2.5.0

- [Synopsis](pritunl_org_info_module.md#synopsis)
- [Parameters](pritunl_org_info_module.md#parameters)
- [Attributes](pritunl_org_info_module.md#attributes)
- [Examples](pritunl_org_info_module.md#examples)
- [Return Values](pritunl_org_info_module.md#return-values)

## [Synopsis](pritunl_org_info_module.md#id1)

- A module to list Pritunl organizations using the Pritunl API.

Aliases: net_tools.pritunl.pritunl_org_info

## [Parameters](pritunl_org_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **organization**  aliases: org  string | Name of the Pritunl organization to search for. If none provided, the module will return all Pritunl organizations. |
| **pritunl_api_secret**  string / required | API Secret found in Administrators > USERNAME > API Secret. |
| **pritunl_api_token**  string / required | API Token of a Pritunl admin user.  It needs to be enabled in Administrators > USERNAME > Enable Token Authentication. |
| **pritunl_url**  string / required | URL and port of the Pritunl server on which the API is enabled. |
| **validate_certs**  boolean | If certificates should be validated or not.  This should never be set to `false`, except if you are very sure that your connection to the server can not be subject to a Man In The Middle attack.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](pritunl_org_info_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](pritunl_org_info_module.md#id4)

```yaml+jinja
- name: List all existing Pritunl organizations
  community.general.pritunl_org_info:

- name: Search for an organization named MyOrg
  community.general.pritunl_user_info:
    organization: MyOrg
```

## [Return Values](pritunl_org_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **organizations**  list / elements=dictionary | List of Pritunl organizations.  **Returned:** success  **Sample:** `[{"auth_api": false, "auth_secret": null, "auth_token": null, "id": "csftwlu6uhralzi2dpmhekz3", "name": "FooOrg", "user_count": 0}, {"auth_api": false, "auth_secret": null, "auth_token": null, "id": "58070daee63f3b2e6e472c36", "name": "MyOrg", "user_count": 3}, {"auth_api": false, "auth_secret": null, "auth_token": null, "id": "v1sncsxxybnsylc8gpqg85pg", "name": "BarOrg", "user_count": 0}]` |

### Authors

- Florian Dambrine (@Lowess)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
