---
collection: ansible
version: "6"
title: "community.general.atomic_image module – Manage the container images on the atomic host platform"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/atomic_image_module.html
fetched_at: 2026-07-27T17:08:11+00:00
---
# community.general.atomic_image module – Manage the container images on the atomic host platform

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
> see [Requirements](atomic_image_module.md#ansible-collections-community-general-atomic-image-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.atomic_image`.

- [Synopsis](atomic_image_module.md#synopsis)
- [Requirements](atomic_image_module.md#requirements)
- [Parameters](atomic_image_module.md#parameters)
- [Notes](atomic_image_module.md#notes)
- [Examples](atomic_image_module.md#examples)
- [Return Values](atomic_image_module.md#return-values)

## [Synopsis](atomic_image_module.md#id1)

- Manage the container images on the atomic host platform.
- Allows to execute the commands specified by the RUN label in the container image when present.

## [Requirements](atomic_image_module.md#id2)

The below requirements are needed on the host that executes this module.

- atomic
- python >= 2.6

## [Parameters](atomic_image_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **backend**  string | Define the backend where the image is pulled.  Choices:   - `"docker"` - `"ostree"` |
| **name**  string / required | Name of the container image. |
| **started**  boolean | Start or Stop the container.  Choices:   - `false` - `true` ← (default) |
| **state**  string | The state of the container image.  The state `latest` will ensure container image is upgraded to the latest version and forcefully restart container, if running.  Choices:   - `"absent"` - `"latest"` ← (default) - `"present"` |

## [Notes](atomic_image_module.md#id4)

> **Note:**
>
> - Host should support `atomic` command.

## [Examples](atomic_image_module.md#id5)

```yaml+jinja
- name: Execute the run command on rsyslog container image (atomic run rhel7/rsyslog)
  community.general.atomic_image:
    name: rhel7/rsyslog
    state: latest

- name: Pull busybox to the OSTree backend
  community.general.atomic_image:
    name: busybox
    state: latest
    backend: ostree
```

## [Return Values](atomic_image_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | The command standard output  Returned: always  Sample: `"Using default tag: latest ..."` |

### Authors

- Saravanan KR (@krsacme)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
