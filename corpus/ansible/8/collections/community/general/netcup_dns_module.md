---
collection: ansible
version: "8"
title: "community.general.netcup_dns module – Manage Netcup DNS records"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/netcup_dns_module.html
fetched_at: 2026-07-28T01:48:05+00:00
---
# community.general.netcup_dns module – Manage Netcup DNS records

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](netcup_dns_module.md#ansible-collections-community-general-netcup-dns-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.netcup_dns`.

- [Synopsis](netcup_dns_module.md#synopsis)
- [Requirements](netcup_dns_module.md#requirements)
- [Parameters](netcup_dns_module.md#parameters)
- [Attributes](netcup_dns_module.md#attributes)
- [Examples](netcup_dns_module.md#examples)
- [Return Values](netcup_dns_module.md#return-values)

## [Synopsis](netcup_dns_module.md#id1)

- Manages DNS records via the Netcup API, see the docs <https://ccp.netcup.net/run/webservice/servers/endpoint.php>.

Aliases: net_tools.netcup_dns

## [Requirements](netcup_dns_module.md#id2)

The below requirements are needed on the host that executes this module.

- nc-dnsapi >= 0.1.3

## [Parameters](netcup_dns_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_key**  string / required | API key for authentication, must be obtained via the netcup CCP (<https://ccp.netcup.net>). |
| **api_password**  string / required | API password for authentication, must be obtained via the netcup CCP (<https://ccp.netcup.net>). |
| **customer_id**  integer / required | Netcup customer id. |
| **domain**  string / required | Domainname the records should be added / removed. |
| **priority**  integer | Record priority. Required for `type=MX`. |
| **record**  aliases: name  string | Record to add or delete, supports wildcard (`*`). Default is `@` (that is, the zone name).  **Default:** `"@"` |
| **solo**  boolean | Whether the record should be the only one for that record type and record name. Only use with `state=present`.  This will delete all other records with the same record name and type.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | Whether the record should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer  *added in community.general 5.7.0* | HTTP(S) connection timeout in seconds.  **Default:** `5` |
| **type**  string / required | Record type.  **Choices:**   - `"A"` - `"AAAA"` - `"MX"` - `"CNAME"` - `"CAA"` - `"SRV"` - `"TXT"` - `"TLSA"` - `"NS"` - `"DS"` |
| **value**  string / required | Record value. |

## [Attributes](netcup_dns_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](netcup_dns_module.md#id5)

```yaml+jinja
- name: Create a record of type A
  community.general.netcup_dns:
    api_key: "..."
    api_password: "..."
    customer_id: "..."
    domain: "example.com"
    name: "mail"
    type: "A"
    value: "127.0.0.1"

- name: Delete that record
  community.general.netcup_dns:
    api_key: "..."
    api_password: "..."
    customer_id: "..."
    domain: "example.com"
    name: "mail"
    type: "A"
    value: "127.0.0.1"
    state: absent

- name: Create a wildcard record
  community.general.netcup_dns:
    api_key: "..."
    api_password: "..."
    customer_id: "..."
    domain: "example.com"
    name: "*"
    type: "A"
    value: "127.0.1.1"

- name: Set the MX record for example.com
  community.general.netcup_dns:
    api_key: "..."
    api_password: "..."
    customer_id: "..."
    domain: "example.com"
    type: "MX"
    value: "mail.example.com"

- name: Set a record and ensure that this is the only one
  community.general.netcup_dns:
    api_key: "..."
    api_password: "..."
    customer_id: "..."
    name: "demo"
    domain: "example.com"
    type: "AAAA"
    value: "::1"
    solo: true

- name: Increase the connection timeout to avoid problems with an unstable connection
  community.general.netcup_dns:
    api_key: "..."
    api_password: "..."
    customer_id: "..."
    domain: "example.com"
    name: "mail"
    type: "A"
    value: "127.0.0.1"
    timeout: 30
```

## [Return Values](netcup_dns_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **records**  complex | list containing all records  **Returned:** success |
| **id**  integer | internal id of the record  **Returned:** success  **Sample:** `12345` |
| **name**  string | the record name  **Returned:** success  **Sample:** `"fancy-hostname"` |
| **priority**  integer | the record priority (only relevant if type=MX)  **Returned:** success  **Sample:** `0` |
| **type**  string | the record type  **Returned:** success  **Sample:** `"A"` |
| **value**  string | the record destination  **Returned:** success  **Sample:** `"127.0.0.1"` |

### Authors

- Nicolai Buchwitz (@nbuchwitz)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
