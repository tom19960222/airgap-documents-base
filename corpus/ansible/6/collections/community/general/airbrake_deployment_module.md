---
collection: ansible
version: "6"
title: "community.general.airbrake_deployment module – Notify airbrake about app deployments"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/airbrake_deployment_module.html
fetched_at: 2026-07-27T17:07:59+00:00
---
# community.general.airbrake_deployment module – Notify airbrake about app deployments

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
> To use it in a playbook, specify: `community.general.airbrake_deployment`.

- [Synopsis](airbrake_deployment_module.md#synopsis)
- [Parameters](airbrake_deployment_module.md#parameters)
- [Examples](airbrake_deployment_module.md#examples)

## [Synopsis](airbrake_deployment_module.md#id1)

- Notify airbrake about app deployments (see <https://airbrake.io/docs/api/#deploys-v4>).

## [Parameters](airbrake_deployment_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **environment**  string / required | The airbrake environment name, typically ‘production’, ‘staging’, etc. |
| **project_id**  string / required  added in community.general 0.2.0 | Airbrake PROJECT_ID |
| **project_key**  string / required  added in community.general 0.2.0 | Airbrake PROJECT_KEY. |
| **repo**  string | URL of the project repository |
| **revision**  string | A hash, number, tag, or other identifier showing what revision from version control was deployed |
| **url**  string | Optional URL to submit the notification to. Use to send notifications to Airbrake-compliant tools like Errbit.  Default: `"https://api.airbrake.io/api/v4/projects/"` |
| **user**  string | The username of the person doing the deployment |
| **validate_certs**  boolean | If `false`, SSL certificates for the target url will not be validated. This should only be used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **version**  string  added in community.general 1.0.0 | A string identifying what version was deployed |

## [Examples](airbrake_deployment_module.md#id3)

```yaml+jinja
- name: Notify airbrake about an app deployment
  community.general.airbrake_deployment:
    project_id: '12345'
    project_key: 'AAAAAA'
    environment: staging
    user: ansible
    revision: '4.2'

- name: Notify airbrake about an app deployment, using git hash as revision
  community.general.airbrake_deployment:
    project_id: '12345'
    project_key: 'AAAAAA'
    environment: staging
    user: ansible
    revision: 'e54dd3a01f2c421b558ef33b5f79db936e2dcf15'
    version: '0.2.0'
```

### Authors

- Bruce Pennypacker (@bpennypacker)
- Patrick Humpal (@phumpal)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
