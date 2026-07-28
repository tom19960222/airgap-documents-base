---
collection: ansible
version: "6"
title: "containers.podman.podman_generate_systemd module – Generate systemd unit from a pod or a container"
source_url: https://docs.ansible.com/projects/ansible/6/collections/containers/podman/podman_generate_systemd_module.html
fetched_at: 2026-07-27T17:24:30+00:00
---
# containers.podman.podman_generate_systemd module – Generate systemd unit from a pod or a container

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
> see [Requirements](podman_generate_systemd_module.md#ansible-collections-containers-podman-podman-generate-systemd-module-requirements) for details.
>
> To use it in a playbook, specify: `containers.podman.podman_generate_systemd`.

- [Synopsis](podman_generate_systemd_module.md#synopsis)
- [Requirements](podman_generate_systemd_module.md#requirements)
- [Parameters](podman_generate_systemd_module.md#parameters)
- [Notes](podman_generate_systemd_module.md#notes)
- [Examples](podman_generate_systemd_module.md#examples)
- [Return Values](podman_generate_systemd_module.md#return-values)

## [Synopsis](podman_generate_systemd_module.md#id1)

- Generate systemd .service unit file(s) from a pod or a container
- Support Ansible check mode

## [Requirements](podman_generate_systemd_module.md#id2)

The below requirements are needed on the host that executes this module.

- Podman installed on target host

## [Parameters](podman_generate_systemd_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **after**  list / elements=string | Add the systemd unit after (`After=`) option, that ordering dependencies between the list of dependencies and this service.  This option may be specified more than once.  User-defined dependencies will be appended to the generated unit file  But any existing options such as needed or defined by default (e.g. `online.target`) will not be removed or overridden.  Only with Podman 4.0.0 and above |
| **container_prefix**  string | Set the systemd unit name prefix for containers.  If not set, use the default defined by podman, `container`.  Refer to podman-generate-systemd(1) man page for more information. |
| **dest**  path | Destination of the generated systemd unit file(s) |
| **env**  dictionary | Set environment variables to the systemd unit files.  Keys are the environment variable names, and values are the environment variable values  Only with Podman 4.3.0 and above |
| **executable**  string | `Podman` executable name or full path  Default: `"podman"` |
| **name**  string / required | Name of the pod or container to export |
| **new**  boolean | Generate unit files that create containers and pods, not only start them.  Refer to podman-generate-systemd(1) man page for more information.  Choices:   - `false` ← (default) - `true` |
| **no_header**  boolean | Do not generate the header including meta data such as the Podman version and the timestamp.  Choices:   - `false` ← (default) - `true` |
| **pod_prefix**  string | Set the systemd unit name prefix for pods.  If not set, use the default defined by podman, `pod`.  Refer to podman-generate-systemd(1) man page for more information. |
| **requires**  list / elements=string | Set the systemd unit requires (Requires=) option.  Similar to wants, but declares a stronger requirement dependency.  Only with Podman 4.0.0 and above |
| **restart_policy**  string | Restart policy of the service  Choices:   - `"no-restart"` - `"on-success"` - `"on-failure"` - `"on-abnormal"` - `"on-watchdog"` - `"on-abort"` - `"always"` |
| **restart_sec**  integer | Configures the time to sleep before restarting a service (as configured with restart-policy).  Takes a value in seconds.  Only with Podman 4.0.0 and above |
| **separator**  string | Systemd unit name separator between the name/id of a container/pod and the prefix.  If not set, use the default defined by podman, `-`.  Refer to podman-generate-systemd(1) man page for more information. |
| **start_timeout**  integer | Override the default start timeout for the container with the given value in seconds.  Only with Podman 4.0.0 and above |
| **stop_timeout**  integer | Override the default stop timeout for the container with the given value in seconds. |
| **use_names**  boolean | Use name of the containers for the start, stop, and description in the unit file.  Choices:   - `false` - `true` ← (default) |
| **wants**  list / elements=string | Add the systemd unit wants (`Wants=`) option, that this service is (weak) dependent on.  This option may be specified more than once.  This option does not influence the order in which services are started or stopped.  User-defined dependencies will be appended to the generated unit file  But any existing options such as needed or defined by default (e.g. `online.target`) will not be removed or overridden.  Only with Podman 4.0.0 and above |

## [Notes](podman_generate_systemd_module.md#id4)

> **Note:**
>
> - You can store your systemd unit files in `/etc/systemd/user/` for system wide usage
> - Or you can store them in `~/.config/systemd/user/` for usage at a specific user
> - If you indicate a pod, the systemd units for it and all its containers will be generated
> - Create all your pods, containers and their dependencies before generating the systemd files
> - If a container or pod is already started before you do a `systemctl daemon reload`, systemd will not see the container or pod as started
> - Stop your container or pod before you do a `systemctl daemon reload`, then you can start them with `systemctl start my_container.service`

## [Examples](podman_generate_systemd_module.md#id5)

```yaml+jinja
# Exemple of creating a container and integrate it into systemd
- name: A postgres container must exist, stopped
  containers.podman.podman_container:
    name: postgres_local
    image: docker.io/library/postgres:latest
    state: stopped

- name: Systemd unit files for postgres container must exist
  containers.podman.podman_generate_systemd:
    name: postgres_local
    dest: ~/.config/systemd/user/

- name: Postgres container must be started and enabled on systemd
  ansible.builtin.systemd:
    name: container-postgres_local
    daemon_reload: yes
    state: started
    enabled: yes

# Generate the unit files, but store them on an Ansible variable
# instead of writting them on target host
- name: Systemd unit files for postgres container must be generated
  containers.podman.podman_generate_systemd:
    name: postgres_local
  register: postgres_local_systemd_unit

# Generate the unit files with environment variables sets
- name: Systemd unit files for postgres container must be generated
  containers.podman.podman_generate_systemd:
    name: postgres_local
    env:
      POSTGRES_USER: my_app
      POSTGRES_PASSWORD: example
  register: postgres_local_systemd_unit
```

## [Return Values](podman_generate_systemd_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **podman_command**  string | A copy of the podman command used to generate the systemd unit(s)  Returned: always  Sample: `"podman generate systemd my_webapp"` |
| **systemd_units**  dictionary | A copy of the generated systemd .service unit(s)  Returned: always  Sample: `{"container-postgres_local": " #Content of the systemd .servec unit for postgres_local container", "pod-my_webapp": " #Content of the systemd .servec unit for my_webapp pod"}` |

### Authors

- Sébastien Gendre (@CyberFox001)

### Collection links

[Issue Tracker](https://github.com/containers/ansible-podman-collections/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/containers/ansible-podman-collections.git)
