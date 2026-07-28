---
collection: ansible
version: "8"
title: "community.general.scaleway_lb module – Scaleway load-balancer management module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/scaleway_lb_module.html
fetched_at: 2026-07-28T01:50:19+00:00
---
# community.general.scaleway_lb module – Scaleway load-balancer management module

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
> To use it in a playbook, specify: `community.general.scaleway_lb`.

- [Synopsis](scaleway_lb_module.md#synopsis)
- [Parameters](scaleway_lb_module.md#parameters)
- [Attributes](scaleway_lb_module.md#attributes)
- [Notes](scaleway_lb_module.md#notes)
- [Examples](scaleway_lb_module.md#examples)

## [Synopsis](scaleway_lb_module.md#id1)

- This module manages load-balancers on Scaleway.

Aliases: cloud.scaleway.scaleway_lb

## [Parameters](scaleway_lb_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  aliases: timeout  integer | HTTP timeout to Scaleway API in seconds.  **Default:** `30` |
| **api_token**  aliases: oauth_token  string / required | Scaleway OAuth token. |
| **api_url**  aliases: base_url  string | Scaleway API URL.  **Default:** `"https://api.scaleway.com"` |
| **description**  string / required | Description of the load-balancer. |
| **name**  string / required | Name of the load-balancer. |
| **organization_id**  string / required | Organization identifier. |
| **query_parameters**  dictionary | List of parameters passed to the query string.  **Default:** `{}` |
| **region**  string / required | Scaleway zone.  **Choices:**   - `"nl-ams"` - `"fr-par"` - `"pl-waw"` |
| **state**  string | Indicate desired state of the instance.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=string | List of tags to apply to the load-balancer.  **Default:** `[]` |
| **validate_certs**  boolean | Validate SSL certs of the Scaleway API.  **Choices:**   - `false` - `true` ← (default) |
| **wait**  boolean | Wait for the load-balancer to reach its desired state before returning.  **Choices:**   - `false` ← (default) - `true` |
| **wait_sleep_time**  integer | Time to wait before every attempt to check the state of the load-balancer.  **Default:** `3` |
| **wait_timeout**  integer | Time to wait for the load-balancer to reach the expected state.  **Default:** `300` |

## [Attributes](scaleway_lb_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](scaleway_lb_module.md#id4)

> **Note:**
>
> - Also see the API documentation on <https://developer.scaleway.com/>
> - If `api_token` is not set within the module, the following environment variables can be used in decreasing order of precedence [`SCW_TOKEN`](../../environment_variables.md#envvar-SCW_TOKEN), [`SCW_API_KEY`](../../environment_variables.md#envvar-SCW_API_KEY), [`SCW_OAUTH_TOKEN`](../../environment_variables.md#envvar-SCW_OAUTH_TOKEN) or `SCW_API_TOKEN`.
> - If one wants to use a different `api_url` one can also set the `SCW_API_URL` environment variable.

## [Examples](scaleway_lb_module.md#id5)

```yaml+jinja
- name: Create a load-balancer
  community.general.scaleway_lb:
    name: foobar
    state: present
    organization_id: 951df375-e094-4d26-97c1-ba548eeb9c42
    region: fr-par
    tags:
      - hello

- name: Delete a load-balancer
  community.general.scaleway_lb:
    name: foobar
    state: absent
    organization_id: 951df375-e094-4d26-97c1-ba548eeb9c42
    region: fr-par
```

### Authors

- Remy Leone (@remyleone)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
