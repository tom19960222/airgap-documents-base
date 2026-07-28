---
collection: ansible
version: "8"
title: "cisco.meraki.meraki_mx_site_to_site_vpn module – Manage AutoVPN connections in Meraki"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/meraki_mx_site_to_site_vpn_module.html
fetched_at: 2026-07-28T01:32:41+00:00
---
# cisco.meraki.meraki_mx_site_to_site_vpn module – Manage AutoVPN connections in Meraki

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
> To use it in a playbook, specify: `cisco.meraki.meraki_mx_site_to_site_vpn`.

New in cisco.meraki 1.1.0

- [DEPRECATED](meraki_mx_site_to_site_vpn_module.md#deprecated)
- [Synopsis](meraki_mx_site_to_site_vpn_module.md#synopsis)
- [Parameters](meraki_mx_site_to_site_vpn_module.md#parameters)
- [Notes](meraki_mx_site_to_site_vpn_module.md#notes)
- [Examples](meraki_mx_site_to_site_vpn_module.md#examples)
- [Return Values](meraki_mx_site_to_site_vpn_module.md#return-values)
- [Status](meraki_mx_site_to_site_vpn_module.md#status)

## [DEPRECATED](meraki_mx_site_to_site_vpn_module.md#id1)

Removed in:
:   version 3.0.0

Why:
:   Updated modules released with increased functionality

Alternative:
:   cisco.meraki.networks_appliance_vpn_site_to_site_vpn

## [Synopsis](meraki_mx_site_to_site_vpn_module.md#id2)

- Allows for creation, management, and visibility into AutoVPNs implemented on Meraki MX firewalls.

## [Parameters](meraki_mx_site_to_site_vpn_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  **Default:** `"api.meraki.com"` |
| **hubs**  list / elements=dictionary | List of hubs to assign to a spoke. |
| **hub_id**  string | Network ID of hub |
| **use_default_route**  boolean | Indicates whether deafult troute traffic should be sent to this hub.  Only valid in spoke mode.  **Choices:**   - `false` - `true` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  **Default:** `60` |
| **mode**  string | Set VPN mode for network  **Choices:**   - `"none"` - `"hub"` - `"spoke"` |
| **net_id**  string | ID of network which MX firewall is in. |
| **net_name**  string | Name of network which MX firewall is in. |
| **org_id**  string | ID of organization. |
| **org_name**  aliases: organization  string | Name of organization. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  **Choices:**   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  **Choices:**   - `"debug"` - `"normal"` ← (default) |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  **Default:** `165` |
| **state**  string | Create or modify an organization.  **Choices:**   - `"present"` ← (default) - `"query"` |
| **subnets**  list / elements=dictionary | List of subnets to advertise over VPN. |
| **local_subnet**  string | CIDR formatted subnet. |
| **use_vpn**  boolean | Whether to advertise over VPN.  **Choices:**   - `false` - `true` |
| **timeout**  integer | Time to timeout for HTTP requests.  **Default:** `30` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  **Choices:**   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](meraki_mx_site_to_site_vpn_module.md#id4)

> **Note:**
>
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_mx_site_to_site_vpn_module.md#id5)

```yaml+jinja
- name: Set hub mode
  meraki_site_to_site_vpn:
    auth_key: abc123
    state: present
    org_name: YourOrg
    net_name: hub_network
    mode: hub
  delegate_to: localhost
  register: set_hub

- name: Set spoke mode
  meraki_site_to_site_vpn:
    auth_key: abc123
    state: present
    org_name: YourOrg
    net_name: spoke_network
    mode: spoke
    hubs:
      - hub_id: N_1234
        use_default_route: false
  delegate_to: localhost
  register: set_spoke

- name: Add subnet to hub for VPN. Hub is required.
  meraki_site_to_site_vpn:
    auth_key: abc123
    state: present
    org_name: YourOrg
    net_name: hub_network
    mode: hub
    hubs:
      - hub_id: N_1234
        use_default_route: false
    subnets:
      - local_subnet: 192.168.1.0/24
        use_vpn: true
  delegate_to: localhost
  register: set_hub

- name: Query rules for hub
  meraki_site_to_site_vpn:
    auth_key: abc123
    state: query
    org_name: YourOrg
    net_name: hub_network
  delegate_to: localhost
  register: query_all_hub
```

## [Return Values](meraki_mx_site_to_site_vpn_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | VPN settings.  **Returned:** success |
| **hubs**  complex | Hub networks to associate to.  **Returned:** always |
| **hub_id**  complex | ID of hub network.  **Returned:** always  **Sample:** `"N_12345"` |
| **use_default_route**  boolean | Whether to send all default route traffic over VPN.  **Returned:** always  **Sample:** `true` |
| **mode**  string | Mode assigned to network.  **Returned:** always  **Sample:** `"spoke"` |
| **subnets**  complex | List of subnets to advertise over VPN.  **Returned:** always |
| **local_subnet**  string | CIDR formatted subnet.  **Returned:** always  **Sample:** `"192.168.1.0/24"` |
| **use_vpn**  boolean | Whether subnet should use the VPN.  **Returned:** always  **Sample:** `true` |

## [Status](meraki_mx_site_to_site_vpn_module.md#id7)

- This module will be removed in version 3.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](meraki_mx_site_to_site_vpn_module.md#deprecated).

### Authors

- Kevin Breit (@kbreit)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
