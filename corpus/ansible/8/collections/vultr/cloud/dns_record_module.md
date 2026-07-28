---
collection: ansible
version: "8"
title: "vultr.cloud.dns_record module – Manages DNS records on Vultr"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vultr/cloud/dns_record_module.html
fetched_at: 2026-07-28T02:58:49+00:00
---
# vultr.cloud.dns_record module – Manages DNS records on Vultr

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
> To use it in a playbook, specify: `vultr.cloud.dns_record`.

New in vultr.cloud 1.0.0

- [Synopsis](dns_record_module.md#synopsis)
- [Parameters](dns_record_module.md#parameters)
- [Notes](dns_record_module.md#notes)
- [Examples](dns_record_module.md#examples)
- [Return Values](dns_record_module.md#return-values)

## [Synopsis](dns_record_module.md#id1)

- Create, update and remove DNS records.

## [Parameters](dns_record_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_endpoint**  string | URL to API endpint (without trailing slash).  Fallback environment variable `VULTR_API_ENDPOINT`.  **Default:** `"https://api.vultr.com/v2"` |
| **api_key**  string / required | API key of the Vultr API.  Fallback environment variable `VULTR_API_KEY`. |
| **api_retries**  integer | Amount of retries in case of the Vultr API retuns an HTTP 503 code.  Fallback environment variable `VULTR_API_RETRIES`.  **Default:** `5` |
| **api_retry_max_delay**  integer | Retry backoff delay in seconds is exponential up to this max. value, in seconds.  Fallback environment variable `VULTR_API_RETRY_MAX_DELAY`.  **Default:** `12` |
| **api_timeout**  integer | HTTP timeout to Vultr API.  Fallback environment variable `VULTR_API_TIMEOUT`.  **Default:** `180` |
| **data**  string | Data of the record.  Required if `state=present`. |
| **domain**  string / required | The domain the record is related to. |
| **multiple**  boolean | Whether to use more than one record with similar *name* including no name and *type*.  Only allowed for a few record types, e.g. `type=A`, `type=NS` or `type=MX`.  *data* will not be updated, instead it is used as a key to find existing records.  **Choices:**   - `false` ← (default) - `true` |
| **name**  string | The record name.  **Default:** `""` |
| **priority**  integer | Priority of the record. |
| **state**  string | State of the DNS record.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **ttl**  integer | TTL of the record.  **Default:** `300` |
| **type**  aliases: record_type  string | Type of the record.  **Choices:**   - `"A"` ← (default) - `"AAAA"` - `"CNAME"` - `"NS"` - `"MX"` - `"SRV"` - `"TXT"` - `"CAA"` - `"SSHFP"` |
| **validate_certs**  boolean | Validate SSL certs of the Vultr API.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](dns_record_module.md#id3)

> **Note:**
>
> - Also see the API documentation on <https://www.vultr.com/api/>.

## [Examples](dns_record_module.md#id4)

```yaml+jinja
- name: Ensure an A record exists
  vultr.cloud.dns_record:
    name: www
    domain: example.com
    data: 10.10.10.10
    ttl: 3600

- name: Ensure a second A record exists for round robin LB
  vultr.cloud.dns_record:
    name: www
    domain: example.com
    data: 10.10.10.11
    ttl: 60
    multiple: true

- name: Ensure a CNAME record exists
  vultr.cloud.dns_record:
    name: web
    type: CNAME
    domain: example.com
    data: www.example.com

- name: Ensure MX record exists
  vultr.cloud.dns_record:
    type: MX
    domain: example.com
    data: "{{ item.data }}"
    priority: "{{ item.priority }}"
    multiple: true
  with_items:
    - { data: mx1.example.com, priority: 10 }
    - { data: mx2.example.com, priority: 10 }
    - { data: mx3.example.com, priority: 20 }

- name: Ensure a record is absent
  vultr.cloud.dns_record:
    name: www
    domain: example.com
    state: absent

- name: Ensure one MX record is absent if multiple exists
  vultr.cloud.dns_record:
    record_type: MX
    domain: example.com
    data: mx1.example.com
    multiple: true
    state: absent
```

## [Return Values](dns_record_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dns_record**  dictionary | Response from Vultr API.  **Returned:** success |
| **data**  string | Data of the DNS record.  **Returned:** success  **Sample:** `"10.10.10.10"` |
| **id**  string | The ID of the DNS record.  **Returned:** success  **Sample:** `"cb676a46-66fd-4dfb-b839-443f2e6c0b60"` |
| **name**  string | The name of the DNS record.  **Returned:** success  **Sample:** `"web"` |
| **priority**  integer | Priority of the DNS record.  **Returned:** success  **Sample:** `10` |
| **ttl**  integer | Time to live of the DNS record.  **Returned:** success  **Sample:** `300` |
| **type**  string | The name of the DNS record.  **Returned:** success  **Sample:** `"A"` |
| **vultr_api**  dictionary | Response from Vultr API with a few additions/modification.  **Returned:** success |
| **api_endpoint**  string | Endpoint used for the API requests.  **Returned:** success  **Sample:** `"https://api.vultr.com/v2"` |
| **api_retries**  integer | Amount of max retries for the API requests.  **Returned:** success  **Sample:** `5` |
| **api_retry_max_delay**  integer | Exponential backoff delay in seconds between retries up to this max delay value.  **Returned:** success  **Sample:** `12` |
| **api_timeout**  integer | Timeout used for the API requests.  **Returned:** success  **Sample:** `60` |

### Authors

- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/vultr/ansible-collection-vultr/issues)
- [Repository (Sources)](https://github.com/vultr/ansible-collection-vultr)
