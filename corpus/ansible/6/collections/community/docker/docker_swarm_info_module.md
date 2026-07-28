---
collection: ansible
version: "6"
title: "community.docker.docker_swarm_info module – Retrieves facts about Docker Swarm cluster."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/docker/docker_swarm_info_module.html
fetched_at: 2026-07-27T17:07:28+00:00
---
# community.docker.docker_swarm_info module – Retrieves facts about Docker Swarm cluster.

> **Note:**
>
> This module is part of the [community.docker collection](https://galaxy.ansible.com/community/docker) (version 2.7.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.docker`.
> You need further requirements to be able to use this module,
> see [Requirements](docker_swarm_info_module.md#ansible-collections-community-docker-docker-swarm-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.docker.docker_swarm_info`.

- [Synopsis](docker_swarm_info_module.md#synopsis)
- [Requirements](docker_swarm_info_module.md#requirements)
- [Parameters](docker_swarm_info_module.md#parameters)
- [Notes](docker_swarm_info_module.md#notes)
- [Examples](docker_swarm_info_module.md#examples)
- [Return Values](docker_swarm_info_module.md#return-values)

## [Synopsis](docker_swarm_info_module.md#id1)

- Retrieves facts about a Docker Swarm.
- Returns lists of swarm objects names for the services - nodes, services, tasks.
- The output differs depending on API version available on docker host.
- Must be run on Swarm Manager node; otherwise module fails with error message. It does return boolean flags in on both error and success which indicate whether the docker daemon can be communicated with, whether it is in Swarm mode, and whether it is a Swarm Manager node.

## [Requirements](docker_swarm_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- Docker API >= 1.24
- Docker SDK for Python: Please note that the [docker-py](https://pypi.org/project/docker-py/) Python module has been superseded by [docker](https://pypi.org/project/docker/) (see [here](https://github.com/docker/docker-py/issues/1310) for details). For Python 2.6, `docker-py` must be used. Otherwise, it is recommended to install the `docker` Python module. Note that both modules should \*not\* be installed at the same time. Also note that when both modules are installed and one of them is uninstalled, the other might no longer function and a reinstall of it is required.
- [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/) >= 1.10.0 (use [docker-py](https://pypi.org/project/docker-py/) for Python 2.6)

## [Parameters](docker_swarm_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_version**  aliases: docker_api_version  string | The version of the Docker API running on the Docker Host.  Defaults to the latest version of the API supported by Docker SDK for Python and the docker daemon.  If the value is not specified in the task, the value of environment variable `DOCKER_API_VERSION` will be used instead. If the environment variable is not set, the default value will be used.  Default: `"auto"` |
| **ca_cert**  aliases: tls_ca_cert, cacert_path  path | Use a CA certificate when performing server verification by providing the path to a CA certificate file.  If the value is not specified in the task and the environment variable `DOCKER_CERT_PATH` is set, the file `ca.pem` from the directory specified in the environment variable `DOCKER_CERT_PATH` will be used. |
| **client_cert**  aliases: tls_client_cert, cert_path  path | Path to the client’s TLS certificate file.  If the value is not specified in the task and the environment variable `DOCKER_CERT_PATH` is set, the file `cert.pem` from the directory specified in the environment variable `DOCKER_CERT_PATH` will be used. |
| **client_key**  aliases: tls_client_key, key_path  path | Path to the client’s TLS key file.  If the value is not specified in the task and the environment variable `DOCKER_CERT_PATH` is set, the file `key.pem` from the directory specified in the environment variable `DOCKER_CERT_PATH` will be used. |
| **debug**  boolean | Debug mode  Choices:   - `false` ← (default) - `true` |
| **docker_host**  aliases: docker_url  string | The URL or Unix socket path used to connect to the Docker API. To connect to a remote host, provide the TCP connection string. For example, `tcp://192.0.2.23:2376`. If TLS is used to encrypt the connection, the module will automatically replace `tcp` in the connection URL with `https`.  If the value is not specified in the task, the value of environment variable `DOCKER_HOST` will be used instead. If the environment variable is not set, the default value will be used.  Default: `"unix://var/run/docker.sock"` |
| **nodes**  boolean | Whether to list swarm nodes.  Choices:   - `false` ← (default) - `true` |
| **nodes_filters**  dictionary | A dictionary of filter values used for selecting nodes to list.  For example, `name: mynode`.  See [the docker documentation](https://docs.docker.com/engine/reference/commandline/node_ls/#filtering) for more information on possible filters. |
| **services**  boolean | Whether to list swarm services.  Choices:   - `false` ← (default) - `true` |
| **services_filters**  dictionary | A dictionary of filter values used for selecting services to list.  For example, `name: myservice`.  See [the docker documentation](https://docs.docker.com/engine/reference/commandline/service_ls/#filtering) for more information on possible filters. |
| **ssl_version**  string | Provide a valid SSL version number. Default value determined by ssl.py module.  If the value is not specified in the task, the value of environment variable `DOCKER_SSL_VERSION` will be used instead. |
| **tasks**  boolean | Whether to list containers.  Choices:   - `false` ← (default) - `true` |
| **tasks_filters**  dictionary | A dictionary of filter values used for selecting tasks to list.  For example, `node: mynode-1`.  See [the docker documentation](https://docs.docker.com/engine/reference/commandline/service_ps/#filtering) for more information on possible filters. |
| **timeout**  integer | The maximum amount of time in seconds to wait on a response from the API.  If the value is not specified in the task, the value of environment variable `DOCKER_TIMEOUT` will be used instead. If the environment variable is not set, the default value will be used.  Default: `60` |
| **tls**  boolean | Secure the connection to the API by using TLS without verifying the authenticity of the Docker host server. Note that if *validate_certs* is set to `true` as well, it will take precedence.  If the value is not specified in the task, the value of environment variable `DOCKER_TLS` will be used instead. If the environment variable is not set, the default value will be used.  Choices:   - `false` ← (default) - `true` |
| **tls_hostname**  string | When verifying the authenticity of the Docker Host server, provide the expected name of the server.  If the value is not specified in the task, the value of environment variable `DOCKER_TLS_HOSTNAME` will be used instead. If the environment variable is not set, the default value will be used.  The current default value is `localhost`. This default is deprecated and will change in community.docker 2.0.0 to be a value computed from *docker_host*. Explicitly specify `localhost` to make sure this value will still be used, and to disable the deprecation message which will be shown otherwise. |
| **unlock_key**  boolean | Whether to retrieve the swarm unlock key.  Choices:   - `false` ← (default) - `true` |
| **use_ssh_client**  boolean  added in community.docker 1.5.0 | For SSH transports, use the `ssh` CLI tool instead of paramiko.  Requires Docker SDK for Python 4.4.0 or newer.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  aliases: tls_verify  boolean | Secure the connection to the API by using TLS and verifying the authenticity of the Docker host server.  If the value is not specified in the task, the value of environment variable `DOCKER_TLS_VERIFY` will be used instead. If the environment variable is not set, the default value will be used.  Choices:   - `false` ← (default) - `true` |
| **verbose_output**  boolean | When set to `true` and *nodes*, *services* or *tasks* is set to `true`, then the module output will contain verbose information about objects matching the full output of API method.  For details see the documentation of your version of Docker API at <https://docs.docker.com/engine/api/>.  The verbose output in this module contains only subset of information returned by *_info* module for each type of the objects.  Choices:   - `false` ← (default) - `true` |

## [Notes](docker_swarm_info_module.md#id4)

> **Note:**
>
> - Connect to the Docker daemon by providing parameters with each task or by defining environment variables. You can define `DOCKER_HOST`, `DOCKER_TLS_HOSTNAME`, `DOCKER_API_VERSION`, `DOCKER_CERT_PATH`, `DOCKER_SSL_VERSION`, `DOCKER_TLS`, `DOCKER_TLS_VERIFY` and `DOCKER_TIMEOUT`. If you are using docker machine, run the script shipped with the product that sets up the environment. It will set these variables for you. See <https://docs.docker.com/machine/reference/env/> for more details.
> - When connecting to Docker daemon with TLS, you might need to install additional Python packages. For the Docker SDK for Python, version 2.4 or newer, this can be done by installing `docker[tls]` with [ansible.builtin.pip](../../ansible/builtin/pip_module.md#ansible-collections-ansible-builtin-pip-module).
> - Note that the Docker SDK for Python only allows to specify the path to the Docker configuration for very few functions. In general, it will use `$HOME/.docker/config.json` if the `DOCKER_CONFIG` environment variable is not specified, and use `$DOCKER_CONFIG/config.json` otherwise.
> - This module uses the [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/) to communicate with the Docker daemon.

## [Examples](docker_swarm_info_module.md#id5)

```yaml+jinja
- name: Get info on Docker Swarm
  community.docker.docker_swarm_info:
  ignore_errors: true
  register: result

- name: Inform about basic flags
  ansible.builtin.debug:
    msg: |
      Was able to talk to docker daemon: {{ result.can_talk_to_docker }}
      Docker in Swarm mode: {{ result.docker_swarm_active }}
      This is a Manager node: {{ result.docker_swarm_manager }}

- block:

- name: Get info on Docker Swarm and list of registered nodes
  community.docker.docker_swarm_info:
    nodes: true
  register: result

- name: Get info on Docker Swarm and extended list of registered nodes
  community.docker.docker_swarm_info:
    nodes: true
    verbose_output: true
  register: result

- name: Get info on Docker Swarm and filtered list of registered nodes
  community.docker.docker_swarm_info:
    nodes: true
    nodes_filters:
      name: mynode
  register: result

- ansible.builtin.debug:
    var: result.swarm_facts

- name: Get the swarm unlock key
  community.docker.docker_swarm_info:
    unlock_key: true
  register: result

- ansible.builtin.debug:
    var: result.swarm_unlock_key
```

## [Return Values](docker_swarm_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **can_talk_to_docker**  boolean | Will be `true` if the module can talk to the docker daemon.  Returned: both on success and on error |
| **docker_swarm_active**  boolean | Will be `true` if the module can talk to the docker daemon, and the docker daemon is in Swarm mode.  Returned: both on success and on error |
| **docker_swarm_manager**  boolean | Will be `true` if the module can talk to the docker daemon, the docker daemon is in Swarm mode, and the current node is a manager node.  Only if this one is `true`, the module will not fail.  Returned: both on success and on error |
| **nodes**  list / elements=dictionary | List of dict objects containing the basic information about each volume. Keys matches the `docker node ls` output unless *verbose_output=true*. See description for *verbose_output*.  Returned: When *nodes* is `true` |
| **services**  list / elements=dictionary | List of dict objects containing the basic information about each volume. Keys matches the `docker service ls` output unless *verbose_output=true*. See description for *verbose_output*.  Returned: When *services* is `true` |
| **swarm_facts**  dictionary | Facts representing the basic state of the docker Swarm cluster.  Contains tokens to connect to the Swarm  Returned: always |
| **swarm_unlock_key**  string | Contains the key needed to unlock the swarm.  Returned: When *unlock_key* is `true`. |
| **tasks**  list / elements=dictionary | List of dict objects containing the basic information about each volume. Keys matches the `docker service ps` output unless *verbose_output=true*. See description for *verbose_output*.  Returned: When *tasks* is `true` |

### Authors

- Piotr Wojciechowski (@WojciechowskiPiotr)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.docker/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.docker)
[Submit a bug report](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-docker)
