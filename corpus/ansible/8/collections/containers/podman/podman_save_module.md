---
collection: ansible
version: "8"
title: "containers.podman.podman_save module – Saves podman image to tar file"
source_url: https://docs.ansible.com/projects/ansible/8/collections/containers/podman/podman_save_module.html
fetched_at: 2026-07-28T02:03:16+00:00
---
# containers.podman.podman_save module – Saves podman image to tar file

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
> see [Requirements](podman_save_module.md#ansible-collections-containers-podman-podman-save-module-requirements) for details.
>
> To use it in a playbook, specify: `containers.podman.podman_save`.

- [Synopsis](podman_save_module.md#synopsis)
- [Requirements](podman_save_module.md#requirements)
- [Parameters](podman_save_module.md#parameters)
- [Examples](podman_save_module.md#examples)

## [Synopsis](podman_save_module.md#id1)

- podman save saves an image to either docker-archive, oci-archive, oci-dir (directory with oci manifest type), or docker-dir (directory with v2s2 manifest type) on the local machine, default is docker-archive.

## [Requirements](podman_save_module.md#id2)

The below requirements are needed on the host that executes this module.

- Podman installed on host

## [Parameters](podman_save_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **compress**  boolean | Compress tarball image layers when pushing to a directory using the ‘dir’ transport. (default is same compression type, compressed or uncompressed, as source)  **Choices:**   - `false` - `true` |
| **dest**  aliases: path  string / required | Destination file to write image to. |
| **executable**  string | Path to `podman` executable if it is not in the `$PATH` on the machine running `podman`  **Default:** `"podman"` |
| **force**  boolean | Force saving to file even if it exists.  **Choices:**   - `false` - `true` ← (default) |
| **format**  string | Save image to docker-archive, oci-archive (see containers-transports(5)), oci-dir (oci transport), or docker-dir (dir transport with v2s2 manifest type).  **Choices:**   - `"docker-archive"` - `"oci-archive"` - `"oci-dir"` - `"docker-dir"` |
| **image**  string / required | Image to save. |
| **multi_image_archive**  boolean | Allow for creating archives with more than one image. Additional names will be interpreted as images instead of tags. Only supported for docker-archive.  **Choices:**   - `false` - `true` |

## [Examples](podman_save_module.md#id4)

```yaml+jinja
# What modules does for example
- containers.podman.podman_save:
    dest: /path/to/tar/file
    compress: true
    format: oci-dir
```

### Authors

- Sagi Shnaidman (@sshnaidm)

### Collection links

- [Issue Tracker](https://github.com/containers/ansible-podman-collections/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/containers/ansible-podman-collections.git)
