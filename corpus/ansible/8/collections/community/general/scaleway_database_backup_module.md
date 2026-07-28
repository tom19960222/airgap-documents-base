---
collection: ansible
version: "8"
title: "community.general.scaleway_database_backup module – Scaleway database backups management module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/scaleway_database_backup_module.html
fetched_at: 2026-07-28T01:50:13+00:00
---
# community.general.scaleway_database_backup module – Scaleway database backups management module

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
> To use it in a playbook, specify: `community.general.scaleway_database_backup`.

New in community.general 1.2.0

- [Synopsis](scaleway_database_backup_module.md#synopsis)
- [Parameters](scaleway_database_backup_module.md#parameters)
- [Attributes](scaleway_database_backup_module.md#attributes)
- [Notes](scaleway_database_backup_module.md#notes)
- [Examples](scaleway_database_backup_module.md#examples)
- [Return Values](scaleway_database_backup_module.md#return-values)

## [Synopsis](scaleway_database_backup_module.md#id1)

- This module manages database backups on Scaleway account <https://developer.scaleway.com>.

Aliases: cloud.scaleway.scaleway_database_backup

## [Parameters](scaleway_database_backup_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  aliases: timeout  integer | HTTP timeout to Scaleway API in seconds.  **Default:** `30` |
| **api_token**  aliases: oauth_token  string / required | Scaleway OAuth token. |
| **api_url**  aliases: base_url  string | Scaleway API URL.  **Default:** `"https://api.scaleway.com"` |
| **database_name**  string | Name used to identify the database.  Required for `present` and `restored` states.  Ignored when `state=absent` or `state=exported`. |
| **expires_at**  string | Expiration datetime of the database backup (ISO 8601 format).  Ignored when `state=absent`, `state=exported` or `state=restored`. |
| **id**  string | UUID used to identify the database backup.  Required for `absent`, `exported` and `restored` states. |
| **instance_id**  string | UUID of the instance associated to the database backup.  Required for `present` and `restored` states.  Ignored when `state=absent` or `state=exported`. |
| **name**  string | Name used to identify the database backup.  Required for `present` state.  Ignored when `state=absent`, `state=exported` or `state=restored`. |
| **query_parameters**  dictionary | List of parameters passed to the query string.  **Default:** `{}` |
| **region**  string / required | Scaleway region to use (for example `fr-par`).  **Choices:**   - `"fr-par"` - `"nl-ams"` - `"pl-waw"` |
| **state**  string | Indicate desired state of the database backup.  `present` creates a backup.  `absent` deletes the backup.  `exported` creates a download link for the backup.  `restored` restores the backup to a new database.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"exported"` - `"restored"` |
| **validate_certs**  boolean | Validate SSL certs of the Scaleway API.  **Choices:**   - `false` - `true` ← (default) |
| **wait**  boolean | Wait for the instance to reach its desired state before returning.  **Choices:**   - `false` ← (default) - `true` |
| **wait_sleep_time**  integer | Time to wait before every attempt to check the state of the backup.  **Default:** `3` |
| **wait_timeout**  integer | Time to wait for the backup to reach the expected state.  **Default:** `300` |

## [Attributes](scaleway_database_backup_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](scaleway_database_backup_module.md#id4)

> **Note:**
>
> - Also see the API documentation on <https://developer.scaleway.com/>
> - If `api_token` is not set within the module, the following environment variables can be used in decreasing order of precedence [`SCW_TOKEN`](../../environment_variables.md#envvar-SCW_TOKEN), [`SCW_API_KEY`](../../environment_variables.md#envvar-SCW_API_KEY), [`SCW_OAUTH_TOKEN`](../../environment_variables.md#envvar-SCW_OAUTH_TOKEN) or `SCW_API_TOKEN`.
> - If one wants to use a different `api_url` one can also set the `SCW_API_URL` environment variable.

## [Examples](scaleway_database_backup_module.md#id5)

```yaml+jinja
- name: Create a backup
  community.general.scaleway_database_backup:
      name: 'my_backup'
      state: present
      region: 'fr-par'
      database_name: 'my-database'
      instance_id: '50968a80-2909-4e5c-b1af-a2e19860dddb'

- name: Export a backup
  community.general.scaleway_database_backup:
      id: '6ef1125a-037e-494f-a911-6d9c49a51691'
      state: exported
      region: 'fr-par'

- name: Restore a backup
  community.general.scaleway_database_backup:
      id: '6ef1125a-037e-494f-a911-6d9c49a51691'
      state: restored
      region: 'fr-par'
      database_name: 'my-new-database'
      instance_id: '50968a80-2909-4e5c-b1af-a2e19860dddb'

- name: Remove a backup
  community.general.scaleway_database_backup:
      id: '6ef1125a-037e-494f-a911-6d9c49a51691'
      state: absent
      region: 'fr-par'
```

## [Return Values](scaleway_database_backup_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **metadata**  dictionary | Backup metadata.  **Returned:** when `state=present`, `state=exported`, or `state=restored`  **Sample:** `{"metadata": {"created_at": "2020-08-06T12:42:05.631049Z", "database_name": "my-database", "download_url": null, "download_url_expires_at": null, "expires_at": null, "id": "a15297bd-0c4a-4b4f-8fbb-b36a35b7eb07", "instance_id": "617be32e-6497-4ed7-b4c7-0ee5a81edf49", "instance_name": "my-instance", "name": "backup_name", "region": "fr-par", "size": 600000, "status": "ready", "updated_at": "2020-08-06T12:42:10.581649Z"}}` |

### Authors

- Guillaume Rodriguez (@guillaume_ro_fr)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
