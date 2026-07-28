---
collection: ansible
version: "8"
title: "community.fortios.fmgr_secprof_voip module – VOIP security profiles in FMG"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/fortios/fmgr_secprof_voip_module.html
fetched_at: 2026-07-28T01:44:24+00:00
---
# community.fortios.fmgr_secprof_voip module – VOIP security profiles in FMG

> **Note:**
>
> This module is part of the [community.fortios collection](https://galaxy.ansible.com/ui/repo/published/community/fortios/) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.fortios`.
>
> To use it in a playbook, specify: `community.fortios.fmgr_secprof_voip`.

- [Synopsis](fmgr_secprof_voip_module.md#synopsis)
- [Parameters](fmgr_secprof_voip_module.md#parameters)
- [Notes](fmgr_secprof_voip_module.md#notes)
- [Examples](fmgr_secprof_voip_module.md#examples)
- [Return Values](fmgr_secprof_voip_module.md#return-values)

## [Synopsis](fmgr_secprof_voip_module.md#id1)

- Manage VOIP security profiles in FortiManager via API

## [Parameters](fmgr_secprof_voip_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string | The ADOM the configuration should belong to.  **Default:** `"root"` |
| **comment**  string | Comment. |
| **mode**  string | Sets one of three modes for managing the object.  Allows use of soft-adds instead of overwriting existing values  **Choices:**   - `"add"` ← (default) - `"set"` - `"delete"` - `"update"` |
| **name**  string | Profile name. |
| **sccp**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **sccp_block_mcast**  string | Enable/disable block multicast RTP connections.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sccp_log_call_summary**  string | Enable/disable log summary of SCCP calls.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sccp_log_violations**  string | Enable/disable logging of SCCP violations.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sccp_max_calls**  string | Maximum calls per minute per SCCP client (max 65535). |
| **sccp_status**  string | Enable/disable SCCP.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sccp_verify_header**  string | Enable/disable verify SCCP header content.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **sip_ack_rate**  string | ACK request rate limit (per second, per policy). |
| **sip_block_ack**  string | Enable/disable block ACK requests.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_block_bye**  string | Enable/disable block BYE requests.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_block_cancel**  string | Enable/disable block CANCEL requests.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_block_geo_red_options**  string | Enable/disable block OPTIONS requests, but OPTIONS requests still notify for redundancy.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_block_info**  string | Enable/disable block INFO requests.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_block_invite**  string | Enable/disable block INVITE requests.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_block_long_lines**  string | Enable/disable block requests with headers exceeding max-line-length.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_block_message**  string | Enable/disable block MESSAGE requests.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_block_notify**  string | Enable/disable block NOTIFY requests.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_block_options**  string | Enable/disable block OPTIONS requests and no OPTIONS as notifying message for redundancy either.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_block_prack**  string | Enable/disable block prack requests.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_block_publish**  string | Enable/disable block PUBLISH requests.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_block_refer**  string | Enable/disable block REFER requests.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_block_register**  string | Enable/disable block REGISTER requests.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_block_subscribe**  string | Enable/disable block SUBSCRIBE requests.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_block_unknown**  string | Block unrecognized SIP requests (enabled by default).  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_block_update**  string | Enable/disable block UPDATE requests.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_bye_rate**  string | BYE request rate limit (per second, per policy). |
| **sip_call_keepalive**  string | Continue tracking calls with no RTP for this many minutes. |
| **sip_cancel_rate**  string | CANCEL request rate limit (per second, per policy). |
| **sip_contact_fixup**  string | Fixup contact anyway even if contact’s IP|port doesn’t match session’s IP|port.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_hnt_restrict_source_ip**  string | Enable/disable restrict RTP source IP to be the same as SIP source IP when HNT is enabled.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_hosted_nat_traversal**  string | Hosted NAT Traversal (HNT).  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_info_rate**  string | INFO request rate limit (per second, per policy). |
| **sip_invite_rate**  string | INVITE request rate limit (per second, per policy). |
| **sip_ips_rtp**  string | Enable/disable allow IPS on RTP.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_log_call_summary**  string | Enable/disable logging of SIP call summary.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_log_violations**  string | Enable/disable logging of SIP violations.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_malformed_header_allow**  string | Action for malformed Allow header.  choice | pass | Bypass malformed messages.  choice | discard | Discard malformed messages.  choice | respond | Respond with error code.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **sip_malformed_header_call_id**  string | Action for malformed Call-ID header.  choice | pass | Bypass malformed messages.  choice | discard | Discard malformed messages.  choice | respond | Respond with error code.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **sip_malformed_header_contact**  string | Action for malformed Contact header.  choice | pass | Bypass malformed messages.  choice | discard | Discard malformed messages.  choice | respond | Respond with error code.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **sip_malformed_header_content_length**  string | Action for malformed Content-Length header.  choice | pass | Bypass malformed messages.  choice | discard | Discard malformed messages.  choice | respond | Respond with error code.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **sip_malformed_header_content_type**  string | Action for malformed Content-Type header.  choice | pass | Bypass malformed messages.  choice | discard | Discard malformed messages.  choice | respond | Respond with error code.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **sip_malformed_header_cseq**  string | Action for malformed CSeq header.  choice | pass | Bypass malformed messages.  choice | discard | Discard malformed messages.  choice | respond | Respond with error code.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **sip_malformed_header_expires**  string | Action for malformed Expires header.  choice | pass | Bypass malformed messages.  choice | discard | Discard malformed messages.  choice | respond | Respond with error code.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **sip_malformed_header_from**  string | Action for malformed From header.  choice | pass | Bypass malformed messages.  choice | discard | Discard malformed messages.  choice | respond | Respond with error code.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **sip_malformed_header_max_forwards**  string | Action for malformed Max-Forwards header.  choice | pass | Bypass malformed messages.  choice | discard | Discard malformed messages.  choice | respond | Respond with error code.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **sip_malformed_header_p_asserted_identity**  string | Action for malformed P-Asserted-Identity header.  choice | pass | Bypass malformed messages.  choice | discard | Discard malformed messages.  choice | respond | Respond with error code.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **sip_malformed_header_rack**  string | Action for malformed RAck header.  choice | pass | Bypass malformed messages.  choice | discard | Discard malformed messages.  choice | respond | Respond with error code.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **sip_malformed_header_record_route**  string | Action for malformed Record-Route header.  choice | pass | Bypass malformed messages.  choice | discard | Discard malformed messages.  choice | respond | Respond with error code.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **sip_malformed_header_route**  string | Action for malformed Route header.  choice | pass | Bypass malformed messages.  choice | discard | Discard malformed messages.  choice | respond | Respond with error code.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **sip_malformed_header_rseq**  string | Action for malformed RSeq header.  choice | pass | Bypass malformed messages.  choice | discard | Discard malformed messages.  choice | respond | Respond with error code.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **sip_malformed_header_sdp_a**  string | Action for malformed SDP a line.  choice | pass | Bypass malformed messages.  choice | discard | Discard malformed messages.  choice | respond | Respond with error code.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **sip_malformed_header_sdp_b**  string | Action for malformed SDP b line.  choice | pass | Bypass malformed messages.  choice | discard | Discard malformed messages.  choice | respond | Respond with error code.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **sip_malformed_header_sdp_c**  string | Action for malformed SDP c line.  choice | pass | Bypass malformed messages.  choice | discard | Discard malformed messages.  choice | respond | Respond with error code.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **sip_malformed_header_sdp_i**  string | Action for malformed SDP i line.  choice | pass | Bypass malformed messages.  choice | discard | Discard malformed messages.  choice | respond | Respond with error code.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **sip_malformed_header_sdp_k**  string | Action for malformed SDP k line.  choice | pass | Bypass malformed messages.  choice | discard | Discard malformed messages.  choice | respond | Respond with error code.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **sip_malformed_header_sdp_m**  string | Action for malformed SDP m line.  choice | pass | Bypass malformed messages.  choice | discard | Discard malformed messages.  choice | respond | Respond with error code.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **sip_malformed_header_sdp_o**  string | Action for malformed SDP o line.  choice | pass | Bypass malformed messages.  choice | discard | Discard malformed messages.  choice | respond | Respond with error code.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **sip_malformed_header_sdp_r**  string | Action for malformed SDP r line.  choice | pass | Bypass malformed messages.  choice | discard | Discard malformed messages.  choice | respond | Respond with error code.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **sip_malformed_header_sdp_s**  string | Action for malformed SDP s line.  choice | pass | Bypass malformed messages.  choice | discard | Discard malformed messages.  choice | respond | Respond with error code.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **sip_malformed_header_sdp_t**  string | Action for malformed SDP t line.  choice | pass | Bypass malformed messages.  choice | discard | Discard malformed messages.  choice | respond | Respond with error code.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **sip_malformed_header_sdp_v**  string | Action for malformed SDP v line.  choice | pass | Bypass malformed messages.  choice | discard | Discard malformed messages.  choice | respond | Respond with error code.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **sip_malformed_header_sdp_z**  string | Action for malformed SDP z line.  choice | pass | Bypass malformed messages.  choice | discard | Discard malformed messages.  choice | respond | Respond with error code.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **sip_malformed_header_to**  string | Action for malformed To header.  choice | pass | Bypass malformed messages.  choice | discard | Discard malformed messages.  choice | respond | Respond with error code.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **sip_malformed_header_via**  string | Action for malformed VIA header.  choice | pass | Bypass malformed messages.  choice | discard | Discard malformed messages.  choice | respond | Respond with error code.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **sip_malformed_request_line**  string | Action for malformed request line.  choice | pass | Bypass malformed messages.  choice | discard | Discard malformed messages.  choice | respond | Respond with error code.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **sip_max_body_length**  string | Maximum SIP message body length (0 meaning no limit). |
| **sip_max_dialogs**  string | Maximum number of concurrent calls/dialogs (per policy). |
| **sip_max_idle_dialogs**  string | Maximum number established but idle dialogs to retain (per policy). |
| **sip_max_line_length**  string | Maximum SIP header line length (78-4096). |
| **sip_message_rate**  string | MESSAGE request rate limit (per second, per policy). |
| **sip_nat_trace**  string | Enable/disable preservation of original IP in SDP i line.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_no_sdp_fixup**  string | Enable/disable no SDP fix-up.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_notify_rate**  string | NOTIFY request rate limit (per second, per policy). |
| **sip_open_contact_pinhole**  string | Enable/disable open pinhole for non-REGISTER Contact port.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_open_record_route_pinhole**  string | Enable/disable open pinhole for Record-Route port.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_open_register_pinhole**  string | Enable/disable open pinhole for REGISTER Contact port.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_open_via_pinhole**  string | Enable/disable open pinhole for Via port.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_options_rate**  string | OPTIONS request rate limit (per second, per policy). |
| **sip_prack_rate**  string | PRACK request rate limit (per second, per policy). |
| **sip_preserve_override**  string | Override i line to preserve original IPS (default| append).  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_provisional_invite_expiry_time**  string | Expiry time for provisional INVITE (10 - 3600 sec). |
| **sip_publish_rate**  string | PUBLISH request rate limit (per second, per policy). |
| **sip_refer_rate**  string | REFER request rate limit (per second, per policy). |
| **sip_register_contact_trace**  string | Enable/disable trace original IP/port within the contact header of REGISTER requests.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_register_rate**  string | REGISTER request rate limit (per second, per policy). |
| **sip_rfc2543_branch**  string | Enable/disable support via branch compliant with RFC 2543.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_rtp**  string | Enable/disable create pinholes for RTP traffic to traverse firewall.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_ssl_algorithm**  string | Relative strength of encryption algorithms accepted in negotiation.  choice | high | High encryption. Allow only AES and ChaCha.  choice | medium | Medium encryption. Allow AES, ChaCha, 3DES, and RC4.  choice | low | Low encryption. Allow AES, ChaCha, 3DES, RC4, and DES.  **Choices:**   - `"high"` - `"medium"` - `"low"` |
| **sip_ssl_auth_client**  string | Require a client certificate and authenticate it with the peer/peergrp. |
| **sip_ssl_auth_server**  string | Authenticate the server’s certificate with the peer/peergrp. |
| **sip_ssl_client_certificate**  string | Name of Certificate to offer to server if requested. |
| **sip_ssl_client_renegotiation**  string | Allow/block client renegotiation by server.  choice | allow | Allow a SSL client to renegotiate.  choice | deny | Abort any SSL connection that attempts to renegotiate.  choice | secure | Reject any SSL connection that does not offer a RFC 5746 Secure Renegotiation Indication.  **Choices:**   - `"allow"` - `"deny"` - `"secure"` |
| **sip_ssl_max_version**  string | Highest SSL/TLS version to negotiate.  choice | ssl-3.0 | SSL 3.0.  choice | tls-1.0 | TLS 1.0.  choice | tls-1.1 | TLS 1.1.  choice | tls-1.2 | TLS 1.2.  **Choices:**   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` |
| **sip_ssl_min_version**  string | Lowest SSL/TLS version to negotiate.  choice | ssl-3.0 | SSL 3.0.  choice | tls-1.0 | TLS 1.0.  choice | tls-1.1 | TLS 1.1.  choice | tls-1.2 | TLS 1.2.  **Choices:**   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` |
| **sip_ssl_mode**  string | SSL/TLS mode for encryption &amp; decryption of traffic.  choice | off | No SSL.  choice | full | Client to FortiGate and FortiGate to Server SSL.  **Choices:**   - `"off"` - `"full"` |
| **sip_ssl_pfs**  string | SSL Perfect Forward Secrecy.  choice | require | PFS mandatory.  choice | deny | PFS rejected.  choice | allow | PFS allowed.  **Choices:**   - `"require"` - `"deny"` - `"allow"` |
| **sip_ssl_send_empty_frags**  string | Send empty fragments to avoid attack on CBC IV (SSL 3.0 &amp; TLS 1.0 only).  choice | disable | Do not send empty fragments.  choice | enable | Send empty fragments.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_ssl_server_certificate**  string | Name of Certificate return to the client in every SSL connection. |
| **sip_status**  string | Enable/disable SIP.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_strict_register**  string | Enable/disable only allow the registrar to connect.  choice | disable | Disable status.  choice | enable | Enable status.  **Choices:**   - `"disable"` - `"enable"` |
| **sip_subscribe_rate**  string | SUBSCRIBE request rate limit (per second, per policy). |
| **sip_unknown_header**  string | Action for unknown SIP header.  choice | pass | Bypass malformed messages.  choice | discard | Discard malformed messages.  choice | respond | Respond with error code.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **sip_update_rate**  string | UPDATE request rate limit (per second, per policy). |

## [Notes](fmgr_secprof_voip_module.md#id3)

> **Note:**
>
> - Full Documentation at <https://ftnt-ansible-docs.readthedocs.io/en/latest/>.

## [Examples](fmgr_secprof_voip_module.md#id4)

```yaml+jinja
- name: DELETE Profile
  community.fortios.fmgr_secprof_voip:
    name: "Ansible_VOIP_Profile"
    mode: "delete"

- name: Create FMGR_VOIP_PROFILE
  community.fortios.fmgr_secprof_voip:
    mode: "set"
    adom: "root"
    name: "Ansible_VOIP_Profile"
    comment: "Created by Ansible"
    sccp: {block-mcast: "enable", log-call-summary: "enable", log-violations: "enable", status: "enable"}
```

## [Return Values](fmgr_secprof_voip_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_result**  string | full API response, includes status code and message  **Returned:** always |

### Authors

- Luke Weighall (@lweighall)
- Andrew Welsh (@Ghilli3)
- Jim Huber (@p4r4n0y1ng)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.fortios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.fortios)
