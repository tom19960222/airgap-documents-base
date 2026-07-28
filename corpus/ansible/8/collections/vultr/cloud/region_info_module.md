---
collection: ansible
version: "8"
title: "vultr.cloud.region_info module – Gather information about the Vultr regions"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vultr/cloud/region_info_module.html
fetched_at: 2026-07-28T02:58:57+00:00
---
# vultr.cloud.region_info module – Gather information about the Vultr regions

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
> To use it in a playbook, specify: `vultr.cloud.region_info`.

New in vultr.cloud 1.0.0

- [Synopsis](region_info_module.md#synopsis)
- [Parameters](region_info_module.md#parameters)
- [Notes](region_info_module.md#notes)
- [Examples](region_info_module.md#examples)
- [Return Values](region_info_module.md#return-values)

## [Synopsis](region_info_module.md#id1)

- Gather information about regions available to boot servers.

## [Parameters](region_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_endpoint**  string | URL to API endpint (without trailing slash).  Fallback environment variable `VULTR_API_ENDPOINT`.  **Default:** `"https://api.vultr.com/v2"` |
| **api_key**  string / required | API key of the Vultr API.  Fallback environment variable `VULTR_API_KEY`. |
| **api_retries**  integer | Amount of retries in case of the Vultr API retuns an HTTP 503 code.  Fallback environment variable `VULTR_API_RETRIES`.  **Default:** `5` |
| **api_retry_max_delay**  integer | Retry backoff delay in seconds is exponential up to this max. value, in seconds.  Fallback environment variable `VULTR_API_RETRY_MAX_DELAY`.  **Default:** `12` |
| **api_timeout**  integer | HTTP timeout to Vultr API.  Fallback environment variable `VULTR_API_TIMEOUT`.  **Default:** `180` |
| **validate_certs**  boolean | Validate SSL certs of the Vultr API.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](region_info_module.md#id3)

> **Note:**
>
> - Also see the API documentation on <https://www.vultr.com/api/>.

## [Examples](region_info_module.md#id4)

```yaml+jinja
- name: Gather Vultr regions information
  vultr.cloud.region_info:
  register: result

- name: Print the gathered information
  ansible.builtin.debug:
    var: result.vultr_region_info
```

## [Return Values](region_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vultr_api**  dictionary | Response from Vultr API with a few additions/modification.  **Returned:** success |
| **api_endpoint**  string | Endpoint used for the API requests.  **Returned:** success  **Sample:** `"https://api.vultr.com/v2"` |
| **api_retries**  integer | Amount of max retries for the API requests.  **Returned:** success  **Sample:** `5` |
| **api_retry_max_delay**  integer | Exponential backoff delay in seconds between retries up to this max delay value.  **Returned:** success  **Sample:** `12` |
| **api_timeout**  integer | Timeout used for the API requests.  **Returned:** success  **Sample:** `60` |
| **vultr_region_info**  list / elements=string | Response from Vultr API.  **Returned:** success  **Sample:** `[{"block_storage": false, "continent": "Europe", "country": "GB", "ddos_protection": true, "id": 8, "name": "London", "regioncode": "LHR", "state": ""}]` |

### Authors

- Yanis Guenane (@Spredzy)
- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/vultr/ansible-collection-vultr/issues)
- [Repository (Sources)](https://github.com/vultr/ansible-collection-vultr)
