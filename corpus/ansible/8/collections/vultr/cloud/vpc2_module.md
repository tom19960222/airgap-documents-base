---
collection: ansible
version: "8"
title: "vultr.cloud.vpc2 module – Manages VPCs 2.0 on Vultr"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vultr/cloud/vpc2_module.html
fetched_at: 2026-07-28T02:59:05+00:00
---
# vultr.cloud.vpc2 module – Manages VPCs 2.0 on Vultr

> **Note:**
>
> This module is part of the [vultr.cloud collection](https://galaxy.ansible.com/ui/repo/published/vultr/cloud/) (version 1.11.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vultr.cloud`.
>
> To use it in a playbook, specify: `vultr.cloud.vpc2`.

New in vultr.cloud 1.9.0

- [Synopsis](vpc2_module.md#synopsis)
- [Parameters](vpc2_module.md#parameters)
- [Notes](vpc2_module.md#notes)
- [Examples](vpc2_module.md#examples)
- [Return Values](vpc2_module.md#return-values)

## [Synopsis](vpc2_module.md#id1)

- Create and remove VPCs 2.0.

## [Parameters](vpc2_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_endpoint**  string | URL to API endpint (without trailing slash).  Fallback environment variable `VULTR_API_ENDPOINT`.  **Default:** `"https://api.vultr.com/v2"` |
| **api_key**  string / required | API key of the Vultr API.  Fallback environment variable `VULTR_API_KEY`. |
| **api_retries**  integer | Amount of retries in case of the Vultr API retuns an HTTP 503 code.  Fallback environment variable `VULTR_API_RETRIES`.  **Default:** `5` |
| **api_retry_max_delay**  integer | Retry backoff delay in seconds is exponential up to this max. value, in seconds.  Fallback environment variable `VULTR_API_RETRY_MAX_DELAY`.  **Default:** `12` |
| **api_timeout**  integer | HTTP timeout to Vultr API.  Fallback environment variable `VULTR_API_TIMEOUT`.  **Default:** `180` |
| **description**  aliases: name  string / required | Description of the VPC. |
| **ip_block**  string | The subnet of the VPC.  Required if *state=present*. |
| **ip_type**  string | Type of the IP version.  Required if *state=present*.  **Choices:**   - `"v4"` ← (default) |
| **prefix_length**  integer | The number of bits for the netmask in CIDR notation, e.g. 24.  Required if *state=present*. |
| **region**  string | Region the VPC will be related to.  Required if *state=present*. |
| **state**  string | State of the VPC.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | Validate SSL certs of the Vultr API.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vpc2_module.md#id3)

> **Note:**
>
> - Also see the API documentation on <https://www.vultr.com/api/>.

## [Examples](vpc2_module.md#id4)

```yaml+jinja
- name: Ensure a VPC is present
  vultr.cloud.vpc2:
    description: my VPC.
    ip_block: 10.99.1.0
    prefix_length: 24
    region: ewr

- name: Ensure a VPC is absent
  vultr.cloud.vpc2:
    description: my VPC.
    state: absent
```

## [Return Values](vpc2_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vultr_api**  dictionary | Response from Vultr API with a few additions/modification.  **Returned:** success |
| **api_endpoint**  string | Endpoint used for the API requests.  **Returned:** success  **Sample:** `"https://api.vultr.com/v2"` |
| **api_retries**  integer | Amount of max retries for the API requests.  **Returned:** success  **Sample:** `5` |
| **api_retry_max_delay**  integer | Exponential backoff delay in seconds between retries up to this max delay value.  **Returned:** success  **Sample:** `12` |
| **api_timeout**  integer | Timeout used for the API requests.  **Returned:** success  **Sample:** `60` |
| **vultr_vpc2**  dictionary | Response from Vultr API.  **Returned:** success |
| **date_created**  string | Date the VPC was created.  **Returned:** success  **Sample:** `"2023-08-20T19:39:20+00:00"` |
| **description**  string | Description of the VPC.  **Returned:** success  **Sample:** `"my vpc"` |
| **id**  string | ID of the VPC.  **Returned:** success  **Sample:** `"cb676a46-66fd-4dfb-b839-443f2e6c0b60"` |
| **ip_block**  string | Subnet of the VPC.  **Returned:** success  **Sample:** `"10.99.1.0"` |
| **prefix_length**  integer | The number of bits for the netmask in CIDR notation.  **Returned:** success  **Sample:** `24` |
| **region**  string | The region the VPC is located in.  **Returned:** success  **Sample:** `"ewr"` |

### Authors

- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/vultr/ansible-collection-vultr/issues)
- [Repository (Sources)](https://github.com/vultr/ansible-collection-vultr)
