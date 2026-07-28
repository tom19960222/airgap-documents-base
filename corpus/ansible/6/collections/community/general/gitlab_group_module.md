---
collection: ansible
version: "6"
title: "community.general.gitlab_group module – Creates/updates/deletes GitLab Groups"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/gitlab_group_module.html
fetched_at: 2026-07-27T17:09:07+00:00
---
# community.general.gitlab_group module – Creates/updates/deletes GitLab Groups

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
> see [Requirements](gitlab_group_module.md#ansible-collections-community-general-gitlab-group-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.gitlab_group`.

- [Synopsis](gitlab_group_module.md#synopsis)
- [Requirements](gitlab_group_module.md#requirements)
- [Parameters](gitlab_group_module.md#parameters)
- [Examples](gitlab_group_module.md#examples)
- [Return Values](gitlab_group_module.md#return-values)

## [Synopsis](gitlab_group_module.md#id1)

- When the group does not exist in GitLab, it will be created.
- When the group does exist and state=absent, the group will be deleted.

## [Requirements](gitlab_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- python-gitlab python module
- requests (Python library <https://pypi.org/project/requests/>)

## [Parameters](gitlab_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_job_token**  string  added in community.general 4.2.0 | GitLab CI job token for logging in. |
| **api_oauth_token**  string  added in community.general 4.2.0 | GitLab OAuth token for logging in. |
| **api_password**  string | The password to use for authentication against the API |
| **api_token**  string | GitLab access token with API permissions. |
| **api_url**  string | The resolvable endpoint for the API |
| **api_username**  string | The username to use for authentication against the API |
| **auto_devops_enabled**  boolean  added in community.general 3.7.0 | Default to Auto DevOps pipeline for all projects within this group.  Choices:   - `false` - `true` |
| **avatar_path**  path  added in community.general 4.2.0 | Absolute path image to configure avatar. File size should not exceed 200 kb.  This option is only used on creation, not for updates. |
| **description**  string | A description for the group. |
| **name**  string / required | Name of the group you want to create. |
| **parent**  string | Allow to create subgroups  Id or Full path of parent group in the form of group/name |
| **path**  string | The path of the group you want to create, this will be api_url/group_path  If not supplied, the group_name will be used. |
| **project_creation_level**  string  added in community.general 3.7.0 | Determine if developers can create projects in the group.  Choices:   - `"developer"` - `"maintainer"` - `"noone"` |
| **require_two_factor_authentication**  boolean  added in community.general 3.7.0 | Require all users in this group to setup two-factor authentication.  Choices:   - `false` - `true` |
| **state**  string | create or delete group.  Possible values are present and absent.  Choices:   - `"present"` ← (default) - `"absent"` |
| **subgroup_creation_level**  string  added in community.general 3.7.0 | Allowed to create subgroups.  Choices:   - `"maintainer"` - `"owner"` |
| **validate_certs**  boolean | Whether or not to validate SSL certs when supplying a https endpoint.  Choices:   - `false` - `true` ← (default) |
| **visibility**  string | Default visibility of the group  Choices:   - `"private"` ← (default) - `"internal"` - `"public"` |

## [Examples](gitlab_group_module.md#id4)

```yaml+jinja
- name: "Delete GitLab Group"
  community.general.gitlab_group:
    api_url: https://gitlab.example.com/
    api_token: "{{ access_token }}"
    validate_certs: false
    name: my_first_group
    state: absent

- name: "Create GitLab Group"
  community.general.gitlab_group:
    api_url: https://gitlab.example.com/
    validate_certs: true
    api_username: dj-wasabi
    api_password: "MySecretPassword"
    name: my_first_group
    path: my_first_group
    state: present

# The group will by created at https://gitlab.dj-wasabi.local/super_parent/parent/my_first_group
- name: "Create GitLab SubGroup"
  community.general.gitlab_group:
    api_url: https://gitlab.example.com/
    validate_certs: true
    api_username: dj-wasabi
    api_password: "MySecretPassword"
    name: my_first_group
    path: my_first_group
    state: present
    parent: "super_parent/parent"

# Other group which only allows sub-groups - no projects
- name: "Create GitLab Group for SubGroups only"
  community.general.gitlab_group:
    api_url: https://gitlab.example.com/
    validate_certs: true
    api_username: dj-wasabi
    api_password: "MySecretPassword"
    name: my_main_group
    path: my_main_group
    state: present
    project_creation_level: noone
    auto_devops_enabled: false
    subgroup_creation_level: maintainer
```

## [Return Values](gitlab_group_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error**  string | the error message returned by the GitLab API  Returned: failed  Sample: `"400: path is already in use"` |
| **group**  dictionary | API object  Returned: always |
| **msg**  string | Success or failure message  Returned: always  Sample: `"Success"` |
| **result**  dictionary | json parsed response from the server  Returned: always |

### Authors

- Werner Dijkerman (@dj-wasabi)
- Guillaume Martinez (@Lunik)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
