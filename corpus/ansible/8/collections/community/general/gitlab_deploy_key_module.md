---
collection: ansible
version: "8"
title: "community.general.gitlab_deploy_key module – Manages GitLab project deploy keys"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/gitlab_deploy_key_module.html
fetched_at: 2026-07-28T01:45:46+00:00
---
# community.general.gitlab_deploy_key module – Manages GitLab project deploy keys

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
> see [Requirements](gitlab_deploy_key_module.md#ansible-collections-community-general-gitlab-deploy-key-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.gitlab_deploy_key`.

- [Synopsis](gitlab_deploy_key_module.md#synopsis)
- [Requirements](gitlab_deploy_key_module.md#requirements)
- [Parameters](gitlab_deploy_key_module.md#parameters)
- [Attributes](gitlab_deploy_key_module.md#attributes)
- [Examples](gitlab_deploy_key_module.md#examples)
- [Return Values](gitlab_deploy_key_module.md#return-values)

## [Synopsis](gitlab_deploy_key_module.md#id1)

- Adds, updates and removes project deploy keys

Aliases: source_control.gitlab.gitlab_deploy_key

## [Requirements](gitlab_deploy_key_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- python-gitlab python module
- requests (Python library <https://pypi.org/project/requests/>)

## [Parameters](gitlab_deploy_key_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_job_token**  string  *added in community.general 4.2.0* | GitLab CI job token for logging in. |
| **api_oauth_token**  string  *added in community.general 4.2.0* | GitLab OAuth token for logging in. |
| **api_password**  string | The password to use for authentication against the API |
| **api_token**  string | GitLab access token with API permissions. |
| **api_url**  string | The resolvable endpoint for the API |
| **api_username**  string | The username to use for authentication against the API |
| **can_push**  boolean | Whether this key can push to the project.  **Choices:**   - `false` ← (default) - `true` |
| **key**  string / required | Deploy key |
| **project**  string / required | Id or Full path of project in the form of group/name. |
| **state**  string | When `present` the deploy key added to the project if it doesn’t exist.  When `absent` it will be removed from the project if it exists.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **title**  string / required | Deploy key’s title. |
| **validate_certs**  boolean | Whether or not to validate SSL certs when supplying a https endpoint.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](gitlab_deploy_key_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](gitlab_deploy_key_module.md#id5)

```yaml+jinja
- name: "Adding a project deploy key"
  community.general.gitlab_deploy_key:
    api_url: https://gitlab.example.com/
    api_token: "{{ api_token }}"
    project: "my_group/my_project"
    title: "Jenkins CI"
    state: present
    key: "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAIEAiPWx6WM4lhHNedGfBpPJNPpZ7yKu+dnn1SJejgt4596k6YjzGGphH2TUxwKzxcKDKKezwkpfnxPkSMkuEspGRt/aZZ9w..."

- name: "Update the above deploy key to add push access"
  community.general.gitlab_deploy_key:
    api_url: https://gitlab.example.com/
    api_token: "{{ api_token }}"
    project: "my_group/my_project"
    title: "Jenkins CI"
    state: present
    can_push: true

- name: "Remove the previous deploy key from the project"
  community.general.gitlab_deploy_key:
    api_url: https://gitlab.example.com/
    api_token: "{{ api_token }}"
    project: "my_group/my_project"
    state: absent
    key: "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAIEAiPWx6WM4lhHNedGfBpPJNPpZ7yKu+dnn1SJejgt4596k6YjzGGphH2TUxwKzxcKDKKezwkpfnxPkSMkuEspGRt/aZZ9w..."
```

## [Return Values](gitlab_deploy_key_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **deploy_key**  dictionary | API object  **Returned:** always |
| **error**  string | the error message returned by the GitLab API  **Returned:** failed  **Sample:** `"400: key is already in use"` |
| **msg**  string | Success or failure message  **Returned:** always  **Sample:** `"Success"` |
| **result**  dictionary | json parsed response from the server  **Returned:** always |

### Authors

- Marcus Watkins (@marwatk)
- Guillaume Martinez (@Lunik)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
