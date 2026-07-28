---
collection: ansible
version: "6"
title: "community.general.github_repo module – Manage your repositories on Github"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/github_repo_module.html
fetched_at: 2026-07-27T17:09:03+00:00
---
# community.general.github_repo module – Manage your repositories on Github

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
> see [Requirements](github_repo_module.md#ansible-collections-community-general-github-repo-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.github_repo`.

New in community.general 2.2.0

- [Synopsis](github_repo_module.md#synopsis)
- [Requirements](github_repo_module.md#requirements)
- [Parameters](github_repo_module.md#parameters)
- [Notes](github_repo_module.md#notes)
- [Examples](github_repo_module.md#examples)
- [Return Values](github_repo_module.md#return-values)

## [Synopsis](github_repo_module.md#id1)

- Manages Github repositories using PyGithub library.
- Authentication can be done with *access_token* or with *username* and *password*.

## [Requirements](github_repo_module.md#id2)

The below requirements are needed on the host that executes this module.

- PyGithub>=1.54

## [Parameters](github_repo_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token parameter for authentication.  This is only needed when not using *username* and *password*. |
| **api_url**  string  added in community.general 3.5.0 | URL to the GitHub API if not using github.com but you own instance.  Default: `"https://api.github.com"` |
| **description**  string | Description for the repository.  Defaults to empty if *force_defaults=true*, which is the default in this module.  Defaults to empty if *force_defaults=false* when creating a new repository.  This is only used when *state* is `present`. |
| **force_defaults**  boolean  added in community.general 4.1.0 | Overwrite current *description* and *private* attributes with defaults if set to `true`, which currently is the default.  The default for this option will be deprecated in a future version of this collection, and eventually change to `false`.  Choices:   - `false` - `true` ← (default) |
| **name**  string / required | Repository name. |
| **organization**  string | Organization for the repository.  When *state* is `present`, the repository will be created in the current user profile. |
| **password**  string | Password used for authentication.  This is only needed when not using *access_token*. |
| **private**  boolean | Whether the repository should be private or not.  Defaults to `false` if *force_defaults=true*, which is the default in this module.  Defaults to `false` if *force_defaults=false* when creating a new repository.  This is only used when *state* is `present`.  Choices:   - `false` - `true` |
| **state**  string | Whether the repository should exist or not.  Choices:   - `"absent"` - `"present"` ← (default) |
| **username**  string | Username used for authentication.  This is only needed when not using *access_token*. |

## [Notes](github_repo_module.md#id4)

> **Note:**
>
> - For Python 3, PyGithub>=1.54 should be used.
> - For Python 3.5, PyGithub==1.54 should be used. More information: <https://pygithub.readthedocs.io/en/latest/changes.html#version-1-54-november-30-2020>.
> - For Python 2.7, PyGithub==1.45 should be used. More information: <https://pygithub.readthedocs.io/en/latest/changes.html#version-1-45-december-29-2019>.
> - Supports `check_mode`.

## [Examples](github_repo_module.md#id5)

```yaml+jinja
- name: Create a Github repository
  community.general.github_repo:
    access_token: mytoken
    organization: MyOrganization
    name: myrepo
    description: "Just for fun"
    private: true
    state: present
    force_defaults: false
  register: result

- name: Delete the repository
  community.general.github_repo:
    username: octocat
    password: password
    organization: MyOrganization
    name: myrepo
    state: absent
  register: result
```

## [Return Values](github_repo_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **repo**  dictionary | Repository information as JSON. See <https://docs.github.com/en/rest/reference/repos#get-a-repository>.  Returned: success and *state* is `present` |

### Authors

- Álvaro Torres Cogollo (@atorrescogollo)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
