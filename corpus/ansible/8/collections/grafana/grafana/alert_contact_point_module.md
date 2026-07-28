---
collection: ansible
version: "8"
title: "grafana.grafana.alert_contact_point module – Manage Alerting Contact points in Grafana"
source_url: https://docs.ansible.com/projects/ansible/8/collections/grafana/grafana/alert_contact_point_module.html
fetched_at: 2026-07-28T02:33:48+00:00
---
# grafana.grafana.alert_contact_point module – Manage Alerting Contact points in Grafana

> **Note:**
>
> This module is part of the [grafana.grafana collection](https://galaxy.ansible.com/ui/repo/published/grafana/grafana/) (version 2.2.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install grafana.grafana`.
> You need further requirements to be able to use this module,
> see [Requirements](alert_contact_point_module.md#ansible-collections-grafana-grafana-alert-contact-point-module-requirements) for details.
>
> To use it in a playbook, specify: `grafana.grafana.alert_contact_point`.

New in grafana.grafana 0.0.1

- [Synopsis](alert_contact_point_module.md#synopsis)
- [Requirements](alert_contact_point_module.md#requirements)
- [Parameters](alert_contact_point_module.md#parameters)
- [Notes](alert_contact_point_module.md#notes)
- [Examples](alert_contact_point_module.md#examples)
- [Return Values](alert_contact_point_module.md#return-values)

## [Synopsis](alert_contact_point_module.md#id1)

- Create, Update and delete Contact points using Ansible.

## [Requirements](alert_contact_point_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests >= 1.0.0

## [Parameters](alert_contact_point_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **disableResolveMessage**  boolean | When set to `true`, Disables the resolve message [OK] that is sent when alerting state returns to `false`.  **Choices:**   - `false` ← (default) - `true` |
| **grafana_api_key**  string / required | Grafana API Key used to authenticate with Grafana. |
| **grafana_url**  string / required | URL of the Grafana instance. |
| **name**  string / required | Sets the name of the contact point. |
| **settings**  dictionary / required | Sets Contact point settings. |
| **state**  string | State for the Grafana Alert Contact Point.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **type**  string / required | Sets Contact point type. |
| **uid**  string / required | Sets the UID of the Contact point. |

## [Notes](alert_contact_point_module.md#id4)

> **Note:**
>
> - Does not support `check_mode`.

## [Examples](alert_contact_point_module.md#id5)

```yaml+jinja
- name: Create/Update Alerting contact point
  grafana.grafana.alert_contact_point:
    name: ops-email
    uid: opsemail
    type: email
    settings:
      addresses: "ops@mydomain.com,devs@mydomain.com"
    grafana_url: "{{ grafana_url }}"
    grafana_api_key: "{{ grafana_api_key }}"
    state: present

- name: Delete Alerting contact point
  grafana.grafana.alert_contact_point:
    name: ops-email
    uid: opsemail
    type: email
    settings:
      addresses: "ops@mydomain.com,devs@mydomain.com"
    grafana_url: "{{ grafana_url }}"
    grafana_api_key: "{{ grafana_api_key }}"
    state: absent
```

## [Return Values](alert_contact_point_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **output**  dictionary | Dict object containing Contact point information information.  **Returned:** On success |
| **disableResolveMessage**  boolean | When set to True, Disables the resolve message [OK] that is sent when alerting state returns to false.  **Returned:** state is present and on success  **Sample:** `false` |
| **name**  string | The name for the contact point.  **Returned:** state is present and on success  **Sample:** `"ops-email"` |
| **settings**  dictionary | Contains contact point settings.  **Returned:** state is present and on success  **Sample:** `{"addresses": "ops@mydomain.com,devs@mydomain.com"}` |
| **type**  string | The type of contact point.  **Returned:** state is present and on success  **Sample:** `"email"` |
| **uid**  string | The UID for the contact point.  **Returned:** state is present and on success  **Sample:** `"opsemail"` |

### Authors

- Ishan Jain (@ishanjainn)

### Collection links

- [Issue Tracker](https://github.com/grafana/grafana-ansible-collection/issues)
- [Repository (Sources)](https://github.com/grafana/grafana-ansible-collection)
