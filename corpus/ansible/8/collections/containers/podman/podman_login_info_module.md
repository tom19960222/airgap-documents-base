---
collection: ansible
version: "8"
title: "containers.podman.podman_login_info module – Return the logged-in user if any for a given registry"
source_url: https://docs.ansible.com/projects/ansible/8/collections/containers/podman/podman_login_info_module.html
fetched_at: 2026-07-28T02:03:10+00:00
---
# containers.podman.podman_login_info module – Return the logged-in user if any for a given registry

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
> see [Requirements](podman_login_info_module.md#ansible-collections-containers-podman-podman-login-info-module-requirements) for details.
>
> To use it in a playbook, specify: `containers.podman.podman_login_info`.

New in containers.podman 1.0.0

- [Synopsis](podman_login_info_module.md#synopsis)
- [Requirements](podman_login_info_module.md#requirements)
- [Parameters](podman_login_info_module.md#parameters)
- [Examples](podman_login_info_module.md#examples)
- [Return Values](podman_login_info_module.md#return-values)

## [Synopsis](podman_login_info_module.md#id1)

- Return the logged-in user if any for a given registry.

## [Requirements](podman_login_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- Podman installed on host

## [Parameters](podman_login_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **authfile**  path | Path of the authentication file. Default is ``${XDG_RUNTIME_DIR}/containers/auth.json`` (Not available for remote commands) You can also override the default path of the authentication file by setting the ``REGISTRY_AUTH_FILE`` environment variable. ``export REGISTRY_AUTH_FILE=path`` |
| **executable**  string | Path to `podman` executable if it is not in the `$PATH` on the machine running `podman`  **Default:** `"podman"` |
| **registry**  string / required | Registry server. |

## [Examples](podman_login_info_module.md#id4)

```yaml+jinja
- name: Return the logged-in user for docker hub registry
  containers.podman.podman_login_info:
    registry: docker.io

- name: Return the logged-in user for quay.io registry
  containers.podman.podman_login_info:
    registry: quay.io
```

## [Return Values](podman_login_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **login**  dictionary | Logged in user for a registry  **Returned:** always  **Sample:** `{"logged_in": true, "registry": "docker.io", "username": "clelange"}` |

### Authors

- Clemens Lange (@clelange)

### Collection links

- [Issue Tracker](https://github.com/containers/ansible-podman-collections/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/containers/ansible-podman-collections.git)
