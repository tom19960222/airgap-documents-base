---
collection: ansible
version: "6"
title: "community.docker.docker_containers inventory – Ansible dynamic inventory plugin for Docker containers."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/docker/docker_containers_inventory.html
fetched_at: 2026-07-27T17:07:34+00:00
---
# community.docker.docker_containers inventory – Ansible dynamic inventory plugin for Docker containers.

> **Note:**
>
> This inventory plugin is part of the [community.docker collection](https://galaxy.ansible.com/community/docker) (version 2.7.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.docker`.
> You need further requirements to be able to use this inventory plugin,
> see [Requirements](docker_containers_inventory.md#ansible-collections-community-docker-docker-containers-inventory-requirements) for details.
>
> To use it in a playbook, specify: `community.docker.docker_containers`.

New in community.docker 1.1.0

- [Synopsis](docker_containers_inventory.md#synopsis)
- [Requirements](docker_containers_inventory.md#requirements)
- [Parameters](docker_containers_inventory.md#parameters)
- [Notes](docker_containers_inventory.md#notes)
- [Examples](docker_containers_inventory.md#examples)

## [Synopsis](docker_containers_inventory.md#id1)

- Reads inventories from the Docker API.
- Uses a YAML configuration file that ends with `docker.[yml|yaml]`.

## [Requirements](docker_containers_inventory.md#id2)

The below requirements are needed on the local controller node that executes this inventory.

- Docker SDK for Python: Please note that the [docker-py](https://pypi.org/project/docker-py/) Python module has been superseded by [docker](https://pypi.org/project/docker/) (see [here](https://github.com/docker/docker-py/issues/1310) for details). For Python 2.6, `docker-py` must be used. Otherwise, it is recommended to install the `docker` Python module. Note that both modules should \*not\* be installed at the same time. Also note that when both modules are installed and one of them is uninstalled, the other might no longer function and a reinstall of it is required.
- [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/) >= 1.10.0

## [Parameters](docker_containers_inventory.md#id3)

| Parameter | Comments |
| --- | --- |
| **add_legacy_groups**  boolean | Add the same groups as the `docker` inventory script does. These are the following:  `<container id>`: contains the container of this ID.  `<container name>`: contains the container that has this name.  `<container short id>`: contains the containers that have this short ID (first 13 letters of ID).  `image_<image name>`: contains the containers that have the image `<image name>`.  `stack_<stack name>`: contains the containers that belong to the stack `<stack name>`.  `service_<service name>`: contains the containers that belong to the service `<service name>`  `<docker_host>`: contains the containers which belong to the Docker daemon *docker_host*. Useful if you run this plugin against multiple Docker daemons.  `running`: contains all containers that are running.  `stopped`: contains all containers that are not running.  If this is not set to `true`, you should use keyed groups to add the containers to groups. See the examples for how to do that.  Choices:   - `false` ← (default) - `true` |
| **api_version**  aliases: docker_api_version  string | The version of the Docker API running on the Docker Host.  Defaults to the latest version of the API supported by Docker SDK for Python and the docker daemon.  If the value is not specified in the task, the value of environment variable `DOCKER_API_VERSION` will be used instead. If the environment variable is not set, the default value will be used.  Default: `"auto"` |
| **ca_cert**  aliases: tls_ca_cert, cacert_path  path | Use a CA certificate when performing server verification by providing the path to a CA certificate file.  If the value is not specified in the task and the environment variable `DOCKER_CERT_PATH` is set, the file `ca.pem` from the directory specified in the environment variable `DOCKER_CERT_PATH` will be used. |
| **client_cert**  aliases: tls_client_cert, cert_path  path | Path to the client’s TLS certificate file.  If the value is not specified in the task and the environment variable `DOCKER_CERT_PATH` is set, the file `cert.pem` from the directory specified in the environment variable `DOCKER_CERT_PATH` will be used. |
| **client_key**  aliases: tls_client_key, key_path  path | Path to the client’s TLS key file.  If the value is not specified in the task and the environment variable `DOCKER_CERT_PATH` is set, the file `key.pem` from the directory specified in the environment variable `DOCKER_CERT_PATH` will be used. |
| **compose**  dictionary | Create vars from jinja2 expressions.  Default: `{}` |
| **configure_docker_daemon**  boolean  added in community.docker 1.8.0 | Whether to pass all Docker daemon configuration from the inventory plugin to the connection plugin.  Only used when *connection_type=docker-api*.  Choices:   - `false` - `true` ← (default) |
| **connection_type**  string | Which connection type to use the containers.  One way to connect to containers is to use SSH (`ssh`). For this, the options *default_ip* and *private_ssh_port* are used. This requires that a SSH daemon is running inside the containers.  Alternatively, `docker-cli` selects the [docker connection plugin](docker_connection.md#ansible-collections-community-docker-docker-connection), and `docker-api` (default) selects the [docker_api connection plugin](docker_api_connection.md#ansible-collections-community-docker-docker-api-connection).  When `docker-api` is used, all Docker daemon configuration values are passed from the inventory plugin to the connection plugin. This can be controlled with *configure_docker_daemon*.  Choices:   - `"ssh"` - `"docker-cli"` - `"docker-api"` ← (default) |
| **debug**  boolean | Debug mode  Choices:   - `false` ← (default) - `true` |
| **default_ip**  string | The IP address to assign to ansible_host when the container’s SSH port is mapped to interface ‘0.0.0.0’.  Only used if *connection_type* is `ssh`.  Default: `"127.0.0.1"` |
| **docker_host**  aliases: docker_url  string | The URL or Unix socket path used to connect to the Docker API. To connect to a remote host, provide the TCP connection string. For example, `tcp://192.0.2.23:2376`. If TLS is used to encrypt the connection, the module will automatically replace `tcp` in the connection URL with `https`.  If the value is not specified in the task, the value of environment variable `DOCKER_HOST` will be used instead. If the environment variable is not set, the default value will be used.  Default: `"unix://var/run/docker.sock"` |
| **groups**  dictionary | Add hosts to group based on Jinja2 conditionals.  Default: `{}` |
| **keyed_groups**  list / elements=dictionary | Add hosts to group based on the values of a variable.  Default: `[]` |
| **default_value**  string  added in ansible-core 2.12 | The default value when the host variable’s value is an empty string.  This option is mutually exclusive with `trailing_separator`. |
| **key**  string | The key from input dictionary used to generate groups |
| **parent_group**  string | parent group for keyed group |
| **prefix**  string | A keyed group name will start with this prefix  Default: `""` |
| **separator**  string | separator used to build the keyed group name  Default: `"_"` |
| **trailing_separator**  boolean  added in ansible-core 2.12 | Set this option to *False* to omit the `separator` after the host variable when the value is an empty string.  This option is mutually exclusive with `default_value`.  Choices:   - `false` - `true` ← (default) |
| **leading_separator**  boolean  added in ansible-core 2.11 | Use in conjunction with keyed_groups.  By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.  This is because the default prefix is “” and the default separator is “_”.  Set this option to False to omit the leading underscore (or other separator) if no prefix is given.  If the group name is derived from a mapping the separator is still used to concatenate the items.  To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.  Choices:   - `false` - `true` ← (default) |
| **plugin**  string / required | The name of this plugin, it should always be set to `community.docker.docker_containers` for this plugin to recognize it as it’s own.  Choices:   - `"community.docker.docker_containers"` |
| **private_ssh_port**  integer | The port containers use for SSH.  Only used if *connection_type* is `ssh`.  Default: `22` |
| **ssl_version**  string | Provide a valid SSL version number. Default value determined by ssl.py module.  If the value is not specified in the task, the value of environment variable `DOCKER_SSL_VERSION` will be used instead. |
| **strict**  boolean | If `yes` make invalid entries a fatal error, otherwise skip and continue.  Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.  Choices:   - `false` ← (default) - `true` |
| **timeout**  integer | The maximum amount of time in seconds to wait on a response from the API.  If the value is not specified in the task, the value of environment variable `DOCKER_TIMEOUT` will be used instead. If the environment variable is not set, the default value will be used.  Default: `60` |
| **tls**  boolean | Secure the connection to the API by using TLS without verifying the authenticity of the Docker host server. Note that if *validate_certs* is set to `true` as well, it will take precedence.  If the value is not specified in the task, the value of environment variable `DOCKER_TLS` will be used instead. If the environment variable is not set, the default value will be used.  Choices:   - `false` ← (default) - `true` |
| **tls_hostname**  string | When verifying the authenticity of the Docker Host server, provide the expected name of the server.  If the value is not specified in the task, the value of environment variable `DOCKER_TLS_HOSTNAME` will be used instead. If the environment variable is not set, the default value will be used.  The current default value is `localhost`. This default is deprecated and will change in community.docker 2.0.0 to be a value computed from *docker_host*. Explicitly specify `localhost` to make sure this value will still be used, and to disable the deprecation message which will be shown otherwise. |
| **use_extra_vars**  boolean  added in ansible-core 2.11 | Merge extra vars into the available variables for composition (highest precedence).  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [inventory_plugins]   use_extra_vars = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_USE_EXTRA_VARS`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_USE_EXTRA_VARS) |
| **use_ssh_client**  boolean  added in community.docker 1.5.0 | For SSH transports, use the `ssh` CLI tool instead of paramiko.  Requires Docker SDK for Python 4.4.0 or newer.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  aliases: tls_verify  boolean | Secure the connection to the API by using TLS and verifying the authenticity of the Docker host server.  If the value is not specified in the task, the value of environment variable `DOCKER_TLS_VERIFY` will be used instead. If the environment variable is not set, the default value will be used.  Choices:   - `false` ← (default) - `true` |
| **verbose_output**  boolean | Toggle to (not) include all available inspection metadata.  Note that all top-level keys will be transformed to the format `docker_xxx`. For example, `HostConfig` is converted to `docker_hostconfig`.  If this is `false`, these values can only be used during *constructed*, *groups*, and *keyed_groups*.  The `docker` inventory script always added these variables, so for compatibility set this to `true`.  Choices:   - `false` ← (default) - `true` |

## [Notes](docker_containers_inventory.md#id4)

> **Note:**
>
> - Connect to the Docker daemon by providing parameters with each task or by defining environment variables. You can define `DOCKER_HOST`, `DOCKER_TLS_HOSTNAME`, `DOCKER_API_VERSION`, `DOCKER_CERT_PATH`, `DOCKER_SSL_VERSION`, `DOCKER_TLS`, `DOCKER_TLS_VERIFY` and `DOCKER_TIMEOUT`. If you are using docker machine, run the script shipped with the product that sets up the environment. It will set these variables for you. See <https://docs.docker.com/machine/reference/env/> for more details.
> - When connecting to Docker daemon with TLS, you might need to install additional Python packages. For the Docker SDK for Python, version 2.4 or newer, this can be done by installing `docker[tls]` with [ansible.builtin.pip](../../ansible/builtin/pip_module.md#ansible-collections-ansible-builtin-pip-module).
> - Note that the Docker SDK for Python only allows to specify the path to the Docker configuration for very few functions. In general, it will use `$HOME/.docker/config.json` if the `DOCKER_CONFIG` environment variable is not specified, and use `$DOCKER_CONFIG/config.json` otherwise.
> - This module uses the [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/) to communicate with the Docker daemon.

## [Examples](docker_containers_inventory.md#id5)

```yaml+jinja
# Minimal example using local Docker daemon
plugin: community.docker.docker_containers
docker_host: unix://var/run/docker.sock

# Minimal example using remote Docker daemon
plugin: community.docker.docker_containers
docker_host: tcp://my-docker-host:2375

# Example using remote Docker daemon with unverified TLS
plugin: community.docker.docker_containers
docker_host: tcp://my-docker-host:2376
tls: true

# Example using remote Docker daemon with verified TLS and client certificate verification
plugin: community.docker.docker_containers
docker_host: tcp://my-docker-host:2376
validate_certs: true
ca_cert: /somewhere/ca.pem
client_key: /somewhere/key.pem
client_cert: /somewhere/cert.pem

# Example using constructed features to create groups
plugin: community.docker.docker_containers
docker_host: tcp://my-docker-host:2375
strict: false
keyed_groups:
  # Add containers with primary network foo to a network_foo group
  - prefix: network
    key: 'docker_hostconfig.NetworkMode'
  # Add Linux hosts to an os_linux group
  - prefix: os
    key: docker_platform

# Example using SSH connection with an explicit fallback for when port 22 has not been
# exported: use container name as ansible_ssh_host and 22 as ansible_ssh_port
plugin: community.docker.docker_containers
connection_type: ssh
compose:
  ansible_ssh_host: ansible_ssh_host | default(docker_name[1:], true)
  ansible_ssh_port: ansible_ssh_port | default(22, true)
```

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
