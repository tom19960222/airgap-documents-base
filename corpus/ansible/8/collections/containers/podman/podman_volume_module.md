---
collection: ansible
version: "8"
title: "containers.podman.podman_volume module – Manage Podman volumes"
source_url: https://docs.ansible.com/projects/ansible/8/collections/containers/podman/podman_volume_module.html
fetched_at: 2026-07-28T02:03:18+00:00
---
# containers.podman.podman_volume module – Manage Podman volumes

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
> see [Requirements](podman_volume_module.md#ansible-collections-containers-podman-podman-volume-module-requirements) for details.
>
> To use it in a playbook, specify: `containers.podman.podman_volume`.

New in containers.podman 1.1.0

- [Synopsis](podman_volume_module.md#synopsis)
- [Requirements](podman_volume_module.md#requirements)
- [Parameters](podman_volume_module.md#parameters)
- [Examples](podman_volume_module.md#examples)
- [Return Values](podman_volume_module.md#return-values)

## [Synopsis](podman_volume_module.md#id1)

- Manage Podman volumes

## [Requirements](podman_volume_module.md#id2)

The below requirements are needed on the host that executes this module.

- podman

## [Parameters](podman_volume_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **debug**  boolean | Return additional information which can be helpful for investigations.  **Choices:**   - `false` ← (default) - `true` |
| **driver**  string | Specify volume driver name (default local). |
| **executable**  string | Path to `podman` executable if it is not in the `$PATH` on the machine running `podman`  **Default:** `"podman"` |
| **label**  dictionary | Add metadata to a pod volume (e.g., label com.example.key=value). |
| **name**  string / required | Name of volume. |
| **options**  list / elements=string | Set driver specific options. For example ‘device=tpmfs’, ‘type=tmpfs’. UID and GID idempotency is not supported due to changes in podman. |
| **recreate**  boolean | Recreate volume even if exists.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | State of volume, default ‘present’  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Examples](podman_volume_module.md#id4)

```yaml+jinja
# What modules does for example
- podman_volume:
    state: present
    name: volume1
    label:
      key: value
      key2: value2
    options:
      - "device=/dev/loop1"
      - "type=ext4"
```

## [Return Values](podman_volume_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **volume**  dictionary | Volume inspection results if exists.  **Returned:** always  **Sample:** `{"CreatedAt": "2020-06-05T16:38:55.277628769+03:00", "Driver": "local", "Labels": {"key.com": "value", "key.org": "value2"}, "Mountpoint": "/home/user/.local/share/containers/storage/volumes/test/_data", "Name": "test", "Options": {}, "Scope": "local"}` |

### Authors

- Sagi Shnaidman (@sshnaidm)

### Collection links

- [Issue Tracker](https://github.com/containers/ansible-podman-collections/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/containers/ansible-podman-collections.git)
