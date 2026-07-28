---
collection: ansible
version: "8"
title: "grafana.grafana.cloud_stack module – Manage Grafana Cloud stack"
source_url: https://docs.ansible.com/projects/ansible/8/collections/grafana/grafana/cloud_stack_module.html
fetched_at: 2026-07-28T02:33:52+00:00
---
# grafana.grafana.cloud_stack module – Manage Grafana Cloud stack

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
> see [Requirements](cloud_stack_module.md#ansible-collections-grafana-grafana-cloud-stack-module-requirements) for details.
>
> To use it in a playbook, specify: `grafana.grafana.cloud_stack`.

New in grafana.grafana 0.0.1

- [Synopsis](cloud_stack_module.md#synopsis)
- [Requirements](cloud_stack_module.md#requirements)
- [Parameters](cloud_stack_module.md#parameters)
- [Notes](cloud_stack_module.md#notes)
- [Examples](cloud_stack_module.md#examples)
- [Return Values](cloud_stack_module.md#return-values)

## [Synopsis](cloud_stack_module.md#id1)

- Create and delete Grafana Cloud stacks using Ansible.

## [Requirements](cloud_stack_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests >= 1.0.0

## [Parameters](cloud_stack_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cloud_api_key**  string / required | Cloud API Key to authenticate with Grafana Cloud. |
| **name**  string / required | Sets the name of stack. Conventionally matches the URL of the instance. For example, `stackslug.grafana.net`. |
| **org_slug**  string / required | Name of the organization under which Cloud stack is created. |
| **region**  string | Sets the region for the Grafana Cloud stack.  **Choices:**   - `"us"` ← (default) - `"us-azure"` - `"eu"` - `"au"` - `"eu-azure"` - `"prod-ap-southeast-0"` - `"prod-gb-south-0"` - `"prod-eu-west-3"` |
| **stack_slug**  string / required | Sets the subdomain of the Grafana instance. For example, if slug is **stackslug**, the instance URL will be `https://stackslug.grafana.net`. |
| **state**  string | State for the Grafana Cloud stack.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **url**  string | If you use a custom domain for the instance, you can provide it here. If not provided, Will be set to `https://stackslug.grafana.net`. |

## [Notes](cloud_stack_module.md#id4)

> **Note:**
>
> - Does not support `check_mode`.

## [Examples](cloud_stack_module.md#id5)

```yaml+jinja
- name: Create a Grafana Cloud stack
  grafana.grafana.cloud_stack:
    name: stack_name
    stack_slug: stack_name
    cloud_api_key: "{{ grafana_cloud_api_key }}"
    region: eu
    url: https://grafana.company_name.com
    org_slug: org_name
    state: present

- name: Delete a Grafana Cloud stack
  grafana.grafana.cloud_stack:
    name: stack_name
    slug: stack_name
    cloud_api_key: "{{ grafana_cloud_api_key }}"
    org_slug: org_name
    state: absent
```

## [Return Values](cloud_stack_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **alertmanager_name**  string | Name of the alertmanager instance.  **Returned:** always  **Sample:** `"stackname-alerts"` |
| **alertmanager_url**  string | URL of the alertmanager instance.  **Returned:** always  **Sample:** `"https://alertmanager-eu-west-0.grafana.net"` |
| **cluster_slug**  string | Slug for the cluster where the Grafana stack is deployed.  **Returned:** always  **Sample:** `"prod-eu-west-0"` |
| **id**  integer | ID of the Grafana Cloud stack.  **Returned:** always  **Sample:** `458182` |
| **loki_url**  string | URl for the Loki instance.  **Returned:** always  **Sample:** `"https://logs-prod-eu-west-0.grafana.net"` |
| **orgID**  integer | ID of the Grafana Cloud organization.  **Returned:** always  **Sample:** `652992` |
| **prometheus_url**  string | URl for the Prometheus instance.  **Returned:** always  **Sample:** `"https://prometheus-prod-01-eu-west-0.grafana.net"` |
| **tempo_url**  string | URl for the Tempo instance.  **Returned:** always  **Sample:** `"https://tempo-eu-west-0.grafana.net"` |
| **url**  string | URL of the Grafana Cloud stack.  **Returned:** always  **Sample:** `"https://stackname.grafana.net"` |

### Authors

- Ishan Jain (@ishanjainn)

### Collection links

- [Issue Tracker](https://github.com/grafana/grafana-ansible-collection/issues)
- [Repository (Sources)](https://github.com/grafana/grafana-ansible-collection)
