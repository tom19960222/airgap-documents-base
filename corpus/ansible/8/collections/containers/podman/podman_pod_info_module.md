---
collection: ansible
version: "8"
title: "containers.podman.podman_pod_info module – Gather info about podman pods"
source_url: https://docs.ansible.com/projects/ansible/8/collections/containers/podman/podman_pod_info_module.html
fetched_at: 2026-07-28T02:03:14+00:00
---
# containers.podman.podman_pod_info module – Gather info about podman pods

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
> see [Requirements](podman_pod_info_module.md#ansible-collections-containers-podman-podman-pod-info-module-requirements) for details.
>
> To use it in a playbook, specify: `containers.podman.podman_pod_info`.

New in containers.podman 1.0.0

- [Synopsis](podman_pod_info_module.md#synopsis)
- [Requirements](podman_pod_info_module.md#requirements)
- [Parameters](podman_pod_info_module.md#parameters)
- [Examples](podman_pod_info_module.md#examples)
- [Return Values](podman_pod_info_module.md#return-values)

## [Synopsis](podman_pod_info_module.md#id1)

- Gather info about podman pods with podman inspect command.

## [Requirements](podman_pod_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- Podman installed on host

## [Parameters](podman_pod_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **executable**  string | Path to `podman` executable if it is not in the `$PATH` on the machine running `podman`  **Default:** `"podman"` |
| **name**  string | Name of the pod |

## [Examples](podman_pod_info_module.md#id4)

```yaml+jinja
- name: Gather info about all present pods
  containers.podman.podman_pod_info:

- name: Gather info about specific pods
  containers.podman.podman_pod_info:
    name: special_pod
```

## [Return Values](podman_pod_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **pods**  list / elements=string | Facts from all or specified pods  **Returned:** always  **Sample:** `[{"Config": {"cgroupParent": "/libpod_parent", "created": "2020-07-13T20:29:12.572282186+03:00", "hostname": "pod1host", "id": "d9cb6dbb0....", "infraConfig": {"infraPortBindings": [{"containerPort": 7111, "hostIP": "", "hostPort": 7777, "protocol": "tcp"}], "makeInfraContainer": true}, "labels": {}, "lockID": 682, "name": "pod1", "sharesCgroup": true, "sharesIpc": true, "sharesNet": true, "sharesUts": true}, "Containers": [{"id": "ad46737bf....", "state": "configured"}], "State": {"cgroupPath": "/libpod_parent/d9cb6dbb0....", "infraContainerID": "ad46737bf....", "status": "Created"}}]` |

### Authors

- Sagi Shnaidman (@sshnaidm)

### Collection links

- [Issue Tracker](https://github.com/containers/ansible-podman-collections/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/containers/ansible-podman-collections.git)
