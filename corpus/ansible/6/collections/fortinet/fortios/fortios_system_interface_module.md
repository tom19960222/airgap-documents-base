---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_system_interface module – Configure interfaces in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_system_interface_module.html
fetched_at: 2026-07-27T17:44:40+00:00
---
# fortinet.fortios.fortios_system_interface module – Configure interfaces in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_system_interface_module.md#ansible-collections-fortinet-fortios-fortios-system-interface-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_interface`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_interface_module.md#synopsis)
- [Requirements](fortios_system_interface_module.md#requirements)
- [Parameters](fortios_system_interface_module.md#parameters)
- [Notes](fortios_system_interface_module.md#notes)
- [Examples](fortios_system_interface_module.md#examples)
- [Return Values](fortios_system_interface_module.md#return-values)

## [Synopsis](fortios_system_interface_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and interface category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_interface_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_system_interface_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **system_interface**  dictionary | Configure interfaces. |
| **ac_name**  string | PPPoE server name. |
| **aggregate**  string | Aggregate interface. |
| **aggregate_type**  string | Type of aggregation.  Choices:   - `"physical"` - `"vxlan"` |
| **algorithm**  string | Frame distribution algorithm.  Choices:   - `"L2"` - `"L3"` - `"L4"` - `"Source-MAC"` |
| **alias**  string | Alias will be displayed with the interface name to make it easier to distinguish. |
| **allowaccess**  list / elements=string | Permitted types of management access to this interface.  Choices:   - `"ping"` - `"https"` - `"ssh"` - `"snmp"` - `"http"` - `"telnet"` - `"fgfm"` - `"radius-acct"` - `"probe-response"` - `"fabric"` - `"ftm"` - `"speed-test"` - `"capwap"` |
| **ap_discover**  string | Enable/disable automatic registration of unknown FortiAP devices.  Choices:   - `"enable"` - `"disable"` |
| **arpforward**  string | Enable/disable ARP forwarding.  Choices:   - `"enable"` - `"disable"` |
| **auth_cert**  string | HTTPS server certificate. Source vpn.certificate.local.name. |
| **auth_portal_addr**  string | Address of captive portal. |
| **auth_type**  string | PPP authentication type to use.  Choices:   - `"auto"` - `"pap"` - `"chap"` - `"mschapv1"` - `"mschapv2"` |
| **auto_auth_extension_device**  string | Enable/disable automatic authorization of dedicated Fortinet extension device on this interface.  Choices:   - `"enable"` - `"disable"` |
| **bandwidth_measure_time**  integer | Bandwidth measure time. |
| **bfd**  string | Bidirectional Forwarding Detection (BFD) settings.  Choices:   - `"global"` - `"enable"` - `"disable"` |
| **bfd_desired_min_tx**  integer | BFD desired minimal transmit interval. |
| **bfd_detect_mult**  integer | BFD detection multiplier. |
| **bfd_required_min_rx**  integer | BFD required minimal receive interval. |
| **broadcast_forticlient_discovery**  string | Enable/disable broadcasting FortiClient discovery messages.  Choices:   - `"enable"` - `"disable"` |
| **broadcast_forward**  string | Enable/disable broadcast forwarding.  Choices:   - `"enable"` - `"disable"` |
| **captive_portal**  integer | Enable/disable captive portal. |
| **cli_conn_status**  integer | CLI connection status. |
| **client_options**  list / elements=dictionary | DHCP client options. |
| **code**  integer | DHCP client option code. |
| **id**  integer | ID. |
| **ip**  list / elements=string | DHCP option IPs. |
| **type**  string | DHCP client option type.  Choices:   - `"hex"` - `"string"` - `"ip"` - `"fqdn"` |
| **value**  string | DHCP client option value. |
| **color**  integer | Color of icon on the GUI. |
| **dedicated_to**  string | Configure interface for single purpose.  Choices:   - `"none"` - `"management"` |
| **defaultgw**  string | Enable to get the gateway IP from the DHCP or PPPoE server.  Choices:   - `"enable"` - `"disable"` |
| **description**  string | Description. |
| **detected_peer_mtu**  integer | MTU of detected peer (0 - 4294967295). |
| **detectprotocol**  list / elements=string | Protocols used to detect the server.  Choices:   - `"ping"` - `"tcp-echo"` - `"udp-echo"` |
| **detectserver**  string | Gateway”s ping server for this IP. |
| **device_access_list**  string | Device access list. |
| **device_identification**  string | Enable/disable passively gathering of device identity information about the devices on the network connected to this interface.  Choices:   - `"enable"` - `"disable"` |
| **device_identification_active_scan**  string | Enable/disable active gathering of device identity information about the devices on the network connected to this interface.  Choices:   - `"enable"` - `"disable"` |
| **device_netscan**  string | Enable/disable inclusion of devices detected on this interface in network vulnerability scans.  Choices:   - `"disable"` - `"enable"` |
| **device_user_identification**  string | Enable/disable passive gathering of user identity information about users on this interface.  Choices:   - `"enable"` - `"disable"` |
| **devindex**  integer | Device Index. |
| **dhcp_classless_route_addition**  string | Enable/disable addition of classless static routes retrieved from DHCP server.  Choices:   - `"enable"` - `"disable"` |
| **dhcp_client_identifier**  string | DHCP client identifier. |
| **dhcp_relay_agent_option**  string | Enable/disable DHCP relay agent option.  Choices:   - `"enable"` - `"disable"` |
| **dhcp_relay_interface**  string | Specify outgoing interface to reach server. Source system.interface.name. |
| **dhcp_relay_interface_select_method**  string | Specify how to select outgoing interface to reach server.  Choices:   - `"auto"` - `"sdwan"` - `"specify"` |
| **dhcp_relay_ip**  list / elements=string | DHCP relay IP address. |
| **dhcp_relay_link_selection**  string | DHCP relay link selection. |
| **dhcp_relay_request_all_server**  string | Enable/disable sending of DHCP requests to all servers.  Choices:   - `"disable"` - `"enable"` |
| **dhcp_relay_service**  string | Enable/disable allowing this interface to act as a DHCP relay.  Choices:   - `"disable"` - `"enable"` |
| **dhcp_relay_type**  string | DHCP relay type (regular or IPsec).  Choices:   - `"regular"` - `"ipsec"` |
| **dhcp_renew_time**  integer | DHCP renew time in seconds (300-604800), 0 means use the renew time provided by the server. |
| **dhcp_snooping_server_list**  list / elements=dictionary | Configure DHCP server access list. |
| **name**  string | DHCP server name. |
| **server_ip**  string | IP address for DHCP server. |
| **disc_retry_timeout**  integer | Time in seconds to wait before retrying to start a PPPoE discovery, 0 means no timeout. |
| **disconnect_threshold**  integer | Time in milliseconds to wait before sending a notification that this interface is down or disconnected. |
| **distance**  integer | Distance for routes learned through PPPoE or DHCP, lower distance indicates preferred route. |
| **dns_server_override**  string | Enable/disable use DNS acquired by DHCP or PPPoE.  Choices:   - `"enable"` - `"disable"` |
| **dns_server_protocol**  list / elements=string | DNS transport protocols.  Choices:   - `"cleartext"` - `"dot"` - `"doh"` |
| **drop_fragment**  string | Enable/disable drop fragment packets.  Choices:   - `"enable"` - `"disable"` |
| **drop_overlapped_fragment**  string | Enable/disable drop overlapped fragment packets.  Choices:   - `"enable"` - `"disable"` |
| **eap_ca_cert**  string | EAP CA certificate name. Source certificate.ca.name. |
| **eap_identity**  string | EAP identity. |
| **eap_method**  string | EAP method.  Choices:   - `"tls"` - `"peap"` |
| **eap_password**  string | EAP password. |
| **eap_supplicant**  string | Enable/disable EAP-Supplicant.  Choices:   - `"enable"` - `"disable"` |
| **eap_user_cert**  string | EAP user certificate name. Source certificate.local.name. |
| **egress_cos**  string | Override outgoing CoS in user VLAN tag.  Choices:   - `"disable"` - `"cos0"` - `"cos1"` - `"cos2"` - `"cos3"` - `"cos4"` - `"cos5"` - `"cos6"` - `"cos7"` |
| **egress_queues**  dictionary | Configure queues of NP port on egress path. |
| **cos0**  string | CoS profile name for CoS 0. Source system.isf-queue-profile.name. |
| **cos1**  string | CoS profile name for CoS 1. Source system.isf-queue-profile.name. |
| **cos2**  string | CoS profile name for CoS 2. Source system.isf-queue-profile.name. |
| **cos3**  string | CoS profile name for CoS 3. Source system.isf-queue-profile.name. |
| **cos4**  string | CoS profile name for CoS 4. Source system.isf-queue-profile.name. |
| **cos5**  string | CoS profile name for CoS 5. Source system.isf-queue-profile.name. |
| **cos6**  string | CoS profile name for CoS 6. Source system.isf-queue-profile.name. |
| **cos7**  string | CoS profile name for CoS 7. Source system.isf-queue-profile.name. |
| **egress_shaping_profile**  string | Outgoing traffic shaping profile. Source firewall.shaping-profile.profile-name. |
| **endpoint_compliance**  string | Enable/disable endpoint compliance enforcement.  Choices:   - `"enable"` - `"disable"` |
| **estimated_downstream_bandwidth**  integer | Estimated maximum downstream bandwidth (kbps). Used to estimate link utilization. |
| **estimated_upstream_bandwidth**  integer | Estimated maximum upstream bandwidth (kbps). Used to estimate link utilization. |
| **explicit_ftp_proxy**  string | Enable/disable the explicit FTP proxy on this interface.  Choices:   - `"enable"` - `"disable"` |
| **explicit_web_proxy**  string | Enable/disable the explicit web proxy on this interface.  Choices:   - `"enable"` - `"disable"` |
| **external**  string | Enable/disable identifying the interface as an external interface (which usually means it”s connected to the Internet).  Choices:   - `"enable"` - `"disable"` |
| **fail_action_on_extender**  string | Action on FortiExtender when interface fail.  Choices:   - `"soft-restart"` - `"hard-restart"` - `"reboot"` |
| **fail_alert_interfaces**  list / elements=dictionary | Names of the FortiGate interfaces to which the link failure alert is sent. |
| **name**  string | Names of the non-virtual interface. Source system.interface.name. |
| **fail_alert_method**  string | Select link-failed-signal or link-down method to alert about a failed link.  Choices:   - `"link-failed-signal"` - `"link-down"` |
| **fail_detect**  string | Enable/disable fail detection features for this interface.  Choices:   - `"enable"` - `"disable"` |
| **fail_detect_option**  list / elements=string | Options for detecting that this interface has failed.  Choices:   - `"detectserver"` - `"link-down"` |
| **fortiheartbeat**  string | Enable/disable FortiHeartBeat (FortiTelemetry on GUI).  Choices:   - `"enable"` - `"disable"` |
| **fortilink**  string | Enable FortiLink to dedicate this interface to manage other Fortinet devices.  Choices:   - `"enable"` - `"disable"` |
| **fortilink_backup_link**  integer | FortiLink split interface backup link. |
| **fortilink_neighbor_detect**  string | Protocol for FortiGate neighbor discovery.  Choices:   - `"lldp"` - `"fortilink"` |
| **fortilink_split_interface**  string | Enable/disable FortiLink split interface to connect member link to different FortiSwitch in stack for uplink redundancy.  Choices:   - `"enable"` - `"disable"` |
| **fortilink_stacking**  string | Enable/disable FortiLink switch-stacking on this interface.  Choices:   - `"enable"` - `"disable"` |
| **forward_domain**  integer | Transparent mode forward domain. |
| **gi_gk**  string | Enable/disable Gi Gatekeeper.  Choices:   - `"enable"` - `"disable"` |
| **gwdetect**  string | Enable/disable detect gateway alive for first.  Choices:   - `"enable"` - `"disable"` |
| **ha_priority**  integer | HA election priority for the PING server. |
| **icmp_accept_redirect**  string | Enable/disable ICMP accept redirect.  Choices:   - `"enable"` - `"disable"` |
| **icmp_send_redirect**  string | Enable/disable sending of ICMP redirects.  Choices:   - `"enable"` - `"disable"` |
| **ident_accept**  string | Enable/disable authentication for this interface.  Choices:   - `"enable"` - `"disable"` |
| **idle_timeout**  integer | PPPoE auto disconnect after idle timeout seconds, 0 means no timeout. |
| **ike_saml_server**  string | Configure IKE authentication SAML server. Source user.saml.name. |
| **inbandwidth**  integer | Bandwidth limit for incoming traffic (0 - 80000000 kbps), 0 means unlimited. |
| **ingress_cos**  string | Override incoming CoS in user VLAN tag on VLAN interface or assign a priority VLAN tag on physical interface.  Choices:   - `"disable"` - `"cos0"` - `"cos1"` - `"cos2"` - `"cos3"` - `"cos4"` - `"cos5"` - `"cos6"` - `"cos7"` |
| **ingress_shaping_profile**  string | Incoming traffic shaping profile. Source firewall.shaping-profile.profile-name. |
| **ingress_spillover_threshold**  integer | Ingress Spillover threshold (0 - 16776000 kbps), 0 means unlimited. |
| **interface**  string | Interface name. Source system.interface.name. |
| **internal**  integer | Implicitly created. |
| **ip**  string | Interface IPv4 address and subnet mask, syntax: X.X.X.X/24. |
| **ip_managed_by_fortiipam**  string | Enable/disable automatic IP address assignment of this interface by FortiIPAM.  Choices:   - `"enable"` - `"disable"` |
| **ipmac**  string | Enable/disable IP/MAC binding.  Choices:   - `"enable"` - `"disable"` |
| **ips_sniffer_mode**  string | Enable/disable the use of this interface as a one-armed sniffer.  Choices:   - `"enable"` - `"disable"` |
| **ipunnumbered**  string | Unnumbered IP used for PPPoE interfaces for which no unique local address is provided. |
| **ipv6**  dictionary | IPv6 of interface. |
| **autoconf**  string | Enable/disable address auto config.  Choices:   - `"enable"` - `"disable"` |
| **cli_conn6_status**  integer | CLI IPv6 connection status. |
| **dhcp6_client_options**  list / elements=string | DHCPv6 client options.  Choices:   - `"rapid"` - `"iapd"` - `"iana"` |
| **dhcp6_iapd_list**  list / elements=dictionary | DHCPv6 IA-PD list. |
| **iaid**  integer | Identity association identifier. |
| **prefix_hint**  string | DHCPv6 prefix that will be used as a hint to the upstream DHCPv6 server. |
| **prefix_hint_plt**  integer | DHCPv6 prefix hint preferred life time (sec), 0 means unlimited lease time. |
| **prefix_hint_vlt**  integer | DHCPv6 prefix hint valid life time (sec). |
| **dhcp6_information_request**  string | Enable/disable DHCPv6 information request.  Choices:   - `"enable"` - `"disable"` |
| **dhcp6_prefix_delegation**  string | Enable/disable DHCPv6 prefix delegation.  Choices:   - `"enable"` - `"disable"` |
| **dhcp6_prefix_hint**  string | DHCPv6 prefix that will be used as a hint to the upstream DHCPv6 server. |
| **dhcp6_prefix_hint_plt**  integer | DHCPv6 prefix hint preferred life time (sec), 0 means unlimited lease time. |
| **dhcp6_prefix_hint_vlt**  integer | DHCPv6 prefix hint valid life time (sec). |
| **dhcp6_relay_ip**  list / elements=string | DHCPv6 relay IP address. |
| **dhcp6_relay_service**  string | Enable/disable DHCPv6 relay.  Choices:   - `"disable"` - `"enable"` |
| **dhcp6_relay_type**  string | DHCPv6 relay type.  Choices:   - `"regular"` |
| **icmp6_send_redirect**  string | Enable/disable sending of ICMPv6 redirects.  Choices:   - `"enable"` - `"disable"` |
| **interface_identifier**  string | IPv6 interface identifier. |
| **ip6_address**  string | Primary IPv6 address prefix. Syntax: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx. |
| **ip6_allowaccess**  list / elements=string | Allow management access to the interface.  Choices:   - `"ping"` - `"https"` - `"ssh"` - `"snmp"` - `"http"` - `"telnet"` - `"fgfm"` - `"fabric"` - `"capwap"` |
| **ip6_default_life**  integer | Default life (sec). |
| **ip6_delegated_prefix_iaid**  integer | IAID of obtained delegated-prefix from the upstream interface. |
| **ip6_delegated_prefix_list**  list / elements=dictionary | Advertised IPv6 delegated prefix list. |
| **autonomous_flag**  string | Enable/disable the autonomous flag.  Choices:   - `"enable"` - `"disable"` |
| **delegated_prefix_iaid**  integer | IAID of obtained delegated-prefix from the upstream interface. |
| **onlink_flag**  string | Enable/disable the onlink flag.  Choices:   - `"enable"` - `"disable"` |
| **prefix_id**  integer | Prefix ID. |
| **rdnss**  list / elements=string | Recursive DNS server option. |
| **rdnss_service**  string | Recursive DNS service option.  Choices:   - `"delegated"` - `"default"` - `"specify"` |
| **subnet**  string | Add subnet ID to routing prefix. |
| **upstream_interface**  string | Name of the interface that provides delegated information. Source system.interface.name. |
| **ip6_dns_server_override**  string | Enable/disable using the DNS server acquired by DHCP.  Choices:   - `"enable"` - `"disable"` |
| **ip6_extra_addr**  list / elements=dictionary | Extra IPv6 address prefixes of interface. |
| **prefix**  string | IPv6 address prefix. |
| **ip6_hop_limit**  integer | Hop limit (0 means unspecified). |
| **ip6_link_mtu**  integer | IPv6 link MTU. |
| **ip6_manage_flag**  string | Enable/disable the managed flag.  Choices:   - `"enable"` - `"disable"` |
| **ip6_max_interval**  integer | IPv6 maximum interval (4 to 1800 sec). |
| **ip6_min_interval**  integer | IPv6 minimum interval (3 to 1350 sec). |
| **ip6_mode**  string | Addressing mode (static, DHCP, delegated).  Choices:   - `"static"` - `"dhcp"` - `"pppoe"` - `"delegated"` |
| **ip6_other_flag**  string | Enable/disable the other IPv6 flag.  Choices:   - `"enable"` - `"disable"` |
| **ip6_prefix_list**  list / elements=dictionary | Advertised prefix list. |
| **autonomous_flag**  string | Enable/disable the autonomous flag.  Choices:   - `"enable"` - `"disable"` |
| **dnssl**  list / elements=dictionary | DNS search list option. |
| **domain**  string | Domain name. |
| **onlink_flag**  string | Enable/disable the onlink flag.  Choices:   - `"enable"` - `"disable"` |
| **preferred_life_time**  integer | Preferred life time (sec). |
| **prefix**  string | IPv6 prefix. |
| **rdnss**  list / elements=string | Recursive DNS server option. |
| **valid_life_time**  integer | Valid life time (sec). |
| **ip6_prefix_mode**  string | Assigning a prefix from DHCP or RA.  Choices:   - `"dhcp6"` - `"ra"` |
| **ip6_reachable_time**  integer | IPv6 reachable time (milliseconds; 0 means unspecified). |
| **ip6_retrans_time**  integer | IPv6 retransmit time (milliseconds; 0 means unspecified). |
| **ip6_send_adv**  string | Enable/disable sending advertisements about the interface.  Choices:   - `"enable"` - `"disable"` |
| **ip6_subnet**  string | Subnet to routing prefix. Syntax: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx. |
| **ip6_upstream_interface**  string | Interface name providing delegated information. Source system.interface.name. |
| **nd_cert**  string | Neighbor discovery certificate. Source certificate.local.name. |
| **nd_cga_modifier**  string | Neighbor discovery CGA modifier. |
| **nd_mode**  string | Neighbor discovery mode.  Choices:   - `"basic"` - `"SEND-compatible"` |
| **nd_security_level**  integer | Neighbor discovery security level (0 - 7; 0 = least secure). |
| **nd_timestamp_delta**  integer | Neighbor discovery timestamp delta value (1 - 3600 sec; ). |
| **nd_timestamp_fuzz**  integer | Neighbor discovery timestamp fuzz factor (1 - 60 sec; ). |
| **ra_send_mtu**  string | Enable/disable sending link MTU in RA packet.  Choices:   - `"enable"` - `"disable"` |
| **unique_autoconf_addr**  string | Enable/disable unique auto config address.  Choices:   - `"enable"` - `"disable"` |
| **vrip6_link_local**  string | Link-local IPv6 address of virtual router. |
| **vrrp6**  list / elements=dictionary | IPv6 VRRP configuration. |
| **accept_mode**  string | Enable/disable accept mode.  Choices:   - `"enable"` - `"disable"` |
| **adv_interval**  integer | Advertisement interval (1 - 255 seconds). |
| **preempt**  string | Enable/disable preempt mode.  Choices:   - `"enable"` - `"disable"` |
| **priority**  integer | Priority of the virtual router (1 - 255). |
| **start_time**  integer | Startup time (1 - 255 seconds). |
| **status**  string | Enable/disable VRRP.  Choices:   - `"enable"` - `"disable"` |
| **vrdst6**  list / elements=string | Monitor the route to this destination. |
| **vrgrp**  integer | VRRP group ID (1 - 65535). |
| **vrid**  integer | Virtual router identifier (1 - 255). |
| **vrip6**  string | IPv6 address of the virtual router. |
| **vrrp_virtual_mac6**  string | Enable/disable virtual MAC for VRRP.  Choices:   - `"enable"` - `"disable"` |
| **l2forward**  string | Enable/disable l2 forwarding.  Choices:   - `"enable"` - `"disable"` |
| **lacp_ha_secondary**  string | LACP HA secondary member.  Choices:   - `"enable"` - `"disable"` |
| **lacp_ha_slave**  string | LACP HA slave.  Choices:   - `"enable"` - `"disable"` |
| **lacp_mode**  string | LACP mode.  Choices:   - `"static"` - `"passive"` - `"active"` |
| **lacp_speed**  string | How often the interface sends LACP messages.  Choices:   - `"slow"` - `"fast"` |
| **lcp_echo_interval**  integer | Time in seconds between PPPoE Link Control Protocol (LCP) echo requests. |
| **lcp_max_echo_fails**  integer | Maximum missed LCP echo messages before disconnect. |
| **link_up_delay**  integer | Number of milliseconds to wait before considering a link is up. |
| **lldp_network_policy**  string | LLDP-MED network policy profile. Source system.lldp.network-policy.name. |
| **lldp_reception**  string | Enable/disable Link Layer Discovery Protocol (LLDP) reception.  Choices:   - `"enable"` - `"disable"` - `"vdom"` |
| **lldp_transmission**  string | Enable/disable Link Layer Discovery Protocol (LLDP) transmission.  Choices:   - `"enable"` - `"disable"` - `"vdom"` |
| **macaddr**  string | Change the interface”s MAC address. |
| **managed_device**  list / elements=dictionary | Available when FortiLink is enabled, used for managed devices through FortiLink interface. |
| **name**  string | Managed dev identifier. |
| **managed_subnetwork_size**  string | Number of IP addresses to be allocated by FortiIPAM and used by this FortiGate unit”s DHCP server settings.  Choices:   - `"32"` - `"64"` - `"128"` - `"256"` - `"512"` - `"1024"` - `"2048"` - `"4096"` - `"8192"` - `"16384"` - `"32768"` - `"65536"` |
| **management_ip**  string | High Availability in-band management IP address of this interface. |
| **measured_downstream_bandwidth**  integer | Measured downstream bandwidth (kbps). |
| **measured_upstream_bandwidth**  integer | Measured upstream bandwidth (kbps). |
| **mediatype**  string | Select SFP media interface type  Choices:   - `"cfp2-sr10"` - `"cfp2-lr4"` |
| **member**  list / elements=dictionary | Physical interfaces that belong to the aggregate or redundant interface. |
| **interface_name**  string | Physical interface name. Source system.interface.name. |
| **min_links**  integer | Minimum number of aggregated ports that must be up. |
| **min_links_down**  string | Action to take when less than the configured minimum number of links are active.  Choices:   - `"operational"` - `"administrative"` |
| **mode**  string | Addressing mode (static, DHCP, PPPoE).  Choices:   - `"static"` - `"dhcp"` - `"pppoe"` |
| **monitor_bandwidth**  string | Enable monitoring bandwidth on this interface.  Choices:   - `"enable"` - `"disable"` |
| **mtu**  integer | MTU value for this interface. |
| **mtu_override**  string | Enable to set a custom MTU for this interface.  Choices:   - `"enable"` - `"disable"` |
| **name**  string / required | Name. |
| **ndiscforward**  string | Enable/disable NDISC forwarding.  Choices:   - `"enable"` - `"disable"` |
| **netbios_forward**  string | Enable/disable NETBIOS forwarding.  Choices:   - `"disable"` - `"enable"` |
| **netflow_sampler**  string | Enable/disable NetFlow on this interface and set the data that NetFlow collects (rx, tx, or both).  Choices:   - `"disable"` - `"tx"` - `"rx"` - `"both"` |
| **outbandwidth**  integer | Bandwidth limit for outgoing traffic (0 - 80000000 kbps). |
| **padt_retry_timeout**  integer | PPPoE Active Discovery Terminate (PADT) used to terminate sessions after an idle time. |
| **password**  string | PPPoE account”s password. |
| **ping_serv_status**  integer | PING server status. |
| **polling_interval**  integer | sFlow polling interval in seconds (1 - 255). |
| **pppoe_unnumbered_negotiate**  string | Enable/disable PPPoE unnumbered negotiation.  Choices:   - `"enable"` - `"disable"` |
| **pptp_auth_type**  string | PPTP authentication type.  Choices:   - `"auto"` - `"pap"` - `"chap"` - `"mschapv1"` - `"mschapv2"` |
| **pptp_client**  string | Enable/disable PPTP client.  Choices:   - `"enable"` - `"disable"` |
| **pptp_password**  string | PPTP password. |
| **pptp_server_ip**  string | PPTP server IP address. |
| **pptp_timeout**  integer | Idle timer in minutes (0 for disabled). |
| **pptp_user**  string | PPTP user name. |
| **preserve_session_route**  string | Enable/disable preservation of session route when dirty.  Choices:   - `"enable"` - `"disable"` |
| **priority**  integer | Priority of learned routes. |
| **priority_override**  string | Enable/disable fail back to higher priority port once recovered.  Choices:   - `"enable"` - `"disable"` |
| **proxy_captive_portal**  string | Enable/disable proxy captive portal on this interface.  Choices:   - `"enable"` - `"disable"` |
| **reachable_time**  integer | IPv4 reachable time in milliseconds (30000 - 3600000). |
| **redundant_interface**  string | Redundant interface. |
| **remote_ip**  string | Remote IP address of tunnel. |
| **replacemsg_override_group**  string | Replacement message override group. |
| **ring_rx**  integer | RX ring size. |
| **ring_tx**  integer | TX ring size. |
| **role**  string | Interface role.  Choices:   - `"lan"` - `"wan"` - `"dmz"` - `"undefined"` |
| **sample_direction**  string | Data that NetFlow collects (rx, tx, or both).  Choices:   - `"tx"` - `"rx"` - `"both"` |
| **sample_rate**  integer | sFlow sample rate (10 - 99999). |
| **scan_botnet_connections**  string | Enable monitoring or blocking connections to Botnet servers through this interface.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **secondary_IP**  string | Enable/disable adding a secondary IP to this interface.  Choices:   - `"enable"` - `"disable"` |
| **secondaryip**  list / elements=dictionary | Second IP address of interface. |
| **allowaccess**  list / elements=string | Management access settings for the secondary IP address.  Choices:   - `"ping"` - `"https"` - `"ssh"` - `"snmp"` - `"http"` - `"telnet"` - `"fgfm"` - `"radius-acct"` - `"probe-response"` - `"fabric"` - `"ftm"` - `"speed-test"` - `"capwap"` |
| **detectprotocol**  list / elements=string | Protocols used to detect the server.  Choices:   - `"ping"` - `"tcp-echo"` - `"udp-echo"` |
| **detectserver**  string | Gateway”s ping server for this IP. |
| **gwdetect**  string | Enable/disable detect gateway alive for first.  Choices:   - `"enable"` - `"disable"` |
| **ha_priority**  integer | HA election priority for the PING server. |
| **id**  integer | ID. |
| **ip**  string | Secondary IP address of the interface. |
| **ping_serv_status**  integer | PING server status. |
| **security_exempt_list**  string | Name of security-exempt-list. |
| **security_external_logout**  string | URL of external authentication logout server. |
| **security_external_web**  string | URL of external authentication web server. |
| **security_groups**  list / elements=dictionary | User groups that can authenticate with the captive portal. |
| **name**  string | Names of user groups that can authenticate with the captive portal. Source user.group.name. |
| **security_mac_auth_bypass**  string | Enable/disable MAC authentication bypass.  Choices:   - `"mac-auth-only"` - `"enable"` - `"disable"` |
| **security_mode**  string | Turn on captive portal authentication for this interface.  Choices:   - `"none"` - `"captive-portal"` - `"802.1X"` |
| **security_redirect_url**  string | URL redirection after disclaimer/authentication. |
| **service_name**  string | PPPoE service name. |
| **sflow_sampler**  string | Enable/disable sFlow on this interface.  Choices:   - `"enable"` - `"disable"` |
| **snmp_index**  integer | Permanent SNMP Index of the interface. |
| **speed**  string | Interface speed. The default setting and the options available depend on the interface hardware.  Choices:   - `"auto"` - `"10full"` - `"10half"` - `"100full"` - `"100half"` - `"1000full"` - `"1000auto"` - `"10000full"` - `"10000auto"` - `"40000full"` - `"100Gfull"` - `"1000half"` |
| **spillover_threshold**  integer | Egress Spillover threshold (0 - 16776000 kbps), 0 means unlimited. |
| **src_check**  string | Enable/disable source IP check.  Choices:   - `"enable"` - `"disable"` |
| **status**  string | Bring the interface up or shut the interface down.  Choices:   - `"up"` - `"down"` |
| **stp**  string | Enable/disable STP.  Choices:   - `"disable"` - `"enable"` |
| **stp_ha_secondary**  string | Control STP behaviour on HA secondary.  Choices:   - `"disable"` - `"enable"` - `"priority-adjust"` |
| **stp_ha_slave**  string | Control STP behaviour on HA slave.  Choices:   - `"disable"` - `"enable"` - `"priority-adjust"` |
| **stpforward**  string | Enable/disable STP forwarding.  Choices:   - `"enable"` - `"disable"` |
| **stpforward_mode**  string | Configure STP forwarding mode.  Choices:   - `"rpl-all-ext-id"` - `"rpl-bridge-ext-id"` - `"rpl-nothing"` |
| **subst**  string | Enable to always send packets from this interface to a destination MAC address.  Choices:   - `"enable"` - `"disable"` |
| **substitute_dst_mac**  string | Destination MAC address that all packets are sent to from this interface. |
| **sw_algorithm**  string | Frame distribution algorithm for switch.  Choices:   - `"l2"` - `"l3"` - `"eh"` |
| **swc_first_create**  integer | Initial create for switch-controller VLANs. |
| **swc_vlan**  integer | Creation status for switch-controller VLANs. |
| **switch**  string | Contained in switch. |
| **switch_controller_access_vlan**  string | Block FortiSwitch port-to-port traffic.  Choices:   - `"enable"` - `"disable"` |
| **switch_controller_arp_inspection**  string | Enable/disable FortiSwitch ARP inspection.  Choices:   - `"enable"` - `"disable"` |
| **switch_controller_dhcp_snooping**  string | Switch controller DHCP snooping.  Choices:   - `"enable"` - `"disable"` |
| **switch_controller_dhcp_snooping_option82**  string | Switch controller DHCP snooping option82.  Choices:   - `"enable"` - `"disable"` |
| **switch_controller_dhcp_snooping_verify_mac**  string | Switch controller DHCP snooping verify MAC.  Choices:   - `"enable"` - `"disable"` |
| **switch_controller_dynamic**  string | Integrated FortiLink settings for managed FortiSwitch. Source switch-controller.fortilink-settings.name. |
| **switch_controller_feature**  string | Interface”s purpose when assigning traffic (read only).  Choices:   - `"none"` - `"default-vlan"` - `"quarantine"` - `"rspan"` - `"voice"` - `"video"` - `"nac"` - `"nac-segment"` |
| **switch_controller_igmp_snooping**  string | Switch controller IGMP snooping.  Choices:   - `"enable"` - `"disable"` |
| **switch_controller_igmp_snooping_fast_leave**  string | Switch controller IGMP snooping fast-leave.  Choices:   - `"enable"` - `"disable"` |
| **switch_controller_igmp_snooping_proxy**  string | Switch controller IGMP snooping proxy.  Choices:   - `"enable"` - `"disable"` |
| **switch_controller_iot_scanning**  string | Enable/disable managed FortiSwitch IoT scanning.  Choices:   - `"enable"` - `"disable"` |
| **switch_controller_learning_limit**  integer | Limit the number of dynamic MAC addresses on this VLAN (1 - 128, 0 = no limit, default). |
| **switch_controller_mgmt_vlan**  integer | VLAN to use for FortiLink management purposes. |
| **switch_controller_nac**  string | Integrated FortiLink settings for managed FortiSwitch. Source switch-controller.fortilink-settings.name. |
| **switch_controller_netflow_collect**  string | NetFlow collection and processing.  Choices:   - `"disable"` - `"enable"` |
| **switch_controller_rspan_mode**  string | Stop Layer2 MAC learning and interception of BPDUs and other packets on this interface.  Choices:   - `"disable"` - `"enable"` |
| **switch_controller_source_ip**  string | Source IP address used in FortiLink over L3 connections.  Choices:   - `"outbound"` - `"fixed"` |
| **switch_controller_traffic_policy**  string | Switch controller traffic policy for the VLAN. Source switch-controller.traffic-policy.name. |
| **system_id**  string | Define a system ID for the aggregate interface. |
| **system_id_type**  string | Method in which system ID is generated.  Choices:   - `"auto"` - `"user"` |
| **tagging**  list / elements=dictionary | Config object tagging. |
| **category**  string | Tag category. Source system.object-tagging.category. |
| **name**  string | Tagging entry name. |
| **tags**  list / elements=dictionary | Tags. |
| **name**  string | Tag name. Source system.object-tagging.tags.name. |
| **tcp_mss**  integer | TCP maximum segment size. 0 means do not change segment size. |
| **trust_ip6_1**  string | Trusted IPv6 host for dedicated management traffic (::/0 for all hosts). |
| **trust_ip6_2**  string | Trusted IPv6 host for dedicated management traffic (::/0 for all hosts). |
| **trust_ip6_3**  string | Trusted IPv6 host for dedicated management traffic (::/0 for all hosts). |
| **trust_ip_1**  string | Trusted host for dedicated management traffic (0.0.0.0/24 for all hosts). |
| **trust_ip_2**  string | Trusted host for dedicated management traffic (0.0.0.0/24 for all hosts). |
| **trust_ip_3**  string | Trusted host for dedicated management traffic (0.0.0.0/24 for all hosts). |
| **type**  string | Interface type.  Choices:   - `"physical"` - `"vlan"` - `"aggregate"` - `"redundant"` - `"tunnel"` - `"vdom-link"` - `"loopback"` - `"switch"` - `"vap-switch"` - `"wl-mesh"` - `"fext-wan"` - `"vxlan"` - `"geneve"` - `"hdlc"` - `"switch-vlan"` - `"emac-vlan"` - `"ssl"` - `"lan-extension"` - `"hard-switch"` |
| **username**  string | Username of the PPPoE account, provided by your ISP. |
| **vdom**  string | Interface is in this virtual domain (VDOM). Source system.vdom.name. |
| **vindex**  integer | Switch control interface VLAN ID. |
| **vlan_protocol**  string | Ethernet protocol of VLAN.  Choices:   - `"8021q"` - `"8021ad"` |
| **vlanforward**  string | Enable/disable traffic forwarding between VLANs on this interface.  Choices:   - `"enable"` - `"disable"` |
| **vlanid**  integer | VLAN ID (1 - 4094). |
| **vrf**  integer | Virtual Routing Forwarding ID. |
| **vrrp**  list / elements=dictionary | VRRP configuration. |
| **accept_mode**  string | Enable/disable accept mode.  Choices:   - `"enable"` - `"disable"` |
| **adv_interval**  integer | Advertisement interval (1 - 255 seconds). |
| **ignore_default_route**  string | Enable/disable ignoring of default route when checking destination.  Choices:   - `"enable"` - `"disable"` |
| **preempt**  string | Enable/disable preempt mode.  Choices:   - `"enable"` - `"disable"` |
| **priority**  integer | Priority of the virtual router (1 - 255). |
| **proxy_arp**  list / elements=dictionary | VRRP Proxy ARP configuration. |
| **id**  integer | ID. |
| **ip**  string | Set IP addresses of proxy ARP. |
| **start_time**  integer | Startup time (1 - 255 seconds). |
| **status**  string | Enable/disable this VRRP configuration.  Choices:   - `"enable"` - `"disable"` |
| **version**  string | VRRP version.  Choices:   - `"2"` - `"3"` |
| **vrdst**  list / elements=string | Monitor the route to this destination. |
| **vrdst_priority**  integer | Priority of the virtual router when the virtual router destination becomes unreachable (0 - 254). |
| **vrgrp**  integer | VRRP group ID (1 - 65535). |
| **vrid**  integer | Virtual router identifier (1 - 255). |
| **vrip**  string | IP address of the virtual router. |
| **vrrp_virtual_mac**  string | Enable/disable use of virtual MAC for VRRP.  Choices:   - `"enable"` - `"disable"` |
| **wccp**  string | Enable/disable WCCP on this interface. Used for encapsulated WCCP communication between WCCP clients and servers.  Choices:   - `"enable"` - `"disable"` |
| **weight**  integer | Default weight for static routes (if route has no weight configured). |
| **wins_ip**  string | WINS server IP. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_system_interface_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_interface_module.md#id5)

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
  - name: Configure interfaces.
    fortios_system_interface:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      system_interface:
        ac_name: "<your_own_value>"
        aggregate: "<your_own_value>"
        aggregate_type: "physical"
        algorithm: "L2"
        alias: "<your_own_value>"
        allowaccess: "ping"
        ap_discover: "enable"
        arpforward: "enable"
        auth_cert: "<your_own_value> (source vpn.certificate.local.name)"
        auth_portal_addr: "<your_own_value>"
        auth_type: "auto"
        auto_auth_extension_device: "enable"
        bandwidth_measure_time: "0"
        bfd: "global"
        bfd_desired_min_tx: "250"
        bfd_detect_mult: "3"
        bfd_required_min_rx: "250"
        broadcast_forticlient_discovery: "enable"
        broadcast_forward: "enable"
        captive_portal: "2147483647"
        cli_conn_status: "0"
        client_options:
         -
            code: "0"
            id:  "26"
            ip: "<your_own_value>"
            type: "hex"
            value: "<your_own_value>"
        color: "0"
        dedicated_to: "none"
        defaultgw: "enable"
        description: "<your_own_value>"
        detected_peer_mtu: "0"
        detectprotocol: "ping"
        detectserver: "<your_own_value>"
        device_access_list: "<your_own_value>"
        device_identification: "enable"
        device_identification_active_scan: "enable"
        device_netscan: "disable"
        device_user_identification: "enable"
        devindex: "0"
        dhcp_classless_route_addition: "enable"
        dhcp_client_identifier:  "myId_44"
        dhcp_relay_agent_option: "enable"
        dhcp_relay_interface: "<your_own_value> (source system.interface.name)"
        dhcp_relay_interface_select_method: "auto"
        dhcp_relay_ip: "<your_own_value>"
        dhcp_relay_link_selection: "<your_own_value>"
        dhcp_relay_request_all_server: "disable"
        dhcp_relay_service: "disable"
        dhcp_relay_type: "regular"
        dhcp_renew_time: "0"
        dhcp_snooping_server_list:
         -
            name: "default_name_55"
            server_ip: "<your_own_value>"
        disc_retry_timeout: "1"
        disconnect_threshold: "0"
        distance: "5"
        dns_server_override: "enable"
        dns_server_protocol: "cleartext"
        drop_fragment: "enable"
        drop_overlapped_fragment: "enable"
        eap_ca_cert: "<your_own_value> (source certificate.ca.name)"
        eap_identity: "<your_own_value>"
        eap_method: "tls"
        eap_password: "<your_own_value>"
        eap_supplicant: "enable"
        eap_user_cert: "<your_own_value> (source certificate.local.name)"
        egress_cos: "disable"
        egress_queues:
            cos0: "<your_own_value> (source system.isf-queue-profile.name)"
            cos1: "<your_own_value> (source system.isf-queue-profile.name)"
            cos2: "<your_own_value> (source system.isf-queue-profile.name)"
            cos3: "<your_own_value> (source system.isf-queue-profile.name)"
            cos4: "<your_own_value> (source system.isf-queue-profile.name)"
            cos5: "<your_own_value> (source system.isf-queue-profile.name)"
            cos6: "<your_own_value> (source system.isf-queue-profile.name)"
            cos7: "<your_own_value> (source system.isf-queue-profile.name)"
        egress_shaping_profile: "<your_own_value> (source firewall.shaping-profile.profile-name)"
        endpoint_compliance: "enable"
        estimated_downstream_bandwidth: "0"
        estimated_upstream_bandwidth: "0"
        explicit_ftp_proxy: "enable"
        explicit_web_proxy: "enable"
        external: "enable"
        fail_action_on_extender: "soft-restart"
        fail_alert_interfaces:
         -
            name: "default_name_89 (source system.interface.name)"
        fail_alert_method: "link-failed-signal"
        fail_detect: "enable"
        fail_detect_option: "detectserver"
        fortiheartbeat: "enable"
        fortilink: "enable"
        fortilink_backup_link: "0"
        fortilink_neighbor_detect: "lldp"
        fortilink_split_interface: "enable"
        fortilink_stacking: "enable"
        forward_domain: "0"
        gi_gk: "enable"
        gwdetect: "enable"
        ha_priority: "1"
        icmp_accept_redirect: "enable"
        icmp_send_redirect: "enable"
        ident_accept: "enable"
        idle_timeout: "0"
        ike_saml_server: "<your_own_value> (source user.saml.name)"
        inbandwidth: "0"
        ingress_cos: "disable"
        ingress_shaping_profile: "<your_own_value> (source firewall.shaping-profile.profile-name)"
        ingress_spillover_threshold: "0"
        interface: "<your_own_value> (source system.interface.name)"
        internal: "0"
        ip: "<your_own_value>"
        ip_managed_by_fortiipam: "enable"
        ipmac: "enable"
        ips_sniffer_mode: "enable"
        ipunnumbered: "<your_own_value>"
        ipv6:
            autoconf: "enable"
            cli_conn6_status: "0"
            dhcp6_client_options: "rapid"
            dhcp6_iapd_list:
             -
                iaid: "0"
                prefix_hint: "<your_own_value>"
                prefix_hint_plt: "604800"
                prefix_hint_vlt: "2592000"
            dhcp6_information_request: "enable"
            dhcp6_prefix_delegation: "enable"
            dhcp6_prefix_hint: "<your_own_value>"
            dhcp6_prefix_hint_plt: "604800"
            dhcp6_prefix_hint_vlt: "2592000"
            dhcp6_relay_ip: "<your_own_value>"
            dhcp6_relay_service: "disable"
            dhcp6_relay_type: "regular"
            icmp6_send_redirect: "enable"
            interface_identifier:  "myId_137"
            ip6_address: "<your_own_value>"
            ip6_allowaccess: "ping"
            ip6_default_life: "1800"
            ip6_delegated_prefix_iaid: "0"
            ip6_delegated_prefix_list:
             -
                autonomous_flag: "enable"
                delegated_prefix_iaid: "0"
                onlink_flag: "enable"
                prefix_id: "0"
                rdnss: "<your_own_value>"
                rdnss_service: "delegated"
                subnet: "<your_own_value>"
                upstream_interface: "<your_own_value> (source system.interface.name)"
            ip6_dns_server_override: "enable"
            ip6_extra_addr:
             -
                prefix: "<your_own_value>"
            ip6_hop_limit: "0"
            ip6_link_mtu: "0"
            ip6_manage_flag: "enable"
            ip6_max_interval: "600"
            ip6_min_interval: "198"
            ip6_mode: "static"
            ip6_other_flag: "enable"
            ip6_prefix_list:
             -
                autonomous_flag: "enable"
                dnssl:
                 -
                    domain: "<your_own_value>"
                onlink_flag: "enable"
                preferred_life_time: "604800"
                prefix: "<your_own_value>"
                rdnss: "<your_own_value>"
                valid_life_time: "2592000"
            ip6_prefix_mode: "dhcp6"
            ip6_reachable_time: "0"
            ip6_retrans_time: "0"
            ip6_send_adv: "enable"
            ip6_subnet: "<your_own_value>"
            ip6_upstream_interface: "<your_own_value> (source system.interface.name)"
            nd_cert: "<your_own_value> (source certificate.local.name)"
            nd_cga_modifier: "<your_own_value>"
            nd_mode: "basic"
            nd_security_level: "0"
            nd_timestamp_delta: "300"
            nd_timestamp_fuzz: "1"
            ra_send_mtu: "enable"
            unique_autoconf_addr: "enable"
            vrip6_link_local: "<your_own_value>"
            vrrp_virtual_mac6: "enable"
            vrrp6:
             -
                accept_mode: "enable"
                adv_interval: "1"
                preempt: "enable"
                priority: "100"
                start_time: "3"
                status: "enable"
                vrdst6: "<your_own_value>"
                vrgrp: "0"
                vrid: "0"
                vrip6: "<your_own_value>"
        l2forward: "enable"
        lacp_ha_secondary: "enable"
        lacp_ha_slave: "enable"
        lacp_mode: "static"
        lacp_speed: "slow"
        lcp_echo_interval: "5"
        lcp_max_echo_fails: "3"
        link_up_delay: "50"
        lldp_network_policy: "<your_own_value> (source system.lldp.network-policy.name)"
        lldp_reception: "enable"
        lldp_transmission: "enable"
        macaddr: "<your_own_value>"
        managed_device:
         -
            name: "default_name_210"
        managed_subnetwork_size: "32"
        management_ip: "<your_own_value>"
        measured_downstream_bandwidth: "0"
        measured_upstream_bandwidth: "0"
        mediatype: "cfp2-sr10"
        member:
         -
            interface_name: "<your_own_value> (source system.interface.name)"
        min_links: "1"
        min_links_down: "operational"
        mode: "static"
        monitor_bandwidth: "enable"
        mtu: "1500"
        mtu_override: "enable"
        name: "default_name_224"
        ndiscforward: "enable"
        netbios_forward: "disable"
        netflow_sampler: "disable"
        outbandwidth: "0"
        padt_retry_timeout: "1"
        password: "<your_own_value>"
        ping_serv_status: "0"
        polling_interval: "20"
        pppoe_unnumbered_negotiate: "enable"
        pptp_auth_type: "auto"
        pptp_client: "enable"
        pptp_password: "<your_own_value>"
        pptp_server_ip: "<your_own_value>"
        pptp_timeout: "0"
        pptp_user: "<your_own_value>"
        preserve_session_route: "enable"
        priority: "1"
        priority_override: "enable"
        proxy_captive_portal: "enable"
        reachable_time: "30000"
        redundant_interface: "<your_own_value>"
        remote_ip: "<your_own_value>"
        replacemsg_override_group: "<your_own_value>"
        ring_rx: "0"
        ring_tx: "0"
        role: "lan"
        sample_direction: "tx"
        sample_rate: "2000"
        scan_botnet_connections: "disable"
        secondary_IP: "enable"
        secondaryip:
         -
            allowaccess: "ping"
            detectprotocol: "ping"
            detectserver: "<your_own_value>"
            gwdetect: "enable"
            ha_priority: "1"
            id:  "261"
            ip: "<your_own_value>"
            ping_serv_status: "0"
        security_exempt_list: "<your_own_value>"
        security_external_logout: "<your_own_value>"
        security_external_web: "<your_own_value>"
        security_groups:
         -
            name: "default_name_268 (source user.group.name)"
        security_mac_auth_bypass: "mac-auth-only"
        security_mode: "none"
        security_redirect_url: "<your_own_value>"
        service_name: "<your_own_value>"
        sflow_sampler: "enable"
        snmp_index: "0"
        speed: "auto"
        spillover_threshold: "0"
        src_check: "enable"
        status: "up"
        stp: "disable"
        stp_ha_secondary: "disable"
        stp_ha_slave: "disable"
        stpforward: "enable"
        stpforward_mode: "rpl-all-ext-id"
        subst: "enable"
        substitute_dst_mac: "<your_own_value>"
        sw_algorithm: "l2"
        swc_first_create: "0"
        swc_vlan: "0"
        switch: "<your_own_value>"
        switch_controller_access_vlan: "enable"
        switch_controller_arp_inspection: "enable"
        switch_controller_dhcp_snooping: "enable"
        switch_controller_dhcp_snooping_option82: "enable"
        switch_controller_dhcp_snooping_verify_mac: "enable"
        switch_controller_dynamic: "<your_own_value> (source switch-controller.fortilink-settings.name)"
        switch_controller_feature: "none"
        switch_controller_igmp_snooping: "enable"
        switch_controller_igmp_snooping_fast_leave: "enable"
        switch_controller_igmp_snooping_proxy: "enable"
        switch_controller_iot_scanning: "enable"
        switch_controller_learning_limit: "0"
        switch_controller_mgmt_vlan: "4094"
        switch_controller_nac: "<your_own_value> (source switch-controller.fortilink-settings.name)"
        switch_controller_netflow_collect: "disable"
        switch_controller_rspan_mode: "disable"
        switch_controller_source_ip: "outbound"
        switch_controller_traffic_policy: "<your_own_value> (source switch-controller.traffic-policy.name)"
        system_id: "<your_own_value>"
        system_id_type: "auto"
        tagging:
         -
            category: "<your_own_value> (source system.object-tagging.category)"
            name: "default_name_312"
            tags:
             -
                name: "default_name_314 (source system.object-tagging.tags.name)"
        tcp_mss: "0"
        trust_ip_1: "<your_own_value>"
        trust_ip_2: "<your_own_value>"
        trust_ip_3: "<your_own_value>"
        trust_ip6_1: "<your_own_value>"
        trust_ip6_2: "<your_own_value>"
        trust_ip6_3: "<your_own_value>"
        type: "physical"
        username: "<your_own_value>"
        vdom: "<your_own_value> (source system.vdom.name)"
        vindex: "0"
        vlan_protocol: "8021q"
        vlanforward: "enable"
        vlanid: "0"
        vrf: "0"
        vrrp:
         -
            accept_mode: "enable"
            adv_interval: "1"
            ignore_default_route: "enable"
            preempt: "enable"
            priority: "100"
            proxy_arp:
             -
                id:  "337"
                ip: "<your_own_value>"
            start_time: "3"
            status: "enable"
            version: "2"
            vrdst: "<your_own_value>"
            vrdst_priority: "0"
            vrgrp: "0"
            vrid: "0"
            vrip: "<your_own_value>"
        vrrp_virtual_mac: "enable"
        wccp: "enable"
        weight: "0"
        wins_ip: "<your_own_value>"
```

## [Return Values](fortios_system_interface_module.md#id6)

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
