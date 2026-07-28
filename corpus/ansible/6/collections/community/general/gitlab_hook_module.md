---
collection: ansible
version: "6"
title: "community.general.gitlab_hook module – Manages GitLab project hooks"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/gitlab_hook_module.html
fetched_at: 2026-07-27T17:09:09+00:00
---
# community.general.gitlab_hook module – Manages GitLab project hooks

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
> see [Requirements](gitlab_hook_module.md#ansible-collections-community-general-gitlab-hook-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.gitlab_hook`.

- [Synopsis](gitlab_hook_module.md#synopsis)
- [Requirements](gitlab_hook_module.md#requirements)
- [Parameters](gitlab_hook_module.md#parameters)
- [Examples](gitlab_hook_module.md#examples)
- [Return Values](gitlab_hook_module.md#return-values)

## [Synopsis](gitlab_hook_module.md#id1)

- Adds, updates and removes project hook

## [Requirements](gitlab_hook_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- python-gitlab python module
- requests (Python library <https://pypi.org/project/requests/>)

## [Parameters](gitlab_hook_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_job_token**  string  added in community.general 4.2.0 | GitLab CI job token for logging in. |
| **api_oauth_token**  string  added in community.general 4.2.0 | GitLab OAuth token for logging in. |
| **api_password**  string | The password to use for authentication against the API |
| **api_token**  string | GitLab access token with API permissions. |
| **api_url**  string | The resolvable endpoint for the API |
| **api_username**  string | The username to use for authentication against the API |
| **hook_url**  string / required | The url that you want GitLab to post to, this is used as the primary key for updates and deletion. |
| **hook_validate_certs**  aliases: enable_ssl_verification  boolean | Whether GitLab will do SSL verification when triggering the hook.  Choices:   - `false` ← (default) - `true` |
| **issues_events**  boolean | Trigger hook on issues events.  Choices:   - `false` ← (default) - `true` |
| **job_events**  boolean | Trigger hook on job events.  Choices:   - `false` ← (default) - `true` |
| **merge_requests_events**  boolean | Trigger hook on merge requests events.  Choices:   - `false` ← (default) - `true` |
| **note_events**  boolean | Trigger hook on note events or when someone adds a comment.  Choices:   - `false` ← (default) - `true` |
| **pipeline_events**  boolean | Trigger hook on pipeline events.  Choices:   - `false` ← (default) - `true` |
| **project**  string / required | Id or Full path of the project in the form of group/name. |
| **push_events**  boolean | Trigger hook on push events.  Choices:   - `false` - `true` ← (default) |
| **push_events_branch_filter**  string  added in community.general 0.2.0 | Branch name of wildcard to trigger hook on push events  Default: `""` |
| **state**  string | When `present` the hook will be updated to match the input or created if it doesn’t exist.  When `absent` hook will be deleted if it exists.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tag_push_events**  boolean | Trigger hook on tag push events.  Choices:   - `false` ← (default) - `true` |
| **token**  string | Secret token to validate hook messages at the receiver.  If this is present it will always result in a change as it cannot be retrieved from GitLab.  Will show up in the X-GitLab-Token HTTP request header. |
| **validate_certs**  boolean | Whether or not to validate SSL certs when supplying a https endpoint.  Choices:   - `false` - `true` ← (default) |
| **wiki_page_events**  boolean | Trigger hook on wiki events.  Choices:   - `false` ← (default) - `true` |

## [Examples](gitlab_hook_module.md#id4)

```yaml+jinja
- name: "Adding a project hook"
  community.general.gitlab_hook:
    api_url: https://gitlab.example.com/
    api_token: "{{ access_token }}"
    project: "my_group/my_project"
    hook_url: "https://my-ci-server.example.com/gitlab-hook"
    state: present
    push_events: true
    tag_push_events: true
    hook_validate_certs: false
    token: "my-super-secret-token-that-my-ci-server-will-check"

- name: "Delete the previous hook"
  community.general.gitlab_hook:
    api_url: https://gitlab.example.com/
    api_token: "{{ access_token }}"
    project: "my_group/my_project"
    hook_url: "https://my-ci-server.example.com/gitlab-hook"
    state: absent

- name: "Delete a hook by numeric project id"
  community.general.gitlab_hook:
    api_url: https://gitlab.example.com/
    api_token: "{{ access_token }}"
    project: 10
    hook_url: "https://my-ci-server.example.com/gitlab-hook"
    state: absent
```

## [Return Values](gitlab_hook_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error**  string | the error message returned by the GitLab API  Returned: failed  Sample: `"400: path is already in use"` |
| **hook**  dictionary | API object  Returned: always |
| **msg**  string | Success or failure message  Returned: always  Sample: `"Success"` |
| **result**  dictionary | json parsed response from the server  Returned: always |

### Authors

- Marcus Watkins (@marwatk)
- Guillaume Martinez (@Lunik)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
