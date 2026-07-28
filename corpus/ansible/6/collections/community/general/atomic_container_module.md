---
collection: ansible
version: "6"
title: "community.general.atomic_container module – Manage the containers on the atomic host platform"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/atomic_container_module.html
fetched_at: 2026-07-27T17:08:10+00:00
---
# community.general.atomic_container module – Manage the containers on the atomic host platform

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
> see [Requirements](atomic_container_module.md#ansible-collections-community-general-atomic-container-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.atomic_container`.

- [Synopsis](atomic_container_module.md#synopsis)
- [Requirements](atomic_container_module.md#requirements)
- [Parameters](atomic_container_module.md#parameters)
- [Notes](atomic_container_module.md#notes)
- [Examples](atomic_container_module.md#examples)
- [Return Values](atomic_container_module.md#return-values)

## [Synopsis](atomic_container_module.md#id1)

- Manage the containers on the atomic host platform.
- Allows to manage the lifecycle of a container on the atomic host platform.

## [Requirements](atomic_container_module.md#id2)

The below requirements are needed on the host that executes this module.

- atomic
- python >= 2.6

## [Parameters](atomic_container_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **backend**  string / required | Define the backend to use for the container.  Choices:   - `"docker"` - `"ostree"` |
| **image**  string / required | The image to use to install the container. |
| **mode**  string | Define if it is an user or a system container.  Choices:   - `"user"` - `"system"` |
| **name**  string / required | Name of the container. |
| **rootfs**  string | Define the rootfs of the image. |
| **state**  string | State of the container.  Choices:   - `"absent"` - `"latest"` ← (default) - `"present"` - `"rollback"` |
| **values**  list / elements=string | Values for the installation of the container.  This option is permitted only with mode ‘user’ or ‘system’.  The values specified here will be used at installation time as –set arguments for atomic install.  Default: `[]` |

## [Notes](atomic_container_module.md#id4)

> **Note:**
>
> - Host should support `atomic` command

## [Examples](atomic_container_module.md#id5)

```yaml+jinja
- name: Install the etcd system container
  community.general.atomic_container:
    name: etcd
    image: rhel/etcd
    backend: ostree
    state: latest
    mode: system
    values:
        - ETCD_NAME=etcd.server

- name: Uninstall the etcd system container
  community.general.atomic_container:
    name: etcd
    image: rhel/etcd
    backend: ostree
    state: absent
    mode: system
```

## [Return Values](atomic_container_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | The command standard output  Returned: always  Sample: `"Using default tag: latest ..."` |

### Authors

- Giuseppe Scrivano (@giuseppe)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
