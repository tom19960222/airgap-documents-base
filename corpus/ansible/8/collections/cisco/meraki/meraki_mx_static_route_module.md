---
collection: ansible
version: "8"
title: "cisco.meraki.meraki_mx_static_route module – Manage static routes in the Meraki cloud"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/meraki_mx_static_route_module.html
fetched_at: 2026-07-28T01:32:42+00:00
---
# cisco.meraki.meraki_mx_static_route module – Manage static routes in the Meraki cloud

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
> To use it in a playbook, specify: `cisco.meraki.meraki_mx_static_route`.

- [DEPRECATED](meraki_mx_static_route_module.md#deprecated)
- [Synopsis](meraki_mx_static_route_module.md#synopsis)
- [Parameters](meraki_mx_static_route_module.md#parameters)
- [Notes](meraki_mx_static_route_module.md#notes)
- [Examples](meraki_mx_static_route_module.md#examples)
- [Return Values](meraki_mx_static_route_module.md#return-values)
- [Status](meraki_mx_static_route_module.md#status)

## [DEPRECATED](meraki_mx_static_route_module.md#id1)

Removed in:
:   version 3.0.0

Why:
:   Updated modules released with increased functionality

Alternative:
:   cisco.meraki.networks_appliance_static_routes

## [Synopsis](meraki_mx_static_route_module.md#id2)

- Allows for creation, management, and visibility into static routes within Meraki.

## [Parameters](meraki_mx_static_route_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **enabled**  boolean | Indicates whether static route is enabled within a network.  **Choices:**   - `false` - `true` |
| **fixed_ip_assignments**  list / elements=dictionary | List of fixed MAC to IP bindings for DHCP. |
| **ip**  string | IP address of endpoint. |
| **mac**  string | MAC address of endpoint. |
| **name**  string | Hostname of endpoint. |
| **gateway_ip**  string | IP address of the gateway for the subnet. |
| **gateway_vlan_id**  integer | The gateway IP (next hop) VLAN ID of the static route. |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  **Default:** `"api.meraki.com"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  **Default:** `60` |
| **name**  string | Descriptive name of the static route. |
| **net_id**  string | ID number of a network. |
| **net_name**  string | Name of a network. |
| **org_id**  string | ID of organization. |
| **org_name**  aliases: organization  string | Name of organization. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  **Choices:**   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  **Choices:**   - `"debug"` - `"normal"` ← (default) |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  **Default:** `165` |
| **reserved_ip_ranges**  list / elements=dictionary | List of IP ranges reserved for static IP assignments. |
| **comment**  string | Human readable description of reservation range. |
| **end**  string | Last IP address of reserved range. |
| **start**  string | First IP address of reserved range. |
| **route_id**  string | Unique ID of static route. |
| **state**  string | Create or modify an organization.  **Choices:**   - `"absent"` - `"query"` - `"present"` ← (default) |
| **subnet**  string | CIDR notation based subnet for static route. |
| **timeout**  integer | Time to timeout for HTTP requests.  **Default:** `30` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  **Choices:**   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](meraki_mx_static_route_module.md#id4)

> **Note:**
>
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_mx_static_route_module.md#id5)

```yaml+jinja
- name: Create static_route
  meraki_static_route:
    auth_key: abc123
    state: present
    org_name: YourOrg
    net_name: YourNet
    name: Test Route
    subnet: 192.0.1.0/24
    gateway_ip: 192.168.128.1
  delegate_to: localhost

- name: Update static route with fixed IP assignment
  meraki_static_route:
    auth_key: abc123
    state: present
    org_name: YourOrg
    net_name: YourNet
    route_id: d6fa4821-1234-4dfa-af6b-ae8b16c20c39
    fixed_ip_assignments:
      - mac: aa:bb:cc:dd:ee:ff
        ip: 192.0.1.11
        comment: Server
  delegate_to: localhost

- name: Query static routes
  meraki_static_route:
    auth_key: abc123
    state: query
    org_name: YourOrg
    net_name: YourNet
  delegate_to: localhost

- name: Delete static routes
  meraki_static_route:
    auth_key: abc123
    state: absent
    org_name: YourOrg
    net_name: YourNet
    route_id: '{{item}}'
  delegate_to: localhost
```

## [Return Values](meraki_mx_static_route_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | Information about the created or manipulated object.  **Returned:** info |
| **enabled**  boolean | Enabled state of static route.  **Returned:** query or update  **Sample:** `true` |
| **fixedIpAssignments**  complex | List of static MAC to IP address bindings.  **Returned:** query or update |
| **mac**  complex | Key is MAC address of endpoint.  **Returned:** query or update |
| **ip**  string | IP address to be bound to the endpoint.  **Returned:** query or update  **Sample:** `"192.0.1.11"` |
| **name**  string | Hostname given to the endpoint.  **Returned:** query or update  **Sample:** `"JimLaptop"` |
| **gatewayIp**  string | Next hop IP address.  **Returned:** success  **Sample:** `"192.1.1.1"` |
| **id**  string | Unique identification string assigned to each static route.  **Returned:** success  **Sample:** `"d6fa4821-1234-4dfa-af6b-ae8b16c20c39"` |
| **name**  string | Name of static route.  **Returned:** success  **Sample:** `"Data Center static route"` |
| **net_id**  string | Identification string of network.  **Returned:** query or update  **Sample:** `"N_12345"` |
| **reservedIpRanges**  complex | List of IP address ranges which are reserved for static assignment.  **Returned:** query or update |
| **comment**  string | Human readable description of range.  **Returned:** query or update  **Sample:** `"Server range"` |
| **end**  string | Last address in reservation range, inclusive.  **Returned:** query or update  **Sample:** `"192.0.1.10"` |
| **start**  string | First address in reservation range, inclusive.  **Returned:** query or update  **Sample:** `"192.0.1.2"` |
| **subnet**  string | CIDR notation subnet for static route.  **Returned:** success  **Sample:** `"192.0.1.0/24"` |

## [Status](meraki_mx_static_route_module.md#id7)

- This module will be removed in version 3.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](meraki_mx_static_route_module.md#deprecated).

### Authors

- Kevin Breit (@kbreit)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
