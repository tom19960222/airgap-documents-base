---
collection: ansible
version: "6"
title: "community.general.clc_modify_server module – Modify servers in CenturyLink Cloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/clc_modify_server_module.html
fetched_at: 2026-07-27T17:08:27+00:00
---
# community.general.clc_modify_server module – Modify servers in CenturyLink Cloud

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](clc_modify_server_module.md#ansible-collections-community-general-clc-modify-server-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.clc_modify_server`.

- [Synopsis](clc_modify_server_module.md#synopsis)
- [Requirements](clc_modify_server_module.md#requirements)
- [Parameters](clc_modify_server_module.md#parameters)
- [Notes](clc_modify_server_module.md#notes)
- [Examples](clc_modify_server_module.md#examples)
- [Return Values](clc_modify_server_module.md#return-values)

## [Synopsis](clc_modify_server_module.md#id1)

- An Ansible module to modify servers in CenturyLink Cloud.

## [Requirements](clc_modify_server_module.md#id2)

The below requirements are needed on the host that executes this module.

- python = 2.7
- requests >= 2.5.0
- clc-sdk

## [Parameters](clc_modify_server_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **alert_policy_id**  string | The alert policy id to be associated to the server. This is mutually exclusive with ‘alert_policy_name’ |
| **alert_policy_name**  string | The alert policy name to be associated to the server. This is mutually exclusive with ‘alert_policy_id’ |
| **anti_affinity_policy_id**  string | The anti affinity policy id to be set for a hyper scale server. This is mutually exclusive with ‘anti_affinity_policy_name’ |
| **anti_affinity_policy_name**  string | The anti affinity policy name to be set for a hyper scale server. This is mutually exclusive with ‘anti_affinity_policy_id’ |
| **cpu**  string | How many CPUs to update on the server |
| **memory**  string | Memory (in GB) to set to the server. |
| **server_ids**  list / elements=string / required | A list of server Ids to modify. |
| **state**  string | The state to insure that the provided resources are in.  Choices:   - `"present"` ← (default) - `"absent"` |
| **wait**  boolean | Whether to wait for the provisioning tasks to finish before returning.  Choices:   - `false` - `true` ← (default) |

## [Notes](clc_modify_server_module.md#id4)

> **Note:**
>
> - To use this module, it is required to set the below environment variables which enables access to the Centurylink Cloud - CLC_V2_API_USERNAME, the account login id for the centurylink cloud - CLC_V2_API_PASSWORD, the account password for the centurylink cloud
> - Alternatively, the module accepts the API token and account alias. The API token can be generated using the CLC account login and password via the HTTP api call @ <https://api.ctl.io/v2/authentication/login> - CLC_V2_API_TOKEN, the API token generated from <https://api.ctl.io/v2/authentication/login> - CLC_ACCT_ALIAS, the account alias associated with the centurylink cloud
> - Users can set CLC_V2_API_URL to specify an endpoint for pointing to a different CLC environment.

## [Examples](clc_modify_server_module.md#id5)

```yaml+jinja
# Note - You must set the CLC_V2_API_USERNAME And CLC_V2_API_PASSWD Environment variables before running these examples

- name: Set the cpu count to 4 on a server
  community.general.clc_modify_server:
    server_ids:
        - UC1TESTSVR01
        - UC1TESTSVR02
    cpu: 4
    state: present

- name: Set the memory to 8GB on a server
  community.general.clc_modify_server:
    server_ids:
        - UC1TESTSVR01
        - UC1TESTSVR02
    memory: 8
    state: present

- name: Set the anti affinity policy on a server
  community.general.clc_modify_server:
    server_ids:
        - UC1TESTSVR01
        - UC1TESTSVR02
    anti_affinity_policy_name: 'aa_policy'
    state: present

- name: Remove the anti affinity policy on a server
  community.general.clc_modify_server:
    server_ids:
        - UC1TESTSVR01
        - UC1TESTSVR02
    anti_affinity_policy_name: 'aa_policy'
    state: absent

- name: Add the alert policy on a server
  community.general.clc_modify_server:
    server_ids:
        - UC1TESTSVR01
        - UC1TESTSVR02
    alert_policy_name: 'alert_policy'
    state: present

- name: Remove the alert policy on a server
  community.general.clc_modify_server:
    server_ids:
        - UC1TESTSVR01
        - UC1TESTSVR02
    alert_policy_name: 'alert_policy'
    state: absent

- name: Ret the memory to 16GB and cpu to 8 core on a lust if servers
  community.general.clc_modify_server:
    server_ids:
        - UC1TESTSVR01
        - UC1TESTSVR02
    cpu: 8
    memory: 16
    state: present
```

## [Return Values](clc_modify_server_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **server_ids**  list / elements=string | The list of server ids that are changed  Returned: success  Sample: `["UC1TEST-SVR01", "UC1TEST-SVR02"]` |
| **servers**  list / elements=string | The list of server objects that are changed  Returned: success  Sample: `[{"changeInfo": {"createdBy": "service.wfad", "createdDate": 1438196820, "modifiedBy": "service.wfad", "modifiedDate": 1438196820}, "description": "test-server", "details": {"alertPolicies": [], "cpu": 1, "customFields": [], "diskCount": 3, "disks": [{"id": "0:0", "partitionPaths": [], "sizeGB": 1}, {"id": "0:1", "partitionPaths": [], "sizeGB": 2}, {"id": "0:2", "partitionPaths": [], "sizeGB": 14}], "hostName": "", "inMaintenanceMode": false, "ipAddresses": [{"internal": "10.1.1.1"}], "memoryGB": 1, "memoryMB": 1024, "partitions": [], "powerState": "started", "snapshots": [], "storageGB": 17}, "groupId": "086ac1dfe0b6411989e8d1b77c4065f0", "id": "test-server", "ipaddress": "10.120.45.23", "isTemplate": false, "links": [{"href": "/v2/servers/wfad/test-server", "id": "test-server", "rel": "self", "verbs": ["GET", "PATCH", "DELETE"]}, {"href": "/v2/groups/wfad/086ac1dfe0b6411989e8d1b77c4065f0", "id": "086ac1dfe0b6411989e8d1b77c4065f0", "rel": "group"}, {"href": "/v2/accounts/wfad", "id": "wfad", "rel": "account"}, {"href": "/v2/billing/wfad/serverPricing/test-server", "rel": "billing"}, {"href": "/v2/servers/wfad/test-server/publicIPAddresses", "rel": "publicIPAddresses", "verbs": ["POST"]}, {"href": "/v2/servers/wfad/test-server/credentials", "rel": "credentials"}, {"href": "/v2/servers/wfad/test-server/statistics", "rel": "statistics"}, {"href": "/v2/servers/wfad/510ec21ae82d4dc89d28479753bf736a/upcomingScheduledActivities", "rel": "upcomingScheduledActivities"}, {"href": "/v2/servers/wfad/510ec21ae82d4dc89d28479753bf736a/scheduledActivities", "rel": "scheduledActivities", "verbs": ["GET", "POST"]}, {"href": "/v2/servers/wfad/test-server/capabilities", "rel": "capabilities"}, {"href": "/v2/servers/wfad/test-server/alertPolicies", "rel": "alertPolicyMappings", "verbs": ["POST"]}, {"href": "/v2/servers/wfad/test-server/antiAffinityPolicy", "rel": "antiAffinityPolicyMapping", "verbs": ["PUT", "DELETE"]}, {"href": "/v2/servers/wfad/test-server/cpuAutoscalePolicy", "rel": "cpuAutoscalePolicyMapping", "verbs": ["PUT", "DELETE"]}], "locationId": "UC1", "name": "test-server", "os": "ubuntu14_64Bit", "osType": "Ubuntu 14 64-bit", "status": "active", "storageType": "standard", "type": "standard"}]` |

### Authors

- CLC Runner (@clc-runner)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
