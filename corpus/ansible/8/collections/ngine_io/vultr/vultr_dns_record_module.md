---
collection: ansible
version: "8"
title: "ngine_io.vultr.vultr_dns_record module – Manages DNS records on Vultr."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ngine_io/vultr/vultr_dns_record_module.html
fetched_at: 2026-07-28T02:46:55+00:00
---
# ngine_io.vultr.vultr_dns_record module – Manages DNS records on Vultr.

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
> see [Requirements](vultr_dns_record_module.md#ansible-collections-ngine-io-vultr-vultr-dns-record-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.vultr.vultr_dns_record`.

New in ngine_io.vultr 0.1.0

- [Synopsis](vultr_dns_record_module.md#synopsis)
- [Requirements](vultr_dns_record_module.md#requirements)
- [Parameters](vultr_dns_record_module.md#parameters)
- [Notes](vultr_dns_record_module.md#notes)
- [Examples](vultr_dns_record_module.md#examples)
- [Return Values](vultr_dns_record_module.md#return-values)

## [Synopsis](vultr_dns_record_module.md#id1)

- Create, update and remove DNS records.

Aliases: vr_dns_record

## [Requirements](vultr_dns_record_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](vultr_dns_record_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_account**  string | Name of the ini section in the `vultr.ini` file.  The ENV variable `VULTR_API_ACCOUNT` is used as default, when defined.  **Default:** `"default"` |
| **api_endpoint**  string | URL to API endpint (without trailing slash).  The ENV variable `VULTR_API_ENDPOINT` is used as default, when defined.  Fallback value is <https://api.vultr.com> if not specified. |
| **api_key**  string | API key of the Vultr API.  The ENV variable `VULTR_API_KEY` is used as default, when defined. |
| **api_retries**  integer | Amount of retries in case of the Vultr API retuns an HTTP 503 code.  The ENV variable `VULTR_API_RETRIES` is used as default, when defined.  Fallback value is 5 retries if not specified. |
| **api_retry_max_delay**  integer | Retry backoff delay in seconds is exponential up to this max. value, in seconds.  The ENV variable `VULTR_API_RETRY_MAX_DELAY` is used as default, when defined.  Fallback value is 12 seconds. |
| **api_timeout**  integer | HTTP timeout to Vultr API.  The ENV variable `VULTR_API_TIMEOUT` is used as default, when defined.  Fallback value is 60 seconds if not specified. |
| **data**  string | Data of the record.  Required if `state=present` or `multiple=yes`. |
| **domain**  string / required | The domain the record is related to. |
| **multiple**  boolean | Whether to use more than one record with similar `name` including no name and `record_type`.  Only allowed for a few record types, e.g. `record_type=A`, `record_type=NS` or `record_type=MX`.  `data` will not be updated, instead it is used as a key to find existing records.  **Choices:**   - `false` ← (default) - `true` |
| **name**  aliases: subrecord  string | The record name (subrecord).  **Default:** `""` |
| **priority**  integer | Priority of the record.  **Default:** `0` |
| **record_type**  aliases: type  string | Type of the record.  **Choices:**   - `"A"` ← (default) - `"AAAA"` - `"CNAME"` - `"MX"` - `"SRV"` - `"CAA"` - `"TXT"` - `"NS"` - `"SSHFP"` |
| **state**  string | State of the DNS record.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **ttl**  integer | TTL of the record.  **Default:** `300` |
| **validate_certs**  boolean | Validate SSL certs of the Vultr API.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vultr_dns_record_module.md#id4)

> **Note:**
>
> - Also see the API documentation on <https://www.vultr.com/api/>.

## [Examples](vultr_dns_record_module.md#id5)

```yaml+jinja
- name: Ensure an A record exists
  ngine_io.vultr.vultr_dns_record:
    name: www
    domain: example.com
    data: 10.10.10.10
    ttl: 3600

- name: Ensure a second A record exists for round robin LB
  ngine_io.vultr.vultr_dns_record:
    name: www
    domain: example.com
    data: 10.10.10.11
    ttl: 60
    multiple: yes

- name: Ensure a CNAME record exists
  ngine_io.vultr.vultr_dns_record:
    name: web
    record_type: CNAME
    domain: example.com
    data: www.example.com

- name: Ensure MX record exists
  ngine_io.vultr.vultr_dns_record:
    record_type: MX
    domain: example.com
    data: "{{ item.data }}"
    priority: "{{ item.priority }}"
    multiple: yes
  with_items:
  - { data: mx1.example.com, priority: 10 }
  - { data: mx2.example.com, priority: 10 }
  - { data: mx3.example.com, priority: 20 }

- name: Ensure a record is absent
  ngine_io.vultr.vultr_dns_record:
    name: www
    domain: example.com
    state: absent

- name: Ensure MX record is absent in case multiple exists
  ngine_io.vultr.vultr_dns_record:
    record_type: MX
    domain: example.com
    data: mx1.example.com
    multiple: yes
    state: absent
```

## [Return Values](vultr_dns_record_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vultr_api**  complex | Response from Vultr API with a few additions/modification  **Returned:** success |
| **api_account**  string | Account used in the ini file to select the key  **Returned:** success  **Sample:** `"default"` |
| **api_endpoint**  string | Endpoint used for the API requests  **Returned:** success  **Sample:** `"https://api.vultr.com"` |
| **api_retries**  integer | Amount of max retries for the API requests  **Returned:** success  **Sample:** `5` |
| **api_retry_max_delay**  integer | Exponential backoff delay in seconds between retries up to this max delay value.  **Returned:** success  **Sample:** `12` |
| **api_timeout**  integer | Timeout used for the API requests  **Returned:** success  **Sample:** `60` |
| **vultr_dns_record**  complex | Response from Vultr API  **Returned:** success |
| **data**  string | Data of the DNS record.  **Returned:** success  **Sample:** `"10.10.10.10"` |
| **domain**  string | Domain the DNS record is related to.  **Returned:** success  **Sample:** `"example.com"` |
| **id**  integer | The ID of the DNS record.  **Returned:** success  **Sample:** `1265277` |
| **name**  string | The name of the DNS record.  **Returned:** success  **Sample:** `"web"` |
| **priority**  integer | Priority of the DNS record.  **Returned:** success  **Sample:** `10` |
| **record_type**  string | The name of the DNS record.  **Returned:** success  **Sample:** `"web"` |
| **ttl**  integer | Time to live of the DNS record.  **Returned:** success  **Sample:** `300` |

### Authors

- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/ngine-io/ansible-collection-vultr/issues)
- [Repository (Sources)](https://github.com/ngine-io/ansible-collection-vultr)
