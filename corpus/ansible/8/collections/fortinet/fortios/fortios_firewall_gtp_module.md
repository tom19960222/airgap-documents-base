---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_firewall_gtp module – Configure GTP in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_firewall_gtp_module.html
fetched_at: 2026-07-28T02:24:26+00:00
---
# fortinet.fortios.fortios_firewall_gtp module – Configure GTP in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_firewall_gtp_module.md#ansible-collections-fortinet-fortios-fortios-firewall-gtp-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_firewall_gtp`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_firewall_gtp_module.md#synopsis)
- [Requirements](fortios_firewall_gtp_module.md#requirements)
- [Parameters](fortios_firewall_gtp_module.md#parameters)
- [Notes](fortios_firewall_gtp_module.md#notes)
- [Examples](fortios_firewall_gtp_module.md#examples)
- [Return Values](fortios_firewall_gtp_module.md#return-values)

## [Synopsis](fortios_firewall_gtp_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify firewall feature and gtp category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_firewall_gtp_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_firewall_gtp_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_gtp**  dictionary | Configure GTP. |
| **addr_notify**  string | overbilling notify address |
| **apn**  list / elements=dictionary | APN. |
| **action**  string | Action.  **Choices:**   - `"allow"` - `"deny"` |
| **apnmember**  list / elements=dictionary | APN member. |
| **name**  string / required | APN name. Source gtp.apn.name gtp.apngrp.name. |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **selection_mode**  list / elements=string | APN selection mode.  **Choices:**   - `"ms"` - `"net"` - `"vrf"` |
| **apn_filter**  string | apn filter  **Choices:**   - `"enable"` - `"disable"` |
| **authorized_ggsns**  string | Authorized GGSN/PGW group. Source firewall.address.name firewall.addrgrp.name. |
| **authorized_ggsns6**  string | Authorized GGSN/PGW IPv6 group. Source firewall.address6.name firewall.addrgrp6.name. |
| **authorized_sgsns**  string | Authorized SGSN/SGW group. Source firewall.address.name firewall.addrgrp.name. |
| **authorized_sgsns6**  string | Authorized SGSN/SGW IPv6 group. Source firewall.address6.name firewall.addrgrp6.name. |
| **comment**  string | Comment. |
| **context_id**  integer | Overbilling context. |
| **control_plane_message_rate_limit**  integer | control plane message rate limit |
| **default_apn_action**  string | default apn action  **Choices:**   - `"allow"` - `"deny"` |
| **default_imsi_action**  string | default imsi action  **Choices:**   - `"allow"` - `"deny"` |
| **default_ip_action**  string | default action for encapsulated IP traffic  **Choices:**   - `"allow"` - `"deny"` |
| **default_noip_action**  string | default action for encapsulated non-IP traffic  **Choices:**   - `"allow"` - `"deny"` |
| **default_policy_action**  string | default advanced policy action  **Choices:**   - `"allow"` - `"deny"` |
| **denied_log**  string | log denied  **Choices:**   - `"enable"` - `"disable"` |
| **echo_request_interval**  integer | echo request interval (in seconds) |
| **extension_log**  string | log in extension format  **Choices:**   - `"enable"` - `"disable"` |
| **forwarded_log**  string | log forwarded  **Choices:**   - `"enable"` - `"disable"` |
| **global_tunnel_limit**  string | Global tunnel limit. Source gtp.tunnel-limit.name. |
| **gtp_in_gtp**  string | gtp in gtp  **Choices:**   - `"allow"` - `"deny"` |
| **gtpu_denied_log**  string | Enable/disable logging of denied GTP-U packets.  **Choices:**   - `"enable"` - `"disable"` |
| **gtpu_forwarded_log**  string | Enable/disable logging of forwarded GTP-U packets.  **Choices:**   - `"enable"` - `"disable"` |
| **gtpu_log_freq**  integer | Logging of frequency of GTP-U packets. |
| **half_close_timeout**  integer | Half-close tunnel timeout (in seconds). |
| **half_open_timeout**  integer | Half-open tunnel timeout (in seconds). |
| **handover_group**  string | Handover SGSN/SGW group. Source firewall.address.name firewall.addrgrp.name. |
| **handover_group6**  string | Handover SGSN/SGW IPv6 group. Source firewall.address6.name firewall.addrgrp6.name. |
| **ie_allow_list_v0v1**  string | IE allow list. Source gtp.ie-allow-list.name. |
| **ie_allow_list_v2**  string | IE allow list. Source gtp.ie-allow-list.name. |
| **ie_remove_policy**  list / elements=dictionary | IE remove policy. |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **remove_ies**  list / elements=string | GTP IEs to be removed.  **Choices:**   - `"apn-restriction"` - `"rat-type"` - `"rai"` - `"uli"` - `"imei"` |
| **sgsn_addr**  string | SGSN address name. Source firewall.address.name firewall.addrgrp.name. |
| **sgsn_addr6**  string | SGSN IPv6 address name. Source firewall.address6.name firewall.addrgrp6.name. |
| **ie_remover**  string | IE removal policy.  **Choices:**   - `"enable"` - `"disable"` |
| **ie_validation**  dictionary | IE validation. |
| **apn_restriction**  string | Validate APN restriction.  **Choices:**   - `"enable"` - `"disable"` |
| **charging_gateway_addr**  string | Validate charging gateway address.  **Choices:**   - `"enable"` - `"disable"` |
| **charging_ID**  string | Validate charging ID.  **Choices:**   - `"enable"` - `"disable"` |
| **end_user_addr**  string | Validate end user address.  **Choices:**   - `"enable"` - `"disable"` |
| **gsn_addr**  string | Validate GSN address.  **Choices:**   - `"enable"` - `"disable"` |
| **imei**  string | Validate IMEI(SV).  **Choices:**   - `"enable"` - `"disable"` |
| **imsi**  string | Validate IMSI.  **Choices:**   - `"enable"` - `"disable"` |
| **mm_context**  string | Validate MM context.  **Choices:**   - `"enable"` - `"disable"` |
| **ms_tzone**  string | Validate MS time zone.  **Choices:**   - `"enable"` - `"disable"` |
| **ms_validated**  string | Validate MS validated.  **Choices:**   - `"enable"` - `"disable"` |
| **msisdn**  string | Validate MSISDN.  **Choices:**   - `"enable"` - `"disable"` |
| **nsapi**  string | Validate NSAPI.  **Choices:**   - `"enable"` - `"disable"` |
| **pdp_context**  string | Validate PDP context.  **Choices:**   - `"enable"` - `"disable"` |
| **qos_profile**  string | Validate Quality of Service(QoS) profile.  **Choices:**   - `"enable"` - `"disable"` |
| **rai**  string | Validate RAI.  **Choices:**   - `"enable"` - `"disable"` |
| **rat_type**  string | Validate RAT type.  **Choices:**   - `"enable"` - `"disable"` |
| **reordering_required**  string | Validate re-ordering required.  **Choices:**   - `"enable"` - `"disable"` |
| **selection_mode**  string | Validate selection mode.  **Choices:**   - `"enable"` - `"disable"` |
| **uli**  string | Validate user location information.  **Choices:**   - `"enable"` - `"disable"` |
| **ie_white_list_v0v1**  string | IE white list. Source gtp.ie-white-list.name. |
| **ie_white_list_v2**  string | IE white list. Source gtp.ie-white-list.name. |
| **imsi**  list / elements=dictionary | IMSI. |
| **action**  string | Action.  **Choices:**   - `"allow"` - `"deny"` |
| **apnmember**  list / elements=dictionary | APN member. |
| **name**  string / required | APN name. Source gtp.apn.name gtp.apngrp.name. |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **mcc_mnc**  string | MCC MNC. |
| **msisdn_prefix**  string | MSISDN prefix. |
| **selection_mode**  list / elements=string | APN selection mode.  **Choices:**   - `"ms"` - `"net"` - `"vrf"` |
| **imsi_filter**  string | imsi filter  **Choices:**   - `"enable"` - `"disable"` |
| **interface_notify**  string | overbilling interface Source system.interface.name. |
| **invalid_reserved_field**  string | Invalid reserved field in GTP header  **Choices:**   - `"allow"` - `"deny"` |
| **invalid_sgsns6_to_log**  string | Invalid SGSN IPv6 group to be logged. Source firewall.address6.name firewall.addrgrp6.name. |
| **invalid_sgsns_to_log**  string | Invalid SGSN group to be logged Source firewall.address.name firewall.addrgrp.name. |
| **ip_filter**  string | IP filter for encapsulted traffic  **Choices:**   - `"enable"` - `"disable"` |
| **ip_policy**  list / elements=dictionary | IP policy. |
| **action**  string | Action.  **Choices:**   - `"allow"` - `"deny"` |
| **dstaddr**  string | Destination address name. Source firewall.address.name firewall.addrgrp.name. |
| **dstaddr6**  string | Destination IPv6 address name. Source firewall.address6.name firewall.addrgrp6.name. |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **srcaddr**  string | Source address name. Source firewall.address.name firewall.addrgrp.name. |
| **srcaddr6**  string | Source IPv6 address name. Source firewall.address6.name firewall.addrgrp6.name. |
| **log_freq**  integer | Logging of frequency of GTP-C packets. |
| **log_gtpu_limit**  integer | the user data log limit (0-512 bytes) |
| **log_imsi_prefix**  string | IMSI prefix for selective logging. |
| **log_msisdn_prefix**  string | the msisdn prefix for selective logging |
| **max_message_length**  integer | max message length |
| **message_filter_v0v1**  string | Message filter. Source gtp.message-filter-v0v1.name. |
| **message_filter_v2**  string | Message filter. Source gtp.message-filter-v2.name. |
| **message_rate_limit**  dictionary | Message rate limiting. |
| **create_aa_pdp_request**  integer | Rate limit for create AA PDP context request (packets per second). |
| **create_aa_pdp_response**  integer | Rate limit for create AA PDP context response (packets per second). |
| **create_mbms_request**  integer | Rate limit for create MBMS context request (packets per second). |
| **create_mbms_response**  integer | Rate limit for create MBMS context response (packets per second). |
| **create_pdp_request**  integer | Rate limit for create PDP context request (packets per second). |
| **create_pdp_response**  integer | Rate limit for create PDP context response (packets per second). |
| **delete_aa_pdp_request**  integer | Rate limit for delete AA PDP context request (packets per second). |
| **delete_aa_pdp_response**  integer | Rate limit for delete AA PDP context response (packets per second). |
| **delete_mbms_request**  integer | Rate limit for delete MBMS context request (packets per second). |
| **delete_mbms_response**  integer | Rate limit for delete MBMS context response (packets per second). |
| **delete_pdp_request**  integer | Rate limit for delete PDP context request (packets per second). |
| **delete_pdp_response**  integer | Rate limit for delete PDP context response (packets per second). |
| **echo_reponse**  integer | Rate limit for echo response (packets per second). |
| **echo_request**  integer | Rate limit for echo requests (packets per second). |
| **error_indication**  integer | Rate limit for error indication (packets per second). |
| **failure_report_request**  integer | Rate limit for failure report request (packets per second). |
| **failure_report_response**  integer | Rate limit for failure report response (packets per second). |
| **fwd_reloc_complete_ack**  integer | Rate limit for forward relocation complete acknowledge (packets per second). |
| **fwd_relocation_complete**  integer | Rate limit for forward relocation complete (packets per second). |
| **fwd_relocation_request**  integer | Rate limit for forward relocation request (packets per second). |
| **fwd_relocation_response**  integer | Rate limit for forward relocation response (packets per second). |
| **fwd_srns_context**  integer | Rate limit for forward SRNS context (packets per second). |
| **fwd_srns_context_ack**  integer | Rate limit for forward SRNS context acknowledge (packets per second). |
| **g_pdu**  integer | Rate limit for G-PDU (packets per second). |
| **identification_request**  integer | Rate limit for identification request (packets per second). |
| **identification_response**  integer | Rate limit for identification response (packets per second). |
| **mbms_de_reg_request**  integer | Rate limit for MBMS de-registration request (packets per second). |
| **mbms_de_reg_response**  integer | Rate limit for MBMS de-registration response (packets per second). |
| **mbms_notify_rej_request**  integer | Rate limit for MBMS notification reject request (packets per second). |
| **mbms_notify_rej_response**  integer | Rate limit for MBMS notification reject response (packets per second). |
| **mbms_notify_request**  integer | Rate limit for MBMS notification request (packets per second). |
| **mbms_notify_response**  integer | Rate limit for MBMS notification response (packets per second). |
| **mbms_reg_request**  integer | Rate limit for MBMS registration request (packets per second). |
| **mbms_reg_response**  integer | Rate limit for MBMS registration response (packets per second). |
| **mbms_ses_start_request**  integer | Rate limit for MBMS session start request (packets per second). |
| **mbms_ses_start_response**  integer | Rate limit for MBMS session start response (packets per second). |
| **mbms_ses_stop_request**  integer | Rate limit for MBMS session stop request (packets per second). |
| **mbms_ses_stop_response**  integer | Rate limit for MBMS session stop response (packets per second). |
| **note_ms_request**  integer | Rate limit for note MS GPRS present request (packets per second). |
| **note_ms_response**  integer | Rate limit for note MS GPRS present response (packets per second). |
| **pdu_notify_rej_request**  integer | Rate limit for PDU notify reject request (packets per second). |
| **pdu_notify_rej_response**  integer | Rate limit for PDU notify reject response (packets per second). |
| **pdu_notify_request**  integer | Rate limit for PDU notify request (packets per second). |
| **pdu_notify_response**  integer | Rate limit for PDU notify response (packets per second). |
| **ran_info**  integer | Rate limit for RAN information relay (packets per second). |
| **relocation_cancel_request**  integer | Rate limit for relocation cancel request (packets per second). |
| **relocation_cancel_response**  integer | Rate limit for relocation cancel response (packets per second). |
| **send_route_request**  integer | Rate limit for send routing information for GPRS request (packets per second). |
| **send_route_response**  integer | Rate limit for send routing information for GPRS response (packets per second). |
| **sgsn_context_ack**  integer | Rate limit for SGSN context acknowledgement (packets per second). |
| **sgsn_context_request**  integer | Rate limit for SGSN context request (packets per second). |
| **sgsn_context_response**  integer | Rate limit for SGSN context response (packets per second). |
| **support_ext_hdr_notify**  integer | Rate limit for support extension headers notification (packets per second). |
| **update_mbms_request**  integer | Rate limit for update MBMS context request (packets per second). |
| **update_mbms_response**  integer | Rate limit for update MBMS context response (packets per second). |
| **update_pdp_request**  integer | Rate limit for update PDP context request (packets per second). |
| **update_pdp_response**  integer | Rate limit for update PDP context response (packets per second). |
| **version_not_support**  integer | Rate limit for version not supported (packets per second). |
| **message_rate_limit_v0**  dictionary | Message rate limiting for GTP version 0. |
| **create_pdp_request**  integer | Rate limit (packets/s) for create PDP context request. |
| **delete_pdp_request**  integer | Rate limit (packets/s) for delete PDP context request. |
| **echo_request**  integer | Rate limit (packets/s) for echo request. |
| **message_rate_limit_v1**  dictionary | Message rate limiting for GTP version 1. |
| **create_pdp_request**  integer | Rate limit (packets/s) for create PDP context request. |
| **delete_pdp_request**  integer | Rate limit (packets/s) for delete PDP context request. |
| **echo_request**  integer | Rate limit (packets/s) for echo request. |
| **message_rate_limit_v2**  dictionary | Message rate limiting for GTP version 2. |
| **create_session_request**  integer | Rate limit (packets/s) for create session request. |
| **delete_session_request**  integer | Rate limit (packets/s) for delete session request. |
| **echo_request**  integer | Rate limit (packets/s) for echo request. |
| **min_message_length**  integer | min message length |
| **miss_must_ie**  string | Missing mandatory information element  **Choices:**   - `"allow"` - `"deny"` |
| **monitor_mode**  string | GTP monitor mode.  **Choices:**   - `"enable"` - `"disable"` - `"vdom"` |
| **name**  string / required | Profile name. |
| **noip_filter**  string | non-IP filter for encapsulted traffic  **Choices:**   - `"enable"` - `"disable"` |
| **noip_policy**  list / elements=dictionary | No IP policy. |
| **action**  string | Action.  **Choices:**   - `"allow"` - `"deny"` |
| **end**  integer | End of protocol range (0 - 255). |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **start**  integer | Start of protocol range (0 - 255). |
| **type**  string | Protocol field type.  **Choices:**   - `"etsi"` - `"ietf"` |
| **out_of_state_ie**  string | Out of state information element.  **Choices:**   - `"allow"` - `"deny"` |
| **out_of_state_message**  string | Out of state GTP message  **Choices:**   - `"allow"` - `"deny"` |
| **per_apn_shaper**  list / elements=dictionary | Per APN shaper. |
| **apn**  string | APN name. Source gtp.apn.name. |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **rate_limit**  integer | Rate limit (packets/s) for create PDP context request. |
| **version**  integer | GTP version number: 0 or 1. |
| **policy**  list / elements=dictionary | Policy. |
| **action**  string | Action.  **Choices:**   - `"allow"` - `"deny"` |
| **apn_sel_mode**  list / elements=string | APN selection mode.  **Choices:**   - `"ms"` - `"net"` - `"vrf"` |
| **apnmember**  list / elements=dictionary | APN member. |
| **name**  string / required | APN name. Source gtp.apn.name gtp.apngrp.name. |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **imei**  string | IMEI pattern. |
| **imsi**  string | IMSI prefix. |
| **imsi_prefix**  string | IMSI prefix. |
| **max_apn_restriction**  string | Maximum APN restriction value.  **Choices:**   - `"all"` - `"public-1"` - `"public-2"` - `"private-1"` - `"private-2"` |
| **messages**  list / elements=string | GTP messages.  **Choices:**   - `"create-req"` - `"create-res"` - `"update-req"` - `"update-res"` |
| **msisdn**  string | MSISDN prefix. |
| **msisdn_prefix**  string | MSISDN prefix. |
| **rai**  string | RAI pattern. |
| **rat_type**  list / elements=string | RAT Type.  **Choices:**   - `"any"` - `"utran"` - `"geran"` - `"wlan"` - `"gan"` - `"hspa"` - `"eutran"` - `"virtual"` - `"nbiot"` |
| **uli**  string | ULI pattern. |
| **policy_filter**  string | Advanced policy filter  **Choices:**   - `"enable"` - `"disable"` |
| **policy_v2**  list / elements=dictionary | Apply allow or deny action to each GTPv2-c packet. |
| **action**  string | Action.  **Choices:**   - `"allow"` - `"deny"` |
| **apn_sel_mode**  list / elements=string | APN selection mode.  **Choices:**   - `"ms"` - `"net"` - `"vrf"` |
| **apnmember**  list / elements=dictionary | APN member. |
| **name**  string / required | APN name. Source gtp.apn.name gtp.apngrp.name. |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **imsi_prefix**  string | IMSI prefix. |
| **max_apn_restriction**  string | Maximum APN restriction value.  **Choices:**   - `"all"` - `"public-1"` - `"public-2"` - `"private-1"` - `"private-2"` |
| **mei**  string | MEI pattern. |
| **messages**  list / elements=string | GTP messages.  **Choices:**   - `"create-ses-req"` - `"create-ses-res"` - `"modify-bearer-req"` - `"modify-bearer-res"` |
| **msisdn_prefix**  string | MSISDN prefix. |
| **rat_type**  list / elements=string | RAT Type.  **Choices:**   - `"any"` - `"utran"` - `"geran"` - `"wlan"` - `"gan"` - `"hspa"` - `"eutran"` - `"virtual"` - `"nbiot"` - `"ltem"` - `"nr"` |
| **uli**  list / elements=string | GTPv2 ULI patterns (in order of CGI SAI RAI TAI ECGI LAI). |
| **port_notify**  integer | overbilling notify port |
| **rat_timeout_profile**  string | RAT timeout profile. Source gtp.rat-timeout-profile.name. |
| **rate_limit_mode**  string | GTP rate limit mode.  **Choices:**   - `"per-profile"` - `"per-stream"` - `"per-apn"` |
| **rate_limited_log**  string | log rate limited  **Choices:**   - `"enable"` - `"disable"` |
| **rate_sampling_interval**  integer | rate sampling interval (1-3600 seconds) |
| **remove_if_echo_expires**  string | remove if echo response expires  **Choices:**   - `"enable"` - `"disable"` |
| **remove_if_recovery_differ**  string | remove upon different Recovery IE  **Choices:**   - `"enable"` - `"disable"` |
| **reserved_ie**  string | reserved information element  **Choices:**   - `"allow"` - `"deny"` |
| **send_delete_when_timeout**  string | send DELETE request to path endpoints when GTPv0/v1 tunnel timeout.  **Choices:**   - `"enable"` - `"disable"` |
| **send_delete_when_timeout_v2**  string | send DELETE request to path endpoints when GTPv2 tunnel timeout.  **Choices:**   - `"enable"` - `"disable"` |
| **spoof_src_addr**  string | Spoofed source address for Mobile Station.  **Choices:**   - `"allow"` - `"deny"` |
| **state_invalid_log**  string | log state invalid  **Choices:**   - `"enable"` - `"disable"` |
| **sub_second_interval**  string | Sub-second interval (0.1, 0.25, or 0.5 sec).  **Choices:**   - `"0.5"` - `"0.25"` - `"0.1"` |
| **sub_second_sampling**  string | Enable/disable sub-second sampling.  **Choices:**   - `"enable"` - `"disable"` |
| **traffic_count_log**  string | log tunnel traffic counter  **Choices:**   - `"enable"` - `"disable"` |
| **tunnel_limit**  integer | tunnel limit |
| **tunnel_limit_log**  string | tunnel limit  **Choices:**   - `"enable"` - `"disable"` |
| **tunnel_timeout**  integer | Established tunnel timeout (in seconds). |
| **unknown_version_action**  string | action for unknown gtp version  **Choices:**   - `"allow"` - `"deny"` |
| **user_plane_message_rate_limit**  integer | user plane message rate limit |
| **warning_threshold**  integer | Warning threshold for rate limiting (0 - 99 percent). |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_firewall_gtp_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_firewall_gtp_module.md#id5)

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
  - name: Configure GTP.
    fortios_firewall_gtp:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_gtp:
        addr_notify: "<your_own_value>"
        apn:
         -
            action: "allow"
            apnmember:
             -
                name: "default_name_7 (source gtp.apn.name gtp.apngrp.name)"
            id:  "8"
            selection_mode: "ms"
        apn_filter: "enable"
        authorized_ggsns: "<your_own_value> (source firewall.address.name firewall.addrgrp.name)"
        authorized_ggsns6: "<your_own_value> (source firewall.address6.name firewall.addrgrp6.name)"
        authorized_sgsns: "<your_own_value> (source firewall.address.name firewall.addrgrp.name)"
        authorized_sgsns6: "<your_own_value> (source firewall.address6.name firewall.addrgrp6.name)"
        comment: "Comment."
        context_id: "696"
        control_plane_message_rate_limit: "0"
        default_apn_action: "allow"
        default_imsi_action: "allow"
        default_ip_action: "allow"
        default_noip_action: "allow"
        default_policy_action: "allow"
        denied_log: "enable"
        echo_request_interval: "0"
        extension_log: "enable"
        forwarded_log: "enable"
        global_tunnel_limit: "<your_own_value> (source gtp.tunnel-limit.name)"
        gtp_in_gtp: "allow"
        gtpu_denied_log: "enable"
        gtpu_forwarded_log: "enable"
        gtpu_log_freq: "0"
        half_close_timeout: "10"
        half_open_timeout: "300"
        handover_group: "<your_own_value> (source firewall.address.name firewall.addrgrp.name)"
        handover_group6: "<your_own_value> (source firewall.address6.name firewall.addrgrp6.name)"
        ie_allow_list_v0v1: "<your_own_value> (source gtp.ie-allow-list.name)"
        ie_allow_list_v2: "<your_own_value> (source gtp.ie-allow-list.name)"
        ie_remove_policy:
         -
            id:  "39"
            remove_ies: "apn-restriction"
            sgsn_addr: "<your_own_value> (source firewall.address.name firewall.addrgrp.name)"
            sgsn_addr6: "<your_own_value> (source firewall.address6.name firewall.addrgrp6.name)"
        ie_remover: "enable"
        ie_validation:
            apn_restriction: "enable"
            charging_gateway_addr: "enable"
            charging_ID: "enable"
            end_user_addr: "enable"
            gsn_addr: "enable"
            imei: "enable"
            imsi: "enable"
            mm_context: "enable"
            ms_tzone: "enable"
            ms_validated: "enable"
            msisdn: "enable"
            nsapi: "enable"
            pdp_context: "enable"
            qos_profile: "enable"
            rai: "enable"
            rat_type: "enable"
            reordering_required: "enable"
            selection_mode: "enable"
            uli: "enable"
        ie_white_list_v0v1: "<your_own_value> (source gtp.ie-white-list.name)"
        ie_white_list_v2: "<your_own_value> (source gtp.ie-white-list.name)"
        imsi:
         -
            action: "allow"
            apnmember:
             -
                name: "default_name_69 (source gtp.apn.name gtp.apngrp.name)"
            id:  "70"
            mcc_mnc: "<your_own_value>"
            msisdn_prefix: "<your_own_value>"
            selection_mode: "ms"
        imsi_filter: "enable"
        interface_notify: "<your_own_value> (source system.interface.name)"
        invalid_reserved_field: "allow"
        invalid_sgsns_to_log: "<your_own_value> (source firewall.address.name firewall.addrgrp.name)"
        invalid_sgsns6_to_log: "<your_own_value> (source firewall.address6.name firewall.addrgrp6.name)"
        ip_filter: "enable"
        ip_policy:
         -
            action: "allow"
            dstaddr: "<your_own_value> (source firewall.address.name firewall.addrgrp.name)"
            dstaddr6: "<your_own_value> (source firewall.address6.name firewall.addrgrp6.name)"
            id:  "84"
            srcaddr: "<your_own_value> (source firewall.address.name firewall.addrgrp.name)"
            srcaddr6: "<your_own_value> (source firewall.address6.name firewall.addrgrp6.name)"
        log_freq: "0"
        log_gtpu_limit: "0"
        log_imsi_prefix: "<your_own_value>"
        log_msisdn_prefix: "<your_own_value>"
        max_message_length: "1452"
        message_filter_v0v1: "<your_own_value> (source gtp.message-filter-v0v1.name)"
        message_filter_v2: "<your_own_value> (source gtp.message-filter-v2.name)"
        message_rate_limit:
            create_aa_pdp_request: "0"
            create_aa_pdp_response: "0"
            create_mbms_request: "0"
            create_mbms_response: "0"
            create_pdp_request: "0"
            create_pdp_response: "0"
            delete_aa_pdp_request: "0"
            delete_aa_pdp_response: "0"
            delete_mbms_request: "0"
            delete_mbms_response: "0"
            delete_pdp_request: "0"
            delete_pdp_response: "0"
            echo_reponse: "0"
            echo_request: "0"
            error_indication: "0"
            failure_report_request: "0"
            failure_report_response: "0"
            fwd_reloc_complete_ack: "0"
            fwd_relocation_complete: "0"
            fwd_relocation_request: "0"
            fwd_relocation_response: "0"
            fwd_srns_context: "0"
            fwd_srns_context_ack: "0"
            g_pdu: "0"
            identification_request: "0"
            identification_response: "0"
            mbms_de_reg_request: "0"
            mbms_de_reg_response: "0"
            mbms_notify_rej_request: "0"
            mbms_notify_rej_response: "0"
            mbms_notify_request: "0"
            mbms_notify_response: "0"
            mbms_reg_request: "0"
            mbms_reg_response: "0"
            mbms_ses_start_request: "0"
            mbms_ses_start_response: "0"
            mbms_ses_stop_request: "0"
            mbms_ses_stop_response: "0"
            note_ms_request: "0"
            note_ms_response: "0"
            pdu_notify_rej_request: "0"
            pdu_notify_rej_response: "0"
            pdu_notify_request: "0"
            pdu_notify_response: "0"
            ran_info: "0"
            relocation_cancel_request: "0"
            relocation_cancel_response: "0"
            send_route_request: "0"
            send_route_response: "0"
            sgsn_context_ack: "0"
            sgsn_context_request: "0"
            sgsn_context_response: "0"
            support_ext_hdr_notify: "0"
            update_mbms_request: "0"
            update_mbms_response: "0"
            update_pdp_request: "0"
            update_pdp_response: "0"
            version_not_support: "0"
        message_rate_limit_v0:
            create_pdp_request: "0"
            delete_pdp_request: "0"
            echo_request: "0"
        message_rate_limit_v1:
            create_pdp_request: "0"
            delete_pdp_request: "0"
            echo_request: "0"
        message_rate_limit_v2:
            create_session_request: "0"
            delete_session_request: "0"
            echo_request: "0"
        min_message_length: "0"
        miss_must_ie: "allow"
        monitor_mode: "enable"
        name: "default_name_168"
        noip_filter: "enable"
        noip_policy:
         -
            action: "allow"
            end: "0"
            id:  "173"
            start: "0"
            type: "etsi"
        out_of_state_ie: "allow"
        out_of_state_message: "allow"
        per_apn_shaper:
         -
            apn: "<your_own_value> (source gtp.apn.name)"
            id:  "180"
            rate_limit: "0"
            version: "1"
        policy:
         -
            action: "allow"
            apn_sel_mode: "ms"
            apnmember:
             -
                name: "default_name_187 (source gtp.apn.name gtp.apngrp.name)"
            id:  "188"
            imei: "<your_own_value>"
            imsi: "<your_own_value>"
            imsi_prefix: "<your_own_value>"
            max_apn_restriction: "all"
            messages: "create-req"
            msisdn: "<your_own_value>"
            msisdn_prefix: "<your_own_value>"
            rai: "<your_own_value>"
            rat_type: "any"
            uli: "<your_own_value>"
        policy_filter: "enable"
        policy_v2:
         -
            action: "allow"
            apn_sel_mode: "ms"
            apnmember:
             -
                name: "default_name_204 (source gtp.apn.name gtp.apngrp.name)"
            id:  "205"
            imsi_prefix: "<your_own_value>"
            max_apn_restriction: "all"
            mei: "<your_own_value>"
            messages: "create-ses-req"
            msisdn_prefix: "<your_own_value>"
            rat_type: "any"
            uli: "<your_own_value>"
        port_notify: "21123"
        rat_timeout_profile: "<your_own_value> (source gtp.rat-timeout-profile.name)"
        rate_limit_mode: "per-profile"
        rate_limited_log: "enable"
        rate_sampling_interval: "1"
        remove_if_echo_expires: "enable"
        remove_if_recovery_differ: "enable"
        reserved_ie: "allow"
        send_delete_when_timeout: "enable"
        send_delete_when_timeout_v2: "enable"
        spoof_src_addr: "allow"
        state_invalid_log: "enable"
        sub_second_interval: "0.5"
        sub_second_sampling: "enable"
        traffic_count_log: "enable"
        tunnel_limit: "0"
        tunnel_limit_log: "enable"
        tunnel_timeout: "86400"
        unknown_version_action: "allow"
        user_plane_message_rate_limit: "0"
        warning_threshold: "0"
```

## [Return Values](fortios_firewall_gtp_module.md#id6)

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
