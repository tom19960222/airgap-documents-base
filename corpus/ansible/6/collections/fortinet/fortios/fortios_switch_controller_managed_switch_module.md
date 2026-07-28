---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_switch_controller_managed_switch module – Configure FortiSwitch devices that are managed by this FortiGate in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_switch_controller_managed_switch_module.html
fetched_at: 2026-07-27T17:43:34+00:00
---
# fortinet.fortios.fortios_switch_controller_managed_switch module – Configure FortiSwitch devices that are managed by this FortiGate in Fortinet’s FortiOS and FortiGate.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/fortinet/fortios) (version 2.2.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_switch_controller_managed_switch_module.md#ansible-collections-fortinet-fortios-fortios-switch-controller-managed-switch-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_switch_controller_managed_switch`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_switch_controller_managed_switch_module.md#synopsis)
- [Requirements](fortios_switch_controller_managed_switch_module.md#requirements)
- [Parameters](fortios_switch_controller_managed_switch_module.md#parameters)
- [Notes](fortios_switch_controller_managed_switch_module.md#notes)
- [Examples](fortios_switch_controller_managed_switch_module.md#examples)
- [Return Values](fortios_switch_controller_managed_switch_module.md#return-values)

## [Synopsis](fortios_switch_controller_managed_switch_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify switch_controller feature and managed_switch category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_switch_controller_managed_switch_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_switch_controller_managed_switch_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **switch_controller_managed_switch**  dictionary | Configure FortiSwitch devices that are managed by this FortiGate. |
| **access_profile**  string | FortiSwitch access profile. Source switch-controller.security-policy.local-access.name. |
| **custom_command**  list / elements=dictionary | Configuration method to edit FortiSwitch commands to be pushed to this FortiSwitch device upon rebooting the FortiGate switch controller or the FortiSwitch. |
| **command_entry**  string | List of FortiSwitch commands. |
| **command_name**  string | Names of commands to be pushed to this FortiSwitch device, as configured under config switch-controller custom-command. Source switch-controller.custom-command.command-name. |
| **delayed_restart_trigger**  integer | Delayed restart triggered for this FortiSwitch. |
| **description**  string | Description. |
| **dhcp_server_access_list**  string | DHCP snooping server access list.  Choices:   - `"global"` - `"enable"` - `"disable"` |
| **directly_connected**  integer | Directly connected FortiSwitch. |
| **dynamic_capability**  string | List of features this FortiSwitch supports (not configurable) that is sent to the FortiGate device for subsequent configuration initiated by the FortiGate device. |
| **dynamically_discovered**  integer | Dynamically discovered FortiSwitch. |
| **firmware_provision**  string | Enable/disable provisioning of firmware to FortiSwitches on join connection.  Choices:   - `"enable"` - `"disable"` |
| **firmware_provision_latest**  string | Enable/disable one-time automatic provisioning of the latest firmware version.  Choices:   - `"disable"` - `"once"` |
| **firmware_provision_version**  string | Firmware version to provision to this FortiSwitch on bootup (major.minor.build, i.e. 6.2.1234). |
| **flow_identity**  string | Flow-tracking netflow ipfix switch identity in hex format(00000000-FFFFFFFF ). |
| **fsw_wan1_admin**  string | FortiSwitch WAN1 admin status; enable to authorize the FortiSwitch as a managed switch.  Choices:   - `"discovered"` - `"disable"` - `"enable"` |
| **fsw_wan1_peer**  string | FortiSwitch WAN1 peer port. Source system.interface.name. |
| **fsw_wan2_admin**  string | FortiSwitch WAN2 admin status; enable to authorize the FortiSwitch as a managed switch.  Choices:   - `"discovered"` - `"disable"` - `"enable"` |
| **fsw_wan2_peer**  string | FortiSwitch WAN2 peer port. |
| **igmp_snooping**  dictionary | Configure FortiSwitch IGMP snooping global settings. |
| **aging_time**  integer | Maximum time to retain a multicast snooping entry for which no packets have been seen (15 - 3600 sec). |
| **flood_unknown_multicast**  string | Enable/disable unknown multicast flooding.  Choices:   - `"enable"` - `"disable"` |
| **local_override**  string | Enable/disable overriding the global IGMP snooping configuration.  Choices:   - `"enable"` - `"disable"` |
| **vlans**  list / elements=dictionary | Configure IGMP snooping VLAN. |
| **proxy**  string | IGMP snooping proxy for the VLAN interface.  Choices:   - `"disable"` - `"enable"` - `"global"` |
| **querier**  string | Enable/disable IGMP snooping querier for the VLAN interface.  Choices:   - `"disable"` - `"enable"` |
| **querier_addr**  string | IGMP snooping querier address. |
| **version**  integer | IGMP snooping querying version. |
| **vlan_name**  string | List of FortiSwitch VLANs. Source system.interface.name. |
| **ip_source_guard**  list / elements=dictionary | IP source guard. |
| **binding_entry**  list / elements=dictionary | IP and MAC address configuration. |
| **entry_name**  string | Configure binding pair. |
| **ip**  string | Source IP for this rule. |
| **mac**  string | MAC address for this rule. |
| **description**  string | Description. |
| **port**  string | Ingress interface to which source guard is bound. |
| **l3_discovered**  integer | Layer 3 management discovered. |
| **max_allowed_trunk_members**  integer | FortiSwitch maximum allowed trunk members. |
| **mclag_igmp_snooping_aware**  string | Enable/disable MCLAG IGMP-snooping awareness.  Choices:   - `"enable"` - `"disable"` |
| **mirror**  list / elements=dictionary | Configuration method to edit FortiSwitch packet mirror. |
| **dst**  string | Destination port. |
| **name**  string | Mirror name. |
| **src_egress**  list / elements=dictionary | Source egress interfaces. |
| **name**  string | Interface name. |
| **src_ingress**  list / elements=dictionary | Source ingress interfaces. |
| **name**  string | Interface name. |
| **status**  string | Active/inactive mirror configuration.  Choices:   - `"active"` - `"inactive"` |
| **switching_packet**  string | Enable/disable switching functionality when mirroring.  Choices:   - `"enable"` - `"disable"` |
| **name**  string | Managed-switch name. |
| **override_snmp_community**  string | Enable/disable overriding the global SNMP communities.  Choices:   - `"enable"` - `"disable"` |
| **override_snmp_sysinfo**  string | Enable/disable overriding the global SNMP system information.  Choices:   - `"disable"` - `"enable"` |
| **override_snmp_trap_threshold**  string | Enable/disable overriding the global SNMP trap threshold values.  Choices:   - `"enable"` - `"disable"` |
| **override_snmp_user**  string | Enable/disable overriding the global SNMP users.  Choices:   - `"enable"` - `"disable"` |
| **owner_vdom**  string | VDOM which owner of port belongs to. |
| **poe_detection_type**  integer | PoE detection type for FortiSwitch. |
| **poe_lldp_detection**  string | Enable/disable PoE LLDP detection.  Choices:   - `"enable"` - `"disable"` |
| **poe_pre_standard_detection**  string | Enable/disable PoE pre-standard detection.  Choices:   - `"enable"` - `"disable"` |
| **ports**  list / elements=dictionary | Managed-switch port list. |
| **access_mode**  string | Access mode of the port.  Choices:   - `"dynamic"` - `"nac"` - `"static"` - `"normal"` |
| **aggregator_mode**  string | LACP member select mode.  Choices:   - `"bandwidth"` - `"count"` |
| **allowed_vlans**  list / elements=dictionary | Configure switch port tagged VLANs. |
| **vlan_name**  string | VLAN name. Source system.interface.name. |
| **allowed_vlans_all**  string | Enable/disable all defined vlans on this port.  Choices:   - `"enable"` - `"disable"` |
| **arp_inspection_trust**  string | Trusted or untrusted dynamic ARP inspection.  Choices:   - `"untrusted"` - `"trusted"` |
| **bundle**  string | Enable/disable Link Aggregation Group (LAG) bundling for non-FortiLink interfaces.  Choices:   - `"enable"` - `"disable"` |
| **description**  string | Description for port. |
| **dhcp_snoop_option82_trust**  string | Enable/disable allowance of DHCP with option-82 on untrusted interface.  Choices:   - `"enable"` - `"disable"` |
| **dhcp_snooping**  string | Trusted or untrusted DHCP-snooping interface.  Choices:   - `"untrusted"` - `"trusted"` |
| **discard_mode**  string | Configure discard mode for port.  Choices:   - `"none"` - `"all-untagged"` - `"all-tagged"` |
| **edge_port**  string | Enable/disable this interface as an edge port, bridging connections between workstations and/or computers.  Choices:   - `"enable"` - `"disable"` |
| **export_tags**  list / elements=dictionary | Configure export tag(s) for FortiSwitch port when exported to a virtual port pool. |
| **tag_name**  string | FortiSwitch port tag name when exported to a virtual port pool. Source switch-controller.switch-interface-tag.name. |
| **export_to**  string | Export managed-switch port to a tenant VDOM. Source system.vdom.name. |
| **export_to_pool**  string | Switch controller export port to pool-list. Source switch-controller.virtual-port-pool.name. |
| **export_to_pool_flag**  integer | Switch controller export port to pool-list. |
| **fec_capable**  integer | FEC capable. |
| **fec_state**  string | State of forward error correction.  Choices:   - `"disabled"` - `"cl74"` - `"cl91"` |
| **fgt_peer_device_name**  string | FGT peer device name. |
| **fgt_peer_port_name**  string | FGT peer port name. |
| **fiber_port**  integer | Fiber-port. |
| **flags**  integer | Port properties flags. |
| **flap_duration**  integer | Period over which flap events are calculated (seconds). |
| **flap_rate**  integer | Number of stage change events needed within flap-duration. |
| **flap_timeout**  integer | Flap guard disabling protection (min). |
| **flapguard**  string | Enable/disable flap guard.  Choices:   - `"enable"` - `"disable"` |
| **flow_control**  string | Flow control direction.  Choices:   - `"disable"` - `"tx"` - `"rx"` - `"both"` |
| **fortilink_port**  integer | FortiLink uplink port. |
| **igmp_snooping**  string | Set IGMP snooping mode for the physical port interface.  Choices:   - `"enable"` - `"disable"` |
| **igmp_snooping_flood_reports**  string | Enable/disable flooding of IGMP reports to this interface when igmp-snooping enabled.  Choices:   - `"enable"` - `"disable"` |
| **igmps_flood_reports**  string | Enable/disable flooding of IGMP reports to this interface when igmp-snooping enabled.  Choices:   - `"enable"` - `"disable"` |
| **igmps_flood_traffic**  string | Enable/disable flooding of IGMP snooping traffic to this interface.  Choices:   - `"enable"` - `"disable"` |
| **interface_tags**  list / elements=dictionary | Tag(s) associated with the interface for various features including virtual port pool, dynamic port policy. |
| **tag_name**  string | FortiSwitch port tag name when exported to a virtual port pool or matched to dynamic port policy. Source switch-controller.switch-interface-tag.name. |
| **ip_source_guard**  string | Enable/disable IP source guard.  Choices:   - `"disable"` - `"enable"` |
| **isl_local_trunk_name**  string | ISL local trunk name. |
| **isl_peer_device_name**  string | ISL peer device name. |
| **isl_peer_port_name**  string | ISL peer port name. |
| **lacp_speed**  string | End Link Aggregation Control Protocol (LACP) messages every 30 seconds (slow) or every second (fast).  Choices:   - `"slow"` - `"fast"` |
| **learning_limit**  integer | Limit the number of dynamic MAC addresses on this Port (1 - 128, 0 = no limit, default). |
| **lldp_profile**  string | LLDP port TLV profile. Source switch-controller.lldp-profile.name. |
| **lldp_status**  string | LLDP transmit and receive status.  Choices:   - `"disable"` - `"rx-only"` - `"tx-only"` - `"tx-rx"` |
| **loop_guard**  string | Enable/disable loop-guard on this interface, an STP optimization used to prevent network loops.  Choices:   - `"enabled"` - `"disabled"` |
| **loop_guard_timeout**  integer | Loop-guard timeout (0 - 120 min). |
| **mac_addr**  string | Port/Trunk MAC. |
| **matched_dpp_intf_tags**  string | Matched interface tags in the dynamic port policy. |
| **matched_dpp_policy**  string | Matched child policy in the dynamic port policy. |
| **max_bundle**  integer | Maximum size of LAG bundle (1 - 24). |
| **mcast_snooping_flood_traffic**  string | Enable/disable flooding of IGMP snooping traffic to this interface.  Choices:   - `"enable"` - `"disable"` |
| **mclag**  string | Enable/disable multi-chassis link aggregation (MCLAG).  Choices:   - `"enable"` - `"disable"` |
| **mclag_icl_port**  integer | MCLAG-ICL port. |
| **media_type**  string | Media type. |
| **member_withdrawal_behavior**  string | Port behavior after it withdraws because of loss of control packets.  Choices:   - `"forward"` - `"block"` |
| **members**  list / elements=dictionary | Aggregated LAG bundle interfaces. |
| **member_name**  string | Interface name from available options. |
| **min_bundle**  integer | Minimum size of LAG bundle (1 - 24). |
| **mode**  string | LACP mode: ignore and do not send control messages, or negotiate 802.3ad aggregation passively or actively.  Choices:   - `"static"` - `"lacp-passive"` - `"lacp-active"` |
| **p2p_port**  integer | General peer to peer tunnel port. |
| **packet_sample_rate**  integer | Packet sampling rate (0 - 99999 p/sec). |
| **packet_sampler**  string | Enable/disable packet sampling on this interface.  Choices:   - `"enabled"` - `"disabled"` |
| **pause_meter**  integer | Configure ingress pause metering rate, in kbps . |
| **pause_meter_resume**  string | Resume threshold for resuming traffic on ingress port.  Choices:   - `"75%"` - `"50%"` - `"25%"` |
| **poe_capable**  integer | PoE capable. |
| **poe_max_power**  string | PoE maximum power. |
| **poe_pre_standard_detection**  string | Enable/disable PoE pre-standard detection.  Choices:   - `"enable"` - `"disable"` |
| **poe_standard**  string | PoE standard supported. |
| **poe_status**  string | Enable/disable PoE status.  Choices:   - `"enable"` - `"disable"` |
| **port_name**  string | Switch port name. |
| **port_number**  integer | Port number. |
| **port_owner**  string | Switch port name. |
| **port_policy**  string | Switch controller dynamic port policy from available options. Source switch-controller.dynamic-port-policy.name. |
| **port_prefix_type**  integer | Port prefix type. |
| **port_security_policy**  string | Switch controller authentication policy to apply to this managed switch from available options. Source switch-controller .security-policy.802-1X.name. |
| **port_selection_criteria**  string | Algorithm for aggregate port selection.  Choices:   - `"src-mac"` - `"dst-mac"` - `"src-dst-mac"` - `"src-ip"` - `"dst-ip"` - `"src-dst-ip"` |
| **ptp_policy**  string | PTP policy configuration. Source switch-controller.ptp.policy.name. |
| **qos_policy**  string | Switch controller QoS policy from available options. Source switch-controller.qos.qos-policy.name. |
| **rpvst_port**  string | Enable/disable inter-operability with rapid PVST on this interface.  Choices:   - `"disabled"` - `"enabled"` |
| **sample_direction**  string | Packet sampling direction.  Choices:   - `"tx"` - `"rx"` - `"both"` |
| **sflow_counter_interval**  integer | sFlow sampling counter polling interval in seconds (0 - 255). |
| **sflow_sample_rate**  integer | sFlow sampler sample rate (0 - 99999 p/sec). |
| **sflow_sampler**  string | Enable/disable sFlow protocol on this interface.  Choices:   - `"enabled"` - `"disabled"` |
| **speed**  string | Switch port speed; default and available settings depend on hardware.  Choices:   - `"10half"` - `"10full"` - `"100half"` - `"100full"` - `"1000auto"` - `"1000fiber"` - `"1000full"` - `"10000"` - `"40000"` - `"auto"` - `"auto-module"` - `"100FX-half"` - `"100FX-full"` - `"100000full"` - `"2500auto"` - `"25000full"` - `"50000full"` - `"10000cr"` - `"10000sr"` - `"100000sr4"` - `"100000cr4"` - `"25000cr4"` - `"25000sr4"` - `"5000full"` - `"1000full-fiber"` - `"10000full"` - `"40000full"` - `"40000sr4"` - `"40000cr4"` - `"25000cr"` - `"25000sr"` - `"50000cr"` - `"50000sr"` - `"5000auto"` - `"2500full"` |
| **speed_mask**  integer | Switch port speed mask. |
| **stacking_port**  integer | Stacking port. |
| **status**  string | Switch port admin status: up or down.  Choices:   - `"up"` - `"down"` |
| **sticky_mac**  string | Enable or disable sticky-mac on the interface.  Choices:   - `"enable"` - `"disable"` |
| **storm_control_policy**  string | Switch controller storm control policy from available options. Source switch-controller.storm-control-policy.name. |
| **stp_bpdu_guard**  string | Enable/disable STP BPDU guard on this interface.  Choices:   - `"enabled"` - `"disabled"` |
| **stp_bpdu_guard_timeout**  integer | BPDU Guard disabling protection (0 - 120 min). |
| **stp_root_guard**  string | Enable/disable STP root guard on this interface.  Choices:   - `"enabled"` - `"disabled"` |
| **stp_state**  string | Enable/disable Spanning Tree Protocol (STP) on this interface.  Choices:   - `"enabled"` - `"disabled"` |
| **switch_id**  string | Switch id. |
| **type**  string | Interface type: physical or trunk port.  Choices:   - `"physical"` - `"trunk"` |
| **untagged_vlans**  list / elements=dictionary | Configure switch port untagged VLANs. |
| **vlan_name**  string | VLAN name. Source system.interface.name. |
| **virtual_port**  integer | Virtualized switch port. |
| **vlan**  string | Assign switch ports to a VLAN. Source system.interface.name. |
| **pre_provisioned**  integer | Pre-provisioned managed switch. |
| **qos_drop_policy**  string | Set QoS drop-policy.  Choices:   - `"taildrop"` - `"random-early-detection"` |
| **qos_red_probability**  integer | Set QoS RED/WRED drop probability. |
| **remote_log**  list / elements=dictionary | Configure logging by FortiSwitch device to a remote syslog server. |
| **csv**  string | Enable/disable comma-separated value (CSV) strings.  Choices:   - `"enable"` - `"disable"` |
| **facility**  string | Facility to log to remote syslog server.  Choices:   - `"kernel"` - `"user"` - `"mail"` - `"daemon"` - `"auth"` - `"syslog"` - `"lpr"` - `"news"` - `"uucp"` - `"cron"` - `"authpriv"` - `"ftp"` - `"ntp"` - `"audit"` - `"alert"` - `"clock"` - `"local0"` - `"local1"` - `"local2"` - `"local3"` - `"local4"` - `"local5"` - `"local6"` - `"local7"` |
| **name**  string | Remote log name. |
| **port**  integer | Remote syslog server listening port. |
| **server**  string | IPv4 address of the remote syslog server. |
| **severity**  string | Severity of logs to be transferred to remote log server.  Choices:   - `"emergency"` - `"alert"` - `"critical"` - `"error"` - `"warning"` - `"notification"` - `"information"` - `"debug"` |
| **status**  string | Enable/disable logging by FortiSwitch device to a remote syslog server.  Choices:   - `"enable"` - `"disable"` |
| **settings_802_1X**  dictionary | Configuration method to edit FortiSwitch 802.1X global settings. |
| **link_down_auth**  string | Authentication state to set if a link is down.  Choices:   - `"set-unauth"` - `"no-action"` |
| **local_override**  string | Enable to override global 802.1X settings on individual FortiSwitches.  Choices:   - `"enable"` - `"disable"` |
| **mab_reauth**  string | Enable or disable MAB reauthentication settings.  Choices:   - `"disable"` - `"enable"` |
| **max_reauth_attempt**  integer | Maximum number of authentication attempts (0 - 15). |
| **reauth_period**  integer | Reauthentication time interval (1 - 1440 min). |
| **tx_period**  integer | 802.1X Tx period (seconds). |
| **snmp_community**  list / elements=dictionary | Configuration method to edit Simple Network Management Protocol (SNMP) communities. |
| **events**  list / elements=string | SNMP notifications (traps) to send.  Choices:   - `"cpu-high"` - `"mem-low"` - `"log-full"` - `"intf-ip"` - `"ent-conf-change"` |
| **hosts**  list / elements=dictionary | Configure IPv4 SNMP managers (hosts). |
| **id**  integer | Host entry ID. |
| **ip**  string | IPv4 address of the SNMP manager (host). |
| **id**  integer | SNMP community ID. |
| **name**  string | SNMP community name. |
| **query_v1_port**  integer | SNMP v1 query port . |
| **query_v1_status**  string | Enable/disable SNMP v1 queries.  Choices:   - `"disable"` - `"enable"` |
| **query_v2c_port**  integer | SNMP v2c query port . |
| **query_v2c_status**  string | Enable/disable SNMP v2c queries.  Choices:   - `"disable"` - `"enable"` |
| **status**  string | Enable/disable this SNMP community.  Choices:   - `"disable"` - `"enable"` |
| **trap_v1_lport**  integer | SNMP v2c trap local port . |
| **trap_v1_rport**  integer | SNMP v2c trap remote port . |
| **trap_v1_status**  string | Enable/disable SNMP v1 traps.  Choices:   - `"disable"` - `"enable"` |
| **trap_v2c_lport**  integer | SNMP v2c trap local port . |
| **trap_v2c_rport**  integer | SNMP v2c trap remote port . |
| **trap_v2c_status**  string | Enable/disable SNMP v2c traps.  Choices:   - `"disable"` - `"enable"` |
| **snmp_sysinfo**  dictionary | Configuration method to edit Simple Network Management Protocol (SNMP) system info. |
| **contact_info**  string | Contact information. |
| **description**  string | System description. |
| **engine_id**  string | Local SNMP engine ID string (max 24 char). |
| **location**  string | System location. |
| **status**  string | Enable/disable SNMP.  Choices:   - `"disable"` - `"enable"` |
| **snmp_trap_threshold**  dictionary | Configuration method to edit Simple Network Management Protocol (SNMP) trap threshold values. |
| **trap_high_cpu_threshold**  integer | CPU usage when trap is sent. |
| **trap_log_full_threshold**  integer | Log disk usage when trap is sent. |
| **trap_low_memory_threshold**  integer | Memory usage when trap is sent. |
| **snmp_user**  list / elements=dictionary | Configuration method to edit Simple Network Management Protocol (SNMP) users. |
| **auth_proto**  string | Authentication protocol.  Choices:   - `"md5"` - `"sha1"` - `"sha224"` - `"sha256"` - `"sha384"` - `"sha512"` - `"sha"` |
| **auth_pwd**  string | Password for authentication protocol. |
| **name**  string | SNMP user name. |
| **priv_proto**  string | Privacy (encryption) protocol.  Choices:   - `"aes128"` - `"aes192"` - `"aes192c"` - `"aes256"` - `"aes256c"` - `"des"` - `"aes"` |
| **priv_pwd**  string | Password for privacy (encryption) protocol. |
| **queries**  string | Enable/disable SNMP queries for this user.  Choices:   - `"disable"` - `"enable"` |
| **query_port**  integer | SNMPv3 query port . |
| **security_level**  string | Security level for message authentication and encryption.  Choices:   - `"no-auth-no-priv"` - `"auth-no-priv"` - `"auth-priv"` |
| **staged_image_version**  string | Staged image version for FortiSwitch. |
| **static_mac**  list / elements=dictionary | Configuration method to edit FortiSwitch Static and Sticky MAC. |
| **description**  string | Description. |
| **id**  integer | ID. |
| **interface**  string | Interface name. |
| **mac**  string | MAC address. |
| **type**  string | Type.  Choices:   - `"static"` - `"sticky"` |
| **vlan**  string | Vlan. Source system.interface.name. |
| **storm_control**  dictionary | Configuration method to edit FortiSwitch storm control for measuring traffic activity using data rates to prevent traffic disruption. |
| **broadcast**  string | Enable/disable storm control to drop broadcast traffic.  Choices:   - `"enable"` - `"disable"` |
| **local_override**  string | Enable to override global FortiSwitch storm control settings for this FortiSwitch.  Choices:   - `"enable"` - `"disable"` |
| **rate**  integer | Rate in packets per second at which storm traffic is controlled (1 - 10000000). Storm control drops excess traffic data rates beyond this threshold. |
| **unknown_multicast**  string | Enable/disable storm control to drop unknown multicast traffic.  Choices:   - `"enable"` - `"disable"` |
| **unknown_unicast**  string | Enable/disable storm control to drop unknown unicast traffic.  Choices:   - `"enable"` - `"disable"` |
| **stp_instance**  list / elements=dictionary | Configuration method to edit Spanning Tree Protocol (STP) instances. |
| **id**  string | Instance ID. |
| **priority**  string | Priority.  Choices:   - `"0"` - `"4096"` - `"8192"` - `"12288"` - `"16384"` - `"20480"` - `"24576"` - `"28672"` - `"32768"` - `"36864"` - `"40960"` - `"45056"` - `"49152"` - `"53248"` - `"57344"` - `"61440"` |
| **stp_settings**  dictionary | Configuration method to edit Spanning Tree Protocol (STP) settings used to prevent bridge loops. |
| **forward_time**  integer | Period of time a port is in listening and learning state (4 - 30 sec). |
| **hello_time**  integer | Period of time between successive STP frame Bridge Protocol Data Units (BPDUs) sent on a port (1 - 10 sec). |
| **local_override**  string | Enable to configure local STP settings that override global STP settings.  Choices:   - `"enable"` - `"disable"` |
| **max_age**  integer | Maximum time before a bridge port saves its configuration BPDU information (6 - 40 sec). |
| **max_hops**  integer | Maximum number of hops between the root bridge and the furthest bridge (1- 40). |
| **name**  string | Name of local STP settings configuration. |
| **pending_timer**  integer | Pending time (1 - 15 sec). |
| **revision**  integer | STP revision number (0 - 65535). |
| **status**  string | Enable/disable STP.  Choices:   - `"enable"` - `"disable"` |
| **switch_device_tag**  string | User definable label/tag. |
| **switch_dhcp_opt43_key**  string | DHCP option43 key. |
| **switch_id**  string | Managed-switch id. |
| **switch_log**  dictionary | Configuration method to edit FortiSwitch logging settings (logs are transferred to and inserted into the FortiGate event log). |
| **local_override**  string | Enable to configure local logging settings that override global logging settings.  Choices:   - `"enable"` - `"disable"` |
| **severity**  string | Severity of FortiSwitch logs that are added to the FortiGate event log.  Choices:   - `"emergency"` - `"alert"` - `"critical"` - `"error"` - `"warning"` - `"notification"` - `"information"` - `"debug"` |
| **status**  string | Enable/disable adding FortiSwitch logs to the FortiGate event log.  Choices:   - `"enable"` - `"disable"` |
| **switch_profile**  string | FortiSwitch profile. Source switch-controller.switch-profile.name. |
| **switch_stp_settings**  dictionary | Configure spanning tree protocol (STP). |
| **status**  string | Enable/disable STP.  Choices:   - `"enable"` - `"disable"` |
| **tdr_supported**  string | TDR supported. |
| **type**  string | Indication of switch type, physical or virtual.  Choices:   - `"virtual"` - `"physical"` |
| **version**  integer | FortiSwitch version. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_switch_controller_managed_switch_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_switch_controller_managed_switch_module.md#id5)

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
  - name: Configure FortiSwitch devices that are managed by this FortiGate.
    fortios_switch_controller_managed_switch:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      switch_controller_managed_switch:
        settings_802_1X:
            link_down_auth: "set-unauth"
            local_override: "enable"
            mab_reauth: "disable"
            max_reauth_attempt: "3"
            reauth_period: "60"
            tx_period: "30"
        access_profile: "<your_own_value> (source switch-controller.security-policy.local-access.name)"
        custom_command:
         -
            command_entry: "<your_own_value>"
            command_name: "<your_own_value> (source switch-controller.custom-command.command-name)"
        delayed_restart_trigger: "0"
        description: "<your_own_value>"
        dhcp_server_access_list: "global"
        directly_connected: "0"
        dynamic_capability: "<your_own_value>"
        dynamically_discovered: "0"
        firmware_provision: "enable"
        firmware_provision_latest: "disable"
        firmware_provision_version: "<your_own_value>"
        flow_identity: "<your_own_value>"
        fsw_wan1_admin: "discovered"
        fsw_wan1_peer: "<your_own_value> (source system.interface.name)"
        fsw_wan2_admin: "discovered"
        fsw_wan2_peer: "<your_own_value>"
        igmp_snooping:
            aging_time: "300"
            flood_unknown_multicast: "enable"
            local_override: "enable"
            vlans:
             -
                proxy: "disable"
                querier: "disable"
                querier_addr: "<your_own_value>"
                version: "2"
                vlan_name: "<your_own_value> (source system.interface.name)"
        ip_source_guard:
         -
            binding_entry:
             -
                entry_name: "<your_own_value>"
                ip: "<your_own_value>"
                mac: "<your_own_value>"
            description: "<your_own_value>"
            port: "<your_own_value>"
        l3_discovered: "0"
        max_allowed_trunk_members: "0"
        mclag_igmp_snooping_aware: "enable"
        mirror:
         -
            dst: "<your_own_value>"
            name: "default_name_50"
            src_egress:
             -
                name: "default_name_52"
            src_ingress:
             -
                name: "default_name_54"
            status: "active"
            switching_packet: "enable"
        name: "default_name_57"
        override_snmp_community: "enable"
        override_snmp_sysinfo: "disable"
        override_snmp_trap_threshold: "enable"
        override_snmp_user: "enable"
        owner_vdom: "<your_own_value>"
        poe_detection_type: "0"
        poe_lldp_detection: "enable"
        poe_pre_standard_detection: "enable"
        ports:
         -
            access_mode: "dynamic"
            aggregator_mode: "bandwidth"
            allowed_vlans:
             -
                vlan_name: "<your_own_value> (source system.interface.name)"
            allowed_vlans_all: "enable"
            arp_inspection_trust: "untrusted"
            bundle: "enable"
            description: "<your_own_value>"
            dhcp_snoop_option82_trust: "enable"
            dhcp_snooping: "untrusted"
            discard_mode: "none"
            edge_port: "enable"
            export_tags:
             -
                tag_name: "<your_own_value> (source switch-controller.switch-interface-tag.name)"
            export_to: "<your_own_value> (source system.vdom.name)"
            export_to_pool: "<your_own_value> (source switch-controller.virtual-port-pool.name)"
            export_to_pool_flag: "0"
            fec_capable: "0"
            fec_state: "disabled"
            fgt_peer_device_name: "<your_own_value>"
            fgt_peer_port_name: "<your_own_value>"
            fiber_port: "0"
            flags: "0"
            flap_duration: "30"
            flap_rate: "5"
            flap_timeout: "0"
            flapguard: "enable"
            flow_control: "disable"
            fortilink_port: "0"
            igmp_snooping: "enable"
            igmp_snooping_flood_reports: "enable"
            igmps_flood_reports: "enable"
            igmps_flood_traffic: "enable"
            interface_tags:
             -
                tag_name: "<your_own_value> (source switch-controller.switch-interface-tag.name)"
            ip_source_guard: "disable"
            isl_local_trunk_name: "<your_own_value>"
            isl_peer_device_name: "<your_own_value>"
            isl_peer_port_name: "<your_own_value>"
            lacp_speed: "slow"
            learning_limit: "0"
            lldp_profile: "<your_own_value> (source switch-controller.lldp-profile.name)"
            lldp_status: "disable"
            loop_guard: "enabled"
            loop_guard_timeout: "45"
            mac_addr: "<your_own_value>"
            matched_dpp_intf_tags: "<your_own_value>"
            matched_dpp_policy: "<your_own_value>"
            max_bundle: "24"
            mcast_snooping_flood_traffic: "enable"
            mclag: "enable"
            mclag_icl_port: "0"
            media_type: "<your_own_value>"
            member_withdrawal_behavior: "forward"
            members:
             -
                member_name: "<your_own_value>"
            min_bundle: "1"
            mode: "static"
            p2p_port: "0"
            packet_sample_rate: "512"
            packet_sampler: "enabled"
            pause_meter: "0"
            pause_meter_resume: "75%"
            poe_capable: "0"
            poe_max_power: "<your_own_value>"
            poe_pre_standard_detection: "enable"
            poe_standard: "<your_own_value>"
            poe_status: "enable"
            port_name: "<your_own_value>"
            port_number: "0"
            port_owner: "<your_own_value>"
            port_policy: "<your_own_value> (source switch-controller.dynamic-port-policy.name)"
            port_prefix_type: "0"
            port_security_policy: "<your_own_value> (source switch-controller.security-policy.802-1X.name)"
            port_selection_criteria: "src-mac"
            ptp_policy: "<your_own_value> (source switch-controller.ptp.policy.name)"
            qos_policy: "<your_own_value> (source switch-controller.qos.qos-policy.name)"
            rpvst_port: "disabled"
            sample_direction: "tx"
            sflow_counter_interval: "0"
            sflow_sample_rate: "49999"
            sflow_sampler: "enabled"
            speed: "10half"
            speed_mask: "2147483647"
            stacking_port: "0"
            status: "up"
            sticky_mac: "enable"
            storm_control_policy: "<your_own_value> (source switch-controller.storm-control-policy.name)"
            stp_bpdu_guard: "enabled"
            stp_bpdu_guard_timeout: "5"
            stp_root_guard: "enabled"
            stp_state: "enabled"
            switch_id: "<your_own_value>"
            type: "physical"
            untagged_vlans:
             -
                vlan_name: "<your_own_value> (source system.interface.name)"
            virtual_port: "0"
            vlan: "<your_own_value> (source system.interface.name)"
        pre_provisioned: "0"
        qos_drop_policy: "taildrop"
        qos_red_probability: "12"
        remote_log:
         -
            csv: "enable"
            facility: "kernel"
            name: "default_name_171"
            port: "514"
            server: "192.168.100.40"
            severity: "emergency"
            status: "enable"
        snmp_community:
         -
            events: "cpu-high"
            hosts:
             -
                id:  "179"
                ip: "<your_own_value>"
            id:  "181"
            name: "default_name_182"
            query_v1_port: "161"
            query_v1_status: "disable"
            query_v2c_port: "161"
            query_v2c_status: "disable"
            status: "disable"
            trap_v1_lport: "162"
            trap_v1_rport: "162"
            trap_v1_status: "disable"
            trap_v2c_lport: "162"
            trap_v2c_rport: "162"
            trap_v2c_status: "disable"
        snmp_sysinfo:
            contact_info: "<your_own_value>"
            description: "<your_own_value>"
            engine_id: "<your_own_value>"
            location: "<your_own_value>"
            status: "disable"
        snmp_trap_threshold:
            trap_high_cpu_threshold: "80"
            trap_log_full_threshold: "90"
            trap_low_memory_threshold: "80"
        snmp_user:
         -
            auth_proto: "md5"
            auth_pwd: "<your_own_value>"
            name: "default_name_207"
            priv_proto: "aes128"
            priv_pwd: "<your_own_value>"
            queries: "disable"
            query_port: "161"
            security_level: "no-auth-no-priv"
        staged_image_version: "<your_own_value>"
        static_mac:
         -
            description: "<your_own_value>"
            id:  "216"
            interface: "<your_own_value>"
            mac: "<your_own_value>"
            type: "static"
            vlan: "<your_own_value> (source system.interface.name)"
        storm_control:
            broadcast: "enable"
            local_override: "enable"
            rate: "500"
            unknown_multicast: "enable"
            unknown_unicast: "enable"
        stp_instance:
         -
            id:  "228"
            priority: "0"
        stp_settings:
            forward_time: "15"
            hello_time: "2"
            local_override: "enable"
            max_age: "20"
            max_hops: "20"
            name: "default_name_236"
            pending_timer: "4"
            revision: "0"
            status: "enable"
        switch_device_tag: "<your_own_value>"
        switch_dhcp_opt43_key: "<your_own_value>"
        switch_id: "<your_own_value>"
        switch_log:
            local_override: "enable"
            severity: "emergency"
            status: "enable"
        switch_profile: "<your_own_value> (source switch-controller.switch-profile.name)"
        switch_stp_settings:
            status: "enable"
        tdr_supported: "<your_own_value>"
        type: "virtual"
        version: "0"
```

## [Return Values](fortios_switch_controller_managed_switch_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  Returned: always  Sample: `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  Returned: always  Sample: `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  Returned: always  Sample: `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  Returned: success  Sample: `"id"` |
| **name**  string | Name of the table used to fulfill the request  Returned: always  Sample: `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  Returned: always  Sample: `"webfilter"` |
| **revision**  string | Internal revision number  Returned: always  Sample: `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  Returned: always  Sample: `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  Returned: always  Sample: `"success"` |
| **vdom**  string | Virtual domain used  Returned: always  Sample: `"root"` |
| **version**  string | Version of the FortiGate  Returned: always  Sample: `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
[Homepage](https://www.fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
