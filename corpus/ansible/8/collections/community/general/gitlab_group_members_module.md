---
collection: ansible
version: "8"
title: "community.general.gitlab_group_members module – Manage group members on GitLab Server"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/gitlab_group_members_module.html
fetched_at: 2026-07-28T01:45:48+00:00
---
# community.general.gitlab_group_members module – Manage group members on GitLab Server

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
> see [Requirements](gitlab_group_members_module.md#ansible-collections-community-general-gitlab-group-members-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.gitlab_group_members`.

New in community.general 1.2.0

- [Synopsis](gitlab_group_members_module.md#synopsis)
- [Requirements](gitlab_group_members_module.md#requirements)
- [Parameters](gitlab_group_members_module.md#parameters)
- [Attributes](gitlab_group_members_module.md#attributes)
- [Examples](gitlab_group_members_module.md#examples)

## [Synopsis](gitlab_group_members_module.md#id1)

- This module allows to add and remove members to/from a group, or change a member’s access level in a group on GitLab.

Aliases: source_control.gitlab.gitlab_group_members

## [Requirements](gitlab_group_members_module.md#id2)

The below requirements are needed on the host that executes this module.

- administrator rights on the GitLab server
- python-gitlab python module <= 1.15.0
- requests (Python library <https://pypi.org/project/requests/>)

## [Parameters](gitlab_group_members_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_level**  string | The access level for the user.  Required if `state=present`, user state is set to present.  Mutually exclusive with `gitlab_users_access`.  **Choices:**   - `"guest"` - `"reporter"` - `"developer"` - `"maintainer"` - `"owner"` |
| **api_job_token**  string  *added in community.general 4.2.0* | GitLab CI job token for logging in. |
| **api_oauth_token**  string  *added in community.general 4.2.0* | GitLab OAuth token for logging in. |
| **api_password**  string | The password to use for authentication against the API |
| **api_token**  string | GitLab access token with API permissions. |
| **api_url**  string | The resolvable endpoint for the API |
| **api_username**  string | The username to use for authentication against the API |
| **gitlab_group**  string / required | The `full_path` of the GitLab group the member is added to/removed from.  Setting this to `name` or `path` has been disallowed since community.general 6.0.0. Use `full_path` instead. |
| **gitlab_user**  list / elements=string | A username or a list of usernames to add to/remove from the GitLab group.  Mutually exclusive with `gitlab_users_access`. |
| **gitlab_users_access**  list / elements=dictionary  *added in community.general 3.6.0* | Provide a list of user to access level mappings.  Every dictionary in this list specifies a user (by username) and the access level the user should have.  Mutually exclusive with `gitlab_user` and `access_level`.  Use together with `purge_users` to remove all users not specified here from the group. |
| **access_level**  string / required | The access level for the user.  Required if `state=present`, user state is set to present.  **Choices:**   - `"guest"` - `"reporter"` - `"developer"` - `"maintainer"` - `"owner"` |
| **name**  string / required | A username or a list of usernames to add to/remove from the GitLab group. |
| **purge_users**  list / elements=string  *added in community.general 3.6.0* | Adds/remove users of the given access_level to match the given `gitlab_user`/`gitlab_users_access` list. If omitted do not purge orphaned members.  Is only used when `state=present`.  **Choices:**   - `"guest"` - `"reporter"` - `"developer"` - `"maintainer"` - `"owner"` |
| **state**  string | State of the member in the group.  On `present`, it adds a user to a GitLab group.  On `absent`, it removes a user from a GitLab group.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | Whether or not to validate SSL certs when supplying a https endpoint.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](gitlab_group_members_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](gitlab_group_members_module.md#id5)

```yaml+jinja
- name: Add a user to a GitLab Group
  community.general.gitlab_group_members:
    api_url: 'https://gitlab.example.com'
    api_token: 'Your-Private-Token'
    gitlab_group: groupname
    gitlab_user: username
    access_level: developer
    state: present

- name: Remove a user from a GitLab Group
  community.general.gitlab_group_members:
    api_url: 'https://gitlab.example.com'
    api_token: 'Your-Private-Token'
    gitlab_group: groupname
    gitlab_user: username
    state: absent

- name: Add a list of Users to A GitLab Group
  community.general.gitlab_group_members:
    api_url: 'https://gitlab.example.com'
    api_token: 'Your-Private-Token'
    gitlab_group: groupname
    gitlab_user:
      - user1
      - user2
    access_level: developer
    state: present

- name: Add a list of Users with Dedicated Access Levels to A GitLab Group
  community.general.gitlab_group_members:
    api_url: 'https://gitlab.example.com'
    api_token: 'Your-Private-Token'
    gitlab_group: groupname
    gitlab_users_access:
      - name: user1
        access_level: developer
      - name: user2
        access_level: maintainer
    state: present

- name: Add a user, remove all others which might be on this access level
  community.general.gitlab_group_members:
    api_url: 'https://gitlab.example.com'
    api_token: 'Your-Private-Token'
    gitlab_group: groupname
    gitlab_user: username
    access_level: developer
    pruge_users: developer
    state: present

- name: Remove a list of Users with Dedicated Access Levels to A GitLab Group
  community.general.gitlab_group_members:
    api_url: 'https://gitlab.example.com'
    api_token: 'Your-Private-Token'
    gitlab_group: groupname
    gitlab_users_access:
      - name: user1
        access_level: developer
      - name: user2
        access_level: maintainer
    state: absent
```

### Authors

- Zainab Alsaffar (@zanssa)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
