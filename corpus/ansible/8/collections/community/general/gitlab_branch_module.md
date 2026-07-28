---
collection: ansible
version: "8"
title: "community.general.gitlab_branch module – Create or delete a branch"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/gitlab_branch_module.html
fetched_at: 2026-07-28T01:45:45+00:00
---
# community.general.gitlab_branch module – Create or delete a branch

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
> see [Requirements](gitlab_branch_module.md#ansible-collections-community-general-gitlab-branch-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.gitlab_branch`.

New in community.general 4.2.0

- [Synopsis](gitlab_branch_module.md#synopsis)
- [Requirements](gitlab_branch_module.md#requirements)
- [Parameters](gitlab_branch_module.md#parameters)
- [Attributes](gitlab_branch_module.md#attributes)
- [Examples](gitlab_branch_module.md#examples)

## [Synopsis](gitlab_branch_module.md#id1)

- This module allows to create or delete branches.

Aliases: source_control.gitlab.gitlab_branch

## [Requirements](gitlab_branch_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- python-gitlab >= 2.3.0
- requests (Python library <https://pypi.org/project/requests/>)

## [Parameters](gitlab_branch_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_job_token**  string  *added in community.general 4.2.0* | GitLab CI job token for logging in. |
| **api_oauth_token**  string  *added in community.general 4.2.0* | GitLab OAuth token for logging in. |
| **api_password**  string | The password to use for authentication against the API |
| **api_token**  string | GitLab access token with API permissions. |
| **api_url**  string | The resolvable endpoint for the API |
| **api_username**  string | The username to use for authentication against the API |
| **branch**  string / required | The name of the branch that needs to be created. |
| **project**  string / required | The path or name of the project. |
| **ref_branch**  string | Reference branch to create from.  This must be specified if `state=present`. |
| **state**  string | Create or delete branch.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | Whether or not to validate SSL certs when supplying a https endpoint.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](gitlab_branch_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](gitlab_branch_module.md#id5)

```yaml+jinja
- name: Create branch branch2 from main
  community.general.gitlab_branch:
    api_url: https://gitlab.com
    api_token: secret_access_token
    project: "group1/project1"
    branch: branch2
    ref_branch: main
    state: present

- name: Delete branch branch2
  community.general.gitlab_branch:
    api_url: https://gitlab.com
    api_token: secret_access_token
    project: "group1/project1"
    branch: branch2
    state: absent
```

### Authors

- paytroff (@paytroff)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
