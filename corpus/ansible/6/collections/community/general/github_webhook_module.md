---
collection: ansible
version: "6"
title: "community.general.github_webhook module – Manage GitHub webhooks"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/github_webhook_module.html
fetched_at: 2026-07-27T17:09:04+00:00
---
# community.general.github_webhook module – Manage GitHub webhooks

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
> see [Requirements](github_webhook_module.md#ansible-collections-community-general-github-webhook-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.github_webhook`.

- [Synopsis](github_webhook_module.md#synopsis)
- [Requirements](github_webhook_module.md#requirements)
- [Parameters](github_webhook_module.md#parameters)
- [Examples](github_webhook_module.md#examples)
- [Return Values](github_webhook_module.md#return-values)

## [Synopsis](github_webhook_module.md#id1)

- Create and delete GitHub webhooks

## [Requirements](github_webhook_module.md#id2)

The below requirements are needed on the host that executes this module.

- PyGithub >= 1.3.5

## [Parameters](github_webhook_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **active**  boolean | Whether or not the hook is active  Choices:   - `false` - `true` ← (default) |
| **content_type**  string | The media type used to serialize the payloads  Choices:   - `"form"` ← (default) - `"json"` |
| **events**  list / elements=string | A list of GitHub events the hook is triggered for. Events are listed at <https://developer.github.com/v3/activity/events/types/>. Required unless `state` is `absent` |
| **github_url**  string | Base URL of the GitHub API  Default: `"https://api.github.com"` |
| **insecure_ssl**  boolean | Flag to indicate that GitHub should skip SSL verification when calling the hook.  Choices:   - `false` ← (default) - `true` |
| **password**  string | Password to authenticate to GitHub with |
| **repository**  aliases: repo  string / required | Full name of the repository to configure a hook for |
| **secret**  string | The shared secret between GitHub and the payload URL. |
| **state**  string | Whether the hook should be present or absent  Choices:   - `"absent"` - `"present"` ← (default) |
| **token**  string | Token to authenticate to GitHub with |
| **url**  string / required | URL to which payloads will be delivered |
| **user**  string / required | User to authenticate to GitHub as |

## [Examples](github_webhook_module.md#id4)

```yaml+jinja
- name: Create a new webhook that triggers on push (password auth)
  community.general.github_webhook:
    repository: ansible/ansible
    url: https://www.example.com/hooks/
    events:
      - push
    user: "{{ github_user }}"
    password: "{{ github_password }}"

- name: Create a new webhook in a github enterprise installation with multiple event triggers (token auth)
  community.general.github_webhook:
    repository: myorg/myrepo
    url: https://jenkins.example.com/ghprbhook/
    content_type: json
    secret: "{{ github_shared_secret }}"
    insecure_ssl: true
    events:
      - issue_comment
      - pull_request
    user: "{{ github_user }}"
    token: "{{ github_user_api_token }}"
    github_url: https://github.example.com

- name: Delete a webhook (password auth)
  community.general.github_webhook:
    repository: ansible/ansible
    url: https://www.example.com/hooks/
    state: absent
    user: "{{ github_user }}"
    password: "{{ github_password }}"
```

## [Return Values](github_webhook_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hook_id**  integer | The GitHub ID of the hook created/updated  Returned: when state is ‘present’  Sample: `6206` |

### Authors

- Chris St. Pierre (@stpierre)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
