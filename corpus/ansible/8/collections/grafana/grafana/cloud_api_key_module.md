---
collection: ansible
version: "8"
title: "grafana.grafana.cloud_api_key module – Manage Grafana Cloud API keys"
source_url: https://docs.ansible.com/projects/ansible/8/collections/grafana/grafana/cloud_api_key_module.html
fetched_at: 2026-07-28T02:33:49+00:00
---
# grafana.grafana.cloud_api_key module – Manage Grafana Cloud API keys

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
> see [Requirements](cloud_api_key_module.md#ansible-collections-grafana-grafana-cloud-api-key-module-requirements) for details.
>
> To use it in a playbook, specify: `grafana.grafana.cloud_api_key`.

New in grafana.grafana 0.0.1

- [Synopsis](cloud_api_key_module.md#synopsis)
- [Requirements](cloud_api_key_module.md#requirements)
- [Parameters](cloud_api_key_module.md#parameters)
- [Notes](cloud_api_key_module.md#notes)
- [Examples](cloud_api_key_module.md#examples)

## [Synopsis](cloud_api_key_module.md#id1)

- Create and delete Grafana Cloud API keys using Ansible.

## [Requirements](cloud_api_key_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests >= 1.0.0

## [Parameters](cloud_api_key_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **existing_cloud_api_key**  string / required | Cloud API Key to authenticate with Grafana Cloud. |
| **fail_if_already_created**  boolean | If set to `true`, the task will fail if the API key with same name already exists in the Organization.  **Choices:**   - `false` - `true` ← (default) |
| **name**  string / required | Sets the name of the Grafana Cloud API key. |
| **org_slug**  string / required | Name of the Grafana Cloud organization in which Cloud API key will be created. |
| **role**  string / required | Sets the role to be associated with the Cloud API key.  **Choices:**   - `"Admin"` - `"Viewer"` - `"Editor"` - `"MetricsPublisher"` |
| **state**  string | State for the Grafana Cloud API Key.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](cloud_api_key_module.md#id4)

> **Note:**
>
> - Does not support `check_mode`.

## [Examples](cloud_api_key_module.md#id5)

```yaml+jinja
- name: Create Grafana Cloud API key
  grafana.grafana.cloud_api_key:
    name: key_name
    role: Admin
    org_slug: "{{ org_slug }}"
    existing_cloud_api_key: "{{ grafana_cloud_api_key }}"
    fail_if_already_created: False
    state: present

- name: Delete Grafana Cloud API key
  grafana.grafana.cloud_api_key:
    name: key_name
    org_slug: "{{ org_slug }}"
    existing_cloud_api_key: "{{ grafana_cloud_api_key }}"
    state: absent
```

### Authors

- Ishan Jain (@ishanjainn)

### Collection links

- [Issue Tracker](https://github.com/grafana/grafana-ansible-collection/issues)
- [Repository (Sources)](https://github.com/grafana/grafana-ansible-collection)
