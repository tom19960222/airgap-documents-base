---
collection: ansible
version: "8"
title: "community.general.gitlab_merge_request module – Create, update, or delete GitLab merge requests"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/gitlab_merge_request_module.html
fetched_at: 2026-07-28T01:45:50+00:00
---
# community.general.gitlab_merge_request module – Create, update, or delete GitLab merge requests

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
> see [Requirements](gitlab_merge_request_module.md#ansible-collections-community-general-gitlab-merge-request-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.gitlab_merge_request`.

New in community.general 7.1.0

- [Synopsis](gitlab_merge_request_module.md#synopsis)
- [Requirements](gitlab_merge_request_module.md#requirements)
- [Parameters](gitlab_merge_request_module.md#parameters)
- [Attributes](gitlab_merge_request_module.md#attributes)
- [Examples](gitlab_merge_request_module.md#examples)
- [Return Values](gitlab_merge_request_module.md#return-values)

## [Synopsis](gitlab_merge_request_module.md#id1)

- Creates a merge request if it does not exist.
- When a single merge request does exist, it will be updated if the provided parameters are different.
- When a single merge request does exist and `state=absent`, the merge request will be deleted.
- When multiple merge requests are detected, the task fails.
- Existing merge requests are matched based on `title`, `source_branch`, `target_branch`, and `state_filter` filters.

## [Requirements](gitlab_merge_request_module.md#id2)

The below requirements are needed on the host that executes this module.

- Python >= 2.7
- python-gitlab >= 2.3.0
- requests (Python library <https://pypi.org/project/requests/>)

## [Parameters](gitlab_merge_request_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_job_token**  string  *added in community.general 4.2.0* | GitLab CI job token for logging in. |
| **api_oauth_token**  string  *added in community.general 4.2.0* | GitLab OAuth token for logging in. |
| **api_password**  string | The password to use for authentication against the API |
| **api_token**  string | GitLab access token with API permissions. |
| **api_url**  string | The resolvable endpoint for the API |
| **api_username**  string | The username to use for authentication against the API |
| **assignee_ids**  string | Comma separated list of assignees usernames omitting `@` character.  Set to empty string to unassign all assignees. |
| **description**  string | A description for the merge request.  Gets overridden by a content of file specified at `description_path`, if found. |
| **description_path**  path | A path of file containing merge request’s description.  Accepts MarkDown formatted files. |
| **labels**  string | Comma separated list of label names.  **Default:** `""` |
| **project**  string / required | The path or name of the project. |
| **remove_source_branch**  boolean | Flag indicating if a merge request should remove the source branch when merging.  **Choices:**   - `false` ← (default) - `true` |
| **reviewer_ids**  string | Comma separated list of reviewers usernames omitting `@` character.  Set to empty string to unassign all reviewers. |
| **source_branch**  string / required | Merge request’s source branch.  Ignored while updating existing merge request. |
| **state**  string | Create or delete merge request.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **state_filter**  string | Filter specifying state of merge requests while searching.  **Choices:**   - `"opened"` ← (default) - `"closed"` - `"locked"` - `"merged"` |
| **target_branch**  string / required | Merge request’s target branch. |
| **title**  string / required | A title for the merge request. |
| **validate_certs**  boolean | Whether or not to validate SSL certs when supplying a https endpoint.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](gitlab_merge_request_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](gitlab_merge_request_module.md#id5)

```yaml+jinja
- name: Create Merge Request from branch1 to branch2
  community.general.gitlab_merge_request:
    api_url: https://gitlab.com
    api_token: secret_access_token
    project: "group1/project1"
    source_branch: branch1
    target_branch: branch2
    title: "Ansible demo MR"
    description: "Demo MR description"
    labels: "Ansible,Demo"
    state_filter: "opened"
    remove_source_branch: True
    state: present

- name: Delete Merge Request from branch1 to branch2
  community.general.gitlab_merge_request:
    api_url: https://gitlab.com
    api_token: secret_access_token
    project: "group1/project1"
    source_branch: branch1
    target_branch: branch2
    title: "Ansible demo MR"
    state_filter: "opened"
    state: absent
```

## [Return Values](gitlab_merge_request_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **mr**  dictionary | API object.  **Returned:** success |
| **msg**  string | Success or failure message.  **Returned:** always  **Sample:** `"Success"` |

### Authors

- zvaraondrej (@zvaraondrej)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
