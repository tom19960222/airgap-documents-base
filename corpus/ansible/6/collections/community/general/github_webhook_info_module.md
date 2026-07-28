---
collection: ansible
version: "6"
title: "community.general.github_webhook_info module – Query information about GitHub webhooks"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/github_webhook_info_module.html
fetched_at: 2026-07-27T17:09:05+00:00
---
# community.general.github_webhook_info module – Query information about GitHub webhooks

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
> see [Requirements](github_webhook_info_module.md#ansible-collections-community-general-github-webhook-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.github_webhook_info`.

- [Synopsis](github_webhook_info_module.md#synopsis)
- [Requirements](github_webhook_info_module.md#requirements)
- [Parameters](github_webhook_info_module.md#parameters)
- [Examples](github_webhook_info_module.md#examples)
- [Return Values](github_webhook_info_module.md#return-values)

## [Synopsis](github_webhook_info_module.md#id1)

- Query information about GitHub webhooks
- This module was called `github_webhook_facts` before Ansible 2.9. The usage did not change.

## [Requirements](github_webhook_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- PyGithub >= 1.3.5

## [Parameters](github_webhook_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **github_url**  string | Base URL of the github api  Default: `"https://api.github.com"` |
| **password**  string | Password to authenticate to GitHub with |
| **repository**  aliases: repo  string / required | Full name of the repository to configure a hook for |
| **token**  string | Token to authenticate to GitHub with |
| **user**  string / required | User to authenticate to GitHub as |

## [Examples](github_webhook_info_module.md#id4)

```yaml+jinja
- name: List hooks for a repository (password auth)
  community.general.github_webhook_info:
    repository: ansible/ansible
    user: "{{ github_user }}"
    password: "{{ github_password }}"
  register: ansible_webhooks

- name: List hooks for a repository on GitHub Enterprise (token auth)
  community.general.github_webhook_info:
    repository: myorg/myrepo
    user: "{{ github_user }}"
    token: "{{ github_user_api_token }}"
    github_url: https://github.example.com/api/v3/
  register: myrepo_webhooks
```

## [Return Values](github_webhook_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hooks**  list / elements=dictionary | A list of hooks that exist for the repo  Returned: always  Sample: `[{"active": true, "content_type": "json", "events": ["issue_comment", "pull_request"], "has_shared_secret": true, "id": 6206, "insecure_ssl": "1", "last_response": {"code": 200, "message": "OK", "status": "active"}, "url": "https://jenkins.example.com/ghprbhook/"}]` |

### Authors

- Chris St. Pierre (@stpierre)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
