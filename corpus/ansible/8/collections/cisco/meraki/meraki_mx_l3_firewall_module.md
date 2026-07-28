---
collection: ansible
version: "8"
title: "cisco.meraki.meraki_mx_l3_firewall module – Manage MX appliance layer 3 firewalls in the Meraki cloud"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/meraki_mx_l3_firewall_module.html
fetched_at: 2026-07-28T01:32:37+00:00
---
# cisco.meraki.meraki_mx_l3_firewall module – Manage MX appliance layer 3 firewalls in the Meraki cloud

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
> To use it in a playbook, specify: `cisco.meraki.meraki_mx_l3_firewall`.

- [DEPRECATED](meraki_mx_l3_firewall_module.md#deprecated)
- [Synopsis](meraki_mx_l3_firewall_module.md#synopsis)
- [Parameters](meraki_mx_l3_firewall_module.md#parameters)
- [Notes](meraki_mx_l3_firewall_module.md#notes)
- [Examples](meraki_mx_l3_firewall_module.md#examples)
- [Return Values](meraki_mx_l3_firewall_module.md#return-values)
- [Status](meraki_mx_l3_firewall_module.md#status)

## [DEPRECATED](meraki_mx_l3_firewall_module.md#id1)

Removed in:
:   version 3.0.0

Why:
:   Updated modules released with increased functionality

Alternative:
:   cisco.meraki.networks_appliance_firewall_l3_firewall_rules

## [Synopsis](meraki_mx_l3_firewall_module.md#id2)

- Allows for creation, management, and visibility into layer 3 firewalls implemented on Meraki MX firewalls.

## [Parameters](meraki_mx_l3_firewall_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  **Default:** `"api.meraki.com"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  **Default:** `60` |
| **net_id**  string | ID of network which MX firewall is in. |
| **net_name**  string | Name of network which MX firewall is in. |
| **org_id**  string | ID of organization. |
| **org_name**  aliases: organization  string | Name of organization. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  **Choices:**   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  **Choices:**   - `"debug"` - `"normal"` ← (default) |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  **Default:** `165` |
| **rules**  list / elements=dictionary | List of firewall rules. |
| **comment**  string | Optional comment to describe the firewall rule. |
| **dest_cidr**  string | Comma separated list of CIDR notation destination networks.  `Any` must be capitalized. |
| **dest_port**  string | Comma separated list of destination port numbers to match against.  `Any` must be capitalized. |
| **policy**  string | Policy to apply if rule is hit.  **Choices:**   - `"allow"` - `"deny"` |
| **protocol**  string | Protocol to match against.  **Choices:**   - `"any"` - `"icmp"` - `"tcp"` - `"udp"` |
| **src_cidr**  string | Comma separated list of CIDR notation source networks.  `Any` must be capitalized. |
| **src_port**  string | Comma separated list of source port numbers to match against.  `Any` must be capitalized. |
| **syslog_enabled**  boolean | Whether to log hints against the firewall rule.  Only applicable if a syslog server is specified against the network.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | Create or modify an organization.  **Choices:**   - `"present"` ← (default) - `"query"` |
| **syslog_default_rule**  boolean | Whether to log hits against the default firewall rule.  Only applicable if a syslog server is specified against the network.  This is not shown in response from Meraki. Instead, refer to the `syslog_enabled` value in the default rule.  **Choices:**   - `false` - `true` |
| **timeout**  integer | Time to timeout for HTTP requests.  **Default:** `30` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  **Choices:**   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](meraki_mx_l3_firewall_module.md#id4)

> **Note:**
>
> - Module assumes a complete list of firewall rules are passed as a parameter.
> - If there is interest in this module allowing manipulation of a single firewall rule, please submit an issue against this module.
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_mx_l3_firewall_module.md#id5)

```yaml+jinja
- name: Query firewall rules
  meraki_mx_l3_firewall:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    state: query
  delegate_to: localhost

- name: Set two firewall rules
  meraki_mx_l3_firewall:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    state: present
    rules:
      - comment: Block traffic to server
        src_cidr: 192.0.1.0/24
        src_port: any
        dest_cidr: 192.0.2.2/32
        dest_port: any
        protocol: any
        policy: deny
      - comment: Allow traffic to group of servers
        src_cidr: 192.0.1.0/24
        src_port: any
        dest_cidr: 192.0.2.0/24
        dest_port: any
        protocol: any
        policy: allow
  delegate_to: localhost

- name: Set one firewall rule and enable logging of the default rule
  meraki_mx_l3_firewall:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    state: present
    rules:
      - comment: Block traffic to server
        src_cidr: 192.0.1.0/24
        src_port: any
        dest_cidr: 192.0.2.2/32
        dest_port: any
        protocol: any
        policy: deny
    syslog_default_rule: yes
  delegate_to: localhost
```

## [Return Values](meraki_mx_l3_firewall_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | Firewall rules associated to network.  **Returned:** success |
| **rules**  complex | List of firewall rules.  **Returned:** success |
| **comment**  string | Comment to describe the firewall rule.  **Returned:** always  **Sample:** `"Block traffic to server"` |
| **dest_cidr**  string | Comma separated list of CIDR notation destination networks.  **Returned:** always  **Sample:** `"192.0.1.1/32,192.0.1.2/32"` |
| **dest_port**  string | Comma separated list of destination ports.  **Returned:** always  **Sample:** `"80,443"` |
| **policy**  string | Action to take when rule is matched.  **Returned:** always |
| **protocol**  string | Network protocol for which to match against.  **Returned:** always  **Sample:** `"tcp"` |
| **src_cidr**  string | Comma separated list of CIDR notation source networks.  **Returned:** always  **Sample:** `"192.0.1.1/32,192.0.1.2/32"` |
| **src_port**  string | Comma separated list of source ports.  **Returned:** always  **Sample:** `"80,443"` |
| **syslog_enabled**  boolean | Whether to log to syslog when rule is matched.  **Returned:** always  **Sample:** `true` |

## [Status](meraki_mx_l3_firewall_module.md#id7)

- This module will be removed in version 3.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](meraki_mx_l3_firewall_module.md#deprecated).

### Authors

- Kevin Breit (@kbreit)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
