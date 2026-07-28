---
collection: ansible
version: "6"
title: "junipernetworks.junos.junos_ospfv2 module – OSPFv2 resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/junipernetworks/junos/junos_ospfv2_module.html
fetched_at: 2026-07-27T17:54:30+00:00
---
# junipernetworks.junos.junos_ospfv2 module – OSPFv2 resource module

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

- This module manages global OSPFv2 configuration on devices running Juniper JUNOS.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

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
| **router_id**  string | The OSPFv2 router id. |
| **spf_options**  dictionary | Configure options for SPF. |
| **delay**  integer | Time to wait before running an SPF (seconds). |
| **holddown**  integer | Time to hold down before running an SPF (seconds). |
| **rapid_runs**  integer | Number of maximum rapid SPF runs before holddown (seconds). |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the Junos device by executing the command **ERROR while parsing**: While parsing B() at index 103: Cannot find closing “)” after last parameter  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result |
| **state**  string | The state the configuration should be left in.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

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

- name: Merge Junos OSPFv2 config
  junipernetworks.junos.junos_ospfv2:
    config:
    - reference_bandwidth: 10g
      areas:
      - area_id: 0.0.0.100
        area_range: 10.200.16.0/24
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

# After state
# -----------
#
# admin# show protocols ospf
# reference-bandwidth 10g;
# no-rfc-1583;
# area 0.0.0.100 {
#     stub default-metric 100;
#     area-range 10.200.16.0/24;
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
```

## [Return Values](junos_ospfv2_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration model invocation.  Returned: when changed  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration prior to the model invocation.  Returned: always  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["command 1", "command 2", "command 3"]` |

### Authors

- Daniel Mellado (@dmellado)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
[Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
