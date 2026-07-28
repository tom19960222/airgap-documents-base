---
collection: ansible
version: "8"
title: "vultr.cloud.startup_script_info module – Gather information about the Vultr startup scripts"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vultr/cloud/startup_script_info_module.html
fetched_at: 2026-07-28T02:59:02+00:00
---
# vultr.cloud.startup_script_info module – Gather information about the Vultr startup scripts

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
> To use it in a playbook, specify: `vultr.cloud.startup_script_info`.

New in vultr.cloud 1.0.0

- [Synopsis](startup_script_info_module.md#synopsis)
- [Parameters](startup_script_info_module.md#parameters)
- [Notes](startup_script_info_module.md#notes)
- [Examples](startup_script_info_module.md#examples)
- [Return Values](startup_script_info_module.md#return-values)

## [Synopsis](startup_script_info_module.md#id1)

- Gather information about startup scripts available.

## [Parameters](startup_script_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_endpoint**  string | URL to API endpint (without trailing slash).  Fallback environment variable `VULTR_API_ENDPOINT`.  **Default:** `"https://api.vultr.com/v2"` |
| **api_key**  string / required | API key of the Vultr API.  Fallback environment variable `VULTR_API_KEY`. |
| **api_retries**  integer | Amount of retries in case of the Vultr API retuns an HTTP 503 code.  Fallback environment variable `VULTR_API_RETRIES`.  **Default:** `5` |
| **api_retry_max_delay**  integer | Retry backoff delay in seconds is exponential up to this max. value, in seconds.  Fallback environment variable `VULTR_API_RETRY_MAX_DELAY`.  **Default:** `12` |
| **api_timeout**  integer | HTTP timeout to Vultr API.  Fallback environment variable `VULTR_API_TIMEOUT`.  **Default:** `180` |
| **validate_certs**  boolean | Validate SSL certs of the Vultr API.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](startup_script_info_module.md#id3)

> **Note:**
>
> - Also see the API documentation on <https://www.vultr.com/api/>.

## [Examples](startup_script_info_module.md#id4)

```yaml+jinja
- name: Gather Vultr startup scripts information
  vultr.cloud.startup_script_info:
  register: result

- name: Print the gathered information
  ansible.builtin.debug:
    var: result.vultr_startup_script_info
```

## [Return Values](startup_script_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vultr_api**  dictionary | Response from Vultr API with a few additions/modification.  **Returned:** success |
| **api_endpoint**  string | Endpoint used for the API requests.  **Returned:** success  **Sample:** `"https://api.vultr.com/v2"` |
| **api_retries**  integer | Amount of max retries for the API requests.  **Returned:** success  **Sample:** `5` |
| **api_retry_max_delay**  integer | Exponential backoff delay in seconds between retries up to this max delay value.  **Returned:** success  **Sample:** `12` |
| **api_timeout**  integer | Timeout used for the API requests.  **Returned:** success  **Sample:** `60` |
| **vultr_startup_script_info**  list / elements=string | Response from Vultr API.  **Returned:** success |
| **date_created**  string | Date the startup script was created.  **Returned:** success  **Sample:** `"2020-10-10T01:56:20+00:00"` |
| **date_modified**  string | Date the startup script was modified.  **Returned:** success  **Sample:** `"2020-10-10T01:56:20+00:00"` |
| **id**  string | ID of the startup script.  **Returned:** success  **Sample:** `"56e5b8b5-120c-40b1-a087-3abc9cd8df57"` |
| **name**  string | Name of the startup script.  **Returned:** success  **Sample:** `"my startup script"` |
| **type**  string | The type of the startup script.  **Returned:** success  **Sample:** `"pxe"` |

### Authors

- Yanis Guenane (@Spredzy)
- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/vultr/ansible-collection-vultr/issues)
- [Repository (Sources)](https://github.com/vultr/ansible-collection-vultr)
