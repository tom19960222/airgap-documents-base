---
collection: ansible
version: "8"
title: "cisco.meraki.meraki_config_template module – Manage configuration templates in the Meraki cloud"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/meraki_config_template_module.html
fetched_at: 2026-07-28T01:32:20+00:00
---
# cisco.meraki.meraki_config_template module – Manage configuration templates in the Meraki cloud

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
> To use it in a playbook, specify: `cisco.meraki.meraki_config_template`.

New in cisco.meraki 1.0.0

- [DEPRECATED](meraki_config_template_module.md#deprecated)
- [Synopsis](meraki_config_template_module.md#synopsis)
- [Parameters](meraki_config_template_module.md#parameters)
- [Notes](meraki_config_template_module.md#notes)
- [Examples](meraki_config_template_module.md#examples)
- [Return Values](meraki_config_template_module.md#return-values)
- [Status](meraki_config_template_module.md#status)

## [DEPRECATED](meraki_config_template_module.md#id1)

Removed in:
:   version 3.0.0

Why:
:   Updated modules released with increased functionality

Alternative:
:   cisco.meraki.organizations_config_templates

## [Synopsis](meraki_config_template_module.md#id2)

- Allows for querying, deleting, binding, and unbinding of configuration templates.

## [Parameters](meraki_config_template_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **auto_bind**  boolean | Optional boolean indicating whether the network’s switches should automatically bind to profiles of the same model.  This option only affects switch networks and switch templates.  Auto-bind is not valid unless the switch template has at least one profile and has at most one profile per switch model.  **Choices:**   - `false` - `true` |
| **config_template**  aliases: name  string | Name of the configuration template within an organization to manipulate. |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  **Default:** `"api.meraki.com"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  **Default:** `60` |
| **net_id**  string | ID of the network to bind or unbind configuration template to. |
| **net_name**  string | Name of the network to bind or unbind configuration template to. |
| **org_id**  string | ID of organization associated to a configuration template. |
| **org_name**  aliases: organization  string | Name of organization containing the configuration template. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  **Choices:**   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  **Choices:**   - `"debug"` - `"normal"` ← (default) |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  **Default:** `165` |
| **state**  string | Specifies whether configuration template information should be queried, modified, or deleted.  **Choices:**   - `"absent"` - `"query"` ← (default) - `"present"` |
| **timeout**  integer | Time to timeout for HTTP requests.  **Default:** `30` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  **Choices:**   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](meraki_config_template_module.md#id4)

> **Note:**
>
> - Module is not idempotent as the Meraki API is limited in what information it provides about configuration templates.
> - Meraki’s API does not support creating new configuration templates.
> - To use the configuration template, simply pass its ID via `net_id` parameters in Meraki modules.
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_config_template_module.md#id5)

```yaml+jinja
- name: Query configuration templates
  meraki_config_template:
    auth_key: abc12345
    org_name: YourOrg
    state: query
  delegate_to: localhost

- name: Bind a template from a network
  meraki_config_template:
    auth_key: abc123
    state: present
    org_name: YourOrg
    net_name: YourNet
    config_template: DevConfigTemplate
  delegate_to: localhost

- name: Unbind a template from a network
  meraki_config_template:
    auth_key: abc123
    state: absent
    org_name: YourOrg
    net_name: YourNet
    config_template: DevConfigTemplate
  delegate_to: localhost

- name: Delete a configuration template
  meraki_config_template:
    auth_key: abc123
    state: absent
    org_name: YourOrg
    config_template: DevConfigTemplate
  delegate_to: localhost
```

## [Return Values](meraki_config_template_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | Information about queried object.  **Returned:** success |
| **id**  integer | Unique identification number of organization.  **Returned:** success  **Sample:** `"L_2930418"` |
| **name**  string | Name of configuration template.  **Returned:** success  **Sample:** `"YourTemplate"` |
| **product_types**  list / elements=string | List of products which can exist in the network.  **Returned:** success  **Sample:** `["appliance", "switch"]` |
| **time_zone**  string | Timezone applied to each associated network.  **Returned:** success  **Sample:** `"America/Chicago"` |

## [Status](meraki_config_template_module.md#id7)

- This module will be removed in version 3.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](meraki_config_template_module.md#deprecated).

### Authors

- Kevin Breit (@kbreit)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
