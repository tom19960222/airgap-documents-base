---
collection: ansible
version: "6"
title: "cisco.meraki.meraki_mx_l7_firewall module – Manage MX appliance layer 7 firewalls in the Meraki cloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/meraki/meraki_mx_l7_firewall_module.html
fetched_at: 2026-07-27T17:00:34+00:00
---
# cisco.meraki.meraki_mx_l7_firewall module – Manage MX appliance layer 7 firewalls in the Meraki cloud

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
> To use it in a playbook, specify: `cisco.meraki.meraki_mx_l7_firewall`.

- [Synopsis](meraki_mx_l7_firewall_module.md#synopsis)
- [Parameters](meraki_mx_l7_firewall_module.md#parameters)
- [Notes](meraki_mx_l7_firewall_module.md#notes)
- [Examples](meraki_mx_l7_firewall_module.md#examples)
- [Return Values](meraki_mx_l7_firewall_module.md#return-values)

## [Synopsis](meraki_mx_l7_firewall_module.md#id1)

- Allows for creation, management, and visibility into layer 7 firewalls implemented on Meraki MX firewalls.

## [Parameters](meraki_mx_l7_firewall_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **categories**  boolean | When `True`, specifies that applications and application categories should be queried instead of firewall rules.  Choices:   - `false` - `true` |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  Default: `"api.meraki.com"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  Default: `60` |
| **net_id**  string | ID of network which MX firewall is in. |
| **net_name**  string | Name of network which MX firewall is in. |
| **org_id**  string | ID of organization. |
| **org_name**  aliases: organization  string | Name of organization. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  Choices:   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  Choices:   - `"debug"` - `"normal"` ← (default) |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  Default: `165` |
| **rules**  list / elements=dictionary | List of layer 7 firewall rules. |
| **application**  dictionary | Application to filter. |
| **id**  string | URI of application as defined by Meraki. |
| **name**  string | Name of application to filter as defined by Meraki. |
| **countries**  list / elements=string | List of countries to whitelist or blacklist.  The countries follow the two-letter ISO 3166-1 alpha-2 format. |
| **host**  string | FQDN of host to filter. |
| **ip_range**  string | CIDR notation range of IP addresses to apply rule to.  Port can be appended to range with a `":"`. |
| **policy**  string | Policy to apply if rule is hit.  Choices:   - `"deny"` ← (default) |
| **port**  string | TCP or UDP based port to filter. |
| **type**  string | Type of policy to apply.  Choices:   - `"application"` - `"application_category"` - `"blocked_countries"` - `"host"` - `"ip_range"` - `"port"` - `"allowed_countries"` |
| **state**  string | Query or modify a firewall rule.  Choices:   - `"present"` ← (default) - `"query"` |
| **timeout**  integer | Time to timeout for HTTP requests.  Default: `30` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  Choices:   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](meraki_mx_l7_firewall_module.md#id3)

> **Note:**
>
> - Module assumes a complete list of firewall rules are passed as a parameter.
> - If there is interest in this module allowing manipulation of a single firewall rule, please submit an issue against this module.
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_mx_l7_firewall_module.md#id4)

```yaml+jinja
- name: Query firewall rules
  meraki_mx_l7_firewall:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    state: query
  delegate_to: localhost

- name: Query applications and application categories
  meraki_mx_l7_firewall:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    categories: yes
    state: query
  delegate_to: localhost

- name: Set firewall rules
  meraki_mx_l7_firewall:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    state: present
    rules:
      - type: allowed_countries
        countries:
          - US
          - FR
      - type: blocked_countries
        countries:
          - CN
      - policy: deny
        type: port
        port: 8080
      - type: port
        port: 1234
      - type: host
        host: asdf.com
      - type: application
        application:
          id: meraki:layer7/application/205
      - type: application_category
        application:
          id: meraki:layer7/category/24
  delegate_to: localhost
```

## [Return Values](meraki_mx_l7_firewall_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | Firewall rules associated to network.  Returned: success |
| **application_categories**  list / elements=string | List of application categories and applications.  Returned: success, when querying applications |
| **applications**  list / elements=string | List of applications within a category.  Returned: success |
| **id**  string | URI of application.  Returned: success  Sample: `"Gmail"` |
| **name**  string | Descriptive name of application.  Returned: success  Sample: `"meraki:layer7/application/4"` |
| **id**  string | URI of application category.  Returned: success  Sample: `"Email"` |
| **name**  string | Descriptive name of application category.  Returned: success  Sample: `"layer7/category/1"` |
| **rules**  list / elements=string | Ordered list of firewall rules.  Returned: success, when not querying applications |
| **allowedCountries**  string | Countries to be allowed.  Returned: success  Sample: `"CA"` |
| **applicationCategory**  list / elements=string | List of application categories within a category.  Returned: success |
| **id**  string | URI of application.  Returned: success  Sample: `"Gmail"` |
| **name**  string | Descriptive name of application.  Returned: success  Sample: `"meraki:layer7/application/4"` |
| **applications**  list / elements=string | List of applications within a category.  Returned: success |
| **id**  string | URI of application.  Returned: success  Sample: `"Gmail"` |
| **name**  string | Descriptive name of application.  Returned: success  Sample: `"meraki:layer7/application/4"` |
| **blockedCountries**  string | Countries to be blacklisted.  Returned: success  Sample: `"RU"` |
| **ipRange**  string | Range of IP addresses in rule.  Returned: success  Sample: `"1.1.1.0/23"` |
| **policy**  string | Action to apply when rule is hit.  Returned: success  Sample: `"deny"` |
| **port**  string | Port number in rule.  Returned: success  Sample: `"23"` |
| **type**  string | Type of rule category.  Returned: success  Sample: `"applications"` |

### Authors

- Kevin Breit (@kbreit)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-meraki/issues)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-meraki)
