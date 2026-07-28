---
collection: ansible
version: "6"
title: "openvswitch.openvswitch.openvswitch_port module – Manage Open vSwitch ports"
source_url: https://docs.ansible.com/projects/ansible/6/collections/openvswitch/openvswitch/openvswitch_port_module.html
fetched_at: 2026-07-27T16:43:35+00:00
---
# openvswitch.openvswitch.openvswitch_port module – Manage Open vSwitch ports

> **Note:**
>
> This module is part of the [openvswitch.openvswitch collection](https://galaxy.ansible.com/openvswitch/openvswitch) (version 2.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install openvswitch.openvswitch`.
> You need further requirements to be able to use this module,
> see [Requirements](openvswitch_port_module.md#ansible-collections-openvswitch-openvswitch-openvswitch-port-module-requirements) for details.
>
> To use it in a playbook, specify: `openvswitch.openvswitch.openvswitch_port`.

New in openvswitch.openvswitch 1.0.0

- [Synopsis](openvswitch_port_module.md#synopsis)
- [Requirements](openvswitch_port_module.md#requirements)
- [Parameters](openvswitch_port_module.md#parameters)
- [Examples](openvswitch_port_module.md#examples)

## [Synopsis](openvswitch_port_module.md#id1)

- Manage Open vSwitch ports

## [Requirements](openvswitch_port_module.md#id2)

The below requirements are needed on the host that executes this module.

- ovs-vsctl

## [Parameters](openvswitch_port_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **bridge**  string / required | Name of bridge to manage |
| **database_socket**  string | Path/ip to datbase socket to use  Default path is used if not specified  Path should start with ‘unix:’ prefix |
| **external_ids**  dictionary | Dictionary of external_ids applied to a port.  Default: `{}` |
| **port**  string / required | Name of port to manage on the bridge |
| **set**  list / elements=string | Set multiple properties on a port. |
| **state**  string | Whether the port should exist  Choices:   - `"present"` ← (default) - `"absent"` |
| **tag**  string | VLAN tag for this port. Must be a value between 0 and 4095. |
| **timeout**  integer | How long to wait for ovs-vswitchd to respond  Default: `5` |

## [Examples](openvswitch_port_module.md#id4)

```yaml+jinja
# Creates port eth2 on bridge br-ex
- openvswitch.openvswitch.openvswitch_port:
    bridge: br-ex
    port: eth2
    state: present

# Creates port eth6
- openvswitch.openvswitch.openvswitch_port:
    bridge: bridge-loop
    port: eth6
    state: present
    set: Interface eth6

# Creates port vlan10 with tag 10 on bridge br-ex
- openvswitch.openvswitch.openvswitch_port:
    bridge: br-ex
    port: vlan10
    tag: 10
    state: present
    set: Interface vlan10

# Assign interface id server1-vifeth6 and mac address 00:00:5E:00:53:23
# to port vifeth6 and setup port to be managed by a controller.
- openvswitch.openvswitch.openvswitch_port:
    bridge: br-int
    port: vifeth6
    state: present
  args:
    external_ids:
      iface-id: '{{ inventory_hostname }}-vifeth6'
      attached-mac: 00:00:5E:00:53:23
      vm-id: '{{ inventory_hostname }}'
      iface-status: active

# Plugs port veth0 into brdige br0 for database for OVSDB instance
# with socket unix:/opt/second_ovsdb.sock
- openvswitch.openvswitch.openvswitch_port:
    bridge: br0
    port: veth0
    state: present
    database_socket: unix:/opt/second_ovsdb.sock
```

### Authors

- David Stygstra (@stygstra)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/openvswitch.openvswitch/issues)
[Repository (Sources)](https://github.com/ansible-collections/openvswitch.openvswitch)
