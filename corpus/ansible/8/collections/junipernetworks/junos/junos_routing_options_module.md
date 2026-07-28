---
collection: ansible
version: "8"
title: "junipernetworks.junos.junos_routing_options module – Manage routing-options configuration on Junos devices."
source_url: https://docs.ansible.com/projects/ansible/8/collections/junipernetworks/junos/junos_routing_options_module.html
fetched_at: 2026-07-28T02:39:52+00:00
---
# junipernetworks.junos.junos_routing_options module – Manage routing-options configuration on Junos devices.

> **Note:**
>
> This module is part of the [junipernetworks.junos collection](https://galaxy.ansible.com/ui/repo/published/junipernetworks/junos/) (version 5.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install junipernetworks.junos`.
> You need further requirements to be able to use this module,
> see [Requirements](junos_routing_options_module.md#ansible-collections-junipernetworks-junos-junos-routing-options-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_routing_options`.

New in junipernetworks.junos 2.8.0

- [Synopsis](junos_routing_options_module.md#synopsis)
- [Requirements](junos_routing_options_module.md#requirements)
- [Parameters](junos_routing_options_module.md#parameters)
- [Notes](junos_routing_options_module.md#notes)
- [Examples](junos_routing_options_module.md#examples)
- [Return Values](junos_routing_options_module.md#return-values)

## [Synopsis](junos_routing_options_module.md#id1)

- This module manages routing-options configuration on devices running Junos.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: routing_options

## [Requirements](junos_routing_options_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.6.4)
- xmltodict (>=0.12.0)

## [Parameters](junos_routing_options_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dictionary of routing-options configuration. |
| **autonomous_system**  dictionary | Specify Autonomous system number. |
| **as_number**  string / required | Specify Autonomous system number. |
| **asdot_notation**  boolean | Enable AS-Dot notation to display true 4 byte AS numbers.  **Choices:**   - `false` - `true` |
| **loops**  integer | Specify maximum number of times this AS can be in an AS path. |
| **router_id**  string | Specify Router identifier. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the Junos device by executing the command **show system routing-options**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  Refer to examples for more details.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"deleted"` - `"overridden"` - `"parsed"` - `"gathered"` - `"rendered"` |

## [Notes](junos_routing_options_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the device being managed.
> - This module works with connection `netconf`.
> - See [the Junos OS Platform Options](https://docs.ansible.com/ansible/latest/network/user_guide/platform_junos.html).
> - Tested against JunOS v18.4R1

## [Examples](junos_routing_options_module.md#id5)

```yaml+jinja
# Using merged
#
# Before state
# ------------
#
# vagrant@vsrx# show system routing-options
#
- name: Merge provided NTP configuration into running configuration.
  junipernetworks.junos.junos_routing_options:
    config:
      autonomous_system:
        as_number: 2
        asdot_notation: true
    state: merged
#
# -------------------------
# Module Execution Result
# -------------------------
#     "after": {
#         "autonomous_system": {
#             "as_number": "2",
#             "asdot_notation": true
#         }
#     },
#     "before": {},
#     "changed": true,
#     "commands": [
#           "<nc:routing-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
#           "<nc:autonomous-system>2<nc:asdot-notation/></nc:autonomous-system></nc:routing-options>"
#     ]
# After state
# -----------
#
# vagrant@vsrx# show routing-options
# autonomous-system 2 asdot-notation;
#
#
# Using Replaced
# Before state
# ------------
#
# vagrant@vsrx# show routing-options
# autonomous-system 2 asdot-notation;

- name: Replaced running routing-options configuration with provided configuration
  junipernetworks.junos.junos_routing_options:
    config:
      autonomous_system:
        as_number: 2
        asdot_notation: true
      router_id: "1.1.1.1"
    state: replaced
#
# -------------------------
# Module Execution Result
# -------------------------
#     "after": {
#         "autonomous_system": {
#             "as_number": "2",
#             "asdot_notation": true
#         },
#         "router_id": "1.1.1.1"
#     },
#     "before": {
#         "autonomous_system": {
#             "as_number": "2",
#             "asdot_notation": true
#         }
#     },
#     "changed": true,
#     "commands": [
#             "<nc:routing-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
#             "<nc:autonomous-system delete="delete"/><nc:autonomous-system>2<nc:asdot-notation/>"
#             "</nc:autonomous-system><nc:router-id>1.1.1.1</nc:router-id></nc:routing-options>"
#     ]
# After state
# -----------
#
# vagrant@vsrx# show routing-options
# router-id 1.1.1.1;
# autonomous-system 2 asdot-notation;

# Using overridden
#
# vagrant@vsrx# show routing-options
# autonomous-system 2 asdot-notation;

- name: Override running routing-options configuration with provided configuration
  junipernetworks.junos.junos_routing_options:
    config:
      autonomous_system:
        as_number: 2
        asdot_notation: true
      router_id: "1.1.1.1"
    state: overridden
#
# -------------------------
# Module Execution Result
# -------------------------
#     "after": {
#         "autonomous_system": {
#             "as_number": "2",
#             "asdot_notation": true
#         },
#         "router_id": "1.1.1.1"
#     },
#     "before": {
#         "autonomous_system": {
#             "as_number": "2",
#             "asdot_notation": true
#         }
#     },
#     "changed": true,
#     "commands": [
#             "<nc:routing-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
#             "<nc:autonomous-system delete="delete"/><nc:autonomous-system>2<nc:asdot-notation/>"
#             "</nc:autonomous-system><nc:router-id>1.1.1.1</nc:router-id></nc:routing-options>"
#     ]
# After state
# -----------
#
# vagrant@vsrx# show routing-options
# router-id 1.1.1.1;
# autonomous-system 2 asdot-notation;
#
# Using deleted
#
# Before state
# ------------
#
# vagrant@vsrx# show routing-options
# router-id 1.1.1.1;
# autonomous-system 2 asdot-notation;
#
- name: Delete running routing-options configuration
  junipernetworks.junos.junos_routing_options:
    config:
    state: deleted
#
# -------------------------
# Module Execution Result
# -------------------------
#     "after": {},
#     "before": {
#         "autonomous_system": {
#             "as_number": "2",
#             "asdot_notation": true
#         },
#         "router_id": "1.1.1.1"
#     },
#     "changed": true,
#     "commands": [
#               "<nc:routing-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
#               "<nc:autonomous-system delete="delete"/><nc:router-id delete="delete"/></nc:routing-options>"
#     ]
# After state
# -----------
#
# vagrant@vsrx# show routing-options
#
# [edit]
# Using gathered
#
# Before state
# ------------
#
# vagrant@vsrx# show routing-options
# router-id 1.1.1.1;
# autonomous-system 2 asdot-notation;

- name: Gather running routing-options configuration
  junipernetworks.junos.junos_routing_options:
    state: gathered
#
# -------------------------
# Module Execution Result
# -------------------------
#     "gathered": {
#         "autonomous_system": {
#             "as_number": "2",
#             "asdot_notation": true
#         },
#         "router_id": "1.1.1.1"
#     },
#     "changed": false,
# Using rendered
#
# Before state
# ------------
#
- name: Render xml for provided facts.
  junipernetworks.junos.junos_routing_options:
    config:
      autonomous_system:
        as_number: 2
        asdot_notation: true
        loops: 4
      router_id: 12.12.12.12
    state: rendered
#
# -------------------------
# Module Execution Result
# -------------------------
#     "rendered": [
#           "<nc:routing-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#           "<nc:autonomous-system>2<nc:loops>4</nc:loops><nc:asdot-notation/></nc:autonomous-system>
#           "<nc:router-id>12.12.12.12</nc:router-id></nc:routing-options>"
#     ]
#
# Using parsed
# parsed.cfg
# ------------
# <?xml version="1.0" encoding="UTF-8"?>
# <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
#     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
#         <version>18.4R1-S2.4</version>
#         <routing-options>
#             <router-id>12.12.12.12</router-id>
#             <autonomous-system>
#                 <as-number>2</as-number>
#                 <loops>4</loops>
#                 <asdot-notation/>
#             </autonomous-system>
#         </routing-options>
#     </configuration>
# </rpc-reply>
#
- name: Parse routing-options running config
  junipernetworks.junos.junos_routing_options:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "parsed":  {
#         "autonomous_system": {
#             "as_number": "2",
#             "asdot_notation": true,
#             "loops": 4
#         },
#         "router_id": "12.12.12.12"
#     }
#
```

## [Return Values](junos_routing_options_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["<nc:autonomous-system delete=\"delete\"/><nc:router-id delete=\"delete\"/></nc:routing-options>"]` |

### Authors

- Rohit Thakur (@rohitthakur2590)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
