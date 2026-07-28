---
collection: ansible
version: "8"
title: "community.general.pkg5_publisher module – Manages Solaris 11 Image Packaging System publishers"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/pkg5_publisher_module.html
fetched_at: 2026-07-28T01:49:04+00:00
---
# community.general.pkg5_publisher module – Manages Solaris 11 Image Packaging System publishers

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
> To use it in a playbook, specify: `community.general.pkg5_publisher`.

- [Synopsis](pkg5_publisher_module.md#synopsis)
- [Parameters](pkg5_publisher_module.md#parameters)
- [Attributes](pkg5_publisher_module.md#attributes)
- [Examples](pkg5_publisher_module.md#examples)

## [Synopsis](pkg5_publisher_module.md#id1)

- IPS packages are the native packages in Solaris 11 and higher.
- This modules will configure which publishers a client will download IPS packages from.

Aliases: packaging.os.pkg5_publisher

## [Parameters](pkg5_publisher_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **enabled**  boolean | Is the repository enabled or disabled?  **Choices:**   - `false` - `true` |
| **mirror**  list / elements=string | A path or URL to the repository mirror.  Multiple values may be provided. |
| **name**  aliases: publisher  string / required | The publisher’s name. |
| **origin**  list / elements=string | A path or URL to the repository.  Multiple values may be provided. |
| **state**  string | Whether to ensure that a publisher is present or absent.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **sticky**  boolean | Packages installed from a sticky repository can only receive updates from that repository.  **Choices:**   - `false` - `true` |

## [Attributes](pkg5_publisher_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](pkg5_publisher_module.md#id4)

```yaml+jinja
- name: Fetch packages for the solaris publisher direct from Oracle
  community.general.pkg5_publisher:
    name: solaris
    sticky: true
    origin: https://pkg.oracle.com/solaris/support/

- name: Configure a publisher for locally-produced packages
  community.general.pkg5_publisher:
    name: site
    origin: 'https://pkg.example.com/site/'
```

### Authors

- Peter Oliver (@mavit)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
