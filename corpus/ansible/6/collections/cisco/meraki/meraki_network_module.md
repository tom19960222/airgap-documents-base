---
collection: ansible
version: "6"
title: "cisco.meraki.meraki_network module – Manage networks in the Meraki cloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/meraki/meraki_network_module.html
fetched_at: 2026-07-27T17:00:41+00:00
---
# cisco.meraki.meraki_network module – Manage networks in the Meraki cloud

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
> To use it in a playbook, specify: `cisco.meraki.meraki_network`.

- [Synopsis](meraki_network_module.md#synopsis)
- [Parameters](meraki_network_module.md#parameters)
- [Notes](meraki_network_module.md#notes)
- [Examples](meraki_network_module.md#examples)
- [Return Values](meraki_network_module.md#return-values)

## [Synopsis](meraki_network_module.md#id1)

- Allows for creation, management, and visibility into networks within Meraki.

## [Parameters](meraki_network_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **copy_from_network_id**  string | New network inherits properties from this network ID.  Other provided parameters will override the copied configuration.  Type which must match this network’s type exactly. |
| **enable_vlans**  boolean | Boolean value specifying whether VLANs should be supported on a network.  Requires `net_name` or `net_id` to be specified.  Choices:   - `false` - `true` |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  Default: `"api.meraki.com"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  Default: `60` |
| **local_status_page_enabled**  boolean | - Enables the local device status pages (U[my.meraki.com](my.meraki.com), U[ap.meraki.com](ap.meraki.com), U[switch.meraki.com](switch.meraki.com), U[wired.meraki.com](wired.meraki.com)). - Only can be specified on its own or with `remote_status_page_enabled`.   Choices:   - `false` - `true` |
| **net_id**  string | ID number of a network. |
| **net_name**  aliases: name, network  string | Name of a network. |
| **org_id**  string | ID of organization. |
| **org_name**  aliases: organization  string | Name of organization. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  Choices:   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  Choices:   - `"debug"` - `"normal"` ← (default) |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  Default: `165` |
| **remote_status_page_enabled**  boolean | Enables access to the device status page (<http://device%20LAN%20IP>).  Can only be set if `local_status_page_enabled:` is set to `yes`.  Only can be specified on its own or with `local_status_page_enabled`.  Choices:   - `false` - `true` |
| **state**  string | Create or modify an organization.  Choices:   - `"absent"` - `"present"` ← (default) - `"query"` |
| **tags**  list / elements=string | List of tags to assign to network.  `tags` name conflicts with the tags parameter in Ansible. Indentation problems may cause unexpected behaviors.  Ansible 2.8 converts this to a list from a comma separated list. |
| **timeout**  integer | Time to timeout for HTTP requests.  Default: `30` |
| **timezone**  string | Timezone associated to network.  See <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones> for a list of valid timezones. |
| **type**  aliases: net_type  list / elements=string | Type of network device network manages.  Required when creating a network.  As of Ansible 2.8, `combined` type is no longer accepted.  As of Ansible 2.8, changes to this parameter are no longer idempotent.  Choices:   - `"appliance"` - `"switch"` - `"wireless"` - `"sensor"` - `"systemsManager"` - `"camera"` - `"cellularGateway"` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  Choices:   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](meraki_network_module.md#id3)

> **Note:**
>
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_network_module.md#id4)

```yaml+jinja
- delegate_to: localhost
  block:
    - name: List all networks associated to the YourOrg organization
      meraki_network:
        auth_key: abc12345
        state: query
        org_name: YourOrg
    - name: Query network named MyNet in the YourOrg organization
      meraki_network:
        auth_key: abc12345
        state: query
        org_name: YourOrg
        net_name: MyNet
    - name: Create network named MyNet in the YourOrg organization
      meraki_network:
        auth_key: abc12345
        state: present
        org_name: YourOrg
        net_name: MyNet
        type: switch
        timezone: America/Chicago
        tags: production, chicago
    - name: Create combined network named MyNet in the YourOrg organization
      meraki_network:
        auth_key: abc12345
        state: present
        org_name: YourOrg
        net_name: MyNet
        type:
          - switch
          - appliance
        timezone: America/Chicago
        tags: production, chicago
    - name: Create new network based on an existing network
      meraki_network:
        auth_key: abc12345
        state: present
        org_name: YourOrg
        net_name: MyNet
        type:
          - switch
          - appliance
        copy_from_network_id: N_1234
    - name: Enable VLANs on a network
      meraki_network:
        auth_key: abc12345
        state: query
        org_name: YourOrg
        net_name: MyNet
        enable_vlans: yes
    - name: Modify local status page enabled state
      meraki_network:
        auth_key: abc12345
        state: query
        org_name: YourOrg
        net_name: MyNet
        local_status_page_enabled: yes
```

## [Return Values](meraki_network_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | Information about the created or manipulated object.  Returned: info |
| **id**  string | Identification string of network.  Returned: success  Sample: `"N_12345"` |
| **local_status_page_enabled**  boolean | States whether my.meraki.com and other device portals should be enabled.  Returned: success  Sample: `true` |
| **name**  string | Written name of network.  Returned: success  Sample: `"YourNet"` |
| **organization_id**  string | Organization ID which owns the network.  Returned: success  Sample: `"0987654321"` |
| **remote_status_page_enabled**  boolean | Enables access to the device status page.  Returned: success  Sample: `true` |
| **tags**  list / elements=string | Space delimited tags assigned to network.  Returned: success  Sample: `["production"]` |
| **time_zone**  string | Timezone where network resides.  Returned: success  Sample: `"America/Chicago"` |
| **type**  list / elements=string | Functional type of network.  Returned: success  Sample: `["switch"]` |

### Authors

- Kevin Breit (@kbreit)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-meraki/issues)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-meraki)
