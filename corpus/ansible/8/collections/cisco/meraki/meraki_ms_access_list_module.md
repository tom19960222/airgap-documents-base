---
collection: ansible
version: "8"
title: "cisco.meraki.meraki_ms_access_list module – Manage access lists for Meraki switches in the Meraki cloud"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/meraki_ms_access_list_module.html
fetched_at: 2026-07-28T01:32:28+00:00
---
# cisco.meraki.meraki_ms_access_list module – Manage access lists for Meraki switches in the Meraki cloud

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
> To use it in a playbook, specify: `cisco.meraki.meraki_ms_access_list`.

New in cisco.meraki 0.1.0

- [DEPRECATED](meraki_ms_access_list_module.md#deprecated)
- [Synopsis](meraki_ms_access_list_module.md#synopsis)
- [Parameters](meraki_ms_access_list_module.md#parameters)
- [Notes](meraki_ms_access_list_module.md#notes)
- [Examples](meraki_ms_access_list_module.md#examples)
- [Return Values](meraki_ms_access_list_module.md#return-values)
- [Status](meraki_ms_access_list_module.md#status)

## [DEPRECATED](meraki_ms_access_list_module.md#id1)

Removed in:
:   version 3.0.0

Why:
:   Updated modules released with increased functionality

Alternative:
:   cisco.meraki.networks_switch_access_control_lists

## [Synopsis](meraki_ms_access_list_module.md#id2)

- Configure and query information about access lists on Meraki switches within the Meraki cloud.

## [Parameters](meraki_ms_access_list_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  **Default:** `"api.meraki.com"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  **Default:** `60` |
| **net_id**  string | ID of network which configuration is applied to. |
| **net_name**  aliases: network  string | Name of network which configuration is applied to. |
| **org_id**  string | ID of organization. |
| **org_name**  aliases: organization  string | Name of organization. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  **Choices:**   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  **Choices:**   - `"debug"` - `"normal"` ← (default) |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  **Default:** `165` |
| **rules**  list / elements=dictionary | List of access control rules. |
| **comment**  string | Description of the rule. |
| **dst_cidr**  string | CIDR notation of source IP address to match. |
| **dst_port**  string | Port number of destination port to match.  May be a port number or ‘any’. |
| **ip_version**  string | Type of IP packets to match.  **Choices:**   - `"any"` - `"ipv4"` - `"ipv6"` |
| **policy**  string | Action to take on matching traffic.  **Choices:**   - `"allow"` - `"deny"` |
| **protocol**  string | Type of protocol to match.  **Choices:**   - `"any"` - `"tcp"` - `"udp"` |
| **src_cidr**  string | CIDR notation of source IP address to match. |
| **src_port**  string | Port number of source port to match.  May be a port number or ‘any’. |
| **vlan**  string | Incoming traffic VLAN.  May be any port between 1-4095 or ‘any’. |
| **state**  string | Specifies whether object should be queried, created/modified, or removed.  **Choices:**   - `"absent"` - `"present"` - `"query"` ← (default) |
| **timeout**  integer | Time to timeout for HTTP requests.  **Default:** `30` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  **Choices:**   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](meraki_ms_access_list_module.md#id4)

> **Note:**
>
> - Some of the options are likely only used for developers within Meraki.
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_ms_access_list_module.md#id5)

```yaml+jinja
- name: Set access list
  meraki_switch_access_list:
    auth_key: abc123
    state: present
    org_name: YourOrg
    net_name: YourNet
    rules:
      - comment: Fake rule
        policy: allow
        ip_version: ipv4
        protocol: udp
        src_cidr: 192.0.1.0/24
        src_port: "4242"
        dst_cidr: 1.2.3.4/32
        dst_port: "80"
        vlan: "100"
  delegate_to: localhost

- name: Query access lists
  meraki_switch_access_list:
    auth_key: abc123
    state: query
    org_name: YourOrg
    net_name: YourNet
  delegate_to: localhost
```

## [Return Values](meraki_ms_access_list_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | List of administrators.  **Returned:** success |
| **rules**  list / elements=string | List of access control rules.  **Returned:** success |
| **comment**  string | Description of the rule.  **Returned:** success  **Sample:** `"User rule"` |
| **dst_cidr**  string | CIDR notation of source IP address to match.  **Returned:** success  **Sample:** `"1.2.3.4/32"` |
| **dst_port**  string | Port number of destination port to match.  **Returned:** success  **Sample:** `"80"` |
| **ip_version**  string | Type of IP packets to match.  **Returned:** success  **Sample:** `"ipv4"` |
| **policy**  string | Action to take on matching traffic.  **Returned:** success  **Sample:** `"allow"` |
| **protocol**  string | Type of protocol to match.  **Returned:** success  **Sample:** `"udp"` |
| **src_cidr**  string | CIDR notation of source IP address to match.  **Returned:** success  **Sample:** `"192.0.1.0/24"` |
| **src_port**  string | Port number of source port to match.  **Returned:** success  **Sample:** `"1234"` |
| **vlan**  string | Incoming traffic VLAN.  **Returned:** success  **Sample:** `"100"` |

## [Status](meraki_ms_access_list_module.md#id7)

- This module will be removed in version 3.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](meraki_ms_access_list_module.md#deprecated).

### Authors

- Kevin Breit (@kbreit)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
