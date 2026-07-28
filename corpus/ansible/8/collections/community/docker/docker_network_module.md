---
collection: ansible
version: "8"
title: "community.docker.docker_network module – Manage Docker networks"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/docker/docker_network_module.html
fetched_at: 2026-07-28T01:43:49+00:00
---
# community.docker.docker_network module – Manage Docker networks

> **Note:**
>
> This module is part of the [community.docker collection](https://galaxy.ansible.com/ui/repo/published/community/docker/) (version 3.4.11).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.docker`.
> You need further requirements to be able to use this module,
> see [Requirements](docker_network_module.md#ansible-collections-community-docker-docker-network-module-requirements) for details.
>
> To use it in a playbook, specify: `community.docker.docker_network`.

- [Synopsis](docker_network_module.md#synopsis)
- [Requirements](docker_network_module.md#requirements)
- [Parameters](docker_network_module.md#parameters)
- [Attributes](docker_network_module.md#attributes)
- [Notes](docker_network_module.md#notes)
- [Examples](docker_network_module.md#examples)
- [Return Values](docker_network_module.md#return-values)

## [Synopsis](docker_network_module.md#id1)

- Create/remove Docker networks and connect containers to them.
- Performs largely the same function as the `docker network` CLI subcommand.

## [Requirements](docker_network_module.md#id2)

The below requirements are needed on the host that executes this module.

- Docker API >= 1.25
- backports.ssl_match_hostname (when using TLS on Python 2)
- paramiko (when using SSH with `use_ssh_client=false`)
- pyOpenSSL (when using TLS)
- pywin32 (when using named pipes on Windows 32)
- requests

## [Parameters](docker_network_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_version**  aliases: docker_api_version  string | The version of the Docker API running on the Docker Host.  Defaults to the latest version of the API supported by this collection and the docker daemon.  If the value is not specified in the task, the value of environment variable [`DOCKER_API_VERSION`](docsite/scenario_guide.md#envvar-DOCKER_API_VERSION) will be used instead. If the environment variable is not set, the default value will be used.  **Default:** `"auto"` |
| **appends**  aliases: incremental  boolean | By default the connected list is canonical, meaning containers not on the list are removed from the network.  Use `appends` to leave existing containers connected.  **Choices:**   - `false` ← (default) - `true` |
| **attachable**  boolean | If enabled, and the network is in the global scope, non-service containers on worker nodes will be able to connect to the network.  **Choices:**   - `false` - `true` |
| **ca_cert**  aliases: tls_ca_cert, cacert_path  path | Use a CA certificate when performing server verification by providing the path to a CA certificate file.  If the value is not specified in the task and the environment variable [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH) is set, the file `ca.pem` from the directory specified in the environment variable [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH) will be used. |
| **client_cert**  aliases: tls_client_cert, cert_path  path | Path to the client’s TLS certificate file.  If the value is not specified in the task and the environment variable [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH) is set, the file `cert.pem` from the directory specified in the environment variable [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH) will be used. |
| **client_key**  aliases: tls_client_key, key_path  path | Path to the client’s TLS key file.  If the value is not specified in the task and the environment variable [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH) is set, the file `key.pem` from the directory specified in the environment variable [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH) will be used. |
| **connected**  aliases: containers  list / elements=string | List of container names or container IDs to connect to a network.  Please note that the module only makes sure that these containers are connected to the network, but does not care about connection options. If you rely on specific IP addresses etc., use the [community.docker.docker_container](docker_container_module.md#ansible-collections-community-docker-docker-container-module) module to ensure your containers are correctly connected to this network.  **Default:** `[]` |
| **debug**  boolean | Debug mode  **Choices:**   - `false` ← (default) - `true` |
| **docker_host**  aliases: docker_url  string | The URL or Unix socket path used to connect to the Docker API. To connect to a remote host, provide the TCP connection string. For example, `tcp://192.0.2.23:2376`. If TLS is used to encrypt the connection, the module will automatically replace `tcp` in the connection URL with `https`.  If the value is not specified in the task, the value of environment variable [`DOCKER_HOST`](docsite/scenario_guide.md#envvar-DOCKER_HOST) will be used instead. If the environment variable is not set, the default value will be used.  **Default:** `"unix://var/run/docker.sock"` |
| **driver**  string | Specify the type of network. Docker provides bridge and overlay drivers, but 3rd party drivers can also be used.  **Default:** `"bridge"` |
| **driver_options**  dictionary | Dictionary of network settings. Consult docker docs for valid options and values.  **Default:** `{}` |
| **enable_ipv6**  boolean | Enable IPv6 networking.  **Choices:**   - `false` - `true` |
| **force**  boolean | With state `absent` forces disconnecting all containers from the network prior to deleting the network. With state `present` will disconnect all containers, delete the network and re-create the network.  This option is required if you have changed the IPAM or driver options and want an existing network to be updated to use the new options.  **Choices:**   - `false` ← (default) - `true` |
| **internal**  boolean | Restrict external access to the network.  **Choices:**   - `false` - `true` |
| **ipam_config**  list / elements=dictionary | List of IPAM config blocks. Consult [Docker docs](https://docs.docker.com/compose/compose-file/compose-file-v2/#ipam) for valid options and values. Note that `ipam_config[].iprange` is spelled differently here (we use the notation from the Docker SDK for Python). |
| **aux_addresses**  dictionary | Auxiliary IP addresses used by Network driver, as a mapping from hostname to IP. |
| **gateway**  string | IP gateway address. |
| **iprange**  string | IP address range in CIDR notation. |
| **subnet**  string | IP subset in CIDR notation. |
| **ipam_driver**  string | Specify an IPAM driver. |
| **ipam_driver_options**  dictionary | Dictionary of IPAM driver options. |
| **labels**  dictionary | Dictionary of labels.  **Default:** `{}` |
| **name**  aliases: network_name  string / required | Name of the network to operate on. |
| **scope**  string | Specify the network’s scope.  **Choices:**   - `"local"` - `"global"` - `"swarm"` |
| **ssl_version**  string | Provide a valid SSL version number. Default value determined by [SSL Python module](https://docs.python.org/3/library/ssl.html).  If the value is not specified in the task, the value of environment variable [`DOCKER_SSL_VERSION`](docsite/scenario_guide.md#envvar-DOCKER_SSL_VERSION) will be used instead. |
| **state**  string | `absent` deletes the network. If a network has connected containers, it cannot be deleted. Use the `force` option to disconnect all containers and delete the network.  `present` creates the network, if it does not already exist with the specified parameters, and connects the list of containers provided via the connected parameter. Containers not on the list will be disconnected. An empty list will leave no containers connected to the network. Use the `appends` option to leave existing containers connected. Use the `force` options to force re-creation of the network.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **timeout**  integer | The maximum amount of time in seconds to wait on a response from the API.  If the value is not specified in the task, the value of environment variable [`DOCKER_TIMEOUT`](docsite/scenario_guide.md#envvar-DOCKER_TIMEOUT) will be used instead. If the environment variable is not set, the default value will be used.  **Default:** `60` |
| **tls**  boolean | Secure the connection to the API by using TLS without verifying the authenticity of the Docker host server. Note that if `validate_certs` is set to `true` as well, it will take precedence.  If the value is not specified in the task, the value of environment variable [`DOCKER_TLS`](docsite/scenario_guide.md#envvar-DOCKER_TLS) will be used instead. If the environment variable is not set, the default value will be used.  **Choices:**   - `false` ← (default) - `true` |
| **tls_hostname**  string | When verifying the authenticity of the Docker Host server, provide the expected name of the server.  If the value is not specified in the task, the value of environment variable [`DOCKER_TLS_HOSTNAME`](docsite/scenario_guide.md#envvar-DOCKER_TLS_HOSTNAME) will be used instead. If the environment variable is not set, the default value will be used.  Note that this option had a default value `localhost` in older versions. It was removed in community.docker 3.0.0. |
| **use_ssh_client**  boolean  *added in community.docker 1.5.0* | For SSH transports, use the `ssh` CLI tool instead of paramiko.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  aliases: tls_verify  boolean | Secure the connection to the API by using TLS and verifying the authenticity of the Docker host server.  If the value is not specified in the task, the value of environment variable [`DOCKER_TLS_VERIFY`](docsite/scenario_guide.md#envvar-DOCKER_TLS_VERIFY) will be used instead. If the environment variable is not set, the default value will be used.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](docker_network_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | **Action groups:** **community.docker.docker**, **docker** | Use `group/docker` or `group/community.docker.docker` in `module_defaults` to set defaults for this module. |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](docker_network_module.md#id5)

> **Note:**
>
> - When network options are changed, the module disconnects all containers from the network, deletes the network, and re-creates the network. It does not try to reconnect containers, except the ones listed in (`connected`, and even for these, it does not consider specific connection options like fixed IP addresses or MAC addresses. If you need more control over how the containers are connected to the network, loop the [community.docker.docker_container](docker_container_module.md#ansible-collections-community-docker-docker-container-module) module to loop over your containers to make sure they are connected properly.
> - The module does not support Docker Swarm. This means that it will not try to disconnect or reconnect services. If services are connected to the network, deleting the network will fail. When network options are changed, the network has to be deleted and recreated, so this will fail as well.
> - Connect to the Docker daemon by providing parameters with each task or by defining environment variables. You can define [`DOCKER_HOST`](docsite/scenario_guide.md#envvar-DOCKER_HOST), [`DOCKER_TLS_HOSTNAME`](docsite/scenario_guide.md#envvar-DOCKER_TLS_HOSTNAME), [`DOCKER_API_VERSION`](docsite/scenario_guide.md#envvar-DOCKER_API_VERSION), [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH), [`DOCKER_SSL_VERSION`](docsite/scenario_guide.md#envvar-DOCKER_SSL_VERSION), [`DOCKER_TLS`](docsite/scenario_guide.md#envvar-DOCKER_TLS), [`DOCKER_TLS_VERIFY`](docsite/scenario_guide.md#envvar-DOCKER_TLS_VERIFY) and [`DOCKER_TIMEOUT`](docsite/scenario_guide.md#envvar-DOCKER_TIMEOUT). If you are using docker machine, run the script shipped with the product that sets up the environment. It will set these variables for you. See <https://docs.docker.com/machine/reference/env/> for more details.
> - This module does **not** use the [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/) to communicate with the Docker daemon. It uses code derived from the Docker SDK or Python that is included in this collection.

## [Examples](docker_network_module.md#id6)

```yaml+jinja
- name: Create a network
  community.docker.docker_network:
    name: network_one

- name: Remove all but selected list of containers
  community.docker.docker_network:
    name: network_one
    connected:
      - container_a
      - container_b
      - container_c

- name: Remove a single container
  community.docker.docker_network:
    name: network_one
    connected: "{{ fulllist|difference(['container_a']) }}"

- name: Add a container to a network, leaving existing containers connected
  community.docker.docker_network:
    name: network_one
    connected:
      - container_a
    appends: true

- name: Create a network with driver options
  community.docker.docker_network:
    name: network_two
    driver_options:
      com.docker.network.bridge.name: net2

- name: Create a network with custom IPAM config
  community.docker.docker_network:
    name: network_three
    ipam_config:
      - subnet: 172.23.27.0/24
        gateway: 172.23.27.2
        iprange: 172.23.27.0/26
        aux_addresses:
          host1: 172.23.27.3
          host2: 172.23.27.4

- name: Create a network with labels
  community.docker.docker_network:
    name: network_four
    labels:
      key1: value1
      key2: value2

- name: Create a network with IPv6 IPAM config
  community.docker.docker_network:
    name: network_ipv6_one
    enable_ipv6: true
    ipam_config:
      - subnet: fdd1:ac8c:0557:7ce1::/64

- name: Create a network with IPv6 and custom IPv4 IPAM config
  community.docker.docker_network:
    name: network_ipv6_two
    enable_ipv6: true
    ipam_config:
      - subnet: 172.24.27.0/24
      - subnet: fdd1:ac8c:0557:7ce2::/64

- name: Delete a network, disconnecting all containers
  community.docker.docker_network:
    name: network_one
    state: absent
    force: true
```

## [Return Values](docker_network_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **network**  dictionary | Network inspection results for the affected network.  **Returned:** success  **Sample:** `{}` |

### Authors

- Ben Keith (@keitwb)
- Chris Houseknecht (@chouseknecht)
- Dave Bendit (@DBendit)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.docker/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.docker)
- [Submit a bug report](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-docker)
