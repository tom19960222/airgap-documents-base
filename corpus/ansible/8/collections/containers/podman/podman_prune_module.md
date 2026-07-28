---
collection: ansible
version: "8"
title: "containers.podman.podman_prune module – Allows to prune various podman objects"
source_url: https://docs.ansible.com/projects/ansible/8/collections/containers/podman/podman_prune_module.html
fetched_at: 2026-07-28T02:03:15+00:00
---
# containers.podman.podman_prune module – Allows to prune various podman objects

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
> see [Requirements](podman_prune_module.md#ansible-collections-containers-podman-podman-prune-module-requirements) for details.
>
> To use it in a playbook, specify: `containers.podman.podman_prune`.

New in containers.podman 1.10.0

- [Synopsis](podman_prune_module.md#synopsis)
- [Requirements](podman_prune_module.md#requirements)
- [Parameters](podman_prune_module.md#parameters)
- [Examples](podman_prune_module.md#examples)
- [Return Values](podman_prune_module.md#return-values)

## [Synopsis](podman_prune_module.md#id1)

- Allows to run `podman container prune`, `podman image prune`, `podman network prune`, `podman volume prune` and `podman system prune`

## [Requirements](podman_prune_module.md#id2)

The below requirements are needed on the host that executes this module.

- Podman installed on host

## [Parameters](podman_prune_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **container**  boolean | Whether to prune containers.  **Choices:**   - `false` ← (default) - `true` |
| **container_filters**  dictionary | A dictionary of filter values used for selecting containers to delete.  For example, `until: 24h`.  See [the podman documentation](https://docs.podman.io/en/latest/markdown/podman-container-prune.1.html#filter-filters) for more information on possible filters. |
| **executable**  string | Podman binary.  **Default:** `"podman"` |
| **image**  boolean | Whether to prune images.  **Choices:**   - `false` ← (default) - `true` |
| **image_filters**  dictionary | A dictionary of filter values used for selecting images to delete.  You can also use `dangling_only: false` to delete dangling and non-dangling images or `external: true` to delete images even when they are used by external containers.  See [the podman documentation](https://docs.podman.io/en/latest/markdown/podman-image-prune.1.html#filter-filters) for more information on possible filters. |
| **network**  boolean | Whether to prune networks.  **Choices:**   - `false` ← (default) - `true` |
| **network_filters**  dictionary | A dictionary of filter values used for selecting networks to delete.  See [the podman documentation](https://docs.podman.io/en/latest/markdown/podman-network-prune.1.html#filter) for more information on possible filters. |
| **system**  boolean | Whether to prune unused pods, containers, image, networks and volume data  **Choices:**   - `false` ← (default) - `true` |
| **system_all**  boolean | Whether to prune all unused images, not only dangling images.  **Choices:**   - `false` ← (default) - `true` |
| **system_volumes**  boolean | Whether to prune volumes currently unused by any container.  **Choices:**   - `false` ← (default) - `true` |
| **volume**  boolean | Whether to prune volumes.  **Choices:**   - `false` ← (default) - `true` |
| **volume_filters**  dictionary | A dictionary of filter values used for selecting volumes to delete.  See [the podman documentation](https://docs.podman.io/en/latest/markdown/podman-volume-prune.1.html#filter) for more information on possible filters. |

## [Examples](podman_prune_module.md#id4)

```yaml+jinja
- name: Prune containers older than 24h
  containers.podman.podman_prune:
      containers: true
      containers_filters:
          # only consider containers created more than 24 hours ago
          until: 24h

- name: Prune everything
  containers.podman.podman_prune:
      system: true

- name: Prune everything (including non-dangling images)
  containers.podman.podman_prune:
      system: true
      system_all: true
      system_volumes: true
```

## [Return Values](podman_prune_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **containers**  list / elements=string | List of IDs of deleted containers.  **Returned:** *containers* is `true`  **Sample:** `[]` |
| **images**  list / elements=string | List of IDs of deleted images.  **Returned:** *images* is `true`  **Sample:** `[]` |
| **networks**  list / elements=string | List of IDs of deleted networks.  **Returned:** *networks* is `true`  **Sample:** `[]` |
| **system**  list / elements=string | List of ID of deleted containers, volumes, images, network and total reclaimed space  **Returned:** *system* is `true`  **Sample:** `[]` |
| **volumes**  list / elements=string | List of IDs of deleted volumes.  **Returned:** *volumes* is `true`  **Sample:** `[]` |

### Authors

- Roberto Alfieri (@rebtoor)

### Collection links

- [Issue Tracker](https://github.com/containers/ansible-podman-collections/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/containers/ansible-podman-collections.git)
