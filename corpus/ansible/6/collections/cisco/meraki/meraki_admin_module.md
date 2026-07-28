---
collection: ansible
version: "6"
title: "cisco.meraki.meraki_admin module – Manage administrators in the Meraki cloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/meraki/meraki_admin_module.html
fetched_at: 2026-07-27T17:00:17+00:00
---
# cisco.meraki.meraki_admin module – Manage administrators in the Meraki cloud

> **Note:**
>
> This module is part of the [cisco.meraki collection](https://galaxy.ansible.com/cisco/meraki) (version 2.13.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.meraki`.
>
> To use it in a playbook, specify: `cisco.meraki.meraki_admin`.

New in cisco.meraki 1.0.0

- [Synopsis](meraki_admin_module.md#synopsis)
- [Parameters](meraki_admin_module.md#parameters)
- [Notes](meraki_admin_module.md#notes)
- [Examples](meraki_admin_module.md#examples)
- [Return Values](meraki_admin_module.md#return-values)

## [Synopsis](meraki_admin_module.md#id1)

- Allows for creation, management, and visibility into administrators within Meraki.

## [Parameters](meraki_admin_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **email**  string | Email address for the dashboard administrator.  Email cannot be updated.  Required when creating or editing an administrator. |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  Default: `"api.meraki.com"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  Default: `60` |
| **name**  string | Name of the dashboard administrator.  Required when creating a new administrator. |
| **networks**  list / elements=dictionary | List of networks the administrator has privileges on.  When creating a new administrator, `org_name`, `network`, or `tags` must be specified. |
| **access**  string | The privilege of the dashboard administrator on the network.  Valid options are `full`, `read-only`, or `none`. |
| **id**  string | Network ID for which administrator should have privileges assigned. |
| **network**  string | Network name for which administrator should have privileges assigned. |
| **org_access**  aliases: orgAccess  string | Privileges assigned to the administrator in the organization.  Choices:   - `"full"` - `"none"` - `"read-only"` |
| **org_id**  string | ID of organization. |
| **org_name**  aliases: organization  string | Name of organization.  Used when `name` should refer to another object.  When creating a new administrator, `org_name`, `network`, or `tags` must be specified. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  Choices:   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  Choices:   - `"debug"` - `"normal"` ← (default) |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  Default: `165` |
| **state**  string / required | Create or modify, or delete an organization  If `state` is `absent`, name takes priority over email if both are specified.  Choices:   - `"absent"` - `"present"` - `"query"` |
| **tags**  list / elements=dictionary | Tags the administrator has privileges on.  When creating a new administrator, `org_name`, `network`, or `tags` must be specified.  If `none` is specified, `network` or `tags` must be specified. |
| **access**  string | The privilege of the dashboard administrator for the tag. |
| **tag**  string | Object tag which privileges should be assigned. |
| **timeout**  integer | Time to timeout for HTTP requests.  Default: `30` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  Choices:   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](meraki_admin_module.md#id3)

> **Note:**
>
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_admin_module.md#id4)

```yaml+jinja
- name: Query information about all administrators associated to the organization
  meraki_admin:
    auth_key: abc12345
    org_name: YourOrg
    state: query
  delegate_to: localhost

- name: Query information about a single administrator by name
  meraki_admin:
    auth_key: abc12345
    org_id: 12345
    state: query
    name: Jane Doe

- name: Query information about a single administrator by email
  meraki_admin:
    auth_key: abc12345
    org_name: YourOrg
    state: query
    email: jane@doe.com

- name: Create new administrator with organization access
  meraki_admin:
    auth_key: abc12345
    org_name: YourOrg
    state: present
    name: Jane Doe
    org_access: read-only
    email: jane@doe.com

- name: Create new administrator with organization access
  meraki_admin:
    auth_key: abc12345
    org_name: YourOrg
    state: present
    name: Jane Doe
    org_access: read-only
    email: jane@doe.com

- name: Create a new administrator with organization access
  meraki_admin:
    auth_key: abc12345
    org_name: YourOrg
    state: present
    name: Jane Doe
    org_access: read-only
    email: jane@doe.com

- name: Revoke access to an organization for an administrator
  meraki_admin:
    auth_key: abc12345
    org_name: YourOrg
    state: absent
    email: jane@doe.com

- name: Create a new administrator with full access to two tags
  meraki_admin:
    auth_key: abc12345
    org_name: YourOrg
    state: present
    name: Jane Doe
    orgAccess: read-only
    email: jane@doe.com
    tags:
        - tag: tenant
          access: full
        - tag: corporate
          access: read-only

- name: Create a new administrator with full access to a network
  meraki_admin:
    auth_key: abc12345
    org_name: YourOrg
    state: present
    name: Jane Doe
    orgAccess: read-only
    email: jane@doe.com
    networks:
        - id: N_12345
          access: full
```

## [Return Values](meraki_admin_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | List of administrators.  Returned: success |
| **account_status**  string | Status of account.  Returned: success  Sample: `"ok"` |
| **email**  string | Email address of administrator.  Returned: success  Sample: `"your@email.com"` |
| **has_api_key**  boolean | Defines whether administrator has an API assigned to their account.  Returned: success  Sample: `false` |
| **id**  string | Unique identification number of administrator.  Returned: success  Sample: `"1234567890"` |
| **last_active**  string | Date and time of time the administrator was active within Dashboard.  Returned: success  Sample: `"2019-01-28 14:58:56 -0800"` |
| **name**  string | Given name of administrator.  Returned: success  Sample: `"John Doe"` |
| **networks**  complex | List of networks administrator has access on.  Returned: success |
| **access**  string | Access level of administrator. Options are ‘full’, ‘read-only’, or ‘none’.  Returned: when network permissions are set  Sample: `"read-only"` |
| **id**  string | The network ID.  Returned: when network permissions are set  Sample: `"N_0123456789"` |
| **org_access**  string | The privilege of the dashboard administrator on the organization. Options are ‘full’, ‘read-only’, or ‘none’.  Returned: success  Sample: `"full"` |
| **tags**  complex | Tags the administrator has access on.  Returned: success |
| **access**  string | Access level of administrator. Options are ‘full’, ‘read-only’, or ‘none’.  Returned: when tag permissions are set  Sample: `"full"` |
| **tag**  string | Tag name.  Returned: when tag permissions are set  Sample: `"production"` |
| **two_factor_auth_enabled**  boolean | Enabled state of two-factor authentication for administrator.  Returned: success  Sample: `false` |

### Authors

- Kevin Breit (@kbreit)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-meraki/issues)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-meraki)
