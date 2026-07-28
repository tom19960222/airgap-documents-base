---
collection: ansible
version: "8"
title: "containers.podman.podman_containers module – Manage podman containers in a batch"
source_url: https://docs.ansible.com/projects/ansible/8/collections/containers/podman/podman_containers_module.html
fetched_at: 2026-07-28T02:03:04+00:00
---
# containers.podman.podman_containers module – Manage podman containers in a batch

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
> see [Requirements](podman_containers_module.md#ansible-collections-containers-podman-podman-containers-module-requirements) for details.
>
> To use it in a playbook, specify: `containers.podman.podman_containers`.

New in containers.podman 1.4.0

- [Synopsis](podman_containers_module.md#synopsis)
- [Requirements](podman_containers_module.md#requirements)
- [Parameters](podman_containers_module.md#parameters)
- [Examples](podman_containers_module.md#examples)

## [Synopsis](podman_containers_module.md#id1)

- Manage groups of podman containers

## [Requirements](podman_containers_module.md#id2)

The below requirements are needed on the host that executes this module.

- podman

## [Parameters](podman_containers_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **containers**  list / elements=dictionary / required | List of dictionaries with data for running containers for podman_container module. |
| **debug**  boolean | Return additional information which can be helpful for investigations.  **Choices:**   - `false` ← (default) - `true` |

## [Examples](podman_containers_module.md#id4)

```yaml+jinja
- name: Run three containers at once
  podman_containers:
    containers:
      - name: alpine
        image: alpine
        command: sleep 1d
      - name: web
        image: nginx
      - name: test
        image: python:3.10-alpine
        command: python -V
```

### Authors

- Sagi Shnaidman (@sshnaidm)

### Collection links

- [Issue Tracker](https://github.com/containers/ansible-podman-collections/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/containers/ansible-podman-collections.git)
