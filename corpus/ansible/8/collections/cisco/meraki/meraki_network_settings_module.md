---
collection: ansible
version: "8"
title: "cisco.meraki.meraki_network_settings module – Manage the settings of networks in the Meraki cloud"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/meraki_network_settings_module.html
fetched_at: 2026-07-28T01:32:46+00:00
---
# cisco.meraki.meraki_network_settings module – Manage the settings of networks in the Meraki cloud

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
> To use it in a playbook, specify: `cisco.meraki.meraki_network_settings`.

- [DEPRECATED](meraki_network_settings_module.md#deprecated)
- [Synopsis](meraki_network_settings_module.md#synopsis)
- [Parameters](meraki_network_settings_module.md#parameters)
- [Notes](meraki_network_settings_module.md#notes)
- [Examples](meraki_network_settings_module.md#examples)
- [Return Values](meraki_network_settings_module.md#return-values)
- [Status](meraki_network_settings_module.md#status)

## [DEPRECATED](meraki_network_settings_module.md#id1)

Removed in:
:   version 3.0.0

Why:
:   Updated modules released with increased functionality

Alternative:
:   cisco.meraki.networks_settings

## [Synopsis](meraki_network_settings_module.md#id2)

- Allows for management of settings of networks within Meraki.

## [Parameters](meraki_network_settings_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  **Default:** `"api.meraki.com"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  **Default:** `60` |
| **local_status_page**  dictionary | Configuration stanza of the local status page. |
| **authentication**  dictionary | Local status page authentication settings. |
| **enabled**  boolean | Set whether local status page authentication is enabled.  **Choices:**   - `false` - `true` |
| **password**  string | Set password on local status page. |
| **local_status_page_enabled**  boolean | - Enables the local device status pages (U[my.meraki.com](my.meraki.com), U[ap.meraki.com](ap.meraki.com), U[switch.meraki.com](switch.meraki.com), U[wired.meraki.com](wired.meraki.com)). - Only can be specified on its own or with `remote_status_page_enabled`.   **Choices:**   - `false` - `true` |
| **net_id**  string | ID number of a network. |
| **net_name**  aliases: name, network  string | Name of a network. |
| **org_id**  string | ID of organization. |
| **org_name**  aliases: organization  string | Name of organization. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  **Choices:**   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  **Choices:**   - `"debug"` - `"normal"` ← (default) |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  **Default:** `165` |
| **remote_status_page_enabled**  boolean | Enables access to the device status page (<http://device%20LAN%20IP>).  Can only be set if `local_status_page_enabled:` is set to `yes`.  Only can be specified on its own or with `local_status_page_enabled`.  **Choices:**   - `false` - `true` |
| **secure_port**  dictionary | Configuration of SecureConnect options applied to the network. |
| **enabled**  boolean | Set whether SecureConnect is enabled on the network.  **Choices:**   - `false` - `true` |
| **state**  string | Create or modify an organization.  **Choices:**   - `"present"` - `"query"` ← (default) |
| **timeout**  integer | Time to timeout for HTTP requests.  **Default:** `30` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  **Choices:**   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](meraki_network_settings_module.md#id4)

> **Note:**
>
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_network_settings_module.md#id5)

```yaml+jinja
- name: Get network settings
  cisco.meraki.meraki_network_settings:
    auth_key: '{{ auth_key }}'
    state: query
    org_name: '{{test_org_name}}'
    net_name: NetworkSettingsTestNet
  delegate_to: localhost

- name: Update network settings
  cisco.meraki.meraki_network_settings:
    auth_key: '{{ auth_key }}'
    state: present
    org_name: '{{test_org_name}}'
    net_name: NetworkSettingsTestNet
    local_status_page_enabled: false
  delegate_to: localhost

- name: Enable password on local page
  cisco.meraki.meraki_network_settings:
    auth_key: '{{ auth_key }}'
    state: present
    org_name: '{{test_org_name}}'
    net_name: NetworkSettingsTestNet
    local_status_page_enabled: true
    local_status_page:
      authentication:
        enabled: true
        password: abc123
  delegate_to: localhost
```

## [Return Values](meraki_network_settings_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | Information about the created or manipulated object.  **Returned:** info |
| **expire_data_older_than**  integer | The number of days, weeks, or months in Epoch time to expire the data before  **Returned:** success  **Sample:** `1234` |
| **fips**  complex | A hash of FIPS options applied to the Network.  **Returned:** success |
| **enabled**  boolean | Enables/disables FIPS on the network.  **Returned:** success  **Sample:** `true` |
| **local_status_page**  complex | A hash of Local Status Page(s) authentication options applied to the Network.  **Returned:** success |
| **authentication**  complex | A hash of Local Status Pages’ authentication options applied to the Network.  **Returned:** success  **Sample:** `true` |
| **enabled**  boolean | Enables/Disables the authenticaiton on Local Status Pages.  **Returned:** success |
| **username**  string | The username used for Local Status Pages.  **Returned:** success  **Sample:** `"admin"` |
| **local_status_page_enabled**  boolean | States whether my.meraki.com and other device portals should be enabled.  **Returned:** success  **Sample:** `true` |
| **named_vlans**  complex | A hash of Named VLANs options applied to the Network.  **Returned:** success |
| **enabled**  boolean | Enables/disables Named VLANs on the network.  **Returned:** success  **Sample:** `true` |
| **remote_status_page_enabled**  boolean | Enables access to the device status page.  **Returned:** success  **Sample:** `true` |
| **secure_port**  complex | A hash of SecureConnect options applied to the Network.  **Returned:** success |
| **enabled**  boolean | Enables/disables SecureConnect on the network.  **Returned:** success  **Sample:** `true` |

## [Status](meraki_network_settings_module.md#id7)

- This module will be removed in version 3.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](meraki_network_settings_module.md#deprecated).

### Authors

- Kevin Breit (@kbreit)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
