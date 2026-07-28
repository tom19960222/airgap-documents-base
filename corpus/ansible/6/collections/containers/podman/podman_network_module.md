---
collection: ansible
version: "6"
title: "containers.podman.podman_network module – Manage podman networks"
source_url: https://docs.ansible.com/projects/ansible/6/collections/containers/podman/podman_network_module.html
fetched_at: 2026-07-27T17:24:35+00:00
---
# containers.podman.podman_network module – Manage podman networks

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
> see [Requirements](podman_network_module.md#ansible-collections-containers-podman-podman-network-module-requirements) for details.
>
> To use it in a playbook, specify: `containers.podman.podman_network`.

New in containers.podman 1.0.0

- [Synopsis](podman_network_module.md#synopsis)
- [Requirements](podman_network_module.md#requirements)
- [Parameters](podman_network_module.md#parameters)
- [Examples](podman_network_module.md#examples)
- [Return Values](podman_network_module.md#return-values)

## [Synopsis](podman_network_module.md#id1)

- Manage podman networks with podman network command.

## [Requirements](podman_network_module.md#id2)

The below requirements are needed on the host that executes this module.

- podman

## [Parameters](podman_network_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **debug**  boolean | Return additional information which can be helpful for investigations.  Choices:   - `false` ← (default) - `true` |
| **disable_dns**  boolean | disable dns plugin (default “false”)  Choices:   - `false` - `true` |
| **driver**  string | Driver to manage the network (default “bridge”) |
| **executable**  string | Path to `podman` executable if it is not in the `$PATH` on the machine running `podman`  Default: `"podman"` |
| **gateway**  string | IPv4 or IPv6 gateway for the subnet |
| **internal**  boolean | Restrict external access from this network (default “false”)  Choices:   - `false` - `true` |
| **ip_range**  string | Allocate container IP from range |
| **ipv6**  boolean | Enable IPv6 (Dual Stack) networking. You must pass a IPv6 subnet. The subnet option must be used with the ipv6 option.  Choices:   - `false` - `true` |
| **macvlan**  string | Create a Macvlan connection based on this device |
| **name**  string / required | Name of the network |
| **opt**  dictionary | Add network options. Currently ‘vlan’ and ‘mtu’ are supported. |
| **mtu**  integer | MTU size for bridge network interface. |
| **vlan**  integer | VLAN tag for bridge which enables vlan_filtering. |
| **recreate**  boolean | Recreate network even if exists.  Choices:   - `false` ← (default) - `true` |
| **state**  string | State of network, default ‘present’  Choices:   - `"present"` ← (default) - `"absent"` |
| **subnet**  string | Subnet in CIDR format |

## [Examples](podman_network_module.md#id4)

```yaml+jinja
- name: Create a podman network
  containers.podman.podman_network:
    name: podman_network
  become: true

- name: Create internal podman network
  containers.podman.podman_network:
    name: podman_internal
    internal: true
    ip_range: 192.168.22.128/25
    subnet: 192.168.22.0/24
    gateway: 192.168.22.1
  become: true
```

## [Return Values](podman_network_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **network**  list / elements=string | Facts from created or updated networks  Returned: always  Sample: `[{"cniVersion": "0.4.0", "name": "podman", "plugins": [{"bridge": "cni-podman0", "ipMasq": true, "ipam": {"ranges": [[{"gateway": "10.88.0.1", "subnet": "10.88.0.0/16"}]], "routes": [{"dst": "0.0.0.0/0"}], "type": "host-local"}, "isGateway": true, "type": "bridge"}, {"capabilities": {"portMappings": true}, "type": "portmap"}, {"backend": "iptables", "type": "firewall"}]}]` |

### Authors

- Sagi Shnaidman (@sshnaidm)

### Collection links

[Issue Tracker](https://github.com/containers/ansible-podman-collections/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/containers/ansible-podman-collections.git)
