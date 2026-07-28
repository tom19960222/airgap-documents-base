---
collection: ansible
version: "6"
title: "containers.podman.buildah connection – Interact with an existing buildah container"
source_url: https://docs.ansible.com/projects/ansible/6/collections/containers/podman/buildah_connection.html
fetched_at: 2026-07-27T17:24:42+00:00
---
# containers.podman.buildah connection – Interact with an existing buildah container

> **Note:**
>
> This connection plugin is part of the [containers.podman collection](https://galaxy.ansible.com/containers/podman) (version 1.10.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install containers.podman`.
>
> To use it in a playbook, specify: `containers.podman.buildah`.

- [Synopsis](buildah_connection.md#synopsis)
- [Parameters](buildah_connection.md#parameters)

## [Synopsis](buildah_connection.md#id1)

- Run commands or put/fetch files to an existing container using buildah tool.

## [Parameters](buildah_connection.md#id2)

| Parameter | Comments |
| --- | --- |
| **remote_addr**  string | The ID of the container you want to access.  Default: `"inventory_hostname"`  Configuration:   - Variable: ansible_host |
| **remote_user**  string | User specified via name or ID which is used to execute commands inside the container.  Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   remote_user = VALUE   ``` - Environment variable: [`ANSIBLE_REMOTE_USER`](../../../reference_appendices/config.md#envvar-ANSIBLE_REMOTE_USER) - Variable: ansible_user |

### Authors

- Tomas Tomecek (@TomasTomecek)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/containers/ansible-podman-collections/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/containers/ansible-podman-collections.git)
