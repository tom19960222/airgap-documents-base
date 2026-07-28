---
collection: ansible
version: "8"
title: "vultr.cloud.dns_domain module – Manages DNS domains on Vultr"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vultr/cloud/dns_domain_module.html
fetched_at: 2026-07-28T02:58:48+00:00
---
# vultr.cloud.dns_domain module – Manages DNS domains on Vultr

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
> To use it in a playbook, specify: `vultr.cloud.dns_domain`.

New in vultr.cloud 1.0.0

- [Synopsis](dns_domain_module.md#synopsis)
- [Parameters](dns_domain_module.md#parameters)
- [Notes](dns_domain_module.md#notes)
- [Examples](dns_domain_module.md#examples)
- [Return Values](dns_domain_module.md#return-values)

## [Synopsis](dns_domain_module.md#id1)

- Create and remove DNS domains.

## [Parameters](dns_domain_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_endpoint**  string | URL to API endpint (without trailing slash).  Fallback environment variable `VULTR_API_ENDPOINT`.  **Default:** `"https://api.vultr.com/v2"` |
| **api_key**  string / required | API key of the Vultr API.  Fallback environment variable `VULTR_API_KEY`. |
| **api_retries**  integer | Amount of retries in case of the Vultr API retuns an HTTP 503 code.  Fallback environment variable `VULTR_API_RETRIES`.  **Default:** `5` |
| **api_retry_max_delay**  integer | Retry backoff delay in seconds is exponential up to this max. value, in seconds.  Fallback environment variable `VULTR_API_RETRY_MAX_DELAY`.  **Default:** `12` |
| **api_timeout**  integer | HTTP timeout to Vultr API.  Fallback environment variable `VULTR_API_TIMEOUT`.  **Default:** `180` |
| **dns_sec**  string | Ensure DNSSEC is enabled or disabled.  **Choices:**   - `"enabled"` - `"disabled"` ← (default) |
| **domain**  aliases: name  string / required | The domain name. |
| **ip**  aliases: server_ip  string | The default server IP.  Use [vultr.cloud.dns_record](dns_record_module.md#ansible-collections-vultr-cloud-dns-record-module) to change it once the domain is created.  Required if `state=present`. |
| **state**  string | State of the DNS domain.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | Validate SSL certs of the Vultr API.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](dns_domain_module.md#id3)

> **Note:**
>
> - Also see the API documentation on <https://www.vultr.com/api/>.

## [Examples](dns_domain_module.md#id4)

```yaml+jinja
- name: Ensure a domain exists with DNSSEC
  vultr.cloud.dns_domain:
    name: example.com
    dns_sec: enabled
    server_ip: 10.10.10.10

- name: Ensure a domain is absent
  vultr.cloud.dns_domain:
    name: example.com
    state: absent
```

## [Return Values](dns_domain_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vultr_api**  dictionary | Response from Vultr API with a few additions/modification.  **Returned:** success |
| **api_endpoint**  string | Endpoint used for the API requests.  **Returned:** success  **Sample:** `"https://api.vultr.com/v2"` |
| **api_retries**  integer | Amount of max retries for the API requests.  **Returned:** success  **Sample:** `5` |
| **api_retry_max_delay**  integer | Exponential backoff delay in seconds between retries up to this max delay value.  **Returned:** success  **Sample:** `12` |
| **api_timeout**  integer | Timeout used for the API requests.  **Returned:** success  **Sample:** `60` |
| **vultr_dns_domain**  dictionary | Response from Vultr API.  **Returned:** success |
| **date_created**  string | Date the DNS domain was created.  **Returned:** success  **Sample:** `"2020-10-10T01:56:20+00:00"` |
| **dns_sec**  string | Whether DNSSEC is enabled or disabled.  **Returned:** success  **Sample:** `"disabled"` |
| **name**  string | Name of the DNS Domain.  **Returned:** success  **Sample:** `"example.com"` |

### Authors

- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/vultr/ansible-collection-vultr/issues)
- [Repository (Sources)](https://github.com/vultr/ansible-collection-vultr)
