---
collection: ansible
version: "8"
title: "community.general.pkg5 module – Manages packages with the Solaris 11 Image Packaging System"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/pkg5_module.html
fetched_at: 2026-07-28T01:49:03+00:00
---
# community.general.pkg5 module – Manages packages with the Solaris 11 Image Packaging System

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
> To use it in a playbook, specify: `community.general.pkg5`.

- [Synopsis](pkg5_module.md#synopsis)
- [Parameters](pkg5_module.md#parameters)
- [Attributes](pkg5_module.md#attributes)
- [Notes](pkg5_module.md#notes)
- [Examples](pkg5_module.md#examples)

## [Synopsis](pkg5_module.md#id1)

- IPS packages are the native packages in Solaris 11 and higher.

Aliases: packaging.os.pkg5

## [Parameters](pkg5_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **accept_licenses**  aliases: accept, accept_licences  boolean | Accept any licences.  **Choices:**   - `false` ← (default) - `true` |
| **be_name**  string | Creates a new boot environment with the given name. |
| **name**  list / elements=string / required | An FRMI of the package(s) to be installed/removed/updated.  Multiple packages may be specified, separated by `,`. |
| **refresh**  boolean | Refresh publishers before execution.  **Choices:**   - `false` - `true` ← (default) |
| **state**  string | Whether to install (`present`, `latest`), or remove (`absent`) a package.  **Choices:**   - `"absent"` - `"latest"` - `"present"` ← (default) - `"installed"` - `"removed"` - `"uninstalled"` |

## [Attributes](pkg5_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](pkg5_module.md#id4)

> **Note:**
>
> - The naming of IPS packages is explained at <http://www.oracle.com/technetwork/articles/servers-storage-admin/ips-package-versioning-2232906.html>.

## [Examples](pkg5_module.md#id5)

```yaml+jinja
- name: Install Vim
  community.general.pkg5:
    name: editor/vim

- name: Install Vim without refreshing publishers
  community.general.pkg5:
    name: editor/vim
    refresh: false

- name: Remove finger daemon
  community.general.pkg5:
    name: service/network/finger
    state: absent

- name: Install several packages at once
  community.general.pkg5:
    name:
    - /file/gnu-findutils
    - /text/gnu-grep
```

### Authors

- Peter Oliver (@mavit)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
