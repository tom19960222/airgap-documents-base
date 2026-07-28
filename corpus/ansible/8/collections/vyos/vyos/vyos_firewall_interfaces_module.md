---
collection: ansible
version: "8"
title: "vyos.vyos.vyos_firewall_interfaces module – FIREWALL interfaces resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vyos/vyos/vyos_firewall_interfaces_module.html
fetched_at: 2026-07-28T02:59:12+00:00
---
# vyos.vyos.vyos_firewall_interfaces module – FIREWALL interfaces resource module

> **Note:**
>
> This module is part of the [vyos.vyos collection](https://galaxy.ansible.com/ui/repo/published/vyos/vyos/) (version 4.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vyos.vyos`.
>
> To use it in a playbook, specify: `vyos.vyos.vyos_firewall_interfaces`.

New in vyos.vyos 1.0.0

- [Synopsis](vyos_firewall_interfaces_module.md#synopsis)
- [Parameters](vyos_firewall_interfaces_module.md#parameters)
- [Examples](vyos_firewall_interfaces_module.md#examples)
- [Return Values](vyos_firewall_interfaces_module.md#return-values)

## [Synopsis](vyos_firewall_interfaces_module.md#id1)

- Manage firewall rules of interfaces on VyOS network devices.

Aliases: firewall_interfaces

## [Parameters](vyos_firewall_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of firewall rules options for interfaces. |
| **access_rules**  list / elements=dictionary | Specifies firewall rules attached to the interfaces. |
| **afi**  string / required | Specifies the AFI for the Firewall rules to be configured on this interface.  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **rules**  list / elements=dictionary | Specifies the firewall rules for the provided AFI. |
| **direction**  string / required | Specifies the direction of packets that the firewall rule will be applied on.  **Choices:**   - `"in"` - `"local"` - `"out"` |
| **name**  string | Specifies the name of the IPv4/IPv6 Firewall rule for the interface. |
| **name**  string / required | Name/Identifier for the interface. |
| **running_config**  string | The module, by default, will connect to the remote device and retrieve the current running-config to use as a base for comparing against the contents of source. There are times when it is not desirable to have the task get the current running-config for every task in a playbook. The *running_config* argument allows the implementer to pass in the configuration to use as the base config for comparison. This value of this option should be the output received from device by executing command `show configuration commands | grep 'firewall'`. |
| **state**  string | The state the configuration should be left in.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"parsed"` - `"rendered"` - `"gathered"` |

## [Examples](vyos_firewall_interfaces_module.md#id3)

```yaml+jinja
# Using merged
#
# Before state:
# -------------
#
# vyos@192# run show configuration commands | grep firewall
# set firewall ipv6-name 'V6-LOCAL'
# set firewall name 'INBOUND'
# set firewall name 'LOCAL'
# set firewall name 'OUTBOUND'
#
- name: Merge the provided configuration with the existing running configuration
  vyos.vyos.vyos_firewall_interfaces:
    config:
    - access_rules:
      - afi: ipv4
        rules:
        - name: INBOUND
          direction: in
        - name: OUTBOUND
          direction: out
        - name: LOCAL
          direction: local
      - afi: ipv6
        rules:
        - name: V6-LOCAL
          direction: local
      name: eth1
    - access_rules:
      - afi: ipv4
        rules:
        - name: INBOUND
          direction: in
        - name: OUTBOUND
          direction: out
        - name: LOCAL
          direction: local
      - afi: ipv6
        rules:
        - name: V6-LOCAL
          direction: local
      name: eth3
    state: merged
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
# before": [
#        {
#            "name": "eth0"
#        },
#        {
#            "name": "eth1"
#        },
#        {
#            "name": "eth2"
#        },
#        {
#            "name": "eth3"
#        }
#    ]
#
#    "commands": [
#       "set interfaces ethernet eth1 firewall in name 'INBOUND'",
#       "set interfaces ethernet eth1 firewall out name 'OUTBOUND'",
#       "set interfaces ethernet eth1 firewall local name 'LOCAL'",
#       "set interfaces ethernet eth1 firewall local ipv6-name 'V6-LOCAL'",
#       "set interfaces ethernet eth3 firewall in name 'INBOUND'",
#       "set interfaces ethernet eth3 firewall out name 'OUTBOUND'",
#       "set interfaces ethernet eth3 firewall local name 'LOCAL'",
#       "set interfaces ethernet eth3 firewall local ipv6-name 'V6-LOCAL'"
#    ]
#
# "after": [
#        {
#            "name": "eth0"
#        },
#        {
#            "access_rules": [
#                {
#                    "afi": "ipv4",
#                    "rules": [
#                        {
#                            "direction": "in",
#                            "name": "INBOUND"
#                        },
#                        {
#                            "direction": "local",
#                            "name": "LOCAL"
#                        },
#                        {
#                            "direction": "out",
#                            "name": "OUTBOUND"
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "rules": [
#                        {
#                            "direction": "local",
#                            "name": "V6-LOCAL"
#                        }
#                    ]
#                }
#            ],
#            "name": "eth1"
#        },
#        {
#            "name": "eth2"
#        },
#        {
#            "access_rules": [
#                {
#                    "afi": "ipv4",
#                    "rules": [
#                        {
#                            "direction": "in",
#                            "name": "INBOUND"
#                        },
#                        {
#                            "direction": "local",
#                            "name": "LOCAL"
#                        },
#                        {
#                            "direction": "out",
#                            "name": "OUTBOUND"
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "rules": [
#                        {
#                            "direction": "local",
#                            "name": "V6-LOCAL"
#                        }
#                    ]
#                }
#            ],
#            "name": "eth3"
#        }
#    ]
#
# After state:
# -------------
#
# vyos@vyos:~$ show configuration commands| grep firewall
# set firewall ipv6-name 'V6-LOCAL'
# set firewall name 'INBOUND'
# set firewall name 'LOCAL'
# set firewall name 'OUTBOUND'
# set interfaces ethernet eth1 firewall in name 'INBOUND'
# set interfaces ethernet eth1 firewall local ipv6-name 'V6-LOCAL'
# set interfaces ethernet eth1 firewall local name 'LOCAL'
# set interfaces ethernet eth1 firewall out name 'OUTBOUND'
# set interfaces ethernet eth3 firewall in name 'INBOUND'
# set interfaces ethernet eth3 firewall local ipv6-name 'V6-LOCAL'
# set interfaces ethernet eth3 firewall local name 'LOCAL'
# set interfaces ethernet eth3 firewall out name 'OUTBOUND'

# Using merged
#
# Before state:
# -------------
#
# vyos@vyos:~$ show configuration commands| grep firewall
# set firewall ipv6-name 'V6-LOCAL'
# set firewall name 'INBOUND'
# set firewall name 'LOCAL'
# set firewall name 'OUTBOUND'
# set interfaces ethernet eth1 firewall in name 'INBOUND'
# set interfaces ethernet eth1 firewall local ipv6-name 'V6-LOCAL'
# set interfaces ethernet eth1 firewall local name 'LOCAL'
# set interfaces ethernet eth1 firewall out name 'OUTBOUND'
# set interfaces ethernet eth3 firewall in name 'INBOUND'
# set interfaces ethernet eth3 firewall local ipv6-name 'V6-LOCAL'
# set interfaces ethernet eth3 firewall local name 'LOCAL'
# set interfaces ethernet eth3 firewall out name 'OUTBOUND'
#
- name: Merge the provided configuration with the existing running configuration
  vyos.vyos.vyos_firewall_interfaces:
    config:
    - access_rules:
      - afi: ipv4
        rules:
        - name: OUTBOUND
          direction: in
        - name: INBOUND
          direction: out
      name: eth1
    state: merged
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "before": [
#        {
#            "name": "eth0"
#        },
#        {
#            "access_rules": [
#                {
#                    "afi": "ipv4",
#                    "rules": [
#                        {
#                            "direction": "in",
#                            "name": "INBOUND"
#                        },
#                        {
#                            "direction": "local",
#                            "name": "LOCAL"
#                        },
#                        {
#                            "direction": "out",
#                            "name": "OUTBOUND"
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "rules": [
#                        {
#                            "direction": "local",
#                            "name": "V6-LOCAL"
#                        }
#                    ]
#                }
#            ],
#            "name": "eth1"
#        },
#        {
#            "name": "eth2"
#        },
#        {
#            "access_rules": [
#                {
#                    "afi": "ipv4",
#                    "rules": [
#                        {
#                            "direction": "in",
#                            "name": "INBOUND"
#                        },
#                        {
#                            "direction": "local",
#                            "name": "LOCAL"
#                        },
#                        {
#                            "direction": "out",
#                            "name": "OUTBOUND"
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "rules": [
#                        {
#                            "direction": "local",
#                            "name": "V6-LOCAL"
#                        }
#                    ]
#                }
#            ],
#            "name": "eth3"
#        }
#    ]
#
#    "commands": [
#       "set interfaces ethernet eth1 firewall in name 'OUTBOUND'",
#       "set interfaces ethernet eth1 firewall out name 'INBOUND'"
#    ]
#
#    "after": [
#        {
#            "name": "eth0"
#        },
#        {
#            "access_rules": [
#                {
#                    "afi": "ipv4",
#                    "rules": [
#                        {
#                            "direction": "in",
#                            "name": "OUTBOUND"
#                        },
#                        {
#                            "direction": "local",
#                            "name": "LOCAL"
#                        },
#                        {
#                            "direction": "out",
#                            "name": "INBOUND"
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "rules": [
#                        {
#                            "direction": "local",
#                            "name": "V6-LOCAL"
#                        }
#                    ]
#                }
#            ],
#            "name": "eth1"
#        },
#        {
#            "name": "eth2"
#        },
#        {
#            "access_rules": [
#                {
#                    "afi": "ipv4",
#                    "rules": [
#                        {
#                            "direction": "in",
#                            "name": "INBOUND"
#                        },
#                        {
#                            "direction": "local",
#                            "name": "LOCAL"
#                        },
#                        {
#                            "direction": "out",
#                            "name": "OUTBOUND"
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "rules": [
#                        {
#                            "direction": "local",
#                            "name": "V6-LOCAL"
#                        }
#                    ]
#                }
#            ],
#            "name": "eth3"
#        }
#    ]
#
# After state:
# -------------
#
# vyos@vyos:~$ show configuration commands| grep firewall
# set firewall ipv6-name 'V6-LOCAL'
# set firewall name 'INBOUND'
# set firewall name 'LOCAL'
# set firewall name 'OUTBOUND'
# set interfaces ethernet eth1 firewall in name 'OUTBOUND'
# set interfaces ethernet eth1 firewall local ipv6-name 'V6-LOCAL'
# set interfaces ethernet eth1 firewall local name 'LOCAL'
# set interfaces ethernet eth1 firewall out name 'INBOUND'
# set interfaces ethernet eth3 firewall in name 'INBOUND'
# set interfaces ethernet eth3 firewall local ipv6-name 'V6-LOCAL'
# set interfaces ethernet eth3 firewall local name 'LOCAL'
# set interfaces ethernet eth3 firewall out name 'OUTBOUND'

# Using replaced
#
# Before state:
# -------------
#
# vyos@vyos:~$ show configuration commands| grep firewall
# set firewall ipv6-name 'V6-LOCAL'
# set firewall name 'INBOUND'
# set firewall name 'LOCAL'
# set firewall name 'OUTBOUND'
# set interfaces ethernet eth1 firewall in name 'INBOUND'
# set interfaces ethernet eth1 firewall local ipv6-name 'V6-LOCAL'
# set interfaces ethernet eth1 firewall local name 'LOCAL'
# set interfaces ethernet eth1 firewall out name 'OUTBOUND'
# set interfaces ethernet eth3 firewall in name 'INBOUND'
# set interfaces ethernet eth3 firewall local ipv6-name 'V6-LOCAL'
# set interfaces ethernet eth3 firewall local name 'LOCAL'
# set interfaces ethernet eth3 firewall out name 'OUTBOUND'
#
- name: Replace device configurations of listed firewall interfaces with provided
    configurations
  vyos.vyos.vyos_firewall_interfaces:
    config:
    - name: eth1
      access_rules:
      - afi: ipv4
        rules:
        - name: OUTBOUND
          direction: out
      - afi: ipv6
        rules:
        - name: V6-LOCAL
          direction: local
    - name: eth3
      access_rules:
      - afi: ipv4
        rules:
        - name: INBOUND
          direction: in
    state: replaced
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "before": [
#        {
#            "name": "eth0"
#        },
#        {
#            "access_rules": [
#                {
#                    "afi": "ipv4",
#                    "rules": [
#                        {
#                            "direction": "in",
#                            "name": "INBOUND"
#                        },
#                        {
#                            "direction": "local",
#                            "name": "LOCAL"
#                        },
#                        {
#                            "direction": "out",
#                            "name": "OUTBOUND"
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "rules": [
#                        {
#                            "direction": "local",
#                            "name": "V6-LOCAL"
#                        }
#                    ]
#                }
#            ],
#            "name": "eth1"
#        },
#        {
#            "name": "eth2"
#        },
#        {
#            "access_rules": [
#                {
#                    "afi": "ipv4",
#                    "rules": [
#                        {
#                            "direction": "in",
#                            "name": "INBOUND"
#                        },
#                        {
#                            "direction": "local",
#                            "name": "LOCAL"
#                        },
#                        {
#                            "direction": "out",
#                            "name": "OUTBOUND"
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "rules": [
#                        {
#                            "direction": "local",
#                            "name": "V6-LOCAL"
#                        }
#                    ]
#                }
#            ],
#            "name": "eth3"
#        }
#    ]
#
# "commands": [
#        "delete interfaces ethernet eth1 firewall in name",
#        "delete interfaces ethernet eth1 firewall local name",
#        "delete interfaces ethernet eth3 firewall local name",
#        "delete interfaces ethernet eth3 firewall out name",
#        "delete interfaces ethernet eth3 firewall local ipv6-name"
#    ]
#
#    "after": [
#        {
#            "name": "eth0"
#        },
#        {
#            "access_rules": [
#                {
#                    "afi": "ipv4",
#                    "rules": [
#                        {
#                            "direction": "out",
#                            "name": "OUTBOUND"
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "rules": [
#                        {
#                            "direction": "local",
#                            "name": "V6-LOCAL"
#                        }
#                    ]
#                }
#            ],
#            "name": "eth1"
#        },
#        {
#            "name": "eth2"
#        },
#        {
#            "access_rules": [
#                {
#                    "afi": "ipv4",
#                    "rules": [
#                        {
#                            "direction": "in",
#                            "name": "INBOUND"
#                        }
#                    ]
#                }
#            ],
#            "name": "eth3"
#        }
#    ]
#
# After state:
# -------------
#
# vyos@vyos:~$ show configuration commands| grep firewall
# set firewall ipv6-name 'V6-LOCAL'
# set firewall name 'INBOUND'
# set firewall name 'LOCAL'
# set firewall name 'OUTBOUND'
# set interfaces ethernet eth1 firewall 'in'
# set interfaces ethernet eth1 firewall local ipv6-name 'V6-LOCAL'
# set interfaces ethernet eth1 firewall out name 'OUTBOUND'
# set interfaces ethernet eth3 firewall in name 'INBOUND'
# set interfaces ethernet eth3 firewall 'local'
# set interfaces ethernet eth3 firewall 'out'

# Using overridden
#
# Before state
# --------------
#
# vyos@vyos:~$ show configuration commands| grep firewall
# set firewall ipv6-name 'V6-LOCAL'
# set firewall name 'INBOUND'
# set firewall name 'LOCAL'
# set firewall name 'OUTBOUND'
# set interfaces ethernet eth1 firewall 'in'
# set interfaces ethernet eth1 firewall local ipv6-name 'V6-LOCAL'
# set interfaces ethernet eth1 firewall out name 'OUTBOUND'
# set interfaces ethernet eth3 firewall in name 'INBOUND'
# set interfaces ethernet eth3 firewall 'local'
# set interfaces ethernet eth3 firewall 'out'
#
- name: Overrides all device configuration with provided configuration
  vyos.vyos.vyos_firewall_interfaces:
    config:
    - name: eth3
      access_rules:
      - afi: ipv4
        rules:
        - name: INBOUND
          direction: out
    state: overridden
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
# "before":[
#        {
#            "name": "eth0"
#        },
#        {
#            "access_rules": [
#                {
#                    "afi": "ipv4",
#                    "rules": [
#                        {
#                            "direction": "out",
#                            "name": "OUTBOUND"
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "rules": [
#                        {
#                            "direction": "local",
#                            "name": "V6-LOCAL"
#                        }
#                    ]
#                }
#            ],
#            "name": "eth1"
#        },
#        {
#            "name": "eth2"
#        },
#        {
#            "access_rules": [
#                {
#                    "afi": "ipv4",
#                    "rules": [
#                        {
#                            "direction": "in",
#                            "name": "INBOUND"
#                        }
#                    ]
#                }
#            ],
#            "name": "eth3"
#        }
#    ]
#
#    "commands": [
#        "delete interfaces ethernet eth1 firewall",
#        "delete interfaces ethernet eth3 firewall in name",
#        "set interfaces ethernet eth3 firewall out name 'INBOUND'"
#
#
#    "after": [
#        {
#            "name": "eth0"
#        },
#        {
#            "name": "eth1"
#        },
#        {
#            "name": "eth2"
#        },
#        {
#            "access_rules": [
#                {
#                    "afi": "ipv4",
#                    "rules": [
#                        {
#                            "direction": "out",
#                            "name": "INBOUND"
#                        }
#                    ]
#                }
#            ],
#            "name": "eth3"
#        }
#    ]
#
#
# After state
# ------------
#
# vyos@vyos:~$ show configuration commands| grep firewall
# set firewall ipv6-name 'V6-LOCAL'
# set firewall name 'INBOUND'
# set firewall name 'LOCAL'
# set firewall name 'OUTBOUND'
# set interfaces ethernet eth3 firewall 'in'
# set interfaces ethernet eth3 firewall 'local'
# set interfaces ethernet eth3 firewall out name 'INBOUND'

# Using deleted per interface name
#
# Before state
# -------------
#
# vyos@vyos:~$ show configuration commands| grep firewall
# set firewall ipv6-name 'V6-LOCAL'
# set firewall name 'INBOUND'
# set firewall name 'LOCAL'
# set firewall name 'OUTBOUND'
# set interfaces ethernet eth1 firewall in name 'INBOUND'
# set interfaces ethernet eth1 firewall local ipv6-name 'V6-LOCAL'
# set interfaces ethernet eth1 firewall local name 'LOCAL'
# set interfaces ethernet eth1 firewall out name 'OUTBOUND'
# set interfaces ethernet eth3 firewall in name 'INBOUND'
# set interfaces ethernet eth3 firewall local ipv6-name 'V6-LOCAL'
# set interfaces ethernet eth3 firewall local name 'LOCAL'
# set interfaces ethernet eth3 firewall out name 'OUTBOUND'
#
- name: Delete firewall interfaces based on interface name.
  vyos.vyos.vyos_firewall_interfaces:
    config:
    - name: eth1
    - name: eth3
    state: deleted
#
#
# ------------------------
# Module Execution Results
# ------------------------
#
# "before": [
#        {
#            "name": "eth0"
#        },
#        {
#            "access_rules": [
#                {
#                    "afi": "ipv4",
#                    "rules": [
#                        {
#                            "direction": "in",
#                            "name": "INBOUND"
#                        },
#                        {
#                            "direction": "local",
#                            "name": "LOCAL"
#                        },
#                        {
#                            "direction": "out",
#                            "name": "OUTBOUND"
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "rules": [
#                        {
#                            "direction": "local",
#                            "name": "V6-LOCAL"
#                        }
#                    ]
#                }
#            ],
#            "name": "eth1"
#        },
#        {
#            "name": "eth2"
#        },
#        {
#            "access_rules": [
#                {
#                    "afi": "ipv4",
#                    "rules": [
#                        {
#                            "direction": "in",
#                            "name": "INBOUND"
#                        },
#                        {
#                            "direction": "local",
#                            "name": "LOCAL"
#                        },
#                        {
#                            "direction": "out",
#                            "name": "OUTBOUND"
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "rules": [
#                        {
#                            "direction": "local",
#                            "name": "V6-LOCAL"
#                        }
#                    ]
#                }
#            ],
#            "name": "eth3"
#        }
#    ]
#    "commands": [
#        "delete interfaces ethernet eth1 firewall",
#        "delete interfaces ethernet eth3 firewall"
#    ]
#
# "after": [
#        {
#            "name": "eth0"
#        },
#        {
#            "name": "eth1"
#        },
#        {
#            "name": "eth2"
#        },
#        {
#            "name": "eth3"
#        }
#    ]
# After state
# ------------
# vyos@vyos# run show configuration commands | grep firewall
# set firewall ipv6-name 'V6-LOCAL'
# set firewall name 'INBOUND'
# set firewall name 'LOCAL'
# set firewall name 'OUTBOUND'

# Using deleted per afi
#
# Before state
# -------------
#
# vyos@vyos:~$ show configuration commands| grep firewall
# set firewall ipv6-name 'V6-LOCAL'
# set firewall name 'INBOUND'
# set firewall name 'LOCAL'
# set firewall name 'OUTBOUND'
# set interfaces ethernet eth1 firewall in name 'INBOUND'
# set interfaces ethernet eth1 firewall local ipv6-name 'V6-LOCAL'
# set interfaces ethernet eth1 firewall local name 'LOCAL'
# set interfaces ethernet eth1 firewall out name 'OUTBOUND'
# set interfaces ethernet eth3 firewall in name 'INBOUND'
# set interfaces ethernet eth3 firewall local ipv6-name 'V6-LOCAL'
# set interfaces ethernet eth3 firewall local name 'LOCAL'
# set interfaces ethernet eth3 firewall out name 'OUTBOUND'
#
- name: Delete firewall interfaces config per afi.
  vyos.vyos.vyos_firewall_interfaces:
    config:
    - name: eth1
      access_rules:
      - afi: ipv4
      - afi: ipv6
    state: deleted
#
#
# ------------------------
# Module Execution Results
# ------------------------
#
#    "commands": [
#        "delete interfaces ethernet eth1 firewall in name",
#        "delete interfaces ethernet eth1 firewall out name",
#        "delete interfaces ethernet eth1 firewall local name",
#        "delete interfaces ethernet eth1 firewall local ipv6-name"
#    ]
#
# After state
# ------------
# vyos@vyos# run show configuration commands | grep firewall
# set firewall ipv6-name 'V6-LOCAL'
# set firewall name 'INBOUND'
# set firewall name 'LOCAL'
# set firewall name 'OUTBOUND'

# Using deleted without config
#
# Before state
# -------------
#
# vyos@vyos:~$ show configuration commands| grep firewall
# set firewall ipv6-name 'V6-LOCAL'
# set firewall name 'INBOUND'
# set firewall name 'LOCAL'
# set firewall name 'OUTBOUND'
# set interfaces ethernet eth1 firewall in name 'INBOUND'
# set interfaces ethernet eth1 firewall local ipv6-name 'V6-LOCAL'
# set interfaces ethernet eth1 firewall local name 'LOCAL'
# set interfaces ethernet eth1 firewall out name 'OUTBOUND'
# set interfaces ethernet eth3 firewall in name 'INBOUND'
# set interfaces ethernet eth3 firewall local ipv6-name 'V6-LOCAL'
# set interfaces ethernet eth3 firewall local name 'LOCAL'
# set interfaces ethernet eth3 firewall out name 'OUTBOUND'
#
- name: Delete firewall interfaces config when empty config provided.
  vyos.vyos.vyos_firewall_interfaces:
    config:
    state: deleted
#
#
# ------------------------
# Module Execution Results
# ------------------------
#
#    "commands": [
#        "delete interfaces ethernet eth1 firewall",
#        "delete interfaces ethernet eth1 firewall"
#    ]
#
# After state
# ------------
# vyos@vyos# run show configuration commands | grep firewall
# set firewall ipv6-name 'V6-LOCAL'
# set firewall name 'INBOUND'
# set firewall name 'LOCAL'
# set firewall name 'OUTBOUND'

# Using parsed
#
#
- name: Parse the provided  configuration
  vyos.vyos.vyos_firewall_interfaces:
    running_config:
      "set interfaces ethernet eth1 firewall in name 'INBOUND'
       set interfaces ethernet eth1 firewall out name 'OUTBOUND'
       set interfaces ethernet eth1 firewall local name 'LOCAL'
       set interfaces ethernet eth1 firewall local ipv6-name 'V6-LOCAL'
       set interfaces ethernet eth2 firewall in name 'INBOUND'
       set interfaces ethernet eth2 firewall out name 'OUTBOUND'
       set interfaces ethernet eth2 firewall local name 'LOCAL'
       set interfaces ethernet eth2 firewall local ipv6-name 'V6-LOCAL'"
    state: parsed
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "parsed": [
#        {
#            "name": "eth0"
#        },
#        {
#            "access_rules": [
#                {
#                    "afi": "ipv4",
#                    "rules": [
#                        {
#                            "direction": "in",
#                            "name": "INBOUND"
#                        },
#                        {
#                            "direction": "local",
#                            "name": "LOCAL"
#                        },
#                        {
#                            "direction": "out",
#                            "name": "OUTBOUND"
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "rules": [
#                        {
#                            "direction": "local",
#                            "name": "V6-LOCAL"
#                        }
#                    ]
#                }
#            ],
#            "name": "eth1"
#        },
#        {
#            "access_rules": [
#                {
#                    "afi": "ipv4",
#                    "rules": [
#                        {
#                            "direction": "in",
#                            "name": "INBOUND"
#                        },
#                        {
#                            "direction": "local",
#                            "name": "LOCAL"
#                        },
#                        {
#                            "direction": "out",
#                            "name": "OUTBOUND"
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "rules": [
#                        {
#                            "direction": "local",
#                            "name": "V6-LOCAL"
#                        }
#                    ]
#                }
#            ],
#            "name": "eth2"
#        },
#        {
#            "name": "eth3"
#        }
#    ]

# Using gathered
#
# Before state:
# -------------
#
# vyos@vyos:~$ show configuration commands| grep firewall
# set firewall ipv6-name 'V6-LOCAL'
# set firewall name 'INBOUND'
# set firewall name 'LOCAL'
# set firewall name 'OUTBOUND'
# set interfaces ethernet eth1 firewall 'in'
# set interfaces ethernet eth1 firewall local ipv6-name 'V6-LOCAL'
# set interfaces ethernet eth1 firewall out name 'OUTBOUND'
# set interfaces ethernet eth3 firewall in name 'INBOUND'
# set interfaces ethernet eth3 firewall 'local'
# set interfaces ethernet eth3 firewall 'out'
#
- name: Gather listed firewall interfaces.
  vyos.vyos.vyos_firewall_interfaces:
    config:
    state: gathered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "gathered": [
#        {
#            "name": "eth0"
#        },
#        {
#            "access_rules": [
#                {
#                    "afi": "ipv4",
#                    "rules": [
#                        {
#                            "direction": "out",
#                            "name": "OUTBOUND"
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "rules": [
#                        {
#                            "direction": "local",
#                            "name": "V6-LOCAL"
#                        }
#                    ]
#                }
#            ],
#            "name": "eth1"
#        },
#        {
#            "name": "eth2"
#        },
#        {
#            "access_rules": [
#                {
#                    "afi": "ipv4",
#                    "rules": [
#                        {
#                            "direction": "in",
#                            "name": "INBOUND"
#                        }
#                    ]
#                }
#            ],
#            "name": "eth3"
#        }
#    ]
#
#
# After state:
# -------------
#
# vyos@vyos:~$ show configuration commands| grep firewall
# set firewall ipv6-name 'V6-LOCAL'
# set firewall name 'INBOUND'
# set firewall name 'LOCAL'
# set firewall name 'OUTBOUND'
# set interfaces ethernet eth1 firewall 'in'
# set interfaces ethernet eth1 firewall local ipv6-name 'V6-LOCAL'
# set interfaces ethernet eth1 firewall out name 'OUTBOUND'
# set interfaces ethernet eth3 firewall in name 'INBOUND'
# set interfaces ethernet eth3 firewall 'local'
# set interfaces ethernet eth3 firewall 'out'

# Using rendered
#
#
- name: Render the commands for provided  configuration
  vyos.vyos.vyos_firewall_interfaces:
    config:
    - name: eth2
      access_rules:
      - afi: ipv4
        rules:
        - direction: in
          name: INGRESS
        - direction: out
          name: OUTGRESS
        - direction: local
          name: DROP
    state: rendered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "rendered": [
#        "set interfaces ethernet eth2 firewall in name 'INGRESS'",
#        "set interfaces ethernet eth2 firewall out name 'OUTGRESS'",
#        "set interfaces ethernet eth2 firewall local name 'DROP'",
#        "set interfaces ethernet eth2 firewall local ipv6-name 'LOCAL'"
#    ]
```

## [Return Values](vyos_firewall_interfaces_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["set interfaces ethernet eth1 firewall local ipv6-name 'V6-LOCAL'", "set interfaces ethernet eth3 firewall in name 'INBOUND'"]` |

### Authors

- Rohit Thakur (@rohitthakur2590)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)
