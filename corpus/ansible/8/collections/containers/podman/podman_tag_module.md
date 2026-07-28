---
collection: ansible
version: "8"
title: "containers.podman.podman_tag module – Add an additional name to a local image"
source_url: https://docs.ansible.com/projects/ansible/8/collections/containers/podman/podman_tag_module.html
fetched_at: 2026-07-28T02:03:17+00:00
---
# containers.podman.podman_tag module – Add an additional name to a local image

> **Note:**
>
> This module is part of the [containers.podman collection](https://galaxy.ansible.com/ui/repo/published/containers/podman/) (version 1.11.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install containers.podman`.
> You need further requirements to be able to use this module,
> see [Requirements](podman_tag_module.md#ansible-collections-containers-podman-podman-tag-module-requirements) for details.
>
> To use it in a playbook, specify: `containers.podman.podman_tag`.

- [Synopsis](podman_tag_module.md#synopsis)
- [Requirements](podman_tag_module.md#requirements)
- [Parameters](podman_tag_module.md#parameters)
- [Examples](podman_tag_module.md#examples)

## [Synopsis](podman_tag_module.md#id1)

- podman tag adds one or more additional names to locally-stored image.

## [Requirements](podman_tag_module.md#id2)

The below requirements are needed on the host that executes this module.

- Podman installed on host

## [Parameters](podman_tag_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **executable**  string | Path to `podman` executable if it is not in the `$PATH` on the machine running `podman`  **Default:** `"podman"` |
| **image**  string / required | Image to tag. |
| **target_names**  list / elements=string / required | Additional names. |

## [Examples](podman_tag_module.md#id4)

```yaml+jinja
# What modules does for example
- containers.podman.podman_tag:
    image: docker.io/continuumio/miniconda3
    target_names:
      - miniconda3
      - miniconda
```

### Authors

- Christian Bourque (@ocafebabe)

### Collection links

- [Issue Tracker](https://github.com/containers/ansible-podman-collections/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/containers/ansible-podman-collections.git)
