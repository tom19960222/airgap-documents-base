---
collection: ansible
version: "6"
title: "containers.podman.podman_network_info module – Gather info about podman networks"
source_url: https://docs.ansible.com/projects/ansible/6/collections/containers/podman/podman_network_info_module.html
fetched_at: 2026-07-27T17:24:36+00:00
---
# containers.podman.podman_network_info module – Gather info about podman networks

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
> see [Requirements](podman_network_info_module.md#ansible-collections-containers-podman-podman-network-info-module-requirements) for details.
>
> To use it in a playbook, specify: `containers.podman.podman_network_info`.

New in containers.podman 1.0.0

- [Synopsis](podman_network_info_module.md#synopsis)
- [Requirements](podman_network_info_module.md#requirements)
- [Parameters](podman_network_info_module.md#parameters)
- [Examples](podman_network_info_module.md#examples)
- [Return Values](podman_network_info_module.md#return-values)

## [Synopsis](podman_network_info_module.md#id1)

- Gather info about podman networks with podman inspect command.

## [Requirements](podman_network_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- Podman installed on host

## [Parameters](podman_network_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **executable**  string | Path to `podman` executable if it is not in the `$PATH` on the machine running `podman`  Default: `"podman"` |
| **name**  string | Name of the network |

## [Examples](podman_network_info_module.md#id4)

```yaml+jinja
- name: Gather info about all present networks
  containers.podman.podman_network_info:

- name: Gather info about specific network
  containers.podman.podman_network_info:
    name: podman
```

## [Return Values](podman_network_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **networks**  list / elements=string | Facts from all or specified networks  Returned: always  Sample: `[{"cniVersion": "0.4.0", "name": "podman", "plugins": [{"bridge": "cni-podman0", "ipMasq": true, "ipam": {"ranges": [[{"gateway": "10.88.0.1", "subnet": "10.88.0.0/16"}]], "routes": [{"dst": "0.0.0.0/0"}], "type": "host-local"}, "isGateway": true, "type": "bridge"}, {"capabilities": {"portMappings": true}, "type": "portmap"}, {"backend": "iptables", "type": "firewall"}]}]` |

### Authors

- Sagi Shnaidman (@sshnaidm)

### Collection links

[Issue Tracker](https://github.com/containers/ansible-podman-collections/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/containers/ansible-podman-collections.git)
