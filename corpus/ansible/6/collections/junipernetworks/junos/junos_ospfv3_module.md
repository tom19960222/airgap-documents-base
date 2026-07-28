---
collection: ansible
version: "6"
title: "junipernetworks.junos.junos_ospfv3 module – OSPFv3 resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/junipernetworks/junos/junos_ospfv3_module.html
fetched_at: 2026-07-27T17:54:31+00:00
---
# junipernetworks.junos.junos_ospfv3 module – OSPFv3 resource module

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
> see [Requirements](junos_ospfv3_module.md#ansible-collections-junipernetworks-junos-junos-ospfv3-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_ospfv3`.

New in junipernetworks.junos 1.2.0

- [Synopsis](junos_ospfv3_module.md#synopsis)
- [Requirements](junos_ospfv3_module.md#requirements)
- [Parameters](junos_ospfv3_module.md#parameters)
- [Notes](junos_ospfv3_module.md#notes)
- [Examples](junos_ospfv3_module.md#examples)
- [Return Values](junos_ospfv3_module.md#return-values)

## [Synopsis](junos_ospfv3_module.md#id1)

- This module manages global OSPFv3 configuration on devices running Juniper JUNOS.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](junos_ospfv3_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.6.4)
- xmltodict (>=0.12.0)

## [Parameters](junos_ospfv3_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of OSPFv3 process configuration. |
| **areas**  list / elements=dictionary | A list of OSPFv3 areas’ configuration. |
| **area_id**  string / required | The Area ID as an integer or IP Address. |
| **area_range**  string | Configure an address range for the area. |
| **interfaces**  list / elements=dictionary | List of interfaces in this area. |
| **authentication**  dictionary | Specify authentication type |
| **type**  dictionary | Type of authentication to use. |
| **bandwidth_based_metrics**  list / elements=dictionary | Specify list of bandwidth based metrics |
| **bandwidth**  string | BW to apply metric to.  Choices:   - `"1g"` - `"10g"` |
| **metric**  integer | Specify metric |
| **flood_reduction**  boolean | Enable flood reduction.  Choices:   - `false` - `true` |
| **metric**  integer | Metric applied to the interface. |
| **name**  string / required | Name of the interface. |
| **passive**  boolean | Specify passive  Choices:   - `false` - `true` |
| **priority**  integer | Priority for the interface. |
| **timers**  dictionary | Specify timers |
| **dead_interval**  integer | Dead interval (seconds). |
| **hello_interval**  integer | Hello interval (seconds). |
| **poll_interval**  integer | Poll interval (seconds). |
| **retransmit_interval**  integer | Retransmit interval (seconds). |
| **transit_delay**  integer | Transit delay (seconds). |
| **stub**  dictionary | Settings for configuring the area as a stub. |
| **default_metric**  integer | Metric for the default route in this area. |
| **set**  boolean | Configure the area as a stub.  Choices:   - `false` - `true` |
| **external_preference**  integer | Preference of external routes. |
| **overload**  dictionary | Specify time for overload mode reset |
| **timeout**  integer | Time after which overload mode is reset (seconds). |
| **preference**  integer | Preference of internal routes. |
| **prefix_export_limit**  integer | Maximum number of external prefixes that can be exported. |
| **reference_bandwidth**  string | Bandwidth for calculating metric defaults.  Choices:   - `"1g"` - `"10g"` |
| **rfc1583compatibility**  boolean | Set RFC1583 compatibility  Choices:   - `false` - `true` |
| **router_id**  string | The OSPFv3 router id. |
| **spf_options**  dictionary | Configure options for SPF. |
| **delay**  integer | Time to wait before running an SPF (seconds). |
| **holddown**  integer | Time to hold down before running an SPF (seconds). |
| **rapid_runs**  integer | Number of maximum rapid SPF runs before holddown (seconds). |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the Junos device by executing the command **ERROR while parsing**: While parsing B() at index 103: Cannot find closing “)” after last parameter  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result |
| **state**  string | The state the configuration should be left in.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](junos_ospfv3_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the device being managed.
> - This module works with connection `netconf`. See [the Junos OS Platform Options](../network/user_guide/platform_junos.md).
> - Tested against JunOS v18.4R1

## [Examples](junos_ospfv3_module.md#id5)

```yaml+jinja
# Using merged
#
# Before state
# ------------
#
# admin# show protocols ospf3

- name: Merge Junos OSPFv3 config
  junipernetworks.junos.junos_ospfv3:
    config:
    - areas:
        - area_id: 0.0.0.100
          stub:
            default_metric: 200
            set: true
          interfaces:
            - name: so-0/0/0.0
              priority: 3
              metric: 5
    state: merged

# After state
# -----------
#
# adimn# show protocols ospf3
# area 0.0.0.100 {
#     stub default-metric 200;
#     interface so-0/0/0.0 {
#         metric 5;
#         priority 3;
#     }
# }
# Using replaced
#
# Before state
# ------------
#
# adimn# show protocols ospf3
# area 0.0.0.100 {
#     stub default-metric 200;
#     interface so-0/0/0.0 {
#         metric 5;
#         priority 3;
#     }
# }
- name: Replace Junos OSPFv3 config
  junipernetworks.junos.junos_ospfv3:
   config:
     - areas:
         - area_id: 0.0.0.100
           interfaces:
             - name: so-0/0/0.0
   state: replaced

# After state
# -----------
#
# admin# show protocols ospf3
# area 0.0.0.100 {
#     interface so-0/0/0.0;
# }
# Using overridden
#
# Before state
# ------------
#
# admin# show protocols ospf3
# area 0.0.0.100 {
#     interface so-0/0/0.0;
# }
- name: Override Junos OSPFv3 config
  junipernetworks.junos.junos_ospfv3:
  config:
    - areas:
        - area_id: 0.0.0.100
          stub:
            default_metric: 200
            set: true
          interfaces:
            - name: so-0/0/0.0
              priority: 3
              metric: 5
              flood_reduction: true
              passive: true
        - area_id: 0.0.0.200
          interfaces:
            - name: ge-1/1/0.0
            - name: ge-2/2/0.0
  state: overridden

# After state
# -----------
#
# admin# show protocols ospf3
# area 0.0.0.100 {
#     stub default-metric 200;
#     interface so-0/0/0.0 {
#         passive;
#         metric 5;
#         priority 3;
#         flood-reduction;
#     }
# }
# area 0.0.0.200 {
#     interface ge-1/1/0.0;
#     interface ge-2/2/0.0;
# }
#
# Using deleted
#
# Before state
# ------------
#
# adimn# show protocols ospf3
# area 0.0.0.100 {
#     stub default-metric 200;
#     interface so-0/0/0.0 {
#         metric 5;
#         priority 3;
#     }
# }

- name: Delete Junos OSPFv3 config
  junipernetworks.junos.junos_ospfv3:
    config:
      - areas:
          - area_id: 0.0.0.100
            interfaces:
              - name: so-0/0/0.0
    state: deleted

# After state
# -----------
#
# admin# show protocols ospf3
# Using gathered
#
# Before state
# ------------
#
# adimn# show protocols ospf3
# area 0.0.0.100 {
#     stub default-metric 200;
#     interface so-0/0/0.0 {
#         passive;
#         metric 5;
#         priority 3;
#         flood-reduction;
#     }
# }
# area 0.0.0.200 {
#     interface ge-1/1/0.0;
#     interface ge-2/2/0.0;
# }

- name: Gather Junos OSPFv3 config
  junipernetworks.junos.junos_ospfv3:
    config:
    state: gathered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "gathered": {
#             "areas": [
#                 {
#                     "area_id": "0.0.0.100",
#                     "interfaces": [
#                         {
#                             "flood_reduction": true,
#                             "metric": 5,
#                             "name": "so-0/0/0.0",
#                             "passive": true,
#                             "priority": 3
#                         }
#                     ],
#                     "stub": {
#                         "default_metric": 200,
#                         "set": true
#                     }
#                 },
#                 {
#                     "area_id": "0.0.0.200",
#                     "interfaces": [
#                         {
#                             "name": "ge-1/1/0.0"
#                         },
#                         {
#                             "name": "ge-2/2/0.0"
#                         }
#                     ]
#                 }
#             ],
#         }
#
# Using rendered
#
#
- name: Render the commands for provided  configuration
  junipernetworks.junos.junos_ospfv3:
    config:
    - areas:
        - area_id: 0.0.0.100
          stub:
            default_metric: 200
            set: true
          interfaces:
            - name: so-0/0/0.0
              priority: 3
              metric: 5
              flood_reduction: true
              passive: true
        - area_id: 0.0.0.200
          interfaces:
            - name: ge-1/1/0.0
            - name: ge-2/2/0.0
    state: rendered

#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "rendered": "
# <nc:protocols
#     xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#     <nc:ospf3>
#         <nc:area>
#             <nc:name>0.0.0.100</nc:name>
#             <nc:interface>
#                 <nc:name>so-0/0/0.0</nc:name>
#                 <nc:priority>3</nc:priority>
#                 <nc:flood-reduction/>
#                 <nc:metric>5</nc:metric>
#                 <nc:passive/>
#             </nc:interface>
#             <nc:stub>
#                 <nc:default-metric>200</nc:default-metric>
#             </nc:stub>
#         </nc:area>
#         <nc:area>
#             <nc:name>0.0.0.200</nc:name>
#             <nc:interface>
#                 <nc:name>ge-1/1/0.0</nc:name>
#             </nc:interface>
#             <nc:interface>
#                 <nc:name>ge-2/2/0.0</nc:name>
#             </nc:interface>
#         </nc:area>
#     </nc:ospf3>
# </nc:protocols>"
#
# Using parsed
# parsed.cfg
# ------------
# <rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:junos="http://xml.juniper.net/junos/18.4R1/junos">
# <data>
# <configuration xmlns="http://xml.juniper.net/xnm/1.1/xnm"
#      junos:commit-seconds="1601355317" junos:commit-localtime="2020-09-29 04:55:17 UTC" junos:commit-user="rohit">
#     <version>18.4R1-S2.4</version>
#     <interfaces>
#         <interface>
#             <name>ge-0/0/0</name>
#             <description>Configured by Ansi-Team</description>
#         </interface>
#         <interface>
#             <name>gr-0/0/0</name>
#             <description>Configured Manually</description>
#         </interface>
#         <interface>
#             <name>fxp0</name>
#             <unit>
#                 <name>0</name>
#                 <family>
#                     <inet>
#                         <dhcp>
#                         </dhcp>
#                     </inet>
#                 </family>
#             </unit>
#         </interface>
#     </interfaces>
#     <protocols>
#         <ospf3>
#             <area>
#                 <name>0.0.0.100</name>
#                 <stub>
#                     <default-metric>200</default-metric>
#                 </stub>
#                 <interface>
#                     <name>so-0/0/0.0</name>
#                     <passive>
#                     </passive>
#                     <metric>5</metric>
#                     <priority>3</priority>
#                     <flood-reduction/>
#                 </interface>
#             </area>
#             <area>
#                 <name>0.0.0.200</name>
#                 <interface>
#                     <name>ge-1/1/0.0</name>
#                 </interface>
#                 <interface>
#                     <name>ge-2/2/0.0</name>
#                 </interface>
#             </area>
#         </ospf3>
#     </protocols>
#     <routing-options>
#         <router-id>10.200.16.75</router-id>
#     </routing-options>
# </configuration>
# <database-status-information>
# <database-status>
# <user>rohit</user>
# <terminal>pts/0</terminal>
# <pid>38210</pid>
# <start-time junos:seconds="1601354977">2020-09-29 04:49:37 UTC</start-time>
# <idle-time junos:seconds="546">00:09:06</idle-time>
# <edit-path>[edit]</edit-path>
# </database-status>
# </database-status-information>
# </data>
# </rpc-reply>

- name: Parsed the device configuration to get output commands
  junipernetworks.junos.junos_ospfv3:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "parsed": [
#         {
#             "areas": [
#                 {
#                     "area_id": "0.0.0.100",
#                     "interfaces": [
#                         {
#                             "flood_reduction": true,
#                             "metric": 5,
#                             "name": "so-0/0/0.0",
#                             "passive": true,
#                             "priority": 3
#                         }
#                     ],
#                     "stub": {
#                         "default_metric": 200,
#                         "set": true
#                     }
#                 },
#                 {
#                     "area_id": "0.0.0.200",
#                     "interfaces": [
#                         {
#                             "name": "ge-1/1/0.0"
#                         },
#                         {
#                             "name": "ge-2/2/0.0"
#                         }
#                     ]
#                 }
#             ],
#         }
#     ]
#
```

## [Return Values](junos_ospfv3_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration model invocation.  Returned: when changed  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration prior to the model invocation.  Returned: always  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["<nc:protocols xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\"> <nc:ospf3 delete=\"delete\"/> <nc:ospf3> <nc:area> <nc:name>0.0.0.100</nc:name> <nc:interface> <nc:name>so-0/0/0.0</nc:name> <nc:priority>3</nc:priority> <nc:flood-reduction/> <nc:metric>5</nc:metric> <nc:passive/> </nc:interface> <nc:stub> <nc:default-metric>200</nc:default-metric> </nc:stub> </nc:area> <nc:area> <nc:name>0.0.0.200</nc:name> <nc:interface> <nc:name>ge-1/1/0.0</nc:name> </nc:interface> <nc:interface> <nc:name>ge-2/2/0.0</nc:name> </nc:interface> </nc:area> </nc:ospf3> </nc:protocols>\", \" <nc:routing-options xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\"> <nc:router-id delete=\"delete\"/> <nc:router-id>10.200.16.75</nc:router-id> </nc:routing-options>", "xml 2", "xml 3"]` |

### Authors

- Rohit Thakur (@rohitthakur2590)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
[Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
