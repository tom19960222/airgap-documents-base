---
collection: ansible
version: "6"
title: "community.grafana.grafana_dashboard lookup – list or search grafana dashboards"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/grafana/grafana_dashboard_lookup.html
fetched_at: 2026-07-27T17:15:31+00:00
---
# community.grafana.grafana_dashboard lookup – list or search grafana dashboards

> **Note:**
>
> This lookup plugin is part of the [community.grafana collection](https://galaxy.ansible.com/community/grafana) (version 1.5.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.grafana`.
>
> To use it in a playbook, specify: `community.grafana.grafana_dashboard`.

- [Synopsis](grafana_dashboard_lookup.md#synopsis)
- [Keyword parameters](grafana_dashboard_lookup.md#keyword-parameters)
- [Examples](grafana_dashboard_lookup.md#examples)

## [Synopsis](grafana_dashboard_lookup.md#id1)

- This lookup returns a list of grafana dashboards with possibility to filter them by query.

## [Keyword parameters](grafana_dashboard_lookup.md#id2)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.grafana.grafana_dashboard', key1=value1, key2=value2, ...)` and `query('community.grafana.grafana_dashboard', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **grafana_api_key**  string | Grafana API key.  When `grafana_api_key` is set, the options `grafana_user`, `grafana_password` and `grafana_org_id` are ignored.  Configuration:   - Environment variable: [`GRAFANA_API_KEY`](../../environment_variables.md#envvar-GRAFANA_API_KEY) |
| **grafana_org_id**  string | grafana organisation id.  Default: `1`  Configuration:   - Environment variable: [`GRAFANA_ORG_ID`](../../environment_variables.md#envvar-GRAFANA_ORG_ID) |
| **grafana_password**  string | grafana authentication password.  Default: `"admin"`  Configuration:   - Environment variable: [`GRAFANA_PASSWORD`](../../environment_variables.md#envvar-GRAFANA_PASSWORD) |
| **grafana_url**  string | url of grafana.  Default: `"http://127.0.0.1:3000"`  Configuration:   - Environment variable: [`GRAFANA_URL`](../../environment_variables.md#envvar-GRAFANA_URL) |
| **grafana_user**  string | grafana authentication user.  Default: `"admin"`  Configuration:   - Environment variable: [`GRAFANA_USER`](../../environment_variables.md#envvar-GRAFANA_USER) |
| **search**  string | optional filter for dashboard search.  Configuration:   - Environment variable: [`GRAFANA_DASHBOARD_SEARCH`](../../environment_variables.md#envvar-GRAFANA_DASHBOARD_SEARCH) |

## [Examples](grafana_dashboard_lookup.md#id3)

```yaml+jinja
- name: get project foo grafana dashboards
  set_fact:
    grafana_dashboards: "{{ lookup('grafana_dashboard', 'grafana_url=http://grafana.company.com grafana_user=admin grafana_password=admin search=foo') }}"

- name: get all grafana dashboards
  set_fact:
    grafana_dashboards: "{{ lookup('grafana_dashboard', 'grafana_url=http://grafana.company.com grafana_api_key=' ~ grafana_api_key) }}"
```

### Authors

- Thierry Salle (@seuf)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/grafana/issues)
[Homepage](https://github.com/ansible-collections/grafana)
[Repository (Sources)](https://github.com/ansible-collections/grafana.git)
