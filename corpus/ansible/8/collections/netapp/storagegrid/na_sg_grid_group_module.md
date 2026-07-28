---
collection: ansible
version: "8"
title: "netapp.storagegrid.na_sg_grid_group module – NetApp StorageGRID manage groups."
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/storagegrid/na_sg_grid_group_module.html
fetched_at: 2026-07-28T02:43:50+00:00
---
# netapp.storagegrid.na_sg_grid_group module – NetApp StorageGRID manage groups.

> **Note:**
>
> This module is part of the [netapp.storagegrid collection](https://galaxy.ansible.com/ui/repo/published/netapp/storagegrid/) (version 21.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.storagegrid`.
>
> To use it in a playbook, specify: `netapp.storagegrid.na_sg_grid_group`.

New in netapp.storagegrid 20.6.0

- [Synopsis](na_sg_grid_group_module.md#synopsis)
- [Parameters](na_sg_grid_group_module.md#parameters)
- [Notes](na_sg_grid_group_module.md#notes)
- [Examples](na_sg_grid_group_module.md#examples)
- [Return Values](na_sg_grid_group_module.md#return-values)

## [Synopsis](na_sg_grid_group_module.md#id1)

- Create, Update, Delete Administration Groups within NetApp StorageGRID.

## [Parameters](na_sg_grid_group_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_url**  string / required | The url to the StorageGRID Admin Node REST API. |
| **auth_token**  string / required | The authorization token for the API request |
| **display_name**  string | Name of the group.  Required for create operation |
| **management_policy**  dictionary | Management access controls granted to the group within the tenancy. |
| **activate_features**  boolean | Users in this group will have permissions to reactivate features.  **Choices:**   - `false` - `true` |
| **alarm_acknowledgement**  boolean | Group members can have permission to acknowledge alarms.  **Choices:**   - `false` - `true` |
| **change_tenant_root_password**  boolean | Users in this group will have permissions to change tenant password.  **Choices:**   - `false` - `true` |
| **grid_topology_page_configuration**  boolean | Users in this group will have permissions to change grid topology.  **Choices:**   - `false` - `true` |
| **ilm**  boolean | Users in this group will have permissions to manage ILM rules on StorageGRID.  **Choices:**   - `false` - `true` |
| **maintenance**  boolean | Users in this group will have permissions to run maintenance tasks on StorageGRID.  **Choices:**   - `false` - `true` |
| **metrics_query**  boolean | Users in this group will have permissions to query metrics on StorageGRID.  **Choices:**   - `false` - `true` |
| **object_metadata**  boolean | Users in this group will have permissions to manage object metadata.  **Choices:**   - `false` - `true` |
| **other_grid_configuration**  boolean | Need to investigate.  **Choices:**   - `false` - `true` |
| **root_access**  boolean | Users in this group will have root access.  **Choices:**   - `false` - `true` |
| **tenant_accounts**  boolean | Users in this group will have permissions to manage tenant accounts.  **Choices:**   - `false` - `true` |
| **state**  string | Whether the specified group should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **unique_name**  string / required | Unique Name for the group. Must begin with `group/` or `federated-group/`  Required for create, modify or delete operation. |
| **validate_certs**  boolean | Should https certificates be validated?  **Choices:**   - `false` - `true` ← (default) |

## [Notes](na_sg_grid_group_module.md#id3)

> **Note:**
>
> - The modules prefixed with `na_sg` are built to manage NetApp StorageGRID.

## [Examples](na_sg_grid_group_module.md#id4)

```yaml+jinja
- name: create a StorageGRID group
  netapp.storagegrid.na_sg_grid_group:
    api_url: "https://<storagegrid-endpoint-url>"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
    state: present
    display_name: ansiblegroup100
    unique_name: group/ansiblegroup100
    management_policy:
      tenant_accounts: true
      maintenance: true
      root_access: false
```

## [Return Values](na_sg_grid_group_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resp**  dictionary | Returns information about the StorageGRID group attributes.  **Returned:** success  **Sample:** `{"accountId": "12345678901234567890", "displayName": "Example Group", "federated": false, "groupURN": "urn:sgws:identity::12345678901234567890:group/examplegroup", "id": "00000000-0000-0000-0000-000000000000", "policies": {"management": {"activateFeatures": false, "alarmAcknowledgment": true, "changeTenantRootPassword": true, "gridTopologyPageConfiguration": true, "ilm": true, "maintenance": true, "manageAlerts": true, "metricsQuery": true, "objectMetadata": true, "otherGridConfiguration": true, "rootAccess": true, "storageAdmin": true, "tenantAccounts": true}}, "uniqueName": "group/examplegroup"}` |

### Authors

- NetApp Ansible Team (@joshedmonds)

### Collection links

- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.storagegrid)
