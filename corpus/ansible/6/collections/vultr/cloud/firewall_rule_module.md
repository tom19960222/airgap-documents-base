---
collection: ansible
version: "6"
title: "vultr.cloud.firewall_rule module – Manages firewall rules on Vultr"
source_url: https://docs.ansible.com/projects/ansible/6/collections/vultr/cloud/firewall_rule_module.html
fetched_at: 2026-07-28T00:23:01+00:00
---
# vultr.cloud.firewall_rule module – Manages firewall rules on Vultr

> **Note:**
>
> This module is part of the [vultr.cloud collection](https://galaxy.ansible.com/vultr/cloud) (version 1.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vultr.cloud`.
>
> To use it in a playbook, specify: `vultr.cloud.firewall_rule`.

New in vultr.cloud 1.0.0

- [Synopsis](firewall_rule_module.md#synopsis)
- [Parameters](firewall_rule_module.md#parameters)
- [Notes](firewall_rule_module.md#notes)
- [Examples](firewall_rule_module.md#examples)
- [Return Values](firewall_rule_module.md#return-values)

## [Synopsis](firewall_rule_module.md#id1)

- Create and remove firewall rules.

## [Parameters](firewall_rule_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_endpoint**  string | URL to API endpint (without trailing slash).  Fallback environment variable `VULTR_API_ENDPOINT`.  Default: `"https://api.vultr.com/v2"` |
| **api_key**  string / required | API key of the Vultr API.  Fallback environment variable `VULTR_API_KEY`. |
| **api_retries**  integer | Amount of retries in case of the Vultr API retuns an HTTP 503 code.  Fallback environment variable `VULTR_API_RETRIES`.  Default: `5` |
| **api_retry_max_delay**  integer | Retry backoff delay in seconds is exponential up to this max. value, in seconds.  Fallback environment variable `VULTR_API_RETRY_MAX_DELAY`.  Default: `12` |
| **api_timeout**  integer | HTTP timeout to Vultr API.  Fallback environment variable `VULTR_API_TIMEOUT`.  Default: `60` |
| **group**  string / required | Name of the firewall group. |
| **ip_type**  string | IP address version  Choices:   - `"v4"` ← (default) - `"v6"` |
| **notes**  string | Notes of the firewall rule. |
| **port**  aliases: port_range  string | Single port or port range, e.g. `80` or `8000:8080`.  Required if *protocol* is tcp or udp and *state=present*. |
| **protocol**  string | Protocol of the firewall rule.  Choices:   - `"icmp"` - `"tcp"` ← (default) - `"udp"` - `"gre"` - `"esp"` - `"ah"` |
| **source**  string | Possible values are `cloudflare` or a loadbalancer label.  Mutally exclusive with *subnet*. |
| **state**  string | State of the firewall rule.  Choices:   - `"present"` ← (default) - `"absent"` |
| **subnet**  string | The network or IP, e.g. 192.0.2.123 or 0.0.0.0.  Mutally exclusive with *source*. |
| **subnet_size**  integer | The number of bits for the netmask in CIDR notation, e.g. `32`. |
| **validate_certs**  boolean | Validate SSL certs of the Vultr API.  Choices:   - `false` - `true` ← (default) |

## [Notes](firewall_rule_module.md#id3)

> **Note:**
>
> - Also see the API documentation on <https://www.vultr.com/api/>.

## [Examples](firewall_rule_module.md#id4)

```yaml+jinja
- name: Ensure a firewall rule is present
  vultr.cloud.firewall_rule:
    group: web
    port: 80
    protocol: tcp
    ip_type: v4
    subnet: "0.0.0.0"
    subnet_size: 0
    notes: "open HTTP to the world"

- name: Ensure a firewall rule with port range is present
  vultr.cloud.firewall_rule:
    group: apps
    port: "8000:8999"
    protocol: tcp
    ip_type: v4
    subnet: "10.10.10.0"
    subnet_size: 24

- name: Ensure a firewall rule is absent
  vultr.cloud.firewall_rule:
    group: apps
    port: "443"
    protocol: tcp
    ip_type: v6
    subnet: "::"
    subnet_size: 0
    state: absent
```

## [Return Values](firewall_rule_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vultr_api**  dictionary | Response from Vultr API with a few additions/modification.  Returned: success |
| **api_endpoint**  string | Endpoint used for the API requests.  Returned: success  Sample: `"https://api.vultr.com/v2"` |
| **api_retries**  integer | Amount of max retries for the API requests.  Returned: success  Sample: `5` |
| **api_retry_max_delay**  integer | Exponential backoff delay in seconds between retries up to this max delay value.  Returned: success  Sample: `12` |
| **api_timeout**  integer | Timeout used for the API requests.  Returned: success  Sample: `60` |
| **vultr_firewall_rule**  dictionary | Response from Vultr API.  Returned: success |
| **action**  string | Action of the firewall rule.  Returned: success  Sample: `"accept"` |
| **id**  integer | ID of the firewall rule.  Returned: success  Sample: `1` |
| **ip_type**  string | IP type of the firewall rule.  Returned: success  Sample: `"v4"` |
| **notes**  string | Supplied description of the firewall rule.  Returned: success  Sample: `"my rule"` |
| **port**  string | Port or port range of the firewall rule.  Returned: success  Sample: `"80"` |
| **protocol**  string | Protocol of the firewall rule.  Returned: success  Sample: `"tcp"` |
| **source**  string | Source string of the firewall rule.  Returned: success  Sample: `"cloudflare"` |
| **subnet**  string | Subnet of the firewall rule.  Returned: success  Sample: `"0.0.0.0"` |
| **subnet_size**  integer | Size of the subnet of the firewall rule.  Returned: success  Sample: `0` |

### Authors

- René Moser (@resmo)

### Collection links

[Issue Tracker](https://github.com/vultr/ansible-collection-vultr/issues)
[Repository (Sources)](https://github.com/vultr/ansible-collection-vultr)
