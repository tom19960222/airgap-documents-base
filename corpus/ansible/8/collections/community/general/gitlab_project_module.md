---
collection: ansible
version: "8"
title: "community.general.gitlab_project module – Creates/updates/deletes GitLab Projects"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/gitlab_project_module.html
fetched_at: 2026-07-28T01:45:51+00:00
---
# community.general.gitlab_project module – Creates/updates/deletes GitLab Projects

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
> see [Requirements](gitlab_project_module.md#ansible-collections-community-general-gitlab-project-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.gitlab_project`.

- [Synopsis](gitlab_project_module.md#synopsis)
- [Requirements](gitlab_project_module.md#requirements)
- [Parameters](gitlab_project_module.md#parameters)
- [Attributes](gitlab_project_module.md#attributes)
- [Examples](gitlab_project_module.md#examples)
- [Return Values](gitlab_project_module.md#return-values)

## [Synopsis](gitlab_project_module.md#id1)

- When the project does not exist in GitLab, it will be created.
- When the project does exists and `state=absent`, the project will be deleted.
- When changes are made to the project, the project will be updated.

Aliases: source_control.gitlab.gitlab_project

## [Requirements](gitlab_project_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- python-gitlab python module
- requests (Python library <https://pypi.org/project/requests/>)

## [Parameters](gitlab_project_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allow_merge_on_skipped_pipeline**  boolean  *added in community.general 3.4.0* | Allow merge when skipped pipelines exist.  **Choices:**   - `false` - `true` |
| **api_job_token**  string  *added in community.general 4.2.0* | GitLab CI job token for logging in. |
| **api_oauth_token**  string  *added in community.general 4.2.0* | GitLab OAuth token for logging in. |
| **api_password**  string | The password to use for authentication against the API |
| **api_token**  string | GitLab access token with API permissions. |
| **api_url**  string | The resolvable endpoint for the API |
| **api_username**  string | The username to use for authentication against the API |
| **avatar_path**  path  *added in community.general 4.2.0* | Absolute path image to configure avatar. File size should not exceed 200 kb.  This option is only used on creation, not for updates. |
| **builds_access_level**  string  *added in community.general 6.2.0* | `private` means that repository CI/CD is allowed only to project members.  `disabled` means that repository CI/CD is disabled.  `enabled` means that repository CI/CD is enabled.  **Choices:**   - `"private"` - `"disabled"` - `"enabled"` |
| **ci_config_path**  string  *added in community.general 3.7.0* | Custom path to the CI configuration file for this project. |
| **container_registry_access_level**  string  *added in community.general 6.2.0* | `private` means that container registry is allowed only to project members.  `disabled` means that container registry is disabled.  `enabled` means that container registry is enabled.  **Choices:**   - `"private"` - `"disabled"` - `"enabled"` |
| **default_branch**  string  *added in community.general 4.2.0* | Default branch name for a new project.  This option is only used on creation, not for updates. This is also only used if `initialize_with_readme=true`. |
| **description**  string | An description for the project. |
| **environments_access_level**  string  *added in community.general 6.4.0* | `private` means that deployment to environment is allowed only to project members.  `disabled` means that deployment to environment is disabled.  `enabled` means that deployment to environment is enabled.  **Choices:**   - `"private"` - `"disabled"` - `"enabled"` |
| **feature_flags_access_level**  string  *added in community.general 6.4.0* | `private` means that feature rollout is allowed only to project members.  `disabled` means that feature rollout is disabled.  `enabled` means that feature rollout is enabled.  **Choices:**   - `"private"` - `"disabled"` - `"enabled"` |
| **forking_access_level**  string  *added in community.general 6.2.0* | `private` means that repository forks is allowed only to project members.  `disabled` means that repository forks are disabled.  `enabled` means that repository forks are enabled.  **Choices:**   - `"private"` - `"disabled"` - `"enabled"` |
| **group**  string | Id or the full path of the group of which this projects belongs to. |
| **import_url**  string | Git repository which will be imported into gitlab.  GitLab server needs read access to this git repository. |
| **infrastructure_access_level**  string  *added in community.general 6.4.0* | `private` means that configuring infrastructure is allowed only to project members.  `disabled` means that configuring infrastructure is disabled.  `enabled` means that configuring infrastructure is enabled.  **Choices:**   - `"private"` - `"disabled"` - `"enabled"` |
| **initialize_with_readme**  boolean  *added in community.general 4.0.0* | Will initialize the project with a default `README.md`.  Is only used when the project is created, and ignored otherwise.  **Choices:**   - `false` ← (default) - `true` |
| **issues_enabled**  boolean | Whether you want to create issues or not.  Possible values are true and false.  **Choices:**   - `false` - `true` ← (default) |
| **lfs_enabled**  boolean  *added in community.general 2.0.0* | Enable Git large file systems to manages large files such as audio, video, and graphics files.  **Choices:**   - `false` ← (default) - `true` |
| **merge_method**  string  *added in community.general 1.0.0* | What requirements are placed upon merges.  Possible values are `merge`, `rebase_merge` merge commit with semi-linear history, `ff` fast-forward merges only.  **Choices:**   - `"ff"` - `"merge"` ← (default) - `"rebase_merge"` |
| **merge_requests_enabled**  boolean | If merge requests can be made or not.  Possible values are true and false.  **Choices:**   - `false` - `true` ← (default) |
| **monitor_access_level**  string  *added in community.general 6.4.0* | `private` means that monitoring health is allowed only to project members.  `disabled` means that monitoring health is disabled.  `enabled` means that monitoring health is enabled.  **Choices:**   - `"private"` - `"disabled"` - `"enabled"` |
| **name**  string / required | The name of the project. |
| **only_allow_merge_if_all_discussions_are_resolved**  boolean  *added in community.general 3.4.0* | All discussions on a merge request (MR) have to be resolved.  **Choices:**   - `false` - `true` |
| **only_allow_merge_if_pipeline_succeeds**  boolean  *added in community.general 3.4.0* | Only allow merges if pipeline succeeded.  **Choices:**   - `false` - `true` |
| **packages_enabled**  boolean  *added in community.general 3.4.0* | Enable GitLab package repository.  **Choices:**   - `false` - `true` |
| **path**  string | The path of the project you want to create, this will be server_url/<group>/path.  If not supplied, name will be used. |
| **releases_access_level**  string  *added in community.general 6.4.0* | `private` means that accessing release is allowed only to project members.  `disabled` means that accessing release is disabled.  `enabled` means that accessing release is enabled.  **Choices:**   - `"private"` - `"disabled"` - `"enabled"` |
| **remove_source_branch_after_merge**  boolean  *added in community.general 3.4.0* | Remove the source branch after merge.  **Choices:**   - `false` - `true` |
| **security_and_compliance_access_level**  string  *added in community.general 6.4.0* | `private` means that accessing security and complicance tab is allowed only to project members.  `disabled` means that accessing security and complicance tab is disabled.  `enabled` means that accessing security and complicance tab is enabled.  **Choices:**   - `"private"` - `"disabled"` - `"enabled"` |
| **shared_runners_enabled**  boolean  *added in community.general 3.7.0* | Enable shared runners for this project.  **Choices:**   - `false` - `true` |
| **snippets_enabled**  boolean | If creating snippets should be available or not.  **Choices:**   - `false` - `true` ← (default) |
| **squash_option**  string  *added in community.general 3.4.0* | Squash commits when merging.  **Choices:**   - `"never"` - `"always"` - `"default_off"` - `"default_on"` |
| **state**  string | Create or delete project.  Possible values are present and absent.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **topics**  list / elements=string  *added in community.general 6.6.0* | A topic or list of topics to be assigned to a project.  It is compatible with old GitLab server releases (versions before 14, correspond to `tag_list`). |
| **username**  string  *added in community.general 3.3.0* | Used to create a personal project under a user’s name. |
| **validate_certs**  boolean | Whether or not to validate SSL certs when supplying a https endpoint.  **Choices:**   - `false` - `true` ← (default) |
| **visibility**  aliases: visibility_level  string | `private` Project access must be granted explicitly for each user.  `internal` The project can be cloned by any logged in user.  `public` The project can be cloned without any authentication.  **Choices:**   - `"private"` ← (default) - `"internal"` - `"public"` |
| **wiki_enabled**  boolean | If an wiki for this project should be available or not.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](gitlab_project_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](gitlab_project_module.md#id5)

```yaml+jinja
- name: Create GitLab Project
  community.general.gitlab_project:
    api_url: https://gitlab.example.com/
    api_token: "{{ api_token }}"
    name: my_first_project
    group: "10481470"

- name: Delete GitLab Project
  community.general.gitlab_project:
    api_url: https://gitlab.example.com/
    api_token: "{{ access_token }}"
    validate_certs: false
    name: my_first_project
    state: absent
  delegate_to: localhost

- name: Create GitLab Project in group Ansible
  community.general.gitlab_project:
    api_url: https://gitlab.example.com/
    validate_certs: true
    api_username: dj-wasabi
    api_password: "MySecretPassword"
    name: my_first_project
    group: ansible
    issues_enabled: false
    merge_method: rebase_merge
    wiki_enabled: true
    snippets_enabled: true
    import_url: http://git.example.com/example/lab.git
    initialize_with_readme: true
    state: present
  delegate_to: localhost

- name: get the initial root password
  ansible.builtin.shell: |
    grep 'Password:' /etc/gitlab/initial_root_password | sed -e 's/Password\: \(.*\)/\1/'
  register: initial_root_password

- name: Create a GitLab Project using a username/password via oauth_token
  community.general.gitlab_project:
    api_url: https://gitlab.example.com/
    api_username: root
    api_password: "{{ initial_root_password }}"
    name: my_second_project
    group: "10481470"
```

## [Return Values](gitlab_project_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error**  string | the error message returned by the GitLab API.  **Returned:** failed  **Sample:** `"400: path is already in use"` |
| **msg**  string | Success or failure message.  **Returned:** always  **Sample:** `"Success"` |
| **project**  dictionary | API object.  **Returned:** always |
| **result**  dictionary | json parsed response from the server.  **Returned:** always |

### Authors

- Werner Dijkerman (@dj-wasabi)
- Guillaume Martinez (@Lunik)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
