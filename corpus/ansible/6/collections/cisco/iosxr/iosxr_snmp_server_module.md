---
collection: ansible
version: "6"
title: "cisco.iosxr.iosxr_snmp_server module – Resource module to configure snmp server."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/iosxr/iosxr_snmp_server_module.html
fetched_at: 2026-07-27T16:55:56+00:00
---
# cisco.iosxr.iosxr_snmp_server module – Resource module to configure snmp server.

> **Note:**
>
> This module is part of the [cisco.iosxr collection](https://galaxy.ansible.com/cisco/iosxr) (version 3.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.iosxr`.
>
> To use it in a playbook, specify: `cisco.iosxr.iosxr_snmp_server`.

New in cisco.iosxr 2.6.0

- [Synopsis](iosxr_snmp_server_module.md#synopsis)
- [Parameters](iosxr_snmp_server_module.md#parameters)
- [Notes](iosxr_snmp_server_module.md#notes)
- [Examples](iosxr_snmp_server_module.md#examples)
- [Return Values](iosxr_snmp_server_module.md#return-values)

## [Synopsis](iosxr_snmp_server_module.md#id1)

- This module configures and manages the attributes of snmp-server on Cisco IOSXR platforms.

## [Parameters](iosxr_snmp_server_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | SNMP server configuration. |
| **chassis_id**  string | SNMP chassis identifier. |
| **communities**  list / elements=dictionary | Enable SNMP; set community string and access privileges. |
| **acl_v4**  string | Ipv4 access list. |
| **acl_v6**  string | IPv6 access list name. |
| **name**  string | Community name. |
| **ro**  boolean | Only reads are permitted.  Choices:   - `false` - `true` |
| **rw**  boolean | Read-write access.  Choices:   - `false` - `true` |
| **sdrowner**  boolean | SDR Owner permissions for MIB Objects.  Choices:   - `false` - `true` |
| **systemowner**  boolean | System Owner permissions for MIB objects.  Choices:   - `false` - `true` |
| **v4_acl**  string | V4 Access-list name. |
| **community_maps**  list / elements=dictionary | Community Mapping as per RFC-2576. |
| **context**  string | Context Name for the community mapping. |
| **name**  string | Community name |
| **security_name**  string | Security Name for the community mapping. |
| **target_list**  string | list of targets valid with this community. |
| **contact**  string | Person to contact about the syste,. |
| **context**  list / elements=string | Create/Delete a context apart from default |
| **correlator**  dictionary | Configure properties of the event correlator |
| **buffer_size**  integer | Configure size of the correlator buffer. |
| **rule_sets**  list / elements=dictionary | Configure a specified correlation ruleset. |
| **name**  string | Name of the ruleset |
| **rules**  list / elements=dictionary | Configure a specified correlation rule. |
| **rule_name**  string | name of rule. |
| **timeout**  integer | Specify timeout. |
| **drop**  dictionary | Silently drop SNMP packets |
| **report_IPv4**  string | Config to drop snmpv3 error reports matching Ipv4 ACL. |
| **report_IPv6**  string | Config to drop snmpv3 error reports matching Ipv4 ACL. |
| **unknown_user**  boolean | Silently drop unknown v3 user packets  Choices:   - `false` - `true` |
| **engineid**  dictionary | SNMPv3 engine ID configuration. |
| **local**  string | Local SNMP agent |
| **groups**  list / elements=dictionary | SNMP USM group |
| **acl_v4**  aliases: Ipv4_acl  string | Ipv4 Type of Access-list |
| **acl_v6**  aliases: Ipv6_acl  string | Ipv6 Type of Access-list |
| **context**  string | Specify a context to associate with the group |
| **group**  string | SNMP group for the user |
| **notify**  string | View to restrict notifications |
| **read**  string | View to restrict read access |
| **v4_acl**  string | V4 Access-list name |
| **version**  string | snmp security group version  Choices:   - `"v1"` - `"v3"` - `"v2c"` |
| **write**  string | View to restrict write access |
| **hosts**  list / elements=dictionary | Notification destinations |
| **community**  string | community string. |
| **host**  string | Hostname or IP address of SNMP notification host. |
| **informs**  boolean | Use SNMP inform messages.  Choices:   - `false` - `true` |
| **traps**  boolean | Use SNMP trap messages  Choices:   - `false` - `true` |
| **udp_port**  integer | UDP destination port for notification messages. |
| **version**  string | Notification message SNMP version.  Choices:   - `"1"` - `"2c"` - `"3"` |
| **ifindex**  boolean | Enable ifindex persistence  Choices:   - `false` - `true` |
| **ifmib**  dictionary | IF-MIB configuration commands. |
| **ifalias_long**  boolean | Modify parameters for ifAlias object.  Choices:   - `false` - `true` |
| **internal_cache_max_duration**  integer | IFMIB internal lookahead cache. |
| **ipsubscriber**  boolean | Enable ipsubscriber interfaces in IFMIB.  Choices:   - `false` - `true` |
| **stats**  boolean | Modify IF-MIB statistics parameters.  Choices:   - `false` - `true` |
| **inform**  dictionary | Configure SNMP Informs options |
| **pending**  integer | Set number of unacked informs to hold |
| **retries**  integer | Set retry count for informs |
| **timeout**  integer | Set timeout for informs |
| **interfaces**  list / elements=dictionary | Enter the SNMP interface configuration commands. |
| **index_persistent**  boolean | Configure ifIndex attributes Persistency across system reloads.  Choices:   - `false` - `true` |
| **name**  string | Name of interface. |
| **notification_linkupdown_disable**  boolean | Disable linkUp and linkDown notification.  Choices:   - `false` - `true` |
| **ipv4**  dictionary | Mark the dscp/precedence bit for ipv4 packets. |
| **dscp**  string | Set IP DSCP (DiffServ CodePoint).Please refer vendor document for valid entries. |
| **precedence**  string | Set precedence Please refer vendor document for valid entries. |
| **ipv6**  dictionary | Mark the dscp/precedence bit for ipv4 packets. |
| **dscp**  string | Set IP DSCP (DiffServ CodePoint).Please refer vendor document for valid entries. |
| **precedence**  string | Set precedence Please refer vendor document for valid entries. |
| **location**  string | The sysLocation string. |
| **logging_threshold_oid_processing**  integer | Configure threshold to start logging slow OID requests processing. |
| **logging_threshold_pdu_processing**  integer | Configure threshold to start logging slow PDU requests processing. |
| **mib_bulkstat_max_procmem_size**  integer | per process memory limit in kilo bytes |
| **mib_bulkstat_transfer_ids**  list / elements=dictionary | mib bulkstat transfer ids. |
| **buffer_size**  integer | Bulkstat data file maximum size. |
| **enable**  boolean | Start Data Collection for this Configuration  Choices:   - `false` - `true` |
| **format_schemaASCI**  boolean | format  Choices:   - `false` - `true` |
| **name**  string | mib transfer-id name. |
| **retain**  integer | Retention period in Min. |
| **retry**  integer | Number of Retries. |
| **schema**  string | Schema that contains objects to be collected. |
| **transfer_interval**  integer | transfer-interval |
| **mib_object_lists**  list / elements=string | mib object lists |
| **mib_schema**  list / elements=dictionary | mib schema |
| **name**  string | mib schema name. |
| **object_list**  string | Name of an object List. |
| **poll_interval**  integer | Periodicity for polling of objects in this schema in Min. |
| **mroutemib_send_all_vrf**  boolean | Configurations related to IPMROUTE-MIB(cisco-support).  Choices:   - `false` - `true` |
| **notification_log_mib**  dictionary | notification log mib. |
| **default**  boolean | To create a default log  Choices:   - `false` - `true` |
| **disable**  boolean | disable, to disable the logging in default log.  Choices:   - `false` - `true` |
| **GlobalSize**  integer | GlobalSize, max number of notifications that can be logged in all logs. |
| **size**  integer | size, The max number of notifications that this log (default) can hold. |
| **oid_poll_stats**  boolean | Enable OID poll stats oper CLI  Choices:   - `false` - `true` |
| **overload_control**  dictionary | Set overload-control params for handling incoming messages in critical processing mode. |
| **overload_drop_time**  integer | Overload drop time (in seconds) for incoming queue (default 1 sec). |
| **overload_throttle_rate**  integer | Overload throttle rate for incoming queue (default 500 msec) |
| **packetsize**  integer | Largest SNMP packet size. |
| **queue_length**  integer | Queue length (default 100). |
| **targets**  list / elements=dictionary | targets |
| **host**  string | Specify host name. |
| **name**  string | Name of the target list. |
| **vrf**  string | Specify VRF name. |
| **throttle_time**  integer | Set throttle time for handling incoming messages. |
| **timeouts**  dictionary | SNMP timeouts |
| **duplicate**  integer | Duplicate request feature timeout |
| **inQdrop**  integer | incoming queue drop feature. |
| **pdu_stats**  integer | SNMP pdu statistics end to end. |
| **subagent**  integer | Sub-Agent Request timeout. |
| **threshold**  integer | threshold incoming queue drop feature. |
| **trap**  dictionary | MIB trap configurations. |
| **authentication_vrf_disable**  boolean | Disable authentication traps for packets on a vrf.  Choices:   - `false` - `true` |
| **link_ietf**  boolean | Link up/down trap configuratio.  Choices:   - `false` - `true` |
| **throttle_time**  integer | Set throttle time for handling more traps. |
| **trap_source**  string | Assign an interface for the source address of all traps |
| **trap_timeout**  integer | Set timeout for TRAP message retransmissions |
| **traps**  dictionary | Enable traps to all configured recipients. |
| **addrpool**  dictionary | Enable SNMP Address Pool traps. |
| **high**  boolean | Enable SNMP Address Pool High Threshold trap.  Choices:   - `false` - `true` |
| **low**  boolean | Enable SNMP Address Pool Low Threshold trap.  Choices:   - `false` - `true` |
| **bfd**  boolean | Enable BFD traps.  Choices:   - `false` - `true` |
| **bgp**  dictionary | Enable Bgp traps. |
| **cbgp2**  boolean | Enable CISCO-BGP4-MIB v2 traps.  Choices:   - `false` - `true` |
| **updown**  boolean | Enable CISCO-BGP4-MIB v2 up/down traps.  Choices:   - `false` - `true` |
| **bridgemib**  boolean | Enable SNMP Trap for Bridge MIB.  Choices:   - `false` - `true` |
| **bulkstat_collection**  boolean | Enable Data-Collection-MIB Collection notifications.  Choices:   - `false` - `true` |
| **bulkstat_transfer**  boolean | Enable Data-Collection-MIB Trnasfer notifications.  Choices:   - `false` - `true` |
| **cisco_entity_ext**  boolean | Enable SNMP entity traps  Choices:   - `false` - `true` |
| **config**  boolean | Enable SNMP config traps.  Choices:   - `false` - `true` |
| **copy_complete**  boolean | Enable CISCO-CONFIG-COPY-MIB ccCopyCompletion traps.  Choices:   - `false` - `true` |
| **diameter**  dictionary | Enable SNMP diameter traps. |
| **peerdown**  boolean | Enable peer connection down notification.  Choices:   - `false` - `true` |
| **peerup**  boolean | Enable peer connection up notification.  Choices:   - `false` - `true` |
| **permanentfail**  boolean | Enable permanent failure notification.  Choices:   - `false` - `true` |
| **protocolerror**  boolean | Enable protocol error notifications  Choices:   - `false` - `true` |
| **transientfail**  boolean | Enable transient failure notification.  Choices:   - `false` - `true` |
| **entity**  boolean | Enable SNMP entity traps.  Choices:   - `false` - `true` |
| **entity_redundancy**  dictionary | Enable SNMP CISCO-ENTITY-REDUNDANCY-MIB traps. |
| **all**  boolean | Enable all CISCO-ENTITY-REDUNDANCY-MIB traps  Choices:   - `false` - `true` |
| **status**  boolean | Enable status change traps  Choices:   - `false` - `true` |
| **switchover**  boolean | Enable switchover traps.  Choices:   - `false` - `true` |
| **entity_state**  dictionary | Enable SNMP entity-state traps. |
| **operstatus**  boolean | Enable entity oper status enable notification.  Choices:   - `false` - `true` |
| **switchover**  boolean | Enable entity state switchover notifications  Choices:   - `false` - `true` |
| **flash**  dictionary | Enable flash-mib traps. |
| **insertion**  boolean | Enable ciscoFlashDeviceInsertedNotif.  Choices:   - `false` - `true` |
| **removal**  boolean | Enable ciscoFlashDeviceRemovedNotif.  Choices:   - `false` - `true` |
| **fru_ctrl**  boolean | Enable SNMP entity FRU control traps.  Choices:   - `false` - `true` |
| **hsrp**  boolean | Enable SNMP hsrp traps.  Choices:   - `false` - `true` |
| **ipsec**  dictionary | Enable SNMP IPSec traps. |
| **start**  boolean | Enable SNMP IPsec Tunnel Start trap.  Choices:   - `false` - `true` |
| **stop**  boolean | Enable SNMP IPsec Tunnel Stop trap.  Choices:   - `false` - `true` |
| **ipsla**  boolean | Enable SNMP hipsla traps.  Choices:   - `false` - `true` |
| **isakmp**  dictionary | Enable SNMP isakmp traps. |
| **start**  boolean | Enable SNMP isakmp Tunnel Start trap.  Choices:   - `false` - `true` |
| **stop**  boolean | Enable SNMP isakmp Tunnel Stop trap.  Choices:   - `false` - `true` |
| **isis**  dictionary | Enable isis traps. If set to enabled , all the traps are set. |
| **adjacency_change**  boolean | adjacency-change  Choices:   - `false` - `true` |
| **all**  boolean | anable all is-is traps.  Choices:   - `false` - `true` |
| **area_mismatch**  boolean | area-mismatch  Choices:   - `false` - `true` |
| **attempt_to_exceed_max_sequence**  boolean | attempt-to-exceed-max-sequence  Choices:   - `false` - `true` |
| **authentication_failure**  boolean | authentication-failure.  Choices:   - `false` - `true` |
| **authentication_type_failure**  boolean | authentication-type-failure.  Choices:   - `false` - `true` |
| **corrupted_lsp_detected**  boolean | isisCorruptedLSPDetected  Choices:   - `false` - `true` |
| **database_overload**  boolean | database-overload  Choices:   - `false` - `true` |
| **id_len_mismatch**  boolean | isisIDLenMismatch  Choices:   - `false` - `true` |
| **lsp_error_detected**  boolean | lsp-error-detected.  Choices:   - `false` - `true` |
| **lsp_too_large_to_propagate**  boolean | lsp-too-large-to-propagate  Choices:   - `false` - `true` |
| **manual_address_drops**  boolean | manual_address_drops  Choices:   - `false` - `true` |
| **max_area_addresses_mismatch**  boolean | max_area_addresses_mismatch  Choices:   - `false` - `true` |
| **orig_lsp_buff_size_mismatch**  boolean | orig-lsp-buff-size-mismatch  Choices:   - `false` - `true` |
| **own_lsp_purge**  boolean | own-lsp-purge  Choices:   - `false` - `true` |
| **protocols_supported_mismatch**  boolean | protocols-supported-mismatch  Choices:   - `false` - `true` |
| **rejected_adjacency**  boolean | rejected-adjacency  Choices:   - `false` - `true` |
| **sequence_number_skip**  boolean | sequence-number-skip.  Choices:   - `false` - `true` |
| **version_skew**  boolean | version-skew  Choices:   - `false` - `true` |
| **l2tun**  dictionary | Enable L2TUN traps. |
| **pseudowire_status**  boolean | Enable L2TUN pseudowire status traps.  Choices:   - `false` - `true` |
| **sessions**  boolean | Enable L2TUN sessions traps.  Choices:   - `false` - `true` |
| **tunnel_down**  boolean | Enable L2TUN tunnel DOWN traps.  Choices:   - `false` - `true` |
| **tunnel_up**  boolean | Enable L2TUN tunnel UP traps.  Choices:   - `false` - `true` |
| **l2vpn**  dictionary | Enable L2VPN traps. |
| **all**  boolean | Enable L2VPN ALL traps.  Choices:   - `false` - `true` |
| **cisco**  boolean | Enable L2VPN CISCO traps.  Choices:   - `false` - `true` |
| **vc_down**  boolean | Enable L2VPN VC DOWN traps.  Choices:   - `false` - `true` |
| **vc_up**  boolean | Enable L2VPN VC UP traps.  Choices:   - `false` - `true` |
| **msdp_peer_state_change**  boolean | Enable SNMP MSDP traps  Choices:   - `false` - `true` |
| **ntp**  boolean | Enable SNMP Cisco Ntp traps.  Choices:   - `false` - `true` |
| **ospf**  dictionary | Enable Ospf traps. If set to enabled , all the traps are set. |
| **errors**  dictionary | error |
| **authentication_failure**  boolean | authentication-failure.  Choices:   - `false` - `true` |
| **bad_packet**  boolean | bad-packet  Choices:   - `false` - `true` |
| **config_error**  boolean | config-error  Choices:   - `false` - `true` |
| **virt_authentication_failure**  boolean | virt-authentication-failure  Choices:   - `false` - `true` |
| **virt_bad_packet**  boolean | virt-bad-packet  Choices:   - `false` - `true` |
| **virt_config_error**  boolean | virt_config_error  Choices:   - `false` - `true` |
| **lsa**  dictionary | lsa |
| **lsa_maxage**  boolean | lsa-maxage  Choices:   - `false` - `true` |
| **lsa_originate**  boolean | lsa-originate  Choices:   - `false` - `true` |
| **retransmit**  dictionary | retransmit |
| **packets**  boolean | packets  Choices:   - `false` - `true` |
| **virt_packets**  boolean | virt-packets  Choices:   - `false` - `true` |
| **state_change**  dictionary | state-change. |
| **if_state_change**  boolean | if-state-change  Choices:   - `false` - `true` |
| **neighbor_state_change**  boolean | neighbor-state-change  Choices:   - `false` - `true` |
| **virtif_state_change**  boolean | virtif-state-change  Choices:   - `false` - `true` |
| **virtneighbor_state_change**  boolean | virtneighbor-state-change  Choices:   - `false` - `true` |
| **ospfv3**  dictionary | Enable Ospfv3 traps. If set to enabled , all the traps are set. |
| **errors**  dictionary | error |
| **bad_packet**  boolean | bad-packet  Choices:   - `false` - `true` |
| **config_error**  boolean | config-error  Choices:   - `false` - `true` |
| **virt_bad_packet**  boolean | virt-bad-packet  Choices:   - `false` - `true` |
| **virt_config_error**  boolean | virt_config_error  Choices:   - `false` - `true` |
| **state_change**  dictionary | state-change. |
| **if_state_change**  boolean | if-state-change  Choices:   - `false` - `true` |
| **neighbor_state_change**  boolean | neighbor-state-change  Choices:   - `false` - `true` |
| **nssa_state_change**  boolean | nssa-state-change  Choices:   - `false` - `true` |
| **restart_helper_status_change**  boolean | restart-helper-status-change  Choices:   - `false` - `true` |
| **restart_status_change**  boolean | restart-status-change  Choices:   - `false` - `true` |
| **restart_virtual_helper_status_change**  boolean | restart-virtual-helper-status-change  Choices:   - `false` - `true` |
| **virtif_state_change**  boolean | virtif-state-change  Choices:   - `false` - `true` |
| **virtneighbor_state_change**  boolean | virtneighbor-state-change  Choices:   - `false` - `true` |
| **pim**  dictionary | Enable Pim traps. If set to enabled , all the traps are set. |
| **interface_state_change**  boolean | interface-state-change .  Choices:   - `false` - `true` |
| **invalid_message_received**  boolean | invalid-message-received  Choices:   - `false` - `true` |
| **neighbor_change**  boolean | neighbor-change.  Choices:   - `false` - `true` |
| **rp_mapping_change**  boolean | rp-mapping-change.  Choices:   - `false` - `true` |
| **power**  boolean | Enable SNMP entity power traps.  Choices:   - `false` - `true` |
| **rf**  boolean | Enable SNMP RF-MIB traps.  Choices:   - `false` - `true` |
| **rsvp**  dictionary | Enable rsvp traps. If set to enabled , all the traps are set. |
| **all**  boolean | enable all traps.  Choices:   - `false` - `true` |
| **lost_flow**  boolean | lost-flow  Choices:   - `false` - `true` |
| **new_flow**  boolean | new-flow  Choices:   - `false` - `true` |
| **selective_vrf_download_role_change**  boolean | Enable selective VRF download traps.  Choices:   - `false` - `true` |
| **sensor**  boolean | Enable SNMP entity sensor traps  Choices:   - `false` - `true` |
| **snmp**  dictionary | Enable snmp traps. If set to enabled , all the traps are set. |
| **authentication**  boolean | authentication  Choices:   - `false` - `true` |
| **coldstart**  boolean | coldstart.  Choices:   - `false` - `true` |
| **linkdown**  boolean | link-down  Choices:   - `false` - `true` |
| **linkup**  boolean | link-up  Choices:   - `false` - `true` |
| **warmstart**  boolean | warmstart.  Choices:   - `false` - `true` |
| **subscriber**  dictionary | Subscriber notification commands. |
| **session_agg_access_interface**  boolean | Subscriber notification at access interface level  Choices:   - `false` - `true` |
| **session_agg_node**  boolean | Subscriber notification at node level  Choices:   - `false` - `true` |
| **syslog**  boolean | syslog  Choices:   - `false` - `true` |
| **system**  boolean | Enable SNMP SYSTEMMIB-MIB traps.  Choices:   - `false` - `true` |
| **vpls**  dictionary | Enable VPLS traps |
| **all**  boolean | Enable all VPLS traps.  Choices:   - `false` - `true` |
| **full_clear**  boolean | Enable VPLS Full Clear traps.  Choices:   - `false` - `true` |
| **full_raise**  boolean | Enable VPLS Full Raise traps.  Choices:   - `false` - `true` |
| **status**  boolean | Enable VPLS Status traps  Choices:   - `false` - `true` |
| **vrrp_events**  boolean | vrrp  Choices:   - `false` - `true` |
| **users**  list / elements=dictionary | SNMP user configuration. |
| **acl_v4**  aliases: Ipv4_acl  string | Ipv4 Type of Access-list |
| **acl_v6**  aliases: Ipv6_acl  string | Ipv6 Type of Access-list |
| **group**  string | SNMP group for the user. |
| **SDROwner**  boolean | SDR Owner permissions for MIB Objects.  Choices:   - `false` - `true` |
| **SystemOwner**  boolean | System Owner permissions for MIB objects.  Choices:   - `false` - `true` |
| **user**  string | SNMP user name |
| **v4_acl**  string | V4 Access-list name |
| **version**  string | snmp security version  Choices:   - `"v1"` - `"v2c"` - `"v3"` |
| **vrfs**  list / elements=dictionary | Specify the VRF in which the source address is used |
| **context**  list / elements=string | Configure the source interface for SNMP notifications |
| **hosts**  list / elements=dictionary | Notification destinations |
| **community**  string | community string. |
| **host**  string | Hostname or IP address of SNMP notification host. |
| **informs**  boolean | Use SNMP inform messages.  Choices:   - `false` - `true` |
| **traps**  boolean | Use SNMP trap messages  Choices:   - `false` - `true` |
| **udp_port**  integer | UDP destination port for notification messages. |
| **version**  string | Notification message SNMP version.  Choices:   - `"1"` - `"2c"` - `"3"` |
| **vrf**  string | vrf name. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOSXR device by executing the command **show running-config snmp-server**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  The states *replaced* and *overridden* have identical behaviour for this module.  Please refer to examples for more details.  Choices:   - `"deleted"` - `"merged"` ← (default) - `"overridden"` - `"replaced"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](iosxr_snmp_server_module.md#id3)

> **Note:**
>
> - Tested against Cisco Iosxr 7.0.2
> - This module works with connection `network_cli`.

## [Examples](iosxr_snmp_server_module.md#id4)

```yaml+jinja
# Using state: merged
# Before state:
# -------------
# RP/0/RP0/CPU0:test2#show running-config snmp-server
# --------------------- EMPTY -----------------
# Merged play:
# ------------
- name: Merge the provided configuration with the existing running configuration
  cisco.iosxr.iosxr_snmp_server:
        config:
          vrfs:
            - hosts:
                - community: test1
                  host: 1.1.1.1
                  traps: true
              vrf: vrf1
          users:
            - Ipv4_acl: test1
              Ipv6_acl: test2
              group: test2
              user: u1
              version: v1
          timeouts:
            duplicate: 0
            inQdrop: 0
          trap:
            throttle_time: 12
          targets:
            - host: 1.1.1.2
              name: test

          ifmib:
            internal_cache_max_duration: 4
          inform:
            retries: 7
          chassis_id: test2
          packetsize: 490
          queue_length: 2
          throttle_time: 60
          trap_source: GigabitEthernet0/0/0/2
          trap_timeout: 3
          context:
            - c1
            - c2
          contact: t1
          correlator:
            buffer_size: 1024
          communities:
            - name: test2
              ro: true
              sdrowner: true
              acl_v4: test
              acl_v6: test1
          community_maps:
            - name: cm1
              context: c1
              target_list: t1
              security_name: s1
          drop:
            report_IPv4: test1
            unknown_user: true
          ipv6:
            precedence: routine
          ipv4:
            dscp: af11
          location: test1
          logging_threshold_oid_processing: 1
          logging_threshold_pdu_processing: 1
          mib_bulkstat_max_procmem_size: 101
          mroutemib_send_all_vrf: true
          overload_control:
            overload_drop_time: 4
            overload_throttle_rate: 6
          notification_log_mib:
            GlobalSize: 5
            size: 5
          traps:
            hsrp: true
            ipsla: true
            ipsec:
              start: true
              stop: true
            bridgemib: true
            bulkstat_collection: true
            cisco_entity_ext: true
            config: true
            copy_complete: true
            addrpool:
              high: true
              low: true
            bfd: true
            bgp:
              cbgp2: true
            l2tun:
              sessions: true
              tunnel_down: true
              tunnel_up: true
            l2vpn:
              all: true
              vc_down: true
              vc_up: true
            msdp_peer_state_change: true
#
# Commands Fired:
# ------------
# "commands": [
#         "snmp-server chassis-id test2",
#         "snmp-server correlator buffer-size 1024",
#         "snmp-server contact t1",
#         "snmp-server ipv4 dscp af11",
#         "snmp-server ipv6 precedence routine",
#         "snmp-server location test1",
#         "snmp-server logging threshold oid-processing 1",
#         "snmp-server logging threshold pdu-processing 1",
#         "snmp-server mib bulkstat max-procmem-size 101",
#         "snmp-server mroutemib send-all-vrf",
#         "snmp-server overload-control 4 6",
#         "snmp-server packetsize 490",
#         "snmp-server queue-length 2",
#         "snmp-server throttle-time 60",
#         "snmp-server trap-source GigabitEthernet0/0/0/2",
#         "snmp-server trap-timeout 3",
#         "snmp-server drop report acl IPv4 test1",
#         "snmp-server drop unknown-user",
#         "snmp-server ifmib internal cache max-duration 4",
#         "snmp-server inform retries 7",
#         "snmp-server notification-log-mib size 5",
#         "snmp-server notification-log-mib GlobalSize 5",
#         "snmp-server trap throttle-time 12",
#         "snmp-server timeouts inQdrop 0",
#         "snmp-server timeouts duplicate 0",
#         "snmp-server traps addrpool low",
#         "snmp-server traps addrpool high",
#         "snmp-server traps bfd",
#         "snmp-server traps bgp cbgp2",
#         "snmp-server traps bulkstat collection",
#         "snmp-server traps bridgemib",
#         "snmp-server traps copy-complete",
#         "snmp-server traps cisco-entity-ext",
#         "snmp-server traps config",
#         "snmp-server traps hsrp",
#         "snmp-server traps ipsla",
#         "snmp-server traps ipsec tunnel start",
#         "snmp-server traps ipsec tunnel stop",
#         "snmp-server traps l2tun sessions",
#         "snmp-server traps l2tun tunnel-up",
#         "snmp-server traps l2tun tunnel-down",
#         "snmp-server traps l2vpn all",
#         "snmp-server traps l2vpn vc-up",
#         "snmp-server traps l2vpn vc-down",
#         "snmp-server traps msdp peer-state-change",
#         "snmp-server community test2 RO SDROwner IPv4 test IPv6 test1",
#         "snmp-server community-map cm1 context c1 security-name s1 target-list t1",
#         "snmp-server context c1",
#         "snmp-server context c2",
#         "snmp-server user u1 test2 v1 IPv4 test1 IPv6 test2",
#         "snmp-server target list test2 vrf vrf2",
#         "snmp-server target list test host 1.1.1.2",
#         "snmp-server vrf vrf1",
#         "host 1.1.1.1 traps test1"
#
#     ],
# After state:
# ------------
# RP/0/RP0/CPU0:test2#show running-config snmp-server
# Mon Nov 29 12:49:29.521 UTC
# snmp-server vrf vrf1
#  host 1.1.1.1 traps test1
# !
# snmp-server drop report acl IPv4 test1
# snmp-server drop unknown-user
# snmp-server ipv4 dscp af11
# snmp-server ipv6 precedence routine
# snmp-server user u1 test2 v1 IPv4 test1 IPv6 test2
# snmp-server community test2 RO SDROwner IPv4 test IPv6 test1
# snmp-server queue-length 2
# snmp-server trap-timeout 3
# snmp-server trap throttle-time 12
# snmp-server traps bfd
# snmp-server traps bgp cbgp2
# snmp-server traps copy-complete
# snmp-server traps hsrp
# snmp-server traps ipsla
# snmp-server traps msdp peer-state-change
# snmp-server traps ipsec tunnel stop
# snmp-server traps ipsec tunnel start
# snmp-server traps config
# snmp-server traps l2tun sessions
# snmp-server traps l2tun tunnel-up
# snmp-server traps l2tun tunnel-down
# snmp-server traps bulkstat collection
# snmp-server traps l2vpn all
# snmp-server traps l2vpn vc-up
# snmp-server traps l2vpn vc-down
# snmp-server traps bridgemib
# snmp-server traps addrpool low
# snmp-server traps addrpool high
# snmp-server traps cisco-entity-ext
# snmp-server chassis-id test2
# snmp-server contact t1
# snmp-server location test1
# snmp-server target list test host 1.1.1.2
# snmp-server target list test2 vrf vrf2
# snmp-server context c1
# snmp-server context c2
# snmp-server logging threshold oid-processing 1
# snmp-server logging threshold pdu-processing 1
# snmp-server mib bulkstat max-procmem-size 101
# snmp-server timeouts duplicate 0
# snmp-server timeouts inQdrop 0
# snmp-server packetsize 490
# snmp-server correlator buffer-size 1024
# snmp-server trap-source GigabitEthernet0/0/0/2
# snmp-server throttle-time 60
# snmp-server community-map cm1 context c1 security-name s1 target-list t1
# snmp-server inform retries 7
# snmp-server overload-control 4 6
# snmp-server ifmib internal cache max-duration 4
# snmp-server mroutemib send-all-vrf
# snmp-server notification-log-mib size 5
# snmp-server notification-log-mib GlobalSize 5
#
#
# Using state: deleted
# Before state:
# -------------
# RP/0/RP0/CPU0:test2#show running-config snmp-server
# Mon Nov 29 12:49:29.521 UTC
# snmp-server vrf vrf1
#  host 1.1.1.1 traps test1
# !
# snmp-server drop report acl IPv4 test1
# snmp-server drop unknown-user
# snmp-server ipv4 dscp af11
# snmp-server ipv6 precedence routine
# snmp-server user u1 test2 v1 IPv4 test1 IPv6 test2
# snmp-server community test2 RO SDROwner IPv4 test IPv6 test1
# snmp-server queue-length 2
# snmp-server trap-timeout 3
# snmp-server trap throttle-time 12
# snmp-server traps bfd
# snmp-server traps bgp cbgp2
# snmp-server traps copy-complete
# snmp-server traps hsrp
# snmp-server traps ipsla
# snmp-server traps msdp peer-state-change
# snmp-server traps ipsec tunnel stop
# snmp-server traps ipsec tunnel start
# snmp-server traps config
# snmp-server traps l2tun sessions
# snmp-server traps l2tun tunnel-up
# snmp-server traps l2tun tunnel-down
# snmp-server traps bulkstat collection
# snmp-server traps l2vpn all
# snmp-server traps l2vpn vc-up
# snmp-server traps l2vpn vc-down
# snmp-server traps bridgemib
# snmp-server traps addrpool low
# snmp-server traps addrpool high
# snmp-server traps cisco-entity-ext
# snmp-server chassis-id test2
# snmp-server contact t1
# snmp-server location test1
# snmp-server target list test host 1.1.1.2
# snmp-server target list test2 vrf vrf2
# snmp-server context c1
# snmp-server context c2
# snmp-server logging threshold oid-processing 1
# snmp-server logging threshold pdu-processing 1
# snmp-server mib bulkstat max-procmem-size 101
# snmp-server timeouts duplicate 0
# snmp-server timeouts inQdrop 0
# snmp-server packetsize 490
# snmp-server correlator buffer-size 1024
# snmp-server trap-source GigabitEthernet0/0/0/2
# snmp-server throttle-time 60
# snmp-server community-map cm1 context c1 security-name s1 target-list t1
# snmp-server inform retries 7
# snmp-server overload-control 4 6
# snmp-server ifmib internal cache max-duration 4
# snmp-server mroutemib send-all-vrf
# snmp-server notification-log-mib size 5
# snmp-server notification-log-mib GlobalSize 5
# Deleted play:
# -------------
- name: Remove all existing configuration
  cisco.iosxr.iosxr_snmp_server:
    state: deleted
# Commands Fired:
# ---------------
# "commands": [
#        "no snmp-server chassis-id test2",
#         "no snmp-server correlator buffer-size 1024",
#         "no snmp-server contact t1",
#         "no snmp-server ipv4 dscp af11",
#         "no snmp-server ipv6 precedence routine",
#         "no snmp-server location test1",
#         "no snmp-server logging threshold oid-processing 1",
#         "no snmp-server logging threshold pdu-processing 1",
#         "no snmp-server mib bulkstat max-procmem-size 101",
#         "no snmp-server mroutemib send-all-vrf",
#         "no snmp-server overload-control 4 6",
#         "no snmp-server packetsize 490",
#         "no snmp-server queue-length 2",
#         "no snmp-server throttle-time 60",
#         "no snmp-server trap-source GigabitEthernet0/0/0/2",
#         "no snmp-server trap-timeout 3",
#         "no snmp-server drop report acl IPv4 test1",
#         "no snmp-server drop unknown-user",
#         "no snmp-server ifmib internal cache max-duration 4",
#         "no snmp-server inform retries 7",
#         "no snmp-server notification-log-mib size 5",
#         "no snmp-server notification-log-mib GlobalSize 5",
#         "no snmp-server trap throttle-time 12",
#         "no snmp-server timeouts inQdrop 0",
#         "no snmp-server timeouts duplicate 0",
#         "no snmp-server traps addrpool low",
#         "no snmp-server traps addrpool high",
#         "no snmp-server traps bfd",
#         "no snmp-server traps bgp cbgp2",
#         "no snmp-server traps bulkstat collection",
#         "no snmp-server traps bridgemib",
#         "no snmp-server traps copy-complete",
#         "no snmp-server traps cisco-entity-ext",
#         "no snmp-server traps config",
#         "no snmp-server traps hsrp",
#         "no snmp-server traps ipsla",
#         "no snmp-server traps ipsec tunnel start",
#         "no snmp-server traps ipsec tunnel stop",
#         "no snmp-server traps l2tun sessions",
#         "no snmp-server traps l2tun tunnel-up",
#         "no snmp-server traps l2tun tunnel-down",
#         "no snmp-server traps l2vpn all",
#         "no snmp-server traps l2vpn vc-up",
#         "no snmp-server traps l2vpn vc-down",
#         "no snmp-server traps msdp peer-state-change",
#         "no snmp-server community test2 RO SDROwner IPv4 test IPv6 test1",
#         "no snmp-server community-map cm1 context c1 security-name s1 target-list t1",
#         "no snmp-server context c1",
#         "no snmp-server context c2",
#         "no snmp-server user u1 test2 v1 IPv4 test1 IPv6 test2",
#         "no snmp-server target list test host 1.1.1.2",
#         "no snmp-server target list test2 vrf vrf2",
#         "no snmp-server vrf vrf1"
#     ],
# After state:
# ------------
# RP/0/0/CPU0:10#show running-config ntp
# --------------------- EMPTY -----------------
# Using state: overridden
# Before state:
# -------------
# RP/0/0/CPU0:10#show running-config snmp-server
# snmp-server vrf vrf1
#  host 1.1.1.1 traps test1
# !
# snmp-server drop report acl IPv4 test1
# snmp-server drop unknown-user
# snmp-server ipv4 dscp af11
# snmp-server ipv6 precedence routine
# snmp-server user u1 test2 v1 IPv4 test1 IPv6 test2
# snmp-server community test2 RO SDROwner IPv4 test IPv6 test1
# snmp-server queue-length 2
# snmp-server trap-timeout 3
# snmp-server trap throttle-time 12
# snmp-server traps bfd
# snmp-server traps bgp cbgp2
# snmp-server traps copy-complete
# snmp-server traps hsrp
# snmp-server traps ipsla
# snmp-server traps msdp peer-state-change
# snmp-server traps ipsec tunnel stop
# snmp-server traps ipsec tunnel start
# snmp-server traps config
# snmp-server traps l2tun sessions
# snmp-server traps l2tun tunnel-up
# snmp-server traps l2tun tunnel-down
# snmp-server traps bulkstat collection
# snmp-server traps l2vpn all
# snmp-server traps l2vpn vc-up
# snmp-server traps l2vpn vc-down
# snmp-server traps bridgemib
# snmp-server traps addrpool low
# snmp-server traps addrpool high
# snmp-server traps cisco-entity-ext
# snmp-server chassis-id test2
# snmp-server contact t1
# snmp-server location test1
# snmp-server target list test host 1.1.1.2
# snmp-server target list test2 vrf vrf2
# snmp-server context c1
# snmp-server context c2
# snmp-server logging threshold oid-processing 1
# snmp-server logging threshold pdu-processing 1
# snmp-server mib bulkstat max-procmem-size 101
# snmp-server timeouts duplicate 0
# snmp-server timeouts inQdrop 0
# snmp-server packetsize 490
# snmp-server correlator buffer-size 1024
# snmp-server trap-source GigabitEthernet0/0/0/2
# snmp-server throttle-time 60
# snmp-server community-map cm1 context c1 security-name s1 target-list t1
# snmp-server inform retries 7
# snmp-server overload-control 4 6
# snmp-server ifmib internal cache max-duration 4
# snmp-server mroutemib send-all-vrf
# snmp-server notification-log-mib size 5
# snmp-server notification-log-mib GlobalSize 5
# Overridden play:
# ----------------
- name: Override Snmp-server configuration with provided configuration
  cisco.iosxr.iosxr_snmp_server:
        config:
          timeouts:
            duplicate: 0
            inQdrop: 0
          trap:
            throttle_time: 13
          targets:
            - host: 1.1.1.2
              name: test

          ifmib:
            internal_cache_max_duration: 5
          inform:
            retries: 7
          chassis_id: test
          packetsize: 491
          queue_length: 2
          throttle_time: 60
          trap_source: GigabitEthernet0/0/0/2
          trap_timeout: 3
          context:
            - c1
            - c2
          contact: t1
          correlator:
            buffer_size: 1025
          communities:
            - name: test1
              ro: true
              sdrowner: true
              acl_v4: test
              acl_v6: test1
          community_maps:
            - name: cm2
              context: c1
              target_list: t1
              security_name: s1
          drop:
            report_IPv4: test2
            unknown_user: true
          ipv6:
            precedence: routine
          ipv4:
            dscp: af11
          location: test1
          logging_threshold_oid_processing: 2
          logging_threshold_pdu_processing: 2
          mib_bulkstat_max_procmem_size: 101
          mroutemib_send_all_vrf: true
          overload_control:
            overload_drop_time: 4
            overload_throttle_rate: 6
          notification_log_mib:
            GlobalSize: 5
            size: 5
          traps:
            hsrp: true
            ipsla: true
            ipsec:
              start: true
              stop: true
            bridgemib: true
            bulkstat_collection: true
            cisco_entity_ext: true
            config: true
            copy_complete: true
            l2vpn:
              all: true
              vc_down: true
              vc_up: true
            msdp_peer_state_change: true
        state: overridden
# Commands Fired:
# ---------------
# "commands": [
#        "no snmp-server traps addrpool low",
#         "no snmp-server traps addrpool high",
#         "no snmp-server traps bfd",
#         "no snmp-server traps bgp cbgp2",
#         "no snmp-server traps l2tun sessions",
#         "no snmp-server traps l2tun tunnel-up",
#         "no snmp-server traps l2tun tunnel-down",
#         "no snmp-server community test2 RO SDROwner IPv4 test IPv6 test1",
#         "no snmp-server community-map cm1 context c1 security-name s1 target-list t1",
#         "no snmp-server user u1 test2 v1 IPv4 test1 IPv6 test2",
#         "no snmp-server vrf vrf1",
#         "snmp-server chassis-id test",
#         "snmp-server correlator buffer-size 1025",
#         "snmp-server logging threshold oid-processing 2",
#         "snmp-server logging threshold pdu-processing 2",
#         "snmp-server packetsize 491",
#         "snmp-server drop report acl IPv4 test2",
#         "snmp-server ifmib internal cache max-duration 5",
#         "snmp-server trap throttle-time 13",
#         "snmp-server community test1 RO SDROwner IPv4 test IPv6 test1",
#         "snmp-server community-map cm2 context c1 security-name s1 target-list t1"
#     ],
# After state:
# ------------
# RP/0/RP0/CPU0:test2#show running-config snmp-server
# Mon Nov 29 12:57:34.182 UTC
# snmp-server drop report acl IPv4 test2
# snmp-server drop unknown-user
# snmp-server ipv4 dscp af11
# snmp-server ipv6 precedence routine
# snmp-server community test1 RO SDROwner IPv4 test IPv6 test1
# snmp-server queue-length 2
# snmp-server trap-timeout 3
# snmp-server trap throttle-time 13
# snmp-server traps copy-complete
# snmp-server traps hsrp
# snmp-server traps ipsla
# snmp-server traps msdp peer-state-change
# snmp-server traps ipsec tunnel stop
# snmp-server traps ipsec tunnel start
# snmp-server traps config
# snmp-server traps bulkstat collection
# snmp-server traps l2vpn all
# snmp-server traps l2vpn vc-up
# snmp-server traps l2vpn vc-down
# snmp-server traps bridgemib
# snmp-server traps cisco-entity-ext
# snmp-server chassis-id test
# snmp-server contact t1
# snmp-server location test1
# snmp-server target list test host 1.1.1.2
# snmp-server target list test2 vrf vrf2
# snmp-server context c1
# snmp-server context c2
# snmp-server logging threshold oid-processing 2
# snmp-server logging threshold pdu-processing 2
# snmp-server mib bulkstat max-procmem-size 101
# snmp-server timeouts duplicate 0
# snmp-server timeouts inQdrop 0
# snmp-server packetsize 491
# snmp-server correlator buffer-size 1025
# snmp-server trap-source GigabitEthernet0/0/0/2
# snmp-server throttle-time 60
# snmp-server community-map cm2 context c1 security-name s1 target-list t1
# snmp-server inform retries 7
# snmp-server overload-control 4 6
# snmp-server ifmib internal cache max-duration 5
# snmp-server mroutemib send-all-vrf
# snmp-server notification-log-mib size 5
# snmp-server notification-log-mib GlobalSize 5
#
# Using state: replaced
# Before state:
# -------------
# RP/0/0/CPU0:10#show running-config snmp-server
# snmp-server vrf vrf1
#  host 1.1.1.1 traps test1
# !
# snmp-server drop report acl IPv4 test1
# snmp-server drop unknown-user
# snmp-server ipv4 dscp af11
# snmp-server ipv6 precedence routine
# snmp-server user u1 test2 v1 IPv4 test1 IPv6 test2
# snmp-server community test2 RO SDROwner IPv4 test IPv6 test1
# snmp-server queue-length 2
# snmp-server trap-timeout 3
# snmp-server trap throttle-time 12
# snmp-server traps bfd
# snmp-server traps bgp cbgp2
# snmp-server traps copy-complete
# snmp-server traps hsrp
# snmp-server traps ipsla
# snmp-server traps msdp peer-state-change
# snmp-server traps ipsec tunnel stop
# snmp-server traps ipsec tunnel start
# snmp-server traps config
# snmp-server traps l2tun sessions
# snmp-server traps l2tun tunnel-up
# snmp-server traps l2tun tunnel-down
# snmp-server traps bulkstat collection
# snmp-server traps l2vpn all
# snmp-server traps l2vpn vc-up
# snmp-server traps l2vpn vc-down
# snmp-server traps bridgemib
# snmp-server traps addrpool low
# snmp-server traps addrpool high
# snmp-server traps cisco-entity-ext
# snmp-server chassis-id test2
# snmp-server contact t1
# snmp-server location test1
# snmp-server target list test host 1.1.1.2
# snmp-server target list test2 vrf vrf2
# snmp-server context c1
# snmp-server context c2
# snmp-server logging threshold oid-processing 1
# snmp-server logging threshold pdu-processing 1
# snmp-server mib bulkstat max-procmem-size 101
# snmp-server timeouts duplicate 0
# snmp-server timeouts inQdrop 0
# snmp-server packetsize 490
# snmp-server correlator buffer-size 1024
# snmp-server trap-source GigabitEthernet0/0/0/2
# snmp-server throttle-time 60
# snmp-server community-map cm1 context c1 security-name s1 target-list t1
# snmp-server inform retries 7
# snmp-server overload-control 4 6
# snmp-server ifmib internal cache max-duration 4
# snmp-server mroutemib send-all-vrf
# snmp-server notification-log-mib size 5
# snmp-server notification-log-mib GlobalSize 5
#
#
# Replaced play:
# ----------------
- name: Replace Snmp-server configuration with provided configuration
  cisco.iosxr.iosxr_snmp_server:
        state: replaced
        config:
          timeouts:
            duplicate: 0
            inQdrop: 0
          trap:
            throttle_time: 13
          targets:
            - host: 1.1.1.2
              name: test

          ifmib:
            internal_cache_max_duration: 5
          inform:
            retries: 7
          chassis_id: test
          packetsize: 491
          queue_length: 2
          throttle_time: 60
          trap_source: GigabitEthernet0/0/0/2
          trap_timeout: 3
          context:
            - c1
            - c2
          contact: t1
          correlator:
            buffer_size: 1025
          communities:
            - name: test1
              ro: true
              sdrowner: true
              acl_v4: test
              acl_v6: test1
          community_maps:
            - name: cm2
              context: c1
              target_list: t1
              security_name: s1
          drop:
            report_IPv4: test2
            unknown_user: true
          ipv6:
            precedence: routine
          ipv4:
            dscp: af11
          location: test1
          logging_threshold_oid_processing: 2
          logging_threshold_pdu_processing: 2
          mib_bulkstat_max_procmem_size: 101
          mroutemib_send_all_vrf: true
          overload_control:
            overload_drop_time: 4
            overload_throttle_rate: 6
          notification_log_mib:
            GlobalSize: 5
            size: 5
          traps:
            hsrp: true
            ipsla: true
            ipsec:
              start: true
              stop: true
            bridgemib: true
            bulkstat_collection: true
            cisco_entity_ext: true
            config: true
            copy_complete: true
            l2vpn:
              all: true
              vc_down: true
              vc_up: true
            msdp_peer_state_change: true
#
# Commands Fired:
# ---------------
# "commands": [
#         "no snmp-server traps addrpool low",
#         "no snmp-server traps addrpool high",
#         "no snmp-server traps bfd",
#         "no snmp-server traps bgp cbgp2",
#         "no snmp-server traps l2tun sessions",
#         "no snmp-server traps l2tun tunnel-up",
#         "no snmp-server traps l2tun tunnel-down",
#         "no snmp-server community test2 RO SDROwner IPv4 test IPv6 test1",
#         "no snmp-server community-map cm1 context c1 security-name s1 target-list t1",
#         "no snmp-server user u1 test2 v1 IPv4 test1 IPv6 test2",
#         "no snmp-server vrf vrf1",
#         "snmp-server chassis-id test",
#         "snmp-server correlator buffer-size 1025",
#         "snmp-server logging threshold oid-processing 2",
#         "snmp-server logging threshold pdu-processing 2",
#         "snmp-server packetsize 491",
#         "snmp-server drop report acl IPv4 test2",
#         "snmp-server ifmib internal cache max-duration 5",
#         "snmp-server trap throttle-time 13",
#         "snmp-server community test1 RO SDROwner IPv4 test IPv6 test1",
#         "snmp-server community-map cm2 context c1 security-name s1 target-list t1"
#     ],
# After state:
# ------------
# RP/0/RP0/CPU0:ios#show running-config snmp-server
# Mon Sep 13 10:38:22.690 UTC
# RP/0/0/CPU0:10#show running-config snmp-server
# snmp-server vrf vrf1
#  host 1.1.1.1 traps test1
# !
# snmp-server drop report acl IPv4 test1
# snmp-server drop unknown-user
# snmp-server ipv4 dscp af11
# snmp-server ipv6 precedence routine
# snmp-server user u1 test2 v1 IPv4 test1 IPv6 test2
# snmp-server community test2 RO SDROwner IPv4 test IPv6 test1
# snmp-server queue-length 2
# snmp-server trap-timeout 3
# snmp-server trap throttle-time 12
# snmp-server traps bfd
# snmp-server traps bgp cbgp2
# snmp-server traps copy-complete
# snmp-server traps hsrp
# snmp-server traps ipsla
# snmp-server traps msdp peer-state-change
# snmp-server traps ipsec tunnel stop
# snmp-server traps ipsec tunnel start
# snmp-server traps config
# snmp-server traps l2tun sessions
# snmp-server traps l2tun tunnel-up
# snmp-server traps l2tun tunnel-down
# snmp-server traps bulkstat collection
# snmp-server traps l2vpn all
# snmp-server traps l2vpn vc-up
# snmp-server traps l2vpn vc-down
# snmp-server traps bridgemib
# snmp-server traps addrpool low
# snmp-server traps addrpool high
# snmp-server traps cisco-entity-ext
# snmp-server chassis-id test2
# snmp-server contact t1
# snmp-server location test1
# snmp-server target list test host 1.1.1.2
# snmp-server target list test2 vrf vrf2
# snmp-server context c1
# snmp-server context c2
# snmp-server logging threshold oid-processing 1
# snmp-server logging threshold pdu-processing 1
# snmp-server mib bulkstat max-procmem-size 101
# snmp-server timeouts duplicate 0
# snmp-server timeouts inQdrop 0
# snmp-server packetsize 490
# snmp-server correlator buffer-size 1024
# snmp-server trap-source GigabitEthernet0/0/0/2
# snmp-server throttle-time 60
# snmp-server community-map cm1 context c1 security-name s1 target-list t1
# snmp-server inform retries 7
# snmp-server overload-control 4 6
# snmp-server ifmib internal cache max-duration 4
# snmp-server mroutemib send-all-vrf
# snmp-server notification-log-mib size 5
# snmp-server notification-log-mib GlobalSize 5
#
#
# Using state: gathered
# Before state:
# -------------
# RP/0/RP0/CPU0:test2#show running-config snmp-server
# Mon Nov 29 12:49:29.521 UTC
# snmp-server vrf vrf1
#  host 1.1.1.1 traps test1
# !
# snmp-server drop report acl IPv4 test1
# snmp-server drop unknown-user
# snmp-server ipv4 dscp af11
# snmp-server ipv6 precedence routine
# snmp-server user u1 test2 v1 IPv4 test1 IPv6 test2
# snmp-server community test2 RO SDROwner IPv4 test IPv6 test1
# snmp-server queue-length 2
# snmp-server trap-timeout 3
# snmp-server trap throttle-time 12
# snmp-server traps bfd
# snmp-server traps bgp cbgp2
# snmp-server traps copy-complete
# snmp-server traps hsrp
# snmp-server traps ipsla
# snmp-server traps msdp peer-state-change
# snmp-server traps ipsec tunnel stop
# snmp-server traps ipsec tunnel start
# snmp-server traps config
# snmp-server traps l2tun sessions
# snmp-server traps l2tun tunnel-up
# snmp-server traps l2tun tunnel-down
# snmp-server traps bulkstat collection
# snmp-server traps l2vpn all
# snmp-server traps l2vpn vc-up
# snmp-server traps l2vpn vc-down
# snmp-server traps bridgemib
# snmp-server traps addrpool low
# snmp-server traps addrpool high
# snmp-server traps cisco-entity-ext
# snmp-server chassis-id test2
# snmp-server contact t1
# snmp-server location test1
# snmp-server target list test host 1.1.1.2
# snmp-server target list test2 vrf vrf2
# snmp-server context c1
# snmp-server context c2
# snmp-server logging threshold oid-processing 1
# snmp-server logging threshold pdu-processing 1
# snmp-server mib bulkstat max-procmem-size 101
# snmp-server timeouts duplicate 0
# snmp-server timeouts inQdrop 0
# snmp-server packetsize 490
# snmp-server correlator buffer-size 1024
# snmp-server trap-source GigabitEthernet0/0/0/2
# snmp-server throttle-time 60
# snmp-server community-map cm1 context c1 security-name s1 target-list t1
# snmp-server inform retries 7
# snmp-server overload-control 4 6
# snmp-server ifmib internal cache max-duration 4
# snmp-server mroutemib send-all-vrf
# snmp-server notification-log-mib size 5
# snmp-server notification-log-mib GlobalSize 5
# Gathered play:
# --------------
- name: Gather listed snmp server
  cisco.iosxr.iosxr_snmp_server:
    state: gathered
# Module Execution Result:
# ------------------------
# "gathered": {
#         "chassis_id": "test2",
#         "communities": [
#             {
#                 "acl_v4": "test",
#                 "acl_v6": "test1",
#                 "name": "test2",
#                 "ro": true,
#                 "sdrowner": true
#             }
#         ],
#         "community_maps": [
#             {
#                 "context": "c1",
#                 "name": "cm1",
#                 "security_name": "s1",
#                 "target_list": "t1"
#             }
#         ],
#         "contact": "t1",
#         "context": [
#             "c1",
#             "c2"
#         ],
#         "correlator": {
#             "buffer_size": 1024
#         },
#         "drop": {
#             "report_IPv4": "test1",
#             "unknown_user": true
#         },
#         "ifmib": {
#             "internal_cache_max_duration": 4
#         },
#         "inform": {
#             "retries": 7
#         },
#         "ipv4": {
#             "dscp": "af11"
#         },
#         "ipv6": {
#             "precedence": "routine"
#         },
#         "location": "test1",
#         "logging_threshold_oid_processing": 1,
#         "logging_threshold_pdu_processing": 1,
#         "mib_bulkstat_max_procmem_size": 101,
#         "mroutemib_send_all_vrf": true,
#         "notification_log_mib": {
#             "GlobalSize": 5,
#             "size": 5
#         },
#         "overload_control": {
#             "overload_drop_time": 4,
#             "overload_throttle_rate": 6
#         },
#         "packetsize": 490,
#         "queue_length": 2,
#         "targets": [
#             {
#                 "host": "1.1.1.2",
#                 "name": "test"
#             },
#             {
#                 "name": "test2",
#                 "vrf": "vrf2"
#             }
#         ],
#         "throttle_time": 60,
#         "timeouts": {
#             "duplicate": 0,
#             "inQdrop": 0
#         },
#         "trap": {
#             "throttle_time": 12
#         },
#         "trap_source": "GigabitEthernet0/0/0/2",
#         "trap_timeout": 3,
#         "traps": {
#             "addrpool": {
#                 "high": true,
#                 "low": true
#             },
#             "bfd": true,
#             "bgp": {
#                 "cbgp2": true
#             },
#             "bridgemib": true,
#             "bulkstat_collection": true,
#             "cisco_entity_ext": true,
#             "config": true,
#             "copy_complete": true,
#             "hsrp": true,
#             "ipsec": {
#                 "start": true,
#                 "stop": true
#             },
#             "ipsla": true,
#             "l2tun": {
#                 "sessions": true,
#                 "tunnel_down": true,
#                 "tunnel_up": true
#             },
#             "l2vpn": {
#                 "all": true,
#                 "vc_down": true,
#                 "vc_up": true
#             },
#             "msdp_peer_state_change": true
#         },
#         "users": [
#             {
#                 "Ipv4_acl": "test1",
#                 "Ipv6_acl": "test2",
#                 "group": "test2",
#                 "user": "u1",
#                 "version": "v1"
#             }
#         ],
#         "vrfs": [
#             {
#                 "hosts": [
#                     {
#                         "community": "test1",
#                         "host": "1.1.1.1",
#                         "traps": true
#                     }
#                 ],
#                 "vrf": "vrf1"
#             }
#         ]
#     }
#
#
# Using state: rendered
# Rendered play:
# --------------
- name: Render platform specific configuration lines with state rendered (without connecting to the device)
  cisco.iosxr.iosxr_snmp_server:
    state: rendered
    config:
      vrfs:
        - hosts:
            - community: test1
              host: 1.1.1.1
              traps: true
          vrf: vrf1
      users:
        - Ipv4_acl: test1
          Ipv6_acl: test2
          group: test2
          user: u1
          version: v1
      timeouts:
        duplicate: 0
        inQdrop: 0
      trap:
        throttle_time: 12
      targets:
        - host: 1.1.1.2
          name: test

      ifmib:
        internal_cache_max_duration: 4
      inform:
        retries: 7
      chassis_id: test2
      packetsize: 490
      queue_length: 2
      throttle_time: 60
      trap_source: GigabitEthernet0/0/0/2
      trap_timeout: 3
      context:
        - c1
        - c2
      contact: t1
      correlator:
        buffer_size: 1024
      communities:
        - name: test2
          ro: true
          sdrowner: true
          acl_v4: test
          acl_v6: test1
      community_maps:
        - name: cm1
          context: c1
          target_list: t1
          security_name: s1
      drop:
        report_IPv4: test1
        unknown_user: true
      ipv6:
        precedence: routine
      ipv4:
        dscp: af11
      location: test1
      logging_threshold_oid_processing: 1
      logging_threshold_pdu_processing: 1
      mib_bulkstat_max_procmem_size: 101
      mroutemib_send_all_vrf: true
      overload_control:
        overload_drop_time: 4
        overload_throttle_rate: 6
      notification_log_mib:
        GlobalSize: 5
        size: 5
      traps:
        hsrp: true
        ipsla: true
        ipsec:
          start: true
          stop: true
        bridgemib: true
        bulkstat_collection: true
        cisco_entity_ext: true
        config: true
        copy_complete: true
        addrpool:
          high: true
          low: true
        bfd: true
        bgp:
          cbgp2: true
        l2tun:
          sessions: true
          tunnel_down: true
          tunnel_up: true
        l2vpn:
          all: true
          vc_down: true
          vc_up: true
        msdp_peer_state_change: true
  register: result
# Module Execution Result:
# ------------------------
# "rendered": [
#         "snmp-server chassis-id test2",
#         "snmp-server correlator buffer-size 1024",
#         "snmp-server contact t1",
#         "snmp-server ipv4 dscp af11",
#         "snmp-server ipv6 precedence routine",
#         "snmp-server location test1",
#         "snmp-server logging threshold oid-processing 1",
#         "snmp-server logging threshold pdu-processing 1",
#         "snmp-server mib bulkstat max-procmem-size 101",
#         "snmp-server mroutemib send-all-vrf",
#         "snmp-server overload-control 4 6",
#         "snmp-server packetsize 490",
#         "snmp-server queue-length 2",
#         "snmp-server throttle-time 60",
#         "snmp-server trap-source GigabitEthernet0/0/0/2",
#         "snmp-server trap-timeout 3",
#         "snmp-server drop report acl IPv4 test1",
#         "snmp-server drop unknown-user",
#         "snmp-server ifmib internal cache max-duration 4",
#         "snmp-server inform retries 7",
#         "snmp-server notification-log-mib size 5",
#         "snmp-server notification-log-mib GlobalSize 5",
#         "snmp-server trap throttle-time 12",
#         "snmp-server timeouts inQdrop 0",
#         "snmp-server timeouts duplicate 0",
#         "snmp-server traps addrpool low",
#         "snmp-server traps addrpool high",
#         "snmp-server traps bfd",
#         "snmp-server traps bgp cbgp2",
#         "snmp-server traps bulkstat collection",
#         "snmp-server traps bridgemib",
#         "snmp-server traps copy-complete",
#         "snmp-server traps cisco-entity-ext",
#         "snmp-server traps config",
#         "snmp-server traps hsrp",
#         "snmp-server traps ipsla",
#         "snmp-server traps ipsec tunnel start",
#         "snmp-server traps ipsec tunnel stop",
#         "snmp-server traps l2tun sessions",
#         "snmp-server traps l2tun tunnel-up",
#         "snmp-server traps l2tun tunnel-down",
#         "snmp-server traps l2vpn all",
#         "snmp-server traps l2vpn vc-up",
#         "snmp-server traps l2vpn vc-down",
#         "snmp-server traps msdp peer-state-change",
#         "snmp-server community test2 RO SDROwner IPv4 test IPv6 test1",
#         "snmp-server community-map cm1 context c1 security-name s1 target-list t1",
#         "snmp-server context c1",
#         "snmp-server context c2",
#         "snmp-server user u1 test2 v1 IPv4 test1 IPv6 test2",
#         "snmp-server target list test2 vrf vrf2",
#         "snmp-server target list test host 1.1.1.2",
#         "snmp-server vrf vrf1",
#         "host 1.1.1.1 traps test1"
#     ],
# Using state: parsed
# File: parsed.cfg
# ----------------
# snmp-server vrf vrf1
#  host 1.1.1.1 traps test1
# !
# snmp-server drop report acl IPv4 test1
# snmp-server drop unknown-user
# snmp-server ipv4 dscp af11
# snmp-server ipv6 precedence routine
# snmp-server user u1 test2 v1 IPv4 test1 IPv6 test2
# snmp-server community test2 RO SDROwner IPv4 test IPv6 test1
# snmp-server queue-length 2
# snmp-server trap-timeout 3
# snmp-server trap throttle-time 12
# snmp-server traps bfd
# snmp-server traps bgp cbgp2
# snmp-server traps copy-complete
# snmp-server traps hsrp
# snmp-server traps ipsla
# snmp-server traps msdp peer-state-change
# snmp-server traps ipsec tunnel stop
# snmp-server traps ipsec tunnel start
# snmp-server traps config
# snmp-server traps l2tun sessions
# snmp-server traps l2tun tunnel-up
# snmp-server traps l2tun tunnel-down
# snmp-server traps bulkstat collection
# snmp-server traps l2vpn all
# snmp-server traps l2vpn vc-up
# snmp-server traps l2vpn vc-down
# snmp-server traps bridgemib
# snmp-server traps addrpool low
# snmp-server traps addrpool high
# snmp-server traps cisco-entity-ext
# snmp-server chassis-id test2
# snmp-server contact t1
# snmp-server location test1
# snmp-server target list test host 1.1.1.2
# snmp-server target list test2 vrf vrf2
# snmp-server context c1
# snmp-server context c2
# snmp-server logging threshold oid-processing 1
# snmp-server logging threshold pdu-processing 1
# snmp-server mib bulkstat max-procmem-size 101
# snmp-server timeouts duplicate 0
# snmp-server timeouts inQdrop 0
# snmp-server packetsize 490
# snmp-server correlator buffer-size 1024
# snmp-server trap-source GigabitEthernet0/0/0/2
# snmp-server throttle-time 60
# snmp-server community-map cm1 context c1 security-name s1 target-list t1
# snmp-server inform retries 7
# snmp-server overload-control 4 6
# snmp-server ifmib internal cache max-duration 4
# snmp-server mroutemib send-all-vrf
# snmp-server notification-log-mib size 5
# snmp-server notification-log-mib GlobalSize 5
# ------------
- name: Parse the provided configuration with the existing running configuration
  cisco.iosxr.iosxr_snmp_server:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed
# Module Execution Result:
# ------------------------
# "parsed":{
#         "chassis_id": "test2",
#         "communities": [
#             {
#                 "acl_v4": "test",
#                 "acl_v6": "test1",
#                 "name": "test2",
#                 "ro": true,
#                 "sdrowner": true
#             }
#         ],
#         "community_maps": [
#             {
#                 "context": "c1",
#                 "name": "cm1",
#                 "security_name": "s1",
#                 "target_list": "t1"
#             }
#         ],
#         "contact": "t1",
#         "context": [
#             "c1",
#             "c2"
#         ],
#         "correlator": {
#             "buffer_size": 1024
#         },
#         "drop": {
#             "report_IPv4": "test1",
#             "unknown_user": true
#         },
#         "ifmib": {
#             "internal_cache_max_duration": 4
#         },
#         "inform": {
#             "retries": 7
#         },
#         "ipv4": {
#             "dscp": "af11"
#         },
#         "ipv6": {
#             "precedence": "routine"
#         },
#         "location": "test1",
#         "logging_threshold_oid_processing": 1,
#         "logging_threshold_pdu_processing": 1,
#         "mib_bulkstat_max_procmem_size": 101,
#         "mroutemib_send_all_vrf": true,
#         "notification_log_mib": {
#             "GlobalSize": 5,
#             "size": 5
#         },
#         "overload_control": {
#             "overload_drop_time": 4,
#             "overload_throttle_rate": 6
#         },
#         "packetsize": 490,
#         "queue_length": 2,
#         "targets": [
#             {
#                 "host": "1.1.1.2",
#                 "name": "test"
#             },
#             {
#                 "name": "test2",
#                 "vrf": "vrf2"
#             }
#         ],
#         "throttle_time": 60,
#         "timeouts": {
#             "duplicate": 0,
#             "inQdrop": 0
#         },
#         "trap": {
#             "throttle_time": 12
#         },
#         "trap_source": "GigabitEthernet0/0/0/2",
#         "trap_timeout": 3,
#         "traps": {
#             "addrpool": {
#                 "high": true,
#                 "low": true
#             },
#             "bfd": true,
#             "bgp": {
#                 "cbgp2": true
#             },
#             "bridgemib": true,
#             "bulkstat_collection": true,
#             "cisco_entity_ext": true,
#             "config": true,
#             "copy_complete": true,
#             "hsrp": true,
#             "ipsec": {
#                 "start": true,
#                 "stop": true
#             },
#             "ipsla": true,
#             "l2tun": {
#                 "sessions": true,
#                 "tunnel_down": true,
#                 "tunnel_up": true
#             },
#             "l2vpn": {
#                 "all": true,
#                 "vc_down": true,
#                 "vc_up": true
#             },
#             "msdp_peer_state_change": true
#         },
#         "users": [
#             {
#                 "Ipv4_acl": "test1",
#                 "Ipv6_acl": "test2",
#                 "group": "test2",
#                 "user": "u1",
#                 "version": "v1"
#             }
#         ],
#         "vrfs": [
#             {
#                 "hosts": [
#                     {
#                         "community": "test1",
#                         "host": "1.1.1.1",
#                         "traps": true
#                     }
#                 ],
#                 "vrf": "vrf1"
#             }
#         ]
#     }
```

## [Return Values](iosxr_snmp_server_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  Returned: when changed  Sample: `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  Returned: when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  Sample: `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  Sample: `["sample command 1", "sample command 2", "sample command 3"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  Returned: when *state* is `gathered`  Sample: `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  Returned: when *state* is `parsed`  Sample: `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  Returned: when *state* is `rendered`  Sample: `["sample command 1", "sample command 2", "sample command 3"]` |

### Authors

- Ashwini Mhatre (@amhatre)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
