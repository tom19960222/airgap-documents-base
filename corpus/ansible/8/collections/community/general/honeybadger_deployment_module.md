---
collection: ansible
version: "8"
title: "community.general.honeybadger_deployment module – Notify Honeybadger.io about app deployments"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/honeybadger_deployment_module.html
fetched_at: 2026-07-28T01:46:03+00:00
---
# community.general.honeybadger_deployment module – Notify Honeybadger.io about app deployments

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
> To use it in a playbook, specify: `community.general.honeybadger_deployment`.

- [Synopsis](honeybadger_deployment_module.md#synopsis)
- [Parameters](honeybadger_deployment_module.md#parameters)
- [Attributes](honeybadger_deployment_module.md#attributes)
- [Examples](honeybadger_deployment_module.md#examples)

## [Synopsis](honeybadger_deployment_module.md#id1)

- Notify Honeybadger.io about app deployments (see <http://docs.honeybadger.io/article/188-deployment-tracking>).

Aliases: monitoring.honeybadger_deployment

## [Parameters](honeybadger_deployment_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **environment**  string / required | The environment name, typically ‘production’, ‘staging’, etc. |
| **repo**  string | URL of the project repository |
| **revision**  string | A hash, number, tag, or other identifier showing what revision was deployed |
| **token**  string / required | API token. |
| **url**  string | Optional URL to submit the notification to.  **Default:** `"https://api.honeybadger.io/v1/deploys"` |
| **user**  string | The username of the person doing the deployment |
| **validate_certs**  boolean | If `false`, SSL certificates for the target url will not be validated. This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](honeybadger_deployment_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](honeybadger_deployment_module.md#id4)

```yaml+jinja
- name: Notify Honeybadger.io about an app deployment
  community.general.honeybadger_deployment:
    token: AAAAAA
    environment: staging
    user: ansible
    revision: b6826b8
    repo: 'git@github.com:user/repo.git'
```

### Authors

- Benjamin Curtis (@stympy)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
