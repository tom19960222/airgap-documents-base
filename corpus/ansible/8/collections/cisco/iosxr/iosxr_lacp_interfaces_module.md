---
collection: ansible
version: "8"
title: "cisco.iosxr.iosxr_lacp_interfaces module – Resource module to configure LACP interfaces."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/iosxr/iosxr_lacp_interfaces_module.html
fetched_at: 2026-07-28T01:26:46+00:00
---
# cisco.iosxr.iosxr_lacp_interfaces module – Resource module to configure LACP interfaces.

> **Note:**
>
> This module is part of the [cisco.iosxr collection](https://galaxy.ansible.com/ui/repo/published/cisco/iosxr/) (version 5.0.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.iosxr`.
>
> To use it in a playbook, specify: `cisco.iosxr.iosxr_lacp_interfaces`.

New in cisco.iosxr 1.0.0

- [Synopsis](iosxr_lacp_interfaces_module.md#synopsis)
- [Parameters](iosxr_lacp_interfaces_module.md#parameters)
- [Notes](iosxr_lacp_interfaces_module.md#notes)
- [Examples](iosxr_lacp_interfaces_module.md#examples)
- [Return Values](iosxr_lacp_interfaces_module.md#return-values)

## [Synopsis](iosxr_lacp_interfaces_module.md#id1)

- This module manages Link Aggregation Control Protocol (LACP) attributes of interfaces on IOS-XR devices.

Aliases: lacp_interfaces

## [Parameters](iosxr_lacp_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of LACP interfaces options. |
| **churn_logging**  string | Specifies the parameter for logging of LACP churn events.  Valid only for ether-bundles.  Mode ‘actor’ logs actor churn events only.  Mode ‘partner’ logs partner churn events only.  Mode ‘both’ logs actor and partner churn events only.  **Choices:**   - `"actor"` - `"partner"` - `"both"` |
| **collector_max_delay**  integer | Specifies the collector max delay to be signaled to the LACP partner.  Valid only for ether-bundles.  Refer to vendor documentation for valid values. |
| **name**  string | Name/Identifier of the interface or Ether-Bundle. |
| **period**  integer | Specifies the rate at which packets are sent or received.  For ether-bundles, this specifies the period to be used by its member links.  Refer to vendor documentation for valid values. |
| **switchover_suppress_flaps**  integer | Specifies the time for which to suppress flaps during a LACP switchover.  Valid only for ether-bundles.  Refer to vendor documentation for valid values. |
| **system**  dictionary | This dict object contains configurable options related to LACP system parameters for ether-bundles. |
| **mac**  string | Specifies the system ID to use in LACP negotiations for the bundle, encoded as a MAC address. |
| **priority**  integer | Specifies the system priority to use in LACP negotiations for the bundle.  Refer to vendor documentation for valid values. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS-XR device by executing the command **show running-config int**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state of the configuration after module completion.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"parsed"` - `"gathered"` - `"rendered"` |

## [Notes](iosxr_lacp_interfaces_module.md#id3)

> **Note:**
>
> - This module works with connection `network_cli`. See [the IOS-XR Platform Options](../network/user_guide/platform_iosxr.md).

## [Examples](iosxr_lacp_interfaces_module.md#id4)

```yaml+jinja
# Using merged
#
#
# ------------
# Before state
# ------------
#
#
#
# RP/0/0/CPU0:an-iosxr#sh running-config interface
# Sun Jul 21 18:01:35.079 UTC
# interface Bundle-Ether10
# !
# interface Bundle-Ether11
# !
# interface Bundle-Ether12
# !
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  description 'GigabitEthernet - 1'
# !
# interface GigabitEthernet0/0/0/2
#  description "GigabitEthernet - 2"
# !
# interface GigabitEthernet0/0/0/3
#  description "GigabitEthernet - 3"
# !
# interface GigabitEthernet0/0/0/4
#  description "GigabitEthernet - 4"
# !
#
#

- name: Merge provided configuration with device configuration
  cisco.iosxr.iosxr_lacp_interfaces:
    config:
    - name: Bundle-Ether10
      churn_logging: actor
      collector_max_delay: 100
      switchover_suppress_flaps: 500

    - name: Bundle-Ether11
      system:
        mac: 00c2.4c00.bd15

    - name: GigabitEthernet0/0/0/1
      period: 200
    state: merged

#
#
# -----------
# After state
# -----------
#
#
# RP/0/0/CPU0:an-iosxr#sh run int
# Sun Jul 21 18:24:52.413 UTC
# interface Bundle-Ether10
#  lacp churn logging actor
#  lacp switchover suppress-flaps 500
#  lacp collector-max-delay 100
# !
# interface Bundle-Ether11
#  lacp system mac 00c2.4c00.bd15
# !
# interface Bundle-Ether12
# !
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  description 'GigabitEthernet - 1"
#  lacp period 200
# !
# interface GigabitEthernet0/0/0/2
#  description "GigabitEthernet - 2"
# !
# interface GigabitEthernet0/0/0/3
#  description "GigabitEthernet - 3"
# !
# interface GigabitEthernet0/0/0/4
#  description "GigabitEthernet - 4"
# !
#

# Using replaced
#
#
# ------------
# Before state
# ------------
#
#
# RP/0/0/CPU0:an-iosxr#sh run int
# Sun Jul 21 18:24:52.413 UTC
# interface Bundle-Ether10
#  lacp churn logging actor
#  lacp switchover suppress-flaps 500
#  lacp collector-max-delay 100
# !
# interface Bundle-Ether11
#  lacp system mac 00c2.4c00.bd15
# !
# interface Bundle-Ether12
# !
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  description 'GigabitEthernet - 1"
#  lacp period 200
# !
# interface GigabitEthernet0/0/0/2
#  description "GigabitEthernet - 2"
# !
# interface GigabitEthernet0/0/0/3
#  description "GigabitEthernet - 3"
# !
# interface GigabitEthernet0/0/0/4
#  description "GigabitEthernet - 4"
# !
#

- name: Replace LACP configuration of listed interfaces with provided configuration
  cisco.iosxr.iosxr_lacp_interfaces:
    config:
    - name: Bundle-Ether10
      churn_logging: partner

    - name: GigabitEthernet0/0/0/2
      period: 300
    state: replaced

#
#
# -----------
# After state
# -----------
#
#
# RP/0/0/CPU0:an-iosxr#sh run int
# Sun Jul 21 18:50:21.929 UTC
# interface Bundle-Ether10
#  lacp churn logging partner
# !
# interface Bundle-Ether11
#  lacp system mac 00c2.4c00.bd15
# !
# interface Bundle-Ether12
# !
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  description 'GigabitEthernet - 1"
#  lacp period 200
# !
# interface GigabitEthernet0/0/0/2
#  description "GigabitEthernet - 2"
#  lacp period 300
# !
# interface GigabitEthernet0/0/0/3
#  description "GigabitEthernet - 3"
# !
# interface GigabitEthernet0/0/0/4
#  description "GigabitEthernet - 4"
# !
#
#

# Using overridden
#
#
# ------------
# Before state
# ------------
#
#
# RP/0/0/CPU0:an-iosxr#sh run int
# Sun Jul 21 18:24:52.413 UTC
# interface Bundle-Ether10
#  lacp churn logging actor
#  lacp switchover suppress-flaps 500
#  lacp collector-max-delay 100
# !
# interface Bundle-Ether11
#  lacp system mac 00c2.4c00.bd15
# !
# interface Bundle-Ether12
# !
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  description 'GigabitEthernet - 1"
#  lacp period 200
# !
# interface GigabitEthernet0/0/0/2
#  description "GigabitEthernet - 2"
#  lacp period 200
# !
# interface GigabitEthernet0/0/0/3
#  description "GigabitEthernet - 3"
# !
# interface GigabitEthernet0/0/0/4
#  description "GigabitEthernet - 4"
# !
#
#

- name: Override all interface LACP configuration with provided configuration
  cisco.iosxr.iosxr_lacp_interfaces:
    config:
    - name: Bundle-Ether12
      churn_logging: both
      collector_max_delay: 100
      switchover_suppress_flaps: 500

    - name: GigabitEthernet0/0/0/1
      period: 300
    state: overridden

#
#
# -----------
# After state
# -----------
#
#
# RP/0/0/CPU0:an-iosxr(config-if)#do sh run int
# Sun Jul 21 19:32:36.115 UTC
# interface Bundle-Ether10
# !
# interface Bundle-Ether11
# !
# interface Bundle-Ether12
#  lacp churn logging both
#  lacp switchover suppress-flaps 500
#  lacp collector-max-delay 100
# !
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  description 'GigabitEthernet - 1"
#  lacp period 300
# !
# interface GigabitEthernet0/0/0/2
#  description "GigabitEthernet - 2"
# !
# interface GigabitEthernet0/0/0/3
#  description "GigabitEthernet - 3"
# !
# interface GigabitEthernet0/0/0/4
#  description "GigabitEthernet - 4"
# !
#

# Using deleted
#
#
# ------------
# Before state
# ------------
#
#
# RP/0/0/CPU0:an-iosxr#sh run int
# Sun Jul 21 18:24:52.413 UTC
# interface Bundle-Ether10
#  lacp churn logging actor
#  lacp switchover suppress-flaps 500
#  lacp collector-max-delay 100
# !
# interface Bundle-Ether11
#  lacp non-revertive
# !
# interface Bundle-Ether12
# !
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  description 'GigabitEthernet - 1"
#  lacp period 200
# !
# interface GigabitEthernet0/0/0/2
#  description "GigabitEthernet - 2"
#   lacp period 300
# !
# interface GigabitEthernet0/0/0/3
#  description "GigabitEthernet - 3"
# !
# interface GigabitEthernet0/0/0/4
#  description "GigabitEthernet - 4"
# !
#

- name: Deleted LACP configurations of provided interfaces (Note - This won't delete
    the interface itself)
  cisco.iosxr.iosxr_lacp_interfaces:
    config:
    - name: Bundle-Ether10
    - name: Bundle-Ether11
    - name: GigabitEthernet0/0/0/1
    - name: GigabitEthernet0/0/0/2
    state: deleted

#
#
# -----------
# After state
# -----------
#
#
# Using parsed:

# parsed.cfg
# interface Bundle-Ether10
#  lacp churn logging actor
#  lacp switchover suppress-flaps 500
#  lacp collector-max-delay 100
# !
# interface Bundle-Ether11
#  lacp system mac 00c2.4c00.bd15
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  lacp period 200
# !
#

- name: Convert lacp interfaces config to argspec without connecting to the appliance
  cisco.iosxr.iosxr_lacp_interfaces:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed

# --------------
# Output:
# --------------

#    parsed:
#      - name: Bundle-Ether10
#        churn_logging: actor
#        collector_max_delay: 100
#        switchover_suppress_flaps: 500
#
#      - name: Bundle-Ether11
#        system:
#          mac: 00c2.4c00.bd15
#
#      - name: GigabitEthernet0/0/0/1
#        period: 200
#
#

# Using gathered:

# Native config:
# interface Bundle-Ether10
#  lacp churn logging actor
#  lacp switchover suppress-flaps 500
#  lacp collector-max-delay 100
# !
# interface Bundle-Ether11
#  lacp system mac 00c2.4c00.bd15
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  lacp period 200
# !
#

- name: Gather IOSXR lacp interfaces configuration
  cisco.iosxr.iosxr_lacp_interfaces:
    config:
    state: gathered

# ----------
# Output
# ---------
#    gathered:
#      - name: Bundle-Ether10
#        churn_logging: actor
#        collector_max_delay: 100
#        switchover_suppress_flaps: 500
#
#      - name: Bundle-Ether11
#        system:
#          mac: 00c2.4c00.bd15
#
#      - name: GigabitEthernet0/0/0/1
#        period: 200

# Using rendered:

- name: Render platform specific commands from task input using rendered state
  cisco.iosxr.iosxr_lacp_interfaces:
    config:
    - name: Bundle-Ether10
      churn_logging: actor
      collector_max_delay: 100
      switchover_suppress_flaps: 500

    - name: Bundle-Ether11
      system:
        mac: 00c2.4c00.bd15

    - name: GigabitEthernet0/0/0/1
      period: 200
    state: rendered

# -------------
# Output
# -------------
# rendered: [
#     - "interface Bundle-Ether10"
#     - " lacp churn logging actor"
#     - " lacp switchover suppress-flaps 500"
#     - " lacp collector-max-delay 100"
#     - "interface Bundle-Ether11"
#     - " lacp system mac 00c2.4c00.bd15"
#     - "interface MgmtEth0/0/CPU0/0"
#     - " ipv4 address 192.0.2.11 255.255.255.0"
#     - "interface GigabitEthernet0/0/0/1"
#     - " lacp period 200"
#
```

## [Return Values](iosxr_lacp_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["interface Bundle-Ether10", "lacp churn logging partner", "lacp period 150"]` |

### Authors

- Nilashish Chakraborty (@nilashishc)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
