---
collection: ansible
version: "8"
title: "containers.podman.podman_volume_info module – Gather info about podman volumes"
source_url: https://docs.ansible.com/projects/ansible/8/collections/containers/podman/podman_volume_info_module.html
fetched_at: 2026-07-28T02:03:19+00:00
---
# containers.podman.podman_volume_info module – Gather info about podman volumes

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
> see [Requirements](podman_volume_info_module.md#ansible-collections-containers-podman-podman-volume-info-module-requirements) for details.
>
> To use it in a playbook, specify: `containers.podman.podman_volume_info`.

- [Synopsis](podman_volume_info_module.md#synopsis)
- [Requirements](podman_volume_info_module.md#requirements)
- [Parameters](podman_volume_info_module.md#parameters)
- [Examples](podman_volume_info_module.md#examples)
- [Return Values](podman_volume_info_module.md#return-values)

## [Synopsis](podman_volume_info_module.md#id1)

- Gather info about podman volumes with podman inspect command.

## [Requirements](podman_volume_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- Podman installed on host

## [Parameters](podman_volume_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **executable**  string | Path to `podman` executable if it is not in the `$PATH` on the machine running `podman`  **Default:** `"podman"` |
| **name**  string | Name of the volume |

## [Examples](podman_volume_info_module.md#id4)

```yaml+jinja
- name: Gather info about all present volumes
  podman_volume_info:

- name: Gather info about specific volume
  podman_volume_info:
    name: specific_volume
```

## [Return Values](podman_volume_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **volumes**  list / elements=string | Facts from all or specified volumes  **Returned:** always  **Sample:** `[{"driver": "local", "labels": {}, "mountPoint": "/home/ansible/.local/share/testvolume/_data", "name": "testvolume", "options": {}, "scope": "local"}]` |

### Authors

- Sagi Shnaidman (@sshnaidm)

### Collection links

- [Issue Tracker](https://github.com/containers/ansible-podman-collections/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/containers/ansible-podman-collections.git)
