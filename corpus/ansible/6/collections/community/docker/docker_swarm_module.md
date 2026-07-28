---
collection: ansible
version: "6"
title: "community.docker.docker_swarm module – Manage Swarm cluster"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/docker/docker_swarm_module.html
fetched_at: 2026-07-27T17:07:27+00:00
---
# community.docker.docker_swarm module – Manage Swarm cluster

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
> see [Requirements](docker_swarm_module.md#ansible-collections-community-docker-docker-swarm-module-requirements) for details.
>
> To use it in a playbook, specify: `community.docker.docker_swarm`.

- [Synopsis](docker_swarm_module.md#synopsis)
- [Requirements](docker_swarm_module.md#requirements)
- [Parameters](docker_swarm_module.md#parameters)
- [Notes](docker_swarm_module.md#notes)
- [Examples](docker_swarm_module.md#examples)
- [Return Values](docker_swarm_module.md#return-values)

## [Synopsis](docker_swarm_module.md#id1)

- Create a new Swarm cluster.
- Add/Remove nodes or managers to an existing cluster.

## [Requirements](docker_swarm_module.md#id2)

The below requirements are needed on the host that executes this module.

- Docker API >= 1.25
- Docker SDK for Python: Please note that the [docker-py](https://pypi.org/project/docker-py/) Python module has been superseded by [docker](https://pypi.org/project/docker/) (see [here](https://github.com/docker/docker-py/issues/1310) for details). For Python 2.6, `docker-py` must be used. Otherwise, it is recommended to install the `docker` Python module. Note that both modules should \*not\* be installed at the same time. Also note that when both modules are installed and one of them is uninstalled, the other might no longer function and a reinstall of it is required.
- [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/) >= 1.10.0 (use [docker-py](https://pypi.org/project/docker-py/) for Python 2.6)

## [Parameters](docker_swarm_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **advertise_addr**  string | Externally reachable address advertised to other nodes.  This can either be an address/port combination in the form `192.168.1.1:4567`, or an interface followed by a port number, like `eth0:4567`.  If the port number is omitted, the port number from the listen address is used.  If *advertise_addr* is not specified, it will be automatically detected when possible.  Only used when swarm is initialised or joined. Because of this it’s not considered for idempotency checking. |
| **api_version**  aliases: docker_api_version  string | The version of the Docker API running on the Docker Host.  Defaults to the latest version of the API supported by Docker SDK for Python and the docker daemon.  If the value is not specified in the task, the value of environment variable `DOCKER_API_VERSION` will be used instead. If the environment variable is not set, the default value will be used.  Default: `"auto"` |
| **autolock_managers**  boolean | If set, generate a key and use it to lock data stored on the managers.  Docker default value is `false`.  [community.docker.docker_swarm_info](docker_swarm_info_module.md#ansible-collections-community-docker-docker-swarm-info-module) can be used to retrieve the unlock key.  Choices:   - `false` - `true` |
| **ca_cert**  aliases: tls_ca_cert, cacert_path  path | Use a CA certificate when performing server verification by providing the path to a CA certificate file.  If the value is not specified in the task and the environment variable `DOCKER_CERT_PATH` is set, the file `ca.pem` from the directory specified in the environment variable `DOCKER_CERT_PATH` will be used. |
| **ca_force_rotate**  integer | An integer whose purpose is to force swarm to generate a new signing CA certificate and key, if none have been specified.  Docker default value is `0`.  Requires API version >= 1.30. |
| **client_cert**  aliases: tls_client_cert, cert_path  path | Path to the client’s TLS certificate file.  If the value is not specified in the task and the environment variable `DOCKER_CERT_PATH` is set, the file `cert.pem` from the directory specified in the environment variable `DOCKER_CERT_PATH` will be used. |
| **client_key**  aliases: tls_client_key, key_path  path | Path to the client’s TLS key file.  If the value is not specified in the task and the environment variable `DOCKER_CERT_PATH` is set, the file `key.pem` from the directory specified in the environment variable `DOCKER_CERT_PATH` will be used. |
| **data_path_addr**  string  added in community.docker 2.5.0 | Address or interface to use for data path traffic.  This can either be an address in the form `192.168.1.1`, or an interface, like `eth0`.  Only used when swarm is initialised or joined. Because of this it is not considered for idempotency checking. |
| **debug**  boolean | Debug mode  Choices:   - `false` ← (default) - `true` |
| **default_addr_pool**  list / elements=string | Default address pool in CIDR format.  Only used when swarm is initialised. Because of this it’s not considered for idempotency checking.  Requires API version >= 1.39. |
| **dispatcher_heartbeat_period**  integer | The delay for an agent to send a heartbeat to the dispatcher.  Docker default value is `5s`. |
| **docker_host**  aliases: docker_url  string | The URL or Unix socket path used to connect to the Docker API. To connect to a remote host, provide the TCP connection string. For example, `tcp://192.0.2.23:2376`. If TLS is used to encrypt the connection, the module will automatically replace `tcp` in the connection URL with `https`.  If the value is not specified in the task, the value of environment variable `DOCKER_HOST` will be used instead. If the environment variable is not set, the default value will be used.  Default: `"unix://var/run/docker.sock"` |
| **election_tick**  integer | Amount of ticks (in seconds) needed without a leader to trigger a new election.  Docker default value is `10s`. |
| **force**  boolean | Use with state `present` to force creating a new Swarm, even if already part of one.  Use with state `absent` to Leave the swarm even if this node is a manager.  Choices:   - `false` ← (default) - `true` |
| **heartbeat_tick**  integer | Amount of ticks (in seconds) between each heartbeat.  Docker default value is `1s`. |
| **join_token**  string | Swarm token used to join a swarm cluster.  Used with *state=join*.  If this value is specified, the corresponding value in the return values will be censored by Ansible. This is a side-effect of this value not being logged. |
| **keep_old_snapshots**  integer | Number of snapshots to keep beyond the current snapshot.  Docker default value is `0`. |
| **labels**  dictionary | User-defined key/value metadata.  Label operations in this module apply to the docker swarm cluster. Use [community.docker.docker_node](docker_node_module.md#ansible-collections-community-docker-docker-node-module) module to add/modify/remove swarm node labels.  Requires API version >= 1.32. |
| **listen_addr**  string | Listen address used for inter-manager communication.  This can either be an address/port combination in the form `192.168.1.1:4567`, or an interface followed by a port number, like `eth0:4567`.  If the port number is omitted, the default swarm listening port is used.  Only used when swarm is initialised or joined. Because of this it’s not considered for idempotency checking.  Default: `"0.0.0.0:2377"` |
| **log_entries_for_slow_followers**  integer | Number of log entries to keep around to sync up slow followers after a snapshot is created. |
| **name**  string | The name of the swarm. |
| **node_cert_expiry**  integer | Automatic expiry for nodes certificates.  Docker default value is `3months`. |
| **node_id**  string | Swarm id of the node to remove.  Used with *state=remove*. |
| **remote_addrs**  list / elements=string | Remote address of one or more manager nodes of an existing Swarm to connect to.  Used with *state=join*. |
| **rotate_manager_token**  boolean | Rotate the manager join token.  Choices:   - `false` ← (default) - `true` |
| **rotate_worker_token**  boolean | Rotate the worker join token.  Choices:   - `false` ← (default) - `true` |
| **signing_ca_cert**  string | The desired signing CA certificate for all swarm node TLS leaf certificates, in PEM format.  This must not be a path to a certificate, but the contents of the certificate.  Requires API version >= 1.30. |
| **signing_ca_key**  string | The desired signing CA key for all swarm node TLS leaf certificates, in PEM format.  This must not be a path to a key, but the contents of the key.  Requires API version >= 1.30. |
| **snapshot_interval**  integer | Number of logs entries between snapshot.  Docker default value is `10000`. |
| **ssl_version**  string | Provide a valid SSL version number. Default value determined by ssl.py module.  If the value is not specified in the task, the value of environment variable `DOCKER_SSL_VERSION` will be used instead. |
| **state**  string | Set to `present`, to create/update a new cluster.  Set to `join`, to join an existing cluster.  Set to `absent`, to leave an existing cluster.  Set to `remove`, to remove an absent node from the cluster. Note that removing requires Docker SDK for Python >= 2.4.0.  Choices:   - `"present"` ← (default) - `"join"` - `"absent"` - `"remove"` |
| **subnet_size**  integer | Default address pool subnet mask length.  Only used when swarm is initialised. Because of this it’s not considered for idempotency checking.  Requires API version >= 1.39. |
| **task_history_retention_limit**  integer | Maximum number of tasks history stored.  Docker default value is `5`. |
| **timeout**  integer | The maximum amount of time in seconds to wait on a response from the API.  If the value is not specified in the task, the value of environment variable `DOCKER_TIMEOUT` will be used instead. If the environment variable is not set, the default value will be used.  Default: `60` |
| **tls**  boolean | Secure the connection to the API by using TLS without verifying the authenticity of the Docker host server. Note that if *validate_certs* is set to `true` as well, it will take precedence.  If the value is not specified in the task, the value of environment variable `DOCKER_TLS` will be used instead. If the environment variable is not set, the default value will be used.  Choices:   - `false` ← (default) - `true` |
| **tls_hostname**  string | When verifying the authenticity of the Docker Host server, provide the expected name of the server.  If the value is not specified in the task, the value of environment variable `DOCKER_TLS_HOSTNAME` will be used instead. If the environment variable is not set, the default value will be used.  The current default value is `localhost`. This default is deprecated and will change in community.docker 2.0.0 to be a value computed from *docker_host*. Explicitly specify `localhost` to make sure this value will still be used, and to disable the deprecation message which will be shown otherwise. |
| **use_ssh_client**  boolean  added in community.docker 1.5.0 | For SSH transports, use the `ssh` CLI tool instead of paramiko.  Requires Docker SDK for Python 4.4.0 or newer.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  aliases: tls_verify  boolean | Secure the connection to the API by using TLS and verifying the authenticity of the Docker host server.  If the value is not specified in the task, the value of environment variable `DOCKER_TLS_VERIFY` will be used instead. If the environment variable is not set, the default value will be used.  Choices:   - `false` ← (default) - `true` |

## [Notes](docker_swarm_module.md#id4)

> **Note:**
>
> - Connect to the Docker daemon by providing parameters with each task or by defining environment variables. You can define `DOCKER_HOST`, `DOCKER_TLS_HOSTNAME`, `DOCKER_API_VERSION`, `DOCKER_CERT_PATH`, `DOCKER_SSL_VERSION`, `DOCKER_TLS`, `DOCKER_TLS_VERIFY` and `DOCKER_TIMEOUT`. If you are using docker machine, run the script shipped with the product that sets up the environment. It will set these variables for you. See <https://docs.docker.com/machine/reference/env/> for more details.
> - When connecting to Docker daemon with TLS, you might need to install additional Python packages. For the Docker SDK for Python, version 2.4 or newer, this can be done by installing `docker[tls]` with [ansible.builtin.pip](../../ansible/builtin/pip_module.md#ansible-collections-ansible-builtin-pip-module).
> - Note that the Docker SDK for Python only allows to specify the path to the Docker configuration for very few functions. In general, it will use `$HOME/.docker/config.json` if the `DOCKER_CONFIG` environment variable is not specified, and use `$DOCKER_CONFIG/config.json` otherwise.
> - This module uses the [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/) to communicate with the Docker daemon.

## [Examples](docker_swarm_module.md#id5)

```yaml+jinja
- name: Init a new swarm with default parameters
  community.docker.docker_swarm:
    state: present

- name: Update swarm configuration
  community.docker.docker_swarm:
    state: present
    election_tick: 5

- name: Add nodes
  community.docker.docker_swarm:
    state: join
    advertise_addr: 192.168.1.2
    join_token: SWMTKN-1--xxxxx
    remote_addrs: [ '192.168.1.1:2377' ]

- name: Leave swarm for a node
  community.docker.docker_swarm:
    state: absent

- name: Remove a swarm manager
  community.docker.docker_swarm:
    state: absent
    force: true

- name: Remove node from swarm
  community.docker.docker_swarm:
    state: remove
    node_id: mynode

- name: Init a new swarm with different data path interface
  community.docker.docker_swarm:
    state: present
    advertise_addr: eth0
    data_path_addr: ens10
```

## [Return Values](docker_swarm_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **actions**  list / elements=string | Provides the actions done on the swarm.  Returned: when action failed.  Sample: `["This cluster is already a swarm cluster"]` |
| **swarm_facts**  dictionary | Informations about swarm.  Returned: success |
| **JoinTokens**  dictionary | Tokens to connect to the Swarm.  Returned: success |
| **Manager**  string | Token to join the cluster as a new \*manager\* node.  **Note:** if this value has been specified as *join_token*, the value here will not be the token, but `VALUE_SPECIFIED_IN_NO_LOG_PARAMETER`. If you pass *join_token*, make sure your playbook/role does not depend on this return value!  Returned: success  Sample: `"SWMTKN-1--xxxxx"` |
| **Worker**  string | Token to join the cluster as a new \*worker\* node.  **Note:** if this value has been specified as *join_token*, the value here will not be the token, but `VALUE_SPECIFIED_IN_NO_LOG_PARAMETER`. If you pass *join_token*, make sure your playbook/role does not depend on this return value!  Returned: success  Sample: `"SWMTKN-1--xxxxx"` |
| **UnlockKey**  string | The swarm unlock-key if *autolock_managers* is `true`.  Returned: on success if *autolock_managers* is `true` and swarm is initialised, or if *autolock_managers* has changed.  Sample: `"SWMKEY-1-xxx"` |

### Authors

- Thierry Bouvet (@tbouvet)
- Piotr Wojciechowski (@WojciechowskiPiotr)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.docker/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.docker)
[Submit a bug report](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-docker)
