---
collection: ansible
version: "6"
title: "community.general.pagerduty module – Create PagerDuty maintenance windows"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/pagerduty_module.html
fetched_at: 2026-07-27T17:11:45+00:00
---
# community.general.pagerduty module – Create PagerDuty maintenance windows

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
> see [Requirements](pagerduty_module.md#ansible-collections-community-general-pagerduty-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.pagerduty`.

- [Synopsis](pagerduty_module.md#synopsis)
- [Requirements](pagerduty_module.md#requirements)
- [Parameters](pagerduty_module.md#parameters)
- [Examples](pagerduty_module.md#examples)

## [Synopsis](pagerduty_module.md#id1)

- This module will let you create PagerDuty maintenance windows

## [Requirements](pagerduty_module.md#id2)

The below requirements are needed on the host that executes this module.

- PagerDuty API access

## [Parameters](pagerduty_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **desc**  string | Short description of maintenance window.  Default: `"Created by Ansible"` |
| **hours**  string | Length of maintenance window in hours.  Default: `"1"` |
| **minutes**  string | Maintenance window in minutes (this is added to the hours).  Default: `"0"` |
| **name**  string | PagerDuty unique subdomain. Obsolete. It is not used with PagerDuty REST v2 API. |
| **requester_id**  string | ID of user making the request. Only needed when creating a maintenance_window. |
| **service**  aliases: services  list / elements=string | A comma separated list of PagerDuty service IDs. |
| **state**  string / required | Create a maintenance window or get a list of ongoing windows.  Choices:   - `"running"` - `"started"` - `"ongoing"` - `"absent"` |
| **token**  string / required | A pagerduty token, generated on the pagerduty site. It is used for authorization. |
| **user**  string | PagerDuty user ID. Obsolete. Please, use *token* for authorization. |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **window_id**  string | ID of maintenance window. Only needed when absent a maintenance_window. |

## [Examples](pagerduty_module.md#id4)

```yaml+jinja
- name: List ongoing maintenance windows using a token
  community.general.pagerduty:
    name: companyabc
    token: xxxxxxxxxxxxxx
    state: ongoing

- name: Create a 1 hour maintenance window for service FOO123
  community.general.pagerduty:
    name: companyabc
    user: example@example.com
    token: yourtoken
    state: running
    service: FOO123

- name: Create a 5 minute maintenance window for service FOO123
  community.general.pagerduty:
    name: companyabc
    token: xxxxxxxxxxxxxx
    hours: 0
    minutes: 5
    state: running
    service: FOO123

- name: Create a 4 hour maintenance window for service FOO123 with the description "deployment"
  community.general.pagerduty:
    name: companyabc
    user: example@example.com
    state: running
    service: FOO123
    hours: 4
    desc: deployment
  register: pd_window

- name: Delete the previous maintenance window
  community.general.pagerduty:
    name: companyabc
    user: example@example.com
    state: absent
    window_id: '{{ pd_window.result.maintenance_window.id }}'

# Delete a maintenance window from a separate playbook than its creation,
# and if it is the only existing maintenance window
- name: Check
  community.general.pagerduty:
    requester_id: XXXXXXX
    token: yourtoken
    state: ongoing
  register: pd_window

- name: Delete
  community.general.pagerduty:
    requester_id: XXXXXXX
    token: yourtoken
    state: absent
    window_id: "{{ pd_window.result.maintenance_windows[0].id }}"
```

### Authors

- Andrew Newdigate (@suprememoocow)
- Dylan Silva (@thaumos)
- Justin Johns
- Bruce Pennypacker (@bpennypacker)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
