---
collection: ansible
version: "6"
title: "containers.podman.podman_login module – Login to a container registry using podman"
source_url: https://docs.ansible.com/projects/ansible/6/collections/containers/podman/podman_login_module.html
fetched_at: 2026-07-27T17:24:33+00:00
---
# containers.podman.podman_login module – Login to a container registry using podman

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
> see [Requirements](podman_login_module.md#ansible-collections-containers-podman-podman-login-module-requirements) for details.
>
> To use it in a playbook, specify: `containers.podman.podman_login`.

- [Synopsis](podman_login_module.md#synopsis)
- [Requirements](podman_login_module.md#requirements)
- [Parameters](podman_login_module.md#parameters)
- [Examples](podman_login_module.md#examples)

## [Synopsis](podman_login_module.md#id1)

- Login to a container registry server using the podman login command If the registry is not specified, the first registry under `[registries.search]` from `registries.conf `will be used. The path of the authentication file can be overridden by the user by setting the `authfile` flag. The default path used is `${XDG_RUNTIME_DIR}/containers/auth.json`.

## [Requirements](podman_login_module.md#id2)

The below requirements are needed on the host that executes this module.

- Podman installed on host

## [Parameters](podman_login_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **authfile**  path | Path of the authentication file. Default is ``${XDG_RUNTIME_DIR}/containers/auth.json`` You can also override the default path of the authentication file by setting the ``REGISTRY_AUTH_FILE`` environment variable. ``export REGISTRY_AUTH_FILE=path`` |
| **certdir**  path | Use certificates at path (\*.crt, \*.cert, \*.key) to connect to the registry. Default certificates directory is /etc/containers/certs.d. |
| **executable**  string | Path to `podman` executable if it is not in the `$PATH` on the machine running `podman`  Default: `"podman"` |
| **password**  string / required | Password for the registry server. |
| **registry**  string | Registry server. If the registry is not specified, the first registry under `[registries.search]` from `registries.conf` will be used. |
| **tlsverify**  boolean | Require HTTPS and verify certificates when contacting registries. If explicitly set to true, then TLS verification will be used. If set to false, then TLS verification will not be used. If not specified, TLS verification will be used unless the target registry is listed as an insecure registry in registries.conf.  Choices:   - `false` - `true` |
| **username**  string / required | Username for the registry server. |

## [Examples](podman_login_module.md#id4)

```yaml+jinja
- name: Login to default registry and create ${XDG_RUNTIME_DIR}/containers/auth.json
  containers.podman.podman_login:
    username: user
    password: 'p4ssw0rd'

- name: Login to default registry and create ${XDG_RUNTIME_DIR}/containers/auth.json
  containers.podman.podman_login:
    username: user
    password: 'p4ssw0rd'
    registry: quay.io
```

### Authors

- Jason Hiatt (@jthiatt)
- Clemens Lange (@clelange)

### Collection links

[Issue Tracker](https://github.com/containers/ansible-podman-collections/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/containers/ansible-podman-collections.git)
