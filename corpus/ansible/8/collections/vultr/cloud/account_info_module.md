---
collection: ansible
version: "8"
title: "vultr.cloud.account_info module – Get information about the Vultr account"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vultr/cloud/account_info_module.html
fetched_at: 2026-07-28T02:58:45+00:00
---
# vultr.cloud.account_info module – Get information about the Vultr account

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
> To use it in a playbook, specify: `vultr.cloud.account_info`.

New in vultr.cloud 1.0.0

- [Synopsis](account_info_module.md#synopsis)
- [Parameters](account_info_module.md#parameters)
- [Notes](account_info_module.md#notes)
- [Examples](account_info_module.md#examples)
- [Return Values](account_info_module.md#return-values)

## [Synopsis](account_info_module.md#id1)

- Get infos about account balance, charges and payments.

## [Parameters](account_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_endpoint**  string | URL to API endpint (without trailing slash).  Fallback environment variable `VULTR_API_ENDPOINT`.  **Default:** `"https://api.vultr.com/v2"` |
| **api_key**  string / required | API key of the Vultr API.  Fallback environment variable `VULTR_API_KEY`. |
| **api_retries**  integer | Amount of retries in case of the Vultr API retuns an HTTP 503 code.  Fallback environment variable `VULTR_API_RETRIES`.  **Default:** `5` |
| **api_retry_max_delay**  integer | Retry backoff delay in seconds is exponential up to this max. value, in seconds.  Fallback environment variable `VULTR_API_RETRY_MAX_DELAY`.  **Default:** `12` |
| **api_timeout**  integer | HTTP timeout to Vultr API.  Fallback environment variable `VULTR_API_TIMEOUT`.  **Default:** `180` |
| **validate_certs**  boolean | Validate SSL certs of the Vultr API.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](account_info_module.md#id3)

> **Note:**
>
> - Also see the API documentation on <https://www.vultr.com/api/>.

## [Examples](account_info_module.md#id4)

```yaml+jinja
- name: Get Vultr account infos
  vultr.cloud.account_info:
  register: result

- name: Print the infos
  ansible.builtin.debug:
    var: result.vultr_account_info
```

## [Return Values](account_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vultr_account_info**  dictionary | Response from Vultr API.  **Returned:** success |
| **balance**  float | Your account balance.  **Returned:** success  **Sample:** `-214.69` |
| **last_payment_amount**  float | The amount of the last payment transaction.  **Returned:** success  **Sample:** `-250.0` |
| **last_payment_date**  string | Date of the last payment.  **Returned:** success  **Sample:** `"2021-11-07T05:57:59-05:00"` |
| **pending_charges**  float | Charges pending.  **Returned:** success  **Sample:** `57.03` |
| **vultr_api**  dictionary | Response from Vultr API with a few additions/modification.  **Returned:** success |
| **api_account**  string | Account used in the ini file to select the key.  **Returned:** success  **Sample:** `"default"` |
| **api_endpoint**  string | Endpoint used for the API requests.  **Returned:** success  **Sample:** `"https://api.vultr.com/v2"` |
| **api_retries**  integer | Amount of max retries for the API requests.  **Returned:** success  **Sample:** `5` |
| **api_retry_max_delay**  integer | Exponential backoff delay in seconds between retries up to this max delay value.  **Returned:** success  **Sample:** `12` |
| **api_timeout**  integer | Timeout used for the API requests.  **Returned:** success  **Sample:** `60` |

### Authors

- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/vultr/ansible-collection-vultr/issues)
- [Repository (Sources)](https://github.com/vultr/ansible-collection-vultr)
