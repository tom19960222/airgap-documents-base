---
collection: ansible
version: "6"
title: "cisco.meraki.meraki_mr_l3_firewall module – Manage MR access point layer 3 firewalls in the Meraki cloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/meraki/meraki_mr_l3_firewall_module.html
fetched_at: 2026-07-27T17:00:21+00:00
---
# cisco.meraki.meraki_mr_l3_firewall module – Manage MR access point layer 3 firewalls in the Meraki cloud

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
> To use it in a playbook, specify: `cisco.meraki.meraki_mr_l3_firewall`.

- [Synopsis](meraki_mr_l3_firewall_module.md#synopsis)
- [Parameters](meraki_mr_l3_firewall_module.md#parameters)
- [Notes](meraki_mr_l3_firewall_module.md#notes)
- [Examples](meraki_mr_l3_firewall_module.md#examples)

## [Synopsis](meraki_mr_l3_firewall_module.md#id1)

- Allows for creation, management, and visibility into layer 3 firewalls implemented on Meraki MR access points.
- Module is not idempotent as of current release.

## [Parameters](meraki_mr_l3_firewall_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **allow_lan_access**  boolean | Sets whether devices can talk to other devices on the same LAN.  Choices:   - `false` - `true` ← (default) |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  Default: `"api.meraki.com"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  Default: `60` |
| **net_id**  string | ID of network containing access points. |
| **net_name**  string | Name of network containing access points. |
| **number**  aliases: ssid_number  string | Number of SSID to apply firewall rule to. |
| **org_id**  string | ID of organization. |
| **org_name**  aliases: organization  string | Name of organization. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  Choices:   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  Choices:   - `"debug"` - `"normal"` ← (default) |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  Default: `165` |
| **rules**  list / elements=dictionary | List of firewall rules. |
| **comment**  string | Optional comment describing the firewall rule. |
| **dest_cidr**  string | Comma-separated list of CIDR notation networks to match. |
| **dest_port**  string | Comma-seperated list of destination ports to match. |
| **policy**  string | Specifies the action that should be taken when rule is hit.  Choices:   - `"allow"` - `"deny"` |
| **protocol**  string | Specifies protocol to match against.  Choices:   - `"any"` - `"icmp"` - `"tcp"` - `"udp"` |
| **ssid_name**  aliases: ssid  string | Name of SSID to apply firewall rule to. |
| **state**  string | Create or modify an organization.  Choices:   - `"present"` ← (default) - `"query"` |
| **timeout**  integer | Time to timeout for HTTP requests.  Default: `30` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  Choices:   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](meraki_mr_l3_firewall_module.md#id3)

> **Note:**
>
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_mr_l3_firewall_module.md#id4)

```yaml+jinja
- name: Create single firewall rule
  meraki_mr_l3_firewall:
    auth_key: abc123
    state: present
    org_name: YourOrg
    net_id: 12345
    number: 1
    rules:
      - comment: Integration test rule
        policy: allow
        protocol: tcp
        dest_port: 80
        dest_cidr: 192.0.2.0/24
    allow_lan_access: no
  delegate_to: localhost

- name: Enable local LAN access
  meraki_mr_l3_firewall:
    auth_key: abc123
    state: present
    org_name: YourOrg
    net_id: 123
    number: 1
    rules:
    allow_lan_access: yes
  delegate_to: localhost

- name: Query firewall rules
  meraki_mr_l3_firewall:
    auth_key: abc123
    state: query
    org_name: YourOrg
    net_name: YourNet
    number: 1
  delegate_to: localhost
```

### Authors

- Kevin Breit (@kbreit)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-meraki/issues)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-meraki)
