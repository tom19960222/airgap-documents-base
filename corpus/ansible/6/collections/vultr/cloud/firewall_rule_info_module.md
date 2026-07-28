---
collection: ansible
version: "6"
title: "vultr.cloud.firewall_rule_info module – Gather information about the Vultr firewall rules"
source_url: https://docs.ansible.com/projects/ansible/6/collections/vultr/cloud/firewall_rule_info_module.html
fetched_at: 2026-07-28T00:23:01+00:00
---
# vultr.cloud.firewall_rule_info module – Gather information about the Vultr firewall rules

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
> To use it in a playbook, specify: `vultr.cloud.firewall_rule_info`.

New in vultr.cloud 1.0.0

- [Synopsis](firewall_rule_info_module.md#synopsis)
- [Parameters](firewall_rule_info_module.md#parameters)
- [Notes](firewall_rule_info_module.md#notes)
- [Examples](firewall_rule_info_module.md#examples)
- [Return Values](firewall_rule_info_module.md#return-values)

## [Synopsis](firewall_rule_info_module.md#id1)

- Gather information about firewall rules available.

## [Parameters](firewall_rule_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_endpoint**  string | URL to API endpint (without trailing slash).  Fallback environment variable `VULTR_API_ENDPOINT`.  Default: `"https://api.vultr.com/v2"` |
| **api_key**  string / required | API key of the Vultr API.  Fallback environment variable `VULTR_API_KEY`. |
| **api_retries**  integer | Amount of retries in case of the Vultr API retuns an HTTP 503 code.  Fallback environment variable `VULTR_API_RETRIES`.  Default: `5` |
| **api_retry_max_delay**  integer | Retry backoff delay in seconds is exponential up to this max. value, in seconds.  Fallback environment variable `VULTR_API_RETRY_MAX_DELAY`.  Default: `12` |
| **api_timeout**  integer | HTTP timeout to Vultr API.  Fallback environment variable `VULTR_API_TIMEOUT`.  Default: `60` |
| **group**  string / required | Name of the firewall group. |
| **validate_certs**  boolean | Validate SSL certs of the Vultr API.  Choices:   - `false` - `true` ← (default) |

## [Notes](firewall_rule_info_module.md#id3)

> **Note:**
>
> - Also see the API documentation on <https://www.vultr.com/api/>.

## [Examples](firewall_rule_info_module.md#id4)

```yaml+jinja
- name: Gather Vultr firewall rule information
  vultr.cloud.firewall_rule_info:
    group: my group
  register: result

- name: Print the gathered information
  ansible.builtin.debug:
    var: result.vultr_firewall_rule_info
```

## [Return Values](firewall_rule_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vultr_api**  dictionary | Response from Vultr API with a few additions/modification.  Returned: success |
| **api_endpoint**  string | Endpoint used for the API requests.  Returned: success  Sample: `"https://api.vultr.com/v2"` |
| **api_retries**  integer | Amount of max retries for the API requests.  Returned: success  Sample: `5` |
| **api_retry_max_delay**  integer | Exponential backoff delay in seconds between retries up to this max delay value.  Returned: success  Sample: `12` |
| **api_timeout**  integer | Timeout used for the API requests.  Returned: success  Sample: `60` |
| **vultr_firewall_rule_info**  list / elements=string | Response from Vultr API as list.  Returned: success |
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
