---
collection: ansible
version: "6"
title: "cisco.nxos.nxos_lldp_global module – LLDP resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nxos/nxos_lldp_global_module.html
fetched_at: 2026-07-27T17:02:03+00:00
---
# cisco.nxos.nxos_lldp_global module – LLDP resource module

> **Note:**
>
> This module is part of the [cisco.nxos collection](https://galaxy.ansible.com/cisco/nxos) (version 3.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nxos`.
>
> To use it in a playbook, specify: `cisco.nxos.nxos_lldp_global`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_lldp_global_module.md#synopsis)
- [Parameters](nxos_lldp_global_module.md#parameters)
- [Notes](nxos_lldp_global_module.md#notes)
- [Examples](nxos_lldp_global_module.md#examples)
- [Return Values](nxos_lldp_global_module.md#return-values)

## [Synopsis](nxos_lldp_global_module.md#id1)

- This module configures and manages the Link Layer Discovery Protocol(LLDP) attributes on NX-OS platforms.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](nxos_lldp_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A list of link layer discovery configurations |
| **holdtime**  integer | Amount of time the receiving device should hold the information (in seconds) |
| **port_id**  integer | This attribute defines if the interface names should be advertised in the long(0) or short(1) form.  Choices:   - `0` - `1` |
| **reinit**  integer | Amount of time to delay the initialization of LLDP on any interface (in seconds) |
| **timer**  integer | Frequency at which LLDP updates need to be transmitted (in seconds) |
| **tlv_select**  dictionary | This attribute can be used to specify the TLVs that need to be sent and received in the LLDP packets. By default, all TLVs are advertised |
| **dcbxp**  boolean | Used to specify the Data Center Bridging Exchange Protocol TLV  Choices:   - `false` - `true` |
| **management_address**  dictionary | Used to specify the management address in TLV messages |
| **v4**  boolean | Management address with TLV v4  Choices:   - `false` - `true` |
| **v6**  boolean | Management address with TLV v6  Choices:   - `false` - `true` |
| **port**  dictionary | Used to manage port based attributes in TLV messages |
| **description**  boolean | Used to specify the port description TLV  Choices:   - `false` - `true` |
| **vlan**  boolean | Used to specify the port VLAN ID TLV  Choices:   - `false` - `true` |
| **power_management**  boolean | Used to specify IEEE 802.3 DTE Power via MDI TLV  Choices:   - `false` - `true` |
| **system**  dictionary | Used to manage system based attributes in TLV messages |
| **capabilities**  boolean | Used to specify the system capabilities TLV  Choices:   - `false` - `true` |
| **description**  boolean | Used to specify the system description TLV  Choices:   - `false` - `true` |
| **name**  boolean | Used to specify the system name TLV  Choices:   - `false` - `true` |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the NX-OS device by executing the command **show running-config | include lldp**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state of the configuration after module completion  Choices:   - `"merged"` ← (default) - `"replaced"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](nxos_lldp_global_module.md#id3)

> **Note:**
>
> - Tested against NxOS 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - The LLDP feature needs to be enabled before using this module

## [Examples](nxos_lldp_global_module.md#id4)

```yaml+jinja
# Using merged
# Before state:
# -------------
#
# user(config)# show running-config | include lldp
# feature lldp

- name: Merge provided configuration with device configuration
  cisco.nxos.nxos_lldp_global:
    config:
      timer: 35
      holdtime: 100
    state: merged

# After state:
# ------------
#
# user(config)# show running-config | include lldp
# feature lldp
# lldp timer 35
# lldp holdtime 100

# Using replaced
# Before state:
# -------------
#
# user(config)# show running-config | include lldp
# feature lldp
# lldp holdtime 100
# lldp reinit 5
# lldp timer 35

- name: Replace device configuration of specific LLDP attributes with provided configuration
  cisco.nxos.nxos_lldp_global:
    config:
      timer: 40
      tlv_select:
        system:
          description: true
          name: false
        management_address:
          v4: true
    state: replaced

# After state:
# ------------
#
# user(config)# show running-config | include lldp
# feature lldp
# lldp timer 40
# no lldp tlv-select system-name

# Using deleted
# Before state:
# -------------
#
# user(config)# show running-config | include lldp
# feature lldp
# lldp holdtime 5
# lldp reinit 3

- name: Delete LLDP configuration (this will by default remove all lldp configuration)
  cisco.nxos.nxos_lldp_global:
    state: deleted

# After state:
# ------------
#
# user(config)# show running-config | include lldp
# feature lldp

# Using rendered

- name: Use rendered state to convert task input to device specific commands
  cisco.nxos.nxos_lldp_global:
    config:
      holdtime: 130
      port_id: 1
      reinit: 5
      tlv_select:
        dcbxp: yes
        power_management: yes
    state: rendered

# Task Output (redacted)
# -----------------------

# rendered:
#   - "lldp tlv-select dcbxp"
#   - "lldp tlv-select power-management"
#   - "lldp portid-subtype 1"
#   - "lldp reinit 5"
#   - "lldp holdtime 130"

# Using parsed

# parsed.cfg
# ------------
# lldp holdtime 131
# lldp reinit 7
# no lldp tlv-select system-name
# no lldp tlv-select system-description

# Task output (redacted)
# -----------------------

# parsed:
#   holdtime: 131
#   reinit: 7
#   tlv_select:
#     system:
#       description: false
#       name: false

# Using gathered

# Existing device config state
# -------------------------------
# feature lldp
# lldp holdtime 129
# lldp reinit 5
# lldp timer 35
# no lldp tlv-select system-name

# Task output (redacted)
# -----------------------

# gathered:
#   reinit: 5
#   timer: 35
#   tlv_select:
#     system:
#       name: False
#   holdtime: 129
```

## [Return Values](nxos_lldp_global_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The configuration as structured data after module completion.  Returned: when changed  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration as structured data prior to module invocation.  Returned: always  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["lldp holdtime 125", "lldp reinit 4", "no lldp tlv-select system-name"]` |

### Authors

- Adharsh Srivats Rangarajan (@adharshsrivatsr)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
