---
collection: ansible
version: "8"
title: "community.docker.docker_swarm inventory – Ansible dynamic inventory plugin for Docker swarm nodes."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/docker/docker_swarm_inventory.html
fetched_at: 2026-07-28T01:44:05+00:00
---
# community.docker.docker_swarm inventory – Ansible dynamic inventory plugin for Docker swarm nodes.

> **Note:**
>
> This inventory plugin is part of the [community.docker collection](https://galaxy.ansible.com/ui/repo/published/community/docker/) (version 3.4.11).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.docker`.
> You need further requirements to be able to use this inventory plugin,
> see [Requirements](docker_swarm_inventory.md#ansible-collections-community-docker-docker-swarm-inventory-requirements) for details.
>
> To use it in a playbook, specify: `community.docker.docker_swarm`.

- [Synopsis](docker_swarm_inventory.md#synopsis)
- [Requirements](docker_swarm_inventory.md#requirements)
- [Parameters](docker_swarm_inventory.md#parameters)
- [Examples](docker_swarm_inventory.md#examples)

## [Synopsis](docker_swarm_inventory.md#id1)

- Reads inventories from the Docker swarm API.
- Uses a YAML configuration file docker_swarm.[yml|yaml].
- The plugin returns following groups of swarm nodes: `all` - all hosts; `workers` - all worker nodes; `managers` - all manager nodes; `leader` - the swarm leader node; `nonleaders` - all nodes except the swarm leader.

## [Requirements](docker_swarm_inventory.md#id2)

The below requirements are needed on the local controller node that executes this inventory.

- python >= 2.7
- [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/) >= 1.10.0

## [Parameters](docker_swarm_inventory.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_version**  aliases: docker_api_version  string | The version of the Docker API running on the Docker Host.  Defaults to the latest version of the API supported by Docker SDK for Python. |
| **ca_cert**  aliases: tls_ca_cert, cacert_path  path | Use a CA certificate when performing server verification by providing the path to a CA certificate file. |
| **client_cert**  aliases: tls_client_cert, cert_path  path | Path to the client’s TLS certificate file. |
| **client_key**  aliases: tls_client_key, key_path  path | Path to the client’s TLS key file. |
| **compose**  dictionary | Create vars from jinja2 expressions.  **Default:** `{}` |
| **docker_host**  aliases: docker_url  string / required | Socket of a Docker swarm manager node (`tcp`, `unix`).  Use `unix://var/run/docker.sock` to connect via local socket. |
| **groups**  dictionary | Add hosts to group based on Jinja2 conditionals.  **Default:** `{}` |
| **include_host_uri**  boolean | Toggle to return the additional attribute `ansible_host_uri` which contains the URI of the swarm leader in format of `tcp://172.16.0.1:2376`. This value may be used without additional modification as value of option `docker_host` in Docker Swarm modules when connecting via API. The port always defaults to `2376`.  **Choices:**   - `false` ← (default) - `true` |
| **include_host_uri_port**  integer | Override the detected port number included in `ansible_host_uri`. |
| **keyed_groups**  list / elements=dictionary | Add hosts to group based on the values of a variable.  **Default:** `[]` |
| **default_value**  string  *added in ansible-core 2.12* | The default value when the host variable’s value is an empty string.  This option is mutually exclusive with `trailing_separator`. |
| **key**  string | The key from input dictionary used to generate groups |
| **parent_group**  string | parent group for keyed group |
| **prefix**  string | A keyed group name will start with this prefix  **Default:** `""` |
| **separator**  string | separator used to build the keyed group name  **Default:** `"_"` |
| **trailing_separator**  boolean  *added in ansible-core 2.12* | Set this option to *False* to omit the `separator` after the host variable when the value is an empty string.  This option is mutually exclusive with `default_value`.  **Choices:**   - `false` - `true` ← (default) |
| **leading_separator**  boolean  *added in ansible-core 2.11* | Use in conjunction with keyed_groups.  By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.  This is because the default prefix is “” and the default separator is “_”.  Set this option to False to omit the leading underscore (or other separator) if no prefix is given.  If the group name is derived from a mapping the separator is still used to concatenate the items.  To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.  **Choices:**   - `false` - `true` ← (default) |
| **plugin**  string / required | The name of this plugin, it should always be set to `community.docker.docker_swarm` for this plugin to recognize it as it’s own.  **Choices:**   - `"docker_swarm"` - `"community.docker.docker_swarm"` |
| **ssl_version**  string | Provide a valid SSL version number. Default value determined by [SSL Python module](https://docs.python.org/3/library/ssl.html). |
| **strict**  boolean | If `yes` make invalid entries a fatal error, otherwise skip and continue.  Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.  **Choices:**   - `false` ← (default) - `true` |
| **timeout**  aliases: time_out  integer | The maximum amount of time in seconds to wait on a response from the API.  If the value is not specified in the task, the value of environment variable [`DOCKER_TIMEOUT`](docsite/scenario_guide.md#envvar-DOCKER_TIMEOUT). will be used instead. If the environment variable is not set, the default value will be used.  **Default:** `60` |
| **tls**  boolean | Connect using TLS without verifying the authenticity of the Docker host server.  **Choices:**   - `false` ← (default) - `true` |
| **tls_hostname**  string | When verifying the authenticity of the Docker host server, provide the expected name of the server. |
| **use_extra_vars**  boolean  *added in ansible-core 2.11* | Merge extra vars into the available variables for composition (highest precedence).  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory_plugins]   use_extra_vars = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_USE_EXTRA_VARS`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_USE_EXTRA_VARS) |
| **use_ssh_client**  boolean  *added in community.docker 1.5.0* | For SSH transports, use the `ssh` CLI tool instead of paramiko.  Requires Docker SDK for Python 4.4.0 or newer.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  aliases: tls_verify  boolean | Toggle if connecting using TLS with or without verifying the authenticity of the Docker host server.  **Choices:**   - `false` ← (default) - `true` |
| **verbose_output**  boolean | Toggle to (not) include all available nodes metadata (for example `Platform`, `Architecture`, `OS`, `EngineVersion`).  **Choices:**   - `false` - `true` ← (default) |

## [Examples](docker_swarm_inventory.md#id4)

```yaml+jinja
# Minimal example using local docker
plugin: community.docker.docker_swarm
docker_host: unix://var/run/docker.sock

# Minimal example using remote docker
plugin: community.docker.docker_swarm
docker_host: tcp://my-docker-host:2375

# Example using remote docker with unverified TLS
plugin: community.docker.docker_swarm
docker_host: tcp://my-docker-host:2376
tls: true

# Example using remote docker with verified TLS and client certificate verification
plugin: community.docker.docker_swarm
docker_host: tcp://my-docker-host:2376
validate_certs: true
ca_cert: /somewhere/ca.pem
client_key: /somewhere/key.pem
client_cert: /somewhere/cert.pem

# Example using constructed features to create groups and set ansible_host
plugin: community.docker.docker_swarm
docker_host: tcp://my-docker-host:2375
strict: false
keyed_groups:
  # add for example x86_64 hosts to an arch_x86_64 group
  - prefix: arch
    key: 'Description.Platform.Architecture'
  # add for example linux hosts to an os_linux group
  - prefix: os
    key: 'Description.Platform.OS'
  # create a group per node label
  # for exomple a node labeled w/ "production" ends up in group "label_production"
  # hint: labels containing special characters will be converted to safe names
  - key: 'Spec.Labels'
    prefix: label
```

### Authors

- Stefan Heitmüller (@morph027)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.docker/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.docker)
- [Submit a bug report](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-docker)
