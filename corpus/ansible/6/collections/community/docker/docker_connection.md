---
collection: ansible
version: "6"
title: "community.docker.docker connection – Run tasks in docker containers"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/docker/docker_connection.html
fetched_at: 2026-07-27T17:07:32+00:00
---
# community.docker.docker connection – Run tasks in docker containers

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
> To use it in a playbook, specify: `community.docker.docker`.

- [Synopsis](docker_connection.md#synopsis)
- [Parameters](docker_connection.md#parameters)

## [Synopsis](docker_connection.md#id1)

- Run commands or put/fetch files to an existing docker container.
- Uses the Docker CLI to execute commands in the container. If you prefer to directly connect to the Docker daemon, use the [community.docker.docker_api](docker_api_connection.md#ansible-collections-community-docker-docker-api-connection) connection plugin.

## [Parameters](docker_connection.md#id2)

| Parameter | Comments |
| --- | --- |
| **container_timeout**  integer | Controls how long we can wait to access reading output from the container once execution started.  Default: `10`  Configuration:   - INI entries:  ```YAML+Jinja   [defaults]   timeout = 10   ```  ```YAML+Jinja   [docker_connection]   timeout = 10   ```  added in community.docker 2.2.0 - Environment variable: [`ANSIBLE_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_TIMEOUT) - Environment variable: [`ANSIBLE_DOCKER_TIMEOUT`](../../environment_variables.md#envvar-ANSIBLE_DOCKER_TIMEOUT)  added in community.docker 2.2.0 - Variable: ansible_docker_timeout  added in community.docker 2.2.0 - CLI argument: –timeout |
| **docker_extra_args**  string | Extra arguments to pass to the docker command line.  Default: `""`  Configuration:   - INI entry:  ```YAML+Jinja   [docker_connection]   extra_cli_args = ""   ``` - Variable: ansible_docker_extra_args |
| **remote_addr**  string | The name of the container you want to access.  Default: `"inventory_hostname"`  Configuration:   - Variable: inventory_hostname - Variable: ansible_host - Variable: ansible_docker_host |
| **remote_user**  string | The user to execute as inside the container.  If Docker is too old to allow this (< 1.7), the one set by Docker itself will be used.  Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   remote_user = VALUE   ``` - Environment variable: [`ANSIBLE_REMOTE_USER`](../../../reference_appendices/config.md#envvar-ANSIBLE_REMOTE_USER) - Variable: ansible_user - Variable: ansible_docker_user - Keyword: remote_user - CLI argument: –user |

### Authors

- Lorin Hochestein
- Leendert Brouwer

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.docker/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.docker)
[Submit a bug report](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-docker)
