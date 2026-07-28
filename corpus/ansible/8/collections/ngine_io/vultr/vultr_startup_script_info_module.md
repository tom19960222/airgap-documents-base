---
collection: ansible
version: "8"
title: "ngine_io.vultr.vultr_startup_script_info module – Gather information about the Vultr startup scripts available."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ngine_io/vultr/vultr_startup_script_info_module.html
fetched_at: 2026-07-28T02:47:16+00:00
---
# ngine_io.vultr.vultr_startup_script_info module – Gather information about the Vultr startup scripts available.

> **Note:**
>
> This module is part of the [ngine_io.vultr collection](https://galaxy.ansible.com/ui/repo/published/ngine_io/vultr/) (version 1.1.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ngine_io.vultr`.
> You need further requirements to be able to use this module,
> see [Requirements](vultr_startup_script_info_module.md#ansible-collections-ngine-io-vultr-vultr-startup-script-info-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.vultr.vultr_startup_script_info`.

New in ngine_io.vultr 0.1.0

- [Synopsis](vultr_startup_script_info_module.md#synopsis)
- [Requirements](vultr_startup_script_info_module.md#requirements)
- [Parameters](vultr_startup_script_info_module.md#parameters)
- [Notes](vultr_startup_script_info_module.md#notes)
- [Examples](vultr_startup_script_info_module.md#examples)
- [Return Values](vultr_startup_script_info_module.md#return-values)

## [Synopsis](vultr_startup_script_info_module.md#id1)

- Gather information about vultr_startup_scripts available.

Aliases: vultr_startup_script_facts

## [Requirements](vultr_startup_script_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](vultr_startup_script_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_account**  string | Name of the ini section in the `vultr.ini` file.  The ENV variable `VULTR_API_ACCOUNT` is used as default, when defined.  **Default:** `"default"` |
| **api_endpoint**  string | URL to API endpint (without trailing slash).  The ENV variable `VULTR_API_ENDPOINT` is used as default, when defined.  Fallback value is <https://api.vultr.com> if not specified. |
| **api_key**  string | API key of the Vultr API.  The ENV variable `VULTR_API_KEY` is used as default, when defined. |
| **api_retries**  integer | Amount of retries in case of the Vultr API retuns an HTTP 503 code.  The ENV variable `VULTR_API_RETRIES` is used as default, when defined.  Fallback value is 5 retries if not specified. |
| **api_retry_max_delay**  integer | Retry backoff delay in seconds is exponential up to this max. value, in seconds.  The ENV variable `VULTR_API_RETRY_MAX_DELAY` is used as default, when defined.  Fallback value is 12 seconds. |
| **api_timeout**  integer | HTTP timeout to Vultr API.  The ENV variable `VULTR_API_TIMEOUT` is used as default, when defined.  Fallback value is 60 seconds if not specified. |
| **validate_certs**  boolean | Validate SSL certs of the Vultr API.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vultr_startup_script_info_module.md#id4)

> **Note:**
>
> - Also see the API documentation on <https://www.vultr.com/api/>.

## [Examples](vultr_startup_script_info_module.md#id5)

```yaml+jinja
- name: Gather Vultr startup scripts information
  ngine_io.vultr.vultr_startup_script_info:
  register: result

- name: Print the gathered information
  debug:
    var: result.vultr_startup_script_info
```

## [Return Values](vultr_startup_script_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vultr_api**  complex | Response from Vultr API with a few additions/modification  **Returned:** success |
| **api_account**  string | Account used in the ini file to select the key  **Returned:** success  **Sample:** `"default"` |
| **api_endpoint**  string | Endpoint used for the API requests  **Returned:** success  **Sample:** `"https://api.vultr.com"` |
| **api_retries**  integer | Amount of max retries for the API requests  **Returned:** success  **Sample:** `5` |
| **api_retry_max_delay**  integer | Exponential backoff delay in seconds between retries up to this max delay value.  **Returned:** success  **Sample:** `12` |
| **api_timeout**  integer | Timeout used for the API requests  **Returned:** success  **Sample:** `60` |
| **vultr_startup_script_info**  complex | Response from Vultr API  **Returned:** success |
| **date_created**  string | Date the startup script was created.  **Returned:** success  **Sample:** `"2017-08-26 12:47:48"` |
| **date_modified**  string | Date the startup script was modified.  **Returned:** success  **Sample:** `"2017-08-26 12:47:48"` |
| **id**  string | ID of the startup script.  **Returned:** success  **Sample:** `"249395"` |
| **name**  string | Name of the startup script.  **Returned:** success  **Sample:** `"my startup script"` |
| **script**  string | The source code of the startup script.  **Returned:** success  **Sample:** `"#!/bin/bash\necho Hello World > /root/hello"` |
| **type**  string | The type of the startup script.  **Returned:** success  **Sample:** `"pxe"` |

### Authors

- Yanis Guenane (@Spredzy)

### Collection links

- [Issue Tracker](https://github.com/ngine-io/ansible-collection-vultr/issues)
- [Repository (Sources)](https://github.com/ngine-io/ansible-collection-vultr)
