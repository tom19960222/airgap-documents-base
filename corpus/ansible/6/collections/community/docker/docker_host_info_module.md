---
collection: ansible
version: "6"
title: "community.docker.docker_host_info module – Retrieves facts about docker host and lists of objects of the services."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/docker/docker_host_info_module.html
fetched_at: 2026-07-27T17:07:17+00:00
---
# community.docker.docker_host_info module – Retrieves facts about docker host and lists of objects of the services.

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
> see [Requirements](docker_host_info_module.md#ansible-collections-community-docker-docker-host-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.docker.docker_host_info`.

- [Synopsis](docker_host_info_module.md#synopsis)
- [Requirements](docker_host_info_module.md#requirements)
- [Parameters](docker_host_info_module.md#parameters)
- [Notes](docker_host_info_module.md#notes)
- [Examples](docker_host_info_module.md#examples)
- [Return Values](docker_host_info_module.md#return-values)

## [Synopsis](docker_host_info_module.md#id1)

- Retrieves facts about a docker host.
- Essentially returns the output of `docker system info`.
- The module also allows to list object names for containers, images, networks and volumes. It also allows to query information on disk usage.
- The output differs depending on API version of the docker daemon.
- If the docker daemon cannot be contacted or does not meet the API version requirements, the module will fail.

## [Requirements](docker_host_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- Docker API >= 1.21
- Docker SDK for Python: Please note that the [docker-py](https://pypi.org/project/docker-py/) Python module has been superseded by [docker](https://pypi.org/project/docker/) (see [here](https://github.com/docker/docker-py/issues/1310) for details). For Python 2.6, `docker-py` must be used. Otherwise, it is recommended to install the `docker` Python module. Note that both modules should \*not\* be installed at the same time. Also note that when both modules are installed and one of them is uninstalled, the other might no longer function and a reinstall of it is required.
- [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/) >= 1.10.0 (use [docker-py](https://pypi.org/project/docker-py/) for Python 2.6)

## [Parameters](docker_host_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_version**  aliases: docker_api_version  string | The version of the Docker API running on the Docker Host.  Defaults to the latest version of the API supported by Docker SDK for Python and the docker daemon.  If the value is not specified in the task, the value of environment variable `DOCKER_API_VERSION` will be used instead. If the environment variable is not set, the default value will be used.  Default: `"auto"` |
| **ca_cert**  aliases: tls_ca_cert, cacert_path  path | Use a CA certificate when performing server verification by providing the path to a CA certificate file.  If the value is not specified in the task and the environment variable `DOCKER_CERT_PATH` is set, the file `ca.pem` from the directory specified in the environment variable `DOCKER_CERT_PATH` will be used. |
| **client_cert**  aliases: tls_client_cert, cert_path  path | Path to the client’s TLS certificate file.  If the value is not specified in the task and the environment variable `DOCKER_CERT_PATH` is set, the file `cert.pem` from the directory specified in the environment variable `DOCKER_CERT_PATH` will be used. |
| **client_key**  aliases: tls_client_key, key_path  path | Path to the client’s TLS key file.  If the value is not specified in the task and the environment variable `DOCKER_CERT_PATH` is set, the file `key.pem` from the directory specified in the environment variable `DOCKER_CERT_PATH` will be used. |
| **containers**  boolean | Whether to list containers.  Choices:   - `false` ← (default) - `true` |
| **containers_filters**  dictionary | A dictionary of filter values used for selecting containers to list.  For example, `until: 24h`.  `label` is a special case of filter which can be a string `<key>` matching when a label is present, a string `<key>=<value>` matching when a label has a particular value, or a list of strings `<key>`/`<key>=<value`.  See [the docker documentation](https://docs.docker.com/engine/reference/commandline/container_prune/#filtering) for more information on possible filters. |
| **debug**  boolean | Debug mode  Choices:   - `false` ← (default) - `true` |
| **disk_usage**  boolean | Summary information on used disk space by all Docker layers.  The output is a sum of images, volumes, containers and build cache.  Choices:   - `false` ← (default) - `true` |
| **docker_host**  aliases: docker_url  string | The URL or Unix socket path used to connect to the Docker API. To connect to a remote host, provide the TCP connection string. For example, `tcp://192.0.2.23:2376`. If TLS is used to encrypt the connection, the module will automatically replace `tcp` in the connection URL with `https`.  If the value is not specified in the task, the value of environment variable `DOCKER_HOST` will be used instead. If the environment variable is not set, the default value will be used.  Default: `"unix://var/run/docker.sock"` |
| **images**  boolean | Whether to list images.  Choices:   - `false` ← (default) - `true` |
| **images_filters**  dictionary | A dictionary of filter values used for selecting images to list.  For example, `dangling: true`.  `label` is a special case of filter which can be a string `<key>` matching when a label is present, a string `<key>=<value>` matching when a label has a particular value, or a list of strings `<key>`/`<key>=<value`.  See [the docker documentation](https://docs.docker.com/engine/reference/commandline/image_prune/#filtering) for more information on possible filters. |
| **networks**  boolean | Whether to list networks.  Choices:   - `false` ← (default) - `true` |
| **networks_filters**  dictionary | A dictionary of filter values used for selecting networks to list.  `label` is a special case of filter which can be a string `<key>` matching when a label is present, a string `<key>=<value>` matching when a label has a particular value, or a list of strings `<key>`/`<key>=<value`.  See [the docker documentation](https://docs.docker.com/engine/reference/commandline/network_prune/#filtering) for more information on possible filters. |
| **ssl_version**  string | Provide a valid SSL version number. Default value determined by ssl.py module.  If the value is not specified in the task, the value of environment variable `DOCKER_SSL_VERSION` will be used instead. |
| **timeout**  integer | The maximum amount of time in seconds to wait on a response from the API.  If the value is not specified in the task, the value of environment variable `DOCKER_TIMEOUT` will be used instead. If the environment variable is not set, the default value will be used.  Default: `60` |
| **tls**  boolean | Secure the connection to the API by using TLS without verifying the authenticity of the Docker host server. Note that if *validate_certs* is set to `true` as well, it will take precedence.  If the value is not specified in the task, the value of environment variable `DOCKER_TLS` will be used instead. If the environment variable is not set, the default value will be used.  Choices:   - `false` ← (default) - `true` |
| **tls_hostname**  string | When verifying the authenticity of the Docker Host server, provide the expected name of the server.  If the value is not specified in the task, the value of environment variable `DOCKER_TLS_HOSTNAME` will be used instead. If the environment variable is not set, the default value will be used.  The current default value is `localhost`. This default is deprecated and will change in community.docker 2.0.0 to be a value computed from *docker_host*. Explicitly specify `localhost` to make sure this value will still be used, and to disable the deprecation message which will be shown otherwise. |
| **use_ssh_client**  boolean  added in community.docker 1.5.0 | For SSH transports, use the `ssh` CLI tool instead of paramiko.  Requires Docker SDK for Python 4.4.0 or newer.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  aliases: tls_verify  boolean | Secure the connection to the API by using TLS and verifying the authenticity of the Docker host server.  If the value is not specified in the task, the value of environment variable `DOCKER_TLS_VERIFY` will be used instead. If the environment variable is not set, the default value will be used.  Choices:   - `false` ← (default) - `true` |
| **verbose_output**  boolean | When set to `true` and *networks*, *volumes*, *images*, *containers* or *disk_usage* is set to `true` then output will contain verbose information about objects matching the full output of API method. For details see the documentation of your version of Docker API at <https://docs.docker.com/engine/api/>.  The verbose output in this module contains only subset of information returned by *_info* module for each type of the objects.  Choices:   - `false` ← (default) - `true` |
| **volumes**  boolean | Whether to list volumes.  Choices:   - `false` ← (default) - `true` |
| **volumes_filters**  dictionary | A dictionary of filter values used for selecting volumes to list.  `label` is a special case of filter which can be a string `<key>` matching when a label is present, a string `<key>=<value>` matching when a label has a particular value, or a list of strings `<key>`/`<key>=<value`.  See [the docker documentation](https://docs.docker.com/engine/reference/commandline/volume_prune/#filtering) for more information on possible filters. |

## [Notes](docker_host_info_module.md#id4)

> **Note:**
>
> - Connect to the Docker daemon by providing parameters with each task or by defining environment variables. You can define `DOCKER_HOST`, `DOCKER_TLS_HOSTNAME`, `DOCKER_API_VERSION`, `DOCKER_CERT_PATH`, `DOCKER_SSL_VERSION`, `DOCKER_TLS`, `DOCKER_TLS_VERIFY` and `DOCKER_TIMEOUT`. If you are using docker machine, run the script shipped with the product that sets up the environment. It will set these variables for you. See <https://docs.docker.com/machine/reference/env/> for more details.
> - When connecting to Docker daemon with TLS, you might need to install additional Python packages. For the Docker SDK for Python, version 2.4 or newer, this can be done by installing `docker[tls]` with [ansible.builtin.pip](../../ansible/builtin/pip_module.md#ansible-collections-ansible-builtin-pip-module).
> - Note that the Docker SDK for Python only allows to specify the path to the Docker configuration for very few functions. In general, it will use `$HOME/.docker/config.json` if the `DOCKER_CONFIG` environment variable is not specified, and use `$DOCKER_CONFIG/config.json` otherwise.
> - This module uses the [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/) to communicate with the Docker daemon.

## [Examples](docker_host_info_module.md#id5)

```yaml+jinja
- name: Get info on docker host
  community.docker.docker_host_info:
  register: result

- name: Get info on docker host and list images
  community.docker.docker_host_info:
    images: true
  register: result

- name: Get info on docker host and list images matching the filter
  community.docker.docker_host_info:
    images: true
    images_filters:
      label: "mylabel"
  register: result

- name: Get info on docker host and verbose list images
  community.docker.docker_host_info:
    images: true
    verbose_output: true
  register: result

- name: Get info on docker host and used disk space
  community.docker.docker_host_info:
    disk_usage: true
  register: result

- name: Get info on docker host and list containers matching the filter
  community.docker.docker_host_info:
    containers: true
    containers_filters:
      label:
        - key1=value1
        - key2=value2
  register: result

- ansible.builtin.debug:
    var: result.host_info
```

## [Return Values](docker_host_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **can_talk_to_docker**  boolean | Will be `true` if the module can talk to the docker daemon.  Returned: both on success and on error |
| **containers**  list / elements=dictionary | List of dict objects containing the basic information about each container. Keys matches the `docker container ls` output unless *verbose_output=true*. See description for *verbose_output*.  Returned: When *containers* is `true` |
| **disk_usage**  dictionary | Information on summary disk usage by images, containers and volumes on docker host unless *verbose_output=true*. See description for *verbose_output*.  Returned: When *disk_usage* is `true` |
| **host_info**  dictionary | Facts representing the basic state of the docker host. Matches the `docker system info` output.  Returned: always |
| **images**  list / elements=dictionary | List of dict objects containing the basic information about each image. Keys matches the `docker image ls` output unless *verbose_output=true*. See description for *verbose_output*.  Returned: When *images* is `true` |
| **networks**  list / elements=dictionary | List of dict objects containing the basic information about each network. Keys matches the `docker network ls` output unless *verbose_output=true*. See description for *verbose_output*.  Returned: When *networks* is `true` |
| **volumes**  list / elements=dictionary | List of dict objects containing the basic information about each volume. Keys matches the `docker volume ls` output unless *verbose_output=true*. See description for *verbose_output*.  Returned: When *volumes* is `true` |

### Authors

- Piotr Wojciechowski (@WojciechowskiPiotr)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.docker/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.docker)
[Submit a bug report](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-docker)
