---
collection: ansible
version: "6"
title: "cisco.meraki.meraki_device module – Manage devices in the Meraki cloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/meraki/meraki_device_module.html
fetched_at: 2026-07-27T17:00:19+00:00
---
# cisco.meraki.meraki_device module – Manage devices in the Meraki cloud

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
> To use it in a playbook, specify: `cisco.meraki.meraki_device`.

- [Synopsis](meraki_device_module.md#synopsis)
- [Parameters](meraki_device_module.md#parameters)
- [Notes](meraki_device_module.md#notes)
- [Examples](meraki_device_module.md#examples)
- [Return Values](meraki_device_module.md#return-values)

## [Synopsis](meraki_device_module.md#id1)

- Visibility into devices associated to a Meraki environment.

## [Parameters](meraki_device_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **address**  string | Postal address of device’s location. |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  Default: `"api.meraki.com"` |
| **hostname**  aliases: name  string | Hostname of network device to search for. |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  Default: `60` |
| **lat**  aliases: latitude  float | Latitude of device’s geographic location.  Use negative number for southern hemisphere. |
| **lldp_cdp_timespan**  integer | Timespan, in seconds, used to query LLDP and CDP information.  Must be less than 1 month. |
| **lng**  aliases: longitude  float | Longitude of device’s geographic location.  Use negative number for western hemisphere. |
| **model**  string | Model of network device to search for. |
| **move_map_marker**  boolean | Whether or not to set the latitude and longitude of a device based on the new address.  Only applies when `lat` and `lng` are not specified.  Choices:   - `false` - `true` |
| **net_id**  string | ID of a network. |
| **net_name**  aliases: network  string | Name of a network. |
| **note**  string | Informational notes about a device.  Limited to 255 characters. |
| **org_id**  string | ID of organization. |
| **org_name**  aliases: organization  string | Name of organization. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  Choices:   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  Choices:   - `"debug"` - `"normal"` ← (default) |
| **query**  string | Specifies what information should be queried.  Choices:   - `"lldp_cdp"` - `"uplink"` |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  Default: `165` |
| **serial**  string | Serial number of a device to query. |
| **state**  string | Query an organization.  Choices:   - `"absent"` - `"present"` - `"query"` ← (default) |
| **tags**  list / elements=string | Space delimited list of tags to assign to device. |
| **timeout**  integer | Time to timeout for HTTP requests.  Default: `30` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  Choices:   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](meraki_device_module.md#id3)

> **Note:**
>
> - This module does not support claiming of devices or licenses into a Meraki organization.
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_device_module.md#id4)

```yaml+jinja
- name: Query all devices in an organization.
  meraki_device:
    auth_key: abc12345
    org_name: YourOrg
    state: query
  delegate_to: localhost

- name: Query all devices in a network.
  meraki_device:
    auth_key: abc12345
    org_name: YourOrg
    net_name: YourNet
    state: query
  delegate_to: localhost

- name: Query a device by serial number.
  meraki_device:
    auth_key: abc12345
    org_name: YourOrg
    net_name: YourNet
    serial: ABC-123
    state: query
  delegate_to: localhost

- name: Lookup uplink information about a device.
  meraki_device:
    auth_key: abc12345
    org_name: YourOrg
    net_name: YourNet
    serial_uplink: ABC-123
    state: query
  delegate_to: localhost

- name: Lookup LLDP and CDP information about devices connected to specified device.
  meraki_device:
    auth_key: abc12345
    org_name: YourOrg
    net_name: YourNet
    serial_lldp_cdp: ABC-123
    state: query
  delegate_to: localhost

- name: Lookup a device by hostname.
  meraki_device:
    auth_key: abc12345
    org_name: YourOrg
    net_name: YourNet
    hostname: main-switch
    state: query
  delegate_to: localhost

- name: Query all devices of a specific model.
  meraki_device:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    model: MR26
    state: query
  delegate_to: localhost

- name: Update information about a device.
  meraki_device:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    state: present
    serial: '{{serial}}'
    name: mr26
    address: 1060 W. Addison St., Chicago, IL
    lat: 41.948038
    lng: -87.65568
    tags: recently-added
  delegate_to: localhost

- name: Claim a device into a network.
  meraki_device:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    serial: ABC-123
    state: present
  delegate_to: localhost

- name: Remove a device from a network.
  meraki_device:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    serial: ABC-123
    state: absent
  delegate_to: localhost
```

## [Return Values](meraki_device_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **response**  dictionary | Data returned from Meraki dashboard.  Returned: info |

### Authors

- Kevin Breit (@kbreit)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-meraki/issues)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-meraki)
