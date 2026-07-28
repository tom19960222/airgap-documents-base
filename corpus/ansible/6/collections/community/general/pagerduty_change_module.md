---
collection: ansible
version: "6"
title: "community.general.pagerduty_change module – Track a code or infrastructure change as a PagerDuty change event"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/pagerduty_change_module.html
fetched_at: 2026-07-27T17:11:46+00:00
---
# community.general.pagerduty_change module – Track a code or infrastructure change as a PagerDuty change event

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](pagerduty_change_module.md#ansible-collections-community-general-pagerduty-change-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.pagerduty_change`.

New in community.general 1.3.0

- [Synopsis](pagerduty_change_module.md#synopsis)
- [Requirements](pagerduty_change_module.md#requirements)
- [Parameters](pagerduty_change_module.md#parameters)
- [Notes](pagerduty_change_module.md#notes)
- [Examples](pagerduty_change_module.md#examples)

## [Synopsis](pagerduty_change_module.md#id1)

- This module will let you create a PagerDuty change event each time the module is run.
- This is not an idempotent action and a new change event will be created each time it is run.

## [Requirements](pagerduty_change_module.md#id2)

The below requirements are needed on the host that executes this module.

- PagerDuty integration key

## [Parameters](pagerduty_change_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **environment**  string | The environment name, typically `production`, `staging`, etc. |
| **integration_key**  string / required | The integration key that identifies the service the change was made to. This can be found by adding an integration to a service in PagerDuty. |
| **link_text**  string | Descriptive text for a URL where more information about the deployment can be obtained. |
| **link_url**  string | A URL where more information about the deployment can be obtained. |
| **repo**  string | The URL of the project repository. |
| **revision**  string | An identifier of the revision being deployed, typically a number or SHA from a version control system. |
| **source**  string | The source of the change event.  Default: `"Ansible"` |
| **summary**  string / required | A short description of the change that occurred. |
| **url**  string | URL to submit the change event to.  Default: `"https://events.pagerduty.com/v2/change/enqueue"` |
| **user**  string | The name of the user or process that triggered this deployment. |
| **validate_certs**  boolean | If `false`, SSL certificates for the target URL will not be validated. This should only be used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](pagerduty_change_module.md#id4)

> **Note:**
>
> - Supports `check_mode`. Note that check mode simply does nothing except returning `changed=true` in case the *url* seems to be correct.

## [Examples](pagerduty_change_module.md#id5)

```yaml+jinja
- name: Track the deployment as a PagerDuty change event
  community.general.pagerduty_change:
    integration_key: abc123abc123abc123abc123abc123ab
    summary: The application was deployed

- name: Track the deployment as a PagerDuty change event with more details
  community.general.pagerduty_change:
    integration_key: abc123abc123abc123abc123abc123ab
    summary: The application was deployed
    source: Ansible Deploy
    user: ansible
    repo: github.com/ansible/ansible
    revision: '4.2'
    environment: production
    link_url: https://github.com/ansible-collections/community.general/pull/1269
    link_text: View changes on GitHub
```

### Authors

- Adam Vaughan (@adamvaughan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
