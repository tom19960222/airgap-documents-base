---
collection: ansible
version: "8"
title: "community.general.clc_group module – Create/delete Server Groups at Centurylink Cloud"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/clc_group_module.html
fetched_at: 2026-07-28T01:45:02+00:00
---
# community.general.clc_group module – Create/delete Server Groups at Centurylink Cloud

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](clc_group_module.md#ansible-collections-community-general-clc-group-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.clc_group`.

- [Synopsis](clc_group_module.md#synopsis)
- [Requirements](clc_group_module.md#requirements)
- [Parameters](clc_group_module.md#parameters)
- [Attributes](clc_group_module.md#attributes)
- [Notes](clc_group_module.md#notes)
- [Examples](clc_group_module.md#examples)
- [Return Values](clc_group_module.md#return-values)

## [Synopsis](clc_group_module.md#id1)

- Create or delete Server Groups at Centurylink Centurylink Cloud

Aliases: cloud.centurylink.clc_group

## [Requirements](clc_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- python = 2.7
- requests >= 2.5.0
- clc-sdk

## [Parameters](clc_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  string | A description of the Server Group |
| **location**  string | Datacenter to create the group in. If location is not provided, the group gets created in the default datacenter associated with the account |
| **name**  string / required | The name of the Server Group |
| **parent**  string | The parent group of the server group. If parent is not provided, it creates the group at top level. |
| **state**  string | Whether to create or delete the group  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **wait**  boolean | Whether to wait for the tasks to finish before returning.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](clc_group_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](clc_group_module.md#id5)

> **Note:**
>
> - To use this module, it is required to set the below environment variables which enables access to the Centurylink Cloud - CLC_V2_API_USERNAME, the account login id for the centurylink cloud - CLC_V2_API_PASSWORD, the account password for the centurylink cloud
> - Alternatively, the module accepts the API token and account alias. The API token can be generated using the CLC account login and password via the HTTP api call @ <https://api.ctl.io/v2/authentication/login> - CLC_V2_API_TOKEN, the API token generated from <https://api.ctl.io/v2/authentication/login> - CLC_ACCT_ALIAS, the account alias associated with the centurylink cloud
> - Users can set CLC_V2_API_URL to specify an endpoint for pointing to a different CLC environment.

## [Examples](clc_group_module.md#id6)

```yaml+jinja
# Create a Server Group

---
- name: Create Server Group
  hosts: localhost
  gather_facts: false
  connection: local
  tasks:
    - name: Create / Verify a Server Group at CenturyLink Cloud
      community.general.clc_group:
        name: My Cool Server Group
        parent: Default Group
        state: present
      register: clc

    - name: Debug
      ansible.builtin.debug:
        var: clc

# Delete a Server Group
- name: Delete Server Group
  hosts: localhost
  gather_facts: false
  connection: local
  tasks:
    - name: Delete / Verify Absent a Server Group at CenturyLink Cloud
      community.general.clc_group:
        name: My Cool Server Group
        parent: Default Group
        state: absent
      register: clc

    - name: Debug
      ansible.builtin.debug:
        var: clc
```

## [Return Values](clc_group_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **group**  dictionary | The group information  **Returned:** success  **Sample:** `{"changeInfo": {"createdBy": "service.wfad", "createdDate": "2015-07-29T18:52:47Z", "modifiedBy": "service.wfad", "modifiedDate": "2015-07-29T18:52:47Z"}, "customFields": [], "description": "test group", "groups": [], "id": "bb5f12a3c6044ae4ad0a03e73ae12cd1", "links": [{"href": "/v2/groups/wfad", "rel": "createGroup", "verbs": ["POST"]}, {"href": "/v2/servers/wfad", "rel": "createServer", "verbs": ["POST"]}, {"href": "/v2/groups/wfad/bb5f12a3c6044ae4ad0a03e73ae12cd1", "rel": "self", "verbs": ["GET", "PATCH", "DELETE"]}, {"href": "/v2/groups/wfad/086ac1dfe0b6411989e8d1b77c4065f0", "id": "086ac1dfe0b6411989e8d1b77c4065f0", "rel": "parentGroup"}, {"href": "/v2/groups/wfad/bb5f12a3c6044ae4ad0a03e73ae12cd1/defaults", "rel": "defaults", "verbs": ["GET", "POST"]}, {"href": "/v2/groups/wfad/bb5f12a3c6044ae4ad0a03e73ae12cd1/billing", "rel": "billing"}, {"href": "/v2/groups/wfad/bb5f12a3c6044ae4ad0a03e73ae12cd1/archive", "rel": "archiveGroupAction"}, {"href": "/v2/groups/wfad/bb5f12a3c6044ae4ad0a03e73ae12cd1/statistics", "rel": "statistics"}, {"href": "/v2/groups/wfad/bb5f12a3c6044ae4ad0a03e73ae12cd1/upcomingScheduledActivities", "rel": "upcomingScheduledActivities"}, {"href": "/v2/groups/wfad/bb5f12a3c6044ae4ad0a03e73ae12cd1/horizontalAutoscalePolicy", "rel": "horizontalAutoscalePolicyMapping", "verbs": ["GET", "PUT", "DELETE"]}, {"href": "/v2/groups/wfad/bb5f12a3c6044ae4ad0a03e73ae12cd1/scheduledActivities", "rel": "scheduledActivities", "verbs": ["GET", "POST"]}], "locationId": "UC1", "name": "test group", "status": "active", "type": "default"}` |

### Authors

- CLC Runner (@clc-runner)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
