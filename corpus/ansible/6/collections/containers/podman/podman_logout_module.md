---
collection: ansible
version: "6"
title: "containers.podman.podman_logout module – Log out of a container registry using podman"
source_url: https://docs.ansible.com/projects/ansible/6/collections/containers/podman/podman_logout_module.html
fetched_at: 2026-07-27T17:24:34+00:00
---
# containers.podman.podman_logout module – Log out of a container registry using podman

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
> see [Requirements](podman_logout_module.md#ansible-collections-containers-podman-podman-logout-module-requirements) for details.
>
> To use it in a playbook, specify: `containers.podman.podman_logout`.

- [Synopsis](podman_logout_module.md#synopsis)
- [Requirements](podman_logout_module.md#requirements)
- [Parameters](podman_logout_module.md#parameters)
- [Examples](podman_logout_module.md#examples)

## [Synopsis](podman_logout_module.md#id1)

- Log out of a container registry server using the podman logout command by deleting the cached credentials stored in the `auth.json` file. If the registry is not specified, the first registry under `[registries.search]` from `registries.conf `will be used. The path of the authentication file can be overridden by the user by setting the `authfile` flag. The default path used is `${XDG_RUNTIME_DIR}/containers/auth.json`. All the cached credentials can be removed by setting the `all` flag. Warning - podman will use credentials in `${HOME}/.docker/config.json` to authenticate in case they are not found in the default `authfile`. However, the logout command will only removed credentials in the `authfile` specified.

## [Requirements](podman_logout_module.md#id2)

The below requirements are needed on the host that executes this module.

- Podman installed on host

## [Parameters](podman_logout_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **all**  boolean | Remove the cached credentials for all registries in the auth file.  Choices:   - `false` - `true` |
| **authfile**  path | Path of the authentication file. Default is ``${XDG_RUNTIME_DIR}/containers/auth.json`` You can also override the default path of the authentication file by setting the ``REGISTRY_AUTH_FILE`` environment variable. ``export REGISTRY_AUTH_FILE=path`` |
| **executable**  string | Path to `podman` executable if it is not in the `$PATH` on the machine running `podman`  Default: `"podman"` |
| **ignore_docker_credentials**  boolean | Credentials created using other tools such as `docker login` are not removed unless the corresponding `authfile` is explicitly specified. Since podman also uses existing credentials in these files by default (for docker e.g. `${HOME}/.docker/config.json`), module execution will fail if a docker login exists for the registry specified in any `authfile` is used by podman. This can be ignored by setting `ignore_docker_credentials` to `yes` - the credentials will be kept and `changed` will be false. This option cannot be used together with `all` since in this case podman will not check for existing `authfiles` created by other tools.  Choices:   - `false` - `true` |
| **registry**  string | Registry server. If the registry is not specified, the first registry under `[registries.search]` from `registries.conf` will be used. |

## [Examples](podman_logout_module.md#id4)

```yaml+jinja
- name: Log out of default registry
  podman_logout:

- name: Log out of quay.io
  podman_logout:
    registry: quay.io

- name: Log out of all registries in auth file
  podman_logout:
    all: yes

- name: Log out of all registries in specified auth file
  podman_logout:
    authfile: $HOME/.docker/config.json
    all: yes
```

### Authors

- Clemens Lange (@clelange)

### Collection links

[Issue Tracker](https://github.com/containers/ansible-podman-collections/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/containers/ansible-podman-collections.git)
