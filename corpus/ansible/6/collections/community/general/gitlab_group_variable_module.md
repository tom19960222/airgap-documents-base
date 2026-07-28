---
collection: ansible
version: "6"
title: "community.general.gitlab_group_variable module – Creates, updates, or deletes GitLab groups variables"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/gitlab_group_variable_module.html
fetched_at: 2026-07-27T17:09:08+00:00
---
# community.general.gitlab_group_variable module – Creates, updates, or deletes GitLab groups variables

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
> see [Requirements](gitlab_group_variable_module.md#ansible-collections-community-general-gitlab-group-variable-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.gitlab_group_variable`.

New in community.general 1.2.0

- [Synopsis](gitlab_group_variable_module.md#synopsis)
- [Requirements](gitlab_group_variable_module.md#requirements)
- [Parameters](gitlab_group_variable_module.md#parameters)
- [Notes](gitlab_group_variable_module.md#notes)
- [Examples](gitlab_group_variable_module.md#examples)
- [Return Values](gitlab_group_variable_module.md#return-values)

## [Synopsis](gitlab_group_variable_module.md#id1)

- Creates a group variable if it does not exist.
- When a group variable does exist, its value will be updated when the values are different.
- Variables which are untouched in the playbook, but are not untouched in the GitLab group, they stay untouched (*purge* is `false`) or will be deleted (*purge* is `true`).

## [Requirements](gitlab_group_variable_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- python-gitlab python module
- requests (Python library <https://pypi.org/project/requests/>)

## [Parameters](gitlab_group_variable_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_job_token**  string  added in community.general 4.2.0 | GitLab CI job token for logging in. |
| **api_oauth_token**  string  added in community.general 4.2.0 | GitLab OAuth token for logging in. |
| **api_password**  string | The password to use for authentication against the API |
| **api_token**  string | GitLab access token with API permissions. |
| **api_url**  string | The resolvable endpoint for the API |
| **api_username**  string | The username to use for authentication against the API |
| **group**  string / required | The path and name of the group. |
| **purge**  boolean | When set to `true`, delete all variables which are not untouched in the task.  Choices:   - `false` ← (default) - `true` |
| **state**  string | Create or delete group variable.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | Whether or not to validate SSL certs when supplying a https endpoint.  Choices:   - `false` - `true` ← (default) |
| **variables**  list / elements=dictionary  added in community.general 4.5.0 | A list of dictionaries that represents CI/CD variables.  This modules works internal with this sructure, even if the older *vars* parameter is used.  Default: `[]` |
| **environment_scope**  string | The scope for the variable.  Default: `"*"` |
| **masked**  boolean | Wether variable value is masked or not.  Choices:   - `false` ← (default) - `true` |
| **name**  string / required | The name of the variable. |
| **protected**  boolean | Wether variable value is protected or not.  Choices:   - `false` ← (default) - `true` |
| **value**  string | The variable value.  Required when *state=present*. |
| **variable_type**  string | Wether a variable is an environment variable (`env_var`) or a file (`file`).  Choices:   - `"env_var"` ← (default) - `"file"` |
| **vars**  dictionary | When the list element is a simple key-value pair, set masked and protected to false.  When the list element is a dict with the keys *value*, *masked* and *protected*, the user can have full control about whether a value should be masked, protected or both.  Support for group variables requires GitLab >= 9.5.  Support for environment_scope requires GitLab Premium >= 13.11.  Support for protected values requires GitLab >= 9.3.  Support for masked values requires GitLab >= 11.10.  A *value* must be a string or a number.  Field *variable_type* must be a string with either `env_var`, which is the default, or `file`.  When a value is masked, it must be in Base64 and have a length of at least 8 characters. See GitLab documentation on acceptable values for a masked variable (<https://docs.gitlab.com/ce/ci/variables/#masked-variables>).  Default: `{}` |

## [Notes](gitlab_group_variable_module.md#id4)

> **Note:**
>
> - Supports *check_mode*.

## [Examples](gitlab_group_variable_module.md#id5)

```yaml+jinja
- name: Set or update some CI/CD variables
  community.general.gitlab_group_variable:
    api_url: https://gitlab.com
    api_token: secret_access_token
    group: scodeman/testgroup/
    purge: false
    variables:
      - name: ACCESS_KEY_ID
        value: abc123
      - name: SECRET_ACCESS_KEY
        value: 3214cbad
        masked: true
        protected: true
        variable_type: env_var
        environment_scope: production

- name: Delete one variable
  community.general.gitlab_group_variable:
    api_url: https://gitlab.com
    api_token: secret_access_token
    group: scodeman/testgroup/
    state: absent
    vars:
      ACCESS_KEY_ID: abc123
```

## [Return Values](gitlab_group_variable_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **group_variable**  dictionary | Four lists of the variablenames which were added, updated, removed or exist.  Returned: always |
| **added**  list / elements=string | A list of variables which were created.  Returned: always  Sample: `["ACCESS_KEY_ID", "SECRET_ACCESS_KEY"]` |
| **removed**  list / elements=string | A list of variables which were deleted.  Returned: always  Sample: `["ACCESS_KEY_ID", "SECRET_ACCESS_KEY"]` |
| **untouched**  list / elements=string | A list of variables which exist.  Returned: always  Sample: `["ACCESS_KEY_ID", "SECRET_ACCESS_KEY"]` |
| **updated**  list / elements=string | A list of variables whose values were changed.  Returned: always  Sample: `["ACCESS_KEY_ID", "SECRET_ACCESS_KEY"]` |

### Authors

- Florent Madiot (@scodeman)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
