---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_router_ospf6 module – Configure IPv6 OSPF in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_router_ospf6_module.html
fetched_at: 2026-07-28T02:26:50+00:00
---
# fortinet.fortios.fortios_router_ospf6 module – Configure IPv6 OSPF in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_router_ospf6_module.md#ansible-collections-fortinet-fortios-fortios-router-ospf6-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_router_ospf6`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_router_ospf6_module.md#synopsis)
- [Requirements](fortios_router_ospf6_module.md#requirements)
- [Parameters](fortios_router_ospf6_module.md#parameters)
- [Notes](fortios_router_ospf6_module.md#notes)
- [Examples](fortios_router_ospf6_module.md#examples)
- [Return Values](fortios_router_ospf6_module.md#return-values)

## [Synopsis](fortios_router_ospf6_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify router feature and ospf6 category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_router_ospf6_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_router_ospf6_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **router_ospf6**  dictionary | Configure IPv6 OSPF. |
| **abr_type**  string | Area border router type.  **Choices:**   - `"cisco"` - `"ibm"` - `"standard"` |
| **area**  list / elements=dictionary | OSPF6 area configuration. |
| **authentication**  string | Authentication mode.  **Choices:**   - `"none"` - `"ah"` - `"esp"` |
| **default_cost**  integer | Summary default cost of stub or NSSA area. |
| **id**  string / required | Area entry IP address. |
| **ipsec_auth_alg**  string | Authentication algorithm.  **Choices:**   - `"md5"` - `"sha1"` - `"sha256"` - `"sha384"` - `"sha512"` |
| **ipsec_enc_alg**  string | Encryption algorithm.  **Choices:**   - `"null"` - `"des"` - `"3des"` - `"aes128"` - `"aes192"` - `"aes256"` |
| **ipsec_keys**  list / elements=dictionary | IPsec authentication and encryption keys. |
| **auth_key**  string | Authentication key. |
| **enc_key**  string | Encryption key. |
| **spi**  integer / required | Security Parameters Index. see <a href=’#notes’>Notes</a>. |
| **key_rollover_interval**  integer | Key roll-over interval. |
| **nssa_default_information_originate**  string | Enable/disable originate type 7 default into NSSA area.  **Choices:**   - `"enable"` - `"disable"` |
| **nssa_default_information_originate_metric**  integer | OSPFv3 default metric. |
| **nssa_default_information_originate_metric_type**  string | OSPFv3 metric type for default routes.  **Choices:**   - `"1"` - `"2"` |
| **nssa_redistribution**  string | Enable/disable redistribute into NSSA area.  **Choices:**   - `"enable"` - `"disable"` |
| **nssa_translator_role**  string | NSSA translator role type.  **Choices:**   - `"candidate"` - `"never"` - `"always"` |
| **range**  list / elements=dictionary | OSPF6 area range configuration. |
| **advertise**  string | Enable/disable advertise status.  **Choices:**   - `"disable"` - `"enable"` |
| **id**  integer / required | Range entry ID. see <a href=’#notes’>Notes</a>. |
| **prefix6**  string | IPv6 prefix. |
| **stub_type**  string | Stub summary setting.  **Choices:**   - `"no-summary"` - `"summary"` |
| **type**  string | Area type setting.  **Choices:**   - `"regular"` - `"nssa"` - `"stub"` |
| **virtual_link**  list / elements=dictionary | OSPF6 virtual link configuration. |
| **authentication**  string | Authentication mode.  **Choices:**   - `"none"` - `"ah"` - `"esp"` - `"area"` |
| **dead_interval**  integer | Dead interval. |
| **hello_interval**  integer | Hello interval. |
| **ipsec_auth_alg**  string | Authentication algorithm.  **Choices:**   - `"md5"` - `"sha1"` - `"sha256"` - `"sha384"` - `"sha512"` |
| **ipsec_enc_alg**  string | Encryption algorithm.  **Choices:**   - `"null"` - `"des"` - `"3des"` - `"aes128"` - `"aes192"` - `"aes256"` |
| **ipsec_keys**  list / elements=dictionary | IPsec authentication and encryption keys. |
| **auth_key**  string | Authentication key. |
| **enc_key**  string | Encryption key. |
| **spi**  integer / required | Security Parameters Index. see <a href=’#notes’>Notes</a>. |
| **key_rollover_interval**  integer | Key roll-over interval. |
| **name**  string / required | Virtual link entry name. |
| **peer**  string | A.B.C.D, peer router ID. |
| **retransmit_interval**  integer | Retransmit interval. |
| **transmit_delay**  integer | Transmit delay. |
| **auto_cost_ref_bandwidth**  integer | Reference bandwidth in terms of megabits per second. |
| **bfd**  string | Enable/disable Bidirectional Forwarding Detection (BFD).  **Choices:**   - `"enable"` - `"disable"` |
| **default_information_metric**  integer | Default information metric. |
| **default_information_metric_type**  string | Default information metric type.  **Choices:**   - `"1"` - `"2"` |
| **default_information_originate**  string | Enable/disable generation of default route.  **Choices:**   - `"enable"` - `"always"` - `"disable"` |
| **default_information_route_map**  string | Default information route map. Source router.route-map.name. |
| **default_metric**  integer | Default metric of redistribute routes. |
| **log_neighbour_changes**  string | Log OSPFv3 neighbor changes.  **Choices:**   - `"enable"` - `"disable"` |
| **ospf6_interface**  list / elements=dictionary | OSPF6 interface configuration. |
| **area_id**  string | A.B.C.D, in IPv4 address format. |
| **authentication**  string | Authentication mode.  **Choices:**   - `"none"` - `"ah"` - `"esp"` - `"area"` |
| **bfd**  string | Enable/disable Bidirectional Forwarding Detection (BFD).  **Choices:**   - `"global"` - `"enable"` - `"disable"` |
| **cost**  integer | Cost of the interface, value range from 0 to 65535, 0 means auto-cost. |
| **dead_interval**  integer | Dead interval. |
| **hello_interval**  integer | Hello interval. |
| **interface**  string | Configuration interface name. Source system.interface.name. |
| **ipsec_auth_alg**  string | Authentication algorithm.  **Choices:**   - `"md5"` - `"sha1"` - `"sha256"` - `"sha384"` - `"sha512"` |
| **ipsec_enc_alg**  string | Encryption algorithm.  **Choices:**   - `"null"` - `"des"` - `"3des"` - `"aes128"` - `"aes192"` - `"aes256"` |
| **ipsec_keys**  list / elements=dictionary | IPsec authentication and encryption keys. |
| **auth_key**  string | Authentication key. |
| **enc_key**  string | Encryption key. |
| **spi**  integer / required | Security Parameters Index. see <a href=’#notes’>Notes</a>. |
| **key_rollover_interval**  integer | Key roll-over interval. |
| **mtu**  integer | MTU for OSPFv3 packets. |
| **mtu_ignore**  string | Enable/disable ignoring MTU field in DBD packets.  **Choices:**   - `"enable"` - `"disable"` |
| **name**  string / required | Interface entry name. |
| **neighbor**  list / elements=dictionary | OSPFv3 neighbors are used when OSPFv3 runs on non-broadcast media. |
| **cost**  integer | Cost of the interface, value range from 0 to 65535, 0 means auto-cost. |
| **ip6**  string / required | IPv6 link local address of the neighbor. |
| **poll_interval**  integer | Poll interval time in seconds. |
| **priority**  integer | Priority. |
| **network_type**  string | Network type.  **Choices:**   - `"broadcast"` - `"point-to-point"` - `"non-broadcast"` - `"point-to-multipoint"` - `"point-to-multipoint-non-broadcast"` |
| **priority**  integer | Priority. |
| **retransmit_interval**  integer | Retransmit interval. |
| **status**  string | Enable/disable OSPF6 routing on this interface.  **Choices:**   - `"disable"` - `"enable"` |
| **transmit_delay**  integer | Transmit delay. |
| **passive_interface**  list / elements=dictionary | Passive interface configuration. |
| **name**  string / required | Passive interface name. Source system.interface.name. |
| **redistribute**  list / elements=dictionary | Redistribute configuration. |
| **metric**  integer | Redistribute metric setting. |
| **metric_type**  string | Metric type.  **Choices:**   - `"1"` - `"2"` |
| **name**  string / required | Redistribute name. |
| **routemap**  string | Route map name. Source router.route-map.name. |
| **status**  string | Status.  **Choices:**   - `"enable"` - `"disable"` |
| **restart_mode**  string | OSPFv3 restart mode (graceful or none).  **Choices:**   - `"none"` - `"graceful-restart"` |
| **restart_on_topology_change**  string | Enable/disable continuing graceful restart upon topology change.  **Choices:**   - `"enable"` - `"disable"` |
| **restart_period**  integer | Graceful restart period in seconds. |
| **router_id**  string | A.B.C.D, in IPv4 address format. |
| **spf_timers**  string | SPF calculation frequency. |
| **summary_address**  list / elements=dictionary | IPv6 address summary configuration. |
| **advertise**  string | Enable/disable advertise status.  **Choices:**   - `"disable"` - `"enable"` |
| **id**  integer / required | Summary address entry ID. see <a href=’#notes’>Notes</a>. |
| **prefix6**  string | IPv6 prefix. |
| **tag**  integer | Tag value. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_router_ospf6_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_router_ospf6_module.md#id5)

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
  - name: Configure IPv6 OSPF.
    fortios_router_ospf6:
      vdom:  "{{ vdom }}"
      router_ospf6:
        abr_type: "cisco"
        area:
         -
            authentication: "none"
            default_cost: "10"
            id:  "7"
            ipsec_auth_alg: "md5"
            ipsec_enc_alg: "null"
            ipsec_keys:
             -
                auth_key: "<your_own_value>"
                enc_key: "<your_own_value>"
                spi: "<you_own_value>"
            key_rollover_interval: "300"
            nssa_default_information_originate: "enable"
            nssa_default_information_originate_metric: "10"
            nssa_default_information_originate_metric_type: "1"
            nssa_redistribution: "enable"
            nssa_translator_role: "candidate"
            range:
             -
                advertise: "disable"
                id:  "22"
                prefix6: "<your_own_value>"
            stub_type: "no-summary"
            type: "regular"
            virtual_link:
             -
                authentication: "none"
                dead_interval: "40"
                hello_interval: "10"
                ipsec_auth_alg: "md5"
                ipsec_enc_alg: "null"
                ipsec_keys:
                 -
                    auth_key: "<your_own_value>"
                    enc_key: "<your_own_value>"
                    spi: "<you_own_value>"
                key_rollover_interval: "300"
                name: "default_name_37"
                peer: "<your_own_value>"
                retransmit_interval: "5"
                transmit_delay: "1"
        auto_cost_ref_bandwidth: "1000"
        bfd: "enable"
        default_information_metric: "10"
        default_information_metric_type: "1"
        default_information_originate: "enable"
        default_information_route_map: "<your_own_value> (source router.route-map.name)"
        default_metric: "10"
        log_neighbour_changes: "enable"
        ospf6_interface:
         -
            area_id: "<your_own_value>"
            authentication: "none"
            bfd: "global"
            cost: "0"
            dead_interval: "0"
            hello_interval: "0"
            interface: "<your_own_value> (source system.interface.name)"
            ipsec_auth_alg: "md5"
            ipsec_enc_alg: "null"
            ipsec_keys:
             -
                auth_key: "<your_own_value>"
                enc_key: "<your_own_value>"
                spi: "<you_own_value>"
            key_rollover_interval: "300"
            mtu: "0"
            mtu_ignore: "enable"
            name: "default_name_66"
            neighbor:
             -
                cost: "0"
                ip6: "<your_own_value>"
                poll_interval: "10"
                priority: "1"
            network_type: "broadcast"
            priority: "1"
            retransmit_interval: "5"
            status: "disable"
            transmit_delay: "1"
        passive_interface:
         -
            name: "default_name_78 (source system.interface.name)"
        redistribute:
         -
            metric: "0"
            metric_type: "1"
            name: "default_name_82"
            routemap: "<your_own_value> (source router.route-map.name)"
            status: "enable"
        restart_mode: "none"
        restart_on_topology_change: "enable"
        restart_period: "120"
        router_id: "<your_own_value>"
        spf_timers: "<your_own_value>"
        summary_address:
         -
            advertise: "disable"
            id:  "92"
            prefix6: "<your_own_value>"
            tag: "0"
```

## [Return Values](fortios_router_ospf6_module.md#id6)

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
