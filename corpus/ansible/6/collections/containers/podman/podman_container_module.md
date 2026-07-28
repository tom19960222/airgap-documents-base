---
collection: ansible
version: "6"
title: "containers.podman.podman_container module – Manage podman containers"
source_url: https://docs.ansible.com/projects/ansible/6/collections/containers/podman/podman_container_module.html
fetched_at: 2026-07-27T17:24:27+00:00
---
# containers.podman.podman_container module – Manage podman containers

> **Note:**
>
> This module is part of the [containers.podman collection](https://galaxy.ansible.com/containers/podman) (version 1.10.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install containers.podman`.
> You need further requirements to be able to use this module,
> see [Requirements](podman_container_module.md#ansible-collections-containers-podman-podman-container-module-requirements) for details.
>
> To use it in a playbook, specify: `containers.podman.podman_container`.

New in containers.podman 1.0.0

- [Synopsis](podman_container_module.md#synopsis)
- [Requirements](podman_container_module.md#requirements)
- [Parameters](podman_container_module.md#parameters)
- [Examples](podman_container_module.md#examples)
- [Return Values](podman_container_module.md#return-values)

## [Synopsis](podman_container_module.md#id1)

- Start, stop, restart and manage Podman containers

## [Requirements](podman_container_module.md#id2)

The below requirements are needed on the host that executes this module.

- podman

## [Parameters](podman_container_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **annotation**  dictionary | Add an annotation to the container. The format is key value, multiple times. |
| **authfile**  path | Path of the authentication file. Default is ``${XDG_RUNTIME_DIR}/containers/auth.json`` (Not available for remote commands) You can also override the default path of the authentication file by setting the ``REGISTRY_AUTH_FILE`` environment variable. ``export REGISTRY_AUTH_FILE=path`` |
| **blkio_weight**  integer | Block IO weight (relative weight) accepts a weight value between 10 and 1000 |
| **blkio_weight_device**  dictionary | Block IO weight (relative device weight, format DEVICE_NAME[:]WEIGHT). |
| **cap_add**  aliases: capabilities  list / elements=string | List of capabilities to add to the container. |
| **cap_drop**  list / elements=string | List of capabilities to drop from the container. |
| **cgroup_parent**  path | Path to cgroups under which the cgroup for the container will be created. If the path is not absolute, the path is considered to be relative to the cgroups path of the init process. Cgroups will be created if they do not already exist. |
| **cgroupns**  string | Path to cgroups under which the cgroup for the container will be created. |
| **cgroups**  string | Determines whether the container will create CGroups. Valid values are enabled and disabled, which the default being enabled. The disabled option will force the container to not create CGroups, and thus conflicts with CGroup options cgroupns and cgroup-parent. |
| **cidfile**  path | Write the container ID to the file |
| **cmd_args**  list / elements=string | Any additional command options you want to pass to podman command, cmd_args - [’–other-param’, ‘value’] Be aware module doesn’t support idempotency if this is set. |
| **command**  any | Override command of container. Can be a string or a list. |
| **conmon_pidfile**  path | Write the pid of the conmon process to a file. conmon runs in a separate process than Podman, so this is necessary when using systemd to restart Podman containers. |
| **cpu_period**  integer | Limit the CPU real-time period in microseconds |
| **cpu_rt_period**  integer | Limit the CPU real-time period in microseconds. Limit the container’s Real Time CPU usage. This flag tell the kernel to restrict the container’s Real Time CPU usage to the period you specify. |
| **cpu_rt_runtime**  integer | Limit the CPU real-time runtime in microseconds. This flag tells the kernel to limit the amount of time in a given CPU period Real Time tasks may consume. |
| **cpu_shares**  integer | CPU shares (relative weight) |
| **cpus**  string | Number of CPUs. The default is 0.0 which means no limit. |
| **cpuset_cpus**  string | CPUs in which to allow execution (0-3, 0,1) |
| **cpuset_mems**  string | Memory nodes (MEMs) in which to allow execution (0-3, 0,1). Only effective on NUMA systems. |
| **debug**  boolean | Return additional information which can be helpful for investigations.  Choices:   - `false` ← (default) - `true` |
| **detach**  boolean | Run container in detach mode  Choices:   - `false` - `true` ← (default) |
| **detach_keys**  string | Override the key sequence for detaching a container. Format is a single character or ctrl-value |
| **device**  list / elements=string | Add a host device to the container. The format is <device-on-host>[:<device-on-container>][:<permissions>] (e.g. device /dev/sdc:/dev/xvdc:rwm) |
| **device_read_bps**  list / elements=string | Limit read rate (bytes per second) from a device (e.g. device-read-bps /dev/sda:1mb) |
| **device_read_iops**  list / elements=string | Limit read rate (IO per second) from a device (e.g. device-read-iops /dev/sda:1000) |
| **device_write_bps**  list / elements=string | Limit write rate (bytes per second) to a device (e.g. device-write-bps /dev/sda:1mb) |
| **device_write_iops**  list / elements=string | Limit write rate (IO per second) to a device (e.g. device-write-iops /dev/sda:1000) |
| **dns**  aliases: dns_servers  list / elements=string | Set custom DNS servers |
| **dns_option**  aliases: dns_opts  string | Set custom DNS options |
| **dns_search**  aliases: dns_search_domains  string | Set custom DNS search domains (Use dns_search with ‘’ if you don’t wish to set the search domain) |
| **entrypoint**  string | Overwrite the default ENTRYPOINT of the image |
| **env**  dictionary | Set environment variables. This option allows you to specify arbitrary environment variables that are available for the process that will be launched inside of the container. |
| **env_file**  path | Read in a line delimited file of environment variables. Doesn’t support idempotency. If users changes the file with environment variables it’s on them to recreate the container. |
| **env_host**  boolean | Use all current host environment variables in container. Defaults to false.  Choices:   - `false` - `true` |
| **etc_hosts**  aliases: add_hosts  dictionary | Dict of host-to-IP mappings, where each host name is a key in the dictionary. Each host name will be added to the container’s ``/etc/hosts`` file. |
| **executable**  string | Path to `podman` executable if it is not in the `$PATH` on the machine running `podman`  Default: `"podman"` |
| **expose**  aliases: exposed, exposed_ports  list / elements=string | Expose a port, or a range of ports (e.g. expose “3300-3310”) to set up port redirection on the host system. |
| **force_restart**  aliases: restart  boolean | Force restart of container.  Choices:   - `false` ← (default) - `true` |
| **generate_systemd**  dictionary | Generate systemd unit file for container.  Default: `{}` |
| **after**  list / elements=string | Add the systemd unit after (After=) option, that ordering dependencies between the list of dependencies and this service. |
| **container_prefix**  string | Set the systemd unit name prefix for containers. The default is “container”. |
| **names**  boolean | Use names of the containers for the start, stop, and description in the unit file. Default is true.  Choices:   - `false` - `true` ← (default) |
| **new**  boolean | Create containers and pods when the unit is started instead of expecting them to exist. The default is “false”. Refer to podman-generate-systemd(1) for more information.  Choices:   - `false` ← (default) - `true` |
| **no_header**  boolean | Do not generate the header including meta data such as the Podman version and the timestamp. From podman version 3.1.0.  Choices:   - `false` ← (default) - `true` |
| **path**  string | Specify a path to the directory where unit files will be generated. Required for this option. If it doesn’t exist, the directory will be created. |
| **pod_prefix**  string | Set the systemd unit name prefix for pods. The default is “pod”. |
| **requires**  list / elements=string | Set the systemd unit requires (Requires=) option. Similar to wants, but declares a stronger requirement dependency. |
| **restart_policy**  string | Specify a restart policy for the service. The restart-policy must be one of “no”, “on-success”, “on-failure”, “on-abnormal”, “on-watchdog”, “on-abort”, or “always”. The default policy is “on-failure”.  Choices:   - `"no"` - `"on-success"` - `"on-failure"` - `"on-abnormal"` - `"on-watchdog"` - `"on-abort"` - `"always"` |
| **separator**  string | Set the systemd unit name separator between the name/id of a container/pod and the prefix. The default is “-” (dash). |
| **time**  integer | Override the default stop timeout for the container with the given value. |
| **wants**  list / elements=string | Add the systemd unit wants (Wants=) option, that this service is (weak) dependent on. |
| **gidmap**  list / elements=string | Run the container in a new user namespace using the supplied mapping. |
| **group_add**  aliases: groups  list / elements=string | Add additional groups to run as |
| **healthcheck**  string | Set or alter a healthcheck command for a container. |
| **healthcheck_interval**  string | Set an interval for the healthchecks (a value of disable results in no automatic timer setup) (default “30s”) |
| **healthcheck_retries**  integer | The number of retries allowed before a healthcheck is considered to be unhealthy. The default value is 3. |
| **healthcheck_start_period**  string | The initialization time needed for a container to bootstrap. The value can be expressed in time format like 2m3s. The default value is 0s |
| **healthcheck_timeout**  string | The maximum time allowed to complete the healthcheck before an interval is considered failed. Like start-period, the value can be expressed in a time format such as 1m22s. The default value is 30s |
| **hostname**  string | Container host name. Sets the container host name that is available inside the container. |
| **http_proxy**  boolean | By default proxy environment variables are passed into the container if set for the podman process. This can be disabled by setting the http_proxy option to false. The environment variables passed in include http_proxy, https_proxy, ftp_proxy, no_proxy, and also the upper case versions of those. Defaults to true  Choices:   - `false` - `true` |
| **image**  string | Repository path (or image name) and tag used to create the container. If an image is not found, the image will be pulled from the registry. If no tag is included, `latest` will be used.  Can also be an image ID. If this is the case, the image is assumed to be available locally. |
| **image_strict**  boolean | Whether to compare images in idempotency by taking into account a full name with registry and namespaces.  Choices:   - `false` ← (default) - `true` |
| **image_volume**  string | Tells podman how to handle the builtin image volumes. The options are bind, tmpfs, or ignore (default bind)  Choices:   - `"bind"` - `"tmpfs"` - `"ignore"` |
| **init**  boolean | Run an init inside the container that forwards signals and reaps processes. The default is false.  Choices:   - `false` - `true` |
| **init_path**  string | Path to the container-init binary. |
| **interactive**  boolean | Keep STDIN open even if not attached. The default is false. When set to true, keep stdin open even if not attached. The default is false.  Choices:   - `false` - `true` |
| **ip**  string | Specify a static IP address for the container, for example ‘10.88.64.128’. Can only be used if no additional CNI networks to join were specified via ‘network:’, and if the container is not joining another container’s network namespace via ‘network container:<name|id>’. The address must be within the default CNI network’s pool (default 10.88.0.0/16). |
| **ipc**  aliases: ipc_mode  string | Default is to create a private IPC namespace (POSIX SysV IPC) for the container |
| **kernel_memory**  string | Kernel memory limit (format <number>[<unit>], where unit = b, k, m or g) Note - idempotency is supported for integers only. |
| **label**  aliases: labels  dictionary | Add metadata to a container, pass dictionary of label names and values |
| **label_file**  string | Read in a line delimited file of labels |
| **log_driver**  string | Logging driver. Used to set the log driver for the container. For example log_driver “k8s-file”.  Choices:   - `"k8s-file"` - `"journald"` - `"json-file"` |
| **log_level**  string | Logging level for Podman. Log messages above specified level (“debug”|”info”|”warn”|”error”|”fatal”|”panic”) (default “error”)  Choices:   - `"debug"` - `"info"` - `"warn"` - `"error"` - `"fatal"` - `"panic"` |
| **log_opt**  aliases: log_options  dictionary | Logging driver specific options. Used to set the path to the container log file. |
| **max_size**  string | Specify a max size of the log file (e.g 10mb). |
| **path**  string | Specify a path to the log file (e.g. /var/log/container/mycontainer.json). |
| **tag**  string | Specify a custom log tag for the container. |
| **mac_address**  string | Specify a MAC address for the container, for example ‘92:d0:c6:0a:29:33’. Don’t forget that it must be unique within one Ethernet network. |
| **memory**  string | Memory limit (format 10k, where unit = b, k, m or g) Note - idempotency is supported for integers only. |
| **memory_reservation**  string | Memory soft limit (format 100m, where unit = b, k, m or g) Note - idempotency is supported for integers only. |
| **memory_swap**  string | A limit value equal to memory plus swap. Must be used with the -m (–memory) flag. The swap LIMIT should always be larger than -m (–memory) value. By default, the swap LIMIT will be set to double the value of –memory Note - idempotency is supported for integers only. |
| **memory_swappiness**  integer | Tune a container’s memory swappiness behavior. Accepts an integer between 0 and 100. |
| **mount**  aliases: mounts  list / elements=string | Attach a filesystem mount to the container. bind or tmpfs For example mount “type=bind,source=/path/on/host,destination=/path/in/container” |
| **name**  string / required | Name of the container |
| **network**  aliases: net, network_mode  list / elements=string | Set the Network mode for the container \* bridge create a network stack on the default bridge \* none no networking \* container:<name|id> reuse another container’s network stack \* host use the podman host network stack. \* <network-name>|<network-id> connect to a user-defined network \* ns:<path> path to a network namespace to join \* slirp4netns use slirp4netns to create a user network stack. This is the default for rootless containers |
| **network_aliases**  list / elements=string | Add network-scoped alias for the container. A container will only have access to aliases on the first network that it joins. This is a limitation that will be removed in a later release. |
| **no_hosts**  boolean | Do not create /etc/hosts for the container Default is false.  Choices:   - `false` - `true` |
| **oom_kill_disable**  boolean | Whether to disable OOM Killer for the container or not. Default is false.  Choices:   - `false` - `true` |
| **oom_score_adj**  integer | Tune the host’s OOM preferences for containers (accepts -1000 to 1000) |
| **pid**  aliases: pid_mode  string | Set the PID mode for the container |
| **pids_limit**  string | Tune the container’s PIDs limit. Set -1 to have unlimited PIDs for the container. |
| **pod**  string | Run container in an existing pod. If you want podman to make the pod for you, prefix the pod name with “new:” |
| **privileged**  boolean | Give extended privileges to this container. The default is false.  Choices:   - `false` - `true` |
| **publish**  aliases: ports, published, published_ports  list / elements=string | Publish a container’s port, or range of ports, to the host. Format - ip:hostPort:containerPort | ip::containerPort | hostPort:containerPort | containerPort In case of only containerPort is set, the hostPort will chosen randomly by Podman. |
| **publish_all**  boolean | Publish all exposed ports to random ports on the host interfaces. The default is false.  Choices:   - `false` - `true` |
| **read_only**  boolean | Mount the container’s root filesystem as read only. Default is false  Choices:   - `false` - `true` |
| **read_only_tmpfs**  boolean | If container is running in –read-only mode, then mount a read-write tmpfs on /run, /tmp, and /var/tmp. The default is true  Choices:   - `false` - `true` |
| **recreate**  boolean | Use with present and started states to force the re-creation of an existing container.  Choices:   - `false` ← (default) - `true` |
| **requires**  list / elements=string | Specify one or more requirements. A requirement is a dependency container that will be started before this container. Containers can be specified by name or ID. |
| **restart_policy**  string | Restart policy to follow when containers exit. Restart policy will not take effect if a container is stopped via the podman kill or podman stop commands. Valid values are \* no - Do not restart containers on exit \* on-failure[:max_retries] - Restart containers when they exit with a non-0 exit code, retrying indefinitely or until the optional max_retries count is hit \* always - Restart containers when they exit, regardless of status, retrying indefinitely |
| **rm**  aliases: remove, auto_remove  boolean | Automatically remove the container when it exits. The default is false.  Choices:   - `false` - `true` |
| **rootfs**  boolean | If true, the first argument refers to an exploded container on the file system. The default is false.  Choices:   - `false` - `true` |
| **sdnotify**  string | Determines how to use the NOTIFY_SOCKET, as passed with systemd and Type=notify. Can be container, conmon, ignore. |
| **secrets**  list / elements=string | Add the named secrets into the container. The format is `secret[,opt=opt...]`, see [documentation](https://docs.podman.io/en/latest/markdown/podman-run.1.html#secret-secret-opt-opt) for more details. |
| **security_opt**  list / elements=string | Security Options. For example security_opt “seccomp=unconfined” |
| **shm_size**  string | Size of /dev/shm. The format is <number><unit>. number must be greater than 0. Unit is optional and can be b (bytes), k (kilobytes), m(megabytes), or g (gigabytes). If you omit the unit, the system uses bytes. If you omit the size entirely, the system uses 64m |
| **sig_proxy**  boolean | Proxy signals sent to the podman run command to the container process. SIGCHLD, SIGSTOP, and SIGKILL are not proxied. The default is true.  Choices:   - `false` - `true` |
| **state**  string | *absent* - A container matching the specified name will be stopped and removed.  *present* - Asserts the existence of a container matching the name and any provided configuration parameters. If no container matches the name, a container will be created. If a container matches the name but the provided configuration does not match, the container will be updated, if it can be. If it cannot be updated, it will be removed and re-created with the requested config. Image version will be taken into account when comparing configuration. Use the recreate option to force the re-creation of the matching container.  *started* - Asserts there is a running container matching the name and any provided configuration. If no container matches the name, a container will be created and started. Use recreate to always re-create a matching container, even if it is running. Use force_restart to force a matching container to be stopped and restarted.  *stopped* - Asserts that the container is first *present*, and then if the container is running moves it to a stopped state.  *created* - Asserts that the container exists with given configuration. If container doesn’t exist, the module creates it and leaves it in ‘created’ state. If configuration doesn’t match or ‘recreate’ option is set, the container will be recreated  Choices:   - `"absent"` - `"present"` - `"stopped"` - `"started"` ← (default) - `"created"` |
| **stop_signal**  integer | Signal to stop a container. Default is SIGTERM. |
| **stop_timeout**  integer | Timeout (in seconds) to stop a container. Default is 10. |
| **subgidname**  string | Run the container in a new user namespace using the map with ‘name’ in the /etc/subgid file. |
| **subuidname**  string | Run the container in a new user namespace using the map with ‘name’ in the /etc/subuid file. |
| **sysctl**  dictionary | Configure namespaced kernel parameters at runtime |
| **systemd**  string | Run container in systemd mode. The default is true. |
| **timezone**  string | Set timezone in container. This flag takes area-based timezones, GMT time, as well as local, which sets the timezone in the container to match the host machine. See /usr/share/zoneinfo/ for valid timezones. Remote connections use local containers.conf for defaults. |
| **tmpfs**  dictionary | Create a tmpfs mount. For example tmpfs “/tmp” “rw,size=787448k,mode=1777” |
| **tty**  boolean | Allocate a pseudo-TTY. The default is false.  Choices:   - `false` - `true` |
| **uidmap**  list / elements=string | Run the container in a new user namespace using the supplied mapping. |
| **ulimit**  aliases: ulimits  list / elements=string | Ulimit options |
| **user**  string | Sets the username or UID used and optionally the groupname or GID for the specified command. |
| **userns**  aliases: userns_mode  string | Set the user namespace mode for the container. It defaults to the PODMAN_USERNS environment variable. An empty value means user namespaces are disabled. |
| **uts**  string | Set the UTS mode for the container |
| **volume**  aliases: volumes  list / elements=string | Create a bind mount. If you specify, volume /HOST-DIR:/CONTAINER-DIR, podman bind mounts /HOST-DIR in the host to /CONTAINER-DIR in the podman container. |
| **volumes_from**  list / elements=string | Mount volumes from the specified container(s). |
| **workdir**  aliases: working_dir  string | Working directory inside the container. The default working directory for running binaries within a container is the root directory (/). |

## [Examples](podman_container_module.md#id4)

```yaml+jinja
- name: Run container
  containers.podman.podman_container:
    name: container
    image: quay.io/bitnami/wildfly
    state: started

- name: Create a data container
  containers.podman.podman_container:
    name: mydata
    image: busybox
    volume:
      - /tmp/data

- name: Re-create a redis container with systemd service file generated in /tmp/
  containers.podman.podman_container:
    name: myredis
    image: redis
    command: redis-server --appendonly yes
    state: present
    recreate: yes
    expose:
      - 6379
    volumes_from:
      - mydata
    generate_systemd:
      path: /tmp/
      restart_policy: always
      time: 120
      names: true
      container_prefix: ainer

- name: Restart a container
  containers.podman.podman_container:
    name: myapplication
    image: redis
    state: started
    restart: yes
    etc_hosts:
        other: "127.0.0.1"
    restart_policy: "no"
    device: "/dev/sda:/dev/xvda:rwm"
    ports:
        - "8080:9000"
        - "127.0.0.1:8081:9001/udp"
    env:
        SECRET_KEY: "ssssh"
        BOOLEAN_KEY: "yes"

- name: Container present
  containers.podman.podman_container:
    name: mycontainer
    state: present
    image: ubuntu:14.04
    command: "sleep 1d"

- name: Stop a container
  containers.podman.podman_container:
    name: mycontainer
    state: stopped

- name: Start 4 load-balanced containers
  containers.podman.podman_container:
    name: "container{{ item }}"
    recreate: yes
    image: someuser/anotherappimage
    command: sleep 1d
  with_sequence: count=4

- name: remove container
  containers.podman.podman_container:
    name: ohno
    state: absent

- name: Writing output
  containers.podman.podman_container:
    name: myservice
    image: busybox
    log_options: path=/var/log/container/mycontainer.json
    log_driver: k8s-file
```

## [Return Values](podman_container_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **container**  dictionary | Facts representing the current state of the container. Matches the podman inspection output.  Note that facts are part of the registered vars since Ansible 2.8. For compatibility reasons, the facts are also accessible directly as `podman_container`. Note that the returned fact will be removed in Ansible 2.12.  Empty if `state` is *absent*.  Returned: always  Sample: `"{ \"AppArmorProfile\": \"\", \"Args\": [ \"sh\" ], \"BoundingCaps\": [ \"CAP_CHOWN\", ... ], \"Config\": { \"Annotations\": { \"io.kubernetes.cri-o.ContainerType\": \"sandbox\", \"io.kubernetes.cri-o.TTY\": \"false\" }, \"AttachStderr\": false, \"AttachStdin\": false, \"AttachStdout\": false, \"Cmd\": [ \"sh\" ], \"Domainname\": \"\", \"Entrypoint\": \"\", \"Env\": [ \"PATH=/usr/sbin:/usr/bin:/sbin:/bin\", \"TERM=xterm\", \"HOSTNAME=\", \"container=podman\" ], \"Hostname\": \"\", \"Image\": \"docker.io/library/busybox:latest\", \"Labels\": null, \"OpenStdin\": false, \"StdinOnce\": false, \"StopSignal\": 15, \"Tty\": false, \"User\": { \"gid\": 0, \"uid\": 0 }, \"Volumes\": null, \"WorkingDir\": \"/\" }, \"ConmonPidFile\": \"...\", \"Created\": \"2019-06-17T19:13:09.873858307+03:00\", \"Dependencies\": [], \"Driver\": \"overlay\", \"EffectiveCaps\": [ \"CAP_CHOWN\", ... ], \"ExecIDs\": [], \"ExitCommand\": [ \"/usr/bin/podman\", \"--root\", ... ], \"GraphDriver\": { ... }, \"HostConfig\": { ... }, \"HostnamePath\": \"...\", \"HostsPath\": \"...\", \"ID\": \"...\", \"Image\": \"...\", \"ImageName\": \"docker.io/library/busybox:latest\", \"IsInfra\": false, \"LogPath\": \"/tmp/container/mycontainer.json\", \"MountLabel\": \"system_u:object_r:container_file_t:s0:c282,c782\", \"Mounts\": [ ... ], \"Name\": \"myservice\", \"Namespace\": \"\", \"NetworkSettings\": { \"Bridge\": \"\", ... }, \"Path\": \"sh\", \"ProcessLabel\": \"system_u:system_r:container_t:s0:c282,c782\", \"ResolvConfPath\": \"...\", \"RestartCount\": 0, \"Rootfs\": \"\", \"State\": { \"Dead\": false, \"Error\": \"\", \"ExitCode\": 0, \"FinishedAt\": \"2019-06-17T19:13:10.157518963+03:00\", \"Healthcheck\": { \"FailingStreak\": 0, \"Log\": null, \"Status\": \"\" }, \"OOMKilled\": false, \"OciVersion\": \"1.0.1-dev\", \"Paused\": false, \"Pid\": 4083, \"Restarting\": false, \"Running\": false, \"StartedAt\": \"2019-06-17T19:13:10.152479729+03:00\", \"Status\": \"exited\" }, \"StaticDir\": \"...\" ... }"` |

### Authors

- Sagi Shnaidman (@sshnaidm)

### Collection links

[Issue Tracker](https://github.com/containers/ansible-podman-collections/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/containers/ansible-podman-collections.git)
