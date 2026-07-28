---
collection: ansible
version: "6"
title: "community.general.bitbucket_pipeline_variable module – Manages Bitbucket pipeline variables"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/bitbucket_pipeline_variable_module.html
fetched_at: 2026-07-27T17:08:16+00:00
---
# community.general.bitbucket_pipeline_variable module – Manages Bitbucket pipeline variables

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.bitbucket_pipeline_variable`.

- [Synopsis](bitbucket_pipeline_variable_module.md#synopsis)
- [Parameters](bitbucket_pipeline_variable_module.md#parameters)
- [Notes](bitbucket_pipeline_variable_module.md#notes)
- [Examples](bitbucket_pipeline_variable_module.md#examples)

## [Synopsis](bitbucket_pipeline_variable_module.md#id1)

- Manages Bitbucket pipeline variables.

## [Parameters](bitbucket_pipeline_variable_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **client_id**  string | The OAuth consumer key.  If not set the environment variable `BITBUCKET_CLIENT_ID` will be used. |
| **client_secret**  string | The OAuth consumer secret.  If not set the environment variable `BITBUCKET_CLIENT_SECRET` will be used. |
| **name**  string / required | The pipeline variable name. |
| **password**  string  added in community.general 4.0.0 | The App password.  If not set the environment variable `BITBUCKET_PASSWORD` will be used. |
| **repository**  string / required | The repository name. |
| **secured**  boolean | Whether to encrypt the variable value.  Choices:   - `false` ← (default) - `true` |
| **state**  string / required | Indicates desired state of the variable.  Choices:   - `"absent"` - `"present"` |
| **user**  string  added in community.general 4.0.0 | The username.  If not set the environment variable `BITBUCKET_USERNAME` will be used. |
| **value**  string | The pipeline variable value. |
| **workspace**  aliases: username  string / required | The repository owner.  Alias *username* has been deprecated and will become an alias of *user* in community.general 6.0.0. |

## [Notes](bitbucket_pipeline_variable_module.md#id3)

> **Note:**
>
> - Check mode is supported.
> - For secured values return parameter `changed` is always `True`.
> - Bitbucket OAuth consumer key and secret can be obtained from Bitbucket profile -> Settings -> Access Management -> OAuth.
> - Bitbucket App password can be created from Bitbucket profile -> Personal Settings -> App passwords.
> - If both OAuth and Basic Auth credentials are passed, OAuth credentials take precedence.

## [Examples](bitbucket_pipeline_variable_module.md#id4)

```yaml+jinja
- name: Create or update pipeline variables from the list
  community.general.bitbucket_pipeline_variable:
    repository: 'bitbucket-repo'
    workspace: bitbucket_workspace
    name: '{{ item.name }}'
    value: '{{ item.value }}'
    secured: '{{ item.secured }}'
    state: present
  with_items:
    - { name: AWS_ACCESS_KEY, value: ABCD1234, secured: false }
    - { name: AWS_SECRET, value: qwe789poi123vbn0, secured: true }

- name: Remove pipeline variable
  community.general.bitbucket_pipeline_variable:
    repository: bitbucket-repo
    workspace: bitbucket_workspace
    name: AWS_ACCESS_KEY
    state: absent
```

### Authors

- Evgeniy Krysanov (@catcombo)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
