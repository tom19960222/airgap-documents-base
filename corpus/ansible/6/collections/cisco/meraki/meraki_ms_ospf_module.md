---
collection: ansible
version: "6"
title: "cisco.meraki.meraki_ms_ospf module – Manage OSPF configuration on MS switches"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/meraki/meraki_ms_ospf_module.html
fetched_at: 2026-07-27T17:00:28+00:00
---
# cisco.meraki.meraki_ms_ospf module – Manage OSPF configuration on MS switches

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
> To use it in a playbook, specify: `cisco.meraki.meraki_ms_ospf`.

- [Synopsis](meraki_ms_ospf_module.md#synopsis)
- [Parameters](meraki_ms_ospf_module.md#parameters)
- [Notes](meraki_ms_ospf_module.md#notes)
- [Examples](meraki_ms_ospf_module.md#examples)
- [Return Values](meraki_ms_ospf_module.md#return-values)

## [Synopsis](meraki_ms_ospf_module.md#id1)

- Configure OSPF for compatible Meraki MS switches.

## [Parameters](meraki_ms_ospf_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **areas**  list / elements=dictionary | List of areas in OSPF network. |
| **area_id**  aliases: id  integer | OSPF area ID |
| **area_name**  aliases: name  string | Descriptive name of OSPF area. |
| **area_type**  aliases: type  string | OSPF area type.  Choices:   - `"normal"` - `"stub"` - `"nssa"` |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **dead_timer**  integer | Time interval to determine when the peer will be declared inactive.  Value must be between 1 and 65535. |
| **enabled**  boolean | Enable or disable OSPF on the network.  Choices:   - `false` - `true` |
| **hello_timer**  integer | Time interval, in seconds, at which hello packets will be sent to OSPF neighbors to maintain connectivity.  Value must be between 1 and 255.  Default is 10 seconds. |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  Default: `"api.meraki.com"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  Default: `60` |
| **md5_authentication_enabled**  boolean | Whether to enable or disable MD5 authentication.  Choices:   - `false` - `true` |
| **md5_authentication_key**  dictionary | MD5 authentication credentials. |
| **id**  string | MD5 authentication key index.  Must be between 1 and 255. |
| **passphrase**  string | Plain text authentication passphrase |
| **net_id**  string | ID of network containing OSPF configuration. |
| **net_name**  aliases: name, network  string | Name of network containing OSPF configuration. |
| **org_id**  string | ID of organization. |
| **org_name**  aliases: organization  string | Name of organization. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  Choices:   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  Choices:   - `"debug"` - `"normal"` ← (default) |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  Default: `165` |
| **state**  string | Read or edit OSPF settings.  Choices:   - `"present"` ← (default) - `"query"` |
| **timeout**  integer | Time to timeout for HTTP requests.  Default: `30` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  Choices:   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](meraki_ms_ospf_module.md#id3)

> **Note:**
>
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_ms_ospf_module.md#id4)

```yaml+jinja
- name: Query OSPF settings
  meraki_ms_ospf:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    state: query
  delegate_to: localhost

- name: Enable OSPF with check mode
  meraki_ms_ospf:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    state: present
    enabled: true
    hello_timer: 20
    dead_timer: 60
    areas:
      - area_id: 0
        area_name: Backbone
        area_type: normal
      - area_id: 1
        area_name: Office
        area_type: nssa
    md5_authentication_enabled: false
```

## [Return Values](meraki_ms_ospf_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | Information about queried object.  Returned: success |
| **areas**  complex | List of areas in OSPF network.  Returned: success |
| **area_id**  integer | OSPF area ID  Returned: success |
| **area_name**  string | Descriptive name of OSPF area.  Returned: success |
| **area_type**  string | OSPF area type.  Returned: success |
| **dead_timer_in_seconds**  integer | Time interval to determine when the peer will be declared inactive.  Returned: success |
| **enabled**  boolean | Enable or disable OSPF on the network.  Returned: success |
| **hello_timer_in_seconds**  integer | Time interval, in seconds, at which hello packets will be sent to OSPF neighbors to maintain connectivity.  Returned: success |
| **md5_authentication_enabled**  boolean | Whether to enable or disable MD5 authentication.  Returned: success |
| **md5_authentication_key**  complex | MD5 authentication credentials.  Returned: success |
| **id**  integer | MD5 key index.  Returned: success |
| **passphrase**  string | Passphrase for MD5 key.  Returned: success |

### Authors

- Kevin Breit (@kbreit)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-meraki/issues)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-meraki)
