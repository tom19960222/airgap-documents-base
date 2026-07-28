---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_router_ospf module – Configure OSPF in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_router_ospf_module.html
fetched_at: 2026-07-28T02:26:49+00:00
---
# fortinet.fortios.fortios_router_ospf module – Configure OSPF in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_router_ospf_module.md#ansible-collections-fortinet-fortios-fortios-router-ospf-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_router_ospf`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_router_ospf_module.md#synopsis)
- [Requirements](fortios_router_ospf_module.md#requirements)
- [Parameters](fortios_router_ospf_module.md#parameters)
- [Notes](fortios_router_ospf_module.md#notes)
- [Examples](fortios_router_ospf_module.md#examples)
- [Return Values](fortios_router_ospf_module.md#return-values)

## [Synopsis](fortios_router_ospf_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify router feature and ospf category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_router_ospf_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_router_ospf_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **router_ospf**  dictionary | Configure OSPF. |
| **abr_type**  string | Area border router type.  **Choices:**   - `"cisco"` - `"ibm"` - `"shortcut"` - `"standard"` |
| **area**  list / elements=dictionary | OSPF area configuration. |
| **authentication**  string | Authentication type.  **Choices:**   - `"none"` - `"text"` - `"message-digest"` - `"md5"` |
| **comments**  string | Comment. |
| **default_cost**  integer | Summary default cost of stub or NSSA area. |
| **filter_list**  list / elements=dictionary | OSPF area filter-list configuration. |
| **direction**  string | Direction.  **Choices:**   - `"in"` - `"out"` |
| **id**  integer / required | Filter list entry ID. see <a href=’#notes’>Notes</a>. |
| **list**  string | Access-list or prefix-list name. Source router.access-list.name router.prefix-list.name. |
| **id**  string / required | Area entry IP address. |
| **nssa_default_information_originate**  string | Redistribute, advertise, or do not originate Type-7 default route into NSSA area.  **Choices:**   - `"enable"` - `"always"` - `"disable"` |
| **nssa_default_information_originate_metric**  integer | OSPF default metric. |
| **nssa_default_information_originate_metric_type**  string | OSPF metric type for default routes.  **Choices:**   - `"1"` - `"2"` |
| **nssa_redistribution**  string | Enable/disable redistribute into NSSA area.  **Choices:**   - `"enable"` - `"disable"` |
| **nssa_translator_role**  string | NSSA translator role type.  **Choices:**   - `"candidate"` - `"never"` - `"always"` |
| **range**  list / elements=dictionary | OSPF area range configuration. |
| **advertise**  string | Enable/disable advertise status.  **Choices:**   - `"disable"` - `"enable"` |
| **id**  integer / required | Range entry ID. see <a href=’#notes’>Notes</a>. |
| **prefix**  string | Prefix. |
| **substitute**  string | Substitute prefix. |
| **substitute_status**  string | Enable/disable substitute status.  **Choices:**   - `"enable"` - `"disable"` |
| **shortcut**  string | Enable/disable shortcut option.  **Choices:**   - `"disable"` - `"enable"` - `"default"` |
| **stub_type**  string | Stub summary setting.  **Choices:**   - `"no-summary"` - `"summary"` |
| **type**  string | Area type setting.  **Choices:**   - `"regular"` - `"nssa"` - `"stub"` |
| **virtual_link**  list / elements=dictionary | OSPF virtual link configuration. |
| **authentication**  string | Authentication type.  **Choices:**   - `"none"` - `"text"` - `"message-digest"` - `"md5"` |
| **authentication_key**  string | Authentication key. |
| **dead_interval**  integer | Dead interval. |
| **hello_interval**  integer | Hello interval. |
| **keychain**  string | Message-digest key-chain name. Source router.key-chain.name. |
| **md5_key**  string | MD5 key. |
| **md5_keychain**  string | Authentication MD5 key-chain name. Source router.key-chain.name. |
| **md5_keys**  list / elements=dictionary | MD5 key. |
| **id**  integer / required | Key ID (1 - 255). see <a href=’#notes’>Notes</a>. |
| **key_string**  string | Password for the key. |
| **name**  string / required | Virtual link entry name. |
| **peer**  string | Peer IP. |
| **retransmit_interval**  integer | Retransmit interval. |
| **transmit_delay**  integer | Transmit delay. |
| **auto_cost_ref_bandwidth**  integer | Reference bandwidth in terms of megabits per second. |
| **bfd**  string | Bidirectional Forwarding Detection (BFD).  **Choices:**   - `"enable"` - `"disable"` |
| **database_overflow**  string | Enable/disable database overflow.  **Choices:**   - `"enable"` - `"disable"` |
| **database_overflow_max_lsas**  integer | Database overflow maximum LSAs. |
| **database_overflow_time_to_recover**  integer | Database overflow time to recover (sec). |
| **default_information_metric**  integer | Default information metric. |
| **default_information_metric_type**  string | Default information metric type.  **Choices:**   - `"1"` - `"2"` |
| **default_information_originate**  string | Enable/disable generation of default route.  **Choices:**   - `"enable"` - `"always"` - `"disable"` |
| **default_information_route_map**  string | Default information route map. Source router.route-map.name. |
| **default_metric**  integer | Default metric of redistribute routes. |
| **distance**  integer | Distance of the route. |
| **distance_external**  integer | Administrative external distance. |
| **distance_inter_area**  integer | Administrative inter-area distance. |
| **distance_intra_area**  integer | Administrative intra-area distance. |
| **distribute_list**  list / elements=dictionary | Distribute list configuration. |
| **access_list**  string | Access list name. Source router.access-list.name. |
| **id**  integer / required | Distribute list entry ID. see <a href=’#notes’>Notes</a>. |
| **protocol**  string | Protocol type.  **Choices:**   - `"connected"` - `"static"` - `"rip"` |
| **distribute_list_in**  string | Filter incoming routes. Source router.access-list.name router.prefix-list.name. |
| **distribute_route_map_in**  string | Filter incoming external routes by route-map. Source router.route-map.name. |
| **log_neighbour_changes**  string | Log of OSPF neighbor changes.  **Choices:**   - `"enable"` - `"disable"` |
| **neighbor**  list / elements=dictionary | OSPF neighbor configuration are used when OSPF runs on non-broadcast media. |
| **cost**  integer | Cost of the interface, value range from 0 to 65535, 0 means auto-cost. |
| **id**  integer / required | Neighbor entry ID. see <a href=’#notes’>Notes</a>. |
| **ip**  string | Interface IP address of the neighbor. |
| **poll_interval**  integer | Poll interval time in seconds. |
| **priority**  integer | Priority. |
| **network**  list / elements=dictionary | OSPF network configuration. |
| **area**  string | Attach the network to area. |
| **comments**  string | Comment. |
| **id**  integer / required | Network entry ID. see <a href=’#notes’>Notes</a>. |
| **prefix**  string | Prefix. |
| **ospf_interface**  list / elements=dictionary | OSPF interface configuration. |
| **authentication**  string | Authentication type.  **Choices:**   - `"none"` - `"text"` - `"message-digest"` - `"md5"` |
| **authentication_key**  string | Authentication key. |
| **bfd**  string | Bidirectional Forwarding Detection (BFD).  **Choices:**   - `"global"` - `"enable"` - `"disable"` |
| **comments**  string | Comment. |
| **cost**  integer | Cost of the interface, value range from 0 to 65535, 0 means auto-cost. |
| **database_filter_out**  string | Enable/disable control of flooding out LSAs.  **Choices:**   - `"enable"` - `"disable"` |
| **dead_interval**  integer | Dead interval. |
| **hello_interval**  integer | Hello interval. |
| **hello_multiplier**  integer | Number of hello packets within dead interval. |
| **interface**  string | Configuration interface name. Source system.interface.name. |
| **ip**  string | IP address. |
| **keychain**  string | Message-digest key-chain name. Source router.key-chain.name. |
| **md5_key**  string | MD5 key. |
| **md5_keychain**  string | Authentication MD5 key-chain name. Source router.key-chain.name. |
| **md5_keys**  list / elements=dictionary | MD5 key. |
| **id**  integer / required | Key ID (1 - 255). see <a href=’#notes’>Notes</a>. |
| **key_string**  string | Password for the key. |
| **mtu**  integer | MTU for database description packets. |
| **mtu_ignore**  string | Enable/disable ignore MTU.  **Choices:**   - `"enable"` - `"disable"` |
| **name**  string / required | Interface entry name. |
| **network_type**  string | Network type.  **Choices:**   - `"broadcast"` - `"non-broadcast"` - `"point-to-point"` - `"point-to-multipoint"` - `"point-to-multipoint-non-broadcast"` |
| **prefix_length**  integer | Prefix length. |
| **priority**  integer | Priority. |
| **resync_timeout**  integer | Graceful restart neighbor resynchronization timeout. |
| **retransmit_interval**  integer | Retransmit interval. |
| **status**  string | Enable/disable status.  **Choices:**   - `"disable"` - `"enable"` |
| **transmit_delay**  integer | Transmit delay. |
| **passive_interface**  list / elements=dictionary | Passive interface configuration. |
| **name**  string / required | Passive interface name. Source system.interface.name. |
| **redistribute**  list / elements=dictionary | Redistribute configuration. |
| **metric**  integer | Redistribute metric setting. |
| **metric_type**  string | Metric type.  **Choices:**   - `"1"` - `"2"` |
| **name**  string / required | Redistribute name. |
| **routemap**  string | Route map name. Source router.route-map.name. |
| **status**  string | Status.  **Choices:**   - `"enable"` - `"disable"` |
| **tag**  integer | Tag value. |
| **restart_mode**  string | OSPF restart mode (graceful or LLS).  **Choices:**   - `"none"` - `"lls"` - `"graceful-restart"` |
| **restart_on_topology_change**  string | Enable/disable continuing graceful restart upon topology change.  **Choices:**   - `"enable"` - `"disable"` |
| **restart_period**  integer | Graceful restart period. |
| **rfc1583_compatible**  string | Enable/disable RFC1583 compatibility.  **Choices:**   - `"enable"` - `"disable"` |
| **router_id**  string | Router ID. |
| **spf_timers**  string | SPF calculation frequency. |
| **summary_address**  list / elements=dictionary | IP address summary configuration. |
| **advertise**  string | Enable/disable advertise status.  **Choices:**   - `"disable"` - `"enable"` |
| **id**  integer / required | Summary address entry ID. see <a href=’#notes’>Notes</a>. |
| **prefix**  string | Prefix. |
| **tag**  integer | Tag value. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_router_ospf_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_router_ospf_module.md#id5)

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
  - name: Configure OSPF.
    fortios_router_ospf:
      vdom:  "{{ vdom }}"
      router_ospf:
        abr_type: "cisco"
        area:
         -
            authentication: "none"
            comments: "<your_own_value>"
            default_cost: "10"
            filter_list:
             -
                direction: "in"
                id:  "10"
                list: "<your_own_value> (source router.access-list.name router.prefix-list.name)"
            id:  "12"
            nssa_default_information_originate: "enable"
            nssa_default_information_originate_metric: "10"
            nssa_default_information_originate_metric_type: "1"
            nssa_redistribution: "enable"
            nssa_translator_role: "candidate"
            range:
             -
                advertise: "disable"
                id:  "20"
                prefix: "<your_own_value>"
                substitute: "<your_own_value>"
                substitute_status: "enable"
            shortcut: "disable"
            stub_type: "no-summary"
            type: "regular"
            virtual_link:
             -
                authentication: "none"
                authentication_key: "<your_own_value>"
                dead_interval: "40"
                hello_interval: "10"
                keychain: "<your_own_value> (source router.key-chain.name)"
                md5_key: "<your_own_value>"
                md5_keychain: "<your_own_value> (source router.key-chain.name)"
                md5_keys:
                 -
                    id:  "36"
                    key_string: "<your_own_value>"
                name: "default_name_38"
                peer: "<your_own_value>"
                retransmit_interval: "5"
                transmit_delay: "1"
        auto_cost_ref_bandwidth: "1000"
        bfd: "enable"
        database_overflow: "enable"
        database_overflow_max_lsas: "10000"
        database_overflow_time_to_recover: "300"
        default_information_metric: "10"
        default_information_metric_type: "1"
        default_information_originate: "enable"
        default_information_route_map: "<your_own_value> (source router.route-map.name)"
        default_metric: "10"
        distance: "110"
        distance_external: "110"
        distance_inter_area: "110"
        distance_intra_area: "110"
        distribute_list:
         -
            access_list: "<your_own_value> (source router.access-list.name)"
            id:  "58"
            protocol: "connected"
        distribute_list_in: "<your_own_value> (source router.access-list.name router.prefix-list.name)"
        distribute_route_map_in: "<your_own_value> (source router.route-map.name)"
        log_neighbour_changes: "enable"
        neighbor:
         -
            cost: "0"
            id:  "65"
            ip: "<your_own_value>"
            poll_interval: "10"
            priority: "1"
        network:
         -
            area: "<your_own_value>"
            comments: "<your_own_value>"
            id:  "72"
            prefix: "<your_own_value>"
        ospf_interface:
         -
            authentication: "none"
            authentication_key: "<your_own_value>"
            bfd: "global"
            comments: "<your_own_value>"
            cost: "0"
            database_filter_out: "enable"
            dead_interval: "0"
            hello_interval: "0"
            hello_multiplier: "0"
            interface: "<your_own_value> (source system.interface.name)"
            ip: "<your_own_value>"
            keychain: "<your_own_value> (source router.key-chain.name)"
            md5_key: "<your_own_value>"
            md5_keychain: "<your_own_value> (source router.key-chain.name)"
            md5_keys:
             -
                id:  "90"
                key_string: "<your_own_value>"
            mtu: "0"
            mtu_ignore: "enable"
            name: "default_name_94"
            network_type: "broadcast"
            prefix_length: "0"
            priority: "1"
            resync_timeout: "40"
            retransmit_interval: "5"
            status: "disable"
            transmit_delay: "1"
        passive_interface:
         -
            name: "default_name_103 (source system.interface.name)"
        redistribute:
         -
            metric: "0"
            metric_type: "1"
            name: "default_name_107"
            routemap: "<your_own_value> (source router.route-map.name)"
            status: "enable"
            tag: "0"
        restart_mode: "none"
        restart_on_topology_change: "enable"
        restart_period: "120"
        rfc1583_compatible: "enable"
        router_id: "<your_own_value>"
        spf_timers: "<your_own_value>"
        summary_address:
         -
            advertise: "disable"
            id:  "119"
            prefix: "<your_own_value>"
            tag: "0"
```

## [Return Values](fortios_router_ospf_module.md#id6)

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
