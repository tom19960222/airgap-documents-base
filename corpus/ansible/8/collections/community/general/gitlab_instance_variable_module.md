---
collection: ansible
version: "8"
title: "community.general.gitlab_instance_variable module – Creates, updates, or deletes GitLab instance variables"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/gitlab_instance_variable_module.html
fetched_at: 2026-07-28T01:45:50+00:00
---
# community.general.gitlab_instance_variable module – Creates, updates, or deletes GitLab instance variables

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
> see [Requirements](gitlab_instance_variable_module.md#ansible-collections-community-general-gitlab-instance-variable-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.gitlab_instance_variable`.

New in community.general 7.1.0

- [Synopsis](gitlab_instance_variable_module.md#synopsis)
- [Requirements](gitlab_instance_variable_module.md#requirements)
- [Parameters](gitlab_instance_variable_module.md#parameters)
- [Attributes](gitlab_instance_variable_module.md#attributes)
- [Examples](gitlab_instance_variable_module.md#examples)
- [Return Values](gitlab_instance_variable_module.md#return-values)

## [Synopsis](gitlab_instance_variable_module.md#id1)

- Creates a instance variable if it does not exist.
- When a instance variable does exist, its value will be updated if the values are different.
- Support for instance variables requires GitLab >= 13.0.
- Variables which are not mentioned in the modules options, but are present on the GitLab instance, will either stay (`purge=false`) or will be deleted (`purge=true`).

## [Requirements](gitlab_instance_variable_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- python-gitlab python module
- requests (Python library <https://pypi.org/project/requests/>)

## [Parameters](gitlab_instance_variable_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_job_token**  string  *added in community.general 4.2.0* | GitLab CI job token for logging in. |
| **api_oauth_token**  string  *added in community.general 4.2.0* | GitLab OAuth token for logging in. |
| **api_password**  string | The password to use for authentication against the API |
| **api_token**  string | GitLab access token with API permissions. |
| **api_url**  string | The resolvable endpoint for the API |
| **api_username**  string | The username to use for authentication against the API |
| **purge**  boolean | When set to `true`, delete all variables which are not mentioned in the task.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | Create or delete instance variable.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | Whether or not to validate SSL certs when supplying a https endpoint.  **Choices:**   - `false` - `true` ← (default) |
| **variables**  list / elements=dictionary | A list of dictionaries that represents CI/CD variables.  **Default:** `[]` |
| **masked**  boolean | Whether variable value is masked or not.  **Choices:**   - `false` ← (default) - `true` |
| **name**  string / required | The name of the variable. |
| **protected**  boolean | Whether variable value is protected or not.  **Choices:**   - `false` ← (default) - `true` |
| **value**  string | The variable value.  Required when `state=present`. |
| **variable_type**  string | Whether a variable is an environment variable (`env_var`) or a file (`file`).  **Choices:**   - `"env_var"` ← (default) - `"file"` |

## [Attributes](gitlab_instance_variable_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](gitlab_instance_variable_module.md#id5)

```yaml+jinja
- name: Set or update some CI/CD variables
  community.general.gitlab_instance_variable:
    api_url: https://gitlab.com
    api_token: secret_access_token
    purge: false
    variables:
      - name: ACCESS_KEY_ID
        value: abc1312cba
      - name: SECRET_ACCESS_KEY
        value: 1337
        masked: true
        protected: true
        variable_type: env_var

- name: Delete one variable
  community.general.gitlab_instance_variable:
    api_url: https://gitlab.com
    api_token: secret_access_token
    state: absent
    variables:
      - name: ACCESS_KEY_ID
```

## [Return Values](gitlab_instance_variable_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **instance_variable**  dictionary | Four lists of the variablenames which were added, updated, removed or exist.  **Returned:** always |
| **added**  list / elements=string | A list of variables which were created.  **Returned:** always  **Sample:** `["ACCESS_KEY_ID", "SECRET_ACCESS_KEY"]` |
| **removed**  list / elements=string | A list of variables which were deleted.  **Returned:** always  **Sample:** `["ACCESS_KEY_ID", "SECRET_ACCESS_KEY"]` |
| **untouched**  list / elements=string | A list of variables which exist.  **Returned:** always  **Sample:** `["ACCESS_KEY_ID", "SECRET_ACCESS_KEY"]` |
| **updated**  list / elements=string | A list pre-existing variables whose values have been set.  **Returned:** always  **Sample:** `["ACCESS_KEY_ID", "SECRET_ACCESS_KEY"]` |

### Authors

- Benedikt Braunger (@benibr)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
