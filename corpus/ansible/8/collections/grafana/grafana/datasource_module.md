---
collection: ansible
version: "8"
title: "grafana.grafana.datasource module – Manage Data sources in Grafana"
source_url: https://docs.ansible.com/projects/ansible/8/collections/grafana/grafana/datasource_module.html
fetched_at: 2026-07-28T02:33:53+00:00
---
# grafana.grafana.datasource module – Manage Data sources in Grafana

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
> see [Requirements](datasource_module.md#ansible-collections-grafana-grafana-datasource-module-requirements) for details.
>
> To use it in a playbook, specify: `grafana.grafana.datasource`.

New in grafana.grafana 0.0.1

- [Synopsis](datasource_module.md#synopsis)
- [Requirements](datasource_module.md#requirements)
- [Parameters](datasource_module.md#parameters)
- [Notes](datasource_module.md#notes)
- [Examples](datasource_module.md#examples)
- [Return Values](datasource_module.md#return-values)

## [Synopsis](datasource_module.md#id1)

- Create, Update and delete Data sources using Ansible.

## [Requirements](datasource_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests >= 1.0.0

## [Parameters](datasource_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dataSource**  dictionary / required | JSON source code for the Data source. |
| **grafana_api_key**  string / required | Grafana API Key to authenticate with Grafana Cloud. |
| **grafana_url**  string / required | URL of the Grafana instance. |
| **state**  string | State for the Grafana Datasource.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](datasource_module.md#id4)

> **Note:**
>
> - Does not support `check_mode`.
> - Does not support `Idempotency`.

## [Examples](datasource_module.md#id5)

```yaml+jinja
- name: Create/Update Data sources
  grafana.grafana.datasource:
    dataSource: |
      {
        "name": "Prometheus",
        "type": "prometheus",
        "access": "proxy",
        "url": "http://localhost:9090",
        "jsonData": {
          "httpMethod": "POST",
          "manageAlerts": true,
          "prometheusType": "Prometheus",
          "cacheLevel": "High"
        }
      }
    grafana_url: "{{ grafana_url }}"
    grafana_api_key: "{{ grafana_api_key }}"
    state: present

- name: Delete Data sources
  grafana.grafana.datasource:
    dataSource: "{{ lookup('ansible.builtin.file', 'datasource.json') }}"
    grafana_url: "{{ grafana_url }}"
    grafana_api_key: "{{ grafana_api_key }}"
    state: absent
```

## [Return Values](datasource_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **output**  dictionary | Dict object containing Data source information.  **Returned:** On success |
| **datasource**  dictionary | The response body content for the data source configuration.  **Returned:** state is present and on success  **Sample:** `{"access": "proxy", "basicAuth": false, "basicAuthUser": "", "database": "db-name", "id": 20, "isDefault": false, "jsonData": {}, "name": "ansible-integration", "orgId": 1, "readOnly": false, "secureJsonFields": {"password": true}, "type": "influxdb", "typeLogoUrl": "", "uid": "ansibletest", "url": "https://grafana.github.com/grafana-ansible-collection", "user": "user", "version": 1, "withCredentials": false}` |
| **id**  integer | The ID assigned to the data source.  **Returned:** on success  **Sample:** `20` |
| **message**  string | The message returned after the operation on the Data source.  **Returned:** on success  **Sample:** `"Datasource added"` |
| **name**  string | The name of the data source defined in the JSON source code.  **Returned:** state is present and on success  **Sample:** `"ansible-integration"` |

### Authors

- Ishan Jain (@ishanjainn)

### Collection links

- [Issue Tracker](https://github.com/grafana/grafana-ansible-collection/issues)
- [Repository (Sources)](https://github.com/grafana/grafana-ansible-collection)
