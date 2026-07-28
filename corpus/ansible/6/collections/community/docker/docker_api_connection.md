---
collection: ansible
version: "6"
title: "community.docker.docker_api connection – Run tasks in docker containers"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/docker/docker_api_connection.html
fetched_at: 2026-07-27T17:07:33+00:00
---
# community.docker.docker_api connection – Run tasks in docker containers

> **Note:**
>
> This connection plugin is part of the [community.docker collection](https://galaxy.ansible.com/community/docker) (version 2.7.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.docker`.
> You need further requirements to be able to use this connection plugin,
> see [Requirements](docker_api_connection.md#ansible-collections-community-docker-docker-api-connection-requirements) for details.
>
> To use it in a playbook, specify: `community.docker.docker_api`.

New in community.docker 1.1.0

- [Synopsis](docker_api_connection.md#synopsis)
- [Requirements](docker_api_connection.md#requirements)
- [Parameters](docker_api_connection.md#parameters)
- [Notes](docker_api_connection.md#notes)

## [Synopsis](docker_api_connection.md#id1)

- Run commands or put/fetch files to an existing docker container.
- Uses Docker SDK for Python to interact directly with the Docker daemon instead of using the Docker CLI. Use the [community.docker.docker](docker_connection.md#ansible-collections-community-docker-docker-connection) connection plugin if you want to use the Docker CLI.

## [Requirements](docker_api_connection.md#id2)

The below requirements are needed on the local controller node that executes this connection.

- Docker SDK for Python: Please note that the [docker-py](https://pypi.org/project/docker-py/) Python module has been superseded by [docker](https://pypi.org/project/docker/) (see [here](https://github.com/docker/docker-py/issues/1310) for details). For Python 2.6, `docker-py` must be used. Otherwise, it is recommended to install the `docker` Python module. Note that both modules should \*not\* be installed at the same time. Also note that when both modules are installed and one of them is uninstalled, the other might no longer function and a reinstall of it is required.

## [Parameters](docker_api_connection.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_version**  aliases: docker_api_version  string | The version of the Docker API running on the Docker Host.  Defaults to the latest version of the API supported by Docker SDK for Python and the docker daemon.  If the value is not specified in the task, the value of environment variable `DOCKER_API_VERSION` will be used instead. If the environment variable is not set, the default value will be used.  Default: `"auto"`  Configuration:   - Variable: ansible_docker_api_version |
| **ca_cert**  aliases: tls_ca_cert, cacert_path  path | Use a CA certificate when performing server verification by providing the path to a CA certificate file.  If the value is not specified in the task and the environment variable `DOCKER_CERT_PATH` is set, the file `ca.pem` from the directory specified in the environment variable `DOCKER_CERT_PATH` will be used.  Configuration:   - Variable: ansible_docker_ca_cert |
| **client_cert**  aliases: tls_client_cert, cert_path  path | Path to the client’s TLS certificate file.  If the value is not specified in the task and the environment variable `DOCKER_CERT_PATH` is set, the file `cert.pem` from the directory specified in the environment variable `DOCKER_CERT_PATH` will be used.  Configuration:   - Variable: ansible_docker_client_cert |
| **client_key**  aliases: tls_client_key, key_path  path | Path to the client’s TLS key file.  If the value is not specified in the task and the environment variable `DOCKER_CERT_PATH` is set, the file `key.pem` from the directory specified in the environment variable `DOCKER_CERT_PATH` will be used.  Configuration:   - Variable: ansible_docker_client_key |
| **container_timeout**  integer | Controls how long we can wait to access reading output from the container once execution started.  Default: `10`  Configuration:   - INI entries:  ```YAML+Jinja   [defaults]   timeout = 10   ```  ```YAML+Jinja   [docker_connection]   timeout = 10   ```  added in community.docker 2.2.0 - Environment variable: [`ANSIBLE_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_TIMEOUT) - Environment variable: [`ANSIBLE_DOCKER_TIMEOUT`](../../environment_variables.md#envvar-ANSIBLE_DOCKER_TIMEOUT)  added in community.docker 2.2.0 - Variable: ansible_docker_timeout  added in community.docker 2.2.0 - CLI argument: –timeout |
| **debug**  boolean | Debug mode  Choices:   - `false` ← (default) - `true` |
| **docker_host**  aliases: docker_url  string | The URL or Unix socket path used to connect to the Docker API. To connect to a remote host, provide the TCP connection string. For example, `tcp://192.0.2.23:2376`. If TLS is used to encrypt the connection, the module will automatically replace `tcp` in the connection URL with `https`.  If the value is not specified in the task, the value of environment variable `DOCKER_HOST` will be used instead. If the environment variable is not set, the default value will be used.  Default: `"unix://var/run/docker.sock"`  Configuration:   - Variable: ansible_docker_docker_host |
| **remote_addr**  string | The name of the container you want to access.  Default: `"inventory_hostname"`  Configuration:   - Variable: inventory_hostname - Variable: ansible_host - Variable: ansible_docker_host |
| **remote_user**  string | The user to execute as inside the container.  Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   remote_user = VALUE   ``` - Environment variable: [`ANSIBLE_REMOTE_USER`](../../../reference_appendices/config.md#envvar-ANSIBLE_REMOTE_USER) - Variable: ansible_user - Variable: ansible_docker_user - Keyword: remote_user - CLI argument: –user |
| **ssl_version**  string | Provide a valid SSL version number. Default value determined by ssl.py module.  If the value is not specified in the task, the value of environment variable `DOCKER_SSL_VERSION` will be used instead.  Configuration:   - Variable: ansible_docker_ssl_version |
| **timeout**  integer | The maximum amount of time in seconds to wait on a response from the API.  If the value is not specified in the task, the value of environment variable `DOCKER_TIMEOUT` will be used instead. If the environment variable is not set, the default value will be used.  Default: `60`  Configuration:   - Variable: ansible_docker_timeout |
| **tls**  boolean | Secure the connection to the API by using TLS without verifying the authenticity of the Docker host server. Note that if *validate_certs* is set to `true` as well, it will take precedence.  If the value is not specified in the task, the value of environment variable `DOCKER_TLS` will be used instead. If the environment variable is not set, the default value will be used.  Choices:   - `false` ← (default) - `true`   Configuration:   - Variable: ansible_docker_tls |
| **tls_hostname**  string | When verifying the authenticity of the Docker Host server, provide the expected name of the server.  If the value is not specified in the task, the value of environment variable `DOCKER_TLS_HOSTNAME` will be used instead. If the environment variable is not set, the default value will be used.  The current default value is `localhost`. This default is deprecated and will change in community.docker 2.0.0 to be a value computed from *docker_host*. Explicitly specify `localhost` to make sure this value will still be used, and to disable the deprecation message which will be shown otherwise.  Configuration:   - Variable: ansible_docker_tls_hostname |
| **use_ssh_client**  boolean  added in community.docker 1.5.0 | For SSH transports, use the `ssh` CLI tool instead of paramiko.  Requires Docker SDK for Python 4.4.0 or newer.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  aliases: tls_verify  boolean | Secure the connection to the API by using TLS and verifying the authenticity of the Docker host server.  If the value is not specified in the task, the value of environment variable `DOCKER_TLS_VERIFY` will be used instead. If the environment variable is not set, the default value will be used.  Choices:   - `false` ← (default) - `true`   Configuration:   - Variable: ansible_docker_validate_certs |

## [Notes](docker_api_connection.md#id4)

> **Note:**
>
> - Connect to the Docker daemon by providing parameters with each task or by defining environment variables. You can define `DOCKER_HOST`, `DOCKER_TLS_HOSTNAME`, `DOCKER_API_VERSION`, `DOCKER_CERT_PATH`, `DOCKER_SSL_VERSION`, `DOCKER_TLS`, `DOCKER_TLS_VERIFY` and `DOCKER_TIMEOUT`. If you are using docker machine, run the script shipped with the product that sets up the environment. It will set these variables for you. See <https://docs.docker.com/machine/reference/env/> for more details.
> - When connecting to Docker daemon with TLS, you might need to install additional Python packages. For the Docker SDK for Python, version 2.4 or newer, this can be done by installing `docker[tls]` with [ansible.builtin.pip](../../ansible/builtin/pip_module.md#ansible-collections-ansible-builtin-pip-module).
> - Note that the Docker SDK for Python only allows to specify the path to the Docker configuration for very few functions. In general, it will use `$HOME/.docker/config.json` if the `DOCKER_CONFIG` environment variable is not specified, and use `$DOCKER_CONFIG/config.json` otherwise.
> - This module uses the [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/) to communicate with the Docker daemon.

### Authors

- Felix Fontein (@felixfontein)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.docker/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.docker)
[Submit a bug report](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-docker)
