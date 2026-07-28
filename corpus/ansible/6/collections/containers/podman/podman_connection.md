---
collection: ansible
version: "6"
title: "containers.podman.podman connection – Interact with an existing podman container"
source_url: https://docs.ansible.com/projects/ansible/6/collections/containers/podman/podman_connection.html
fetched_at: 2026-07-27T16:43:25+00:00
---
# containers.podman.podman connection – Interact with an existing podman container

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
> To use it in a playbook, specify: `containers.podman.podman`.

- [Synopsis](podman_connection.md#synopsis)
- [Parameters](podman_connection.md#parameters)

## [Synopsis](podman_connection.md#id1)

- Run commands or put/fetch files to an existing container using podman tool.

## [Parameters](podman_connection.md#id2)

| Parameter | Comments |
| --- | --- |
| **podman_executable**  string | Executable for podman command.  Default: `"podman"`  Configuration:   - Environment variable: [`ANSIBLE_PODMAN_EXECUTABLE`](../../environment_variables.md#envvar-ANSIBLE_PODMAN_EXECUTABLE) - Variable: ansible_podman_executable |
| **podman_extra_args**  string | Extra arguments to pass to the podman command line.  Default: `""`  Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   podman_extra_args = ""   ``` - Environment variable: [`ANSIBLE_PODMAN_EXTRA_ARGS`](../../environment_variables.md#envvar-ANSIBLE_PODMAN_EXTRA_ARGS) - Variable: ansible_podman_extra_args |
| **remote_addr**  string | The ID of the container you want to access.  Default: `"inventory_hostname"`  Configuration:   - Variable: ansible_host - Variable: inventory_hostname - Variable: ansible_podman_host |
| **remote_user**  string | User specified via name or UID which is used to execute commands inside the container. If you specify the user via UID, you must set `ANSIBLE_REMOTE_TMP` to a path that exits inside the container and is writable by Ansible.  Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   remote_user = VALUE   ``` - Environment variable: [`ANSIBLE_REMOTE_USER`](../../../reference_appendices/config.md#envvar-ANSIBLE_REMOTE_USER) - Variable: ansible_user |

### Authors

- Tomas Tomecek (@TomasTomecek)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/containers/ansible-podman-collections/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/containers/ansible-podman-collections.git)
