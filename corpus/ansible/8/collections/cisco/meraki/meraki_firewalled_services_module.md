---
collection: ansible
version: "8"
title: "cisco.meraki.meraki_firewalled_services module – Edit firewall policies for administrative network services"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/meraki_firewalled_services_module.html
fetched_at: 2026-07-28T01:32:22+00:00
---
# cisco.meraki.meraki_firewalled_services module – Edit firewall policies for administrative network services

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
> To use it in a playbook, specify: `cisco.meraki.meraki_firewalled_services`.

- [DEPRECATED](meraki_firewalled_services_module.md#deprecated)
- [Synopsis](meraki_firewalled_services_module.md#synopsis)
- [Parameters](meraki_firewalled_services_module.md#parameters)
- [Notes](meraki_firewalled_services_module.md#notes)
- [Examples](meraki_firewalled_services_module.md#examples)
- [Return Values](meraki_firewalled_services_module.md#return-values)
- [Status](meraki_firewalled_services_module.md#status)

## [DEPRECATED](meraki_firewalled_services_module.md#id1)

Removed in:
:   version 3.0.0

Why:
:   Updated modules released with increased functionality

Alternative:
:   cisco.meraki.networks_appliance_firewall_firewalled_services

## [Synopsis](meraki_firewalled_services_module.md#id2)

- Allows for setting policy firewalled services for Meraki network devices.

## [Parameters](meraki_firewalled_services_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access**  string | Network service to query or modify.  **Choices:**   - `"blocked"` - `"restricted"` - `"unrestricted"` |
| **allowed_ips**  list / elements=string | List of IP addresses allowed to access a service.  Only used when `access` is set to restricted. |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable MERAKI_KEY is not set. |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  **Default:** `"api.meraki.com"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  **Default:** `60` |
| **net_id**  string | ID number of a network. |
| **net_name**  aliases: network  string | Name of a network. |
| **org_id**  string | ID of organization associated to a network. |
| **org_name**  aliases: organization  string | Name of organization associated to a network. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  **Choices:**   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  **Choices:**   - `"debug"` - `"normal"` ← (default) |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  **Default:** `165` |
| **service**  string | Network service to query or modify.  **Choices:**   - `"ICMP"` - `"SNMP"` - `"web"` |
| **state**  string | States that a policy should be created or modified.  **Choices:**   - `"present"` ← (default) - `"query"` |
| **timeout**  integer | Time to timeout for HTTP requests.  **Default:** `30` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  **Choices:**   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](meraki_firewalled_services_module.md#id4)

> **Note:**
>
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_firewalled_services_module.md#id5)

```yaml+jinja
- name: Set icmp service to blocked
  meraki_firewalled_services:
    auth_key: '{{ auth_key }}'
    state: present
    org_name: '{{test_org_name}}'
    net_name: IntTestNetworkAppliance
    service: ICMP
    access: blocked
  delegate_to: localhost

- name: Set icmp service to restricted
  meraki_firewalled_services:
    auth_key: abc123
    state: present
    org_name: YourOrg
    net_name: YourNet
    service: web
    access: restricted
    allowed_ips:
      - 192.0.1.1
      - 192.0.1.2
  delegate_to: localhost

- name: Query appliance services
  meraki_firewalled_services:
    auth_key: abc123
    state: query
    org_name: YourOrg
    net_name: YourNet
  delegate_to: localhost

- name: Query services
  meraki_firewalled_services:
    auth_key: abc123
    state: query
    org_name: YourOrg
    net_name: YourNet
    service: ICMP
  delegate_to: localhost
```

## [Return Values](meraki_firewalled_services_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | List of network services.  **Returned:** info |
| **access**  string | Access assigned to a service type.  **Returned:** success  **Sample:** `"unrestricted"` |
| **allowed_ips**  string | List of IP addresses to have access to service.  **Returned:** success  **Sample:** `"192.0.1.0"` |
| **service**  string | Service to apply policy to.  **Returned:** success  **Sample:** `"ICMP"` |

## [Status](meraki_firewalled_services_module.md#id7)

- This module will be removed in version 3.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](meraki_firewalled_services_module.md#deprecated).

### Authors

- Kevin Breit (@kbreit)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
