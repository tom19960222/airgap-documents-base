---
collection: ansible
version: "8"
title: "grafana.grafana.folder module – Manage Folders in Grafana"
source_url: https://docs.ansible.com/projects/ansible/8/collections/grafana/grafana/folder_module.html
fetched_at: 2026-07-28T01:05:45+00:00
---
# grafana.grafana.folder module – Manage Folders in Grafana

> **Note:**
>
> This module is part of the [grafana.grafana collection](https://galaxy.ansible.com/ui/repo/published/grafana/grafana/) (version 2.2.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install grafana.grafana`.
> You need further requirements to be able to use this module,
> see [Requirements](folder_module.md#ansible-collections-grafana-grafana-folder-module-requirements) for details.
>
> To use it in a playbook, specify: `grafana.grafana.folder`.

New in grafana.grafana 0.0.1

- [Synopsis](folder_module.md#synopsis)
- [Requirements](folder_module.md#requirements)
- [Parameters](folder_module.md#parameters)
- [Notes](folder_module.md#notes)
- [Examples](folder_module.md#examples)
- [Return Values](folder_module.md#return-values)

## [Synopsis](folder_module.md#id1)

- Create, Update and delete Folders via Ansible.

## [Requirements](folder_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests >= 1.0.0

## [Parameters](folder_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **grafana_api_key**  string / required | Grafana API Key to authenticate with Grafana. |
| **grafana_url**  string / required | URL of the Grafana instance. |
| **overwrite**  boolean | Set to `false` if you dont want to overwrite existing folder with newer version.  **Choices:**   - `false` - `true` ← (default) |
| **state**  string | State for the Grafana Folder.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **title**  string / required | Sets the title of the folder. |
| **uid**  string / required | Sets the UID for your folder. |

## [Notes](folder_module.md#id4)

> **Note:**
>
> - Does not support `check_mode`.

## [Examples](folder_module.md#id5)

```yaml+jinja
- name: Create/Update a Folder in Grafana
  grafana.grafana.folder:
    title: folder_name
    uid: folder_name
    overwrite: true
    grafana_url: "{{ grafana_url }}"
    grafana_api_key: "{{ grafana_api_key }}"
    state: present

- name: Delete a Folder in Grafana
  grafana.grafana.folder:
    uid: folder_name
    grafana_url: "{{ grafana_url }}"
    grafana_api_key: "{{ grafana_api_key }}"
    state: absent
```

## [Return Values](folder_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **output**  dictionary | Dict object containing folder information.  **Returned:** On success |
| **canAdmin**  boolean | Boolean value specifying if current user can admin in folder.  **Returned:** state is present and on success  **Sample:** `true` |
| **canDelete**  boolean | Boolean value specifying if current user can delete the folder.  **Returned:** state is present and on success  **Sample:** `true` |
| **canEdit**  boolean | Boolean value specifying if current user can edit in folder.  **Returned:** state is present and on success  **Sample:** `true` |
| **canSave**  boolean | Boolean value specifying if current user can save in folder.  **Returned:** state is present and on success  **Sample:** `true` |
| **created**  string | The date when folder was created.  **Returned:** state is present and on success  **Sample:** `"2022-10-20T09:31:53Z"` |
| **createdBy**  string | The name of the user who created the folder.  **Returned:** state is present and on success  **Sample:** `"Anonymous"` |
| **hasAcl**  boolean | Boolean value specifying if folder has acl.  **Returned:** state is present and on success  **Sample:** `true` |
| **id**  integer | The ID for the folder.  **Returned:** state is present and on success  **Sample:** `18` |
| **message**  string | The message returned after the operation on the folder.  **Returned:** state is absent and on success  **Sample:** `"Folder has been succesfuly deleted"` |
| **title**  string | The name of the folder.  **Returned:** on success  **Sample:** `"foldername"` |
| **uid**  string | The UID for the folder.  **Returned:** state is present and on success  **Sample:** `"foldername"` |
| **updated**  string | The date when the folder was last updated.  **Returned:** state is present and on success  **Sample:** `"2022-10-20T09:31:53Z"` |
| **updatedBy**  string | The name of the user who last updated the folder.  **Returned:** state is present and on success  **Sample:** `"Anonymous"` |
| **url**  string | The URl for the folder.  **Returned:** state is present and on success  **Sample:** `"/dashboards/f/foldername/foldername"` |
| **version**  integer | The version of the folder.  **Returned:** state is present and on success  **Sample:** `1` |

### Authors

- Ishan Jain (@ishanjainn)

### Collection links

- [Issue Tracker](https://github.com/grafana/grafana-ansible-collection/issues)
- [Repository (Sources)](https://github.com/grafana/grafana-ansible-collection)
