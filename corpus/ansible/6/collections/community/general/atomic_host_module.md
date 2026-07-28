---
collection: ansible
version: "6"
title: "community.general.atomic_host module – Manage the atomic host platform"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/atomic_host_module.html
fetched_at: 2026-07-27T17:08:11+00:00
---
# community.general.atomic_host module – Manage the atomic host platform

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
> see [Requirements](atomic_host_module.md#ansible-collections-community-general-atomic-host-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.atomic_host`.

- [Synopsis](atomic_host_module.md#synopsis)
- [Requirements](atomic_host_module.md#requirements)
- [Parameters](atomic_host_module.md#parameters)
- [Notes](atomic_host_module.md#notes)
- [Examples](atomic_host_module.md#examples)
- [Return Values](atomic_host_module.md#return-values)

## [Synopsis](atomic_host_module.md#id1)

- Manage the atomic host platform.
- Rebooting of Atomic host platform should be done outside this module.

## [Requirements](atomic_host_module.md#id2)

The below requirements are needed on the host that executes this module.

- atomic
- python >= 2.6

## [Parameters](atomic_host_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **revision**  aliases: version  string | The version number of the atomic host to be deployed.  Providing `latest` will upgrade to the latest available version.  Default: `"latest"` |

## [Notes](atomic_host_module.md#id4)

> **Note:**
>
> - Host should be an atomic platform (verified by existence of ‘/run/ostree-booted’ file).

## [Examples](atomic_host_module.md#id5)

```yaml+jinja
- name: Upgrade the atomic host platform to the latest version (atomic host upgrade)
  community.general.atomic_host:
    revision: latest

- name: Deploy a specific revision as the atomic host (atomic host deploy 23.130)
  community.general.atomic_host:
    revision: 23.130
```

## [Return Values](atomic_host_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | The command standard output  Returned: always  Sample: `"Already on latest"` |

### Authors

- Saravanan KR (@krsacme)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
