---
collection: ansible
version: "8"
title: "community.general.pagerduty_user module – Manage a user account on PagerDuty"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/pagerduty_user_module.html
fetched_at: 2026-07-28T01:48:56+00:00
---
# community.general.pagerduty_user module – Manage a user account on PagerDuty

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](pagerduty_user_module.md#ansible-collections-community-general-pagerduty-user-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.pagerduty_user`.

New in community.general 1.3.0

- [Synopsis](pagerduty_user_module.md#synopsis)
- [Requirements](pagerduty_user_module.md#requirements)
- [Parameters](pagerduty_user_module.md#parameters)
- [Attributes](pagerduty_user_module.md#attributes)
- [Examples](pagerduty_user_module.md#examples)

## [Synopsis](pagerduty_user_module.md#id1)

- This module manages the creation/removal of a user account on PagerDuty.

Aliases: monitoring.pagerduty_user

## [Requirements](pagerduty_user_module.md#id2)

The below requirements are needed on the host that executes this module.

- pdpyras python module = 4.1.1
- PagerDuty API Access

## [Parameters](pagerduty_user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string / required | An API access token to authenticate with the PagerDuty REST API. |
| **pd_email**  string / required | The user’s email address.  `pd_email` is the unique identifier used and cannot be updated using this module. |
| **pd_role**  string | The user’s role.  **Choices:**   - `"global_admin"` - `"manager"` - `"responder"` ← (default) - `"observer"` - `"stakeholder"` - `"limited_stakeholder"` - `"restricted_access"` |
| **pd_teams**  list / elements=string | The teams to which the user belongs.  Required if `state=present`. |
| **pd_user**  string / required | Name of the user in PagerDuty. |
| **state**  string | State of the user.  On `present`, it creates a user if the user doesn’t exist.  On `absent`, it removes a user if the account exists.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Attributes](pagerduty_user_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](pagerduty_user_module.md#id5)

```yaml+jinja
- name: Create a user account on PagerDuty
  community.general.pagerduty_user:
    access_token: 'Your_Access_token'
    pd_user: user_full_name
    pd_email: user_email
    pd_role: user_pd_role
    pd_teams: user_pd_teams
    state: "present"

- name: Remove a user account from PagerDuty
  community.general.pagerduty_user:
    access_token: 'Your_Access_token'
    pd_user: user_full_name
    pd_email: user_email
    state: "absent"
```

### Authors

- Zainab Alsaffar (@zanssa)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
