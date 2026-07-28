---
collection: ansible
version: "8"
title: "containers.podman.podman_pod module – Manage Podman pods"
source_url: https://docs.ansible.com/projects/ansible/8/collections/containers/podman/podman_pod_module.html
fetched_at: 2026-07-28T02:03:13+00:00
---
# containers.podman.podman_pod module – Manage Podman pods

> **Note:**
>
> This module is part of the [containers.podman collection](https://galaxy.ansible.com/ui/repo/published/containers/podman/) (version 1.11.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install containers.podman`.
> You need further requirements to be able to use this module,
> see [Requirements](podman_pod_module.md#ansible-collections-containers-podman-podman-pod-module-requirements) for details.
>
> To use it in a playbook, specify: `containers.podman.podman_pod`.

New in containers.podman 1.0.0

- [Synopsis](podman_pod_module.md#synopsis)
- [Requirements](podman_pod_module.md#requirements)
- [Parameters](podman_pod_module.md#parameters)
- [Examples](podman_pod_module.md#examples)
- [Return Values](podman_pod_module.md#return-values)

## [Synopsis](podman_pod_module.md#id1)

- Manage podman pods.

## [Requirements](podman_pod_module.md#id2)

The below requirements are needed on the host that executes this module.

- podman

## [Parameters](podman_pod_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **add_host**  list / elements=string | Add a host to the /etc/hosts file shared between all containers in the pod. |
| **blkio_weight**  string | Block IO relative weight. The weight is a value between 10 and 1000.  This option is not supported on cgroups V1 rootless systems. |
| **blkio_weight_device**  list / elements=string | Block IO relative device weight. |
| **cgroup_parent**  string | Path to cgroups under which the cgroup for the pod will be created. If the path is not absolute, he path is considered to be relative to the cgroups path of the init process. Cgroups will be created if they do not already exist. |
| **cpu_shares**  string | CPU shares (relative weight). |
| **cpus**  string | Set the total number of CPUs delegated to the pod. Default is 0.000 which indicates that there is no limit on computation power. |
| **cpuset_cpus**  string | Limit the CPUs to support execution. First CPU is numbered 0. Unlike `cpus` this is of type string and parsed as a list of numbers. Format is 0-3,0,1 |
| **cpuset_mems**  string | Memory nodes in which to allow execution (0-3, 0,1). Only effective on NUMA systems. |
| **debug**  boolean | Return additional information which can be helpful for investigations.  **Choices:**   - `false` ← (default) - `true` |
| **device**  list / elements=string | Add a host device to the pod. Optional permissions parameter can be used to specify device permissions. It is a combination of r for read, w for write, and m for mknod(2) |
| **device_read_bps**  list / elements=string | Limit read rate (bytes per second) from a device (e.g. device-read-bps=/dev/sda:1mb) |
| **device_write_bps**  list / elements=string | Limit write rate (in bytes per second) to a device. |
| **dns**  list / elements=string | Set custom DNS servers in the /etc/resolv.conf file that will be shared between all containers in the pod. A special option, “none” is allowed which disables creation of /etc/resolv.conf for the pod. |
| **dns_opt**  list / elements=string | Set custom DNS options in the /etc/resolv.conf file that will be shared between all containers in the pod. |
| **dns_search**  list / elements=string | Set custom DNS search domains in the /etc/resolv.conf file that will be shared between all containers in the pod. |
| **executable**  string | Path to `podman` executable if it is not in the `$PATH` on the machine running `podman`  **Default:** `"podman"` |
| **generate_systemd**  dictionary | Generate systemd unit file for container.  **Default:** `{}` |
| **after**  list / elements=string | Add the systemd unit after (After=) option, that ordering dependencies between the list of dependencies and this service. |
| **container_prefix**  string | Set the systemd unit name prefix for containers. The default is “container”. |
| **names**  boolean | Use names of the containers for the start, stop, and description in the unit file. Default is true.  **Choices:**   - `false` - `true` ← (default) |
| **new**  boolean | Create containers and pods when the unit is started instead of expecting them to exist. The default is “false”. Refer to podman-generate-systemd(1) for more information.  **Choices:**   - `false` ← (default) - `true` |
| **no_header**  boolean | Do not generate the header including meta data such as the Podman version and the timestamp. From podman version 3.1.0.  **Choices:**   - `false` ← (default) - `true` |
| **path**  string | Specify a path to the directory where unit files will be generated. Required for this option. If it doesn’t exist, the directory will be created. |
| **pod_prefix**  string | Set the systemd unit name prefix for pods. The default is “pod”. |
| **requires**  list / elements=string | Set the systemd unit requires (Requires=) option. Similar to wants, but declares a stronger requirement dependency. |
| **restart_policy**  string | Specify a restart policy for the service. The restart-policy must be one of “no”, “on-success”, “on-failure”, “on-abnormal”, “on-watchdog”, “on-abort”, or “always”. The default policy is “on-failure”.  **Choices:**   - `"no"` - `"on-success"` - `"on-failure"` - `"on-abnormal"` - `"on-watchdog"` - `"on-abort"` - `"always"` |
| **restart_sec**  integer | Set the systemd service restartsec value. |
| **separator**  string | Set the systemd unit name separator between the name/id of a container/pod and the prefix. The default is “-” (dash). |
| **start_timeout**  integer | Override the default start timeout for the container with the given value. |
| **stop_timeout**  integer | Override the default stop timeout for the container with the given value. |
| **time**  integer | Override the default stop timeout for the container with the given value. |
| **wants**  list / elements=string | Add the systemd unit wants (Wants=) option, that this service is (weak) dependent on. |
| **gidmap**  list / elements=string | GID map for the user namespace. Using this flag will run the container with user namespace enabled. It conflicts with the `userns` and `subgidname` flags. |
| **hostname**  string | Set a hostname to the pod |
| **infra**  boolean | Create an infra container and associate it with the pod. An infra container is a lightweight container used to coordinate the shared kernel namespace of a pod. Default is true.  **Choices:**   - `false` - `true` |
| **infra_command**  string | The command that will be run to start the infra container. Default is “/pause”. |
| **infra_conmon_pidfile**  string | Write the pid of the infra container’s conmon process to a file. As conmon runs in a separate process than Podman, this is necessary when using systemd to manage Podman containers and pods. |
| **infra_image**  string | The image that will be created for the infra container. Default is “k8s.gcr.io/pause:3.1”. |
| **infra_name**  string | The name that will be used for the pod’s infra container. |
| **ip**  string | Set a static IP for the pod’s shared network. |
| **label**  dictionary | Add metadata to a pod, pass dictionary of label keys and values. |
| **label_file**  string | Read in a line delimited file of labels. |
| **mac_address**  string | Set a static MAC address for the pod’s shared network. |
| **memory**  string | Set memory limit.  A unit can be b (bytes), k (kibibytes), m (mebibytes), or g (gibibytes). |
| **memory_swap**  string | Set limit value equal to memory plus swap.  A unit can be b (bytes), k (kibibytes), m (mebibytes), or g (gibibytes). |
| **name**  string / required | Assign a name to the pod. |
| **network**  list / elements=string | Set network mode for the pod. Supported values are bridge (the default), host (do not create a network namespace, all containers in the pod will use the host’s network), or a list of names of CNI networks to join. |
| **network_alias**  aliases: network_aliases  list / elements=string | Add a network-scoped alias for the pod, setting the alias for all networks that the pod joins. To set a name only for a specific network, use the alias option as described under the -`network` option. Network aliases work only with the bridge networking mode. This option can be specified multiple times. |
| **no_hosts**  boolean | Disable creation of /etc/hosts for the pod.  **Choices:**   - `false` - `true` |
| **pid**  string | Set the PID mode for the pod. The default is to create a private PID namespace for the pod. Requires the PID namespace to be shared via `share` option. |
| **pod_id_file**  string | Write the pod ID to the file. |
| **publish**  aliases: ports  list / elements=string | Publish a port or range of ports from the pod to the host. |
| **recreate**  boolean | Use with present and started states to force the re-creation of an existing pod.  **Choices:**   - `false` ← (default) - `true` |
| **share**  string | A comma delimited list of kernel namespaces to share. If none or “” is specified, no namespaces will be shared. The namespaces to choose from are ipc, net, pid, user, uts. |
| **state**  string | This variable is set for state  **Choices:**   - `"created"` ← (default) - `"killed"` - `"restarted"` - `"absent"` - `"started"` - `"stopped"` - `"paused"` - `"unpaused"` |
| **subgidname**  string | Name for GID map from the /etc/subgid file. Using this flag will run the container with user namespace enabled. This flag conflicts with `userns` and `gidmap`. |
| **subuidname**  string | Name for UID map from the /etc/subuid file. Using this flag will run the container with user namespace enabled. This flag conflicts with `userns` and `uidmap`. |
| **uidmap**  list / elements=string | Run the container in a new user namespace using the supplied mapping. This option conflicts with the `userns` and `subuidname` options. This option provides a way to map host UIDs to container UIDs. It can be passed several times to map different ranges. |
| **userns**  string | Set the user namespace mode for all the containers in a pod. It defaults to the PODMAN_USERNS environment variable. An empty value (“”) means user namespaces are disabled. |
| **volume**  aliases: volumes  list / elements=string | Create a bind mount. |

## [Examples](podman_pod_module.md#id4)

```yaml+jinja
# What modules does for example
- podman_pod:
    name: pod1
    state: started
    ports:
      - "4444:5555"

# Connect random port from localhost to port 80 on pod2
- name: Connect random port from localhost to port 80 on pod2
  containers.podman.podman_pod:
    name: pod2
    state: started
    publish: "127.0.0.1::80"
```

## [Return Values](podman_pod_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **pod**  dictionary | Pod inspection results for the given pod built.  **Returned:** always  **Sample:** `{"Config": {"cgroupParent": "/libpod_parent", "created": "2020-06-14T15:16:12.230818767+03:00", "hostname": "newpod", "id": "a5a5c6cdf8c72272fc5c33f787e8d7501e2fa0c1e92b2b602860defdafeeec58", "infraConfig": {"infraPortBindings": null, "makeInfraContainer": true}, "labels": {}, "lockID": 515, "name": "newpod", "sharesCgroup": true, "sharesIpc": true, "sharesNet": true, "sharesUts": true}, "Containers": [{"id": "dc70a947c7ae15198ec38b3c817587584085dee3919cbeb9969e3ab77ba10fd2", "state": "configured"}], "State": {"cgroupPath": "/libpod_parent/a5a5c6cdf8c72272fc5c33f787e8d7501e2fa0c1e92b2b602860defdafeeec58", "infraContainerID": "dc70a947c7ae15198ec38b3c817587584085dee3919cbeb9969e3ab77ba10fd2", "status": "Created"}}` |

### Authors

- Sagi Shnaidman (@sshnaidm)

### Collection links

- [Issue Tracker](https://github.com/containers/ansible-podman-collections/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/containers/ansible-podman-collections.git)
