---
collection: ansible
version: "8"
title: "containers.podman.podman_container_exec module – Executes a command in a running container."
source_url: https://docs.ansible.com/projects/ansible/8/collections/containers/podman/podman_container_exec_module.html
fetched_at: 2026-07-28T02:03:03+00:00
---
# containers.podman.podman_container_exec module – Executes a command in a running container.

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
> see [Requirements](podman_container_exec_module.md#ansible-collections-containers-podman-podman-container-exec-module-requirements) for details.
>
> To use it in a playbook, specify: `containers.podman.podman_container_exec`.

- [Synopsis](podman_container_exec_module.md#synopsis)
- [Requirements](podman_container_exec_module.md#requirements)
- [Parameters](podman_container_exec_module.md#parameters)
- [Notes](podman_container_exec_module.md#notes)
- [Examples](podman_container_exec_module.md#examples)
- [Return Values](podman_container_exec_module.md#return-values)

## [Synopsis](podman_container_exec_module.md#id1)

- Executes a command in a running container.

## [Requirements](podman_container_exec_module.md#id2)

The below requirements are needed on the host that executes this module.

- podman

## [Parameters](podman_container_exec_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **argv**  list / elements=string | Passes the command as a list rather than a string.  One of the *command* or *args* is required. |
| **command**  string | The command to run in the container.  One of the *command* or *args* is required. |
| **detach**  boolean | If true, the command runs in the background.  The exec session is automatically removed when it completes.  **Choices:**   - `false` ← (default) - `true` |
| **env**  dictionary | Set environment variables. |
| **name**  string / required | Name of the container where the command is executed. |
| **privileged**  boolean | Give extended privileges to the container.  **Choices:**   - `false` ← (default) - `true` |
| **tty**  boolean | Allocate a pseudo-TTY.  **Choices:**   - `false` ← (default) - `true` |
| **user**  string | The username or UID used and, optionally, the groupname or GID for the specified command.  Both user and group may be symbolic or numeric. |
| **workdir**  string | Working directory inside the container. |

## [Notes](podman_container_exec_module.md#id4)

> **Note:**
>
> - See [the Podman documentation](https://docs.podman.io/en/latest/markdown/podman-exec.1.html) for details of podman-exec(1).

## [Examples](podman_container_exec_module.md#id5)

```yaml+jinja
- name: Execute a command with workdir
  containers.podman.podman_container_exec:
    name: ubi8
    command: "cat redhat-release"
    workdir: /etc

- name: Execute a command with a list of args and environment variables
  containers.podman.podman_container_exec:
    name: test_container
    argv:
      - /bin/sh
      - -c
      - echo $HELLO $BYE
    env:
      HELLO: hello world
      BYE: goodbye world

- name: Execute command in background by using detach
  containers.podman.podman_container_exec:
    name: detach_container
    command: "cat redhat-release"
    detach: true
```

## [Return Values](podman_container_exec_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **exec_id**  string | The ID of the exec session.  **Returned:** success and *detach=true*  **Sample:** `"f99002e34c1087fd1aa08d5027e455bf7c2d6b74f019069acf6462a96ddf2a47"` |
| **rc**  integer | The exit code of the command executed in the container.  **Returned:** success  **Sample:** `0` |
| **stderr**  string | The standard output of the command executed in the container.  **Returned:** success |
| **stdout**  string | The standard output of the command executed in the container.  **Returned:** success |

### Authors

- Takuya Nishimura (@nishipy)

### Collection links

- [Issue Tracker](https://github.com/containers/ansible-podman-collections/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/containers/ansible-podman-collections.git)
