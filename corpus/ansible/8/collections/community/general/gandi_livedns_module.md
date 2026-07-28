---
collection: ansible
version: "8"
title: "community.general.gandi_livedns module – Manage Gandi LiveDNS records"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/gandi_livedns_module.html
fetched_at: 2026-07-28T01:45:36+00:00
---
# community.general.gandi_livedns module – Manage Gandi LiveDNS records

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.gandi_livedns`.

New in community.general 2.3.0

- [Synopsis](gandi_livedns_module.md#synopsis)
- [Parameters](gandi_livedns_module.md#parameters)
- [Attributes](gandi_livedns_module.md#attributes)
- [Examples](gandi_livedns_module.md#examples)
- [Return Values](gandi_livedns_module.md#return-values)

## [Synopsis](gandi_livedns_module.md#id1)

- Manages DNS records by the Gandi LiveDNS API, see the docs: <https://doc.livedns.gandi.net/>.

Aliases: net_tools.gandi_livedns

## [Parameters](gandi_livedns_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_key**  string / required | Account API token. |
| **domain**  string / required | The name of the Domain to work with (for example, “example.com”). |
| **record**  string / required | Record to add. |
| **state**  string | Whether the record(s) should exist or not.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **ttl**  integer | The TTL to give the new record.  Required when `state=present`. |
| **type**  string / required | The type of DNS record to create. |
| **values**  list / elements=string | The record values.  Required when `state=present`. |

## [Attributes](gandi_livedns_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](gandi_livedns_module.md#id4)

```yaml+jinja
- name: Create a test A record to point to 127.0.0.1 in the my.com domain
  community.general.gandi_livedns:
    domain: my.com
    record: test
    type: A
    values:
    - 127.0.0.1
    ttl: 7200
    api_key: dummyapitoken
  register: record

- name: Create a mail CNAME record to www.my.com domain
  community.general.gandi_livedns:
    domain: my.com
    type: CNAME
    record: mail
    values:
    - www
    ttl: 7200
    api_key: dummyapitoken
    state: present

- name: Change its TTL
  community.general.gandi_livedns:
    domain: my.com
    type: CNAME
    record: mail
    values:
    - www
    ttl: 10800
    api_key: dummyapitoken
    state: present

- name: Delete the record
  community.general.gandi_livedns:
    domain: my.com
    type: CNAME
    record: mail
    api_key: dummyapitoken
    state: absent
```

## [Return Values](gandi_livedns_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **record**  dictionary | A dictionary containing the record data.  **Returned:** success, except on record deletion |
| **domain**  string | The domain associated with the record.  **Returned:** success  **Sample:** `"my.com"` |
| **record**  string | The record name.  **Returned:** success  **Sample:** `"www"` |
| **ttl**  integer | The time-to-live for the record.  **Returned:** success  **Sample:** `300` |
| **type**  string | The record type.  **Returned:** success  **Sample:** `"A"` |
| **values**  list / elements=string | The record content (details depend on record type).  **Returned:** success  **Sample:** `["192.0.2.91", "192.0.2.92"]` |

### Authors

- Gregory Thiemonge (@gthiemonge)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
