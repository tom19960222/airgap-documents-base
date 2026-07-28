---
collection: ansible
version: "6"
title: "community.general.github_issue module – View GitHub issue"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/github_issue_module.html
fetched_at: 2026-07-27T17:09:01+00:00
---
# community.general.github_issue module – View GitHub issue

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
> To use it in a playbook, specify: `community.general.github_issue`.

- [Synopsis](github_issue_module.md#synopsis)
- [Parameters](github_issue_module.md#parameters)
- [Examples](github_issue_module.md#examples)
- [Return Values](github_issue_module.md#return-values)

## [Synopsis](github_issue_module.md#id1)

- View GitHub issue for a given repository and organization.

## [Parameters](github_issue_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **action**  string | Get various details about issue depending upon action specified.  Choices:   - `"get_status"` ← (default) |
| **issue**  integer / required | Issue number for which information is required. |
| **organization**  string / required | Name of the GitHub organization in which the repository is hosted. |
| **repo**  string / required | Name of repository from which issue needs to be retrieved. |

## [Examples](github_issue_module.md#id3)

```yaml+jinja
- name: Check if GitHub issue is closed or not
  community.general.github_issue:
    organization: ansible
    repo: ansible
    issue: 23642
    action: get_status
  register: r

- name: Take action depending upon issue status
  ansible.builtin.debug:
    msg: Do something when issue 23642 is open
  when: r.issue_status == 'open'
```

## [Return Values](github_issue_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **issue_status**  string | State of the GitHub issue  Returned: success  Sample: `"open, closed"` |

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
