---
collection: ansible
version: "8"
title: "community.general.bzr module – Deploy software (or files) from bzr branches"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/bzr_module.html
fetched_at: 2026-07-28T01:44:54+00:00
---
# community.general.bzr module – Deploy software (or files) from bzr branches

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.bzr`.

- [Synopsis](bzr_module.md#synopsis)
- [Parameters](bzr_module.md#parameters)
- [Attributes](bzr_module.md#attributes)
- [Examples](bzr_module.md#examples)

## [Synopsis](bzr_module.md#id1)

- Manage `bzr` branches to deploy files or software.

Aliases: source_control.bzr

## [Parameters](bzr_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **dest**  path / required | Absolute path of where the branch should be cloned to. |
| **executable**  string | Path to bzr executable to use. If not supplied, the normal mechanism for resolving binary paths will be used. |
| **force**  boolean | If `true`, any modified files in the working tree will be discarded. Before Ansible 1.9 the default value was `true`.  **Choices:**   - `false` ← (default) - `true` |
| **name**  aliases: parent  string / required | SSH or HTTP protocol address of the parent branch. |
| **version**  string | What version of the branch to clone. This can be the bzr revno or revid.  **Default:** `"head"` |

## [Attributes](bzr_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](bzr_module.md#id4)

```yaml+jinja
- name: Checkout
  community.general.bzr:
    name: bzr+ssh://foosball.example.org/path/to/branch
    dest: /srv/checkout
    version: 22
```

### Authors

- André Paramés (@andreparames)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
