---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_voip_profile module – Configure VoIP profiles in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_voip_profile_module.html
fetched_at: 2026-07-27T17:46:11+00:00
---
# fortinet.fortios.fortios_voip_profile module – Configure VoIP profiles in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_voip_profile_module.md#ansible-collections-fortinet-fortios-fortios-voip-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_voip_profile`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_voip_profile_module.md#synopsis)
- [Requirements](fortios_voip_profile_module.md#requirements)
- [Parameters](fortios_voip_profile_module.md#parameters)
- [Notes](fortios_voip_profile_module.md#notes)
- [Examples](fortios_voip_profile_module.md#examples)
- [Return Values](fortios_voip_profile_module.md#return-values)

## [Synopsis](fortios_voip_profile_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify voip feature and profile category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_voip_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_voip_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |
| **voip_profile**  dictionary | Configure VoIP profiles. |
| **comment**  string | Comment. |
| **feature_set**  string | Flow or proxy inspection feature set.  Choices:   - `"flow"` - `"proxy"` |
| **msrp**  dictionary | MSRP. |
| **log_violations**  string | Enable/disable logging of MSRP violations.  Choices:   - `"disable"` - `"enable"` |
| **max_msg_size**  integer | Maximum allowable MSRP message size (1-65535). |
| **max_msg_size_action**  string | Action for violation of max-msg-size.  Choices:   - `"pass"` - `"block"` - `"reset"` - `"monitor"` |
| **status**  string | Enable/disable MSRP.  Choices:   - `"disable"` - `"enable"` |
| **name**  string / required | Profile name. |
| **sccp**  dictionary | SCCP. |
| **block_mcast**  string | Enable/disable block multicast RTP connections.  Choices:   - `"disable"` - `"enable"` |
| **log_call_summary**  string | Enable/disable log summary of SCCP calls.  Choices:   - `"disable"` - `"enable"` |
| **log_violations**  string | Enable/disable logging of SCCP violations.  Choices:   - `"disable"` - `"enable"` |
| **max_calls**  integer | Maximum calls per minute per SCCP client (max 65535). |
| **status**  string | Enable/disable SCCP.  Choices:   - `"disable"` - `"enable"` |
| **verify_header**  string | Enable/disable verify SCCP header content.  Choices:   - `"disable"` - `"enable"` |
| **sip**  dictionary | SIP. |
| **ack_rate**  integer | ACK request rate limit (per second, per policy). |
| **ack_rate_track**  string | Track the packet protocol field.  Choices:   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **block_ack**  string | Enable/disable block ACK requests.  Choices:   - `"disable"` - `"enable"` |
| **block_bye**  string | Enable/disable block BYE requests.  Choices:   - `"disable"` - `"enable"` |
| **block_cancel**  string | Enable/disable block CANCEL requests.  Choices:   - `"disable"` - `"enable"` |
| **block_geo_red_options**  string | Enable/disable block OPTIONS requests, but OPTIONS requests still notify for redundancy.  Choices:   - `"disable"` - `"enable"` |
| **block_info**  string | Enable/disable block INFO requests.  Choices:   - `"disable"` - `"enable"` |
| **block_invite**  string | Enable/disable block INVITE requests.  Choices:   - `"disable"` - `"enable"` |
| **block_long_lines**  string | Enable/disable block requests with headers exceeding max-line-length.  Choices:   - `"disable"` - `"enable"` |
| **block_message**  string | Enable/disable block MESSAGE requests.  Choices:   - `"disable"` - `"enable"` |
| **block_notify**  string | Enable/disable block NOTIFY requests.  Choices:   - `"disable"` - `"enable"` |
| **block_options**  string | Enable/disable block OPTIONS requests and no OPTIONS as notifying message for redundancy either.  Choices:   - `"disable"` - `"enable"` |
| **block_prack**  string | Enable/disable block prack requests.  Choices:   - `"disable"` - `"enable"` |
| **block_publish**  string | Enable/disable block PUBLISH requests.  Choices:   - `"disable"` - `"enable"` |
| **block_refer**  string | Enable/disable block REFER requests.  Choices:   - `"disable"` - `"enable"` |
| **block_register**  string | Enable/disable block REGISTER requests.  Choices:   - `"disable"` - `"enable"` |
| **block_subscribe**  string | Enable/disable block SUBSCRIBE requests.  Choices:   - `"disable"` - `"enable"` |
| **block_unknown**  string | Block unrecognized SIP requests (enabled by default).  Choices:   - `"disable"` - `"enable"` |
| **block_update**  string | Enable/disable block UPDATE requests.  Choices:   - `"disable"` - `"enable"` |
| **bye_rate**  integer | BYE request rate limit (per second, per policy). |
| **bye_rate_track**  string | Track the packet protocol field.  Choices:   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **call_keepalive**  integer | Continue tracking calls with no RTP for this many minutes. |
| **cancel_rate**  integer | CANCEL request rate limit (per second, per policy). |
| **cancel_rate_track**  string | Track the packet protocol field.  Choices:   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **contact_fixup**  string | Fixup contact anyway even if contact”s IP:port doesn”t match session”s IP:port.  Choices:   - `"disable"` - `"enable"` |
| **hnt_restrict_source_ip**  string | Enable/disable restrict RTP source IP to be the same as SIP source IP when HNT is enabled.  Choices:   - `"disable"` - `"enable"` |
| **hosted_nat_traversal**  string | Hosted NAT Traversal (HNT).  Choices:   - `"disable"` - `"enable"` |
| **info_rate**  integer | INFO request rate limit (per second, per policy). |
| **info_rate_track**  string | Track the packet protocol field.  Choices:   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **invite_rate**  integer | INVITE request rate limit (per second, per policy). |
| **invite_rate_track**  string | Track the packet protocol field.  Choices:   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **ips_rtp**  string | Enable/disable allow IPS on RTP.  Choices:   - `"disable"` - `"enable"` |
| **log_call_summary**  string | Enable/disable logging of SIP call summary.  Choices:   - `"disable"` - `"enable"` |
| **log_violations**  string | Enable/disable logging of SIP violations.  Choices:   - `"disable"` - `"enable"` |
| **malformed_header_allow**  string | Action for malformed Allow header.  Choices:   - `"discard"` - `"pass"` - `"respond"` |
| **malformed_header_call_id**  string | Action for malformed Call-ID header.  Choices:   - `"discard"` - `"pass"` - `"respond"` |
| **malformed_header_contact**  string | Action for malformed Contact header.  Choices:   - `"discard"` - `"pass"` - `"respond"` |
| **malformed_header_content_length**  string | Action for malformed Content-Length header.  Choices:   - `"discard"` - `"pass"` - `"respond"` |
| **malformed_header_content_type**  string | Action for malformed Content-Type header.  Choices:   - `"discard"` - `"pass"` - `"respond"` |
| **malformed_header_cseq**  string | Action for malformed CSeq header.  Choices:   - `"discard"` - `"pass"` - `"respond"` |
| **malformed_header_expires**  string | Action for malformed Expires header.  Choices:   - `"discard"` - `"pass"` - `"respond"` |
| **malformed_header_from**  string | Action for malformed From header.  Choices:   - `"discard"` - `"pass"` - `"respond"` |
| **malformed_header_max_forwards**  string | Action for malformed Max-Forwards header.  Choices:   - `"discard"` - `"pass"` - `"respond"` |
| **malformed_header_no_proxy_require**  string | Action for malformed SIP messages without Proxy-Require header.  Choices:   - `"discard"` - `"pass"` - `"respond"` |
| **malformed_header_no_require**  string | Action for malformed SIP messages without Require header.  Choices:   - `"discard"` - `"pass"` - `"respond"` |
| **malformed_header_p_asserted_identity**  string | Action for malformed P-Asserted-Identity header.  Choices:   - `"discard"` - `"pass"` - `"respond"` |
| **malformed_header_rack**  string | Action for malformed RAck header.  Choices:   - `"discard"` - `"pass"` - `"respond"` |
| **malformed_header_record_route**  string | Action for malformed Record-Route header.  Choices:   - `"discard"` - `"pass"` - `"respond"` |
| **malformed_header_route**  string | Action for malformed Route header.  Choices:   - `"discard"` - `"pass"` - `"respond"` |
| **malformed_header_rseq**  string | Action for malformed RSeq header.  Choices:   - `"discard"` - `"pass"` - `"respond"` |
| **malformed_header_sdp_a**  string | Action for malformed SDP a line.  Choices:   - `"discard"` - `"pass"` - `"respond"` |
| **malformed_header_sdp_b**  string | Action for malformed SDP b line.  Choices:   - `"discard"` - `"pass"` - `"respond"` |
| **malformed_header_sdp_c**  string | Action for malformed SDP c line.  Choices:   - `"discard"` - `"pass"` - `"respond"` |
| **malformed_header_sdp_i**  string | Action for malformed SDP i line.  Choices:   - `"discard"` - `"pass"` - `"respond"` |
| **malformed_header_sdp_k**  string | Action for malformed SDP k line.  Choices:   - `"discard"` - `"pass"` - `"respond"` |
| **malformed_header_sdp_m**  string | Action for malformed SDP m line.  Choices:   - `"discard"` - `"pass"` - `"respond"` |
| **malformed_header_sdp_o**  string | Action for malformed SDP o line.  Choices:   - `"discard"` - `"pass"` - `"respond"` |
| **malformed_header_sdp_r**  string | Action for malformed SDP r line.  Choices:   - `"discard"` - `"pass"` - `"respond"` |
| **malformed_header_sdp_s**  string | Action for malformed SDP s line.  Choices:   - `"discard"` - `"pass"` - `"respond"` |
| **malformed_header_sdp_t**  string | Action for malformed SDP t line.  Choices:   - `"discard"` - `"pass"` - `"respond"` |
| **malformed_header_sdp_v**  string | Action for malformed SDP v line.  Choices:   - `"discard"` - `"pass"` - `"respond"` |
| **malformed_header_sdp_z**  string | Action for malformed SDP z line.  Choices:   - `"discard"` - `"pass"` - `"respond"` |
| **malformed_header_to**  string | Action for malformed To header.  Choices:   - `"discard"` - `"pass"` - `"respond"` |
| **malformed_header_via**  string | Action for malformed VIA header.  Choices:   - `"discard"` - `"pass"` - `"respond"` |
| **malformed_request_line**  string | Action for malformed request line.  Choices:   - `"discard"` - `"pass"` - `"respond"` |
| **max_body_length**  integer | Maximum SIP message body length (0 meaning no limit). |
| **max_dialogs**  integer | Maximum number of concurrent calls/dialogs (per policy). |
| **max_idle_dialogs**  integer | Maximum number established but idle dialogs to retain (per policy). |
| **max_line_length**  integer | Maximum SIP header line length (78-4096). |
| **message_rate**  integer | MESSAGE request rate limit (per second, per policy). |
| **message_rate_track**  string | Track the packet protocol field.  Choices:   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **nat_port_range**  string | RTP NAT port range. |
| **nat_trace**  string | Enable/disable preservation of original IP in SDP i line.  Choices:   - `"disable"` - `"enable"` |
| **no_sdp_fixup**  string | Enable/disable no SDP fix-up.  Choices:   - `"disable"` - `"enable"` |
| **notify_rate**  integer | NOTIFY request rate limit (per second, per policy). |
| **notify_rate_track**  string | Track the packet protocol field.  Choices:   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **open_contact_pinhole**  string | Enable/disable open pinhole for non-REGISTER Contact port.  Choices:   - `"disable"` - `"enable"` |
| **open_record_route_pinhole**  string | Enable/disable open pinhole for Record-Route port.  Choices:   - `"disable"` - `"enable"` |
| **open_register_pinhole**  string | Enable/disable open pinhole for REGISTER Contact port.  Choices:   - `"disable"` - `"enable"` |
| **open_via_pinhole**  string | Enable/disable open pinhole for Via port.  Choices:   - `"disable"` - `"enable"` |
| **options_rate**  integer | OPTIONS request rate limit (per second, per policy). |
| **options_rate_track**  string | Track the packet protocol field.  Choices:   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **prack_rate**  integer | PRACK request rate limit (per second, per policy). |
| **prack_rate_track**  string | Track the packet protocol field.  Choices:   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **preserve_override**  string | Override i line to preserve original IPS .  Choices:   - `"disable"` - `"enable"` |
| **provisional_invite_expiry_time**  integer | Expiry time (10-3600, in seconds) for provisional INVITE. |
| **publish_rate**  integer | PUBLISH request rate limit (per second, per policy). |
| **publish_rate_track**  string | Track the packet protocol field.  Choices:   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **refer_rate**  integer | REFER request rate limit (per second, per policy). |
| **refer_rate_track**  string | Track the packet protocol field.  Choices:   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **register_contact_trace**  string | Enable/disable trace original IP/port within the contact header of REGISTER requests.  Choices:   - `"disable"` - `"enable"` |
| **register_rate**  integer | REGISTER request rate limit (per second, per policy). |
| **register_rate_track**  string | Track the packet protocol field.  Choices:   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **rfc2543_branch**  string | Enable/disable support via branch compliant with RFC 2543.  Choices:   - `"disable"` - `"enable"` |
| **rtp**  string | Enable/disable create pinholes for RTP traffic to traverse firewall.  Choices:   - `"disable"` - `"enable"` |
| **ssl_algorithm**  string | Relative strength of encryption algorithms accepted in negotiation.  Choices:   - `"high"` - `"medium"` - `"low"` |
| **ssl_auth_client**  string | Require a client certificate and authenticate it with the peer/peergrp. Source user.peer.name user.peergrp.name. |
| **ssl_auth_server**  string | Authenticate the server”s certificate with the peer/peergrp. Source user.peer.name user.peergrp.name. |
| **ssl_client_certificate**  string | Name of Certificate to offer to server if requested. Source vpn.certificate.local.name. |
| **ssl_client_renegotiation**  string | Allow/block client renegotiation by server.  Choices:   - `"allow"` - `"deny"` - `"secure"` |
| **ssl_max_version**  string | Highest SSL/TLS version to negotiate.  Choices:   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl_min_version**  string | Lowest SSL/TLS version to negotiate.  Choices:   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl_mode**  string | SSL/TLS mode for encryption & decryption of traffic.  Choices:   - `"off"` - `"full"` |
| **ssl_pfs**  string | SSL Perfect Forward Secrecy.  Choices:   - `"require"` - `"deny"` - `"allow"` |
| **ssl_send_empty_frags**  string | Send empty fragments to avoid attack on CBC IV (SSL 3.0 & TLS 1.0 only).  Choices:   - `"enable"` - `"disable"` |
| **ssl_server_certificate**  string | Name of Certificate return to the client in every SSL connection. Source vpn.certificate.local.name. |
| **status**  string | Enable/disable SIP.  Choices:   - `"disable"` - `"enable"` |
| **strict_register**  string | Enable/disable only allow the registrar to connect.  Choices:   - `"disable"` - `"enable"` |
| **subscribe_rate**  integer | SUBSCRIBE request rate limit (per second, per policy). |
| **subscribe_rate_track**  string | Track the packet protocol field.  Choices:   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **unknown_header**  string | Action for unknown SIP header.  Choices:   - `"discard"` - `"pass"` - `"respond"` |
| **update_rate**  integer | UPDATE request rate limit (per second, per policy). |
| **update_rate_track**  string | Track the packet protocol field.  Choices:   - `"none"` - `"src-ip"` - `"dest-ip"` |

## [Notes](fortios_voip_profile_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_voip_profile_module.md#id5)

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
  - name: Configure VoIP profiles.
    fortios_voip_profile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      voip_profile:
        comment: "Comment."
        feature_set: "flow"
        msrp:
            log_violations: "disable"
            max_msg_size: "0"
            max_msg_size_action: "pass"
            status: "disable"
        name: "default_name_10"
        sccp:
            block_mcast: "disable"
            log_call_summary: "disable"
            log_violations: "disable"
            max_calls: "0"
            status: "disable"
            verify_header: "disable"
        sip:
            ack_rate: "0"
            ack_rate_track: "none"
            block_ack: "disable"
            block_bye: "disable"
            block_cancel: "disable"
            block_geo_red_options: "disable"
            block_info: "disable"
            block_invite: "disable"
            block_long_lines: "disable"
            block_message: "disable"
            block_notify: "disable"
            block_options: "disable"
            block_prack: "disable"
            block_publish: "disable"
            block_refer: "disable"
            block_register: "disable"
            block_subscribe: "disable"
            block_unknown: "disable"
            block_update: "disable"
            bye_rate: "0"
            bye_rate_track: "none"
            call_keepalive: "0"
            cancel_rate: "0"
            cancel_rate_track: "none"
            contact_fixup: "disable"
            hnt_restrict_source_ip: "disable"
            hosted_nat_traversal: "disable"
            info_rate: "0"
            info_rate_track: "none"
            invite_rate: "0"
            invite_rate_track: "none"
            ips_rtp: "disable"
            log_call_summary: "disable"
            log_violations: "disable"
            malformed_header_allow: "discard"
            malformed_header_call_id: "discard"
            malformed_header_contact: "discard"
            malformed_header_content_length: "discard"
            malformed_header_content_type: "discard"
            malformed_header_cseq: "discard"
            malformed_header_expires: "discard"
            malformed_header_from: "discard"
            malformed_header_max_forwards: "discard"
            malformed_header_no_proxy_require: "discard"
            malformed_header_no_require: "discard"
            malformed_header_p_asserted_identity: "discard"
            malformed_header_rack: "discard"
            malformed_header_record_route: "discard"
            malformed_header_route: "discard"
            malformed_header_rseq: "discard"
            malformed_header_sdp_a: "discard"
            malformed_header_sdp_b: "discard"
            malformed_header_sdp_c: "discard"
            malformed_header_sdp_i: "discard"
            malformed_header_sdp_k: "discard"
            malformed_header_sdp_m: "discard"
            malformed_header_sdp_o: "discard"
            malformed_header_sdp_r: "discard"
            malformed_header_sdp_s: "discard"
            malformed_header_sdp_t: "discard"
            malformed_header_sdp_v: "discard"
            malformed_header_sdp_z: "discard"
            malformed_header_to: "discard"
            malformed_header_via: "discard"
            malformed_request_line: "discard"
            max_body_length: "0"
            max_dialogs: "0"
            max_idle_dialogs: "0"
            max_line_length: "998"
            message_rate: "0"
            message_rate_track: "none"
            nat_port_range: "<your_own_value>"
            nat_trace: "disable"
            no_sdp_fixup: "disable"
            notify_rate: "0"
            notify_rate_track: "none"
            open_contact_pinhole: "disable"
            open_record_route_pinhole: "disable"
            open_register_pinhole: "disable"
            open_via_pinhole: "disable"
            options_rate: "0"
            options_rate_track: "none"
            prack_rate: "0"
            prack_rate_track: "none"
            preserve_override: "disable"
            provisional_invite_expiry_time: "210"
            publish_rate: "0"
            publish_rate_track: "none"
            refer_rate: "0"
            refer_rate_track: "none"
            register_contact_trace: "disable"
            register_rate: "0"
            register_rate_track: "none"
            rfc2543_branch: "disable"
            rtp: "disable"
            ssl_algorithm: "high"
            ssl_auth_client: "<your_own_value> (source user.peer.name user.peergrp.name)"
            ssl_auth_server: "<your_own_value> (source user.peer.name user.peergrp.name)"
            ssl_client_certificate: "<your_own_value> (source vpn.certificate.local.name)"
            ssl_client_renegotiation: "allow"
            ssl_max_version: "ssl-3.0"
            ssl_min_version: "ssl-3.0"
            ssl_mode: "off"
            ssl_pfs: "require"
            ssl_send_empty_frags: "enable"
            ssl_server_certificate: "<your_own_value> (source vpn.certificate.local.name)"
            status: "disable"
            strict_register: "disable"
            subscribe_rate: "0"
            subscribe_rate_track: "none"
            unknown_header: "discard"
            update_rate: "0"
            update_rate_track: "none"
```

## [Return Values](fortios_voip_profile_module.md#id6)

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
