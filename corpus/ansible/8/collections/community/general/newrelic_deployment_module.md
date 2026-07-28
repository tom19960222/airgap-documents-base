---
collection: ansible
version: "8"
title: "community.general.newrelic_deployment module – Notify New Relic about app deployments"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/newrelic_deployment_module.html
fetched_at: 2026-07-28T01:48:06+00:00
---
# community.general.newrelic_deployment module – Notify New Relic about app deployments

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
> To use it in a playbook, specify: `community.general.newrelic_deployment`.

- [Synopsis](newrelic_deployment_module.md#synopsis)
- [Parameters](newrelic_deployment_module.md#parameters)
- [Attributes](newrelic_deployment_module.md#attributes)
- [Examples](newrelic_deployment_module.md#examples)

## [Synopsis](newrelic_deployment_module.md#id1)

- Notify New Relic about app deployments (see <https://docs.newrelic.com/docs/apm/new-relic-apm/maintenance/record-monitor-deployments/>)

Aliases: monitoring.newrelic_deployment

## [Parameters](newrelic_deployment_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **app_name**  string | The value of `app_name` in the `newrelic.yml` file used by the application.  One of `app_name` or `application_id` is required. |
| **app_name_exact_match**  boolean  *added in community.general 7.5.0* | If this flag is set to `true` then the application ID lookup by name would only work for an exact match. If set to `false` it returns the first result.  **Choices:**   - `false` ← (default) - `true` |
| **application_id**  string | The application ID found in the metadata of the application in APM.  One of `app_name` or `application_id` is required. |
| **changelog**  string | A list of changes for this deployment |
| **description**  string | Text annotation for the deployment - notes for you |
| **revision**  string / required | A revision number (e.g., git commit SHA) |
| **token**  string / required | API token to place in the Api-Key header. |
| **user**  string | The name of the user/process that triggered this deployment |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](newrelic_deployment_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](newrelic_deployment_module.md#id4)

```yaml+jinja
- name:  Notify New Relic about an app deployment
  community.general.newrelic_deployment:
    token: AAAAAA
    app_name: myapp
    user: ansible deployment
    revision: '1.0'
```

### Authors

- Matt Coddington (@mcodd)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
