---
collection: ansible
version: "8"
title: "community.general.copr module – Manage one of the Copr repositories"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/copr_module.html
fetched_at: 2026-07-28T01:45:15+00:00
---
# community.general.copr module – Manage one of the Copr repositories

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
> see [Requirements](copr_module.md#ansible-collections-community-general-copr-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.copr`.

New in community.general 2.0.0

- [Synopsis](copr_module.md#synopsis)
- [Requirements](copr_module.md#requirements)
- [Parameters](copr_module.md#parameters)
- [Attributes](copr_module.md#attributes)
- [Notes](copr_module.md#notes)
- [Examples](copr_module.md#examples)
- [Return Values](copr_module.md#return-values)

## [Synopsis](copr_module.md#id1)

- This module can enable, disable or remove the specified repository.

Aliases: packaging.os.copr

## [Requirements](copr_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnf
- dnf-plugins-core

## [Parameters](copr_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **chroot**  string | The name of the chroot that you want to enable/disable/remove in the project, for example `epel-7-x86_64`. Default chroot is determined by the operating system, version of the operating system, and architecture on which the module is run. |
| **host**  string | The Copr host to work with.  **Default:** `"copr.fedorainfracloud.org"` |
| **name**  string / required | Copr directory name, for example `@copr/copr-dev`. |
| **protocol**  string | This indicate which protocol to use with the host.  **Default:** `"https"` |
| **state**  string | Whether to set this project as `enabled`, `disabled`, or `absent`.  **Choices:**   - `"absent"` - `"enabled"` ← (default) - `"disabled"` |

## [Attributes](copr_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](copr_module.md#id5)

> **Note:**
>
> - Supports `check_mode`.

## [Examples](copr_module.md#id6)

```yaml+jinja
- name: Enable project Test of the user schlupov
  community.general.copr:
    host: copr.fedorainfracloud.org
    state: enabled
    name: schlupov/Test
    chroot: fedora-31-x86_64

- name: Remove project integration_tests of the group copr
  community.general.copr:
    state: absent
    name: '@copr/integration_tests'
```

## [Return Values](copr_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **repo**  string | Path to the project on the host.  **Returned:** success  **Sample:** `"copr.fedorainfracloud.org/group_copr/integration_tests"` |
| **repo_filename**  string | The name of the repo file in which the copr project information is stored.  **Returned:** success  **Sample:** `"_copr:copr.fedorainfracloud.org:group_copr:integration_tests.repo"` |

### Authors

- Silvie Chlupova (@schlupov)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
