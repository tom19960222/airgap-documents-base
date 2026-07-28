---
collection: ansible
version: "6"
title: "openvswitch.openvswitch.openvswitch_bond module – Manage Open vSwitch bonds"
source_url: https://docs.ansible.com/projects/ansible/6/collections/openvswitch/openvswitch/openvswitch_bond_module.html
fetched_at: 2026-07-28T00:17:17+00:00
---
# openvswitch.openvswitch.openvswitch_bond module – Manage Open vSwitch bonds

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
> see [Requirements](openvswitch_bond_module.md#ansible-collections-openvswitch-openvswitch-openvswitch-bond-module-requirements) for details.
>
> To use it in a playbook, specify: `openvswitch.openvswitch.openvswitch_bond`.

New in openvswitch.openvswitch 1.0.0

- [Synopsis](openvswitch_bond_module.md#synopsis)
- [Requirements](openvswitch_bond_module.md#requirements)
- [Parameters](openvswitch_bond_module.md#parameters)
- [Examples](openvswitch_bond_module.md#examples)

## [Synopsis](openvswitch_bond_module.md#id1)

- Manage Open vSwitch bonds and associated options.

## [Requirements](openvswitch_bond_module.md#id2)

The below requirements are needed on the host that executes this module.

- ovs-vsctl

## [Parameters](openvswitch_bond_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **bond_downdelay**  integer | Number of milliseconds a link must be down to be deactivated to prevent flapping. |
| **bond_mode**  string | Sets the bond mode  Choices:   - `"active-backup"` - `"balance-tcp"` - `"balance-slb"` |
| **bond_updelay**  integer | Number of milliseconds a link must be up to be activated to prevent flapping. |
| **bridge**  string / required | Name of bridge to manage |
| **database_socket**  string | Path/ip to datbase socket to use  Default path is used if not specified  Path should start with ‘unix:’ prefix |
| **external_ids**  dictionary | Dictionary of external_ids applied to a port.  Default: `{}` |
| **interfaces**  list / elements=string | List of interfaces to add to the bond |
| **lacp**  string | Sets LACP mode  Choices:   - `"active"` - `"passive"` - `"off"` |
| **other_config**  dictionary | Dictionary of other_config applied to a port.  Default: `{}` |
| **port**  string / required | Name of port to manage on the bridge |
| **set**  list / elements=string | Sets one or more properties on a port. |
| **state**  string | Whether the port should exist  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long to wait for ovs-vswitchd to respond in seconds  Default: `5` |

## [Examples](openvswitch_bond_module.md#id4)

```yaml+jinja
- name: Create an active-backup bond using eth4 and eth5 on bridge br-ex
  openvswitch.openvswitch.openvswitch_bond:
    bridge: br-ex
    port: bond1
    interfaces:
      - eth4
      - eth5
    state: present
- name: Delete the bond from bridge br-ex
  openvswitch.openvswitch.openvswitch_bond:
    bridge: br-ex
    port: bond1
    state: absent
- name: Create an active LACP bond using eth4 and eth5 on bridge br-ex
  openvswitch.openvswitch.openvswitch_bond:
    bridge: br-ex
    port: bond1
    interfaces:
      - eth4
      - eth5
    lacp: active
    state: present
# NOTE: other_config values of integer type must be represented
# as literal strings
- name: Configure bond with miimon link monitoring at 100 millisecond intervals
  openvswitch.openvswitch.openvswitch_bond:
    bridge: br-ex
    port: bond1
    interfaces:
      - eth4
      - eth5
    bond_updelay: 100
    bond_downdelay: 100
    state: present
  args:
    other_config:
      bond-detect-mode: miimon
      bond-miimon-interval: '"100"'
- name: Create an active LACP bond using DPDK interfaces
  openvswitch.openvswitch.openvswitch_bond:
    bridge: br-provider
    port: dpdkbond
    interfaces:
      - "0000:04:00.0"
      - "0000:04:00.1"
    lacp: active
    set:
      - "interface 0000:04:00.0 type=dpdk options:dpdk-devargs=0000:04:00.0"
      - "interface 0000:04:00.1 type=dpdk options:dpdk-devargs=0000:04:00.1"
    state: present
- name: Create an active-backup bond using eth4 and eth5 on bridge br-ex in second OVS database
  openvswitch.openvswitch.openvswitch_bond:
    bridge: br-ex
    port: bond1
    interfaces:
      - eth4
      - eth5
    state: present
    database_socket: unix:/opt/second.sock
```

### Authors

- James Denton (@busterswt)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/openvswitch.openvswitch/issues)
[Repository (Sources)](https://github.com/ansible-collections/openvswitch.openvswitch)
