---
collection: ansible
version: "6"
title: "mellanox.onyx.onyx_interface module – Manage Interfaces on Mellanox ONYX network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/onyx_interface_module.html
fetched_at: 2026-07-27T17:55:28+00:00
---
# mellanox.onyx.onyx_interface module – Manage Interfaces on Mellanox ONYX network devices

> **Note:**
>
> This module is part of the [mellanox.onyx collection](https://galaxy.ansible.com/mellanox/onyx) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install mellanox.onyx`.
>
> To use it in a playbook, specify: `mellanox.onyx.onyx_interface`.

- [Synopsis](onyx_interface_module.md#synopsis)
- [Parameters](onyx_interface_module.md#parameters)
- [Examples](onyx_interface_module.md#examples)
- [Return Values](onyx_interface_module.md#return-values)

## [Synopsis](onyx_interface_module.md#id1)

- This module provides declarative management of Interfaces on Mellanox ONYX network devices.

## [Parameters](onyx_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregate**  string | List of Interfaces definitions. |
| **delay**  string | Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state argument which are *state* with values `up`/`down`.  Default: `10` |
| **description**  string | Description of Interface. |
| **duplex**  string | Interface link status  Choices:   - `"full"` - `"half"` - `"auto"` ← (default) |
| **enabled**  boolean | Interface link status.  Choices:   - `false` - `true` |
| **mtu**  string | Maximum size of transmit packet. |
| **name**  string / required | Name of the Interface. |
| **purge**  boolean | Purge Interfaces not defined in the aggregate parameter. This applies only for logical interface.  Choices:   - `false` ← (default) - `true` |
| **rx_rate**  string | Receiver rate in bits per second (bps).  This is state check parameter only.  Supports conditionals, see [Conditionals in Networking Modules](../network/user_guide/network_working_with_command_output.md) |
| **speed**  string | Interface link speed.  Choices:   - `"1G"` - `"10G"` - `"25G"` - `"40G"` - `"50G"` - `"56G"` - `"100G"` |
| **state**  string | State of the Interface configuration, `up` means present and operationally up and `down` means present and operationally `down`  Choices:   - `"present"` ← (default) - `"absent"` - `"up"` - `"down"` |
| **tx_rate**  string | Transmit rate in bits per second (bps).  This is state check parameter only.  Supports conditionals, see [Conditionals in Networking Modules](../network/user_guide/network_working_with_command_output.md) |

## [Examples](onyx_interface_module.md#id3)

```yaml+jinja
- name: Configure interface
  onyx_interface:
      name: Eth1/2
      description: test-interface
      speed: 100G
      mtu: 512

- name: Make interface up
  onyx_interface:
    name: Eth1/2
    enabled: True

- name: Make interface down
  onyx_interface:
    name: Eth1/2
    enabled: False

- name: Check intent arguments
  onyx_interface:
    name: Eth1/2
    state: up

- name: Config + intent
  onyx_interface:
    name: Eth1/2
    enabled: False
    state: down
```

## [Return Values](onyx_interface_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device.  Returned: always  Sample: `["interface ethernet 1/2", "description test-interface", "mtu 512", "exit"]` |

### Authors

- Samer Deeb (@samerd)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)
