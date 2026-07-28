---
collection: ansible
version: "8"
title: "grafana.grafana.dashboard module – Manage Dashboards in Grafana"
source_url: https://docs.ansible.com/projects/ansible/8/collections/grafana/grafana/dashboard_module.html
fetched_at: 2026-07-28T02:33:52+00:00
---
# grafana.grafana.dashboard module – Manage Dashboards in Grafana

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
> see [Requirements](dashboard_module.md#ansible-collections-grafana-grafana-dashboard-module-requirements) for details.
>
> To use it in a playbook, specify: `grafana.grafana.dashboard`.

New in grafana.grafana 0.0.1

- [Synopsis](dashboard_module.md#synopsis)
- [Requirements](dashboard_module.md#requirements)
- [Parameters](dashboard_module.md#parameters)
- [Notes](dashboard_module.md#notes)
- [Examples](dashboard_module.md#examples)
- [Return Values](dashboard_module.md#return-values)

## [Synopsis](dashboard_module.md#id1)

- Create, Update and delete Dashboards using Ansible.

## [Requirements](dashboard_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests >= 1.0.0

## [Parameters](dashboard_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dashboard**  dictionary / required | JSON source code for dashboard. |
| **grafana_api_key**  string / required | Grafana API Key to authenticate with Grafana Cloud. |
| **grafana_url**  string / required | URL of the Grafana instance. |
| **state**  string | State for the Grafana Dashboard.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](dashboard_module.md#id4)

> **Note:**
>
> - Does not support `check_mode`.
> - Does not support `Idempotency`.

## [Examples](dashboard_module.md#id5)

```yaml+jinja
- name: Create/Update a dashboard
  grafana.grafana.dashboard:
    dashboard: "{{ lookup('ansible.builtin.file', 'dashboard.json') }}"
    grafana_url: "{{ grafana_url }}"
    grafana_api_key: "{{ grafana_api_key }}"
    state: present

- name: Delete dashboard
  grafana.grafana.dashboard:
    dashboard: "{{ lookup('ansible.builtin.file', 'dashboard.json') }}"
    grafana_url: "{{ grafana_url }}"
    grafana_api_key: "{{ grafana_api_key }}"
    state: absent
```

## [Return Values](dashboard_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **output**  dictionary | Dict object containing folder information.  **Returned:** On success |
| **id**  integer | The ID for the dashboard.  **Returned:** on success  **Sample:** `17` |
| **message**  string | The message returned after the operation on the dashboard.  **Returned:** state is absent and on success  **Sample:** `"Dashboard Ansible Integration Test deleted"` |
| **slug**  string | The slug for the dashboard.  **Returned:** state is present and on success  **Sample:** `"ansible-integration-test"` |
| **status**  string | The status of the dashboard.  **Returned:** state is present and on success  **Sample:** `"success"` |
| **title**  string | The name of the dashboard.  **Returned:** state is absent and on success  **Sample:** `"Ansible Integration Test"` |
| **uid**  string | The UID for the dashboard.  **Returned:** state is present and on success  **Sample:** `"test1234"` |
| **url**  string | The endpoint for the dashboard.  **Returned:** state is present and on success  **Sample:** `"/d/test1234/ansible-integration-test"` |
| **version**  integer | The version of the dashboard.  **Returned:** state is present and on success  **Sample:** `2` |

### Authors

- Ishan Jain (@ishanjainn)

### Collection links

- [Issue Tracker](https://github.com/grafana/grafana-ansible-collection/issues)
- [Repository (Sources)](https://github.com/grafana/grafana-ansible-collection)
