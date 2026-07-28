---
collection: ansible
version: "6"
title: "junipernetworks.junos.junos_lldp_global module – LLDP resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/junipernetworks/junos/junos_lldp_global_module.html
fetched_at: 2026-07-27T17:54:24+00:00
---
# junipernetworks.junos.junos_lldp_global module – LLDP resource module

> **Note:**
>
> This module is part of the [junipernetworks.junos collection](https://galaxy.ansible.com/junipernetworks/junos) (version 3.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install junipernetworks.junos`.
> You need further requirements to be able to use this module,
> see [Requirements](junos_lldp_global_module.md#ansible-collections-junipernetworks-junos-junos-lldp-global-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_lldp_global`.

New in junipernetworks.junos 1.0.0

- [Synopsis](junos_lldp_global_module.md#synopsis)
- [Requirements](junos_lldp_global_module.md#requirements)
- [Parameters](junos_lldp_global_module.md#parameters)
- [Notes](junos_lldp_global_module.md#notes)
- [Examples](junos_lldp_global_module.md#examples)
- [Return Values](junos_lldp_global_module.md#return-values)

## [Synopsis](junos_lldp_global_module.md#id1)

- This module manages link layer discovery protocol (LLDP) attributes on Juniper JUNOS devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](junos_lldp_global_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.6.4)

## [Parameters](junos_lldp_global_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | The list of link layer discovery protocol attribute configurations |
| **address**  string | This argument sets the management address from LLDP. |
| **enabled**  boolean | This argument is a boolean value to enabled or disable LLDP.  Choices:   - `false` - `true` |
| **hold_multiplier**  integer | Specify the number of seconds that LLDP information is held before it is discarded. The multiplier value is used in combination with the `interval` value. |
| **interval**  integer | Frequency at which LLDP advertisements are sent (in seconds). |
| **transmit_delay**  integer | Specify the number of seconds the device waits before sending advertisements to neighbors after a change is made in local system. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the Junos device by executing the command **show protocols lldp**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result |
| **state**  string | The state of the configuration after module completion.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](junos_lldp_global_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Tested against vSRX JUNOS version 18.4R1.
> - This module works with connection `netconf`. See [the Junos OS Platform Options](../network/user_guide/platform_junos.md).

## [Examples](junos_lldp_global_module.md#id5)

```yaml+jinja
# Using merged
# Before state:
# -------------
# user@junos01# # show protocols lldp
#
- name: Merge provided configuration with device configuration
  junipernetworks.junos.junos_lldp_global:
    config:
      interval: 10000
      address: 10.1.1.1
      transmit_delay: 400
      hold_multiplier: 10
    state: merged

# After state:
# -------------
# user@junos01# show protocols lldp
# management-address 10.1.1.1;
# advertisement-interval 10000;
# transmit-delay 400;
# hold-multiplier 10;

# Using replaced
# Before state:
# -------------
# user@junos01# show protocols lldp
# management-address 10.1.1.1;
# advertisement-interval 10000;
# transmit-delay 400;
# hold-multiplier 10;

- name: Replace provided configuration with device configuration
  junipernetworks.junos.junos_lldp_global:
    config:
      address: 20.2.2.2
      hold_multiplier: 30
      enabled: false
    state: replaced

# After state:
# -------------
# user@junos01# show protocols lldp
# disable;
# management-address 20.2.2.2;
# hold-multiplier 30;

# Using deleted
# Before state:
# -------------
# user@junos01# show protocols lldp
# management-address 20.2.2.2;
# hold-multiplier 30;

- name: Delete lldp configuration (this will by default remove all lldp configuration)
  junipernetworks.junos.junos_lldp_global:
    state: deleted

# After state:
# -------------
# user@junos01# # show protocols lldp
#
#
# Using gathered
# Before state:
# ------------
#
# ansible@cm123456tr21# show protocols lldp
# management-address 10.1.1.1;
# advertisement-interval 10000;
# transmit-delay 400;
# hold-multiplier 10;
# interface ge-0/0/1;
# interface ge-0/0/2 {
#     disable;
# }
- name: Gather junos lldp_global as in given arguments
  junipernetworks.junos.junos_lldp_global:
    state: gathered
# Task Output (redacted)
# -----------------------
#
# "gathered": {
#         "address": "10.1.1.1",
#         "hold_multiplier": 10,
#         "interval": 10000,
#         "transmit_delay": 400
#     }
# After state:
# ------------
#
# ansible@cm123456tr21# show protocols lldp
# management-address 10.1.1.1;
# advertisement-interval 10000;
# transmit-delay 400;
# hold-multiplier 10;
# interface ge-0/0/1;
# interface ge-0/0/2 {
#     disable;
# }
# Using rendered
- name: Render platform specific xml from task input using rendered state
  junipernetworks.junos.junos_lldp_global:
    config:
      interval: 10000
      address: 10.1.1.1
      transmit_delay: 400
      hold_multiplier: 10
    state: rendered
# Task Output (redacted)
# -----------------------
# "rendered": "<nc:protocols
#     xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#     <nc:lldp>
#         <nc:management-address>10.1.1.1</nc:management-address>
#         <nc:advertisement-interval>10000</nc:advertisement-interval>
#         <nc:transmit-delay>400</nc:transmit-delay>
#         <nc:hold-multiplier>10</nc:hold-multiplier>
#         <nc:disable delete="delete"/>
#     </nc:lldp>
# </nc:protocols>"
#
# parsed.cfg
# ------------
#
# <?xml version="1.0" encoding="UTF-8"?>
# <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
#     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
#         <protocols>
#             <ospf>
#                 <area>
#                     <name>0.0.0.0</name>
#                     <interface>
#                         <name>ge-0/0/0.0</name>
#                     </interface>
#                 </area>
#             </ospf>
#             <lldp>
#                 <management-address>10.1.1.1</management-address>
#                 <advertisement-interval>10000</advertisement-interval>
#                 <transmit-delay>400</transmit-delay>
#                 <hold-multiplier>10</hold-multiplier>
#                 <interface>
#                     <name>ge-0/0/1</name>
#                 </interface>
#                 <interface>
#                     <name>ge-0/0/2</name>
#                     <disable/>
#                 </interface>
#             </lldp>
#         </protocols>
#     </configuration>
# </rpc-reply>
# - name: Convert lldp global config to argspec without connecting to the appliance
#   junipernetworks.junos.junos_lldp_global:
#     running_config: "{{ lookup('file', './parsed.cfg') }}"
#     state: parsed
# Task Output (redacted)
# -----------------------
# "parsed": {
#         "address": "10.1.1.1",
#         "hold_multiplier": 10,
#         "interval": 10000,
#         "transmit_delay": 400
#     }
```

## [Return Values](junos_lldp_global_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The configuration as structured data after module completion.  Returned: when changed  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration as structured data prior to module invocation.  Returned: always  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["<nc:protocols xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\"> <nc:lldp> <nc:management-address>10.1.1.1</nc:management-address> <nc:advertisement-interval>10000</nc:advertisement-interval> <nc:transmit-delay>400</nc:transmit-delay> <nc:hold-multiplier>10</nc:hold-multiplier> <nc:disable delete=\"delete\"/> </nc:lldp> </nc:protocols>", "xml 2", "xml 3"]` |

### Authors

- Ganesh Nalawade (@ganeshrn)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
[Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
