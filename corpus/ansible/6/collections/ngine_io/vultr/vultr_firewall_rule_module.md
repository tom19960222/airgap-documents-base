---
collection: ansible
version: "6"
title: "ngine_io.vultr.vultr_firewall_rule module – Manages firewall rules on Vultr."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ngine_io/vultr/vultr_firewall_rule_module.html
fetched_at: 2026-07-28T00:16:06+00:00
---
# ngine_io.vultr.vultr_firewall_rule module – Manages firewall rules on Vultr.

> **Note:**
>
> This module is part of the [ngine_io.vultr collection](https://galaxy.ansible.com/ngine_io/vultr) (version 1.1.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ngine_io.vultr`.
> You need further requirements to be able to use this module,
> see [Requirements](vultr_firewall_rule_module.md#ansible-collections-ngine-io-vultr-vultr-firewall-rule-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.vultr.vultr_firewall_rule`.

New in ngine_io.vultr 0.1.0

- [Synopsis](vultr_firewall_rule_module.md#synopsis)
- [Requirements](vultr_firewall_rule_module.md#requirements)
- [Parameters](vultr_firewall_rule_module.md#parameters)
- [Notes](vultr_firewall_rule_module.md#notes)
- [Examples](vultr_firewall_rule_module.md#examples)
- [Return Values](vultr_firewall_rule_module.md#return-values)

## [Synopsis](vultr_firewall_rule_module.md#id1)

- Create and remove firewall rules.

## [Requirements](vultr_firewall_rule_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](vultr_firewall_rule_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_account**  string | Name of the ini section in the `vultr.ini` file.  The ENV variable `VULTR_API_ACCOUNT` is used as default, when defined.  Default: `"default"` |
| **api_endpoint**  string | URL to API endpint (without trailing slash).  The ENV variable `VULTR_API_ENDPOINT` is used as default, when defined.  Fallback value is <https://api.vultr.com> if not specified. |
| **api_key**  string | API key of the Vultr API.  The ENV variable `VULTR_API_KEY` is used as default, when defined. |
| **api_retries**  integer | Amount of retries in case of the Vultr API retuns an HTTP 503 code.  The ENV variable `VULTR_API_RETRIES` is used as default, when defined.  Fallback value is 5 retries if not specified. |
| **api_retry_max_delay**  integer | Retry backoff delay in seconds is exponential up to this max. value, in seconds.  The ENV variable `VULTR_API_RETRY_MAX_DELAY` is used as default, when defined.  Fallback value is 12 seconds. |
| **api_timeout**  integer | HTTP timeout to Vultr API.  The ENV variable `VULTR_API_TIMEOUT` is used as default, when defined.  Fallback value is 60 seconds if not specified. |
| **cidr**  string | Network in CIDR format  The CIDR format must match with the `ip_version` value.  Required if `state=present`.  Defaulted to 0.0.0.0/0 or ::/0 depending on `ip_version`. |
| **end_port**  integer | End port for the firewall rule.  Only considered if `protocol` is tcp or udp and *state=present*. |
| **group**  string / required | Name of the firewall group. |
| **ip_version**  aliases: ip_type  string | IP address version  Choices:   - `"v4"` ← (default) - `"v6"` |
| **protocol**  string | Protocol of the firewall rule.  Choices:   - `"icmp"` - `"tcp"` ← (default) - `"udp"` - `"gre"` |
| **start_port**  aliases: port  integer | Start port for the firewall rule.  Required if `protocol` is tcp or udp and *state=present*. |
| **state**  string | State of the firewall rule.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | Validate SSL certs of the Vultr API.  Choices:   - `false` - `true` ← (default) |

## [Notes](vultr_firewall_rule_module.md#id4)

> **Note:**
>
> - Also see the API documentation on <https://www.vultr.com/api/>.

## [Examples](vultr_firewall_rule_module.md#id5)

```yaml+jinja
- name: ensure a firewall rule is present
  ngine_io.vultr.vultr_firewall_rule:
    group: application
    protocol: tcp
    start_port: 8000
    end_port: 9000
    cidr: 17.17.17.0/24

- name: open DNS port for all ipv4 and ipv6
  ngine_io.vultr.vultr_firewall_rule:
    group: dns
    protocol: udp
    port: 53
    ip_version: "{{ item }}"
  with_items: [ v4, v6 ]

- name: allow ping
  ngine_io.vultr.vultr_firewall_rule:
    group: web
    protocol: icmp

- name: ensure a firewall rule is absent
  ngine_io.vultr.vultr_firewall_rule:
    group: application
    protocol: tcp
    start_port: 8000
    end_port: 9000
    cidr: 17.17.17.0/24
    state: absent
```

## [Return Values](vultr_firewall_rule_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vultr_api**  complex | Response from Vultr API with a few additions/modification  Returned: success |
| **api_account**  string | Account used in the ini file to select the key  Returned: success  Sample: `"default"` |
| **api_endpoint**  string | Endpoint used for the API requests  Returned: success  Sample: `"https://api.vultr.com"` |
| **api_retries**  integer | Amount of max retries for the API requests  Returned: success  Sample: `5` |
| **api_retry_max_delay**  integer | Exponential backoff delay in seconds between retries up to this max delay value.  Returned: success  Sample: `12` |
| **api_timeout**  integer | Timeout used for the API requests  Returned: success  Sample: `60` |
| **vultr_firewall_rule**  complex | Response from Vultr API  Returned: success |
| **action**  string | Action of the firewall rule  Returned: success  Sample: `"accept"` |
| **cidr**  string | CIDR of the firewall rule (IPv4 or IPv6)  Returned: success and when port range  Sample: `"0.0.0.0/0"` |
| **end_port**  integer | End port of the firewall rule  Returned: success and when port range and protocol is tcp or udp  Sample: `8080` |
| **group**  string | Firewall group the rule is into.  Returned: success  Sample: `"web"` |
| **protocol**  string | Protocol of the firewall rule  Returned: success  Sample: `"tcp"` |
| **rule_number**  integer | Rule number of the firewall rule  Returned: success  Sample: `2` |
| **start_port**  integer | Start port of the firewall rule  Returned: success and protocol is tcp or udp  Sample: `80` |

### Authors

- René Moser (@resmo)

### Collection links

[Issue Tracker](https://github.com/ngine-io/ansible-collection-vultr/issues)
[Repository (Sources)](https://github.com/ngine-io/ansible-collection-vultr)
