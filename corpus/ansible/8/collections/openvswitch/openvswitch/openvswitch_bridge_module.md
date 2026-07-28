---
collection: ansible
version: "8"
title: "openvswitch.openvswitch.openvswitch_bridge module – Manage Open vSwitch bridges"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openvswitch/openvswitch/openvswitch_bridge_module.html
fetched_at: 2026-07-28T02:49:10+00:00
---
# openvswitch.openvswitch.openvswitch_bridge module – Manage Open vSwitch bridges

> **Note:**
>
> This module is part of the [openvswitch.openvswitch collection](https://galaxy.ansible.com/ui/repo/published/openvswitch/openvswitch/) (version 2.1.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install openvswitch.openvswitch`.
> You need further requirements to be able to use this module,
> see [Requirements](openvswitch_bridge_module.md#ansible-collections-openvswitch-openvswitch-openvswitch-bridge-module-requirements) for details.
>
> To use it in a playbook, specify: `openvswitch.openvswitch.openvswitch_bridge`.

New in openvswitch.openvswitch 1.0.0

- [Synopsis](openvswitch_bridge_module.md#synopsis)
- [Requirements](openvswitch_bridge_module.md#requirements)
- [Parameters](openvswitch_bridge_module.md#parameters)
- [Examples](openvswitch_bridge_module.md#examples)

## [Synopsis](openvswitch_bridge_module.md#id1)

- Manage Open vSwitch bridges

Aliases: bridge

## [Requirements](openvswitch_bridge_module.md#id2)

The below requirements are needed on the host that executes this module.

- ovs-vsctl

## [Parameters](openvswitch_bridge_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **bridge**  string / required | Name of bridge or fake bridge to manage |
| **database_socket**  string | Path/ip to datbase socket to use  Default path is used if not specified  Path should start with ‘unix:’ prefix |
| **external_ids**  dictionary | A dictionary of external-ids. Omitting this parameter is a No-op. To clear all external-ids pass an empty value. |
| **fail_mode**  string | Set bridge fail-mode. The default value (None) is a No-op. |
| **parent**  string | Bridge parent of the fake bridge to manage |
| **set**  string | Run set command after bridge configuration. This parameter is non-idempotent, play will always return *changed* state if present |
| **state**  string | Whether the bridge should exist  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long to wait for ovs-vswitchd to respond  **Default:** `5` |
| **vlan**  integer | The VLAN id of the fake bridge to manage (must be between 0 and 4095). This parameter is required if *parent* parameter is set. |

## [Examples](openvswitch_bridge_module.md#id4)

```yaml+jinja
# Create a bridge named br-int
- openvswitch.openvswitch.openvswitch_bridge:
    bridge: br-int
    state: present

# Create a fake bridge named br-int within br-parent on the VLAN 405
- openvswitch.openvswitch.openvswitch_bridge:
    bridge: br-int
    parent: br-parent
    vlan: 405
    state: present

# Create an integration bridge
- openvswitch.openvswitch.openvswitch_bridge:
    bridge: br-int
    state: present
    fail_mode: secure
  args:
    external_ids:
      bridge-id: br-int
# Create a bridge named br0 in database with socket at /opt/second.sock
- openvswitch.openvswitch.openvswitch_bridge:
    bridge: br0
    state: present
    database_socket: unix:/opt/second.sock
```

### Authors

- David Stygstra (@stygstra)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/openvswitch.openvswitch/issues)
- [Repository (Sources)](https://github.com/ansible-collections/openvswitch.openvswitch)
