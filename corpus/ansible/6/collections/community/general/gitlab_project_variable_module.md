---
collection: ansible
version: "6"
title: "community.general.gitlab_project_variable module – Creates/updates/deletes GitLab Projects Variables"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/gitlab_project_variable_module.html
fetched_at: 2026-07-27T17:09:11+00:00
---
# community.general.gitlab_project_variable module – Creates/updates/deletes GitLab Projects Variables

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
> see [Requirements](gitlab_project_variable_module.md#ansible-collections-community-general-gitlab-project-variable-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.gitlab_project_variable`.

- [Synopsis](gitlab_project_variable_module.md#synopsis)
- [Requirements](gitlab_project_variable_module.md#requirements)
- [Parameters](gitlab_project_variable_module.md#parameters)
- [Examples](gitlab_project_variable_module.md#examples)
- [Return Values](gitlab_project_variable_module.md#return-values)

## [Synopsis](gitlab_project_variable_module.md#id1)

- When a project variable does not exist, it will be created.
- When a project variable does exist, its value will be updated when the values are different.
- Variables which are untouched in the playbook, but are not untouched in the GitLab project, they stay untouched (*purge* is `false`) or will be deleted (*purge* is `true`).

## [Requirements](gitlab_project_variable_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- python-gitlab python module
- requests (Python library <https://pypi.org/project/requests/>)

## [Parameters](gitlab_project_variable_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_job_token**  string  added in community.general 4.2.0 | GitLab CI job token for logging in. |
| **api_oauth_token**  string  added in community.general 4.2.0 | GitLab OAuth token for logging in. |
| **api_password**  string | The password to use for authentication against the API |
| **api_token**  string | GitLab access token with API permissions. |
| **api_url**  string | The resolvable endpoint for the API |
| **api_username**  string | The username to use for authentication against the API |
| **project**  string / required | The path and name of the project. |
| **purge**  boolean | When set to true, all variables which are not untouched in the task will be deleted.  Choices:   - `false` ← (default) - `true` |
| **state**  string | Create or delete project variable.  Possible values are present and absent.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | Whether or not to validate SSL certs when supplying a https endpoint.  Choices:   - `false` - `true` ← (default) |
| **variables**  list / elements=dictionary  added in community.general 4.4.0 | A list of dictionaries that represents CI/CD variables.  This module works internal with this structure, even if the older *vars* parameter is used.  Default: `[]` |
| **environment_scope**  string | The scope for the variable.  Support for *environment_scope* requires GitLab Premium >= 13.11.  Default: `"*"` |
| **masked**  boolean | Wether variable value is masked or not.  Support for masked values requires GitLab >= 11.10.  Choices:   - `false` ← (default) - `true` |
| **name**  string / required | The name of the variable. |
| **protected**  boolean | Wether variable value is protected or not.  Support for protected values requires GitLab >= 9.3.  Choices:   - `false` ← (default) - `true` |
| **value**  string | The variable value.  Required when *state=present*. |
| **variable_type**  string | Wether a variable is an environment variable (`env_var`) or a file (`file`).  Support for *variable_type* requires GitLab >= 11.11.  Choices:   - `"env_var"` ← (default) - `"file"` |
| **vars**  dictionary | When the list element is a simple key-value pair, masked and protected will be set to false.  When the list element is a dict with the keys *value*, *masked* and *protected*, the user can have full control about whether a value should be masked, protected or both.  Support for protected values requires GitLab >= 9.3.  Support for masked values requires GitLab >= 11.10.  Support for environment_scope requires GitLab Premium >= 13.11.  Support for variable_type requires GitLab >= 11.11.  A *value* must be a string or a number.  Field *variable_type* must be a string with either `env_var`, which is the default, or `file`.  Field *environment_scope* must be a string defined by scope environment.  When a value is masked, it must be in Base64 and have a length of at least 8 characters. See GitLab documentation on acceptable values for a masked variable (<https://docs.gitlab.com/ce/ci/variables/#masked-variables>).  Default: `{}` |

## [Examples](gitlab_project_variable_module.md#id4)

```yaml+jinja
- name: Set or update some CI/CD variables
  community.general.gitlab_project_variable:
    api_url: https://gitlab.com
    api_token: secret_access_token
    project: markuman/dotfiles
    purge: false
    variables:
      - name: ACCESS_KEY_ID
        value: abc123
      - name: SECRET_ACCESS_KEY
        value: dassgrfaeui8989
        masked: true
        protected: true
        environment_scope: production

- name: Set or update some CI/CD variables
  community.general.gitlab_project_variable:
    api_url: https://gitlab.com
    api_token: secret_access_token
    project: markuman/dotfiles
    purge: false
    vars:
      ACCESS_KEY_ID: abc123
      SECRET_ACCESS_KEY:
        value: 3214cbad
        masked: true
        protected: true
        variable_type: env_var
        environment_scope: '*'

- name: Delete one variable
  community.general.gitlab_project_variable:
    api_url: https://gitlab.com
    api_token: secret_access_token
    project: markuman/dotfiles
    state: absent
    vars:
      ACCESS_KEY_ID: abc123
```

## [Return Values](gitlab_project_variable_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **project_variable**  dictionary | Four lists of the variablenames which were added, updated, removed or exist.  Returned: always |
| **added**  list / elements=string | A list of variables which were created.  Returned: always  Sample: `["ACCESS_KEY_ID", "SECRET_ACCESS_KEY"]` |
| **removed**  list / elements=string | A list of variables which were deleted.  Returned: always  Sample: `["ACCESS_KEY_ID", "SECRET_ACCESS_KEY"]` |
| **untouched**  list / elements=string | A list of variables which exist.  Returned: always  Sample: `["ACCESS_KEY_ID", "SECRET_ACCESS_KEY"]` |
| **updated**  list / elements=string | A list of variables whose values were changed.  Returned: always  Sample: `["ACCESS_KEY_ID", "SECRET_ACCESS_KEY"]` |

### Authors

- Markus Bergholz (@markuman)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
