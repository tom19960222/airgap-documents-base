---
collection: ansible
version: "6"
title: "vultr.cloud.firewall_group module – Manages firewall groups on Vultr"
source_url: https://docs.ansible.com/projects/ansible/6/collections/vultr/cloud/firewall_group_module.html
fetched_at: 2026-07-28T00:22:59+00:00
---
# vultr.cloud.firewall_group module – Manages firewall groups on Vultr

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
> To use it in a playbook, specify: `vultr.cloud.firewall_group`.

New in vultr.cloud 1.0.0

- [Synopsis](firewall_group_module.md#synopsis)
- [Parameters](firewall_group_module.md#parameters)
- [Notes](firewall_group_module.md#notes)
- [Examples](firewall_group_module.md#examples)
- [Return Values](firewall_group_module.md#return-values)

## [Synopsis](firewall_group_module.md#id1)

- Create and remove firewall groups.

## [Parameters](firewall_group_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_endpoint**  string | URL to API endpint (without trailing slash).  Fallback environment variable `VULTR_API_ENDPOINT`.  Default: `"https://api.vultr.com/v2"` |
| **api_key**  string / required | API key of the Vultr API.  Fallback environment variable `VULTR_API_KEY`. |
| **api_retries**  integer | Amount of retries in case of the Vultr API retuns an HTTP 503 code.  Fallback environment variable `VULTR_API_RETRIES`.  Default: `5` |
| **api_retry_max_delay**  integer | Retry backoff delay in seconds is exponential up to this max. value, in seconds.  Fallback environment variable `VULTR_API_RETRY_MAX_DELAY`.  Default: `12` |
| **api_timeout**  integer | HTTP timeout to Vultr API.  Fallback environment variable `VULTR_API_TIMEOUT`.  Default: `60` |
| **description**  aliases: name  string / required | Description of the firewall group. |
| **state**  string | State of the firewall group.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | Validate SSL certs of the Vultr API.  Choices:   - `false` - `true` ← (default) |

## [Notes](firewall_group_module.md#id3)

> **Note:**
>
> - Also see the API documentation on <https://www.vultr.com/api/>.

## [Examples](firewall_group_module.md#id4)

```yaml+jinja
- name: ensure a firewall group is present
  vultr.cloud.firewall_group:
    description: my http firewall.

- name: ensure a firewall group is absent
  vultr.cloud.firewall_group:
    description: my http firewall.
    state: absent
```

## [Return Values](firewall_group_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vultr_api**  dictionary | Response from Vultr API with a few additions/modification.  Returned: success |
| **api_endpoint**  string | Endpoint used for the API requests.  Returned: success  Sample: `"https://api.vultr.com/v2"` |
| **api_retries**  integer | Amount of max retries for the API requests.  Returned: success  Sample: `5` |
| **api_retry_max_delay**  integer | Exponential backoff delay in seconds between retries up to this max delay value.  Returned: success  Sample: `12` |
| **api_timeout**  integer | Timeout used for the API requests.  Returned: success  Sample: `60` |
| **vultr_firewall_group**  dictionary | Response from Vultr API.  Returned: success |
| **date_created**  string | Date the firewall group was created.  Returned: success  Sample: `"2020-10-10T01:56:20+00:00"` |
| **date_modified**  string | Date the firewall group was modified.  Returned: success  Sample: `"2020-10-10T01:56:20+00:00"` |
| **description**  string | Description (name) of the firewall group  Returned: success  Sample: `"my firewall group"` |
| **id**  string | ID of the firewall group.  Returned: success  Sample: `"cb676a46-66fd-4dfb-b839-443f2e6c0b60"` |

### Authors

- René Moser (@resmo)

### Collection links

[Issue Tracker](https://github.com/vultr/ansible-collection-vultr/issues)
[Repository (Sources)](https://github.com/vultr/ansible-collection-vultr)
