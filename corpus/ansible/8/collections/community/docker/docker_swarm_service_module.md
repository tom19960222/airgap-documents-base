---
collection: ansible
version: "8"
title: "community.docker.docker_swarm_service module – docker swarm service"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/docker/docker_swarm_service_module.html
fetched_at: 2026-07-28T01:43:58+00:00
---
# community.docker.docker_swarm_service module – docker swarm service

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
> see [Requirements](docker_swarm_service_module.md#ansible-collections-community-docker-docker-swarm-service-module-requirements) for details.
>
> To use it in a playbook, specify: `community.docker.docker_swarm_service`.

- [Synopsis](docker_swarm_service_module.md#synopsis)
- [Requirements](docker_swarm_service_module.md#requirements)
- [Parameters](docker_swarm_service_module.md#parameters)
- [Attributes](docker_swarm_service_module.md#attributes)
- [Notes](docker_swarm_service_module.md#notes)
- [Examples](docker_swarm_service_module.md#examples)
- [Return Values](docker_swarm_service_module.md#return-values)

## [Synopsis](docker_swarm_service_module.md#id1)

- Manages docker services via a swarm manager node.
- This modules does not support updating services in a stack.

## [Requirements](docker_swarm_service_module.md#id2)

The below requirements are needed on the host that executes this module.

- Docker API >= 1.25
- Docker SDK for Python: Please note that the [docker-py](https://pypi.org/project/docker-py/) Python module has been superseded by [docker](https://pypi.org/project/docker/) (see [here](https://github.com/docker/docker-py/issues/1310) for details). This module does \*not\* work with docker-py.
- [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/) >= 2.0.2
- Python >= 2.7

## [Parameters](docker_swarm_service_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_version**  aliases: docker_api_version  string | The version of the Docker API running on the Docker Host.  Defaults to the latest version of the API supported by Docker SDK for Python and the docker daemon.  If the value is not specified in the task, the value of environment variable [`DOCKER_API_VERSION`](docsite/scenario_guide.md#envvar-DOCKER_API_VERSION) will be used instead. If the environment variable is not set, the default value will be used.  **Default:** `"auto"` |
| **args**  list / elements=string | List arguments to be passed to the container.  Corresponds to the `ARG` parameter of `docker service create`. |
| **ca_cert**  aliases: tls_ca_cert, cacert_path  path | Use a CA certificate when performing server verification by providing the path to a CA certificate file.  If the value is not specified in the task and the environment variable [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH) is set, the file `ca.pem` from the directory specified in the environment variable [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH) will be used. |
| **cap_add**  list / elements=string  *added in community.docker 2.2.0* | List of capabilities to add to the container.  Requires API version >= 1.41. |
| **cap_drop**  list / elements=string  *added in community.docker 2.2.0* | List of capabilities to drop from the container.  Requires API version >= 1.41. |
| **client_cert**  aliases: tls_client_cert, cert_path  path | Path to the client’s TLS certificate file.  If the value is not specified in the task and the environment variable [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH) is set, the file `cert.pem` from the directory specified in the environment variable [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH) will be used. |
| **client_key**  aliases: tls_client_key, key_path  path | Path to the client’s TLS key file.  If the value is not specified in the task and the environment variable [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH) is set, the file `key.pem` from the directory specified in the environment variable [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH) will be used. |
| **command**  any | Command to execute when the container starts.  A command may be either a string or a list or a list of strings.  Corresponds to the `COMMAND` parameter of `docker service create`. |
| **configs**  list / elements=dictionary | List of dictionaries describing the service configs.  Corresponds to the `--config` option of `docker service create`.  Requires API version >= 1.30. |
| **config_id**  string | Config’s ID. |
| **config_name**  string / required | Config’s name as defined at its creation. |
| **filename**  string | Name of the file containing the config. Defaults to the `configs[].config_name` if not specified. |
| **gid**  string | GID of the config file’s group. |
| **mode**  integer | File access mode inside the container. Must be an octal number (like `0644` or `0444`). |
| **uid**  string | UID of the config file’s owner. |
| **container_labels**  dictionary | Dictionary of key value pairs.  Corresponds to the `--container-label` option of `docker service create`. |
| **debug**  boolean | Debug mode  **Choices:**   - `false` ← (default) - `true` |
| **dns**  list / elements=string | List of custom DNS servers.  Corresponds to the `--dns` option of `docker service create`. |
| **dns_options**  list / elements=string | List of custom DNS options.  Corresponds to the `--dns-option` option of `docker service create`. |
| **dns_search**  list / elements=string | List of custom DNS search domains.  Corresponds to the `--dns-search` option of `docker service create`. |
| **docker_host**  aliases: docker_url  string | The URL or Unix socket path used to connect to the Docker API. To connect to a remote host, provide the TCP connection string. For example, `tcp://192.0.2.23:2376`. If TLS is used to encrypt the connection, the module will automatically replace `tcp` in the connection URL with `https`.  If the value is not specified in the task, the value of environment variable [`DOCKER_HOST`](docsite/scenario_guide.md#envvar-DOCKER_HOST) will be used instead. If the environment variable is not set, the default value will be used.  **Default:** `"unix://var/run/docker.sock"` |
| **endpoint_mode**  string | Service endpoint mode.  Corresponds to the `--endpoint-mode` option of `docker service create`.  **Choices:**   - `"vip"` - `"dnsrr"` |
| **env**  any | List or dictionary of the service environment variables.  If passed a list each items need to be in the format of `KEY=VALUE`.  If passed a dictionary values which might be parsed as numbers, booleans or other types by the YAML parser must be quoted (for example `"true"`) in order to avoid data loss.  Corresponds to the `--env` option of `docker service create`. |
| **env_files**  list / elements=path | List of paths to files, present on the target, containing environment variables `FOO=BAR`.  The order of the list is significant in determining the value assigned to a variable that shows up more than once.  If variable also present in `env`, then `env` value will override. |
| **force_update**  boolean | Force update even if no changes require it.  Corresponds to the `--force` option of `docker service update`.  **Choices:**   - `false` ← (default) - `true` |
| **groups**  list / elements=string | List of additional group names and/or IDs that the container process will run as.  Corresponds to the `--group` option of `docker service update`. |
| **healthcheck**  dictionary | Configure a check that is run to determine whether or not containers for this service are “healthy”. See the docs for the [HEALTHCHECK Dockerfile instruction](https://docs.docker.com/engine/reference/builder/#healthcheck) for details on how healthchecks work.  `healthcheck.interval`, `healthcheck.timeout`, and `healthcheck.start_period` are specified as durations. They accept duration as a string in a format that look like: `5h34m56s`, `1m30s`, and so on. The supported units are `us`, `ms`, `s`, `m` and `h`. |
| **interval**  string | Time between running the check. |
| **retries**  integer | Consecutive failures needed to report unhealthy. It accept integer value. |
| **start_period**  string | Start period for the container to initialize before starting health-retries countdown. |
| **test**  any | Command to run to check health.  Must be either a string or a list. If it is a list, the first item must be one of `NONE`, `CMD` or `CMD-SHELL`. |
| **timeout**  string | Maximum time to allow one check to run. |
| **hostname**  string | Container hostname.  Corresponds to the `--hostname` option of `docker service create`. |
| **hosts**  dictionary | Dict of host-to-IP mappings, where each host name is a key in the dictionary. Each host name will be added to the container’s /etc/hosts file.  Corresponds to the `--host` option of `docker service create`. |
| **image**  string | Service image path and tag.  Corresponds to the `IMAGE` parameter of `docker service create`. |
| **init**  boolean | Use an init inside each service container to forward signals and reap processes.  Corresponds to the `--init` option of `docker service create`.  Requires API version >= 1.37.  **Choices:**   - `false` - `true` |
| **labels**  dictionary | Dictionary of key value pairs.  Corresponds to the `--label` option of `docker service create`. |
| **limits**  dictionary | Configures service resource limits. |
| **cpus**  float | Service CPU limit. `0` equals no limit.  Corresponds to the `--limit-cpu` option of `docker service create`. |
| **memory**  string | Service memory limit in format `<number>[<unit>]`. Number is a positive integer. Unit can be `B` (byte), `K` (kibibyte, 1024B), `M` (mebibyte), `G` (gibibyte), `T` (tebibyte), or `P` (pebibyte).  `0` equals no limit.  Omitting the unit defaults to bytes.  Corresponds to the `--limit-memory` option of `docker service create`. |
| **logging**  dictionary | Logging configuration for the service. |
| **driver**  string | Configure the logging driver for a service.  Corresponds to the `--log-driver` option of `docker service create`. |
| **options**  dictionary | Options for service logging driver.  Corresponds to the `--log-opt` option of `docker service create`. |
| **mode**  string | Service replication mode.  Service will be removed and recreated when changed.  Corresponds to the `--mode` option of `docker service create`.  **Choices:**   - `"replicated"` ← (default) - `"global"` |
| **mounts**  list / elements=dictionary | List of dictionaries describing the service mounts.  Corresponds to the `--mount` option of `docker service create`. |
| **driver_config**  dictionary | Volume driver configuration.  Can only be used when `mounts[].type=volume`. |
| **name**  string | Name of the volume-driver plugin to use for the volume. |
| **options**  dictionary | Options as key-value pairs to pass to the driver for this volume. |
| **labels**  dictionary | Volume labels to apply. |
| **no_copy**  boolean | Disable copying of data from a container when a volume is created.  Can only be used when `mounts[].type=volume`.  **Choices:**   - `false` - `true` |
| **propagation**  string | The propagation mode to use.  Can only be used when `mounts[].type=bind`.  **Choices:**   - `"shared"` - `"slave"` - `"private"` - `"rshared"` - `"rslave"` - `"rprivate"` |
| **readonly**  boolean | Whether the mount should be read-only.  **Choices:**   - `false` - `true` |
| **source**  string | Mount source (for example a volume name or a host path).  Must be specified if `mounts[].type` is not `tmpfs`. |
| **target**  string / required | Container path. |
| **tmpfs_mode**  integer | File mode of the tmpfs in octal.  Can only be used when `mounts[].type=tmpfs`. |
| **tmpfs_size**  string | Size of the tmpfs mount in format `<number>[<unit>]`. Number is a positive integer. Unit can be `B` (byte), `K` (kibibyte, 1024B), `M` (mebibyte), `G` (gibibyte), `T` (tebibyte), or `P` (pebibyte).  Can only be used when `mounts[].type=tmpfs`. |
| **type**  string | The mount type.  Note that `npipe` is only supported by Docker for Windows. Also note that `npipe` was added in Ansible 2.9.  **Choices:**   - `"bind"` ← (default) - `"volume"` - `"tmpfs"` - `"npipe"` |
| **name**  string / required | Service name.  Corresponds to the `--name` option of `docker service create`. |
| **networks**  list / elements=any | List of the service networks names or dictionaries.  When passed dictionaries valid sub-options are `name`, which is required, and `aliases` and `options`.  Prior to API version 1.29, updating and removing networks is not supported. If changes are made the service will then be removed and recreated.  Corresponds to the `--network` option of `docker service create`. |
| **placement**  dictionary | Configures service placement preferences and constraints. |
| **constraints**  list / elements=string | List of the service constraints.  Corresponds to the `--constraint` option of `docker service create`. |
| **preferences**  list / elements=dictionary | List of the placement preferences as key value pairs.  Corresponds to the `--placement-pref` option of `docker service create`.  Requires API version >= 1.27. |
| **replicas_max_per_node**  integer  *added in community.docker 1.3.0* | Maximum number of tasks per node.  Corresponds to the `--replicas_max_per_node` option of `docker service create`.  Requires API version >= 1.40 |
| **publish**  list / elements=dictionary | List of dictionaries describing the service published ports.  Corresponds to the `--publish` option of `docker service create`. |
| **mode**  string | What publish mode to use.  Requires API version >= 1.32.  **Choices:**   - `"ingress"` - `"host"` |
| **protocol**  string | What protocol to use.  **Choices:**   - `"tcp"` ← (default) - `"udp"` |
| **published_port**  integer | The port to make externally available. |
| **target_port**  integer / required | The port inside the container to expose. |
| **read_only**  boolean | Mount the containers root filesystem as read only.  Corresponds to the `--read-only` option of `docker service create`.  **Choices:**   - `false` - `true` |
| **replicas**  integer | Number of containers instantiated in the service. Valid only if `mode=replicated`.  If set to `-1`, and service is not present, service replicas will be set to `1`.  If set to `-1`, and service is present, service replicas will be unchanged.  Corresponds to the `--replicas` option of `docker service create`.  **Default:** `-1` |
| **reservations**  dictionary | Configures service resource reservations. |
| **cpus**  float | Service CPU reservation. `0` equals no reservation.  Corresponds to the `--reserve-cpu` option of `docker service create`. |
| **memory**  string | Service memory reservation in format `<number>[<unit>]`. Number is a positive integer. Unit can be `B` (byte), `K` (kibibyte, 1024B), `M` (mebibyte), `G` (gibibyte), `T` (tebibyte), or `P` (pebibyte).  `0` equals no reservation.  Omitting the unit defaults to bytes.  Corresponds to the `--reserve-memory` option of `docker service create`. |
| **resolve_image**  boolean | If the current image digest should be resolved from registry and updated if changed.  Requires API version >= 1.30.  **Choices:**   - `false` ← (default) - `true` |
| **restart_config**  dictionary | Configures if and how to restart containers when they exit. |
| **condition**  string | Restart condition of the service.  Corresponds to the `--restart-condition` option of `docker service create`.  **Choices:**   - `"none"` - `"on-failure"` - `"any"` |
| **delay**  string | Delay between restarts.  Accepts a a string in a format that look like: `5h34m56s`, `1m30s` etc. The supported units are `us`, `ms`, `s`, `m` and `h`.  Corresponds to the `--restart-delay` option of `docker service create`. |
| **max_attempts**  integer | Maximum number of service restarts.  Corresponds to the `--restart-condition` option of `docker service create`. |
| **window**  string | Restart policy evaluation window.  Accepts a string in a format that look like: `5h34m56s`, `1m30s` etc. The supported units are `us`, `ms`, `s`, `m` and `h`.  Corresponds to the `--restart-window` option of `docker service create`. |
| **rollback_config**  dictionary | Configures how the service should be rolled back in case of a failing update. |
| **delay**  string | Delay between task rollbacks.  Accepts a string in a format that look like: `5h34m56s`, `1m30s` etc. The supported units are `us`, `ms`, `s`, `m` and `h`.  Corresponds to the `--rollback-delay` option of `docker service create`.  Requires API version >= 1.28. |
| **failure_action**  string | Action to take in case of rollback failure.  Corresponds to the `--rollback-failure-action` option of `docker service create`.  Requires API version >= 1.28.  **Choices:**   - `"continue"` - `"pause"` |
| **max_failure_ratio**  float | Fraction of tasks that may fail during a rollback.  Corresponds to the `--rollback-max-failure-ratio` option of `docker service create`.  Requires API version >= 1.28. |
| **monitor**  string | Duration after each task rollback to monitor for failure.  Accepts a string in a format that look like: `5h34m56s`, `1m30s` etc. The supported units are `us`, `ms`, `s`, `m` and `h`.  Corresponds to the `--rollback-monitor` option of `docker service create`.  Requires API version >= 1.28. |
| **order**  string | Specifies the order of operations during rollbacks.  Corresponds to the `--rollback-order` option of `docker service create`.  Requires API version >= 1.29. |
| **parallelism**  integer | The number of containers to rollback at a time. If set to 0, all containers rollback simultaneously.  Corresponds to the `--rollback-parallelism` option of `docker service create`.  Requires API version >= 1.28. |
| **secrets**  list / elements=dictionary | List of dictionaries describing the service secrets.  Corresponds to the `--secret` option of `docker service create`. |
| **filename**  string | Name of the file containing the secret. Defaults to the `secrets[].secret_name` if not specified.  Corresponds to the `target` key of `docker service create --secret`. |
| **gid**  string | GID of the secret file’s group. |
| **mode**  integer | File access mode inside the container. Must be an octal number (like `0644` or `0444`). |
| **secret_id**  string | Secret’s ID. |
| **secret_name**  string / required | Secret’s name as defined at its creation. |
| **uid**  string | UID of the secret file’s owner. |
| **ssl_version**  string | Provide a valid SSL version number. Default value determined by [SSL Python module](https://docs.python.org/3/library/ssl.html).  If the value is not specified in the task, the value of environment variable [`DOCKER_SSL_VERSION`](docsite/scenario_guide.md#envvar-DOCKER_SSL_VERSION) will be used instead. |
| **state**  string | `absent` - A service matching the specified name will be removed and have its tasks stopped.  `present` - Asserts the existence of a service matching the name and provided configuration parameters. Unspecified configuration parameters will be set to docker defaults.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **stop_grace_period**  string | Time to wait before force killing a container.  Accepts a duration as a string in a format that look like: `5h34m56s`, `1m30s` etc. The supported units are `us`, `ms`, `s`, `m` and `h`.  Corresponds to the `--stop-grace-period` option of `docker service create`. |
| **stop_signal**  string | Override default signal used to stop the container.  Corresponds to the `--stop-signal` option of `docker service create`. |
| **timeout**  integer | The maximum amount of time in seconds to wait on a response from the API.  If the value is not specified in the task, the value of environment variable [`DOCKER_TIMEOUT`](docsite/scenario_guide.md#envvar-DOCKER_TIMEOUT) will be used instead. If the environment variable is not set, the default value will be used.  **Default:** `60` |
| **tls**  boolean | Secure the connection to the API by using TLS without verifying the authenticity of the Docker host server. Note that if `validate_certs` is set to `true` as well, it will take precedence.  If the value is not specified in the task, the value of environment variable [`DOCKER_TLS`](docsite/scenario_guide.md#envvar-DOCKER_TLS) will be used instead. If the environment variable is not set, the default value will be used.  **Choices:**   - `false` ← (default) - `true` |
| **tls_hostname**  string | When verifying the authenticity of the Docker Host server, provide the expected name of the server.  If the value is not specified in the task, the value of environment variable [`DOCKER_TLS_HOSTNAME`](docsite/scenario_guide.md#envvar-DOCKER_TLS_HOSTNAME) will be used instead. If the environment variable is not set, the default value will be used.  Note that this option had a default value `localhost` in older versions. It was removed in community.docker 3.0.0. |
| **tty**  boolean | Allocate a pseudo-TTY.  Corresponds to the `--tty` option of `docker service create`.  **Choices:**   - `false` - `true` |
| **update_config**  dictionary | Configures how the service should be updated. Useful for configuring rolling updates. |
| **delay**  string | Rolling update delay.  Accepts a string in a format that look like: `5h34m56s`, `1m30s` etc. The supported units are `us`, `ms`, `s`, `m` and `h`.  Corresponds to the `--update-delay` option of `docker service create`. |
| **failure_action**  string | Action to take in case of container failure.  Corresponds to the `--update-failure-action` option of `docker service create`.  Usage of `rollback` requires API version >= 1.29.  **Choices:**   - `"continue"` - `"pause"` - `"rollback"` |
| **max_failure_ratio**  float | Fraction of tasks that may fail during an update before the failure action is invoked.  Corresponds to the `--update-max-failure-ratio` option of `docker service create`. |
| **monitor**  string | Time to monitor updated tasks for failures.  Accepts a string in a format that look like: `5h34m56s`, `1m30s` etc. The supported units are `us`, `ms`, `s`, `m` and `h`.  Corresponds to the `--update-monitor` option of `docker service create`. |
| **order**  string | Specifies the order of operations when rolling out an updated task.  Corresponds to the `--update-order` option of `docker service create`.  Requires API version >= 1.29. |
| **parallelism**  integer | Rolling update parallelism.  Corresponds to the `--update-parallelism` option of `docker service create`. |
| **use_ssh_client**  boolean  *added in community.docker 1.5.0* | For SSH transports, use the `ssh` CLI tool instead of paramiko.  Requires Docker SDK for Python 4.4.0 or newer.  **Choices:**   - `false` ← (default) - `true` |
| **user**  string | Sets the username or UID used for the specified command.  Before Ansible 2.8, the default value for this option was `root`.  The default has been removed so that the user defined in the image is used if no user is specified here.  Corresponds to the `--user` option of `docker service create`. |
| **validate_certs**  aliases: tls_verify  boolean | Secure the connection to the API by using TLS and verifying the authenticity of the Docker host server.  If the value is not specified in the task, the value of environment variable [`DOCKER_TLS_VERIFY`](docsite/scenario_guide.md#envvar-DOCKER_TLS_VERIFY) will be used instead. If the environment variable is not set, the default value will be used.  **Choices:**   - `false` ← (default) - `true` |
| **working_dir**  string | Path to the working directory.  Corresponds to the `--workdir` option of `docker service create`. |

## [Attributes](docker_swarm_service_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | **Action groups:** **community.docker.docker**, **docker** | Use `group/docker` or `group/community.docker.docker` in `module_defaults` to set defaults for this module. |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](docker_swarm_service_module.md#id5)

> **Note:**
>
> - Images will only resolve to the latest digest when using Docker API >= 1.30 and Docker SDK for Python >= 3.2.0. When using older versions use `force_update=true` to trigger the swarm to resolve a new image.
> - Connect to the Docker daemon by providing parameters with each task or by defining environment variables. You can define [`DOCKER_HOST`](docsite/scenario_guide.md#envvar-DOCKER_HOST), [`DOCKER_TLS_HOSTNAME`](docsite/scenario_guide.md#envvar-DOCKER_TLS_HOSTNAME), [`DOCKER_API_VERSION`](docsite/scenario_guide.md#envvar-DOCKER_API_VERSION), [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH), [`DOCKER_SSL_VERSION`](docsite/scenario_guide.md#envvar-DOCKER_SSL_VERSION), [`DOCKER_TLS`](docsite/scenario_guide.md#envvar-DOCKER_TLS), [`DOCKER_TLS_VERIFY`](docsite/scenario_guide.md#envvar-DOCKER_TLS_VERIFY) and [`DOCKER_TIMEOUT`](docsite/scenario_guide.md#envvar-DOCKER_TIMEOUT). If you are using docker machine, run the script shipped with the product that sets up the environment. It will set these variables for you. See <https://docs.docker.com/machine/reference/env/> for more details.
> - When connecting to Docker daemon with TLS, you might need to install additional Python packages. For the Docker SDK for Python, version 2.4 or newer, this can be done by installing `docker[tls]` with [ansible.builtin.pip](../../ansible/builtin/pip_module.md#ansible-collections-ansible-builtin-pip-module).
> - Note that the Docker SDK for Python only allows to specify the path to the Docker configuration for very few functions. In general, it will use `$HOME/.docker/config.json` if the `DOCKER_CONFIG` environment variable is not specified, and use `$DOCKER_CONFIG/config.json` otherwise.
> - This module uses the [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/) to communicate with the Docker daemon.

## [Examples](docker_swarm_service_module.md#id6)

```yaml+jinja
- name: Set command and arguments
  community.docker.docker_swarm_service:
    name: myservice
    image: alpine
    command: sleep
    args:
      - "3600"

- name: Set a bind mount
  community.docker.docker_swarm_service:
    name: myservice
    image: alpine
    mounts:
      - source: /tmp/
        target: /remote_tmp/
        type: bind

- name: Set service labels
  community.docker.docker_swarm_service:
    name: myservice
    image: alpine
    labels:
      com.example.description: "Accounting webapp"
      com.example.department: "Finance"

- name: Set environment variables
  community.docker.docker_swarm_service:
    name: myservice
    image: alpine
    env:
      ENVVAR1: envvar1
      ENVVAR2: envvar2
    env_files:
      - envs/common.env
      - envs/apps/web.env

- name: Set fluentd logging
  community.docker.docker_swarm_service:
    name: myservice
    image: alpine
    logging:
      driver: fluentd
      options:
        fluentd-address: "127.0.0.1:24224"
        fluentd-async-connect: "true"
        tag: myservice

- name: Set restart policies
  community.docker.docker_swarm_service:
    name: myservice
    image: alpine
    restart_config:
      condition: on-failure
      delay: 5s
      max_attempts: 3
      window: 120s

- name: Set update config
  community.docker.docker_swarm_service:
    name: myservice
    image: alpine
    update_config:
      parallelism: 2
      delay: 10s
      order: stop-first

- name: Set rollback config
  community.docker.docker_swarm_service:
    name: myservice
    image: alpine
    update_config:
      failure_action: rollback
    rollback_config:
      parallelism: 2
      delay: 10s
      order: stop-first

- name: Set placement preferences
  community.docker.docker_swarm_service:
    name: myservice
    image: alpine:edge
    placement:
      preferences:
        - spread: node.labels.mylabel
      constraints:
        - node.role == manager
        - engine.labels.operatingsystem == ubuntu 14.04
      replicas_max_per_node: 2

- name: Set configs
  community.docker.docker_swarm_service:
    name: myservice
    image: alpine:edge
    configs:
      - config_name: myconfig_name
        filename: "/tmp/config.txt"

- name: Set networks
  community.docker.docker_swarm_service:
    name: myservice
    image: alpine:edge
    networks:
      - mynetwork

- name: Set networks as a dictionary
  community.docker.docker_swarm_service:
    name: myservice
    image: alpine:edge
    networks:
      - name: "mynetwork"
        aliases:
          - "mynetwork_alias"
        options:
          foo: bar

- name: Set secrets
  community.docker.docker_swarm_service:
    name: myservice
    image: alpine:edge
    secrets:
      - secret_name: mysecret_name
        filename: "/run/secrets/secret.txt"

- name: Start service with healthcheck
  community.docker.docker_swarm_service:
    name: myservice
    image: nginx:1.13
    healthcheck:
      # Check if nginx server is healthy by curl'ing the server.
      # If this fails or timeouts, the healthcheck fails.
      test: ["CMD", "curl", "--fail", "http://nginx.host.com"]
      interval: 1m30s
      timeout: 10s
      retries: 3
      start_period: 30s

- name: Configure service resources
  community.docker.docker_swarm_service:
    name: myservice
    image: alpine:edge
    reservations:
      cpus: 0.25
      memory: 20M
    limits:
      cpus: 0.50
      memory: 50M

- name: Remove service
  community.docker.docker_swarm_service:
    name: myservice
    state: absent
```

## [Return Values](docker_swarm_service_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changes**  list / elements=string | List of changed service attributes if a service has been altered, [] otherwise.  **Returned:** always  **Sample:** `["container_labels", "replicas"]` |
| **rebuilt**  boolean | True if the service has been recreated (removed and created)  **Returned:** always  **Sample:** `true` |
| **swarm_service**  dictionary | Dictionary of variables representing the current state of the service. Matches the module parameters format.  Note that facts are not part of registered vars but accessible directly.  Note that before Ansible 2.7.9, the return variable was documented as `ansible_swarm_service`, while the module actually returned a variable called `ansible_docker_service`. The variable was renamed to `swarm_service` in both code and documentation for Ansible 2.7.9 and Ansible 2.8.0. In Ansible 2.7.x, the old name `ansible_docker_service` can still be used.  **Returned:** always  **Sample:** `{"args": ["3600"], "cap_add": null, "cap_drop": ["ALL"], "command": ["sleep"], "configs": null, "constraints": ["node.role == manager", "engine.labels.operatingsystem == ubuntu 14.04"], "container_labels": null, "dns": null, "dns_options": null, "dns_search": null, "endpoint_mode": null, "env": ["ENVVAR1=envvar1", "ENVVAR2=envvar2"], "force_update": null, "groups": null, "healthcheck": {"interval": 90000000000, "retries": 3, "start_period": 30000000000, "test": ["CMD", "curl", "--fail", "http://nginx.host.com"], "timeout": 10000000000}, "healthcheck_disabled": false, "hostname": null, "hosts": null, "image": "alpine:latest@sha256:b3dbf31b77fd99d9c08f780ce6f5282aba076d70a513a8be859d8d3a4d0c92b8", "labels": {"com.example.department": "Finance", "com.example.description": "Accounting webapp"}, "limit_cpu": 0.5, "limit_memory": 52428800, "log_driver": "fluentd", "log_driver_options": {"fluentd-address": "127.0.0.1:24224", "fluentd-async-connect": "true", "tag": "myservice"}, "mode": "replicated", "mounts": [{"driver_config": null, "labels": null, "no_copy": null, "propagation": null, "readonly": false, "source": "/tmp/", "target": "/remote_tmp/", "tmpfs_mode": null, "tmpfs_size": null, "type": "bind"}], "networks": null, "placement_preferences": [{"spread": "node.labels.mylabel"}], "publish": null, "read_only": null, "replicas": 1, "replicas_max_per_node": 1, "reserve_cpu": 0.25, "reserve_memory": 20971520, "restart_policy": "on-failure", "restart_policy_attempts": 3, "restart_policy_delay": 5000000000, "restart_policy_window": 120000000000, "secrets": null, "stop_grace_period": null, "stop_signal": null, "tty": null, "update_delay": 10000000000, "update_failure_action": null, "update_max_failure_ratio": null, "update_monitor": null, "update_order": "stop-first", "update_parallelism": 2, "user": null, "working_dir": null}` |

### Authors

- Dario Zanzico (@dariko)
- Jason Witkowski (@jwitko)
- Hannes Ljungberg (@hannseman)
- Piotr Wojciechowski (@wojciechowskipiotr)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.docker/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.docker)
- [Submit a bug report](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-docker)
