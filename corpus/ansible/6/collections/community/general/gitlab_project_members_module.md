---
collection: ansible
version: "6"
title: "community.general.gitlab_project_members module – Manage project members on GitLab Server"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/gitlab_project_members_module.html
fetched_at: 2026-07-27T17:09:10+00:00
---
# community.general.gitlab_project_members module – Manage project members on GitLab Server

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
> see [Requirements](gitlab_project_members_module.md#ansible-collections-community-general-gitlab-project-members-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.gitlab_project_members`.

New in community.general 2.2.0

- [Synopsis](gitlab_project_members_module.md#synopsis)
- [Requirements](gitlab_project_members_module.md#requirements)
- [Parameters](gitlab_project_members_module.md#parameters)
- [Notes](gitlab_project_members_module.md#notes)
- [Examples](gitlab_project_members_module.md#examples)

## [Synopsis](gitlab_project_members_module.md#id1)

- This module allows to add and remove members to/from a project, or change a member’s access level in a project on GitLab.

## [Requirements](gitlab_project_members_module.md#id2)

The below requirements are needed on the host that executes this module.

- owner or maintainer rights to project on the GitLab server
- python-gitlab python module <= 1.15.0
- requests (Python library <https://pypi.org/project/requests/>)

## [Parameters](gitlab_project_members_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_level**  string | The access level for the user.  Required if *state=present*, user state is set to present.  Choices:   - `"guest"` - `"reporter"` - `"developer"` - `"maintainer"` |
| **api_job_token**  string  added in community.general 4.2.0 | GitLab CI job token for logging in. |
| **api_oauth_token**  string  added in community.general 4.2.0 | GitLab OAuth token for logging in. |
| **api_password**  string | The password to use for authentication against the API |
| **api_token**  string | GitLab access token with API permissions. |
| **api_url**  string | The resolvable endpoint for the API |
| **api_username**  string | The username to use for authentication against the API |
| **gitlab_user**  list / elements=string | A username or a list of usernames to add to/remove from the GitLab project.  Mutually exclusive with *gitlab_users_access*. |
| **gitlab_users_access**  list / elements=dictionary  added in community.general 3.7.0 | Provide a list of user to access level mappings.  Every dictionary in this list specifies a user (by username) and the access level the user should have.  Mutually exclusive with *gitlab_user* and *access_level*.  Use together with *purge_users* to remove all users not specified here from the project. |
| **access_level**  string / required | The access level for the user.  Required if *state=present*, user state is set to present.  Choices:   - `"guest"` - `"reporter"` - `"developer"` - `"maintainer"` |
| **name**  string / required | A username or a list of usernames to add to/remove from the GitLab project. |
| **project**  string / required | The name (or full path) of the GitLab project the member is added to/removed from. |
| **purge_users**  list / elements=string  added in community.general 3.7.0 | Adds/remove users of the given access_level to match the given *gitlab_user*/*gitlab_users_access* list. If omitted do not purge orphaned members.  Is only used when *state=present*.  Choices:   - `"guest"` - `"reporter"` - `"developer"` - `"maintainer"` |
| **state**  string | State of the member in the project.  On `present`, it adds a user to a GitLab project.  On `absent`, it removes a user from a GitLab project.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | Whether or not to validate SSL certs when supplying a https endpoint.  Choices:   - `false` - `true` ← (default) |

## [Notes](gitlab_project_members_module.md#id4)

> **Note:**
>
> - Supports `check_mode`.

## [Examples](gitlab_project_members_module.md#id5)

```yaml+jinja
- name: Add a user to a GitLab Project
  community.general.gitlab_project_members:
    api_url: 'https://gitlab.example.com'
    api_token: 'Your-Private-Token'
    validate_certs: true
    project: projectname
    gitlab_user: username
    access_level: developer
    state: present

- name: Remove a user from a GitLab project
  community.general.gitlab_project_members:
    api_url: 'https://gitlab.example.com'
    api_token: 'Your-Private-Token'
    validate_certs: false
    project: projectname
    gitlab_user: username
    state: absent

- name: Add a list of Users to A GitLab project
  community.general.gitlab_project_members:
    api_url: 'https://gitlab.example.com'
    api_token: 'Your-Private-Token'
    gitlab_project: projectname
    gitlab_user:
      - user1
      - user2
    access_level: developer
    state: present

- name: Add a list of Users with Dedicated Access Levels to A GitLab project
  community.general.gitlab_project_members:
    api_url: 'https://gitlab.example.com'
    api_token: 'Your-Private-Token'
    project: projectname
    gitlab_users_access:
      - name: user1
        access_level: developer
      - name: user2
        access_level: maintainer
    state: present

- name: Add a user, remove all others which might be on this access level
  community.general.gitlab_project_members:
    api_url: 'https://gitlab.example.com'
    api_token: 'Your-Private-Token'
    project: projectname
    gitlab_user: username
    access_level: developer
    pruge_users: developer
    state: present

- name: Remove a list of Users with Dedicated Access Levels to A GitLab project
  community.general.gitlab_project_members:
    api_url: 'https://gitlab.example.com'
    api_token: 'Your-Private-Token'
    project: projectname
    gitlab_users_access:
      - name: user1
        access_level: developer
      - name: user2
        access_level: maintainer
    state: absent
```

### Authors

- Sergey Mikhaltsov (@metanovii)
- Zainab Alsaffar (@zanssa)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
