---
collection: ansible
version: "6"
title: "community.docker.docker_node module – Manage Docker Swarm node"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/docker/docker_node_module.html
fetched_at: 2026-07-27T17:07:22+00:00
---
# community.docker.docker_node module – Manage Docker Swarm node

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
> see [Requirements](docker_node_module.md#ansible-collections-community-docker-docker-node-module-requirements) for details.
>
> To use it in a playbook, specify: `community.docker.docker_node`.

- [Synopsis](docker_node_module.md#synopsis)
- [Requirements](docker_node_module.md#requirements)
- [Parameters](docker_node_module.md#parameters)
- [Notes](docker_node_module.md#notes)
- [Examples](docker_node_module.md#examples)
- [Return Values](docker_node_module.md#return-values)

## [Synopsis](docker_node_module.md#id1)

- Manages the Docker nodes via Swarm Manager.
- This module allows to change the node’s role, its availability, and to modify, add or remove node labels.

## [Requirements](docker_node_module.md#id2)

The below requirements are needed on the host that executes this module.

- Docker API >= 1.25
- Docker SDK for Python: Please note that the [docker-py](https://pypi.org/project/docker-py/) Python module has been superseded by [docker](https://pypi.org/project/docker/) (see [here](https://github.com/docker/docker-py/issues/1310) for details). For Python 2.6, `docker-py` must be used. Otherwise, it is recommended to install the `docker` Python module. Note that both modules should \*not\* be installed at the same time. Also note that when both modules are installed and one of them is uninstalled, the other might no longer function and a reinstall of it is required.
- [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/) >= 2.4.0

## [Parameters](docker_node_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_version**  aliases: docker_api_version  string | The version of the Docker API running on the Docker Host.  Defaults to the latest version of the API supported by Docker SDK for Python and the docker daemon.  If the value is not specified in the task, the value of environment variable `DOCKER_API_VERSION` will be used instead. If the environment variable is not set, the default value will be used.  Default: `"auto"` |
| **availability**  string | Node availability to assign. If not provided then node availability remains unchanged.  Choices:   - `"active"` - `"pause"` - `"drain"` |
| **ca_cert**  aliases: tls_ca_cert, cacert_path  path | Use a CA certificate when performing server verification by providing the path to a CA certificate file.  If the value is not specified in the task and the environment variable `DOCKER_CERT_PATH` is set, the file `ca.pem` from the directory specified in the environment variable `DOCKER_CERT_PATH` will be used. |
| **client_cert**  aliases: tls_client_cert, cert_path  path | Path to the client’s TLS certificate file.  If the value is not specified in the task and the environment variable `DOCKER_CERT_PATH` is set, the file `cert.pem` from the directory specified in the environment variable `DOCKER_CERT_PATH` will be used. |
| **client_key**  aliases: tls_client_key, key_path  path | Path to the client’s TLS key file.  If the value is not specified in the task and the environment variable `DOCKER_CERT_PATH` is set, the file `key.pem` from the directory specified in the environment variable `DOCKER_CERT_PATH` will be used. |
| **debug**  boolean | Debug mode  Choices:   - `false` ← (default) - `true` |
| **docker_host**  aliases: docker_url  string | The URL or Unix socket path used to connect to the Docker API. To connect to a remote host, provide the TCP connection string. For example, `tcp://192.0.2.23:2376`. If TLS is used to encrypt the connection, the module will automatically replace `tcp` in the connection URL with `https`.  If the value is not specified in the task, the value of environment variable `DOCKER_HOST` will be used instead. If the environment variable is not set, the default value will be used.  Default: `"unix://var/run/docker.sock"` |
| **hostname**  string / required | The hostname or ID of node as registered in Swarm.  If more than one node is registered using the same hostname the ID must be used, otherwise module will fail. |
| **labels**  dictionary | User-defined key/value metadata that will be assigned as node attribute.  Label operations in this module apply to the docker swarm node specified by *hostname*. Use [community.docker.docker_swarm](docker_swarm_module.md#ansible-collections-community-docker-docker-swarm-module) module to add/modify/remove swarm cluster labels.  The actual state of labels assigned to the node when module completes its work depends on *labels_state* and *labels_to_remove* parameters values. See description below. |
| **labels_state**  string | It defines the operation on the labels assigned to node and labels specified in *labels* option.  Set to `merge` to combine labels provided in *labels* with those already assigned to the node. If no labels are assigned then it will add listed labels. For labels that are already assigned to the node, it will update their values. The labels not specified in *labels* will remain unchanged. If *labels* is empty then no changes will be made.  Set to `replace` to replace all assigned labels with provided ones. If *labels* is empty then all labels assigned to the node will be removed.  Choices:   - `"merge"` ← (default) - `"replace"` |
| **labels_to_remove**  list / elements=string | List of labels that will be removed from the node configuration. The list has to contain only label names, not their values.  If the label provided on the list is not assigned to the node, the entry is ignored.  If the label is both on the *labels_to_remove* and *labels*, then value provided in *labels* remains assigned to the node.  If *labels_state* is `replace` and *labels* is not provided or empty then all labels assigned to node are removed and *labels_to_remove* is ignored. |
| **role**  string | Node role to assign. If not provided then node role remains unchanged.  Choices:   - `"manager"` - `"worker"` |
| **ssl_version**  string | Provide a valid SSL version number. Default value determined by ssl.py module.  If the value is not specified in the task, the value of environment variable `DOCKER_SSL_VERSION` will be used instead. |
| **timeout**  integer | The maximum amount of time in seconds to wait on a response from the API.  If the value is not specified in the task, the value of environment variable `DOCKER_TIMEOUT` will be used instead. If the environment variable is not set, the default value will be used.  Default: `60` |
| **tls**  boolean | Secure the connection to the API by using TLS without verifying the authenticity of the Docker host server. Note that if *validate_certs* is set to `true` as well, it will take precedence.  If the value is not specified in the task, the value of environment variable `DOCKER_TLS` will be used instead. If the environment variable is not set, the default value will be used.  Choices:   - `false` ← (default) - `true` |
| **tls_hostname**  string | When verifying the authenticity of the Docker Host server, provide the expected name of the server.  If the value is not specified in the task, the value of environment variable `DOCKER_TLS_HOSTNAME` will be used instead. If the environment variable is not set, the default value will be used.  The current default value is `localhost`. This default is deprecated and will change in community.docker 2.0.0 to be a value computed from *docker_host*. Explicitly specify `localhost` to make sure this value will still be used, and to disable the deprecation message which will be shown otherwise. |
| **use_ssh_client**  boolean  added in community.docker 1.5.0 | For SSH transports, use the `ssh` CLI tool instead of paramiko.  Requires Docker SDK for Python 4.4.0 or newer.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  aliases: tls_verify  boolean | Secure the connection to the API by using TLS and verifying the authenticity of the Docker host server.  If the value is not specified in the task, the value of environment variable `DOCKER_TLS_VERIFY` will be used instead. If the environment variable is not set, the default value will be used.  Choices:   - `false` ← (default) - `true` |

## [Notes](docker_node_module.md#id4)

> **Note:**
>
> - Connect to the Docker daemon by providing parameters with each task or by defining environment variables. You can define `DOCKER_HOST`, `DOCKER_TLS_HOSTNAME`, `DOCKER_API_VERSION`, `DOCKER_CERT_PATH`, `DOCKER_SSL_VERSION`, `DOCKER_TLS`, `DOCKER_TLS_VERIFY` and `DOCKER_TIMEOUT`. If you are using docker machine, run the script shipped with the product that sets up the environment. It will set these variables for you. See <https://docs.docker.com/machine/reference/env/> for more details.
> - When connecting to Docker daemon with TLS, you might need to install additional Python packages. For the Docker SDK for Python, version 2.4 or newer, this can be done by installing `docker[tls]` with [ansible.builtin.pip](../../ansible/builtin/pip_module.md#ansible-collections-ansible-builtin-pip-module).
> - Note that the Docker SDK for Python only allows to specify the path to the Docker configuration for very few functions. In general, it will use `$HOME/.docker/config.json` if the `DOCKER_CONFIG` environment variable is not specified, and use `$DOCKER_CONFIG/config.json` otherwise.
> - This module uses the [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/) to communicate with the Docker daemon.

## [Examples](docker_node_module.md#id5)

```yaml+jinja
- name: Set node role
  community.docker.docker_node:
    hostname: mynode
    role: manager

- name: Set node availability
  community.docker.docker_node:
    hostname: mynode
    availability: drain

- name: Replace node labels with new labels
  community.docker.docker_node:
    hostname: mynode
    labels:
      key: value
    labels_state: replace

- name: Merge node labels and new labels
  community.docker.docker_node:
    hostname: mynode
    labels:
      key: value

- name: Remove all labels assigned to node
  community.docker.docker_node:
    hostname: mynode
    labels_state: replace

- name: Remove selected labels from the node
  community.docker.docker_node:
    hostname: mynode
    labels_to_remove:
      - key1
      - key2
```

## [Return Values](docker_node_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **node**  dictionary | Information about node after ‘update’ operation  Returned: success |

### Authors

- Piotr Wojciechowski (@WojciechowskiPiotr)
- Thierry Bouvet (@tbouvet)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.docker/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.docker)
[Submit a bug report](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-docker)
