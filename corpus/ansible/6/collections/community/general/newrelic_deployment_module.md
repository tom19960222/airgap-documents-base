---
collection: ansible
version: "6"
title: "community.general.newrelic_deployment module – Notify New Relic about app deployments"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/newrelic_deployment_module.html
fetched_at: 2026-07-27T17:11:03+00:00
---
# community.general.newrelic_deployment module – Notify New Relic about app deployments

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
> To use it in a playbook, specify: `community.general.newrelic_deployment`.

- [Synopsis](newrelic_deployment_module.md#synopsis)
- [Parameters](newrelic_deployment_module.md#parameters)
- [Examples](newrelic_deployment_module.md#examples)

## [Synopsis](newrelic_deployment_module.md#id1)

- Notify New Relic about app deployments (see <https://docs.newrelic.com/docs/apm/new-relic-apm/maintenance/record-monitor-deployments/>)

## [Parameters](newrelic_deployment_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **app_name**  string | The value of app_name in the newrelic.yml file used by the application.  One of *app_name* or *application_id* is required. |
| **application_id**  string | The application ID found in the metadata of the application in APM.  One of *app_name* or *application_id* is required. |
| **appname**  string | Name of the application.  This option has been deprecated and will be removed in community.general 7.0.0. Please do not use. |
| **changelog**  string | A list of changes for this deployment |
| **description**  string | Text annotation for the deployment - notes for you |
| **environment**  string | The environment for this deployment.  This option has been deprecated and will be removed community.general 7.0.0. Please do not use. |
| **revision**  string / required | A revision number (e.g., git commit SHA) |
| **token**  string / required | API token to place in the Api-Key header. |
| **user**  string | The name of the user/process that triggered this deployment |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Examples](newrelic_deployment_module.md#id3)

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

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
