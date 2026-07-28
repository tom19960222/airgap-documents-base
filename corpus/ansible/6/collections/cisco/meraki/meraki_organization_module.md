---
collection: ansible
version: "6"
title: "cisco.meraki.meraki_organization module – Manage organizations in the Meraki cloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/meraki/meraki_organization_module.html
fetched_at: 2026-07-27T17:00:42+00:00
---
# cisco.meraki.meraki_organization module – Manage organizations in the Meraki cloud

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
> To use it in a playbook, specify: `cisco.meraki.meraki_organization`.

- [Synopsis](meraki_organization_module.md#synopsis)
- [Parameters](meraki_organization_module.md#parameters)
- [Notes](meraki_organization_module.md#notes)
- [Examples](meraki_organization_module.md#examples)
- [Return Values](meraki_organization_module.md#return-values)

## [Synopsis](meraki_organization_module.md#id1)

- Allows for creation, management, and visibility into organizations within Meraki.

## [Parameters](meraki_organization_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **clone**  string | Organization to clone to a new organization. |
| **delete_confirm**  string | ID of organization required for confirmation before deletion. |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  Default: `"api.meraki.com"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  Default: `60` |
| **org_id**  aliases: id  string | ID of organization. |
| **org_name**  aliases: name, organization  string | Name of organization.  If `clone` is specified, `org_name` is the name of the new organization. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  Choices:   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  Choices:   - `"debug"` - `"normal"` ← (default) |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  Default: `165` |
| **state**  string | Create or modify an organization.  `org_id` must be specified if multiple organizations of the same name exist.  `absent` WILL DELETE YOUR ENTIRE ORGANIZATION, AND ALL ASSOCIATED OBJECTS, WITHOUT CONFIRMATION. USE WITH CAUTION.  Choices:   - `"absent"` - `"present"` ← (default) - `"query"` |
| **timeout**  integer | Time to timeout for HTTP requests.  Default: `30` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  Choices:   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](meraki_organization_module.md#id3)

> **Note:**
>
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_organization_module.md#id4)

```yaml+jinja
- name: Create a new organization named YourOrg
  meraki_organization:
    auth_key: abc12345
    org_name: YourOrg
    state: present
  delegate_to: localhost

- name: Delete an organization named YourOrg
  meraki_organization:
    auth_key: abc12345
    org_name: YourOrg
    state: absent
  delegate_to: localhost

- name: Query information about all organizations associated to the user
  meraki_organization:
    auth_key: abc12345
    state: query
  delegate_to: localhost

- name: Query information about a single organization named YourOrg
  meraki_organization:
    auth_key: abc12345
    org_name: YourOrg
    state: query
  delegate_to: localhost

- name: Rename an organization to RenamedOrg
  meraki_organization:
    auth_key: abc12345
    org_id: 987654321
    org_name: RenamedOrg
    state: present
  delegate_to: localhost

- name: Clone an organization named Org to a new one called ClonedOrg
  meraki_organization:
    auth_key: abc12345
    clone: Org
    org_name: ClonedOrg
    state: present
  delegate_to: localhost
```

## [Return Values](meraki_organization_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | Information about the organization which was created or modified  Returned: success |
| **id**  integer | Unique identification number of organization  Returned: success  Sample: `2930418` |
| **name**  string | Name of organization  Returned: success  Sample: `"YourOrg"` |

### Authors

- Kevin Breit (@kbreit)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-meraki/issues)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-meraki)
