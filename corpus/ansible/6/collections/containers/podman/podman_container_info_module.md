---
collection: ansible
version: "6"
title: "containers.podman.podman_container_info module – Gather facts about containers using podman"
source_url: https://docs.ansible.com/projects/ansible/6/collections/containers/podman/podman_container_info_module.html
fetched_at: 2026-07-27T17:24:28+00:00
---
# containers.podman.podman_container_info module – Gather facts about containers using podman

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
> see [Requirements](podman_container_info_module.md#ansible-collections-containers-podman-podman-container-info-module-requirements) for details.
>
> To use it in a playbook, specify: `containers.podman.podman_container_info`.

- [Synopsis](podman_container_info_module.md#synopsis)
- [Requirements](podman_container_info_module.md#requirements)
- [Parameters](podman_container_info_module.md#parameters)
- [Notes](podman_container_info_module.md#notes)
- [Examples](podman_container_info_module.md#examples)
- [Return Values](podman_container_info_module.md#return-values)

## [Synopsis](podman_container_info_module.md#id1)

- Gather facts about containers using `podman`

## [Requirements](podman_container_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- Podman installed on host

## [Parameters](podman_container_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **executable**  string | Path to `podman` executable if it is not in the `$PATH` on the machine running `podman`  Default: `"podman"` |
| **name**  list / elements=string | List of container names to gather facts about. If no name is given return facts about all containers. |

## [Notes](podman_container_info_module.md#id4)

> **Note:**
>
> - Podman may require elevated privileges in order to run properly.

## [Examples](podman_container_info_module.md#id5)

```yaml+jinja
- name: Gather facts for all containers
  containers.podman.podman_container_info:

- name: Gather facts on a specific container
  containers.podman.podman_container_info:
    name: web1

- name: Gather facts on several containers
  containers.podman.podman_container_info:
    name:
      - redis
      - web1
```

## [Return Values](podman_container_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **containers**  list / elements=dictionary | Facts from all or specificed containers  Returned: always  Sample: `[{"AppArmorProfile": "", "Args": ["--single-child", "--", "kolla_start"], "BoundingCaps": ["CAP_CHOWN", "CAP_DAC_OVERRIDE", "CAP_FSETID", "CAP_FOWNER", "CAP_MKNOD", "CAP_NET_RAW", "CAP_SETGID", "CAP_SETUID", "CAP_SETFCAP", "CAP_SETPCAP", "CAP_NET_BIND_SERVICE", "CAP_SYS_CHROOT", "CAP_KILL", "CAP_AUDIT_WRITE"], "Config": {"Annotations": {"io.kubernetes.cri-o.ContainerType": "sandbox", "io.kubernetes.cri-o.TTY": "false", "io.podman.annotations.autoremove": "FALSE", "io.podman.annotations.init": "FALSE", "io.podman.annotations.privileged": "FALSE", "io.podman.annotations.publish-all": "FALSE"}, "AttachStderr": false, "AttachStdin": false, "AttachStdout": false, "Cmd": ["kolla_start"], "Domainname": "", "Entrypoint": "dumb-init --single-child --", "Env": ["PATH=/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin", "TERM=xterm", "HOSTNAME=", "container=oci", "KOLLA_INSTALL_METATYPE=rdo", "KOLLA_BASE_DISTRO=centos", "KOLLA_INSTALL_TYPE=binary", "KOLLA_DISTRO_PYTHON_VERSION=2.7", "KOLLA_BASE_ARCH=x86_64"], "Hostname": "c5c39e813703", "Image": "docker.io/tripleomaster/centos-haproxy:latest", "Labels": {"build-date": "20190919", "kolla_version": "8.1.0", "name": "haproxy", "org.label-schema.build-date": "20190801", "org.label-schema.license": "GPLv2", "org.label-schema.name": "CentOS Base Image", "org.label-schema.schema-version": "1.0", "org.label-schema.vendor": "CentOS"}, "OnBuild": null, "OpenStdin": false, "StdinOnce": false, "StopSignal": 15, "Tty": false, "User": "", "Volumes": null, "WorkingDir": "/"}, "Created": "2019-10-01T12:51:00.233106443Z", "Dependencies": [], "Driver": "overlay", "EffectiveCaps": ["CAP_CHOWN", "CAP_DAC_OVERRIDE", "CAP_FSETID", "CAP_FOWNER", "CAP_MKNOD", "CAP_NET_RAW", "CAP_SETGID", "CAP_SETUID", "CAP_SETFCAP", "CAP_SETPCAP", "CAP_NET_BIND_SERVICE", "CAP_SYS_CHROOT", "CAP_KILL", "CAP_AUDIT_WRITE"], "ExecIDs": [], "ExitCommand": ["/usr/bin/podman", "--root", "/var/lib/containers/storage", "--runroot", "/var/run/containers/storage", "--log-level", "error", "--cgroup-manager", "systemd", "--tmpdir", "/var/run/libpod", "--runtime", "runc", "--storage-driver", "overlay", "--events-backend", "journald", "container", "cleanup", "c9e813703f9b80a6ea2ad665aa9946435934e478a0c5322da835f3883872f"], "GraphDriver": {"Name": "overlay"}, "HostConfig": {"AutoRemove": false, "Binds": [], "BlkioDeviceReadBps": null, "BlkioDeviceReadIOps": null, "BlkioDeviceWriteBps": null, "BlkioDeviceWriteIOps": null, "BlkioWeight": 0, "BlkioWeightDevice": null, "CapAdd": [], "CapDrop": [], "Cgroup": "", "CgroupParent": "", "ConsoleSize": [0, 0], "ContainerIDFile": "", "CpuCount": 0, "CpuPercent": 0, "CpuPeriod": 0, "CpuQuota": 0, "CpuRealtimePeriod": 0, "CpuRealtimeRuntime": 0, "CpuShares": 0, "CpusetCpus": "", "CpusetMems": "", "Devices": [], "DiskQuota": 0, "Dns": [], "DnsOptions": [], "DnsSearch": [], "ExtraHosts": [], "GroupAdd": [], "IOMaximumBandwidth": 0, "IOMaximumIOps": 0, "IpcMode": "", "Isolation": "", "KernelMemory": 0, "Links": null, "LogConfig": {"Config": null, "Type": "k8s-file"}, "Memory": 0, "MemoryReservation": 0, "MemorySwap": 0, "MemorySwappiness": -1, "NanoCpus": 0, "NetworkMode": "default", "OomKillDisable": false, "OomScoreAdj": 0, "PidMode": "", "PidsLimit": 0, "PortBindings": {}, "Privileged": false, "PublishAllPorts": false, "ReadonlyRootfs": false, "RestartPolicy": {"MaximumRetryCount": 0, "Name": ""}, "Runtime": "oci", "SecurityOpt": [], "ShmSize": 65536000, "Tmpfs": {}, "UTSMode": "", "Ulimits": [{"Hard": 1048576, "Name": "RLIMIT_NOFILE", "Soft": 1048576}, {"Hard": 1048576, "Name": "RLIMIT_NPROC", "Soft": 1048576}], "UsernsMode": "", "VolumeDriver": "", "VolumesFrom": null}, "HostnamePath": "", "HostsPath": "", "Id": "c5c39f9b80a6ea2ad665aa9946435934e478a0c5322da835f3883872f", "Image": "0e267acda67d0ebd643e900d820a91b961d859743039e620191ca1", "ImageName": "docker.io/tripleomaster/centos-haproxy:latest", "IsInfra": false, "MountLabel": "system_u:object_r:svirt_sandbox_file_t:s0:c78,c866", "Mounts": [], "Name": "haproxy", "Namespace": "", "NetworkSettings": {"Bridge": "", "EndpointID": "", "Gateway": "", "GlobalIPv6Address": "", "GlobalIPv6PrefixLen": 0, "HairpinMode": false, "IPAddress": "", "IPPrefixLen": 0, "IPv6Gateway": "", "LinkLocalIPv6Address": "", "LinkLocalIPv6PrefixLen": 0, "MacAddress": "", "Ports": [], "SandboxID": "", "SandboxKey": "", "SecondaryIPAddresses": null, "SecondaryIPv6Addresses": null}, "OCIRuntime": "runc", "Path": "dumb-init", "Pod": "", "ProcessLabel": "system_u:system_r:svirt_lxc_net_t:s0:c785,c866", "ResolvConfPath": "", "RestartCount": 0, "Rootfs": "", "State": {"Dead": false, "Error": "", "ExitCode": 0, "FinishedAt": "0001-01-01T00:00:00Z", "Healthcheck": {"FailingStreak": 0, "Log": null, "Status": ""}, "OOMKilled": false, "OciVersion": "1.0.1-dev", "Paused": false, "Pid": 0, "Restarting": false, "Running": false, "StartedAt": "0001-01-01T00:00:00Z", "Status": "configured"}}]` |

### Authors

- Sagi Shnaidman (@sshnaidm)
- Emilien Macchi (@EmilienM)

### Collection links

[Issue Tracker](https://github.com/containers/ansible-podman-collections/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/containers/ansible-podman-collections.git)
