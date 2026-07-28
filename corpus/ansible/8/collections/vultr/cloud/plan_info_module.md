---
collection: ansible
version: "8"
title: "vultr.cloud.plan_info module – Gather information about the Vultr plans"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vultr/cloud/plan_info_module.html
fetched_at: 2026-07-28T02:58:56+00:00
---
# vultr.cloud.plan_info module – Gather information about the Vultr plans

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
> To use it in a playbook, specify: `vultr.cloud.plan_info`.

New in vultr.cloud 1.0.0

- [Synopsis](plan_info_module.md#synopsis)
- [Parameters](plan_info_module.md#parameters)
- [Notes](plan_info_module.md#notes)
- [Examples](plan_info_module.md#examples)
- [Return Values](plan_info_module.md#return-values)

## [Synopsis](plan_info_module.md#id1)

- Gather information about plans available to boot servers.

## [Parameters](plan_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_endpoint**  string | URL to API endpint (without trailing slash).  Fallback environment variable `VULTR_API_ENDPOINT`.  **Default:** `"https://api.vultr.com/v2"` |
| **api_key**  string / required | API key of the Vultr API.  Fallback environment variable `VULTR_API_KEY`. |
| **api_retries**  integer | Amount of retries in case of the Vultr API retuns an HTTP 503 code.  Fallback environment variable `VULTR_API_RETRIES`.  **Default:** `5` |
| **api_retry_max_delay**  integer | Retry backoff delay in seconds is exponential up to this max. value, in seconds.  Fallback environment variable `VULTR_API_RETRY_MAX_DELAY`.  **Default:** `12` |
| **api_timeout**  integer | HTTP timeout to Vultr API.  Fallback environment variable `VULTR_API_TIMEOUT`.  **Default:** `180` |
| **validate_certs**  boolean | Validate SSL certs of the Vultr API.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](plan_info_module.md#id3)

> **Note:**
>
> - Also see the API documentation on <https://www.vultr.com/api/>.

## [Examples](plan_info_module.md#id4)

```yaml+jinja
- name: Gather Vultr plans information
  vultr.cloud.plan_info:
  register: result

- name: Print the gathered information
  ansible.builtin.debug:
    var: result.vultr_plan_info
```

## [Return Values](plan_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vultr_api**  dictionary | Response from Vultr API with a few additions/modification.  **Returned:** success |
| **api_endpoint**  string | Endpoint used for the API requests.  **Returned:** success  **Sample:** `"https://api.vultr.com/v2"` |
| **api_retries**  integer | Amount of max retries for the API requests.  **Returned:** success  **Sample:** `5` |
| **api_retry_max_delay**  integer | Exponential backoff delay in seconds between retries up to this max delay value.  **Returned:** success  **Sample:** `12` |
| **api_timeout**  integer | Timeout used for the API requests.  **Returned:** success  **Sample:** `60` |
| **vultr_plan_info**  list / elements=string | Response from Vultr API as list.  **Returned:** success |
| **bandwidth**  integer | Bandwidth in MB.  **Returned:** success  **Sample:** `6144` |
| **disk**  integer | Disk size in GB.  **Returned:** success  **Sample:** `512` |
| **disk_count**  integer | Amount of disks.  **Returned:** success  **Sample:** `1` |
| **id**  string | ID of the plan.  **Returned:** success  **Sample:** `"vhf-8c-32gb"` |
| **locations**  list / elements=string | List of locations the plan is available in.  **Returned:** success  **Sample:** `["ewr"]` |
| **monthly_cost**  integer | Monthly cost in $.  **Returned:** success  **Sample:** `192` |
| **ram**  integer | Amount of RAM in MB.  **Returned:** success  **Sample:** `32768` |
| **type**  string | Type of plan.  **Returned:** success  **Sample:** `"vhf"` |
| **vcpu_count**  integer | Amount of CPUs.  **Returned:** success  **Sample:** `8` |

### Authors

- Yanis Guenane (@Spredzy)
- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/vultr/ansible-collection-vultr/issues)
- [Repository (Sources)](https://github.com/vultr/ansible-collection-vultr)
