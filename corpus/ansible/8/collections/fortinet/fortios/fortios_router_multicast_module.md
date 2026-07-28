---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_router_multicast module – Configure router multicast in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_router_multicast_module.html
fetched_at: 2026-07-28T02:26:47+00:00
---
# fortinet.fortios.fortios_router_multicast module – Configure router multicast in Fortinet’s FortiOS and FortiGate.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/ui/repo/published/fortinet/fortios/) (version 2.3.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_router_multicast_module.md#ansible-collections-fortinet-fortios-fortios-router-multicast-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_router_multicast`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_router_multicast_module.md#synopsis)
- [Requirements](fortios_router_multicast_module.md#requirements)
- [Parameters](fortios_router_multicast_module.md#parameters)
- [Notes](fortios_router_multicast_module.md#notes)
- [Examples](fortios_router_multicast_module.md#examples)
- [Return Values](fortios_router_multicast_module.md#return-values)

## [Synopsis](fortios_router_multicast_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify router feature and multicast category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_router_multicast_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_router_multicast_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **router_multicast**  dictionary | Configure router multicast. |
| **interface**  list / elements=dictionary | PIM interfaces. |
| **bfd**  string | Enable/disable Protocol Independent Multicast (PIM) Bidirectional Forwarding Detection (BFD).  **Choices:**   - `"enable"` - `"disable"` |
| **cisco_exclude_genid**  string | Exclude GenID from hello packets (compatibility with old Cisco IOS).  **Choices:**   - `"enable"` - `"disable"` |
| **dr_priority**  integer | DR election priority. |
| **hello_holdtime**  integer | Time before old neighbor information expires (0 - 65535 sec). |
| **hello_interval**  integer | Interval between sending PIM hello messages (0 - 65535 sec). |
| **igmp**  dictionary | IGMP configuration options. |
| **access_group**  string | Groups IGMP hosts are allowed to join. Source router.access-list.name. |
| **immediate_leave_group**  string | Groups to drop membership for immediately after receiving IGMPv2 leave. Source router.access-list.name. |
| **last_member_query_count**  integer | Number of group specific queries before removing group (2 - 7). |
| **last_member_query_interval**  integer | Timeout between IGMPv2 leave and removing group (1 - 65535 msec). |
| **query_interval**  integer | Interval between queries to IGMP hosts (1 - 65535 sec). |
| **query_max_response_time**  integer | Maximum time to wait for a IGMP query response (1 - 25 sec). |
| **query_timeout**  integer | Timeout between queries before becoming querying unit for network (60 - 900). |
| **router_alert_check**  string | Enable/disable require IGMP packets contain router alert option.  **Choices:**   - `"enable"` - `"disable"` |
| **version**  string | Maximum version of IGMP to support.  **Choices:**   - `"3"` - `"2"` - `"1"` |
| **join_group**  list / elements=dictionary | Join multicast groups. |
| **address**  string / required | Multicast group IP address. |
| **multicast_flow**  string | Acceptable source for multicast group. Source router.multicast-flow.name. |
| **name**  string / required | Interface name. Source system.interface.name. |
| **neighbour_filter**  string | Routers acknowledged as neighbor routers. Source router.access-list.name. |
| **passive**  string | Enable/disable listening to IGMP but not participating in PIM.  **Choices:**   - `"enable"` - `"disable"` |
| **pim_mode**  string | PIM operation mode.  **Choices:**   - `"sparse-mode"` - `"dense-mode"` |
| **propagation_delay**  integer | Delay flooding packets on this interface (100 - 5000 msec). |
| **rp_candidate**  string | Enable/disable compete to become RP in elections.  **Choices:**   - `"enable"` - `"disable"` |
| **rp_candidate_group**  string | Multicast groups managed by this RP. Source router.access-list.name. |
| **rp_candidate_interval**  integer | RP candidate advertisement interval (1 - 16383 sec). |
| **rp_candidate_priority**  integer | Router”s priority as RP. |
| **rpf_nbr_fail_back**  string | Enable/disable fail back for RPF neighbor query.  **Choices:**   - `"enable"` - `"disable"` |
| **rpf_nbr_fail_back_filter**  string | Filter for fail back RPF neighbors. Source router.access-list.name. |
| **state_refresh_interval**  integer | Interval between sending state-refresh packets (1 - 100 sec). |
| **static_group**  string | Statically set multicast groups to forward out. Source router.multicast-flow.name. |
| **ttl_threshold**  integer | Minimum TTL of multicast packets that will be forwarded (applied only to new multicast routes) (1 - 255). |
| **multicast_routing**  string | Enable/disable IP multicast routing.  **Choices:**   - `"enable"` - `"disable"` |
| **pim_sm_global**  dictionary | PIM sparse-mode global settings. |
| **accept_register_list**  string | Sources allowed to register packets with this Rendezvous Point (RP). Source router.access-list.name. |
| **accept_source_list**  string | Sources allowed to send multicast traffic. Source router.access-list.name. |
| **bsr_allow_quick_refresh**  string | Enable/disable accept BSR quick refresh packets from neighbors.  **Choices:**   - `"enable"` - `"disable"` |
| **bsr_candidate**  string | Enable/disable allowing this router to become a bootstrap router (BSR).  **Choices:**   - `"enable"` - `"disable"` |
| **bsr_hash**  integer | BSR hash length (0 - 32). |
| **bsr_interface**  string | Interface to advertise as candidate BSR. Source system.interface.name. |
| **bsr_priority**  integer | BSR priority (0 - 255). |
| **cisco_crp_prefix**  string | Enable/disable making candidate RP compatible with old Cisco IOS.  **Choices:**   - `"enable"` - `"disable"` |
| **cisco_ignore_rp_set_priority**  string | Use only hash for RP selection (compatibility with old Cisco IOS).  **Choices:**   - `"enable"` - `"disable"` |
| **cisco_register_checksum**  string | Checksum entire register packet(for old Cisco IOS compatibility).  **Choices:**   - `"enable"` - `"disable"` |
| **cisco_register_checksum_group**  string | Cisco register checksum only these groups. Source router.access-list.name. |
| **join_prune_holdtime**  integer | Join/prune holdtime (1 - 65535). |
| **message_interval**  integer | Period of time between sending periodic PIM join/prune messages in seconds (1 - 65535). |
| **null_register_retries**  integer | Maximum retries of null register (1 - 20). |
| **pim_use_sdwan**  string | Enable/disable use of SDWAN when checking RPF neighbor and sending of REG packet.  **Choices:**   - `"enable"` - `"disable"` |
| **register_rate_limit**  integer | Limit of packets/sec per source registered through this RP (0 - 65535). |
| **register_rp_reachability**  string | Enable/disable check RP is reachable before registering packets.  **Choices:**   - `"enable"` - `"disable"` |
| **register_source**  string | Override source address in register packets.  **Choices:**   - `"disable"` - `"interface"` - `"ip-address"` |
| **register_source_interface**  string | Override with primary interface address. Source system.interface.name. |
| **register_source_ip**  string | Override with local IP address. |
| **register_supression**  integer | Period of time to honor register-stop message (1 - 65535 sec). |
| **rp_address**  list / elements=dictionary | Statically configure RP addresses. |
| **group**  string | Groups to use this RP. Source router.access-list.name. |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **ip_address**  string | RP router address. |
| **rp_register_keepalive**  integer | Timeout for RP receiving data on (S,G) tree (1 - 65535 sec). |
| **spt_threshold**  string | Enable/disable switching to source specific trees.  **Choices:**   - `"enable"` - `"disable"` |
| **spt_threshold_group**  string | Groups allowed to switch to source tree. Source router.access-list.name. |
| **ssm**  string | Enable/disable source specific multicast.  **Choices:**   - `"enable"` - `"disable"` |
| **ssm_range**  string | Groups allowed to source specific multicast. Source router.access-list.name. |
| **route_limit**  integer | Maximum number of multicast routes. |
| **route_threshold**  integer | Generate warnings when the number of multicast routes exceeds this number, must not be greater than route-limit. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_router_multicast_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_router_multicast_module.md#id5)

```yaml+jinja
- hosts: fortigates
  collections:
    - fortinet.fortios
  connection: httpapi
  vars:
   vdom: "root"
   ansible_httpapi_use_ssl: yes
   ansible_httpapi_validate_certs: no
   ansible_httpapi_port: 443
  tasks:
  - name: Configure router multicast.
    fortios_router_multicast:
      vdom:  "{{ vdom }}"
      router_multicast:
        interface:
         -
            bfd: "enable"
            cisco_exclude_genid: "enable"
            dr_priority: "1"
            hello_holdtime: ""
            hello_interval: "30"
            igmp:
                access_group: "<your_own_value> (source router.access-list.name)"
                immediate_leave_group: "<your_own_value> (source router.access-list.name)"
                last_member_query_count: "2"
                last_member_query_interval: "1000"
                query_interval: "125"
                query_max_response_time: "10"
                query_timeout: "255"
                router_alert_check: "enable"
                version: "3"
            join_group:
             -
                address: "<your_own_value>"
            multicast_flow: "<your_own_value> (source router.multicast-flow.name)"
            name: "default_name_22 (source system.interface.name)"
            neighbour_filter: "<your_own_value> (source router.access-list.name)"
            passive: "enable"
            pim_mode: "sparse-mode"
            propagation_delay: "500"
            rp_candidate: "enable"
            rp_candidate_group: "<your_own_value> (source router.access-list.name)"
            rp_candidate_interval: "60"
            rp_candidate_priority: "192"
            rpf_nbr_fail_back: "enable"
            rpf_nbr_fail_back_filter: "<your_own_value> (source router.access-list.name)"
            state_refresh_interval: "60"
            static_group: "<your_own_value> (source router.multicast-flow.name)"
            ttl_threshold: "1"
        multicast_routing: "enable"
        pim_sm_global:
            accept_register_list: "<your_own_value> (source router.access-list.name)"
            accept_source_list: "<your_own_value> (source router.access-list.name)"
            bsr_allow_quick_refresh: "enable"
            bsr_candidate: "enable"
            bsr_hash: "10"
            bsr_interface: "<your_own_value> (source system.interface.name)"
            bsr_priority: "0"
            cisco_crp_prefix: "enable"
            cisco_ignore_rp_set_priority: "enable"
            cisco_register_checksum: "enable"
            cisco_register_checksum_group: "<your_own_value> (source router.access-list.name)"
            join_prune_holdtime: "210"
            message_interval: "60"
            null_register_retries: "1"
            pim_use_sdwan: "enable"
            register_rate_limit: "0"
            register_rp_reachability: "enable"
            register_source: "disable"
            register_source_interface: "<your_own_value> (source system.interface.name)"
            register_source_ip: "<your_own_value>"
            register_supression: "60"
            rp_address:
             -
                group: "<your_own_value> (source router.access-list.name)"
                id:  "61"
                ip_address: "<your_own_value>"
            rp_register_keepalive: "185"
            spt_threshold: "enable"
            spt_threshold_group: "<your_own_value> (source router.access-list.name)"
            ssm: "enable"
            ssm_range: "<your_own_value> (source router.access-list.name)"
        route_limit: "2147483647"
        route_threshold: ""
```

## [Return Values](fortios_router_multicast_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  **Returned:** always  **Sample:** `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  **Returned:** always  **Sample:** `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  **Returned:** always  **Sample:** `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  **Returned:** success  **Sample:** `"id"` |
| **name**  string | Name of the table used to fulfill the request  **Returned:** always  **Sample:** `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  **Returned:** always  **Sample:** `"webfilter"` |
| **revision**  string | Internal revision number  **Returned:** always  **Sample:** `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  **Returned:** always  **Sample:** `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  **Returned:** always  **Sample:** `"success"` |
| **vdom**  string | Virtual domain used  **Returned:** always  **Sample:** `"root"` |
| **version**  string | Version of the FortiGate  **Returned:** always  **Sample:** `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

- [Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
- [Homepage](https://www.fortinet.com)
- [Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
