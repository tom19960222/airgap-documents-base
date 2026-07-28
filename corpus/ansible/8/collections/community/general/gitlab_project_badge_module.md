---
collection: ansible
version: "8"
title: "community.general.gitlab_project_badge module – Manage project badges on GitLab Server"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/gitlab_project_badge_module.html
fetched_at: 2026-07-28T01:45:52+00:00
---
# community.general.gitlab_project_badge module – Manage project badges on GitLab Server

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
> see [Requirements](gitlab_project_badge_module.md#ansible-collections-community-general-gitlab-project-badge-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.gitlab_project_badge`.

New in community.general 6.1.0

- [Synopsis](gitlab_project_badge_module.md#synopsis)
- [Requirements](gitlab_project_badge_module.md#requirements)
- [Parameters](gitlab_project_badge_module.md#parameters)
- [Attributes](gitlab_project_badge_module.md#attributes)
- [Examples](gitlab_project_badge_module.md#examples)
- [Return Values](gitlab_project_badge_module.md#return-values)

## [Synopsis](gitlab_project_badge_module.md#id1)

- This module allows to add and remove badges to/from a project.

## [Requirements](gitlab_project_badge_module.md#id2)

The below requirements are needed on the host that executes this module.

- `owner` or `maintainer` rights to project on the GitLab server
- requests (Python library <https://pypi.org/project/requests/>)

## [Parameters](gitlab_project_badge_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_job_token**  string  *added in community.general 4.2.0* | GitLab CI job token for logging in. |
| **api_oauth_token**  string  *added in community.general 4.2.0* | GitLab OAuth token for logging in. |
| **api_password**  string | The password to use for authentication against the API |
| **api_token**  string | GitLab access token with API permissions. |
| **api_url**  string | The resolvable endpoint for the API |
| **api_username**  string | The username to use for authentication against the API |
| **image_url**  string / required | The image URL of the badge.  A badge is identified by this URL. |
| **link_url**  string / required | The URL associated with the badge. |
| **project**  string / required | The name (or full path) of the GitLab project the badge is added to/removed from. |
| **state**  string | State of the badge in the project.  On `present`, it adds a badge to a GitLab project.  On `absent`, it removes a badge from a GitLab project.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | Whether or not to validate SSL certs when supplying a https endpoint.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](gitlab_project_badge_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](gitlab_project_badge_module.md#id5)

```yaml+jinja
- name: Add a badge to a GitLab Project
  community.general.gitlab_project_badge:
    api_url: 'https://example.gitlab.com'
    api_token: 'Your-Private-Token'
    project: projectname
    state: present
    link_url: 'https://example.gitlab.com/%{project_path}'
    image_url: 'https://example.gitlab.com/%{project_path}/badges/%{default_branch}/pipeline.svg'

- name: Remove a badge from a GitLab Project
  community.general.gitlab_project_badge:
    api_url: 'https://example.gitlab.com'
    api_token: 'Your-Private-Token'
    project: projectname
    state: absent
    link_url: 'https://example.gitlab.com/%{project_path}'
    image_url: 'https://example.gitlab.com/%{project_path}/badges/%{default_branch}/pipeline.svg'
```

## [Return Values](gitlab_project_badge_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **badge**  dictionary | The badge information.  **Returned:** when `state=present`  **Sample:** `{"id": 1, "image_url": "https://shields.io/my/badge", "kind": "project", "link_url": "http://example.com/ci_status.svg?project=%{project_path}&ref=%{default_branch}", "rendered_image_url": "https://shields.io/my/badge", "rendered_link_url": "http://example.com/ci_status.svg?project=example-org/example-project&ref=master"}` |

### Authors

- Guillaume MARTINEZ (@Lunik)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
