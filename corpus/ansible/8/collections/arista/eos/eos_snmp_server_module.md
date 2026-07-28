---
collection: ansible
version: "8"
title: "arista.eos.eos_snmp_server module – Manages snmp_server resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/arista/eos/eos_snmp_server_module.html
fetched_at: 2026-07-28T01:11:15+00:00
---
# arista.eos.eos_snmp_server module – Manages snmp_server resource module

> **Note:**
>
> This module is part of the [arista.eos collection](https://galaxy.ansible.com/ui/repo/published/arista/eos/) (version 6.2.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install arista.eos`.
>
> To use it in a playbook, specify: `arista.eos.eos_snmp_server`.

New in arista.eos 3.2.0

- [Synopsis](eos_snmp_server_module.md#synopsis)
- [Parameters](eos_snmp_server_module.md#parameters)
- [Notes](eos_snmp_server_module.md#notes)
- [Examples](eos_snmp_server_module.md#examples)
- [Return Values](eos_snmp_server_module.md#return-values)

## [Synopsis](eos_snmp_server_module.md#id1)

- This module configures and manages the attributes of snmp_server on Arista EOS platforms.

Aliases: snmp_server

## [Parameters](eos_snmp_server_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | SNMP server configuration. |
| **acls**  list / elements=dictionary | ipv4/ipv6 access_lists |
| **acl**  string | acl name |
| **afi**  string | ipv4/ipv6  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **vrf**  string | vrf name |
| **chassis_id**  string | SNMP chassis identifier. |
| **communities**  list / elements=dictionary | Community name configuration. |
| **acl_v4**  string | standard access_list name |
| **acl_v6**  string | IPv6 access list name. |
| **name**  string | Community name |
| **ro**  boolean | Only reads are permitted.  **Choices:**   - `false` - `true` |
| **rw**  boolean | Read_write access  **Choices:**   - `false` - `true` |
| **view**  string | MIB view name |
| **contact**  string | Person to contact about the syste,. |
| **engineid**  dictionary | SNMPv3 engine ID configuration. |
| **local**  string | Local SNMP agent |
| **remote**  dictionary | Remote SNMP agent |
| **host**  string | Hostname or IP address of remote SNMP notification host |
| **id**  string | engine ID octet string |
| **udp_port**  integer | The remote SNMP notification host’s UDP port number. |
| **extension**  dictionary | Configure extension script to serve an OID range |
| **oneshot**  boolean | Use inefficient one_shot interface  **Choices:**   - `false` - `true` |
| **root_oid**  string | Extension root oid |
| **script_location**  string | script location |
| **groups**  list / elements=dictionary | SNMP USM group |
| **auth_privacy**  string | auth and privacy config. Valid when version = v3.  **Choices:**   - `"auth"` - `"noauth"` - `"priv"` |
| **context**  string | Specify a context to associate with the group |
| **group**  string | SNMP group for the user |
| **notify**  string | View to restrict notifications |
| **read**  string | View to restrict read access |
| **version**  string | snmp security group version  **Choices:**   - `"v1"` - `"v3"` - `"v2c"` |
| **write**  string | View to restrict write access |
| **hosts**  list / elements=dictionary | Notification destinations |
| **host**  string | Hostname or IP address of SNMP notification host. |
| **informs**  boolean | Use SNMP inform messages.  **Choices:**   - `false` - `true` |
| **traps**  boolean | Use SNMP trap messages  **Choices:**   - `false` - `true` |
| **udp_port**  integer | UDP destination port for notification messages. |
| **user**  string | Community or user name. |
| **version**  string | Notification message SNMP version.  **Choices:**   - `"1"` - `"2c"` - `"3 auth"` - `"3 noauth"` - `"3 priv"` |
| **vrf**  string | Specify the VRF in which the host is configured |
| **local_interface**  string | Configure the source interface for SNMP notifications. |
| **location**  string | The sysLocation string. |
| **notification**  integer | Maximum number of notifications in the log |
| **objects**  dictionary | when true Disable implementation of a group of objects |
| **mac_address_tables**  boolean | dot1dTpFdbTable, dot1qTpFdbTable  **Choices:**   - `false` - `true` |
| **route_tables**  boolean | ipCidrRouteTable, ipCidrRouteNumber, aristaFIBStats\*  **Choices:**   - `false` - `true` |
| **qos**  integer | Configure QoS parameters. |
| **qosmib**  integer | Set QOS_MIB counter update interval |
| **transmit**  integer | Maximum number of bytes in SNMP message (UDP/TCP payload) |
| **transport**  string | Enable snmpd transport layer protocol |
| **traps**  dictionary | Enable traps to all configured recipients. |
| **bgp**  dictionary | Enable Bgp traps. If set to enabled , all the traps are set. |
| **arista_backward_transition**  boolean | arista_backward_transition  **Choices:**   - `false` - `true` |
| **arista_established**  boolean | arista_established  **Choices:**   - `false` - `true` |
| **backward_transition**  boolean | backward_transition  **Choices:**   - `false` - `true` |
| **enabled**  boolean | All traps are set.  **Choices:**   - `false` - `true` |
| **established**  boolean | established.  **Choices:**   - `false` - `true` |
| **bridge**  dictionary | Enable Bridge traps. If set to enabled , all the traps are set. |
| **arista_mac_age**  boolean | arista_mac_age  **Choices:**   - `false` - `true` |
| **arista_mac_learn**  boolean | arista_mac_learn  **Choices:**   - `false` - `true` |
| **arista_mac_move**  boolean | arista_mac_move  **Choices:**   - `false` - `true` |
| **enabled**  boolean | All traps are set.  **Choices:**   - `false` - `true` |
| **capacity**  dictionary | Enable Capacity traps. If set to enabled , all the traps are set. |
| **arista_hardware_utilization_alert**  boolean | arista_hardware_utilization_alert  **Choices:**   - `false` - `true` |
| **enabled**  boolean | All traps are set.  **Choices:**   - `false` - `true` |
| **entity**  dictionary | Enable Entity traps. If set to enabled , all the traps are set. |
| **arista_ent_sensor_alarm**  boolean | arista_ent_sensor_alarm  **Choices:**   - `false` - `true` |
| **enabled**  boolean | All traps are set.  **Choices:**   - `false` - `true` |
| **ent_config_change**  boolean | ent_config_change  **Choices:**   - `false` - `true` |
| **ent_state_oper**  boolean | ent_state_oper  **Choices:**   - `false` - `true` |
| **ent_state_oper_disabled**  boolean | ent_state_oper_disabled.  **Choices:**   - `false` - `true` |
| **ent_state_oper_enabled**  boolean | ent_state_oper_enabled.  **Choices:**   - `false` - `true` |
| **external_alarm**  dictionary | Enable external alarm traps. If set to enabled , all the traps are set. |
| **arista_external_alarm_asserted_notif**  boolean | arista_external_alarm_asserted_notif  **Choices:**   - `false` - `true` |
| **arista_external_alarm_deasserted_notif**  boolean | arista_external_alarm_deasserted_notif  **Choices:**   - `false` - `true` |
| **enabled**  boolean | All traps are set.  **Choices:**   - `false` - `true` |
| **isis**  dictionary | Enable isis traps. If set to enabled , all the traps are set. |
| **adjacency_change**  boolean | adjacency_change  **Choices:**   - `false` - `true` |
| **area_mismatch**  boolean | area_mismatch  **Choices:**   - `false` - `true` |
| **attempt_to_exceed_max_sequence**  boolean | attempt_to_exceed_max_sequence  **Choices:**   - `false` - `true` |
| **authentication_type_failure**  boolean | authentication_type_failure.  **Choices:**   - `false` - `true` |
| **database_overload**  boolean | database_overload  **Choices:**   - `false` - `true` |
| **enabled**  boolean | All traps are set.  **Choices:**   - `false` - `true` |
| **own_lsp_purge**  boolean | own_lsp_purge  **Choices:**   - `false` - `true` |
| **rejected_adjacency**  boolean | rejected_adjacency  **Choices:**   - `false` - `true` |
| **sequence_number_skip**  boolean | sequence_number_skip.  **Choices:**   - `false` - `true` |
| **lldp**  dictionary | Enable Lldp traps. If set to enabled , all the traps are set. |
| **enabled**  boolean | All traps are set.  **Choices:**   - `false` - `true` |
| **rem_tables_change**  boolean | rem_tables_change  **Choices:**   - `false` - `true` |
| **mpls_ldp**  dictionary | Enable mpls_ldp traps. If set to enabled , all the traps are set. |
| **enabled**  boolean | All traps are set.  **Choices:**   - `false` - `true` |
| **mpls_ldp_session_down**  boolean | mpls_ldp_session_down  **Choices:**   - `false` - `true` |
| **mpls_ldp_session_up**  boolean | mpls_ldp_session_up  **Choices:**   - `false` - `true` |
| **msdp**  dictionary | Enable msdp traps. If set to enabled , all the traps are set. |
| **backward_transition**  boolean | backward_transition.  **Choices:**   - `false` - `true` |
| **enabled**  boolean | All traps are set.  **Choices:**   - `false` - `true` |
| **established**  boolean | established.  **Choices:**   - `false` - `true` |
| **ospf**  dictionary | Enable Ospf traps. If set to enabled , all the traps are set. |
| **enabled**  boolean | All traps are set.  **Choices:**   - `false` - `true` |
| **if_auth_failure**  boolean | if_auth_failure  **Choices:**   - `false` - `true` |
| **if_config_error**  boolean | if_config_error  **Choices:**   - `false` - `true` |
| **if_state_change**  boolean | if_state_change  **Choices:**   - `false` - `true` |
| **nbr_state_change**  boolean | nbr_state_change.  **Choices:**   - `false` - `true` |
| **ospfv3**  dictionary | Enable Ospfv3 traps. If set to enabled , all the traps are set. |
| **enabled**  boolean | All traps are set.  **Choices:**   - `false` - `true` |
| **if_config_error**  boolean | if_config_error  **Choices:**   - `false` - `true` |
| **if_rx_bad_packet**  boolean | if_rx_bad_packet  **Choices:**   - `false` - `true` |
| **if_state_change**  boolean | if_state_change  **Choices:**   - `false` - `true` |
| **nbr_restart_helper_status_change**  boolean | Enable ospfv3NbrRestartHelperStatusChange trap  **Choices:**   - `false` - `true` |
| **nbr_state_change**  boolean | nbr_state_change.  **Choices:**   - `false` - `true` |
| **nssa_translator_status_change**  boolean | Enable ospfv3NssaTranslatorStatusChange trap  **Choices:**   - `false` - `true` |
| **restart_status_change**  boolean | restart_status_change  **Choices:**   - `false` - `true` |
| **pim**  dictionary | Enable Pim traps. If set to enabled , all the traps are set. |
| **enabled**  boolean | All traps are set.  **Choices:**   - `false` - `true` |
| **neighbor_loss**  boolean | neighbor_loss  **Choices:**   - `false` - `true` |
| **snmp**  dictionary | Enable snmp traps. If set to enabled , all the traps are set. |
| **authentication**  boolean | authentication  **Choices:**   - `false` - `true` |
| **enabled**  boolean | All traps are set.  **Choices:**   - `false` - `true` |
| **link_down**  boolean | link_down  **Choices:**   - `false` - `true` |
| **link_up**  boolean | link_up  **Choices:**   - `false` - `true` |
| **snmpConfigManEvent**  dictionary | Enable snmpConfigManEvent traps. If set to enabled , all the traps are set. |
| **arista_config_man_event**  boolean | arista_config_man_event  **Choices:**   - `false` - `true` |
| **enabled**  boolean | All traps are set.  **Choices:**   - `false` - `true` |
| **switchover**  dictionary | Enable switchover traps. If set to enabled , all the traps are set. |
| **arista_redundancy_switch_over_notif**  boolean | arista_redundancy_switch_over_notif  **Choices:**   - `false` - `true` |
| **enabled**  boolean | All traps are set.  **Choices:**   - `false` - `true` |
| **test**  dictionary | Enable test traps. If set to enabled , all the traps are set. |
| **arista_test_notification**  boolean | arista_test_notification  **Choices:**   - `false` - `true` |
| **enabled**  boolean | All traps are set.  **Choices:**   - `false` - `true` |
| **vrrp**  dictionary | Enable vrrp traps. If set to enabled , all the traps are set. |
| **enabled**  boolean | All traps are set.  **Choices:**   - `false` - `true` |
| **trap_new_master**  boolean | vrrp  **Choices:**   - `false` - `true` |
| **users**  list / elements=dictionary | SNMP user configuration. |
| **auth**  dictionary | User authentication settings |
| **algorithm**  string | algorithm for authentication |
| **auth_passphrase**  string | authentication passphrase hex string |
| **encryption**  string | algorithm for encryption. |
| **priv_passphrase**  string | privacy passphrase hexstring |
| **group**  string | SNMP group for the user. |
| **localized**  dictionary | localized auth and privacy passphrases. |
| **algorithm**  string | algorithm for authentication |
| **auth_passphrase**  string | authentication passphrase hex string |
| **encryption**  string | algorithm for encryption. |
| **engineid**  string | Engine id |
| **priv_passphrase**  string | privacy passphrase hexstring |
| **remote**  string | System where an SNMPv3 user is hosted |
| **udp_port**  integer | UDP port used by the remote SNMP system |
| **user**  string | SNMP user name |
| **version**  string | snmp security version  **Choices:**   - `"v1"` - `"v2c"` - `"v3"` |
| **views**  list / elements=dictionary | SNMPv2 MIB view configuration |
| **action**  string | Action to be performed.  **Choices:**   - `"excluded"` - `"included"` |
| **mib**  string | SNMP MIB name |
| **view**  string | SNMP view name |
| **vrfs**  list / elements=dictionary | Specify the VRF in which the source address is used |
| **local_interface**  string | Configure the source interface for SNMP notifications |
| **vrf**  string | vrf name. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the EOS device by executing the command **show running_config | section snmp_server**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  The states *replaced* and *overridden* have identical behaviour for this module.  Please refer to examples for more details.  **Choices:**   - `"deleted"` - `"merged"` ← (default) - `"overridden"` - `"replaced"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](eos_snmp_server_module.md#id3)

> **Note:**
>
> - Tested against Arista EOS 4.24.6F
> - This module works with connection `network_cli` and `httpapi`.

## [Examples](eos_snmp_server_module.md#id4)

```yaml+jinja
# Using merged:

# Before State
# eos#show running-config | section snmp-server
# eos#

- name: merge given snmp_server configuration
  arista.eos.eos_snmp_server:
    config:
      communities:
        - name: "comm3"
          acl_v6: "list1"
          view: "view1"
        - name: "comm4"
          acl_v4: "list3"
          view: "view1"
        - name: "comm5"
          acl_v4: "list4"
          ro: true
      contact: "admin"
      engineid:
        remote:
          host: 1.1.1.1
          id: "1234567"
      groups:
        - group: "group1"
          version: "v1"
          read: "view1"
        - group: "group2"
          version: "v3"
          auth_privacy: "priv"
          notify: "view1"
          write: "view2"
      hosts:
        - host: "host02"
          user: "user01"
          udp_port: 23
          version: "2c"
        - host: "host01"
          user: "user01"
          udp_port: 23
          version: "3 priv"
      traps:
        capacity:
          arista_hardware_utilization_alert: true
        bgp:
          enabled: true
        external_alarm:
          arista_external_alarm_deasserted_notif: true
          arista_external_alarm_asserted_notif: true
      vrfs:
        - vrf: "vrf01"
          local_interface: "Ethernet1"

# After state
# eos#show running-config | section snmp-server
# snmp-server community comm3 view view1 ipv6 list1
# snmp-server community comm4 view view1 list3
# snmp-server community comm5 ro list4
# snmp-server group group1 v1 read view1
# snmp-server group group2 v3 priv write view2 notify view1
# snmp-server host host02 version 2c user01 udp-port 23
# snmp-server host host01 version 3 priv user01 udp-port 23
# snmp-server vrf vrf01 local-interface Ethernet1
# snmp-server contact admin
# snmp-server enable traps bgp
# snmp-server enable traps capacity arista-hardware-utilization-alert
# snmp-server enable traps external-alarm arista-external-alarm-asserted-notif arista-external-alarm-deasserted-notif
#
# Module Execution
#
# "after": {
#         "communities": [
#             {
#                 "acl_v6": "list1",
#                 "name": "comm3",
#                 "ro": true,
#                 "view": "view1"
#             },
#             {
#                 "acl_v4": "list3",
#                 "name": "comm4",
#                 "ro": true,
#                 "view": "view1"
#             },
#             {
#                 "acl_v4": "list4",
#                 "name": "comm5",
#                 "ro": true
#             }
#         ],
#         "contact": "admin",
#         "groups": [
#             {
#                 "group": "group1",
#                 "read": "view1",
#                 "version": "v1"
#             },
#             {
#                 "auth_privacy": "priv",
#                 "group": "group2",
#                 "notify": "view1",
#                 "version": "v3",
#                 "write": "view2"
#             }
#         ],
#         "hosts": [
#             {
#                 "host": "host01",
#                 "udp_port": 23,
#                 "user": "user01",
#                 "version": "3 priv"
#             },
#             {
#                 "host": "host02",
#                 "udp_port": 23,
#                 "user": "user01",
#                 "version": "2c"
#             }
#         ],
#         "traps": {
#             "bgp": {
#                 "enabled": true
#             },
#             "capacity": {
#                 "arista_hardware_utilization_alert": true
#             },
#             "external_alarm": {
#                 "arista_external_alarm_asserted_notif": true,
#                 "arista_external_alarm_deasserted_notif": true
#             }
#         },
#         "vrfs": [
#             {
#                 "local_interface": "Ethernet1",
#                 "vrf": "vrf01"
#             }
#         ]
#     },
#     "before": {},
#     "changed": true,
#     "commands": [
#         "snmp-server community comm3 view view1 ipv6 list1",
#         "snmp-server community comm4 view view1 list3",
#         "snmp-server community comm5 ro list4",
#         "snmp-server group group1 v1 read view1",
#         "snmp-server group group2 v3 priv write view2 notify view1",
#         "snmp-server host host02 version 2c user01 udp-port 23",
#         "snmp-server host host01 version 3 priv user01 udp-port 23",
#         "snmp-server vrf vrf01 local-interface Ethernet1",
#         "snmp-server contact admin",
#         "snmp-server engineID remote 1.1.1.1 1234567",
#         "snmp-server enable traps bgp",
#         "snmp-server enable traps capacity arista-hardware-utilization-alert",
#         "snmp-server enable traps external-alarm arista-external-alarm-asserted-notif arista-external-alarm-deasserted-notif"
#     ],
#

# Using replaced:

# Before State:
# eos#show running-config | section snmp-server
# snmp-server community comm3 view view1 ipv6 list1
# snmp-server community comm4 view view1 list3
# snmp-server community comm5 ro list4
# snmp-server group group1 v1 read view1
# snmp-server group group2 v3 priv write view2 notify view1
# snmp-server host host02 version 2c user01 udp-port 23
# snmp-server host host01 version 3 priv user01 udp-port 23
# snmp-server vrf vrf01 local-interface Ethernet1
# snmp-server contact admin
# snmp-server enable traps bgp
# snmp-server enable traps capacity arista-hardware-utilization-alert
# snmp-server enable traps external-alarm arista-external-alarm-asserted-notif arista-external-alarm-deasserted-notif

- name: Replace given snmp_server configuration
  become: true
  register: result
  arista.eos.eos_snmp_server: &replaced
    state: replaced
    config:
      communities:
        - name: "comm3"
          acl_v6: "list1"
          view: "view1"
        - name: "replacecomm"
          acl_v4: "list4"
      extension:
        root_oid: "123456"
        script_location: "flash:"
      traps:
        test:
          arista_test_notification: true
        bgp:
          enabled: true
      vrfs:
        - vrf: "vrf_replace"
          local_interface: "Ethernet1"

# After State:

# eos#show running-config | section snmp-server
# snmp-server community comm3 view view1 ipv6 list1
# snmp-server community replacecomm list4
# snmp-server vrf vrf_replace local-interface Ethernet1
# snmp-server extension 123456 flash:
# snmp-server enable traps test arista-test-notification
# snmp-server enable traps bgp

# Module Execution:
#    "after": {
#        "communities": [
#            {
#                "acl_v6": "list1",
#                "name": "comm3",
#                "ro": true,
#                "view": "view1"
#            },
#            {
#                "acl_v4": "list4",
#                "name": "replacecomm",
#                "ro": true
#            }
#        ],
#        "extension": {
#            "root_oid": "0.123456",
#            "script_location": "flash:"
#        },
#        "traps": {
#            "bgp": {
#                "enabled": true
#            },
#            "test": {
#                "arista_test_notification": true
#            }
#        },
#        "vrfs": [
#            {
#                "local_interface": "Ethernet1",
#                "vrf": "vrf_replace"
#            }
#        ]
#    },
#    "before": {
#        "communities": [
#            {
#                "acl_v6": "list1",
#                "name": "comm3",
#                "ro": true,
#                "view": "view1"
#            },
#            {
#                "acl_v4": "list3",
#                "name": "comm4",
#                "ro": true,
#                "view": "view1"
#            },
#            {
#                "acl_v4": "list4",
#                "name": "comm5",
#                "ro": true
#            }
#        ],
#        "contact": "admin",
#        "groups": [
#            {
#                "group": "group1",
#                "read": "view1",
#                "version": "v1"
#            },
#            {
#                "auth_privacy": "priv",
#                "group": "group2",
#                "notify": "view1",
#                "version": "v3",
#                "write": "view2"
#            }
#        ],
#        "hosts": [
#            {
#                "host": "host01",
#                "udp_port": 23,
#                "user": "user01",
#                "version": "3 priv"
#            },
#            {
#                "host": "host02",
#                "udp_port": 23,
#                "user": "user01",
#                "version": "2c"
#            }
#        ],
#        "traps": {
#            "bgp": {
#                "enabled": true
#            },
#            "capacity": {
#                "arista_hardware_utilization_alert": true
#            },
#            "external_alarm": {
#                "arista_external_alarm_asserted_notif": true,
#                "arista_external_alarm_deasserted_notif": true
#            }
#        },
#        "vrfs": [
#            {
#                "local_interface": "Ethernet1",
#                "vrf": "vrf01"
#            }
#        ]
#    },
#    "changed": true,
#    "commands": [
#        "snmp-server community comm3 view view1 ipv6 list1",
#        "snmp-server community replacecomm list4",
#        "no snmp-server community comm4 view view1 ro list3",
#        "no snmp-server community comm5 ro list4",
#        "no snmp-server group group1 v1 read view1",
#        "no snmp-server group group2 v3 priv write view2 notify view1",
#        "no snmp-server host host01 version 3 priv user01 udp-port 23",
#        "no snmp-server host host02 version 2c user01 udp-port 23",
#        "snmp-server vrf vrf_replace local-interface Ethernet1",
#        "no snmp-server vrf vrf01 local-interface Ethernet1",
#        "snmp-server extension 123456 flash:",
#        "default snmp-server enable traps capacity arista-hardware-utilization-alert",
#        "default snmp-server enable traps external-alarm arista-external-alarm-asserted-notif arista-external-alarm-deasserted-notif",
#        "snmp-server enable traps test arista-test-notification",
#        "no snmp-server contact admin"
#    ],

# Using overridden:
# Before State:
# eos#show running-config | section snmp-server
# snmp-server community comm3 view view1 ipv6 list1
# snmp-server community comm4 view view1 list3
# snmp-server community comm5 ro list4
# snmp-server group group1 v1 read view1
# snmp-server group group2 v3 priv write view2 notify view1
# snmp-server host host02 version 2c user01 udp-port 23
# snmp-server host host01 version 3 priv user01 udp-port 23
# snmp-server vrf vrf01 local-interface Ethernet1
# snmp-server contact admin
# snmp-server enable traps bgp
# snmp-server enable traps capacity arista-hardware-utilization-alert
# snmp-server enable traps external-alarm arista-external-alarm-asserted-notif arista-external-alarm-deasserted-notif

- name: Override given snmp_server configuration
  arista.eos.eos_snmp_server:
    state: overridden
    config:
      communities:
        - name: "comm3"
          acl_v6: "list1"
          view: "view1"
        - name: "replacecomm"
          acl_v4: "list4"
      extension:
        root_oid: "123456"
        script_location: "flash:"
      traps:
        test:
          arista_test_notification: true
        bgp:
          enabled: true
      vrfs:
        - vrf: "vrf_replace"
          local_interface: "Ethernet1"

# After State:

# eos#show running-config | section snmp-server
# snmp-server community comm3 view view1 ipv6 list1
# snmp-server community replacecomm list4
# snmp-server vrf vrf_replace local-interface Ethernet1
# snmp-server extension 123456 flash:
# snmp-server enable traps test arista-test-notification
# snmp-server enable traps bgp

# Module Execution:
#    "after": {
#        "communities": [
#            {
#                "acl_v6": "list1",
#                "name": "comm3",
#                "ro": true,
#                "view": "view1"
#            },
#            {
#                "acl_v4": "list4",
#                "name": "replacecomm",
#                "ro": true
#            }
#        ],
#        "extension": {
#            "root_oid": "0.123456",
#            "script_location": "flash:"
#        },
#        "traps": {
#            "bgp": {
#                "enabled": true
#            },
#            "test": {
#                "arista_test_notification": true
#            }
#        },
#        "vrfs": [
#            {
#                "local_interface": "Ethernet1",
#                "vrf": "vrf_replace"
#            }
#        ]
#    },
#    "before": {
#        "communities": [
#            {
#                "acl_v6": "list1",
#                "name": "comm3",
#                "ro": true,
#                "view": "view1"
#            },
#            {
#                "acl_v4": "list3",
#                "name": "comm4",
#                "ro": true,
#                "view": "view1"
#            },
#            {
#                "acl_v4": "list4",
#                "name": "comm5",
#                "ro": true
#            }
#        ],
#        "contact": "admin",
#        "groups": [
#            {
#                "group": "group1",
#                "read": "view1",
#                "version": "v1"
#            },
#            {
#                "auth_privacy": "priv",
#                "group": "group2",
#                "notify": "view1",
#                "version": "v3",
#                "write": "view2"
#            }
#        ],
#        "hosts": [
#            {
#                "host": "host01",
#                "udp_port": 23,
#                "user": "user01",
#                "version": "3 priv"
#            },
#            {
#                "host": "host02",
#                "udp_port": 23,
#                "user": "user01",
#                "version": "2c"
#            }
#        ],
#        "traps": {
#            "bgp": {
#                "enabled": true
#            },
#            "capacity": {
#                "arista_hardware_utilization_alert": true
#            },
#            "external_alarm": {
#                "arista_external_alarm_asserted_notif": true,
#                "arista_external_alarm_deasserted_notif": true
#            }
#        },
#        "vrfs": [
#            {
#                "local_interface": "Ethernet1",
#                "vrf": "vrf01"
#            }
#        ]
#    },
#    "changed": true,
#    "commands": [
#        "snmp-server community comm3 view view1 ipv6 list1",
#        "snmp-server community replacecomm list4",
#        "no snmp-server community comm4 view view1 ro list3",
#        "no snmp-server community comm5 ro list4",
#        "no snmp-server group group1 v1 read view1",
#        "no snmp-server group group2 v3 priv write view2 notify view1",
#        "no snmp-server host host01 version 3 priv user01 udp-port 23",
#        "no snmp-server host host02 version 2c user01 udp-port 23",
#        "snmp-server vrf vrf_replace local-interface Ethernet1",
#        "no snmp-server vrf vrf01 local-interface Ethernet1",
#        "snmp-server extension 123456 flash:",
#        "default snmp-server enable traps capacity arista-hardware-utilization-alert",
#        "default snmp-server enable traps external-alarm arista-external-alarm-asserted-notif arista-external-alarm-deasserted-notif",
#        "snmp-server enable traps test arista-test-notification",
#        "no snmp-server contact admin"
#    ],

# Using deleted:
# Before State:
# eos#show running-config | section snmp-server
# snmp-server community comm3 view view1 ipv6 list1
# snmp-server community comm4 view view1 list3
# snmp-server community comm5 ro list4
# snmp-server group group1 v1 read view1
# snmp-server group group2 v3 priv write view2 notify view1
# snmp-server host host02 version 2c user01 udp-port 23
# snmp-server host host01 version 3 priv user01 udp-port 23
# snmp-server vrf vrf01 local-interface Ethernet1
# snmp-server contact admin
# snmp-server enable traps bgp
# snmp-server enable traps capacity arista-hardware-utilization-alert
# snmp-server enable traps external-alarm arista-external-alarm-asserted-notif arista-external-alarm-deasserted-notif

- name: Delete given snmp_server configuration
  arista.eos.eos_snmp_server:
    state: deleted

# After State:
# eos#show running-config | section snmp-server
#

# Module Execution:
#   "after": {},
#    "before": {
#        "communities": [
#            {
#                "acl_v6": "list1",
#                "name": "comm3",
#                "ro": true,
#                "view": "view1"
#            },
#            {
#                "acl_v4": "list3",
#                "name": "comm4",
#                "ro": true,
#                "view": "view1"
#            },
#            {
#                "acl_v4": "list4",
#                "name": "comm5",
#                "ro": true
#            }
#        ],
#        "contact": "admin",
#        "groups": [
#            {
#                "group": "group1",
#                "read": "view1",
#                "version": "v1"
#            },
#            {
#                "auth_privacy": "priv",
#                "group": "group2",
#                "notify": "view1",
#                "version": "v3",
#                "write": "view2"
#            }
#        ],
#        "hosts": [
#            {
#                "host": "host01",
#                "udp_port": 23,
#                "user": "user01",
#                "version": "3 priv"
#            },
#            {
#                "host": "host02",
#                "udp_port": 23,
#                "user": "user01",
#                "version": "2c"
#            }
#        ],
#        "traps": {
#            "bgp": {
#                "enabled": true
#            },
#            "capacity": {
#                "arista_hardware_utilization_alert": true
#            },
#            "external_alarm": {
#                "arista_external_alarm_asserted_notif": true,
#                "arista_external_alarm_deasserted_notif": true
#            }
#        },
#        "vrfs": [
#            {
#                "local_interface": "Ethernet1",
#                "vrf": "vrf01"
#            }
#        ]
#    },
#    "changed": true,
#    "commands": [
#        "no snmp-server community comm3 view view1 ro ipv6 list1",
#        "no snmp-server community comm4 view view1 ro list3",
#        "no snmp-server community comm5 ro list4",
#        "no snmp-server group group1 v1 read view1",
#        "no snmp-server group group2 v3 priv write view2 notify view1",
#        "no snmp-server host host01 version 3 priv user01 udp-port 23",
#        "no snmp-server host host02 version 2c user01 udp-port 23",
#        "no snmp-server vrf vrf01 local-interface Ethernet1",
#        "no snmp-server contact admin",
#        "default snmp-server enable traps bgp",
#        "default snmp-server enable traps capacity arista-hardware-utilization-alert",
#        "default snmp-server enable traps external-alarm arista-external-alarm-asserted-notif arista-external-alarm-deasserted-notif"
#    ],
#

# Using parsed:

# _parsed.cfg
# snmp-server contact admin
# snmp-server vrf vrf01 local-interface Ethernet1
# snmp-server community comm3 view view1 ro ipv6 list1
# snmp-server community comm4 view view1 ro list3
# snmp-server community comm5 ro list4
# snmp-server group group1 v1 read view1
# snmp-server group group2 v3 priv write view2 notify view1
# snmp-server host host01 version 3 priv user01 udp-port 23
# snmp-server host host02 version 2c user01 udp-port 23
# snmp-server enable traps bgp
# snmp-server enable traps capacity arista-hardware-utilization-alert
# snmp-server enable traps external-alarm arista-external-alarm-asserted-notif
# snmp-server enable traps external-alarm arista-external-alarm-deasserted-notif

- name: Provide the running configuration for parsing (config to be parsed)
  arista.eos.eos_snmp_server:
    running_config: "{{ lookup('file', '_parsed.cfg') }}"
    state: parsed

# Module Execution:
#     "parsed": {
#         "communities": [
#             {
#                 "acl_v6": "list1",
#                 "name": "comm3",
#                 "ro": true,
#                 "view": "view1"
#             },
#             {
#                 "acl_v4": "list3",
#                 "name": "comm4",
#                 "ro": true,
#                 "view": "view1"
#             },
#             {
#                 "acl_v4": "list4",
#                 "name": "comm5",
#                 "ro": true
#             }
#         ],
#         "contact": "admin",
#         "groups": [
#             {
#                 "group": "group1",
#                 "read": "view1",
#                 "version": "v1"
#             },
#             {
#                 "auth_privacy": "priv",
#                 "group": "group2",
#                 "notify": "view1",
#                 "version": "v3",
#                 "write": "view2"
#             }
#         ],
#         "hosts": [
#             {
#                 "host": "host01",
#                 "udp_port": 23,
#                 "user": "user01",
#                 "version": "3 priv"
#             },
#             {
#                 "host": "host02",
#                 "udp_port": 23,
#                 "user": "user01",
#                 "version": "2c"
#             }
#         ],
#         "traps": {
#             "bgp": {
#                 "enabled": true
#             },
#             "capacity": {
#                 "arista_hardware_utilization_alert": true
#             },
#             "external_alarm": {
#                 "arista_external_alarm_asserted_notif": true,
#                 "arista_external_alarm_deasserted_notif": true
#             }
#         },
#         "vrfs": [
#             {
#                 "local_interface": "Ethernet1",
#                 "vrf": "vrf01"
#             }
#         ]
#   }

# Using rendered:
- name: Render given snmp_server configuration
  arista.eos.eos_snmp_server:
    state: "rendered"
    config:
      communities:
        - name: "comm3"
          acl_v6: "list1"
          view: "view1"
        - name: "comm4"
          acl_v4: "list3"
          view: "view1"
        - name: "comm5"
          acl_v4: "list4"
          ro: true
      contact: "admin"
      engineid:
        remote:
          host: 1.1.1.1
          id: "1234567"
      groups:
        - group: "group1"
          version: "v1"
          read: "view1"
        - group: "group2"
          version: "v3"
          auth_privacy: "priv"
          notify: "view1"
          write: "view2"
      hosts:
        - host: "host02"
          user: "user01"
          udp_port: 23
          version: "2c"
        - host: "host01"
          user: "user01"
          udp_port: 23
          version: "3 priv"
      traps:
        capacity:
          arista_hardware_utilization_alert: true
        bgp:
          enabled: true
        external_alarm:
          arista_external_alarm_deasserted_notif: true
          arista_external_alarm_asserted_notif: true
      vrfs:
        - vrf: "vrf01"
          local_interface: "Ethernet1"

# Module Execution:
#    "rendered": [
#        "snmp-server community comm3 view view1 ipv6 list1",
#        "snmp-server community comm4 view view1 list3",
#        "snmp-server community comm5 ro list4",
#        "snmp-server group group1 v1 read view1",
#        "snmp-server group group2 v3 priv write view2 notify view1",
#        "snmp-server host host02 version 2c user01 udp-port 23",
#        "snmp-server host host01 version 3 priv user01 udp-port 23",
#        "snmp-server vrf vrf01 local-interface Ethernet1",
#        "snmp-server contact admin",
#        "snmp-server engineID remote 1.1.1.1 1234567",
#        "snmp-server enable traps bgp",
#        "snmp-server enable traps capacity arista-hardware-utilization-alert",
#        "snmp-server enable traps external-alarm arista-external-alarm-asserted-notif arista-external-alarm-deasserted-notif"
#    ]

# using gathered:

# eos#show running-config | section snmp-server
# snmp-server community comm3 view view1 ipv6 list1
# snmp-server community comm4 view view1 list3
# snmp-server community comm5 ro list4
# snmp-server group group1 v1 read view1
# snmp-server group group2 v3 priv write view2 notify view1
# snmp-server host host02 version 2c user01 udp-port 23
# snmp-server host host01 version 3 priv user01 udp-port 23
# snmp-server vrf vrf01 local-interface Ethernet1
# snmp-server contact admin
# snmp-server enable traps bgp
# snmp-server enable traps capacity arista-hardware-utilization-alert
# snmp-server enable traps external-alarm arista-external-alarm-asserted-notif arista-external-alarm-deasserted-notif

- name: Gathered the provided configuration with the exisiting running configuration
  arista.eos.eos_snmp_server:
    config:
    state: gathered

# Module Execution:
#     "gathered": {
#         "communities": [
#             {
#                 "acl_v6": "list1",
#                 "name": "comm3",
#                 "ro": true,
#                 "view": "view1"
#             },
#             {
#                 "acl_v4": "list3",
#                 "name": "comm4",
#                 "ro": true,
#                 "view": "view1"
#             },
#             {
#                 "acl_v4": "list4",
#                 "name": "comm5",
#                 "ro": true
#             }
#         ],
#         "contact": "admin",
#         "groups": [
#             {
#                 "group": "group1",
#                 "read": "view1",
#                 "version": "v1"
#             },
#             {
#                 "auth_privacy": "priv",
#                 "group": "group2",
#                 "notify": "view1",
#                 "version": "v3",
#                 "write": "view2"
#             }
#         ],
#         "hosts": [
#             {
#                 "host": "host01",
#                 "udp_port": 23,
#                 "user": "user01",
#                 "version": "3 priv"
#             },
#             {
#                 "host": "host02",
#                 "udp_port": 23,
#                 "user": "user01",
#                 "version": "2c"
#             }
#         ],
#         "traps": {
#             "bgp": {
#                 "enabled": true
#             },
#             "capacity": {
#                 "arista_hardware_utilization_alert": true
#             },
#             "external_alarm": {
#                 "arista_external_alarm_asserted_notif": true,
#                 "arista_external_alarm_deasserted_notif": true
#             }
#         },
#         "vrfs": [
#             {
#                 "local_interface": "Ethernet1",
#                 "vrf": "vrf01"
#             }
#         ]
#     },
```

## [Return Values](eos_snmp_server_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  **Returned:** when changed  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `["snmp-server community comm3 view view1 ipv6 list1", "snmp-server community comm4 view view1 list3", "snmp-server community comm5 ro list4", "snmp-server group group1 v1 read view1", "snmp-server group group2 v3 priv write view2 notify view1", "snmp-server host host02 version 2c user01 udp-port 23", "snmp-server host host01 version 3 priv user01 udp-port 23", "snmp-server vrf vrf01 local-interface Ethernet1", "snmp-server contact admin", "snmp-server engineID remote 1.1.1.1 1234567", "snmp-server enable traps bgp", "snmp-server enable traps capacity arista-hardware-utilization-alert", "snmp-server enable traps external-alarm arista-external-alarm-asserted-notif arista-external-alarm-deasserted-notif"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when *state* is `gathered`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  **Returned:** when *state* is `parsed`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  **Returned:** when *state* is `rendered`  **Sample:** `["snmp-server community comm3 view view1 ipv6 list1", "snmp-server community comm4 view view1 list3", "snmp-server community comm5 ro list4", "snmp-server group group1 v1 read view1", "snmp-server group group2 v3 priv write view2 notify view1", "snmp-server host host02 version 2c user01 udp-port 23", "snmp-server host host01 version 3 priv user01 udp-port 23", "snmp-server vrf vrf01 local-interface Ethernet1", "snmp-server contact admin", "snmp-server engineID remote 1.1.1.1 1234567", "snmp-server enable traps bgp", "snmp-server enable traps capacity arista-hardware-utilization-alert", "snmp-server enable traps external-alarm arista-external-alarm-asserted-notif arista-external-alarm-deasserted-notif"]` |

### Authors

- Gomathi Selvi Srinivasan (@GomathiselviS)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/arista.eos)
