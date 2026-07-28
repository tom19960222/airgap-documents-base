---
collection: ansible
version: "8"
title: "community.general.heroku_collaborator module – Add or delete app collaborators on Heroku"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/heroku_collaborator_module.html
fetched_at: 2026-07-28T01:45:58+00:00
---
# community.general.heroku_collaborator module – Add or delete app collaborators on Heroku

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
> see [Requirements](heroku_collaborator_module.md#ansible-collections-community-general-heroku-collaborator-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.heroku_collaborator`.

- [Synopsis](heroku_collaborator_module.md#synopsis)
- [Requirements](heroku_collaborator_module.md#requirements)
- [Parameters](heroku_collaborator_module.md#parameters)
- [Attributes](heroku_collaborator_module.md#attributes)
- [Notes](heroku_collaborator_module.md#notes)
- [Examples](heroku_collaborator_module.md#examples)

## [Synopsis](heroku_collaborator_module.md#id1)

- Manages collaborators for Heroku apps.
- If set to `present` and heroku user is already collaborator, then do nothing.
- If set to `present` and heroku user is not collaborator, then add user to app.
- If set to `absent` and heroku user is collaborator, then delete user from app.

Aliases: cloud.heroku.heroku_collaborator

## [Requirements](heroku_collaborator_module.md#id2)

The below requirements are needed on the host that executes this module.

- heroku3

## [Parameters](heroku_collaborator_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_key**  string | Heroku API key |
| **apps**  list / elements=string / required | List of Heroku App names |
| **state**  string | Create or remove the heroku collaborator  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **suppress_invitation**  boolean | Suppress email invitation when creating collaborator  **Choices:**   - `false` ← (default) - `true` |
| **user**  string / required | User ID or e-mail |

## [Attributes](heroku_collaborator_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](heroku_collaborator_module.md#id5)

> **Note:**
>
> - `HEROKU_API_KEY` and `TF_VAR_HEROKU_API_KEY` environment variables can be used instead setting `api_key`.
> - If you use `check_mode`, you can also pass the `-v` flag to see affected apps in `msg`, e.g. [“heroku-example-app”].

## [Examples](heroku_collaborator_module.md#id6)

```yaml+jinja
- name: Create a heroku collaborator
  community.general.heroku_collaborator:
    api_key: YOUR_API_KEY
    user: max.mustermann@example.com
    apps: heroku-example-app
    state: present

- name: An example of using the module in loop
  community.general.heroku_collaborator:
    api_key: YOUR_API_KEY
    user: '{{ item.user }}'
    apps: '{{ item.apps | default(apps) }}'
    suppress_invitation: '{{ item.suppress_invitation | default(suppress_invitation) }}'
    state: '{{ item.state | default("present") }}'
  with_items:
    - { user: 'a.b@example.com' }
    - { state: 'absent', user: 'b.c@example.com', suppress_invitation: false }
    - { user: 'x.y@example.com', apps: ["heroku-example-app"] }
```

### Authors

- Marcel Arns (@marns93)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
