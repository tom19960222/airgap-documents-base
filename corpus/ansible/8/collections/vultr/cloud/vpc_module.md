---
collection: ansible
version: "8"
title: "vultr.cloud.vpc module – Manages VPCs on Vultr"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vultr/cloud/vpc_module.html
fetched_at: 2026-07-28T02:59:05+00:00
---
# vultr.cloud.vpc module – Manages VPCs on Vultr

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
> To use it in a playbook, specify: `vultr.cloud.vpc`.

New in vultr.cloud 1.0.0

- [Synopsis](vpc_module.md#synopsis)
- [Parameters](vpc_module.md#parameters)
- [Notes](vpc_module.md#notes)
- [Examples](vpc_module.md#examples)
- [Return Values](vpc_module.md#return-values)

## [Synopsis](vpc_module.md#id1)

- Create and remove VPCs.

## [Parameters](vpc_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_endpoint**  string | URL to API endpint (without trailing slash).  Fallback environment variable `VULTR_API_ENDPOINT`.  **Default:** `"https://api.vultr.com/v2"` |
| **api_key**  string / required | API key of the Vultr API.  Fallback environment variable `VULTR_API_KEY`. |
| **api_retries**  integer | Amount of retries in case of the Vultr API retuns an HTTP 503 code.  Fallback environment variable `VULTR_API_RETRIES`.  **Default:** `5` |
| **api_retry_max_delay**  integer | Retry backoff delay in seconds is exponential up to this max. value, in seconds.  Fallback environment variable `VULTR_API_RETRY_MAX_DELAY`.  **Default:** `12` |
| **api_timeout**  integer | HTTP timeout to Vultr API.  Fallback environment variable `VULTR_API_TIMEOUT`.  **Default:** `180` |
| **description**  aliases: name  string / required | Description of the VPC. |
| **region**  string | Region the VPC will be related to.  Required if *state=present*. |
| **state**  string | State of the VPC.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **v4_subnet**  string | IPv4 subnet of the VPC.  Required if *state=present*. |
| **v4_subnet_mask**  integer | IPv4 subnet mask of the VPC.  Required if *state=present*. |
| **validate_certs**  boolean | Validate SSL certs of the Vultr API.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vpc_module.md#id3)

> **Note:**
>
> - Also see the API documentation on <https://www.vultr.com/api/>.

## [Examples](vpc_module.md#id4)

```yaml+jinja
- name: Ensure a VPC is present
  vultr.cloud.vpc:
    description: my VPC.
    subnet: 10.99.1.0
    subnet_mask: 24
    region: ewr

- name: Ensure a VPC is absent
  vultr.cloud.vpc:
    description: my VPC.
    state: absent
```

## [Return Values](vpc_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vultr_api**  dictionary | Response from Vultr API with a few additions/modification.  **Returned:** success |
| **api_endpoint**  string | Endpoint used for the API requests.  **Returned:** success  **Sample:** `"https://api.vultr.com/v2"` |
| **api_retries**  integer | Amount of max retries for the API requests.  **Returned:** success  **Sample:** `5` |
| **api_retry_max_delay**  integer | Exponential backoff delay in seconds between retries up to this max delay value.  **Returned:** success  **Sample:** `12` |
| **api_timeout**  integer | Timeout used for the API requests.  **Returned:** success  **Sample:** `60` |
| **vultr_vpc**  dictionary | Response from Vultr API.  **Returned:** success |
| **date_created**  string | Date the VPC was created.  **Returned:** success  **Sample:** `"2020-10-10T01:56:20+00:00"` |
| **date_modified**  string | Date the VPC was modified.  **Returned:** success  **Sample:** `"2020-10-10T01:56:20+00:00"` |
| **description**  string | Description of the VPC.  **Returned:** success  **Sample:** `"my vpc"` |
| **id**  string | ID of the VPC.  **Returned:** success  **Sample:** `"cb676a46-66fd-4dfb-b839-443f2e6c0b60"` |
| **v4_subnet**  string | Subnet of the VPC.  **Returned:** success  **Sample:** `"10.99.1.0"` |
| **v4_subnet_maks**  string | Subnet mask of the VPC.  **Returned:** success  **Sample:** `"10.99.1.0"` |

### Authors

- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/vultr/ansible-collection-vultr/issues)
- [Repository (Sources)](https://github.com/vultr/ansible-collection-vultr)
