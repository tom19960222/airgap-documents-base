---
collection: ansible
version: "8"
title: "community.general.alerta_customer module – Manage customers in Alerta"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/alerta_customer_module.html
fetched_at: 2026-07-28T01:44:35+00:00
---
# community.general.alerta_customer module – Manage customers in Alerta

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
> To use it in a playbook, specify: `community.general.alerta_customer`.

New in community.general 4.8.0

- [Synopsis](alerta_customer_module.md#synopsis)
- [Parameters](alerta_customer_module.md#parameters)
- [Attributes](alerta_customer_module.md#attributes)
- [See Also](alerta_customer_module.md#see-also)
- [Examples](alerta_customer_module.md#examples)
- [Return Values](alerta_customer_module.md#return-values)

## [Synopsis](alerta_customer_module.md#id1)

- Create or delete customers in Alerta with the REST API.

Aliases: monitoring.alerta_customer

## [Parameters](alerta_customer_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **alerta_url**  string / required | The Alerta API endpoint. |
| **api_key**  string | The access token for the API. |
| **api_password**  string | The password for the API using basic auth. |
| **api_username**  string | The username for the API using basic auth. |
| **customer**  string / required | Name of the customer. |
| **match**  string / required | The matching logged in user for the customer. |
| **state**  string | Whether the customer should exist or not.  Both `customer` and `match` identify a customer that should be added or removed.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Attributes](alerta_customer_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [See Also](alerta_customer_module.md#id4)

> **See also:**
>
> [API documentation](https://docs.alerta.io/api/reference.html#customers)
> :   Documentation for Alerta API

## [Examples](alerta_customer_module.md#id5)

```yaml+jinja
- name: Create customer
  community.general.alerta_customer:
    alerta_url: https://alerta.example.com
    api_username: admin@example.com
    api_password: password
    customer: Developer
    match: dev@example.com

- name: Delete customer
  community.general.alerta_customer:
    alerta_url: https://alerta.example.com
    api_username: admin@example.com
    api_password: password
    customer: Developer
    match: dev@example.com
    state: absent
```

## [Return Values](alerta_customer_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Success or failure message.  **Returned:** always  **Sample:** `"Customer customer1 created"` |
| **response**  dictionary | The response from the API.  **Returned:** always |

### Authors

- Christian Wollinger (@cwollinger)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
