---
collection: ansible
version: "6"
title: "community.docker.nsenter connection – execute on host running controller container"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/docker/nsenter_connection.html
fetched_at: 2026-07-27T17:07:33+00:00
---
# community.docker.nsenter connection – execute on host running controller container

> **Note:**
>
> This connection plugin is part of the [community.docker collection](https://galaxy.ansible.com/community/docker) (version 2.7.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.docker`.
>
> To use it in a playbook, specify: `community.docker.nsenter`.

New in community.docker 1.9.0

- [Synopsis](nsenter_connection.md#synopsis)
- [Parameters](nsenter_connection.md#parameters)
- [Notes](nsenter_connection.md#notes)

## [Synopsis](nsenter_connection.md#id1)

- This connection plugin allows Ansible, running in a privileged container, to execute tasks on the container host instead of in the container itself.
- This is useful for running Ansible in a pull model, while still keeping the Ansible control node containerized.
- It relies on having privileged access to run `nsenter` in the host’s PID namespace, allowing it to enter the namespaces of the provided PID (default PID 1, or init/systemd).

## [Parameters](nsenter_connection.md#id2)

| Parameter | Comments |
| --- | --- |
| **nsenter_pid**  integer | PID to attach with using nsenter.  The default should be fine unless you are attaching as a non-root user.  Default: `1`  Configuration:   - INI entry:  ```YAML+Jinja   [nsenter_connection]   nsenter_pid = 1   ``` - Environment variable: [`ANSIBLE_NSENTER_PID`](../../environment_variables.md#envvar-ANSIBLE_NSENTER_PID) - Variable: ansible_nsenter_pid |

## [Notes](nsenter_connection.md#id3)

> **Note:**
>
> - The remote user is ignored; this plugin always runs as root.
> - This plugin requires the Ansible controller container to be launched in the following way: (1) The container image contains the `nsenter` program; (2) The container is launched in privileged mode; (3) The container is launched in the host’s PID namespace (`--pid host`).

### Authors

- Jeff Goldschrafe (@jgoldschrafe)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.docker/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.docker)
[Submit a bug report](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-docker)
