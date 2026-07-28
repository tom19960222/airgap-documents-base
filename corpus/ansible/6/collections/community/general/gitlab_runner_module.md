---
collection: ansible
version: "6"
title: "community.general.gitlab_runner module – Create, modify and delete GitLab Runners"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/gitlab_runner_module.html
fetched_at: 2026-07-27T17:09:12+00:00
---
# community.general.gitlab_runner module – Create, modify and delete GitLab Runners

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
> see [Requirements](gitlab_runner_module.md#ansible-collections-community-general-gitlab-runner-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.gitlab_runner`.

- [Synopsis](gitlab_runner_module.md#synopsis)
- [Requirements](gitlab_runner_module.md#requirements)
- [Parameters](gitlab_runner_module.md#parameters)
- [Notes](gitlab_runner_module.md#notes)
- [Examples](gitlab_runner_module.md#examples)
- [Return Values](gitlab_runner_module.md#return-values)

## [Synopsis](gitlab_runner_module.md#id1)

- Register, update and delete runners with the GitLab API.
- All operations are performed using the GitLab API v4.
- For details, consult the full API documentation at <https://docs.gitlab.com/ee/api/runners.html>.
- A valid private API token is required for all operations. You can create as many tokens as you like using the GitLab web interface at <https://%24GITLAB_URL/profile/personal_access_tokens>.
- A valid registration token is required for registering a new runner. To create shared runners, you need to ask your administrator to give you this token. It can be found at <https://%24GITLAB_URL/admin/runners/>.

## [Requirements](gitlab_runner_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- python-gitlab >= 1.5.0
- requests (Python library <https://pypi.org/project/requests/>)

## [Parameters](gitlab_runner_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_level**  string | Determines if a runner can pick up jobs only from protected branches.  If set to `ref_protected`, runner can pick up jobs only from protected branches.  If set to `not_protected`, runner can pick up jobs from both protected and unprotected branches.  Choices:   - `"ref_protected"` ← (default) - `"not_protected"` |
| **active**  boolean | Define if the runners is immediately active after creation.  Choices:   - `false` - `true` ← (default) |
| **api_job_token**  string  added in community.general 4.2.0 | GitLab CI job token for logging in. |
| **api_oauth_token**  string  added in community.general 4.2.0 | GitLab OAuth token for logging in. |
| **api_password**  string | The password to use for authentication against the API |
| **api_token**  string | GitLab access token with API permissions. |
| **api_url**  string | The resolvable endpoint for the API |
| **api_username**  string | The username to use for authentication against the API |
| **description**  aliases: name  string / required | The unique name of the runner. |
| **locked**  boolean | Determines if the runner is locked or not.  Choices:   - `false` ← (default) - `true` |
| **maximum_timeout**  integer | The maximum time that a runner has to complete a specific job.  Default: `3600` |
| **owned**  boolean  added in community.general 2.0.0 | Searches only runners available to the user when searching for existing, when false admin token required.  Mutually exclusive with *project* since community.general 4.5.0.  Choices:   - `false` ← (default) - `true` |
| **project**  string  added in community.general 3.7.0 | ID or full path of the project in the form of group/name.  Mutually exclusive with *owned* since community.general 4.5.0. |
| **registration_token**  string | The registration token is used to register new runners.  Required if *state* is `present`. |
| **run_untagged**  boolean | Run untagged jobs or not.  Choices:   - `false` - `true` ← (default) |
| **state**  string | Make sure that the runner with the same name exists with the same configuration or delete the runner with the same name.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tag_list**  list / elements=string | The tags that apply to the runner.  Default: `[]` |
| **validate_certs**  boolean | Whether or not to validate SSL certs when supplying a https endpoint.  Choices:   - `false` - `true` ← (default) |

## [Notes](gitlab_runner_module.md#id4)

> **Note:**
>
> - To create a new runner at least the `api_token`, `description` and `api_url` options are required.
> - Runners need to have unique descriptions.

## [Examples](gitlab_runner_module.md#id5)

```yaml+jinja
- name: "Register runner"
  community.general.gitlab_runner:
    api_url: https://gitlab.example.com/
    api_token: "{{ access_token }}"
    registration_token: 4gfdsg345
    description: Docker Machine t1
    state: present
    active: true
    tag_list: ['docker']
    run_untagged: false
    locked: false

- name: "Delete runner"
  community.general.gitlab_runner:
    api_url: https://gitlab.example.com/
    api_token: "{{ access_token }}"
    description: Docker Machine t1
    state: absent

- name: Delete an owned runner as a non-admin
  community.general.gitlab_runner:
    api_url: https://gitlab.example.com/
    api_token: "{{ access_token }}"
    description: Docker Machine t1
    owned: true
    state: absent

- name: Register runner for a specific project
  community.general.gitlab_runner:
    api_url: https://gitlab.example.com/
    api_token: "{{ access_token }}"
    registration_token: 4gfdsg345
    description: MyProject runner
    state: present
    project: mygroup/mysubgroup/myproject
```

## [Return Values](gitlab_runner_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error**  string | the error message returned by the GitLab API  Returned: failed  Sample: `"400: path is already in use"` |
| **msg**  string | Success or failure message  Returned: always  Sample: `"Success"` |
| **result**  dictionary | json parsed response from the server  Returned: always |
| **runner**  dictionary | API object  Returned: always |

### Authors

- Samy Coenen (@SamyCoenen)
- Guillaume Martinez (@Lunik)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
