---
collection: ansible
version: "8"
title: "containers.podman.podman_import module – Import Podman container from a tar file."
source_url: https://docs.ansible.com/projects/ansible/8/collections/containers/podman/podman_import_module.html
fetched_at: 2026-07-28T02:03:08+00:00
---
# containers.podman.podman_import module – Import Podman container from a tar file.

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
> see [Requirements](podman_import_module.md#ansible-collections-containers-podman-podman-import-module-requirements) for details.
>
> To use it in a playbook, specify: `containers.podman.podman_import`.

- [Synopsis](podman_import_module.md#synopsis)
- [Requirements](podman_import_module.md#requirements)
- [Parameters](podman_import_module.md#parameters)
- [Examples](podman_import_module.md#examples)
- [Return Values](podman_import_module.md#return-values)

## [Synopsis](podman_import_module.md#id1)

- podman import imports a tarball (.tar, .tar.gz, .tgz, .bzip, .tar.xz, .txz) and saves it as a filesystem image.

## [Requirements](podman_import_module.md#id2)

The below requirements are needed on the host that executes this module.

- Podman installed on host

## [Parameters](podman_import_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **change**  list / elements=dictionary | Set changes as list of key-value pairs, see example. |
| **commit_message**  string | Set commit message for imported image |
| **executable**  string | Path to `podman` executable if it is not in the `$PATH` on the machine running `podman`  **Default:** `"podman"` |
| **src**  string / required | Path to image file to load. |
| **volume**  string | Volume to import, cannot be used with change and commit_message |

## [Examples](podman_import_module.md#id4)

```yaml+jinja
# What modules does for example
- containers.podman.podman_import:
    src: /path/to/tar/file
    change:
      - "CMD": /bin/bash
      - "User": root
    commit_message: "Importing image"
- containers.podman.podman_import:
    src: /path/to/tar/file
    volume: myvolume
```

## [Return Values](podman_import_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **image**  dictionary | info from loaded image  **Returned:** always  **Sample:** `{"Annotations": {}, "Architecture": "amd64", "Author": "", "Comment": "imported from tarball", "Config": {}, "Created": "2021-09-07T04:45:38.749977105+03:00", "Digest": "sha256:8730c75be86a718929a658db4663d487e562d66762....", "GraphDriver": {"Data": {"UpperDir": "/home/...34/diff", "WorkDir": "/home/.../work"}, "Name": "overlay"}, "History": [{"comment": "imported from tarball", "created": "2021-09-07T04:45:38.749977105+03:00", "created_by": "/bin/sh -c #(nop) ADD file:091... in /"}], "Id": "cbc6d73c4d232db6e8441df96af81855f62c74157b5db80a1d5...", "Labels": null, "ManifestType": "application/vnd.oci.image.manifest.v1+json", "NamesHistory": null, "Os": "linux", "Parent": "", "RepoDigests": [], "RepoTags": [], "RootFS": {"Layers": ["sha256:...."], "Type": "layers"}, "Size": 5882449, "User": "", "Version": "", "VirtualSize": 5882449}` |

### Authors

- Sagi Shnaidman (@sshnaidm)

### Collection links

- [Issue Tracker](https://github.com/containers/ansible-podman-collections/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/containers/ansible-podman-collections.git)
