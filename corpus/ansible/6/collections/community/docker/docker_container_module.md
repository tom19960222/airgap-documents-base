---
collection: ansible
version: "6"
title: "community.docker.docker_container module – manage docker containers"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/docker/docker_container_module.html
fetched_at: 2026-07-27T17:07:15+00:00
---
# community.docker.docker_container module – manage docker containers

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
> see [Requirements](docker_container_module.md#ansible-collections-community-docker-docker-container-module-requirements) for details.
>
> To use it in a playbook, specify: `community.docker.docker_container`.

- [Synopsis](docker_container_module.md#synopsis)
- [Requirements](docker_container_module.md#requirements)
- [Parameters](docker_container_module.md#parameters)
- [Notes](docker_container_module.md#notes)
- [Examples](docker_container_module.md#examples)
- [Return Values](docker_container_module.md#return-values)

## [Synopsis](docker_container_module.md#id1)

- Manage the life cycle of docker containers.
- Supports check mode. Run with `--check` and `--diff` to view config difference and list of actions to be taken.

## [Requirements](docker_container_module.md#id2)

The below requirements are needed on the host that executes this module.

- Docker API >= 1.20
- Docker SDK for Python: Please note that the [docker-py](https://pypi.org/project/docker-py/) Python module has been superseded by [docker](https://pypi.org/project/docker/) (see [here](https://github.com/docker/docker-py/issues/1310) for details). For Python 2.6, `docker-py` must be used. Otherwise, it is recommended to install the `docker` Python module. Note that both modules should \*not\* be installed at the same time. Also note that when both modules are installed and one of them is uninstalled, the other might no longer function and a reinstall of it is required.
- [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/) >= 1.8.0 (use [docker-py](https://pypi.org/project/docker-py/) for Python 2.6)

## [Parameters](docker_container_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_version**  aliases: docker_api_version  string | The version of the Docker API running on the Docker Host.  Defaults to the latest version of the API supported by Docker SDK for Python and the docker daemon.  If the value is not specified in the task, the value of environment variable `DOCKER_API_VERSION` will be used instead. If the environment variable is not set, the default value will be used.  Default: `"auto"` |
| **auto_remove**  boolean | Enable auto-removal of the container on daemon side when the container’s process exits.  If *container_default_behavior* is set to `compatibility`, this option has a default of `false`.  Choices:   - `false` - `true` |
| **blkio_weight**  integer | Block IO (relative weight), between 10 and 1000. |
| **ca_cert**  aliases: tls_ca_cert, cacert_path  path | Use a CA certificate when performing server verification by providing the path to a CA certificate file.  If the value is not specified in the task and the environment variable `DOCKER_CERT_PATH` is set, the file `ca.pem` from the directory specified in the environment variable `DOCKER_CERT_PATH` will be used. |
| **cap_drop**  list / elements=string | List of capabilities to drop from the container. |
| **capabilities**  list / elements=string | List of capabilities to add to the container.  This is equivalent to `docker run --cap-add`, or the docker-compose option `cap_add`. |
| **cgroup_parent**  string  added in community.docker 1.1.0 | Specify the parent cgroup for the container. |
| **cleanup**  boolean | Use with *detach=false* to remove the container after successful execution.  Choices:   - `false` ← (default) - `true` |
| **client_cert**  aliases: tls_client_cert, cert_path  path | Path to the client’s TLS certificate file.  If the value is not specified in the task and the environment variable `DOCKER_CERT_PATH` is set, the file `cert.pem` from the directory specified in the environment variable `DOCKER_CERT_PATH` will be used. |
| **client_key**  aliases: tls_client_key, key_path  path | Path to the client’s TLS key file.  If the value is not specified in the task and the environment variable `DOCKER_CERT_PATH` is set, the file `key.pem` from the directory specified in the environment variable `DOCKER_CERT_PATH` will be used. |
| **command**  any | Command to execute when the container starts. A command may be either a string or a list.  Prior to version 2.4, strings were split on commas.  See *command_handling* for differences in how strings and lists are handled. |
| **command_handling**  string  added in community.docker 1.9.0 | The default behavior for *command* (when provided as a list) and *entrypoint* is to convert them to strings without considering shell quoting rules. (For comparing idempotency, the resulting string is split considering shell quoting rules.)  Also, setting *command* to an empty list of string, and setting *entrypoint* to an empty list will be handled as if these options are not specified. This is different from idempotency handling for other container-config related options.  When this is set to `compatibility`, which is the default until community.docker 3.0.0, the current behavior will be kept.  When this is set to `correct`, these options are kept as lists, and an empty value or empty list will be handled correctly for idempotency checks.  In community.docker 3.0.0, the default will change to `correct`.  Choices:   - `"compatibility"` - `"correct"` |
| **comparisons**  dictionary | Allows to specify how properties of existing containers are compared with module options to decide whether the container should be recreated / updated or not.  Only options which correspond to the state of a container as handled by the Docker daemon can be specified, as well as *networks*.  Must be a dictionary specifying for an option one of the keys `strict`, `ignore` and `allow_more_present`.  If `strict` is specified, values are tested for equality, and changes always result in updating or restarting. If `ignore` is specified, changes are ignored.  `allow_more_present` is allowed only for lists, sets and dicts. If it is specified for lists or sets, the container will only be updated or restarted if the module option contains a value which is not present in the container’s options. If the option is specified for a dict, the container will only be updated or restarted if the module option contains a key which is not present in the container’s option, or if the value of a key present differs.  The wildcard option `*` can be used to set one of the default values `strict` or `ignore` to *all* comparisons which are not explicitly set to other values.  See the examples for details. |
| **container_default_behavior**  string | In older versions of this module, various module options used to have default values. This caused problems with containers which use different values for these options.  The default value is now `no_defaults`. To restore the old behavior, set it to `compatibility`, which will ensure that the default values are used when the values are not explicitly specified by the user.  This affects the *auto_remove*, *detach*, *init*, *interactive*, *memory*, *paused*, *privileged*, *read_only* and *tty* options.  Choices:   - `"compatibility"` - `"no_defaults"` ← (default) |
| **cpu_period**  integer | Limit CPU CFS (Completely Fair Scheduler) period.  See *cpus* for an easier to use alternative. |
| **cpu_quota**  integer | Limit CPU CFS (Completely Fair Scheduler) quota.  See *cpus* for an easier to use alternative. |
| **cpu_shares**  integer | CPU shares (relative weight). |
| **cpus**  float | Specify how much of the available CPU resources a container can use.  A value of `1.5` means that at most one and a half CPU (core) will be used. |
| **cpuset_cpus**  string | CPUs in which to allow execution `1,3` or `1-3`. |
| **cpuset_mems**  string | Memory nodes (MEMs) in which to allow execution `0-3` or `0,1`. |
| **debug**  boolean | Debug mode  Choices:   - `false` ← (default) - `true` |
| **default_host_ip**  string  added in community.docker 1.2.0 | Define the default host IP to use.  Must be an empty string, an IPv4 address, or an IPv6 address.  With Docker 20.10.2 or newer, this should be set to an empty string (`""`) to avoid the port bindings without an explicit IP address to only bind to IPv4. See <https://github.com/ansible-collections/community.docker/issues/70> for details.  By default, the module will try to auto-detect this value from the `bridge` network’s `com.docker.network.bridge.host_binding_ipv4` option. If it cannot auto-detect it, it will fall back to `0.0.0.0`. |
| **detach**  boolean | Enable detached mode to leave the container running in background.  If disabled, the task will reflect the status of the container run (failed if the command failed).  If *container_default_behavior* is set to `compatibility`, this option has a default of `true`.  Choices:   - `false` - `true` |
| **device_read_bps**  list / elements=dictionary | List of device path and read rate (bytes per second) from device. |
| **path**  string / required | Device path in the container. |
| **rate**  string / required | Device read limit in format `<number>[<unit>]`.  Number is a positive integer. Unit can be one of `B` (byte), `K` (kibibyte, 1024B), `M` (mebibyte), `G` (gibibyte), `T` (tebibyte), or `P` (pebibyte).  Omitting the unit defaults to bytes. |
| **device_read_iops**  list / elements=dictionary | List of device and read rate (IO per second) from device. |
| **path**  string / required | Device path in the container. |
| **rate**  integer / required | Device read limit.  Must be a positive integer. |
| **device_requests**  list / elements=dictionary  added in community.docker 0.1.0 | Allows to request additional resources, such as GPUs. |
| **capabilities**  list / elements=list | List of lists of strings to request capabilities.  The top-level list entries are combined by OR, and for every list entry, the entries in the list it contains are combined by AND.  The driver tries to satisfy one of the sub-lists.  Available capabilities for the `nvidia` driver can be found at <https://github.com/NVIDIA/nvidia-container-runtime>. |
| **count**  integer | Number or devices to request.  Set to `-1` to request all available devices. |
| **device_ids**  list / elements=string | List of device IDs. |
| **driver**  string | Which driver to use for this device. |
| **options**  dictionary | Driver-specific options. |
| **device_write_bps**  list / elements=dictionary | List of device and write rate (bytes per second) to device. |
| **path**  string / required | Device path in the container. |
| **rate**  string / required | Device read limit in format `<number>[<unit>]`.  Number is a positive integer. Unit can be one of `B` (byte), `K` (kibibyte, 1024B), `M` (mebibyte), `G` (gibibyte), `T` (tebibyte), or `P` (pebibyte).  Omitting the unit defaults to bytes. |
| **device_write_iops**  list / elements=dictionary | List of device and write rate (IO per second) to device. |
| **path**  string / required | Device path in the container. |
| **rate**  integer / required | Device read limit.  Must be a positive integer. |
| **devices**  list / elements=string | List of host device bindings to add to the container.  Each binding is a mapping expressed in the format `<path_on_host>:<path_in_container>:<cgroup_permissions>`. |
| **dns_opts**  list / elements=string | List of DNS options. |
| **dns_search_domains**  list / elements=string | List of custom DNS search domains. |
| **dns_servers**  list / elements=string | List of custom DNS servers. |
| **docker_host**  aliases: docker_url  string | The URL or Unix socket path used to connect to the Docker API. To connect to a remote host, provide the TCP connection string. For example, `tcp://192.0.2.23:2376`. If TLS is used to encrypt the connection, the module will automatically replace `tcp` in the connection URL with `https`.  If the value is not specified in the task, the value of environment variable `DOCKER_HOST` will be used instead. If the environment variable is not set, the default value will be used.  Default: `"unix://var/run/docker.sock"` |
| **domainname**  string | Container domainname. |
| **entrypoint**  list / elements=string | Command that overwrites the default `ENTRYPOINT` of the image.  See *command_handling* for differences in how strings and lists are handled. |
| **env**  dictionary | Dictionary of key,value pairs.  Values which might be parsed as numbers, booleans or other types by the YAML parser must be quoted (for example `"true"`) in order to avoid data loss.  Please note that if you are passing values in with Jinja2 templates, like `"{{ value }}"`, you need to add `| string` to prevent Ansible to convert strings such as `"true"` back to booleans. The correct way is to use `"{{ value | string }}"`. |
| **env_file**  path | Path to a file, present on the target, containing environment variables *FOO=BAR*.  If variable also present in *env*, then the *env* value will override. |
| **etc_hosts**  dictionary | Dict of host-to-IP mappings, where each host name is a key in the dictionary. Each host name will be added to the container’s `/etc/hosts` file. |
| **exposed_ports**  aliases: exposed, expose  list / elements=string | List of additional container ports which informs Docker that the container listens on the specified network ports at runtime.  If the port is already exposed using `EXPOSE` in a Dockerfile, it does not need to be exposed again. |
| **force_kill**  aliases: forcekill  boolean | Use the kill command when stopping a running container.  Choices:   - `false` ← (default) - `true` |
| **groups**  list / elements=string | List of additional group names and/or IDs that the container process will run as. |
| **healthcheck**  dictionary | Configure a check that is run to determine whether or not containers for this service are “healthy”.  See the docs for the [HEALTHCHECK Dockerfile instruction](https://docs.docker.com/engine/reference/builder/#healthcheck) for details on how healthchecks work.  *interval*, *timeout* and *start_period* are specified as durations. They accept duration as a string in a format that look like: `5h34m56s`, `1m30s` etc. The supported units are `us`, `ms`, `s`, `m` and `h`. |
| **interval**  string | Time between running the check.  The default used by the Docker daemon is `30s`. |
| **retries**  integer | Consecutive number of failures needed to report unhealthy.  The default used by the Docker daemon is `3`. |
| **start_period**  string | Start period for the container to initialize before starting health-retries countdown.  The default used by the Docker daemon is `0s`. |
| **test**  any | Command to run to check health.  Must be either a string or a list. If it is a list, the first item must be one of `NONE`, `CMD` or `CMD-SHELL`. |
| **timeout**  string | Maximum time to allow one check to run.  The default used by the Docker daemon is `30s`. |
| **hostname**  string | The container’s hostname. |
| **ignore_image**  boolean | When *state* is `present` or `started`, the module compares the configuration of an existing container to requested configuration. The evaluation includes the image version. If the image version in the registry does not match the container, the container will be recreated. You can stop this behavior by setting *ignore_image* to `true`.  **Warning:** This option is ignored if `image: ignore` or `*: ignore` is specified in the *comparisons* option.  Choices:   - `false` ← (default) - `true` |
| **image**  string | Repository path and tag used to create the container. If an image is not found or pull is true, the image will be pulled from the registry. If no tag is included, `latest` will be used.  Can also be an image ID. If this is the case, the image is assumed to be available locally. The *pull* option is ignored for this case. |
| **image_label_mismatch**  string  added in community.docker 2.6.0 | How to handle labels inherited from the image that are not set explicitly.  When `ignore`, labels that are present in the image but not specified in *labels* will be ignored. This is useful to avoid having to specify the image labels in *labels* while keeping labels *comparisons* `strict`.  When `fail`, if there are labels present in the image which are not set from *labels*, the module will fail. This prevents introducing unexpected labels from the base image.  **Warning:** This option is ignored unless `labels: strict` or `*: strict` is specified in the *comparisons* option.  Choices:   - `"ignore"` ← (default) - `"fail"` |
| **init**  boolean | Run an init inside the container that forwards signals and reaps processes.  This option requires Docker API >= 1.25.  If *container_default_behavior* is set to `compatibility`, this option has a default of `false`.  Choices:   - `false` - `true` |
| **interactive**  boolean | Keep stdin open after a container is launched, even if not attached.  If *container_default_behavior* is set to `compatibility`, this option has a default of `false`.  Choices:   - `false` - `true` |
| **ipc_mode**  string | Set the IPC mode for the container.  Can be one of `container:<name|id>` to reuse another container’s IPC namespace or `host` to use the host’s IPC namespace within the container. |
| **keep_volumes**  boolean | Retain anonymous volumes associated with a removed container.  Choices:   - `false` - `true` ← (default) |
| **kernel_memory**  string | Kernel memory limit in format `<number>[<unit>]`. Number is a positive integer. Unit can be `B` (byte), `K` (kibibyte, 1024B), `M` (mebibyte), `G` (gibibyte), `T` (tebibyte), or `P` (pebibyte). Minimum is `4M`.  Omitting the unit defaults to bytes. |
| **kill_signal**  string | Override default signal used to kill a running container. |
| **labels**  dictionary | Dictionary of key value pairs. |
| **links**  list / elements=string | List of name aliases for linked containers in the format `container_name:alias`.  Setting this will force container to be restarted. |
| **log_driver**  string | Specify the logging driver. Docker uses `json-file` by default.  See [here](https://docs.docker.com/config/containers/logging/configure/) for possible choices. |
| **log_options**  aliases: log_opt  dictionary | Dictionary of options specific to the chosen *log_driver*.  See <https://docs.docker.com/engine/admin/logging/overview/> for details.  *log_driver* needs to be specified for *log_options* to take effect, even if using the default `json-file` driver. |
| **mac_address**  string | Container MAC address (for example, `92:d0:c6:0a:29:33`). |
| **memory**  string | Memory limit in format `<number>[<unit>]`. Number is a positive integer. Unit can be `B` (byte), `K` (kibibyte, 1024B), `M` (mebibyte), `G` (gibibyte), `T` (tebibyte), or `P` (pebibyte).  Omitting the unit defaults to bytes.  If *container_default_behavior* is set to `compatibility`, this option has a default of `"0"`. |
| **memory_reservation**  string | Memory soft limit in format `<number>[<unit>]`. Number is a positive integer. Unit can be `B` (byte), `K` (kibibyte, 1024B), `M` (mebibyte), `G` (gibibyte), `T` (tebibyte), or `P` (pebibyte).  Omitting the unit defaults to bytes. |
| **memory_swap**  string | Total memory limit (memory + swap) in format `<number>[<unit>]`, or the special values `unlimited` or `-1` for unlimited swap usage. Number is a positive integer. Unit can be `B` (byte), `K` (kibibyte, 1024B), `M` (mebibyte), `G` (gibibyte), `T` (tebibyte), or `P` (pebibyte).  Omitting the unit defaults to bytes. |
| **memory_swappiness**  integer | Tune a container’s memory swappiness behavior. Accepts an integer between 0 and 100.  If not set, the value will be remain the same if container exists and will be inherited from the host machine if it is (re-)created. |
| **mounts**  list / elements=dictionary | Specification for mounts to be added to the container. More powerful alternative to *volumes*. |
| **consistency**  string | The consistency requirement for the mount.  Choices:   - `"cached"` - `"consistent"` - `"default"` - `"delegated"` |
| **labels**  dictionary | User-defined name and labels for the volume. Only valid for the `volume` type. |
| **no_copy**  boolean | False if the volume should be populated with the data from the target. Only valid for the `volume` type.  The default value is `false`.  Choices:   - `false` - `true` |
| **propagation**  string | Propagation mode. Only valid for the `bind` type.  Choices:   - `"private"` - `"rprivate"` - `"shared"` - `"rshared"` - `"slave"` - `"rslave"` |
| **read_only**  boolean | Whether the mount should be read-only.  Choices:   - `false` - `true` |
| **source**  string | Mount source.  For example, this can be a volume name or a host path.  If not supplied when *type=volume* an anonymous volume will be created. |
| **target**  string / required | Path inside the container. |
| **tmpfs_mode**  string | The permission mode for the tmpfs mount. |
| **tmpfs_size**  string | The size for the tmpfs mount in bytes in format <number>[<unit>].  Number is a positive integer. Unit can be one of `B` (byte), `K` (kibibyte, 1024B), `M` (mebibyte), `G` (gibibyte), `T` (tebibyte), or `P` (pebibyte).  Omitting the unit defaults to bytes. |
| **type**  string | The mount type.  Note that `npipe` is only supported by Docker for Windows.  Choices:   - `"bind"` - `"npipe"` - `"tmpfs"` - `"volume"` ← (default) |
| **volume_driver**  string | Specify the volume driver. Only valid for the `volume` type.  See [here](https://docs.docker.com/storage/volumes/#use-a-volume-driver) for details. |
| **volume_options**  dictionary | Dictionary of options specific to the chosen volume_driver. See [here](https://docs.docker.com/storage/volumes/#use-a-volume-driver) for details. |
| **name**  string / required | Assign a name to a new container or match an existing container.  When identifying an existing container name may be a name or a long or short container ID. |
| **network_mode**  string | Connect the container to a network. Choices are `bridge`, `host`, `none`, `container:<name|id>`, `<network_name>` or `default`.  Since community.docker 2.0.0, if *networks_cli_compatible* is `true` and *networks* contains at least one network, the default value for *network_mode* is the name of the first network in the *networks* list. You can prevent this by explicitly specifying a value for *network_mode*, like the default value `default` which will be used by Docker if *network_mode* is not specified. |
| **networks**  list / elements=dictionary | List of networks the container belongs to.  For examples of the data structure and usage see EXAMPLES below.  To remove a container from one or more networks, use the *purge_networks* option.  If *networks_cli_compatible* is set to `false`, this will not remove the default network if *networks* is specified. This is different from the behavior of `docker run ...`. You need to explicitly use *purge_networks* to enforce the removal of the default network (and all other networks not explicitly mentioned in *networks*) in that case. |
| **aliases**  list / elements=string | List of aliases for this container in this network. These names can be used in the network to reach this container. |
| **ipv4_address**  string | The container’s IPv4 address in this network. |
| **ipv6_address**  string | The container’s IPv6 address in this network. |
| **links**  list / elements=string | A list of containers to link to. |
| **name**  string / required | The network’s name. |
| **networks_cli_compatible**  boolean | If *networks_cli_compatible* is set to `true` (default), this module will behave as `docker run --network` and will **not** add the default network if *networks* is specified. If *networks* is not specified, the default network will be attached.  When *networks_cli_compatible* is set to `false` and networks are provided to the module via the *networks* option, the module behaves differently than `docker run --network`: `docker run --network other` will create a container with network `other` attached, but the default network not attached. This module with *networks: {name: other}* will create a container with both `default` and `other` attached. If *purge_networks* is set to `true`, the `default` network will be removed afterwards.  Choices:   - `false` - `true` ← (default) |
| **oom_killer**  boolean | Whether or not to disable OOM Killer for the container.  Choices:   - `false` - `true` |
| **oom_score_adj**  integer | An integer value containing the score given to the container in order to tune OOM killer preferences. |
| **output_logs**  boolean | If set to true, output of the container command will be printed.  Only effective when *log_driver* is set to `json-file`, `journald`, or `local`.  Choices:   - `false` ← (default) - `true` |
| **paused**  boolean | Use with the started state to pause running processes inside the container.  If *container_default_behavior* is set to `compatibility`, this option has a default of `false`.  Choices:   - `false` - `true` |
| **pid_mode**  string | Set the PID namespace mode for the container.  Note that Docker SDK for Python < 2.0 only supports `host`. Newer versions of the Docker SDK for Python (docker) allow all values supported by the Docker daemon. |
| **pids_limit**  integer | Set PIDs limit for the container. It accepts an integer value.  Set `-1` for unlimited PIDs. |
| **privileged**  boolean | Give extended privileges to the container.  If *container_default_behavior* is set to `compatibility`, this option has a default of `false`.  Choices:   - `false` - `true` |
| **publish_all_ports**  boolean  added in community.docker 1.8.0 | Publish all ports to the host.  Any specified port bindings from *published_ports* will remain intact when `true`.  Choices:   - `false` - `true` |
| **published_ports**  aliases: ports  list / elements=string | List of ports to publish from the container to the host.  Use docker CLI syntax: `8000`, `9000:8000`, or `0.0.0.0:9000:8000`, where 8000 is a container port, 9000 is a host port, and 0.0.0.0 is a host interface.  Port ranges can be used for source and destination ports. If two ranges with different lengths are specified, the shorter range will be used. Since community.general 0.2.0, if the source port range has length 1, the port will not be assigned to the first port of the destination range, but to a free port in that range. This is the same behavior as for `docker` command line utility.  Bind addresses must be either IPv4 or IPv6 addresses. Hostnames are **not** allowed. This is different from the `docker` command line utility. Use the [dig lookup](../general/dig_lookup.md#ansible-collections-community-general-dig-lookup) to resolve hostnames.  A value of `all` will publish all exposed container ports to random host ports, ignoring any other mappings. This is deprecated since version 2.0.0 and will be disallowed in community.docker 3.0.0. Use the *publish_all_ports* option instead.  If *networks* parameter is provided, will inspect each network to see if there exists a bridge network with optional parameter `com.docker.network.bridge.host_binding_ipv4`. If such a network is found, then published ports where no host IP address is specified will be bound to the host IP pointed to by `com.docker.network.bridge.host_binding_ipv4`. Note that the first bridge network with a `com.docker.network.bridge.host_binding_ipv4` value encountered in the list of *networks* is the one that will be used. |
| **pull**  boolean | If true, always pull the latest version of an image. Otherwise, will only pull an image when missing.  **Note:** images are only pulled when specified by name. If the image is specified as a image ID (hash), it cannot be pulled.  Choices:   - `false` ← (default) - `true` |
| **purge_networks**  boolean | Remove the container from ALL networks not included in *networks* parameter.  Any default networks such as `bridge`, if not found in *networks*, will be removed as well.  Choices:   - `false` ← (default) - `true` |
| **read_only**  boolean | Mount the container’s root file system as read-only.  If *container_default_behavior* is set to `compatibility`, this option has a default of `false`.  Choices:   - `false` - `true` |
| **recreate**  boolean | Use with present and started states to force the re-creation of an existing container.  Choices:   - `false` ← (default) - `true` |
| **removal_wait_timeout**  float | When removing an existing container, the docker daemon API call exists after the container is scheduled for removal. Removal usually is very fast, but it can happen that during high I/O load, removal can take longer. By default, the module will wait until the container has been removed before trying to (re-)create it, however long this takes.  By setting this option, the module will wait at most this many seconds for the container to be removed. If the container is still in the removal phase after this many seconds, the module will fail. |
| **restart**  boolean | Use with started state to force a matching container to be stopped and restarted.  Choices:   - `false` ← (default) - `true` |
| **restart_policy**  string | Container restart policy.  Place quotes around `no` option.  Choices:   - `"no"` - `"on-failure"` - `"always"` - `"unless-stopped"` |
| **restart_retries**  integer | Use with restart policy to control maximum number of restart attempts. |
| **runtime**  string | Runtime to use for the container. |
| **security_opts**  list / elements=string | List of security options in the form of `"label:user:User"`. |
| **shm_size**  string | Size of `/dev/shm` in format `<number>[<unit>]`. Number is positive integer. Unit can be `B` (byte), `K` (kibibyte, 1024B), `M` (mebibyte), `G` (gibibyte), `T` (tebibyte), or `P` (pebibyte).  Omitting the unit defaults to bytes. If you omit the size entirely, Docker daemon uses `64M`. |
| **ssl_version**  string | Provide a valid SSL version number. Default value determined by ssl.py module.  If the value is not specified in the task, the value of environment variable `DOCKER_SSL_VERSION` will be used instead. |
| **state**  string | `absent` - A container matching the specified name will be stopped and removed. Use *force_kill* to kill the container rather than stopping it. Use *keep_volumes* to retain anonymous volumes associated with the removed container.  `present` - Asserts the existence of a container matching the name and any provided configuration parameters. If no container matches the name, a container will be created. If a container matches the name but the provided configuration does not match, the container will be updated, if it can be. If it cannot be updated, it will be removed and re-created with the requested config.  `started` - Asserts that the container is first `present`, and then if the container is not running moves it to a running state. Use *restart* to force a matching container to be stopped and restarted.  `stopped` - Asserts that the container is first `present`, and then if the container is running moves it to a stopped state.  To control what will be taken into account when comparing configuration, see the *comparisons* option. To avoid that the image version will be taken into account, you can also use the *ignore_image* option.  Use the *recreate* option to always force re-creation of a matching container, even if it is running.  If the container should be killed instead of stopped in case it needs to be stopped for recreation, or because *state* is `stopped`, please use the *force_kill* option. Use *keep_volumes* to retain anonymous volumes associated with a removed container.  Use *keep_volumes* to retain anonymous volumes associated with a removed container.  Choices:   - `"absent"` - `"present"` - `"stopped"` - `"started"` ← (default) |
| **stop_signal**  string | Override default signal used to stop the container. |
| **stop_timeout**  integer | Number of seconds to wait for the container to stop before sending `SIGKILL`. When the container is created by this module, its `StopTimeout` configuration will be set to this value.  When the container is stopped, will be used as a timeout for stopping the container. In case the container has a custom `StopTimeout` configuration, the behavior depends on the version of the docker daemon. New versions of the docker daemon will always use the container’s configured `StopTimeout` value if it has been configured. |
| **storage_opts**  dictionary  added in community.docker 1.3.0 | Storage driver options for this container as a key-value mapping. |
| **sysctls**  dictionary | Dictionary of key,value pairs. |
| **timeout**  integer | The maximum amount of time in seconds to wait on a response from the API.  If the value is not specified in the task, the value of environment variable `DOCKER_TIMEOUT` will be used instead. If the environment variable is not set, the default value will be used.  Default: `60` |
| **tls**  boolean | Secure the connection to the API by using TLS without verifying the authenticity of the Docker host server. Note that if *validate_certs* is set to `true` as well, it will take precedence.  If the value is not specified in the task, the value of environment variable `DOCKER_TLS` will be used instead. If the environment variable is not set, the default value will be used.  Choices:   - `false` ← (default) - `true` |
| **tls_hostname**  string | When verifying the authenticity of the Docker Host server, provide the expected name of the server.  If the value is not specified in the task, the value of environment variable `DOCKER_TLS_HOSTNAME` will be used instead. If the environment variable is not set, the default value will be used.  The current default value is `localhost`. This default is deprecated and will change in community.docker 2.0.0 to be a value computed from *docker_host*. Explicitly specify `localhost` to make sure this value will still be used, and to disable the deprecation message which will be shown otherwise. |
| **tmpfs**  list / elements=string | Mount a tmpfs directory. |
| **tty**  boolean | Allocate a pseudo-TTY.  If *container_default_behavior* is set to `compatibility`, this option has a default of `false`.  Choices:   - `false` - `true` |
| **ulimits**  list / elements=string | List of ulimit options. A ulimit is specified as `nofile:262144:262144`. |
| **use_ssh_client**  boolean  added in community.docker 1.5.0 | For SSH transports, use the `ssh` CLI tool instead of paramiko.  Requires Docker SDK for Python 4.4.0 or newer.  Choices:   - `false` ← (default) - `true` |
| **user**  string | Sets the username or UID used and optionally the groupname or GID for the specified command.  Can be of the forms `user`, `user:group`, `uid`, `uid:gid`, `user:gid` or `uid:group`. |
| **userns_mode**  string | Set the user namespace mode for the container. Currently, the only valid value are `host` and the empty string. |
| **uts**  string | Set the UTS namespace mode for the container. |
| **validate_certs**  aliases: tls_verify  boolean | Secure the connection to the API by using TLS and verifying the authenticity of the Docker host server.  If the value is not specified in the task, the value of environment variable `DOCKER_TLS_VERIFY` will be used instead. If the environment variable is not set, the default value will be used.  Choices:   - `false` ← (default) - `true` |
| **volume_driver**  string | The container volume driver. |
| **volumes**  list / elements=string | List of volumes to mount within the container.  Use docker CLI-style syntax: `/host:/container[:mode]`  Mount modes can be a comma-separated list of various modes such as `ro`, `rw`, `consistent`, `delegated`, `cached`, `rprivate`, `private`, `rshared`, `shared`, `rslave`, `slave`, and `nocopy`. Note that the docker daemon might not support all modes and combinations of such modes.  SELinux hosts can additionally use `z` or `Z` to use a shared or private label for the volume.  Note that Ansible 2.7 and earlier only supported one mode, which had to be one of `ro`, `rw`, `z`, and `Z`. |
| **volumes_from**  list / elements=string | List of container names or IDs to get volumes from. |
| **working_dir**  string | Path to the working directory. |

## [Notes](docker_container_module.md#id4)

> **Note:**
>
> - For most config changes, the container needs to be recreated. This means that the existing container has to be destroyed and a new one created. This can cause unexpected data loss and downtime. You can use the *comparisons* option to prevent this.
> - If the module needs to recreate the container, it will only use the options provided to the module to create the new container (except *image*). Therefore, always specify **all** options relevant to the container.
> - When *restart* is set to `true`, the module will only restart the container if no config changes are detected.
> - Connect to the Docker daemon by providing parameters with each task or by defining environment variables. You can define `DOCKER_HOST`, `DOCKER_TLS_HOSTNAME`, `DOCKER_API_VERSION`, `DOCKER_CERT_PATH`, `DOCKER_SSL_VERSION`, `DOCKER_TLS`, `DOCKER_TLS_VERIFY` and `DOCKER_TIMEOUT`. If you are using docker machine, run the script shipped with the product that sets up the environment. It will set these variables for you. See <https://docs.docker.com/machine/reference/env/> for more details.
> - When connecting to Docker daemon with TLS, you might need to install additional Python packages. For the Docker SDK for Python, version 2.4 or newer, this can be done by installing `docker[tls]` with [ansible.builtin.pip](../../ansible/builtin/pip_module.md#ansible-collections-ansible-builtin-pip-module).
> - Note that the Docker SDK for Python only allows to specify the path to the Docker configuration for very few functions. In general, it will use `$HOME/.docker/config.json` if the `DOCKER_CONFIG` environment variable is not specified, and use `$DOCKER_CONFIG/config.json` otherwise.
> - This module uses the [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/) to communicate with the Docker daemon.

## [Examples](docker_container_module.md#id5)

```yaml+jinja
- name: Create a data container
  community.docker.docker_container:
    name: mydata
    image: busybox
    volumes:
      - /data

- name: Re-create a redis container
  community.docker.docker_container:
    name: myredis
    image: redis
    command: redis-server --appendonly yes
    state: present
    recreate: true
    exposed_ports:
      - 6379
    volumes_from:
      - mydata

- name: Restart a container
  community.docker.docker_container:
    name: myapplication
    image: someuser/appimage
    state: started
    restart: true
    links:
     - "myredis:aliasedredis"
    devices:
     - "/dev/sda:/dev/xvda:rwm"
    ports:
     # Publish container port 9000 as host port 8080
     - "8080:9000"
     # Publish container UDP port 9001 as host port 8081 on interface 127.0.0.1
     - "127.0.0.1:8081:9001/udp"
     # Publish container port 9002 as a random host port
     - "9002"
     # Publish container port 9003 as a free host port in range 8000-8100
     # (the host port will be selected by the Docker daemon)
     - "8000-8100:9003"
     # Publish container ports 9010-9020 to host ports 7000-7010
     - "7000-7010:9010-9020"
    env:
        SECRET_KEY: "ssssh"
        # Values which might be parsed as numbers, booleans or other types by the YAML parser need to be quoted
        BOOLEAN_KEY: "yes"

- name: Container present
  community.docker.docker_container:
    name: mycontainer
    state: present
    image: ubuntu:14.04
    command: sleep infinity

- name: Stop a container
  community.docker.docker_container:
    name: mycontainer
    state: stopped

- name: Start 4 load-balanced containers
  community.docker.docker_container:
    name: "container{{ item }}"
    recreate: true
    image: someuser/anotherappimage
    command: sleep 1d
  with_sequence: count=4

- name: Remove container
  community.docker.docker_container:
    name: ohno
    state: absent

- name: Syslogging output
  community.docker.docker_container:
    name: myservice
    image: busybox
    log_driver: syslog
    log_options:
      syslog-address: tcp://my-syslog-server:514
      syslog-facility: daemon
      # NOTE: in Docker 1.13+ the "syslog-tag" option was renamed to "tag" for
      # older docker installs, use "syslog-tag" instead
      tag: myservice

- name: Create db container and connect to network
  community.docker.docker_container:
    name: db_test
    image: "postgres:latest"
    networks:
      - name: "{{ docker_network_name }}"

- name: Start container, connect to network and link
  community.docker.docker_container:
    name: sleeper
    image: ubuntu:14.04
    networks:
      - name: TestingNet
        ipv4_address: "172.16.1.100"
        aliases:
          - sleepyzz
        links:
          - db_test:db
      - name: TestingNet2

- name: Start a container with a command
  community.docker.docker_container:
    name: sleepy
    image: ubuntu:14.04
    command: ["sleep", "infinity"]

- name: Add container to networks
  community.docker.docker_container:
    name: sleepy
    networks:
      - name: TestingNet
        ipv4_address: 172.16.1.18
        links:
          - sleeper
      - name: TestingNet2
        ipv4_address: 172.16.10.20

- name: Update network with aliases
  community.docker.docker_container:
    name: sleepy
    networks:
      - name: TestingNet
        aliases:
          - sleepyz
          - zzzz

- name: Remove container from one network
  community.docker.docker_container:
    name: sleepy
    networks:
      - name: TestingNet2
    purge_networks: true

- name: Remove container from all networks
  community.docker.docker_container:
    name: sleepy
    purge_networks: true

- name: Start a container and use an env file
  community.docker.docker_container:
    name: agent
    image: jenkinsci/ssh-slave
    env_file: /var/tmp/jenkins/agent.env

- name: Create a container with limited capabilities
  community.docker.docker_container:
    name: sleepy
    image: ubuntu:16.04
    command: sleep infinity
    capabilities:
      - sys_time
    cap_drop:
      - all

- name: Finer container restart/update control
  community.docker.docker_container:
    name: test
    image: ubuntu:18.04
    env:
      arg1: "true"
      arg2: "whatever"
    volumes:
      - /tmp:/tmp
    comparisons:
      image: ignore   # do not restart containers with older versions of the image
      env: strict   # we want precisely this environment
      volumes: allow_more_present   # if there are more volumes, that's ok, as long as `/tmp:/tmp` is there

- name: Finer container restart/update control II
  community.docker.docker_container:
    name: test
    image: ubuntu:18.04
    env:
      arg1: "true"
      arg2: "whatever"
    comparisons:
      '*': ignore  # by default, ignore *all* options (including image)
      env: strict   # except for environment variables; there, we want to be strict

- name: Start container with healthstatus
  community.docker.docker_container:
    name: nginx-proxy
    image: nginx:1.13
    state: started
    healthcheck:
      # Check if nginx server is healthy by curl'ing the server.
      # If this fails or timeouts, the healthcheck fails.
      test: ["CMD", "curl", "--fail", "http://nginx.host.com"]
      interval: 1m30s
      timeout: 10s
      retries: 3
      start_period: 30s

- name: Remove healthcheck from container
  community.docker.docker_container:
    name: nginx-proxy
    image: nginx:1.13
    state: started
    healthcheck:
      # The "NONE" check needs to be specified
      test: ["NONE"]

- name: Start container with block device read limit
  community.docker.docker_container:
    name: test
    image: ubuntu:18.04
    state: started
    device_read_bps:
      # Limit read rate for /dev/sda to 20 mebibytes per second
      - path: /dev/sda
        rate: 20M
    device_read_iops:
      # Limit read rate for /dev/sdb to 300 IO per second
      - path: /dev/sdb
        rate: 300

- name: Start container with GPUs
  community.docker.docker_container:
    name: test
    image: ubuntu:18.04
    state: started
    device_requests:
      - # Add some specific devices to this container
        device_ids:
          - '0'
          - 'GPU-3a23c669-1f69-c64e-cf85-44e9b07e7a2a'
      - # Add nVidia GPUs to this container
        driver: nvidia
        count: -1  # this means we want all
        capabilities:
          # We have one OR condition: 'gpu' AND 'utility'
          - - gpu
            - utility
          # See https://github.com/NVIDIA/nvidia-container-runtime#supported-driver-capabilities
          # for a list of capabilities supported by the nvidia driver

- name: Start container with storage options
  community.docker.docker_container:
    name: test
    image: ubuntu:18.04
    state: started
    storage_opts:
      # Limit root filesystem to 12 MB - note that this requires special storage backends
      # (https://fabianlee.org/2020/01/15/docker-use-overlay2-with-an-xfs-backing-filesystem-to-limit-rootfs-size/)
      size: 12m
```

## [Return Values](docker_container_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **container**  dictionary | Facts representing the current state of the container. Matches the docker inspection output.  Empty if *state* is `absent`.  If *detach=false*, will include `Output` attribute containing any output from container run.  Returned: success; or when *state=started* and *detach=false*, and when waiting for the container result did not fail  Sample: `"{ \"AppArmorProfile\": \"\", \"Args\": [], \"Config\": { \"AttachStderr\": false, \"AttachStdin\": false, \"AttachStdout\": false, \"Cmd\": [ \"/usr/bin/supervisord\" ], \"Domainname\": \"\", \"Entrypoint\": null, \"Env\": [ \"PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\" ], \"ExposedPorts\": { \"443/tcp\": {}, \"80/tcp\": {} }, \"Hostname\": \"8e47bf643eb9\", \"Image\": \"lnmp_nginx:v1\", \"Labels\": {}, \"OnBuild\": null, \"OpenStdin\": false, \"StdinOnce\": false, \"Tty\": false, \"User\": \"\", \"Volumes\": { \"/tmp/lnmp/nginx-sites/logs/\": {} }, ... }"` |
| **status**  integer | In case a container is started without detaching, this contains the exit code of the process in the container.  Before community.docker 1.1.0, this was only returned when non-zero.  Returned: when *state=started* and *detach=false*, and when waiting for the container result did not fail  Sample: `0` |

### Authors

- Cove Schneider (@cove)
- Joshua Conner (@joshuaconner)
- Pavel Antonov (@softzilla)
- Thomas Steinbach (@ThomasSteinbach)
- Philippe Jandot (@zfil)
- Daan Oosterveld (@dusdanig)
- Chris Houseknecht (@chouseknecht)
- Kassian Sun (@kassiansun)
- Felix Fontein (@felixfontein)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.docker/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.docker)
[Submit a bug report](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-docker)
