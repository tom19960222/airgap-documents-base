---
collection: ansible
version: "6"
title: "community.fortios.fmgr_fwpol_ipv4 module – Allows the add/delete of Firewall Policies on Packages in FortiManager."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/fortios/fmgr_fwpol_ipv4_module.html
fetched_at: 2026-07-27T17:07:43+00:00
---
# community.fortios.fmgr_fwpol_ipv4 module – Allows the add/delete of Firewall Policies on Packages in FortiManager.

> **Note:**
>
> This module is part of the [community.fortios collection](https://galaxy.ansible.com/community/fortios) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.fortios`.
>
> To use it in a playbook, specify: `community.fortios.fmgr_fwpol_ipv4`.

- [Synopsis](fmgr_fwpol_ipv4_module.md#synopsis)
- [Parameters](fmgr_fwpol_ipv4_module.md#parameters)
- [Notes](fmgr_fwpol_ipv4_module.md#notes)
- [Examples](fmgr_fwpol_ipv4_module.md#examples)
- [Return Values](fmgr_fwpol_ipv4_module.md#return-values)

## [Synopsis](fmgr_fwpol_ipv4_module.md#id1)

- Allows the add/delete of Firewall Policies on Packages in FortiManager.

## [Parameters](fmgr_fwpol_ipv4_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **action**  string | Policy action (allow/deny/ipsec).  choice | deny | Blocks sessions that match the firewall policy.  choice | accept | Allows session that match the firewall policy.  choice | ipsec | Firewall policy becomes a policy-based IPsec VPN policy.  Choices:   - `"deny"` - `"accept"` - `"ipsec"` |
| **adom**  string | The ADOM the configuration should belong to.  Default: `"root"` |
| **app_category**  string | Application category ID list. |
| **app_group**  string | Application group names. |
| **application**  string | Application ID list. |
| **application_list**  string | Name of an existing Application list. |
| **auth_cert**  string | HTTPS server certificate for policy authentication. |
| **auth_path**  string | Enable/disable authentication-based routing.  choice | disable | Disable authentication-based routing.  choice | enable | Enable authentication-based routing.  Choices:   - `"disable"` - `"enable"` |
| **auth_redirect_addr**  string | HTTP-to-HTTPS redirect address for firewall authentication. |
| **auto_asic_offload**  string | Enable/disable offloading security profile processing to CP processors.  choice | disable | Disable ASIC offloading.  choice | enable | Enable auto ASIC offloading.  Choices:   - `"disable"` - `"enable"` |
| **av_profile**  string | Name of an existing Antivirus profile. |
| **block_notification**  string | Enable/disable block notification.  choice | disable | Disable setting.  choice | enable | Enable setting.  Choices:   - `"disable"` - `"enable"` |
| **captive_portal_exempt**  string | Enable to exempt some users from the captive portal.  choice | disable | Disable exemption of captive portal.  choice | enable | Enable exemption of captive portal.  Choices:   - `"disable"` - `"enable"` |
| **capture_packet**  string | Enable/disable capture packets.  choice | disable | Disable capture packets.  choice | enable | Enable capture packets.  Choices:   - `"disable"` - `"enable"` |
| **comments**  string | Comment. |
| **custom_log_fields**  string | Custom fields to append to log messages for this policy. |
| **delay_tcp_npu_session**  string | Enable TCP NPU session delay to guarantee packet order of 3-way handshake.  choice | disable | Disable TCP NPU session delay in order to guarantee packet order of 3-way handshake.  choice | enable | Enable TCP NPU session delay in order to guarantee packet order of 3-way handshake.  Choices:   - `"disable"` - `"enable"` |
| **devices**  string | Names of devices or device groups that can be matched by the policy. |
| **diffserv_forward**  string | Enable to change packet’s DiffServ values to the specified diffservcode-forward value.  choice | disable | Disable WAN optimization.  choice | enable | Enable WAN optimization.  Choices:   - `"disable"` - `"enable"` |
| **diffserv_reverse**  string | Enable to change packet’s reverse (reply) DiffServ values to the specified diffservcode-rev value.  choice | disable | Disable setting.  choice | enable | Enable setting.  Choices:   - `"disable"` - `"enable"` |
| **diffservcode_forward**  string | Change packet’s DiffServ to this value. |
| **diffservcode_rev**  string | Change packet’s reverse (reply) DiffServ to this value. |
| **disclaimer**  string | Enable/disable user authentication disclaimer.  choice | disable | Disable user authentication disclaimer.  choice | enable | Enable user authentication disclaimer.  Choices:   - `"disable"` - `"enable"` |
| **dlp_sensor**  string | Name of an existing DLP sensor. |
| **dnsfilter_profile**  string | Name of an existing DNS filter profile. |
| **dscp_match**  string | Enable DSCP check.  choice | disable | Disable DSCP check.  choice | enable | Enable DSCP check.  Choices:   - `"disable"` - `"enable"` |
| **dscp_negate**  string | Enable negated DSCP match.  choice | disable | Disable DSCP negate.  choice | enable | Enable DSCP negate.  Choices:   - `"disable"` - `"enable"` |
| **dscp_value**  string | DSCP value. |
| **dsri**  string | Enable DSRI to ignore HTTP server responses.  choice | disable | Disable DSRI.  choice | enable | Enable DSRI.  Choices:   - `"disable"` - `"enable"` |
| **dstaddr**  string | Destination address and address group names. |
| **dstaddr_negate**  string | When enabled dstaddr specifies what the destination address must NOT be.  choice | disable | Disable destination address negate.  choice | enable | Enable destination address negate.  Choices:   - `"disable"` - `"enable"` |
| **dstintf**  string | Outgoing (egress) interface. |
| **fail_on_missing_dependency**  string | Normal behavior is to “skip” tasks that fail dependency checks, so other tasks can run.  If set to “enabled” if a failed dependency check happeens, Ansible will exit as with failure instead of skip.  Choices:   - `"enable"` - `"disable"` ← (default) |
| **firewall_session_dirty**  string | How to handle sessions if the configuration of this firewall policy changes.  choice | check-all | Flush all current sessions accepted by this policy.  choice | check-new | Continue to allow sessions already accepted by this policy.  Choices:   - `"check-all"` - `"check-new"` |
| **fixedport**  string | Enable to prevent source NAT from changing a session’s source port.  choice | disable | Disable setting.  choice | enable | Enable setting.  Choices:   - `"disable"` - `"enable"` |
| **fsso**  string | Enable/disable Fortinet Single Sign-On.  choice | disable | Disable setting.  choice | enable | Enable setting.  Choices:   - `"disable"` - `"enable"` |
| **fsso_agent_for_ntlm**  string | FSSO agent to use for NTLM authentication. |
| **global_label**  string | Label for the policy that appears when the GUI is in Global View mode. |
| **groups**  string | Names of user groups that can authenticate with this policy. |
| **gtp_profile**  string | GTP profile. |
| **icap_profile**  string | Name of an existing ICAP profile. |
| **identity_based_route**  string | Name of identity-based routing rule. |
| **inbound**  string | Policy-based IPsec VPN | only traffic from the remote network can initiate a VPN.  choice | disable | Disable setting.  choice | enable | Enable setting.  Choices:   - `"disable"` - `"enable"` |
| **internet_service**  string | Enable/disable use of Internet Services for this policy. If enabled, dstaddr and service are not used.  choice | disable | Disable use of Internet Services in policy.  choice | enable | Enable use of Internet Services in policy.  Choices:   - `"disable"` - `"enable"` |
| **internet_service_custom**  string | Custom Internet Service name. |
| **internet_service_id**  string | Internet Service ID. |
| **internet_service_negate**  string | When enabled internet-service specifies what the service must NOT be.  choice | disable | Disable negated Internet Service match.  choice | enable | Enable negated Internet Service match.  Choices:   - `"disable"` - `"enable"` |
| **internet_service_src**  string | Enable/disable use of Internet Services in source for this policy. If enabled, source address is not used.  choice | disable | Disable use of Internet Services source in policy.  choice | enable | Enable use of Internet Services source in policy.  Choices:   - `"disable"` - `"enable"` |
| **internet_service_src_custom**  string | Custom Internet Service source name. |
| **internet_service_src_id**  string | Internet Service source ID. |
| **internet_service_src_negate**  string | When enabled internet-service-src specifies what the service must NOT be.  choice | disable | Disable negated Internet Service source match.  choice | enable | Enable negated Internet Service source match.  Choices:   - `"disable"` - `"enable"` |
| **ippool**  string | Enable to use IP Pools for source NAT.  choice | disable | Disable setting.  choice | enable | Enable setting.  Choices:   - `"disable"` - `"enable"` |
| **ips_sensor**  string | Name of an existing IPS sensor. |
| **label**  string | Label for the policy that appears when the GUI is in Section View mode. |
| **learning_mode**  string | Enable to allow everything, but log all of the meaningful data for security information gathering.  choice | disable | Disable learning mode in firewall policy.  choice | enable | Enable learning mode in firewall policy.  Choices:   - `"disable"` - `"enable"` |
| **logtraffic**  string | Enable or disable logging. Log all sessions or security profile sessions.  choice | disable | Disable all logging for this policy.  choice | all | Log all sessions accepted or denied by this policy.  choice | utm | Log traffic that has a security profile applied to it.  Choices:   - `"disable"` - `"all"` - `"utm"` |
| **logtraffic_start**  string | Record logs when a session starts and ends.  choice | disable | Disable setting.  choice | enable | Enable setting.  Choices:   - `"disable"` - `"enable"` |
| **match_vip**  string | Enable to match packets that have had their destination addresses changed by a VIP.  choice | disable | Do not match DNATed packet.  choice | enable | Match DNATed packet.  Choices:   - `"disable"` - `"enable"` |
| **mms_profile**  string | Name of an existing MMS profile. |
| **mode**  string | Sets one of three modes for managing the object.  Allows use of soft-adds instead of overwriting existing values  Choices:   - `"add"` ← (default) - `"set"` - `"delete"` - `"update"` |
| **name**  string | Policy name. |
| **nat**  string | Enable/disable source NAT.  choice | disable | Disable setting.  choice | enable | Enable setting.  Choices:   - `"disable"` - `"enable"` |
| **natinbound**  string | Policy-based IPsec VPN | apply destination NAT to inbound traffic.  choice | disable | Disable setting.  choice | enable | Enable setting.  Choices:   - `"disable"` - `"enable"` |
| **natip**  string | Policy-based IPsec VPN | source NAT IP address for outgoing traffic. |
| **natoutbound**  string | Policy-based IPsec VPN | apply source NAT to outbound traffic.  choice | disable | Disable setting.  choice | enable | Enable setting.  Choices:   - `"disable"` - `"enable"` |
| **np_acceleration**  string | Enable/disable UTM Network Processor acceleration.  choice | disable | Disable UTM Network Processor acceleration.  choice | enable | Enable UTM Network Processor acceleration.  Choices:   - `"disable"` - `"enable"` |
| **ntlm**  string | Enable/disable NTLM authentication.  choice | disable | Disable setting.  choice | enable | Enable setting.  Choices:   - `"disable"` - `"enable"` |
| **ntlm_enabled_browsers**  string | HTTP-User-Agent value of supported browsers. |
| **ntlm_guest**  string | Enable/disable NTLM guest user access.  choice | disable | Disable setting.  choice | enable | Enable setting.  Choices:   - `"disable"` - `"enable"` |
| **outbound**  string | Policy-based IPsec VPN | only traffic from the internal network can initiate a VPN.  choice | disable | Disable setting.  choice | enable | Enable setting.  Choices:   - `"disable"` - `"enable"` |
| **package_name**  string | The policy package you want to modify  Default: `"default"` |
| **per_ip_shaper**  string | Per-IP traffic shaper. |
| **permit_any_host**  string | Accept UDP packets from any host.  choice | disable | Disable setting.  choice | enable | Enable setting.  Choices:   - `"disable"` - `"enable"` |
| **permit_stun_host**  string | Accept UDP packets from any Session Traversal Utilities for NAT (STUN) host.  choice | disable | Disable setting.  choice | enable | Enable setting.  Choices:   - `"disable"` - `"enable"` |
| **policyid**  string | Policy ID. |
| **poolname**  string | IP Pool names. |
| **profile_group**  string | Name of profile group. |
| **profile_protocol_options**  string | Name of an existing Protocol options profile. |
| **profile_type**  string | Determine whether the firewall policy allows security profile groups or single profiles only.  choice | single | Do not allow security profile groups.  choice | group | Allow security profile groups.  Choices:   - `"single"` - `"group"` |
| **radius_mac_auth_bypass**  string | Enable MAC authentication bypass. The bypassed MAC address must be received from RADIUS server.  choice | disable | Disable MAC authentication bypass.  choice | enable | Enable MAC authentication bypass.  Choices:   - `"disable"` - `"enable"` |
| **redirect_url**  string | URL users are directed to after seeing and accepting the disclaimer or authenticating. |
| **replacemsg_override_group**  string | Override the default replacement message group for this policy. |
| **rsso**  string | Enable/disable RADIUS single sign-on (RSSO).  choice | disable | Disable setting.  choice | enable | Enable setting.  Choices:   - `"disable"` - `"enable"` |
| **rtp_addr**  string | Address names if this is an RTP NAT policy. |
| **rtp_nat**  string | Enable Real Time Protocol (RTP) NAT.  choice | disable | Disable setting.  choice | enable | Enable setting.  Choices:   - `"disable"` - `"enable"` |
| **scan_botnet_connections**  string | Block or monitor connections to Botnet servers or disable Botnet scanning.  choice | disable | Do not scan connections to botnet servers.  choice | block | Block connections to botnet servers.  choice | monitor | Log connections to botnet servers.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **schedule**  string | Schedule name. |
| **schedule_timeout**  string | Enable to force current sessions to end when the schedule object times out.  choice | disable | Disable schedule timeout.  choice | enable | Enable schedule timeout.  Choices:   - `"disable"` - `"enable"` |
| **send_deny_packet**  string | Enable to send a reply when a session is denied or blocked by a firewall policy.  choice | disable | Disable deny-packet sending.  choice | enable | Enable deny-packet sending.  Choices:   - `"disable"` - `"enable"` |
| **service**  string | Service and service group names. |
| **service_negate**  string | When enabled service specifies what the service must NOT be.  choice | disable | Disable negated service match.  choice | enable | Enable negated service match.  Choices:   - `"disable"` - `"enable"` |
| **session_ttl**  string | TTL in seconds for sessions accepted by this policy (0 means use the system default session TTL). |
| **spamfilter_profile**  string | Name of an existing Spam filter profile. |
| **srcaddr**  string | Source address and address group names. |
| **srcaddr_negate**  string | When enabled srcaddr specifies what the source address must NOT be.  choice | disable | Disable source address negate.  choice | enable | Enable source address negate.  Choices:   - `"disable"` - `"enable"` |
| **srcintf**  string | Incoming (ingress) interface. |
| **ssh_filter_profile**  string | Name of an existing SSH filter profile. |
| **ssl_mirror**  string | Enable to copy decrypted SSL traffic to a FortiGate interface (called SSL mirroring).  choice | disable | Disable SSL mirror.  choice | enable | Enable SSL mirror.  Choices:   - `"disable"` - `"enable"` |
| **ssl_mirror_intf**  string | SSL mirror interface name. |
| **ssl_ssh_profile**  string | Name of an existing SSL SSH profile. |
| **status**  string | Enable or disable this policy.  choice | disable | Disable setting.  choice | enable | Enable setting.  Choices:   - `"disable"` - `"enable"` |
| **tcp_mss_receiver**  string | Receiver TCP maximum segment size (MSS). |
| **tcp_mss_sender**  string | Sender TCP maximum segment size (MSS). |
| **tcp_session_without_syn**  string | Enable/disable creation of TCP session without SYN flag.  choice | all | Enable TCP session without SYN.  choice | data-only | Enable TCP session data only.  choice | disable | Disable TCP session without SYN.  Choices:   - `"all"` - `"data-only"` - `"disable"` |
| **timeout_send_rst**  string | Enable/disable sending RST packets when TCP sessions expire.  choice | disable | Disable sending of RST packet upon TCP session expiration.  choice | enable | Enable sending of RST packet upon TCP session expiration.  Choices:   - `"disable"` - `"enable"` |
| **traffic_shaper**  string | Traffic shaper. |
| **traffic_shaper_reverse**  string | Reverse traffic shaper. |
| **url_category**  string | URL category ID list. |
| **users**  string | Names of individual users that can authenticate with this policy. |
| **utm_status**  string | Enable to add one or more security profiles (AV, IPS, etc.) to the firewall policy.  choice | disable | Disable setting.  choice | enable | Enable setting.  Choices:   - `"disable"` - `"enable"` |
| **vlan_cos_fwd**  string | VLAN forward direction user priority | 255 passthrough, 0 lowest, 7 highest. |
| **vlan_cos_rev**  string | VLAN reverse direction user priority | 255 passthrough, 0 lowest, 7 highest.. |
| **vlan_filter**  string | Set VLAN filters. |
| **voip_profile**  string | Name of an existing VoIP profile. |
| **vpn_dst_node**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED. This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide. |
| **vpn_dst_node_host**  string | VPN Destination Node Host. |
| **vpn_dst_node_seq**  string | VPN Destination Node Seq. |
| **vpn_dst_node_subnet**  string | VPN Destination Node Seq. |
| **vpn_src_node**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED. This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide. |
| **vpn_src_node_host**  string | VPN Source Node Host. |
| **vpn_src_node_seq**  string | VPN Source Node Seq. |
| **vpn_src_node_subnet**  string | VPN Source Node. |
| **vpntunnel**  string | Policy-based IPsec VPN | name of the IPsec VPN Phase 1. |
| **waf_profile**  string | Name of an existing Web application firewall profile. |
| **wanopt**  string | Enable/disable WAN optimization.  choice | disable | Disable setting.  choice | enable | Enable setting.  Choices:   - `"disable"` - `"enable"` |
| **wanopt_detection**  string | WAN optimization auto-detection mode.  choice | active | Active WAN optimization peer auto-detection.  choice | passive | Passive WAN optimization peer auto-detection.  choice | off | Turn off WAN optimization peer auto-detection.  Choices:   - `"active"` - `"passive"` - `"off"` |
| **wanopt_passive_opt**  string | WAN optimization passive mode options. This option decides what IP address will be used to connect server.  choice | default | Allow client side WAN opt peer to decide.  choice | transparent | Use address of client to connect to server.  choice | non-transparent | Use local FortiGate address to connect to server.  Choices:   - `"default"` - `"transparent"` - `"non-transparent"` |
| **wanopt_peer**  string | WAN optimization peer. |
| **wanopt_profile**  string | WAN optimization profile. |
| **wccp**  string | Enable/disable forwarding traffic matching this policy to a configured WCCP server.  choice | disable | Disable WCCP setting.  choice | enable | Enable WCCP setting.  Choices:   - `"disable"` - `"enable"` |
| **webcache**  string | Enable/disable web cache.  choice | disable | Disable setting.  choice | enable | Enable setting.  Choices:   - `"disable"` - `"enable"` |
| **webcache_https**  string | Enable/disable web cache for HTTPS.  choice | disable | Disable web cache for HTTPS.  choice | enable | Enable web cache for HTTPS.  Choices:   - `"disable"` - `"enable"` |
| **webfilter_profile**  string | Name of an existing Web filter profile. |
| **wsso**  string | Enable/disable WiFi Single Sign On (WSSO).  choice | disable | Disable setting.  choice | enable | Enable setting.  Choices:   - `"disable"` - `"enable"` |

## [Notes](fmgr_fwpol_ipv4_module.md#id3)

> **Note:**
>
> - Full Documentation at <https://ftnt-ansible-docs.readthedocs.io/en/latest/>.

## [Examples](fmgr_fwpol_ipv4_module.md#id4)

```yaml+jinja
- name: ADD VERY BASIC IPV4 POLICY WITH NO NAT (WIDE OPEN)
  community.fortios.fmgr_fwpol_ipv4:
    mode: "set"
    adom: "ansible"
    package_name: "default"
    name: "Basic_IPv4_Policy"
    comments: "Created by Ansible"
    action: "accept"
    dstaddr: "all"
    srcaddr: "all"
    dstintf: "any"
    srcintf: "any"
    logtraffic: "utm"
    service: "ALL"
    schedule: "always"

- name: ADD VERY BASIC IPV4 POLICY WITH NAT AND MULTIPLE ENTRIES
  community.fortios.fmgr_fwpol_ipv4:
    mode: "set"
    adom: "ansible"
    package_name: "default"
    name: "Basic_IPv4_Policy_2"
    comments: "Created by Ansible"
    action: "accept"
    dstaddr: "google-play"
    srcaddr: "all"
    dstintf: "any"
    srcintf: "any"
    logtraffic: "utm"
    service: "HTTP, HTTPS"
    schedule: "always"
    nat: "enable"
    users: "karen, kevin"

- name: ADD VERY BASIC IPV4 POLICY WITH NAT AND MULTIPLE ENTRIES AND SEC PROFILES
  community.fortios.fmgr_fwpol_ipv4:
    mode: "set"
    adom: "ansible"
    package_name: "default"
    name: "Basic_IPv4_Policy_3"
    comments: "Created by Ansible"
    action: "accept"
    dstaddr: "google-play, autoupdate.opera.com"
    srcaddr: "corp_internal"
    dstintf: "zone_wan1, zone_wan2"
    srcintf: "zone_int1"
    logtraffic: "utm"
    service: "HTTP, HTTPS"
    schedule: "always"
    nat: "enable"
    users: "karen, kevin"
    av_profile: "sniffer-profile"
    ips_sensor: "default"
```

## [Return Values](fmgr_fwpol_ipv4_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_result**  string | full API response, includes status code and message  Returned: always |

### Authors

- Luke Weighall (@lweighall)
- Andrew Welsh (@Ghilli3)
- Jim Huber (@p4r4n0y1ng)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.fortios/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.fortios)
