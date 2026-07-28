---
collection: ansible
version: "8"
title: "community.network.ce_ospf_vrf module – Manages configuration of an OSPF VPN instance on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_ospf_vrf_module.html
fetched_at: 2026-07-28T01:55:47+00:00
---
# community.network.ce_ospf_vrf module – Manages configuration of an OSPF VPN instance on HUAWEI CloudEngine switches.

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.ce_ospf_vrf`.

- [Synopsis](ce_ospf_vrf_module.md#synopsis)
- [Parameters](ce_ospf_vrf_module.md#parameters)
- [Notes](ce_ospf_vrf_module.md#notes)
- [Examples](ce_ospf_vrf_module.md#examples)
- [Return Values](ce_ospf_vrf_module.md#return-values)

## [Synopsis](ce_ospf_vrf_module.md#id1)

- Manages configuration of an OSPF VPN instance on HUAWEI CloudEngine switches.

Aliases: network.cloudengine.ce_ospf_vrf

## [Parameters](ce_ospf_vrf_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **bandwidth**  string | Specifies the reference bandwidth used to assign ospf cost. Valid values are an integer, in Mbps, 1 - 2147483648, the default value is 100. |
| **description**  string | Specifies the description information of ospf process. |
| **lsaaholdinterval**  string | Specifies the hold interval of arrive LSA when use the intelligent timer. Valid value is an integer, in millisecond, from 0 to 10000, the default value is 500. |
| **lsaainterval**  string | Specifies the interval of arrive LSA when use the general timer. Valid value is an integer, in millisecond, from 0 to 10000. |
| **lsaalflag**  boolean | Specifies the mode of timer to calculate interval of arrive LSA. If set the parameter but not specifies value, the default will be used. If true use general timer. If false use intelligent timer.  **Choices:**   - `false` ← (default) - `true` |
| **lsaamaxinterval**  string | Specifies the max interval of arrive LSA when use the intelligent timer. Valid value is an integer, in millisecond, from 0 to 10000, the default value is 1000. |
| **lsaastartinterval**  string | Specifies the start interval of arrive LSA when use the intelligent timer. Valid value is an integer, in millisecond, from 0 to 10000, the default value is 500. |
| **lsaoholdinterval**  string | Specifies the hold interval of originate LSA . Valid value is an integer, in millisecond, from 0 to 5000, the default value is 1000. |
| **lsaointerval**  string | Specifies the interval of originate LSA . Valid value is an integer, in second, from 0 to 10, the default value is 5. |
| **lsaointervalflag**  boolean | Specifies whether cancel the interval of LSA originate or not. If set the parameter but noe specifies value, the default will be used. true:cancel the interval of LSA originate, the interval is 0. false:do not cancel the interval of LSA originate.  **Choices:**   - `false` ← (default) - `true` |
| **lsaomaxinterval**  string | Specifies the max interval of originate LSA . Valid value is an integer, in millisecond, from 1 to 10000, the default value is 5000. |
| **lsaostartinterval**  string | Specifies the start interval of originate LSA . Valid value is an integer, in millisecond, from 0 to 1000, the default value is 500. |
| **ospf**  string / required | The ID of the ospf process. Valid values are an integer, 1 - 4294967295, the default value is 1. |
| **route_id**  string | Specifies the ospf private route id,. Valid values are a string, formatted as an IP address (i.e. “10.1.1.1”) the length is 0 - 20. |
| **spfholdinterval**  string | Specifies the hold interval to calculate SPF when use intelligent timer. Valid value is an integer, in millisecond, from 1 to 5000, the default value is 200. |
| **spfinterval**  string | Specifies the interval to calculate SPF when use second level timer. Valid value is an integer, in second, from 1 to 10. |
| **spfintervalmi**  string | Specifies the interval to calculate SPF when use millisecond level timer. Valid value is an integer, in millisecond, from 1 to 10000. |
| **spfintervaltype**  string | Specifies the mode of timer which used to calculate SPF. If set the parameter but noe specifies value, the default will be used. If is intelligent-timer, then use intelligent timer. If is timer, then use second level timer. If is millisecond, then use millisecond level timer.  **Choices:**   - `"intelligent-timer"` ← (default) - `"timer"` - `"millisecond"` |
| **spfmaxinterval**  string | Specifies the max interval to calculate SPF when use intelligent timer. Valid value is an integer, in millisecond, from 1 to 20000, the default value is 5000. |
| **spfstartinterval**  string | Specifies the start interval to calculate SPF when use intelligent timer. Valid value is an integer, in millisecond, from 1 to 1000, the default value is 50. |
| **state**  string | Specify desired state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **vrf**  string | Specifies the vpn instance which use ospf,length is 1 - 31. Valid values are a string.  **Default:** `"_public_"` |

## [Notes](ce_ospf_vrf_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_ospf_vrf_module.md#id4)

```yaml+jinja
- name: Ospf vrf module test
  hosts: cloudengine
  connection: local
  gather_facts: false

  tasks:

  - name: Configure ospf route id
    community.network.ce_ospf_vrf:
      ospf: 2
      route_id: 2.2.2.2
      lsaointervalflag: false
      lsaointerval: 2
