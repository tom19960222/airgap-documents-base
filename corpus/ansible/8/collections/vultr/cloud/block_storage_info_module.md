---
collection: ansible
version: "8"
title: "vultr.cloud.block_storage_info module – Get information about the Vultr block storage"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vultr/cloud/block_storage_info_module.html
fetched_at: 2026-07-28T02:58:47+00:00
---
# vultr.cloud.block_storage_info module – Get information about the Vultr block storage

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
> To use it in a playbook, specify: `vultr.cloud.block_storage_info`.

New in vultr.cloud 1.0.0

- [Synopsis](block_storage_info_module.md#synopsis)
- [Parameters](block_storage_info_module.md#parameters)
- [Notes](block_storage_info_module.md#notes)
- [Examples](block_storage_info_module.md#examples)
- [Return Values](block_storage_info_module.md#return-values)

## [Synopsis](block_storage_info_module.md#id1)

- Get infos about block storages available.

## [Parameters](block_storage_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_endpoint**  string | URL to API endpint (without trailing slash).  Fallback environment variable `VULTR_API_ENDPOINT`.  **Default:** `"https://api.vultr.com/v2"` |
| **api_key**  string / required | API key of the Vultr API.  Fallback environment variable `VULTR_API_KEY`. |
| **api_retries**  integer | Amount of retries in case of the Vultr API retuns an HTTP 503 code.  Fallback environment variable `VULTR_API_RETRIES`.  **Default:** `5` |
| **api_retry_max_delay**  integer | Retry backoff delay in seconds is exponential up to this max. value, in seconds.  Fallback environment variable `VULTR_API_RETRY_MAX_DELAY`.  **Default:** `12` |
| **api_timeout**  integer | HTTP timeout to Vultr API.  Fallback environment variable `VULTR_API_TIMEOUT`.  **Default:** `180` |
| **validate_certs**  boolean | Validate SSL certs of the Vultr API.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](block_storage_info_module.md#id3)

> **Note:**
>
> - Also see the API documentation on <https://www.vultr.com/api/>.

## [Examples](block_storage_info_module.md#id4)

```yaml+jinja
- name: Get Vultr block_storage infos
  vultr.cloud.block_storage_info:
  register: result

- name: Print the infos
  ansible.builtin.debug:
    var: result.vultr_block_storage_info
```

## [Return Values](block_storage_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vultr_api**  dictionary | Response from Vultr API with a few additions/modification.  **Returned:** success |
| **api_endpoint**  string | Endpoint used for the API requests.  **Returned:** success  **Sample:** `"https://api.vultr.com/v2"` |
| **api_retries**  integer | Amount of max retries for the API requests.  **Returned:** success  **Sample:** `5` |
| **api_retry_max_delay**  integer | Exponential backoff delay in seconds between retries up to this max delay value.  **Returned:** success  **Sample:** `12` |
| **api_timeout**  integer | Timeout used for the API requests.  **Returned:** success  **Sample:** `60` |
| **vultr_block_storage_info**  list / elements=string | Response from Vultr API as list.  **Returned:** success |
| **attached_to_instance**  string | The ID of the server instance the volume is attached to.  **Returned:** success  **Sample:** `"cb676a46-66fd-4dfb-b839-443f2e6c0b60"` |
| **cost**  float | Cost per month for the volume.  **Returned:** success  **Sample:** `1.0` |
| **date_created**  string | Date when the volume was created.  **Returned:** success  **Sample:** `"2020-10-10T01:56:20+00:00"` |
| **id**  string | ID of the block storage volume.  **Returned:** success  **Sample:** `"cb676a46-66fd-4dfb-b839-443f2e6c0b60"` |
| **label**  string | Label of the volume.  **Returned:** success  **Sample:** `"my volume"` |
| **mount_id**  string | Mount ID of the volume.  **Returned:** success  **Sample:** `"ewr-2f5d7a314fe44f"` |
| **region**  string | Region the volume was deployed into.  **Returned:** success  **Sample:** `"ews"` |
| **size_gb**  integer | Information about the volume size in GB.  **Returned:** success  **Sample:** `50` |
| **status**  string | Status about the deployment of the volume.  **Returned:** success  **Sample:** `"active"` |

### Authors

- René Moser (@resmo)
- Yanis Guenane (@Spredzy)

### Collection links

- [Issue Tracker](https://github.com/vultr/ansible-collection-vultr/issues)
- [Repository (Sources)](https://github.com/vultr/ansible-collection-vultr)
