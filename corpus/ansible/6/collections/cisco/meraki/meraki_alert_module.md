---
collection: ansible
version: "6"
title: "cisco.meraki.meraki_alert module – Manage alerts in the Meraki cloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/meraki/meraki_alert_module.html
fetched_at: 2026-07-27T17:00:18+00:00
---
# cisco.meraki.meraki_alert module – Manage alerts in the Meraki cloud

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
> To use it in a playbook, specify: `cisco.meraki.meraki_alert`.

New in cisco.meraki 2.1.0

- [Synopsis](meraki_alert_module.md#synopsis)
- [Parameters](meraki_alert_module.md#parameters)
- [Notes](meraki_alert_module.md#notes)
- [Examples](meraki_alert_module.md#examples)
- [Return Values](meraki_alert_module.md#return-values)

## [Synopsis](meraki_alert_module.md#id1)

- Allows for creation, management, and visibility into alert settings within Meraki.

## [Parameters](meraki_alert_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **alerts**  list / elements=dictionary | Alert-specific configuration for each type. |
| **alert_destinations**  dictionary | A hash of destinations for this specific alert. |
| **all_admins**  boolean | If true, all network admins will receive emails.  Choices:   - `false` - `true` |
| **emails**  list / elements=string | A list of emails that will recieve the alert(s). |
| **http_server_ids**  list / elements=string | A list of HTTP server IDs to send a Webhook to.  Default: `[]` |
| **snmp**  boolean | If true, then an SNMP trap will be sent if there is an SNMP trap server configured for this network.  Choices:   - `false` - `true` |
| **alert_type**  string | The type of alert. |
| **enabled**  boolean | A boolean depicting if the alert is turned on or off.  Choices:   - `false` - `true` |
| **filters**  any | A hash of specific configuration data for the alert. Only filters specific to the alert will be updated.  No validation checks occur against `filters`.  Default: `{}` |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **default_destinations**  dictionary | Properties for destinations when alert specific destinations aren’t specified. |
| **all_admins**  boolean | If true, all network admins will receive emails.  Choices:   - `false` - `true` |
| **emails**  list / elements=string | A list of emails that will recieve the alert(s). |
| **http_server_ids**  list / elements=string | A list of HTTP server IDs to send a Webhook to.  Default: `[]` |
| **snmp**  boolean | If true, then an SNMP trap will be sent if there is an SNMP trap server configured for this network.  Choices:   - `false` - `true` |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  Default: `"api.meraki.com"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  Default: `60` |
| **net_id**  string | ID number of a network. |
| **net_name**  aliases: name, network  string | Name of a network. |
| **org_id**  string | ID of organization. |
| **org_name**  aliases: organization  string | Name of organization. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  Choices:   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  Choices:   - `"debug"` - `"normal"` ← (default) |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  Default: `165` |
| **state**  string | Create or modify an alert.  Choices:   - `"present"` ← (default) - `"query"` |
| **timeout**  integer | Time to timeout for HTTP requests.  Default: `30` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  Choices:   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](meraki_alert_module.md#id3)

> **Note:**
>
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_alert_module.md#id4)

```yaml+jinja
- name: Update settings
  meraki_alert:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    state: present
    default_destinations:
      emails:
      - 'youremail@yourcorp'
      - 'youremail2@yourcorp'
      all_admins: yes
      snmp: no
    alerts:
      - alert_type: "gatewayDown"
        enabled: yes
        filters:
          timeout: 60
        alert_destinations:
          emails:
          - 'youremail@yourcorp'
          - 'youremail2@yourcorp'
          all_admins: yes
          snmp: no
      - alert_type: "usageAlert"
        enabled: yes
        filters:
          period: 1200
          threshold: 104857600
        alert_destinations:
          emails:
          - 'youremail@yourcorp'
          - 'youremail2@yourcorp'
          all_admins: yes
          snmp: no

- name: Query all settings
  meraki_alert:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    state: query
  delegate_to: localhost
```

## [Return Values](meraki_alert_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | Information about the created or manipulated object.  Returned: info |
| **alerts**  complex | Alert-specific configuration for each type.  Returned: success |
| **alert_destinations**  complex | A hash of destinations for this specific alert.  Returned: success |
| **all_admins**  boolean | If true, all network admins will receive emails.  Returned: success |
| **emails**  list / elements=string | A list of emails that will recieve the alert(s).  Returned: success |
| **http_server_ids**  list / elements=string | A list of HTTP server IDs to send a Webhook to.  Returned: success |
| **snmp**  boolean | If true, then an SNMP trap will be sent if there is an SNMP trap server configured for this network.  Returned: success |
| **alert_type**  string | The type of alert.  Returned: success |
| **enabled**  boolean | A boolean depicting if the alert is turned on or off.  Returned: success |
| **filters**  complex | A hash of specific configuration data for the alert. Only filters specific to the alert will be updated.  No validation checks occur against `filters`.  Returned: success |
| **default_destinations**  complex | Properties for destinations when alert specific destinations aren’t specified.  Returned: success |
| **all_admins**  boolean | If true, all network admins will receive emails.  Returned: success  Sample: `true` |
| **emails**  list / elements=string | A list of emails that will recieve the alert(s).  Returned: success |
| **http_server_ids**  list / elements=string | A list of HTTP server IDs to send a Webhook to.  Returned: success |
| **snmp**  boolean | If true, then an SNMP trap will be sent if there is an SNMP trap server configured for this network.  Returned: success  Sample: `true` |

### Authors

- Kevin Breit (@kbreit)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-meraki/issues)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-meraki)
