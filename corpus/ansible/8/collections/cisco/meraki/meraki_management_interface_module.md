---
collection: ansible
version: "8"
title: "cisco.meraki.meraki_management_interface module – Configure Meraki management interfaces"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/meraki_management_interface_module.html
fetched_at: 2026-07-28T01:32:23+00:00
---
# cisco.meraki.meraki_management_interface module – Configure Meraki management interfaces

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
> To use it in a playbook, specify: `cisco.meraki.meraki_management_interface`.

New in cisco.meraki 1.1.0

- [DEPRECATED](meraki_management_interface_module.md#deprecated)
- [Synopsis](meraki_management_interface_module.md#synopsis)
- [Parameters](meraki_management_interface_module.md#parameters)
- [Notes](meraki_management_interface_module.md#notes)
- [Examples](meraki_management_interface_module.md#examples)
- [Return Values](meraki_management_interface_module.md#return-values)
- [Status](meraki_management_interface_module.md#status)

## [DEPRECATED](meraki_management_interface_module.md#id1)

Removed in:
:   version 3.0.0

Why:
:   Updated modules released with increased functionality

Alternative:
:   cisco.meraki.devices_management_interface

## [Synopsis](meraki_management_interface_module.md#id2)

- Allows for configuration of management interfaces on Meraki MX, MS, and MR devices.

## [Parameters](meraki_management_interface_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  **Default:** `"api.meraki.com"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  **Default:** `60` |
| **net_id**  string | ID of the network to bind or unbind configuration template to. |
| **net_name**  string | Name of the network to bind or unbind configuration template to. |
| **org_id**  string | ID of organization associated to a configuration template. |
| **org_name**  aliases: organization  string | Name of organization containing the configuration template. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  **Choices:**   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  **Choices:**   - `"debug"` - `"normal"` ← (default) |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  **Default:** `165` |
| **serial**  string / required | serial number of the device to configure. |
| **state**  string | Specifies whether configuration template information should be queried, modified, or deleted.  **Choices:**   - `"absent"` - `"query"` ← (default) - `"present"` |
| **timeout**  integer | Time to timeout for HTTP requests.  **Default:** `30` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  **Choices:**   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  **Choices:**   - `false` - `true` ← (default) |
| **wan1**  aliases: mgmt1  dictionary | Management interface details for management interface. |
| **static_dns**  list / elements=string | DNS servers to use.  Allows for a maximum of 2 addresses. |
| **static_gateway_ip**  string | IP address for default gateway.  Valid only if `using_static_ip` is `True`. |
| **static_ip**  string | IP address assigned to Management interface.  Valid only if `using_static_ip` is `True`. |
| **static_subnet_mask**  string | Netmask for static IP address.  Valid only if `using_static_ip` is `True`. |
| **using_static_ip**  boolean | Configures the interface to use static IP or DHCP.  **Choices:**   - `false` - `true` |
| **vlan**  integer | VLAN number to use for the management network. |
| **wan_enabled**  string | States whether the management interface is enabled.  Only valid for MX devices.  **Choices:**   - `"disabled"` - `"enabled"` - `"not configured"` |
| **wan2**  aliases: mgmt2  dictionary | Management interface details for management interface. |
| **static_dns**  list / elements=string | DNS servers to use.  Allows for a maximum of 2 addresses. |
| **static_gateway_ip**  string | IP address for default gateway.  Valid only if `using_static_ip` is `True`. |
| **static_ip**  string | IP address assigned to Management interface.  Valid only if `using_static_ip` is `True`. |
| **static_subnet_mask**  string | Netmask for static IP address.  Valid only if `using_static_ip` is `True`. |
| **using_static_ip**  boolean | Configures the interface to use static IP or DHCP.  **Choices:**   - `false` - `true` |
| **vlan**  integer | VLAN number to use for the management network. |
| **wan_enabled**  string | States whether the management interface is enabled.  Only valid for MX devices.  **Choices:**   - `"disabled"` - `"enabled"` - `"not configured"` |

## [Notes](meraki_management_interface_module.md#id4)

> **Note:**
>
> - `WAN2` parameter is only valid for MX appliances.
> - `wan_enabled` should not be provided for non-MX devies.
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_management_interface_module.md#id5)

```yaml+jinja
- name: Set WAN2 as static IP
  meraki_management_interface:
    auth_key: abc123
    state: present
    org_name: YourOrg
    net_id: YourNetId
    serial: AAAA-BBBB-CCCC
    wan2:
      wan_enabled: enabled
      using_static_ip: yes
      static_ip: 192.168.16.195
      static_gateway_ip: 192.168.16.1
      static_subnet_mask: 255.255.255.0
      static_dns:
        - 1.1.1.1
      vlan: 1
  delegate_to: localhost

- name: Query management information
  meraki_management_interface:
    auth_key: abc123
    state: query
    org_name: YourOrg
    net_id: YourNetId
    serial: AAAA-BBBB-CCCC
  delegate_to: localhost
```

## [Return Values](meraki_management_interface_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | Information about queried object.  **Returned:** success |
| **wan1**  complex | Management configuration for WAN1 interface  **Returned:** success |
| **static_dns**  list / elements=string | List of DNS IP addresses  **Returned:** only if static IP assignment is used  **Sample:** `["1.1.1.1"]` |
| **static_gateway_ip**  string | Assigned static gateway IP  **Returned:** only if static IP assignment is used  **Sample:** `"192.0.1.1"` |
| **static_ip**  string | Assigned static IP  **Returned:** only if static IP assignment is used  **Sample:** `"192.0.1.2"` |
| **static_subnet_mask**  string | Assigned netmask for static IP  **Returned:** only if static IP assignment is used  **Sample:** `"255.255.255.0"` |
| **using_static_ip**  boolean | Boolean value of whether static IP assignment is used on interface  **Returned:** success  **Sample:** `true` |
| **vlan**  integer | VLAN tag id of management VLAN  **Returned:** success  **Sample:** `2` |
| **wan_enabled**  string | Enabled state of interface  **Returned:** success  **Sample:** `"enabled"` |
| **wan2**  complex | Management configuration for WAN1 interface  **Returned:** success |
| **static_dns**  list / elements=string | List of DNS IP addresses  **Returned:** only if static IP assignment is used  **Sample:** `["1.1.1.1"]` |
| **static_gateway_ip**  string | Assigned static gateway IP  **Returned:** only if static IP assignment is used  **Sample:** `"192.0.1.1"` |
| **static_ip**  string | Assigned static IP  **Returned:** only if static IP assignment is used  **Sample:** `"192.0.1.2"` |
| **static_subnet_mask**  string | Assigned netmask for static IP  **Returned:** only if static IP assignment is used  **Sample:** `"255.255.255.0"` |
| **using_static_ip**  boolean | Boolean value of whether static IP assignment is used on interface  **Returned:** success  **Sample:** `true` |
| **vlan**  integer | VLAN tag id of management VLAN  **Returned:** success  **Sample:** `2` |
| **wan_enabled**  string | Enabled state of interface  **Returned:** success  **Sample:** `"enabled"` |

## [Status](meraki_management_interface_module.md#id7)

- This module will be removed in version 3.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](meraki_management_interface_module.md#deprecated).

### Authors

- Kevin Breit (@kbreit)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
