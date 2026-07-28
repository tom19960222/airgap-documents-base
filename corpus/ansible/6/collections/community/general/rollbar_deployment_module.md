---
collection: ansible
version: "6"
title: "community.general.rollbar_deployment module – Notify Rollbar about app deployments"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/rollbar_deployment_module.html
fetched_at: 2026-07-27T17:12:46+00:00
---
# community.general.rollbar_deployment module – Notify Rollbar about app deployments

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.rollbar_deployment`.

- [Synopsis](rollbar_deployment_module.md#synopsis)
- [Parameters](rollbar_deployment_module.md#parameters)
- [Examples](rollbar_deployment_module.md#examples)

## [Synopsis](rollbar_deployment_module.md#id1)

- Notify Rollbar about app deployments (see <https://rollbar.com/docs/deploys_other/>)

## [Parameters](rollbar_deployment_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **comment**  string | Deploy comment (e.g. what is being deployed). |
| **environment**  string / required | Name of the environment being deployed, e.g. ‘production’. |
| **revision**  string / required | Revision number/sha being deployed. |
| **rollbar_user**  string | Rollbar username of the user who deployed. |
| **token**  string / required | Your project access token. |
| **url**  string | Optional URL to submit the notification to.  Default: `"https://api.rollbar.com/api/1/deploy/"` |
| **user**  string | User who deployed. |
| **validate_certs**  boolean | If `false`, SSL certificates for the target url will not be validated. This should only be used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Examples](rollbar_deployment_module.md#id3)

```yaml+jinja
- name: Rollbar deployment notification
  community.general.rollbar_deployment:
  token: AAAAAA
  environment: staging
  user: ansible
  revision: '4.2'
  rollbar_user: admin
  comment: Test Deploy

- name: Notify rollbar about current git revision deployment by current user
  community.general.rollbar_deployment:
  token: "{{ rollbar_access_token }}"
  environment: production
  revision: "{{ lookup('pipe', 'git rev-parse HEAD') }}"
  user: "{{ lookup('env', 'USER') }}"
```

### Authors

- Max Riveiro (@kavu)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
