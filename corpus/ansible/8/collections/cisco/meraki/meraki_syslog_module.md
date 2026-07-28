---
collection: ansible
version: "8"
title: "cisco.meraki.meraki_syslog module – Manage syslog server settings in the Meraki cloud."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/meraki_syslog_module.html
fetched_at: 2026-07-28T01:32:48+00:00
---
# cisco.meraki.meraki_syslog module – Manage syslog server settings in the Meraki cloud.

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
> To use it in a playbook, specify: `cisco.meraki.meraki_syslog`.

- [DEPRECATED](meraki_syslog_module.md#deprecated)
- [Synopsis](meraki_syslog_module.md#synopsis)
- [Parameters](meraki_syslog_module.md#parameters)
- [Notes](meraki_syslog_module.md#notes)
- [Examples](meraki_syslog_module.md#examples)
- [Return Values](meraki_syslog_module.md#return-values)
- [Status](meraki_syslog_module.md#status)

## [DEPRECATED](meraki_syslog_module.md#id1)

Removed in:
:   version 3.0.0

Why:
:   Updated modules released with increased functionality

Alternative:
:   cisco.meraki.networks_syslog_servers

## [Synopsis](meraki_syslog_module.md#id2)

- Allows for creation and management of Syslog servers within Meraki.

## [Parameters](meraki_syslog_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable MERAKI_KEY is not set. |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  **Default:** `"api.meraki.com"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  **Default:** `60` |
| **net_id**  string | ID number of a network. |
| **net_name**  aliases: name, network  string | Name of a network. |
| **org_id**  string | ID of organization. |
| **org_name**  aliases: organization  string | Name of organization. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  **Choices:**   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  **Choices:**   - `"debug"` - `"normal"` ← (default) |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  **Default:** `165` |
| **servers**  list / elements=dictionary | List of syslog server settings |
| **host**  string | IP address or hostname of Syslog server. |
| **port**  integer | Port number Syslog server is listening on.  **Default:** `514` |
| **roles**  list / elements=string | List of applicable Syslog server roles.  Choices can be one of Wireless Event log, Appliance event log, Switch event log, Air Marshal events, Flows, URLs, IDS alerts, Security events |
| **state**  string | Query or edit syslog servers  To delete a syslog server, do not include server in list of servers  **Choices:**   - `"present"` ← (default) - `"query"` |
| **timeout**  integer | Time to timeout for HTTP requests.  **Default:** `30` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  **Choices:**   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](meraki_syslog_module.md#id4)

> **Note:**
>
> - Changes to existing syslog servers replaces existing configuration. If you need to add to an existing configuration set state to query to gather the existing configuration and then modify or add.
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_syslog_module.md#id5)

```yaml+jinja
- name: Query syslog configurations on network named MyNet in the YourOrg organization
  meraki_syslog:
    auth_key: abc12345
    state: query
    org_name: YourOrg
    net_name: MyNet
  delegate_to: localhost

- name: Add single syslog server with Appliance event log role
  meraki_syslog:
    auth_key: abc12345
    state: present
    org_name: YourOrg
    net_name: MyNet
    servers:
      - host: 192.0.1.2
        port: 514
        roles:
          - Appliance event log
  delegate_to: localhost

- name: Add multiple syslog servers
  meraki_syslog:
    auth_key: abc12345
    state: present
    org_name: YourOrg
    net_name: MyNet
    servers:
      - host: 192.0.1.2
        port: 514
        roles:
          - Appliance event log
      - host: 192.0.1.3
        port: 514
        roles:
          - Appliance event log
          - Flows
  delegate_to: localhost
```

## [Return Values](meraki_syslog_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | Information about the created or manipulated object.  **Returned:** info |
| **servers**  complex | List of syslog servers.  **Returned:** info |
| **host**  string | Hostname or IP address of syslog server.  **Returned:** success  **Sample:** `"192.0.1.1"` |
| **port**  string | Port number for syslog communication.  **Returned:** success  **Sample:** `"443"` |
| **roles**  list / elements=string | List of roles assigned to syslog server.  **Returned:** success  **Sample:** `["Wireless event log", " URLs"]` |

## [Status](meraki_syslog_module.md#id7)

- This module will be removed in version 3.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](meraki_syslog_module.md#deprecated).

### Authors

- Kevin Breit (@kbreit)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
