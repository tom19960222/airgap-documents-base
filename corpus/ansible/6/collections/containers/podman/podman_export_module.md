---
collection: ansible
version: "6"
title: "containers.podman.podman_export module – Export a podman container"
source_url: https://docs.ansible.com/projects/ansible/6/collections/containers/podman/podman_export_module.html
fetched_at: 2026-07-27T17:24:29+00:00
---
# containers.podman.podman_export module – Export a podman container

> **Note:**
>
> This module is part of the [containers.podman collection](https://galaxy.ansible.com/containers/podman) (version 1.10.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install containers.podman`.
> You need further requirements to be able to use this module,
> see [Requirements](podman_export_module.md#ansible-collections-containers-podman-podman-export-module-requirements) for details.
>
> To use it in a playbook, specify: `containers.podman.podman_export`.

- [Synopsis](podman_export_module.md#synopsis)
- [Requirements](podman_export_module.md#requirements)
- [Parameters](podman_export_module.md#parameters)
- [Examples](podman_export_module.md#examples)

## [Synopsis](podman_export_module.md#id1)

- podman export exports the filesystem of a container and saves it as a tarball on the local machine

## [Requirements](podman_export_module.md#id2)

The below requirements are needed on the host that executes this module.

- Podman installed on host

## [Parameters](podman_export_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **container**  string / required | Container to export. |
| **dest**  string / required | Path to export container to. |
| **executable**  string | Path to `podman` executable if it is not in the `$PATH` on the machine running `podman`  Default: `"podman"` |
| **force**  boolean | Force saving to file even if it exists.  Choices:   - `false` - `true` ← (default) |

## [Examples](podman_export_module.md#id4)

```yaml+jinja
# What modules does for example
- containers.podman.podman_export:
    dest: /path/to/tar/file
    container: container-name
```

### Authors

- Sagi Shnaidman (@sshnaidm)

### Collection links

[Issue Tracker](https://github.com/containers/ansible-podman-collections/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/containers/ansible-podman-collections.git)
