---
collection: ansible
version: "8"
title: "community.general.github_release module – Interact with GitHub Releases"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/github_release_module.html
fetched_at: 2026-07-28T01:45:42+00:00
---
# community.general.github_release module – Interact with GitHub Releases

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
> see [Requirements](github_release_module.md#ansible-collections-community-general-github-release-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.github_release`.

- [Synopsis](github_release_module.md#synopsis)
- [Requirements](github_release_module.md#requirements)
- [Parameters](github_release_module.md#parameters)
- [Attributes](github_release_module.md#attributes)
- [Examples](github_release_module.md#examples)
- [Return Values](github_release_module.md#return-values)

## [Synopsis](github_release_module.md#id1)

- Fetch metadata about GitHub Releases

Aliases: source_control.github.github_release

## [Requirements](github_release_module.md#id2)

The below requirements are needed on the host that executes this module.

- github3.py >= 1.0.0a3

## [Parameters](github_release_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **action**  string / required | Action to perform  **Choices:**   - `"latest_release"` - `"create_release"` |
| **body**  string | Description of the release when creating a release |
| **draft**  boolean | Sets if the release is a draft or not. (boolean)  **Choices:**   - `false` ← (default) - `true` |
| **name**  string | Name of release when creating a release |
| **password**  string | The GitHub account password for the user. Mutually exclusive with `token`. |
| **prerelease**  boolean | Sets if the release is a prerelease or not. (boolean)  **Choices:**   - `false` ← (default) - `true` |
| **repo**  string / required | Repository name |
| **tag**  string | Tag name when creating a release. Required when using `action=create_release`. |
| **target**  string | Target of release when creating a release |
| **token**  string | GitHub Personal Access Token for authenticating. Mutually exclusive with `password`. |
| **user**  string / required | The GitHub account that owns the repository |

## [Attributes](github_release_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](github_release_module.md#id5)

```yaml+jinja
- name: Get latest release of a public repository
  community.general.github_release:
    user: ansible
    repo: ansible
    action: latest_release

- name: Get latest release of testuseer/testrepo
  community.general.github_release:
    token: tokenabc1234567890
    user: testuser
    repo: testrepo
    action: latest_release

- name: Get latest release of test repo using username and password. Ansible 2.4.
  community.general.github_release:
    user: testuser
    password: secret123
    repo: testrepo
    action: latest_release

- name: Create a new release
  community.general.github_release:
    token: tokenabc1234567890
    user: testuser
    repo: testrepo
    action: create_release
    tag: test
    target: master
    name: My Release
    body: Some description
```

## [Return Values](github_release_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **tag**  string | Version of the created/latest release.  **Returned:** success  **Sample:** `"1.1.0"` |

### Authors

- Adrian Moisey (@adrianmoisey)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
