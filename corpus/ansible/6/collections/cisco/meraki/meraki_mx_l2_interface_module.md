---
collection: ansible
version: "6"
title: "cisco.meraki.meraki_mx_l2_interface module – Configure MX layer 2 interfaces"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/meraki/meraki_mx_l2_interface_module.html
fetched_at: 2026-07-27T17:00:33+00:00
---
# cisco.meraki.meraki_mx_l2_interface module – Configure MX layer 2 interfaces

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
> To use it in a playbook, specify: `cisco.meraki.meraki_mx_l2_interface`.

New in cisco.meraki 2.1.0

- [Synopsis](meraki_mx_l2_interface_module.md#synopsis)
- [Parameters](meraki_mx_l2_interface_module.md#parameters)
- [Notes](meraki_mx_l2_interface_module.md#notes)
- [Examples](meraki_mx_l2_interface_module.md#examples)
- [Return Values](meraki_mx_l2_interface_module.md#return-values)

## [Synopsis](meraki_mx_l2_interface_module.md#id1)

- Allows for management and visibility of Merkai MX layer 2 ports.

## [Parameters](meraki_mx_l2_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_policy**  string | The name of the policy. Only applicable to access ports.  Choices:   - `"open"` - `"8021x-radius"` - `"mac-radius"` - `"hybris-radius"` |
| **allowed_vlans**  string | Comma-delimited list of the VLAN ID’s allowed on the port, or ‘all’ to permit all VLAN’s on the port. |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **drop_untagged_traffic**  boolean | Trunk port can Drop all Untagged traffic. When true, no VLAN is required.  Access ports cannot have dropUntaggedTraffic set to true.  Choices:   - `false` - `true` |
| **enabled**  boolean | Enabled state of port.  Choices:   - `false` - `true` |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  Default: `"api.meraki.com"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  Default: `60` |
| **net_id**  string | ID number of a network. |
| **net_name**  aliases: name, network  string | Name of a network. |
| **number**  aliases: port, port_id  integer | ID number of MX port. |
| **org_id**  string | ID of organization associated to a network. |
| **org_name**  aliases: organization  string | Name of organization. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  Choices:   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  Choices:   - `"debug"` - `"normal"` ← (default) |
| **port_type**  string | Type of port.  Choices:   - `"access"` - `"trunk"` |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  Default: `165` |
| **state**  string | Modify or query an port.  Choices:   - `"present"` ← (default) - `"query"` |
| **timeout**  integer | Time to timeout for HTTP requests.  Default: `30` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  Choices:   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  Choices:   - `false` - `true` ← (default) |
| **vlan**  integer | Native VLAN when the port is in Trunk mode.  Access VLAN when the port is in Access mode. |

## [Notes](meraki_mx_l2_interface_module.md#id3)

> **Note:**
>
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_mx_l2_interface_module.md#id4)

```yaml+jinja
- name: Query layer 2 interface settings
  meraki_mx_l2_interface:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    state: query
  delegate_to: localhost

- name: Query a single layer 2 interface settings
  meraki_mx_l2_interface:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    state: query
    number: 2
  delegate_to: localhost

- name: Update interface configuration
  meraki_mx_l2_interface:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    state: present
    number: 2
    port_type: access
    vlan: 10
  delegate_to: localhost
```

## [Return Values](meraki_mx_l2_interface_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | Information about the created or manipulated object.  Returned: success |
| **access_policy**  string | The name of the policy. Only applicable to access ports.  Returned: success  Sample: `"guestUsers"` |
| **allowed_vlans**  string | Comma-delimited list of the VLAN ID’s allowed on the port, or ‘all’ to permit all VLAN’s on the port.  Returned: success  Sample: `"1,5,10"` |
| **drop_untagged_traffic**  boolean | Trunk port can Drop all Untagged traffic. When true, no VLAN is required.  Access ports cannot have dropUntaggedTraffic set to true.  Returned: success  Sample: `true` |
| **enabled**  boolean | Enabled state of port.  Returned: success  Sample: `true` |
| **number**  integer | ID number of MX port.  Returned: success  Sample: `4` |
| **type**  string | Type of port.  Returned: success  Sample: `"access"` |
| **vlan**  integer | Native VLAN when the port is in Trunk mode.  Access VLAN when the port is in Access mode.  Returned: success  Sample: `1` |

### Authors

- Kevin Breit (@kbreit)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-meraki/issues)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-meraki)
