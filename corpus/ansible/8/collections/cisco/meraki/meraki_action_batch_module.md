---
collection: ansible
version: "8"
title: "cisco.meraki.meraki_action_batch module – Manage Action Batch jobs within the Meraki Dashboard."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/meraki_action_batch_module.html
fetched_at: 2026-07-28T01:32:18+00:00
---
# cisco.meraki.meraki_action_batch module – Manage Action Batch jobs within the Meraki Dashboard.

> **Note:**
>
> This module is part of the [cisco.meraki collection](https://galaxy.ansible.com/ui/repo/published/cisco/meraki/) (version 2.17.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.meraki`.
>
> To use it in a playbook, specify: `cisco.meraki.meraki_action_batch`.

- [DEPRECATED](meraki_action_batch_module.md#deprecated)
- [Synopsis](meraki_action_batch_module.md#synopsis)
- [Parameters](meraki_action_batch_module.md#parameters)
- [Notes](meraki_action_batch_module.md#notes)
- [Examples](meraki_action_batch_module.md#examples)
- [Return Values](meraki_action_batch_module.md#return-values)
- [Status](meraki_action_batch_module.md#status)

## [DEPRECATED](meraki_action_batch_module.md#id1)

Removed in:
:   version 3.0.0

Why:
:   Updated modules released with increased functionality

Alternative:
:   cisco.meraki.organizations_action_batches

## [Synopsis](meraki_action_batch_module.md#id2)

- Allows for management of Action Batch jobs for Meraki.

## [Parameters](meraki_action_batch_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **action_batch_id**  string | ID of an existing Action Batch job. |
| **actions**  list / elements=dictionary | List of actions the job should execute. |
| **body**  any | Required body of action. |
| **operation**  string | Operation type of action  **Choices:**   - `"create"` - `"destroy"` - `"update"` - `"claim"` - `"bind"` - `"split"` - `"unbind"` - `"combine"` - `"update_order"` - `"cycle"` - `"swap"` - `"assignSeats"` - `"move"` - `"moveSeats"` - `"renewSeats"` |
| **resource**  string | Path to Action Batch resource. |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **confirmed**  boolean | Whether job is to be executed.  **Choices:**   - `false` ← (default) - `true` |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  **Default:** `"api.meraki.com"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  **Default:** `60` |
| **net_id**  string | ID of network, if applicable. |
| **net_name**  string | Name of network, if applicable. |
| **org_id**  string | ID of organization. |
| **org_name**  aliases: organization  string | Name of organization. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  **Choices:**   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  **Choices:**   - `"debug"` - `"normal"` ← (default) |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  **Default:** `165` |
| **state**  string | Specifies whether to lookup, create, or delete an Action Batch job.  **Choices:**   - `"query"` - `"present"` ← (default) - `"absent"` |
| **synchronous**  boolean | Whether job is a synchronous or asynchronous job.  **Choices:**   - `false` - `true` ← (default) |
| **timeout**  integer | Time to timeout for HTTP requests.  **Default:** `30` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  **Choices:**   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](meraki_action_batch_module.md#id4)

> **Note:**
>
> - This module is in active development and the interface may change.
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_action_batch_module.md#id5)

```yaml+jinja
- name: Query all Action Batches
  meraki_action_batch:
    auth_key: abc123
    org_name: YourOrg
    state: query
  delegate_to: localhost

- name: Query one Action Batch job
  meraki_action_batch:
    auth_key: abc123
    org_name: YourOrg
    state: query
    action_batch_id: 12345
  delegate_to: localhost

- name: Create an Action Batch job
  meraki_action_batch:
    auth_key: abc123
    org_name: YourOrg
    state: present
    actions:
    - resource: '/organizations/org_123/networks'
      operation: 'create'
      body:
        name: 'AnsibleActionBatch1'
        productTypes:
          - 'switch'
  delegate_to: localhost

- name: Update Action Batch job
  meraki_action_batch:
    auth_key: abc123
    org_name: YourOrg
    state: present
    action_batch_id: 12345
    synchronous: false

- name: Create an Action Batch job with multiple actions
  meraki_action_batch:
    auth_key: abc123
    org_name: YourOrg
    state: present
    actions:
    - resource: '/organizations/org_123/networks'
      operation: 'create'
      body:
        name: 'AnsibleActionBatch2'
        productTypes:
          - 'switch'
    - resource: '/organizations/org_123/networks'
      operation: 'create'
      body:
        name: 'AnsibleActionBatch3'
        productTypes:
          - 'switch'
  delegate_to: localhost

- name: Delete an Action Batch job
  meraki_action_batch:
    auth_key: abc123
    org_name: YourOrg
    state: absent
    action_batch_id: 12345
  delegate_to: localhost
```

## [Return Values](meraki_action_batch_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | Information about action batch jobs.  **Returned:** always |
| **actions**  dictionary | List of actions associated to job.  **Returned:** success |
| **confirmed**  boolean | Whether action batch job was confirmed for execution.  **Returned:** success |
| **id**  string | Unique ID of action batch job.  **Returned:** success  **Sample:** `"123"` |
| **organization_id**  string | Unique ID of organization which owns batch job.  **Returned:** success  **Sample:** `"2930418"` |
| **status**  complex | Information about the action batch job state.  **Returned:** success |
| **completed**  boolean | Whether job has completed.  **Returned:** success |
| **created_resources**  list / elements=string | List of resources created during execution.  **Returned:** success  **Sample:** `[{"id": 100, "uri": "/networks/L_XXXXX/groupPolicies/100"}]` |
| **errors**  list / elements=string | List of errors, if any, created during execution.  **Returned:** success |
| **failed**  boolean | Whether execution of action batch job failed.  **Returned:** success |
| **synchronous**  boolean | Whether action batch job executes synchronously or asynchronously.  **Returned:** success |

## [Status](meraki_action_batch_module.md#id7)

- This module will be removed in version 3.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](meraki_action_batch_module.md#deprecated).

### Authors

- Kevin Breit (@kbreit)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
