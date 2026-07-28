---
collection: ansible
version: "8"
title: "junipernetworks.junos.junos_ospfv2 module – OSPFv2 resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/junipernetworks/junos/junos_ospfv2_module.html
fetched_at: 2026-07-28T02:39:47+00:00
---
# junipernetworks.junos.junos_ospfv2 module – OSPFv2 resource module

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
> see [Requirements](junos_ospfv2_module.md#ansible-collections-junipernetworks-junos-junos-ospfv2-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_ospfv2`.

New in junipernetworks.junos 1.0.0

- [Synopsis](junos_ospfv2_module.md#synopsis)
- [Requirements](junos_ospfv2_module.md#requirements)
- [Parameters](junos_ospfv2_module.md#parameters)
- [Notes](junos_ospfv2_module.md#notes)
- [Examples](junos_ospfv2_module.md#examples)
- [Return Values](junos_ospfv2_module.md#return-values)

## [Synopsis](junos_ospfv2_module.md#id1)

- This module manages OSPFv2 configuration on devices running Juniper JUNOS.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: ospfv2

## [Requirements](junos_ospfv2_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.6.4)
- xmltodict (>=0.12.0)

## [Parameters](junos_ospfv2_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of OSPFv2 process configuration. |
| **areas**  list / elements=dictionary | A list of OSPFv2 areas’ configuration. |
| **area_id**  string / required | The Area ID as an integer or IP Address. |
| **area_range**  string | Configure an address range for the area.  Included for compatibility, remove/deprecate after 2025-07-01.  Alternate for this would be area_ranges which is a list. |
| **area_ranges**  list / elements=dictionary | Configure IP address ranges for the area. |
| **address**  string | Specify ip address. |
| **exact**  boolean | Enforce exact match for advertisement of this area range.  **Choices:**   - `false` - `true` |
| **override_metric**  integer | Override the dynamic metric for this area-range. |
| **restrict**  boolean | Restrict advertisement of this area range.  **Choices:**   - `false` - `true` |
| **interfaces**  list / elements=dictionary | List of interfaces in this area. |
| **authentication**  dictionary | Specify authentication type |
| **md5**  list / elements=dictionary | MD5 authentication keys |
| **key**  string | Specify key value |
| **key_id**  integer | Specify the key identity |
| **start_time**  string | Specify Start time for key transmission (YYYY-MM-DD.HH:MM) |
| **password**  string | Specify authentication key. |
| **type**  dictionary | Type of authentication to use.  Included for compatibility, remove/deprecate after 2025-07-01. |
| **bandwidth_based_metrics**  list / elements=dictionary | Specify list of bandwidth based metrics |
| **bandwidth**  string | BW to apply metric to.  **Choices:**   - `"1g"` - `"10g"` |
| **metric**  integer | Specify metric |
| **flood_reduction**  boolean | Enable flood reduction.  **Choices:**   - `false` - `true` |
| **metric**  integer | Metric applied to the interface. |
| **name**  string / required | Name of the interface. |
| **passive**  boolean | Specify passive  **Choices:**   - `false` - `true` |
| **priority**  integer | Priority for the interface. |
| **timers**  dictionary | Specify timers |
| **dead_interval**  integer | Dead interval (seconds). |
| **hello_interval**  integer | Hello interval (seconds). |
| **poll_interval**  integer | Poll interval (seconds). |
| **retransmit_interval**  integer | Retransmit interval (seconds). |
| **transit_delay**  integer | Transit delay (seconds). |
| **stub**  dictionary | Settings for configuring the area as a stub. |
| **default_metric**  integer | Metric for the default route in this area. |
| **set**  boolean | Configure the area as a stub.  **Choices:**   - `false` - `true` |
| **external_preference**  integer | Preference of external routes. |
| **overload**  dictionary | Specify time for overload mode reset |
| **allow_route_leaking**  boolean | Allow routes to be leaked when overload is configured.  **Choices:**   - `false` - `true` |
| **as_external**  boolean | Advertise As External with maximum usable metric.  **Choices:**   - `false` - `true` |
| **stub_network**  boolean | Advertise Stub Network with maximum metric.  **Choices:**   - `false` - `true` |
| **timeout**  integer | Time after which overload mode is reset (seconds). |
| **preference**  integer | Preference of internal routes. |
| **prefix_export_limit**  integer | Maximum number of external prefixes that can be exported. |
| **reference_bandwidth**  string | Bandwidth for calculating metric defaults.  **Choices:**   - `"1g"` - `"10g"` |
| **rfc1583compatibility**  boolean | Set RFC1583 compatibility  **Choices:**   - `false` - `true` |
| **router_id**  string | The OSPFv2 router id. |
| **spf_options**  dictionary | Configure options for SPF. |
| **delay**  integer | Time to wait before running an SPF (seconds). |
| **holddown**  integer | Time to hold down before running an SPF (seconds). |
| **no_ignore_our_externals**  boolean | Do not ignore self-generated external and NSSA LSAs.  **Choices:**   - `false` - `true` |
| **rapid_runs**  integer | Number of maximum rapid SPF runs before holddown (seconds). |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the Junos device by executing the command **show protocols ospf**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result |
| **state**  string | The state the configuration should be left in.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](junos_ospfv2_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the device being managed.
> - This module works with connection `netconf`.
> - See [the Junos OS Platform Options](https://docs.ansible.com/ansible/latest/network/user_guide/platform_junos.html).
> - Tested against JunOS v18.4R1

## [Examples](junos_ospfv2_module.md#id5)

```yaml+jinja
# Using merged
#
# Before state
# ------------
#
# admin# show protocols ospf

- name: Merge provided OSPFv2 configuration into running config.
  junipernetworks.junos.junos_ospfv2:
    config:
      - reference_bandwidth: 10g
        areas:
          - area_id: 0.0.0.100
            area_ranges:
              - address: 10.200.17.0/24
                exact: true
                restrict: true
                override_metric: 2000
              - address: 10.200.15.0/24
                exact: true
                restrict: true
                override_metric: 2000
                stub:
                  default_metric: 100
                  set: true
                interfaces:
                  - name: so-0/0/0.0
                    priority: 3
                    metric: 5
                    flood_reduction: false
                    passive: true
                    bandwidth_based_metrics:
                      - bandwidth: 1g
                        metric: 5
                      - bandwidth: 10g
                        metric: 40
                    timers:
                      dead_interval: 4
                      hello_interval: 2
                      poll_interval: 2
                      retransmit_interval: 2
        rfc1583compatibility: false
    state: merged

# Task Output:
# ------------
#
# before: []
#
# commands:
# - <nc:protocols xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#   <nc:ospf><nc:reference-bandwidth>10g</nc:reference-bandwidth><nc:no-rfc-1583/>
#   <nc:area><nc:name>0.0.0.100</nc:name><nc:area-range><nc:name>10.200.17.0/24</nc:name><nc:exact/>
#   <nc:restrict/><nc:override-metric>2000</nc:override-metric></nc:area-range><nc:area-range>
#   <nc:name>10.200.15.0/24</nc:name><nc:exact/><nc:restrict/><nc:override-metric>2000</nc:override-metric>
#   </nc:area-range><nc:interface><nc:name>so-0/0/0.0</nc:name><nc:priority>3</nc:priority>
#   <nc:metric>5</nc:metric><nc:passive/><nc:bandwidth-based-metrics><nc:bandwidth><nc:name>1g</nc:name>
#   <nc:metric>5</nc:metric></nc:bandwidth><nc:bandwidth><nc:name>10g</nc:name><nc:metric>40</nc:metric>
#   </nc:bandwidth></nc:bandwidth-based-metrics><nc:dead-interval>4</nc:dead-interval>
#   <nc:hello-interval>2</nc:hello-interval><nc:poll-interval>2</nc:poll-interval>
#   <nc:retransmit-interval>2</nc:retransmit-interval></nc:interface><nc:stub>
#   <nc:default-metric>100</nc:default-metric></nc:stub></nc:area></nc:ospf></nc:protocols>
#
# after:
# - areas:
#   - area_id: 0.0.0.100
#     area_range: '[''10.200.17.0/24'', ''10.200.15.0/24'']'
#     area_ranges:
#     - address: 10.200.17.0/24
#       exact: true
#       override_metric: 2000
#       restrict: true
#     - address: 10.200.15.0/24
#       exact: true
#       override_metric: 2000
#       restrict: true
#     interfaces:
#     - bandwidth_based_metrics:
#       - bandwidth: 1g
#         metric: 5
#       - bandwidth: 10g
#         metric: 40
#       metric: 5
#       name: so-0/0/0.0
#       passive: true
#       priority: 3
#       timers:
#         dead_interval: 4
#         hello_interval: 2
#         poll_interval: 2
#         retransmit_interval: 2
#     stub:
#       default_metric: 100
#       set: true
#   reference_bandwidth: 10g
#   rfc1583compatibility: false

# After state
# -----------
#
# admin# show protocols ospf
# reference-bandwidth 10g;
# no-rfc-1583;
# area 0.0.0.100 {
#     stub default-metric 100;
#     area-range 10.200.17.0/24 {
#         restrict;
#         exact;
#         override-metric 2000;
#     }
#     area-range 10.200.15.0/24 {
#         restrict;
#         exact;
#         override-metric 2000;
#     }
#     interface so-0/0/0.0 {
#         passive;
#         bandwidth-based-metrics {
#             bandwidth 1g metric 5;
#             bandwidth 10g metric 40;
#         }
#         metric 5;
#         priority 3;
#         retransmit-interval 2;
#         hello-interval 2;
#         dead-interval 4;
#         poll-interval 2;
#     }
# }
#
# Using replaced
#
# Before state
# ------------
#
# admin# show protocols ospf
# reference-bandwidth 10g;
# no-rfc-1583;
# area 0.0.0.100 {
#     stub default-metric 100;
#     area-range 10.200.17.0/24 {
#         restrict;
#         exact;
#         override-metric 2000;
#     }
#     area-range 10.200.15.0/24 {
#         restrict;
#         exact;
#         override-metric 2000;
#     }
#     interface so-0/0/0.0 {
#         passive;
#         bandwidth-based-metrics {
#             bandwidth 1g metric 5;
#             bandwidth 10g metric 40;
#         }
#         metric 5;
#         priority 3;
#         retransmit-interval 2;
#         hello-interval 2;
#         dead-interval 4;
#         poll-interval 2;
#     }
# }

- name: Replace existing Junos OSPFv2 config with provided config
  junipernetworks.junos.junos_ospfv2:
    config:
      - reference_bandwidth: 10g
        areas:
          - area_id: 0.0.0.100
            area_ranges:
              - address: 10.200.17.0/24
                exact: true
                restrict: true
              - address: 10.200.16.0/24
                exact: true
                restrict: true
                override_metric: 1000
            stub:
              default_metric: 100
              set: true
            interfaces:
              - name: so-0/0/0.0
                priority: 3
                metric: 5
                flood_reduction: false
                passive: true
                bandwidth_based_metrics:
                  - bandwidth: 1g
                    metric: 5
                  - bandwidth: 10g
                    metric: 40
                timers:
                  dead_interval: 4
                  hello_interval: 2
                  poll_interval: 2
                  retransmit_interval: 2
        rfc1583compatibility: false
    state: replacedd

# Task Output:
# ------------
#
# before:
#   - areas:
#     - area_id: 0.0.0.100
#       area_range: '[''10.200.17.0/24'', ''10.200.15.0/24'']'
#       area_ranges:
#       - address: 10.200.17.0/24
#         exact: true
#         override_metric: 2000
#         restrict: true
#       - address: 10.200.15.0/24
#         exact: true
#         override_metric: 2000
#         restrict: true
#       interfaces:
#       - bandwidth_based_metrics:
#         - bandwidth: 1g
#           metric: 5
#         - bandwidth: 10g
#           metric: 40
#         metric: 5
#         name: so-0/0/0.0
#         passive: true
#         priority: 3
#         timers:
#           dead_interval: 4
#           hello_interval: 2
#           poll_interval: 2
#           retransmit_interval: 2
#       stub:
#         default_metric: 100
#         set: true
#     reference_bandwidth: 10g
#     rfc1583compatibility: false
#
# commands:
# - <nc:protocols xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#   <nc:ospf><nc:area delete="delete">0.0.0.100</nc:area></nc:ospf><nc:ospf>
#   <nc:reference-bandwidth>10g</nc:reference-bandwidth><nc:no-rfc-1583/><nc:area>
#   <nc:name>0.0.0.100</nc:name><nc:area-range><nc:name>10.200.17.0/24</nc:name><nc:exact/>
#   <nc:restrict/></nc:area-range><nc:area-range><nc:name>10.200.16.0/24</nc:name><nc:exact/>
#   <nc:restrict/><nc:override-metric>1000</nc:override-metric></nc:area-range><nc:interface>
#   <nc:name>so-0/0/0.0</nc:name><nc:priority>3</nc:priority><nc:metric>5</nc:metric><nc:passive/>
#   <nc:bandwidth-based-metrics><nc:bandwidth><nc:name>1g</nc:name><nc:metric>5</nc:metric>
#   </nc:bandwidth><nc:bandwidth><nc:name>10g</nc:name><nc:metric>40</nc:metric></nc:bandwidth>
#   </nc:bandwidth-based-metrics><nc:dead-interval>4</nc:dead-interval><nc:hello-interval>2</nc:hello-interval>
#   <nc:poll-interval>2</nc:poll-interval><nc:retransmit-interval>2</nc:retransmit-interval></nc:interface>
#   <nc:stub><nc:default-metric>100</nc:default-metric></nc:stub></nc:area></nc:ospf></nc:protocols>
#
# after:
#   - areas:
#     - area_id: 0.0.0.100
#       area_range: '[''10.200.17.0/24'', ''10.200.16.0/24'']'
#       area_ranges:
#       - address: 10.200.17.0/24
#         exact: true
#         restrict: true
#       - address: 10.200.16.0/24
#         exact: true
#         override_metric: 1000
#         restrict: true
#       interfaces:
#       - bandwidth_based_metrics:
#         - bandwidth: 1g
#           metric: 5
#         - bandwidth: 10g
#           metric: 40
#         metric: 5
#         name: so-0/0/0.0
#         passive: true
#         priority: 3
#         timers:
#           dead_interval: 4
#           hello_interval: 2
#           poll_interval: 2
#           retransmit_interval: 2
#       stub:
#         default_metric: 100
#         set: true
#     reference_bandwidth: 10g
#     rfc1583compatibility: false
#
# After state
# -----------
#
# admin# show protocols ospf
# reference-bandwidth 10g;
# no-rfc-1583;
# area 0.0.0.100 {
#     stub default-metric 100;
#     area-range 10.200.17.0/24 {
#         restrict;
#         exact;
#     }
#     area-range 10.200.16.0/24 {
#         restrict;
#         exact;
#         override-metric 1000;
#     }
#     interface so-0/0/0.0 {
#         passive;
#         bandwidth-based-metrics {
#             bandwidth 1g metric 5;
#             bandwidth 10g metric 40;
#         }
#         metric 5;
#         priority 3;
#         retransmit-interval 2;
#         hello-interval 2;
#         dead-interval 4;
#         poll-interval 2;
#     }
# }
#
# Using overridden
#
# Before state
# ------------
#
# admin# show protocols ospf
# reference-bandwidth 10g;
# no-rfc-1583;
# area 0.0.0.100 {
#     stub default-metric 100;
#     area-range 10.200.17.0/24 {
#         restrict;
#         exact;
#     }
#     area-range 10.200.16.0/24 {
#         restrict;
#         exact;
#         override-metric 1000;
#     }
#     interface so-0/0/0.0 {
#         passive;
#         bandwidth-based-metrics {
#             bandwidth 1g metric 5;
#             bandwidth 10g metric 40;
#         }
#         metric 5;
#         priority 3;
#         retransmit-interval 2;
#         hello-interval 2;
#         dead-interval 4;
#         poll-interval 2;
#     }
# }

- name: Override runnig OSPFv2 config with provided config
  junipernetworks.junos.junos_ospfv2:
    config:
      - reference_bandwidth: 10g
        areas:
          - area_id: 0.0.0.110
            area_ranges:
              - address: 20.200.17.0/24
                exact: true
                restrict: true
                override_metric: 2000
              - address: 20.200.15.0/24
                exact: true
                restrict: true
                override_metric: 2000
            stub:
              default_metric: 200
              set: true
            interfaces:
              - name: so-0/0/0.0
                priority: 3
                metric: 5
                flood_reduction: false
                passive: true
                bandwidth_based_metrics:
                  - bandwidth: 1g
                    metric: 5
                  - bandwidth: 10g
                    metric: 40
    state: overridden

# Task Output:
# ------------
#
# before:
# - areas:
#   - area_id: 0.0.0.100
#     area_range: '[''10.200.17.0/24'', ''10.200.16.0/24'']'
#     area_ranges:
#     - address: 10.200.17.0/24
#       exact: true
#       restrict: true
#     - address: 10.200.16.0/24
#       exact: true
#       override_metric: 1000
#       restrict: true
#     interfaces:
#     - bandwidth_based_metrics:
#       - bandwidth: 1g
#         metric: 5
#       - bandwidth: 10g
#         metric: 40
#       metric: 5
#       name: so-0/0/0.0
#       passive: true
#       priority: 3
#       timers:
#         dead_interval: 4
#         hello_interval: 2
#         poll_interval: 2
#         retransmit_interval: 2
#     stub:
#       default_metric: 100
#       set: true
#   reference_bandwidth: 10g
#   rfc1583compatibility: false
#
# commands:
# - <nc:protocols xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#   <nc:ospf><nc:area delete="delete">0.0.0.100</nc:area></nc:ospf><nc:ospf>
#   <nc:reference-bandwidth>10g</nc:reference-bandwidth><nc:area><nc:name>0.0.0.110</nc:name>
#   <nc:area-range><nc:name>20.200.17.0/24</nc:name><nc:exact/><nc:restrict/>
#   <nc:override-metric>2000</nc:override-metric></nc:area-range><nc:area-range>
#   <nc:name>20.200.15.0/24</nc:name><nc:exact/><nc:restrict/><nc:override-metric>2000</nc:override-metric>
#   </nc:area-range><nc:interface><nc:name>so-0/0/0.0</nc:name><nc:priority>3</nc:priority>
#   <nc:metric>5</nc:metric><nc:passive/><nc:bandwidth-based-metrics><nc:bandwidth><nc:name>1g</nc:name>
#   <nc:metric>5</nc:metric></nc:bandwidth><nc:bandwidth><nc:name>10g</nc:name><nc:metric>40</nc:metric>
#   </nc:bandwidth></nc:bandwidth-based-metrics></nc:interface><nc:stub>
#   <nc:default-metric>200</nc:default-metric></nc:stub></nc:area></nc:ospf></nc:protocols>
#
# after:
#   - areas:
#     - area_id: 0.0.0.110
#       area_range: '[''20.200.17.0/24'', ''20.200.15.0/24'']'
#       area_ranges:
#       - address: 20.200.17.0/24
#         exact: true
#         override_metric: 2000
#         restrict: true
#       - address: 20.200.15.0/24
#         exact: true
#         override_metric: 2000
#         restrict: true
#       interfaces:
#       - bandwidth_based_metrics:
#         - bandwidth: 1g
#           metric: 5
#         - bandwidth: 10g
#           metric: 40
#         metric: 5
#         name: so-0/0/0.0
#         passive: true
#         priority: 3
#       stub:
#         default_metric: 200
#         set: true
#     reference_bandwidth: 10g
#     rfc1583compatibility: false

# After state
# -----------
#
# admin# show protocols ospf
# reference-bandwidth 10g;
# no-rfc-1583;
# area 0.0.0.110 {
#     stub default-metric 200;
#     area-range 20.200.17.0/24 {
#         restrict;
#         exact;
#         override-metric 2000;
#     }
#     area-range 20.200.15.0/24 {
#         restrict;
#         exact;
#         override-metric 2000;
#     }
#     interface so-0/0/0.0 {
#         passive;
#         bandwidth-based-metrics {
#             bandwidth 1g metric 5;
#             bandwidth 10g metric 40;
#         }
#         metric 5;
#         priority 3;
#     }
# }
# Using deleted
#
# Before state
# ------------
#
# admin# show protocols ospf
# reference-bandwidth 10g;
# no-rfc-1583;
# area 0.0.0.110 {
#     stub default-metric 200;
#     area-range 20.200.17.0/24 {
#         restrict;
#         exact;
#         override-metric 2000;
#     }
#     area-range 20.200.15.0/24 {
#         restrict;
#         exact;
#         override-metric 2000;
#     }
#     interface so-0/0/0.0 {
#         passive;
#         bandwidth-based-metrics {
#             bandwidth 1g metric 5;
#             bandwidth 10g metric 40;
#         }
#         metric 5;
#         priority 3;
#     }
# }

- name: Delete OSPFv2 running config.
  junipernetworks.junos.junos_ospfv2:
    config:
    state: deleted

# Task Output:
# ------------
#
# before:
#   - areas:
#     - area_id: 0.0.0.110
#       area_range: '[''20.200.17.0/24'', ''20.200.15.0/24'']'
#       area_ranges:
#       - address: 20.200.17.0/24
#         exact: true
#         override_metric: 2000
#         restrict: true
#       - address: 20.200.15.0/24
#         exact: true
#         override_metric: 2000
#         restrict: true
#       interfaces:
#       - bandwidth_based_metrics:
#         - bandwidth: 1g
#           metric: 5
#         - bandwidth: 10g
#           metric: 40
#         metric: 5
#         name: so-0/0/0.0
#         passive: true
#         priority: 3
#       stub:
#         default_metric: 200
#         set: true
#     reference_bandwidth: 10g
#     rfc1583compatibility: false
#
# commands:
# - <nc:protocols xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#   <nc:ospf><nc:area delete="delete">0.0.0.100</nc:area><nc:reference-bandwidth delete="delete"/>
#   <nc:no-rfc-1583 delete="delete"/></nc:ospf></nc:protocols>
#
# after: []
#
#
# After state
# -----------
#
# admin# show protocols ospf

# Using gathered
#
# Before state
# ------------
#
# admin# show protocols ospf
# reference-bandwidth 10g;
# no-rfc-1583;
# area 0.0.0.100 {
#     stub default-metric 100;
#     area-range 10.200.17.0/24 {
#         restrict;
#         exact;
#         override-metric 2000;
#     }
#     area-range 10.200.15.0/24 {
#         restrict;
#         exact;
#         override-metric 2000;
#     }
#     interface so-0/0/0.0 {
#         passive;
#         bandwidth-based-metrics {
#             bandwidth 1g metric 5;
#             bandwidth 10g metric 40;
#         }
#         metric 5;
#         priority 3;
#         retransmit-interval 2;
#         hello-interval 2;
#         dead-interval 4;
#         poll-interval 2;
#     }
# }

- name: Gather Junos OSPFv2 running-configuration
  junipernetworks.junos.junos_ospfv2:
    config:
    state: gathered
#
#
# Task Output:
# ------------
#
# gathered:
#
#  - areas:
# - area_id: 0.0.0.100
#   area_range: '[''10.200.17.0/24'', ''10.200.15.0/24'']'
#   area_ranges:
#   - address: 10.200.17.0/24
#     exact: true
#     override_metric: 2000
#     restrict: true
#   - address: 10.200.15.0/24
#     exact: true
#     override_metric: 2000
#     restrict: true
#   interfaces:
#   - bandwidth_based_metrics:
#     - bandwidth: 1g
#       metric: 5
#     - bandwidth: 10g
#       metric: 40
#     metric: 5
#     name: so-0/0/0.0
#     passive: true
#     priority: 3
#     timers:
#       dead_interval: 4
#       hello_interval: 2
#       poll_interval: 2
#       retransmit_interval: 2
#   stub:
#     default_metric: 100
#     set: true
# reference_bandwidth: 10g
# rfc1583compatibility: false

# Using parsed
# parsed.cfg
# ------------
# <?xml version="1.0" encoding="UTF-8"?>
# <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
#     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
#         <version>18.4R1-S2.4</version>
#         <protocols>
#             <ospf>
#             <reference-bandwidth>10g</reference-bandwidth>
#             <no-rfc-1583/>
#             <area>
#                 <name>0.0.0.100</name>
#                 <stub>
#                     <default-metric>100</default-metric>
#                 </stub>
#                 <area-range>
#                     <name>10.200.16.0/24</name>
#                     <exact/>
#                     <override-metric>10000</override-metric>
#                 </area-range>
#                 <area-range>
#                     <name>10.200.11.0/24</name>
#                     <restrict/>
#                     <exact/>
#                 </area-range>
#                 <interface>
#                     <name>so-0/0/0.0</name>
#                     <passive>
#                     </passive>
#                     <bandwidth-based-metrics>
#                         <bandwidth>
#                             <name>1g</name>
#                             <metric>5</metric>
#                         </bandwidth>
#                         <bandwidth>
#                             <name>10g</name>
#                             <metric>40</metric>
#                         </bandwidth>
#                     </bandwidth-based-metrics>
#                     <metric>5</metric>
#                     <priority>3</priority>
#                     <retransmit-interval>2</retransmit-interval>
#                     <hello-interval>2</hello-interval>
#                     <dead-interval>4</dead-interval>
#                     <poll-interval>2</poll-interval>
#                 </interface>
#             </area>
#         </ospf>
#         </protocols>
#         <routing-options>
#             <static>
#                 <route>
#                     <name>172.16.17.0/24</name>
#                     <discard />
#                 </route>
#             </static>
#             <router-id>10.200.16.75</router-id>
#             <autonomous-system>
#                 <as-number>65432</as-number>
#             </autonomous-system>
#         </routing-options>
#     </configuration>
# </rpc-reply>

- name: Parsed the ospfv2 config into structured ansible resource facts.
  junipernetworks.junos.junos_ospfv2:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed
#
# Task Output:
# ------------
#
# parsed:
# - areas:
#     - area_id: 0.0.0.100
#       area_range: '[''10.200.16.0/24'', ''10.200.11.0/24'']'
#       area_ranges:
#       - address: 10.200.16.0/24
#         exact: true
#         override_metric: 10000
#       - address: 10.200.11.0/24
#         exact: true
#         restrict: true
#       interfaces:
#       - bandwidth_based_metrics:
#         - bandwidth: 1g
#           metric: 5
#         - bandwidth: 10g
#           metric: 40
#         metric: 5
#         name: so-0/0/0.0
#         passive: true
#         priority: 3
#         timers:
#           dead_interval: 4
#           hello_interval: 2
#           poll_interval: 2
#           retransmit_interval: 2
#       stub:
#         default_metric: 100
#         set: true
#     reference_bandwidth: 10g
#     rfc1583compatibility: false
#     router_id: 10.200.16.75

# Using rendered
#
- name: Render the commands for provided  configuration
  junipernetworks.junos.junos_ospfv2:
    config:
      - reference_bandwidth: 10g
        areas:
          - area_id: 0.0.0.100
            area_ranges:
              - address: 10.200.17.0/24
                exact: true
                restrict: true
                override_metric: 2000
              - address: 10.200.15.0/24
                exact: true
                restrict: true
                override_metric: 2000
            stub:
              default_metric: 100
              set: true
            interfaces:
              - name: so-0/0/0.0
                priority: 3
                metric: 5
                flood_reduction: false
                passive: true
                bandwidth_based_metrics:
                  - bandwidth: 1g
                    metric: 5
                  - bandwidth: 10g
                    metric: 40
                timers:
                  dead_interval: 4
                  hello_interval: 2
                  poll_interval: 2
                  retransmit_interval: 2
        rfc1583compatibility: false
    state: rendered

# Task Output:
# ------------
#
# rendered: "<nc:protocols xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
# <nc:ospf><nc:reference-bandwidth>10g</nc:reference-bandwidth><nc:no-rfc-1583/><nc:area><nc:name>0.0.0.100</nc:name>
# <nc:area-range><nc:name>10.200.17.0/24</nc:name><nc:exact/><nc:restrict/><nc:override-metric>2000</nc:override-metric>
# </nc:area-range><nc:area-range><nc:name>10.200.15.0/24</nc:name><nc:exact/><nc:restrict/>
# <nc:override-metric>2000</nc:override-metric></nc:area-range><nc:interface><nc:name>so-0/0/0.0</nc:name>
# <nc:priority>3</nc:priority><nc:metric>5</nc:metric><nc:passive/><nc:bandwidth-based-metrics><nc:bandwidth>
# <nc:name>1g</nc:name><nc:metric>5</nc:metric></nc:bandwidth><nc:bandwidth><nc:name>10g</nc:name>
# <nc:metric>40</nc:metric></nc:bandwidth></nc:bandwidth-based-metrics><nc:dead-interval>4</nc:dead-interval>
# <nc:hello-interval>2</nc:hello-interval><nc:poll-interval>2</nc:poll-interval>
# <nc:retransmit-interval>2</nc:retransmit-interval></nc:interface><nc:stub>
# <nc:default-metric>100</nc:default-metric></nc:stub></nc:area></nc:ospf></nc:protocols>"
```

## [Return Values](junos_ospfv2_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration module invocation.  **Returned:** when changed  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration prior to the module invocation.  **Returned:** always  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["<nc:protocols xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\">< nc:ospf><nc:area delete=\"delete\">0.0.0.100</nc:area><nc:reference-bandwidth delete=\"delete\"/> <nc:no-rfc-1583 delete=\"delete\"/></nc:ospf></nc:protocols>", "xml 2", "xml 3"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when *state* is `gathered`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  **Returned:** when *state* is `parsed`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  **Returned:** when *state* is `rendered`  **Sample:** `["<nc:protocols xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\">"]` |

### Authors

- Daniel Mellado (@dmellado)
- Rohit Thakur (@rohitthakur2590)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
