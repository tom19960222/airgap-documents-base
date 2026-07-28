---
collection: ansible
version: "8"
title: "community.grafana.grafana_folder module – Manage Grafana Folders"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/grafana/grafana_folder_module.html
fetched_at: 2026-07-28T01:53:14+00:00
---
# community.grafana.grafana_folder module – Manage Grafana Folders

> **Note:**
>
> This module is part of the [community.grafana collection](https://galaxy.ansible.com/ui/repo/published/community/grafana/) (version 1.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.grafana`.
> You need further requirements to be able to use this module,
> see [Requirements](grafana_folder_module.md#ansible-collections-community-grafana-grafana-folder-module-requirements) for details.
>
> To use it in a playbook, specify: `community.grafana.grafana_folder`.

New in community.grafana 1.0.0

- [Synopsis](grafana_folder_module.md#synopsis)
- [Requirements](grafana_folder_module.md#requirements)
- [Parameters](grafana_folder_module.md#parameters)
- [Examples](grafana_folder_module.md#examples)
- [Return Values](grafana_folder_module.md#return-values)

## [Synopsis](grafana_folder_module.md#id1)

- Create/update/delete Grafana Folders through the Folders API.

## [Requirements](grafana_folder_module.md#id2)

The below requirements are needed on the host that executes this module.

- The Folders API is only available starting Grafana 5 and the module will fail if the server version is lower than version 5.

## [Parameters](grafana_folder_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **client_cert**  path | PEM formatted certificate chain file to be used for SSL client authentication.  This file can also include the key as well, and if the key is included, *client_key* is not required |
| **client_key**  path | PEM formatted file that contains your private key to be used for SSL client authentication.  If *client_cert* contains both the certificate and key, this option is not required. |
| **grafana_api_key**  string | The Grafana API key.  If set, `url_username` and `url_password` will be ignored. |
| **name**  aliases: title  string / required | The title of the Grafana Folder. |
| **skip_version_check**  boolean  *added in community.grafana 1.2.0* | Skip Grafana version check and try to reach api endpoint anyway.  This parameter can be useful if you enabled `hide_version` in grafana.ini  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | Delete the members not found in the `members` parameters from the  list of members found on the Folder.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **url**  aliases: grafana_url  string / required | The Grafana URL. |
| **url_password**  aliases: grafana_password  string | The Grafana password for API authentication.  **Default:** `"admin"` |
| **url_username**  aliases: grafana_user  string | The Grafana user for API authentication.  **Default:** `"admin"` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` - `true` ← (default) |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Examples](grafana_folder_module.md#id4)

```yaml+jinja
---
- name: Create a folder
  community.grafana.grafana_folder:
      url: "https://grafana.example.com"
      grafana_api_key: "{{ some_api_token_value }}"
      title: "grafana_working_group"
      state: present

- name: Delete a folder
  community.grafana.grafana_folder:
      url: "https://grafana.example.com"
      grafana_api_key: "{{ some_api_token_value }}"
      title: "grafana_working_group"
      state: absent
```

## [Return Values](grafana_folder_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **folder**  complex | Information about the Folder  **Returned:** On success |
| **canAdmin**  boolean | Boolean specifying if current user can admin in folder  **Returned:** always  **Sample:** `[false]` |
| **canEdit**  boolean | Boolean specifying if current user can edit in folder  **Returned:** always  **Sample:** `[false]` |
| **canSave**  boolean | Boolean specifying if current user can save in folder  **Returned:** always  **Sample:** `[false]` |
| **created**  string | The folder creation date  **Returned:** always  **Sample:** `"['2018-01-31T17:43:12+01:00']"` |
| **createdBy**  string | The name of the user who created the folder  **Returned:** always  **Sample:** `"['admin']"` |
| **hasAcl**  boolean | Boolean specifying if folder has acl  **Returned:** always  **Sample:** `[false]` |
| **id**  integer | The Folder identifier  **Returned:** always  **Sample:** `[42]` |
| **title**  string | The Folder title  **Returned:** always  **Sample:** `"['Department ABC']"` |
| **uid**  string | The Folder uid  **Returned:** always  **Sample:** `"['nErXDvCkzz']"` |
| **updated**  string | The date the folder was last updated  **Returned:** always  **Sample:** `"['2018-01-31T17:43:12+01:00']"` |
| **updatedBy**  string | The name of the user who last updated the folder  **Returned:** always  **Sample:** `"['admin']"` |
| **url**  string | The Folder url  **Returned:** always  **Sample:** `"['/dashboards/f/nErXDvCkzz/department-abc']"` |
| **version**  integer | The folder version  **Returned:** always  **Sample:** `[1]` |

### Authors

- Rémi REY (@rrey)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.grafana/issues)
- [Homepage](https://github.com/ansible-collections/grafana)
- [Repository (Sources)](https://github.com/ansible-collections/community.grafana.git)
