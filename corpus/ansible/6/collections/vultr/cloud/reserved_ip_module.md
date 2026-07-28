---
collection: ansible
version: "6"
title: "vultr.cloud.reserved_ip module – Manages reserved IPs on Vultr"
source_url: https://docs.ansible.com/projects/ansible/6/collections/vultr/cloud/reserved_ip_module.html
fetched_at: 2026-07-28T00:23:06+00:00
---
# vultr.cloud.reserved_ip module – Manages reserved IPs on Vultr

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
> To use it in a playbook, specify: `vultr.cloud.reserved_ip`.

New in vultr.cloud 1.0.0

- [Synopsis](reserved_ip_module.md#synopsis)
- [Parameters](reserved_ip_module.md#parameters)
- [Notes](reserved_ip_module.md#notes)
- [Examples](reserved_ip_module.md#examples)
- [Return Values](reserved_ip_module.md#return-values)

## [Synopsis](reserved_ip_module.md#id1)

- Create, attach, detach and remove reserved IPs.

## [Parameters](reserved_ip_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_endpoint**  string | URL to API endpint (without trailing slash).  Fallback environment variable `VULTR_API_ENDPOINT`.  Default: `"https://api.vultr.com/v2"` |
| **api_key**  string / required | API key of the Vultr API.  Fallback environment variable `VULTR_API_KEY`. |
| **api_retries**  integer | Amount of retries in case of the Vultr API retuns an HTTP 503 code.  Fallback environment variable `VULTR_API_RETRIES`.  Default: `5` |
| **api_retry_max_delay**  integer | Retry backoff delay in seconds is exponential up to this max. value, in seconds.  Fallback environment variable `VULTR_API_RETRY_MAX_DELAY`.  Default: `12` |
| **api_timeout**  integer | HTTP timeout to Vultr API.  Fallback environment variable `VULTR_API_TIMEOUT`.  Default: `60` |
| **instance_id**  string | ID of the Instance the reserved IP should be attached to.  Mutually exclusive with *instance_name*. |
| **instance_name**  string | Name of the Instance the reserved IP should be attached to.  Mutually exclusive with *instance_id*. |
| **ip_type**  string / required | Type of the IP.  Choices:   - `"v4"` - `"v6"` |
| **label**  aliases: name  string / required | Label of the reserved IP. |
| **region**  string / required | Region of the reserved IP will be related to. |
| **state**  string | State of the reserved IP.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | Validate SSL certs of the Vultr API.  Choices:   - `false` - `true` ← (default) |

## [Notes](reserved_ip_module.md#id3)

> **Note:**
>
> - Also see the API documentation on <https://www.vultr.com/api/>.

## [Examples](reserved_ip_module.md#id4)

```yaml+jinja
- name: Ensure a reserved IP present and attached to an instance
  vultr.cloud.reserved_ip:
    label: my attached IP
    region: ewr
    ip_type: v4
    instance_name: web-01

- name: Ensure a reserved IP is detached
  vultr.cloud.reserved_ip:
    label: my reserved IP
    region: ewr
    ip_type: v4
    instance_id: ""

- name: Ensure a reserved IP is absent
  vultr.cloud.reserved_ip:
    label: my attached IP
    region: ewr
    ip_type: v4
    state: absent
```

## [Return Values](reserved_ip_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vultr_api**  dictionary | Response from Vultr API with a few additions/modification.  Returned: success |
| **api_endpoint**  string | Endpoint used for the API requests.  Returned: success  Sample: `"https://api.vultr.com/v2"` |
| **api_retries**  integer | Amount of max retries for the API requests.  Returned: success  Sample: `5` |
| **api_retry_max_delay**  integer | Exponential backoff delay in seconds between retries up to this max delay value.  Returned: success  Sample: `12` |
| **api_timeout**  integer | Timeout used for the API requests.  Returned: success  Sample: `60` |
| **vultr_reserved_ip**  dictionary | Response from Vultr API.  Returned: success |
| **id**  string | ID of the reserved IP.  Returned: success  Sample: `"cb676a46-66fd-4dfb-b839-443f2e6c0b60"` |
| **instance_id**  string | ID of the Instance the reserved IP is attached to.  Returned: success  Sample: `"cb676a46-66fd-4dfb-b839-443f2e6c0b"` |
| **ip_type**  string | Type of the reserved IP.  Returned: success  Sample: `"v4"` |
| **label**  string | Name of the reserved IP.  Returned: success  Sample: `"example.com"` |
| **region**  string | Region of the reserved IP is related to.  Returned: success  Sample: `"ewr"` |
| **subnet**  string | Subnet of the reserved IP.  Returned: success  Sample: `"v4"` |
| **subnet_size**  integer | Size of the subnet of the reserved IP.  Returned: success  Sample: `32` |

### Authors

- René Moser (@resmo)

### Collection links

[Issue Tracker](https://github.com/vultr/ansible-collection-vultr/issues)
[Repository (Sources)](https://github.com/vultr/ansible-collection-vultr)