```

## [Return Values](ce_ospf_vrf_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `false` |
| **end_state**  dictionary | k/v pairs of configuration after module execution  **Returned:** verbose mode  **Sample:** `{"bandwidthReference": "100", "description": null, "lsaArrivalFlag": "false", "lsaArrivalHoldInterval": "500", "lsaArrivalInterval": null, "lsaArrivalMaxInterval": "1000", "lsaArrivalStartInterval": "500", "lsaOriginateHoldInterval": "1000", "lsaOriginateInterval": "2", "lsaOriginateIntervalFlag": "false", "lsaOriginateMaxInterval": "5000", "lsaOriginateStartInterval": "500", "processId": "2", "routerId": "2.2.2.2", "spfScheduleHoldInterval": "1000", "spfScheduleInterval": null, "spfScheduleIntervalMillisecond": null, "spfScheduleIntervalType": "intelligent-timer", "spfScheduleMaxInterval": "10000", "spfScheduleStartInterval": "500", "vrfName": "_public_"}` |
| **existing**  dictionary | k/v pairs of existing configuration  **Returned:** verbose mode  **Sample:** `{"bandwidthReference": "100", "description": null, "lsaArrivalFlag": "false", "lsaArrivalHoldInterval": "500", "lsaArrivalInterval": null, "lsaArrivalMaxInterval": "1000", "lsaArrivalStartInterval": "500", "lsaOriginateHoldInterval": "1000", "lsaOriginateInterval": "2", "lsaOriginateIntervalFlag": "false", "lsaOriginateMaxInterval": "5000", "lsaOriginateStartInterval": "500", "processId": "2", "routerId": "2.2.2.2", "spfScheduleHoldInterval": "1000", "spfScheduleInterval": null, "spfScheduleIntervalMillisecond": null, "spfScheduleIntervalType": "intelligent-timer", "spfScheduleMaxInterval": "10000", "spfScheduleStartInterval": "500", "vrfName": "_public_"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** verbose mode  **Sample:** `{"bandwidth": "100", "description": null, "lsaaholdinterval": "500", "lsaainterval": null, "lsaalflag": "False", "lsaamaxinterval": "1000", "lsaastartinterval": "500", "lsaoholdinterval": "1000", "lsaointerval": "2", "lsaointervalflag": "False", "lsaomaxinterval": "5000", "lsaostartinterval": "500", "process_id": "2", "route_id": "2.2.2.2", "spfholdinterval": "1000", "spfinterval": null, "spfintervalmi": null, "spfintervaltype": "intelligent-timer", "spfmaxinterval": "10000", "spfstartinterval": "500", "vrf": "_public_"}` |
| **updates**  list / elements=string | commands sent to the device  **Returned:** always  **Sample:** `["ospf 2"]` |

### Authors

- Yang yang (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
