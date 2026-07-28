---
collection: ansible
version: "8"
title: "community.general.clc_server module – Create, Delete, Start and Stop servers in CenturyLink Cloud"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/clc_server_module.html
fetched_at: 2026-07-28T01:45:05+00:00
---
# community.general.clc_server module – Create, Delete, Start and Stop servers in CenturyLink Cloud

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
> see [Requirements](clc_server_module.md#ansible-collections-community-general-clc-server-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.clc_server`.

- [Synopsis](clc_server_module.md#synopsis)
- [Requirements](clc_server_module.md#requirements)
- [Parameters](clc_server_module.md#parameters)
- [Attributes](clc_server_module.md#attributes)
- [Notes](clc_server_module.md#notes)
- [Examples](clc_server_module.md#examples)
- [Return Values](clc_server_module.md#return-values)

## [Synopsis](clc_server_module.md#id1)

- An Ansible module to Create, Delete, Start and Stop servers in CenturyLink Cloud.

Aliases: cloud.centurylink.clc_server

## [Requirements](clc_server_module.md#id2)

The below requirements are needed on the host that executes this module.

- python = 2.7
- requests >= 2.5.0
- clc-sdk

## [Parameters](clc_server_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **add_public_ip**  boolean | Whether to add a public ip to the server  **Choices:**   - `false` ← (default) - `true` |
| **additional_disks**  list / elements=dictionary | The list of additional disks for the server  **Default:** `[]` |
| **alert_policy_id**  string | The alert policy to assign to the server. This is mutually exclusive with ‘alert_policy_name’. |
| **alert_policy_name**  string | The alert policy to assign to the server. This is mutually exclusive with ‘alert_policy_id’. |
| **alias**  string | The account alias to provision the servers under. |
| **anti_affinity_policy_id**  string | The anti-affinity policy to assign to the server. This is mutually exclusive with ‘anti_affinity_policy_name’. |
| **anti_affinity_policy_name**  string | The anti-affinity policy to assign to the server. This is mutually exclusive with ‘anti_affinity_policy_id’. |
| **configuration_id**  string | Only required for bare metal servers. Specifies the identifier for the specific configuration type of bare metal server to deploy. |
| **count**  integer | The number of servers to build (mutually exclusive with exact_count)  **Default:** `1` |
| **count_group**  string | Required when exact_count is specified. The Server Group use to determine how many servers to deploy. |
| **cpu**  integer | How many CPUs to provision on the server  **Default:** `1` |
| **cpu_autoscale_policy_id**  string | The autoscale policy to assign to the server. |
| **custom_fields**  list / elements=dictionary | The list of custom fields to set on the server.  **Default:** `[]` |
| **description**  string | The description to set for the server. |
| **exact_count**  integer | Run in idempotent mode. Will insure that this exact number of servers are running in the provided group, creating and deleting them to reach that count. Requires count_group to be set. |
| **group**  string | The Server Group to create servers under.  **Default:** `"Default Group"` |
| **ip_address**  string | The IP Address for the server. One is assigned if not provided. |
| **location**  string | The Datacenter to create servers in. |
| **managed_os**  boolean | Whether to create the server as ‘Managed’ or not.  **Choices:**   - `false` ← (default) - `true` |
| **memory**  integer | Memory in GB.  **Default:** `1` |
| **name**  string | A 1 to 6 character identifier to use for the server. This is required when state is ‘present’ |
| **network_id**  string | The network UUID on which to create servers. |
| **os_type**  string | Only required for bare metal servers. Specifies the OS to provision with the bare metal server.  **Choices:**   - `"redHat6_64Bit"` - `"centOS6_64Bit"` - `"windows2012R2Standard_64Bit"` - `"ubuntu14_64Bit"` |
| **packages**  list / elements=dictionary | The list of blue print packages to run on the server after its created.  **Default:** `[]` |
| **password**  string | Password for the administrator / root user |
| **primary_dns**  string | Primary DNS used by the server. |
| **public_ip_ports**  list / elements=dictionary | A list of ports to allow on the firewall to the servers public ip, if add_public_ip is set to True.  **Default:** `[]` |
| **public_ip_protocol**  string | The protocol to use for the public ip if add_public_ip is set to True.  **Choices:**   - `"TCP"` ← (default) - `"UDP"` - `"ICMP"` |
| **secondary_dns**  string | Secondary DNS used by the server. |
| **server_ids**  list / elements=string | Required for started, stopped, and absent states. A list of server Ids to insure are started, stopped, or absent.  **Default:** `[]` |
| **source_server_password**  string | The password for the source server if a clone is specified. |
| **state**  string | The state to insure that the provided resources are in.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"started"` - `"stopped"` |
| **storage_type**  string | The type of storage to attach to the server.  **Choices:**   - `"standard"` ← (default) - `"hyperscale"` |
| **template**  string | The template to use for server creation. Will search for a template if a partial string is provided. This is required when state is ‘present’ |
| **ttl**  string | The time to live for the server in seconds. The server will be deleted when this time expires. |
| **type**  string | The type of server to create.  **Choices:**   - `"standard"` ← (default) - `"hyperscale"` - `"bareMetal"` |
| **wait**  boolean | Whether to wait for the provisioning tasks to finish before returning.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](clc_server_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](clc_server_module.md#id5)

> **Note:**
>
> - To use this module, it is required to set the below environment variables which enables access to the Centurylink Cloud - CLC_V2_API_USERNAME, the account login id for the centurylink cloud - CLC_V2_API_PASSWORD, the account password for the centurylink cloud
> - Alternatively, the module accepts the API token and account alias. The API token can be generated using the CLC account login and password via the HTTP api call @ <https://api.ctl.io/v2/authentication/login> - CLC_V2_API_TOKEN, the API token generated from <https://api.ctl.io/v2/authentication/login> - CLC_ACCT_ALIAS, the account alias associated with the centurylink cloud
> - Users can set CLC_V2_API_URL to specify an endpoint for pointing to a different CLC environment.

## [Examples](clc_server_module.md#id6)

```yaml+jinja
# Note - You must set the CLC_V2_API_USERNAME And CLC_V2_API_PASSWD Environment variables before running these examples

- name: Provision a single Ubuntu Server
  community.general.clc_server:
    name: test
    template: ubuntu-14-64
    count: 1
    group: Default Group
    state: present

- name: Ensure 'Default Group' has exactly 5 servers
  community.general.clc_server:
    name: test
    template: ubuntu-14-64
    exact_count: 5
    count_group: Default Group
    group: Default Group

- name: Stop a Server
  community.general.clc_server:
    server_ids:
      - UC1ACCT-TEST01
    state: stopped

- name: Start a Server
  community.general.clc_server:
    server_ids:
      - UC1ACCT-TEST01
    state: started

- name: Delete a Server
  community.general.clc_server:
    server_ids:
      - UC1ACCT-TEST01
    state: absent
```

## [Return Values](clc_server_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **partially_created_server_ids**  list / elements=string | The list of server ids that are partially created  **Returned:** success  **Sample:** `["UC1TEST-SVR01", "UC1TEST-SVR02"]` |
| **server_ids**  list / elements=string | The list of server ids that are created  **Returned:** success  **Sample:** `["UC1TEST-SVR01", "UC1TEST-SVR02"]` |
| **servers**  list / elements=string | The list of server objects returned from CLC  **Returned:** success  **Sample:** `[{"changeInfo": {"createdBy": "service.wfad", "createdDate": 1438196820, "modifiedBy": "service.wfad", "modifiedDate": 1438196820}, "description": "test-server", "details": {"alertPolicies": [], "cpu": 1, "customFields": [], "diskCount": 3, "disks": [{"id": "0:0", "partitionPaths": [], "sizeGB": 1}, {"id": "0:1", "partitionPaths": [], "sizeGB": 2}, {"id": "0:2", "partitionPaths": [], "sizeGB": 14}], "hostName": "", "inMaintenanceMode": false, "ipAddresses": [{"internal": "10.1.1.1"}], "memoryGB": 1, "memoryMB": 1024, "partitions": [], "powerState": "started", "snapshots": [], "storageGB": 17}, "groupId": "086ac1dfe0b6411989e8d1b77c4065f0", "id": "test-server", "ipaddress": "10.120.45.23", "isTemplate": false, "links": [{"href": "/v2/servers/wfad/test-server", "id": "test-server", "rel": "self", "verbs": ["GET", "PATCH", "DELETE"]}, {"href": "/v2/groups/wfad/086ac1dfe0b6411989e8d1b77c4065f0", "id": "086ac1dfe0b6411989e8d1b77c4065f0", "rel": "group"}, {"href": "/v2/accounts/wfad", "id": "wfad", "rel": "account"}, {"href": "/v2/billing/wfad/serverPricing/test-server", "rel": "billing"}, {"href": "/v2/servers/wfad/test-server/publicIPAddresses", "rel": "publicIPAddresses", "verbs": ["POST"]}, {"href": "/v2/servers/wfad/test-server/credentials", "rel": "credentials"}, {"href": "/v2/servers/wfad/test-server/statistics", "rel": "statistics"}, {"href": "/v2/servers/wfad/510ec21ae82d4dc89d28479753bf736a/upcomingScheduledActivities", "rel": "upcomingScheduledActivities"}, {"href": "/v2/servers/wfad/510ec21ae82d4dc89d28479753bf736a/scheduledActivities", "rel": "scheduledActivities", "verbs": ["GET", "POST"]}, {"href": "/v2/servers/wfad/test-server/capabilities", "rel": "capabilities"}, {"href": "/v2/servers/wfad/test-server/alertPolicies", "rel": "alertPolicyMappings", "verbs": ["POST"]}, {"href": "/v2/servers/wfad/test-server/antiAffinityPolicy", "rel": "antiAffinityPolicyMapping", "verbs": ["PUT", "DELETE"]}, {"href": "/v2/servers/wfad/test-server/cpuAutoscalePolicy", "rel": "cpuAutoscalePolicyMapping", "verbs": ["PUT", "DELETE"]}], "locationId": "UC1", "name": "test-server", "os": "ubuntu14_64Bit", "osType": "Ubuntu 14 64-bit", "status": "active", "storageType": "standard", "type": "standard"}]` |

### Authors

- CLC Runner (@clc-runner)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
