---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_firewall_gtp module – Configure GTP."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_firewall_gtp_module.html
fetched_at: 2026-07-28T02:11:53+00:00
---
# fortinet.fortimanager.fmgr_firewall_gtp module – Configure GTP.

> **Note:**
>
> This module is part of the [fortinet.fortimanager collection](https://galaxy.ansible.com/ui/repo/published/fortinet/fortimanager/) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortimanager`.
>
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_firewall_gtp`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_firewall_gtp_module.md#synopsis)
- [Parameters](fmgr_firewall_gtp_module.md#parameters)
- [Notes](fmgr_firewall_gtp_module.md#notes)
- [Examples](fmgr_firewall_gtp_module.md#examples)
- [Return Values](fmgr_firewall_gtp_module.md#return-values)

## [Synopsis](fmgr_firewall_gtp_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_firewall_gtp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_gtp**  dictionary | the top level parameters set |
| **addr-notify**  string | overbilling notify address |
| **apn**  list / elements=dictionary | Apn. |
| **action**  string | Action.  **Choices:**   - `"allow"` - `"deny"` |
| **apnmember**  any | (list or str) APN member. |
| **id**  integer | ID. |
| **selection-mode**  list / elements=string | APN selection mode.  **Choices:**   - `"ms"` - `"net"` - `"vrf"` |
| **apn-filter**  string | apn filter  **Choices:**   - `"disable"` - `"enable"` |
| **authorized-ggsns**  string | Authorized GGSN group |
| **authorized-ggsns6**  string | Authorized GGSN/PGW IPv6 group. |
| **authorized-sgsns**  string | Authorized SGSN group |
| **authorized-sgsns6**  string | Authorized SGSN/SGW IPv6 group. |
| **comment**  string | Comment. |
| **context-id**  integer | Overbilling context. |
| **control-plane-message-rate-limit**  integer | control plane message rate limit |
| **default-apn-action**  string | default apn action  **Choices:**   - `"allow"` - `"deny"` |
| **default-imsi-action**  string | default imsi action  **Choices:**   - `"allow"` - `"deny"` |
| **default-ip-action**  string | default action for encapsulated IP traffic  **Choices:**   - `"allow"` - `"deny"` |
| **default-noip-action**  string | default action for encapsulated non-IP traffic  **Choices:**   - `"allow"` - `"deny"` |
| **default-policy-action**  string | default advanced policy action  **Choices:**   - `"allow"` - `"deny"` |
| **denied-log**  string | log denied  **Choices:**   - `"disable"` - `"enable"` |
| **echo-request-interval**  integer | echo request interval |
| **extension-log**  string | log in extension format  **Choices:**   - `"disable"` - `"enable"` |
| **forwarded-log**  string | log forwarded  **Choices:**   - `"disable"` - `"enable"` |
| **global-tunnel-limit**  string | Global tunnel limit. |
| **gtp-in-gtp**  string | gtp in gtp  **Choices:**   - `"allow"` - `"deny"` |
| **gtpu-denied-log**  string | Enable/disable logging of denied GTP-U packets.  **Choices:**   - `"disable"` - `"enable"` |
| **gtpu-forwarded-log**  string | Enable/disable logging of forwarded GTP-U packets.  **Choices:**   - `"disable"` - `"enable"` |
| **gtpu-log-freq**  integer | Logging of frequency of GTP-U packets. |
| **half-close-timeout**  integer | Half-close tunnel timeout |
| **half-open-timeout**  integer | Half-open tunnel timeout |
| **handover-group**  string | Handover SGSN group |
| **handover-group6**  string | Handover SGSN/SGW IPv6 group. |
| **ie-allow-list-v0v1**  string | IE allow list. |
| **ie-allow-list-v2**  string | IE allow list. |
| **ie-remove-policy**  list / elements=dictionary | Ie-Remove-Policy. |
| **id**  integer | ID. |
| **remove-ies**  list / elements=string | GTP IEs to be removed.  **Choices:**   - `"apn-restriction"` - `"rat-type"` - `"rai"` - `"uli"` - `"imei"` |
| **sgsn-addr**  string | SGSN address name. |
| **sgsn-addr6**  string | SGSN IPv6 address name. |
| **ie-remover**  string | IE removal policy.  **Choices:**   - `"disable"` - `"enable"` |
| **ie-validation**  dictionary | no description |
| **apn-restriction**  string | Validate APN restriction.  **Choices:**   - `"disable"` - `"enable"` |
| **charging-gateway-addr**  string | Validate charging gateway address.  **Choices:**   - `"disable"` - `"enable"` |
| **charging-ID**  string | Validate charging ID.  **Choices:**   - `"disable"` - `"enable"` |
| **end-user-addr**  string | Validate end user address.  **Choices:**   - `"disable"` - `"enable"` |
| **gsn-addr**  string | Validate GSN address.  **Choices:**   - `"disable"` - `"enable"` |
| **imei**  string | Validate IMEI  **Choices:**   - `"disable"` - `"enable"` |
| **imsi**  string | Validate IMSI.  **Choices:**   - `"disable"` - `"enable"` |
| **mm-context**  string | Validate MM context.  **Choices:**   - `"disable"` - `"enable"` |
| **ms-tzone**  string | Validate MS time zone.  **Choices:**   - `"disable"` - `"enable"` |
| **ms-validated**  string | Validate MS validated.  **Choices:**   - `"disable"` - `"enable"` |
| **msisdn**  string | Validate MSISDN.  **Choices:**   - `"disable"` - `"enable"` |
| **nsapi**  string | Validate NSAPI.  **Choices:**   - `"disable"` - `"enable"` |
| **pdp-context**  string | Validate PDP context.  **Choices:**   - `"disable"` - `"enable"` |
| **qos-profile**  string | Validate Quality of Service  **Choices:**   - `"disable"` - `"enable"` |
| **rai**  string | Validate RAI.  **Choices:**   - `"disable"` - `"enable"` |
| **rat-type**  string | Validate RAT type.  **Choices:**   - `"disable"` - `"enable"` |
| **reordering-required**  string | Validate re-ordering required.  **Choices:**   - `"disable"` - `"enable"` |
| **selection-mode**  string | Validate selection mode.  **Choices:**   - `"disable"` - `"enable"` |
| **uli**  string | Validate user location information.  **Choices:**   - `"disable"` - `"enable"` |
| **ie-white-list-v0v1**  string | IE white list. |
| **ie-white-list-v2**  string | IE white list. |
| **imsi**  list / elements=dictionary | Imsi. |
| **action**  string | Action.  **Choices:**   - `"allow"` - `"deny"` |
| **apnmember**  any | (list or str) APN member. |
| **id**  integer | ID. |
| **mcc-mnc**  string | MCC MNC. |
| **msisdn-prefix**  string | MSISDN prefix. |
| **selection-mode**  list / elements=string | APN selection mode.  **Choices:**   - `"ms"` - `"net"` - `"vrf"` |
| **imsi-filter**  string | imsi filter  **Choices:**   - `"disable"` - `"enable"` |
| **interface-notify**  string | overbilling interface |
| **invalid-reserved-field**  string | Invalid reserved field in GTP header  **Choices:**   - `"allow"` - `"deny"` |
| **invalid-sgsns-to-log**  string | Invalid SGSN group to be logged |
| **invalid-sgsns6-to-log**  string | Invalid SGSN IPv6 group to be logged. |
| **ip-filter**  string | IP filter for encapsulted traffic  **Choices:**   - `"disable"` - `"enable"` |
| **ip-policy**  list / elements=dictionary | Ip-Policy. |
| **action**  string | Action.  **Choices:**   - `"allow"` - `"deny"` |
| **dstaddr**  string | Destination address name. |
| **dstaddr6**  string | Destination IPv6 address name. |
| **id**  integer | ID. |
| **srcaddr**  string | Source address name. |
| **srcaddr6**  string | Source IPv6 address name. |
| **log-freq**  integer | Logging of frequency of GTP-C packets. |
| **log-gtpu-limit**  integer | the user data log limit |
| **log-imsi-prefix**  string | IMSI prefix for selective logging. |
| **log-msisdn-prefix**  string | the msisdn prefix for selective logging |
| **max-message-length**  integer | max message length |
| **message-filter**  dictionary | no description |
| **create-aa-pdp**  string | Create AA PDP.  **Choices:**   - `"allow"` - `"deny"` |
| **create-mbms**  string | Create MBMS.  **Choices:**   - `"allow"` - `"deny"` |
| **create-pdp**  string | Create PDP.  **Choices:**   - `"allow"` - `"deny"` |
| **data-record**  string | Data record.  **Choices:**   - `"allow"` - `"deny"` |
| **delete-aa-pdp**  string | Delete AA PDP.  **Choices:**   - `"allow"` - `"deny"` |
| **delete-mbms**  string | Delete MBMS.  **Choices:**   - `"allow"` - `"deny"` |
| **delete-pdp**  string | Delete PDP.  **Choices:**   - `"allow"` - `"deny"` |
| **echo**  string | Echo.  **Choices:**   - `"allow"` - `"deny"` |
| **error-indication**  string | Error indication.  **Choices:**   - `"allow"` - `"deny"` |
| **failure-report**  string | Failure report.  **Choices:**   - `"allow"` - `"deny"` |
| **fwd-relocation**  string | Forward relocation.  **Choices:**   - `"allow"` - `"deny"` |
| **fwd-srns-context**  string | Forward SRNS context.  **Choices:**   - `"allow"` - `"deny"` |
| **gtp-pdu**  string | GTP PDU.  **Choices:**   - `"allow"` - `"deny"` |
| **identification**  string | Identification.  **Choices:**   - `"allow"` - `"deny"` |
| **mbms-notification**  string | MBMS notification.  **Choices:**   - `"allow"` - `"deny"` |
| **node-alive**  string | Node alive.  **Choices:**   - `"allow"` - `"deny"` |
| **note-ms-present**  string | Note MS present.  **Choices:**   - `"allow"` - `"deny"` |
| **pdu-notification**  string | PDU notification.  **Choices:**   - `"allow"` - `"deny"` |
| **ran-info**  string | Ran info.  **Choices:**   - `"allow"` - `"deny"` |
| **redirection**  string | Redirection.  **Choices:**   - `"allow"` - `"deny"` |
| **relocation-cancel**  string | Relocation cancel.  **Choices:**   - `"allow"` - `"deny"` |
| **send-route**  string | Send route.  **Choices:**   - `"allow"` - `"deny"` |
| **sgsn-context**  string | SGSN context.  **Choices:**   - `"allow"` - `"deny"` |
| **support-extension**  string | Support extension.  **Choices:**   - `"allow"` - `"deny"` |
| **unknown-message-action**  string | Unknown message action.  **Choices:**   - `"allow"` - `"deny"` |
| **update-mbms**  string | Update MBMS.  **Choices:**   - `"allow"` - `"deny"` |
| **update-pdp**  string | Update PDP.  **Choices:**   - `"allow"` - `"deny"` |
| **version-not-support**  string | Version not supported.  **Choices:**   - `"allow"` - `"deny"` |
| **message-filter-v0v1**  string | Message filter. |
| **message-filter-v2**  string | Message filter. |
| **message-rate-limit**  dictionary | no description |
| **create-aa-pdp-request**  integer | Rate limit for create AA PDP context request |
| **create-aa-pdp-response**  integer | Rate limit for create AA PDP context response |
| **create-mbms-request**  integer | Rate limit for create MBMS context request |
| **create-mbms-response**  integer | Rate limit for create MBMS context response |
| **create-pdp-request**  integer | Rate limit for create PDP context request |
| **create-pdp-response**  integer | Rate limit for create PDP context response |
| **delete-aa-pdp-request**  integer | Rate limit for delete AA PDP context request |
| **delete-aa-pdp-response**  integer | Rate limit for delete AA PDP context response |
| **delete-mbms-request**  integer | Rate limit for delete MBMS context request |
| **delete-mbms-response**  integer | Rate limit for delete MBMS context response |
| **delete-pdp-request**  integer | Rate limit for delete PDP context request |
| **delete-pdp-response**  integer | Rate limit for delete PDP context response |
| **echo-reponse**  integer | Rate limit for echo response |
| **echo-request**  integer | Rate limit for echo requests |
| **error-indication**  integer | Rate limit for error indication |
| **failure-report-request**  integer | Rate limit for failure report request |
| **failure-report-response**  integer | Rate limit for failure report response |
| **fwd-reloc-complete-ack**  integer | Rate limit for forward relocation complete acknowledge |
| **fwd-relocation-complete**  integer | Rate limit for forward relocation complete |
| **fwd-relocation-request**  integer | Rate limit for forward relocation request |
| **fwd-relocation-response**  integer | Rate limit for forward relocation response |
| **fwd-srns-context**  integer | Rate limit for forward SRNS context |
| **fwd-srns-context-ack**  integer | Rate limit for forward SRNS context acknowledge |
| **g-pdu**  integer | Rate limit for G-PDU |
| **identification-request**  integer | Rate limit for identification request |
| **identification-response**  integer | Rate limit for identification response |
| **mbms-de-reg-request**  integer | Rate limit for MBMS de-registration request |
| **mbms-de-reg-response**  integer | Rate limit for MBMS de-registration response |
| **mbms-notify-rej-request**  integer | Rate limit for MBMS notification reject request |
| **mbms-notify-rej-response**  integer | Rate limit for MBMS notification reject response |
| **mbms-notify-request**  integer | Rate limit for MBMS notification request |
| **mbms-notify-response**  integer | Rate limit for MBMS notification response |
| **mbms-reg-request**  integer | Rate limit for MBMS registration request |
| **mbms-reg-response**  integer | Rate limit for MBMS registration response |
| **mbms-ses-start-request**  integer | Rate limit for MBMS session start request |
| **mbms-ses-start-response**  integer | Rate limit for MBMS session start response |
| **mbms-ses-stop-request**  integer | Rate limit for MBMS session stop request |
| **mbms-ses-stop-response**  integer | Rate limit for MBMS session stop response |
| **note-ms-request**  integer | Rate limit for note MS GPRS present request |
| **note-ms-response**  integer | Rate limit for note MS GPRS present response |
| **pdu-notify-rej-request**  integer | Rate limit for PDU notify reject request |
| **pdu-notify-rej-response**  integer | Rate limit for PDU notify reject response |
| **pdu-notify-request**  integer | Rate limit for PDU notify request |
| **pdu-notify-response**  integer | Rate limit for PDU notify response |
| **ran-info**  integer | Rate limit for RAN information relay |
| **relocation-cancel-request**  integer | Rate limit for relocation cancel request |
| **relocation-cancel-response**  integer | Rate limit for relocation cancel response |
| **send-route-request**  integer | Rate limit for send routing information for GPRS request |
| **send-route-response**  integer | Rate limit for send routing information for GPRS response |
| **sgsn-context-ack**  integer | Rate limit for SGSN context acknowledgement |
| **sgsn-context-request**  integer | Rate limit for SGSN context request |
| **sgsn-context-response**  integer | Rate limit for SGSN context response |
| **support-ext-hdr-notify**  integer | Rate limit for support extension headers notification |
| **update-mbms-request**  integer | Rate limit for update MBMS context request |
| **update-mbms-response**  integer | Rate limit for update MBMS context response |
| **update-pdp-request**  integer | Rate limit for update PDP context request |
| **update-pdp-response**  integer | Rate limit for update PDP context response |
| **version-not-support**  integer | Rate limit for version not supported |
| **message-rate-limit-v0**  dictionary | no description |
| **create-pdp-request**  integer | Rate limit |
| **delete-pdp-request**  integer | Rate limit |
| **echo-request**  integer | Rate limit |
| **message-rate-limit-v1**  dictionary | no description |
| **create-pdp-request**  integer | Rate limit |
| **delete-pdp-request**  integer | Rate limit |
| **echo-request**  integer | Rate limit |
| **message-rate-limit-v2**  dictionary | no description |
| **create-session-request**  integer | Rate limit |
| **delete-session-request**  integer | Rate limit |
| **echo-request**  integer | Rate limit |
| **min-message-length**  integer | min message length |
| **miss-must-ie**  string | Missing mandatory information element  **Choices:**   - `"allow"` - `"deny"` |
| **monitor-mode**  string | GTP monitor mode  **Choices:**   - `"disable"` - `"enable"` - `"vdom"` |
| **name**  string / required | Profile name. |
| **noip-filter**  string | non-IP filter for encapsulted traffic  **Choices:**   - `"disable"` - `"enable"` |
| **noip-policy**  list / elements=dictionary | Noip-Policy. |
| **action**  string | Action.  **Choices:**   - `"allow"` - `"deny"` |
| **end**  integer | End of protocol range |
| **id**  integer | ID. |
| **start**  integer | Start of protocol range |
| **type**  string | Protocol field type.  **Choices:**   - `"etsi"` - `"ietf"` |
| **out-of-state-ie**  string | Out of state information element.  **Choices:**   - `"allow"` - `"deny"` |
| **out-of-state-message**  string | Out of state GTP message  **Choices:**   - `"allow"` - `"deny"` |
| **per-apn-shaper**  list / elements=dictionary | Per-Apn-Shaper. |
| **apn**  string | APN name. |
| **id**  integer | ID. |
| **rate-limit**  integer | Rate limit |
| **version**  integer | GTP version number |
| **policy**  list / elements=dictionary | Policy. |
| **action**  string | Action.  **Choices:**   - `"allow"` - `"deny"` |
| **apn**  string | APN subfix. |
| **apn-sel-mode**  list / elements=string | APN selection mode.  **Choices:**   - `"ms"` - `"net"` - `"vrf"` |
| **apnmember**  any | (list or str) APN member. |
| **id**  integer | ID. |
| **imei**  string | IMEI |
| **imsi**  string | IMSI prefix. |
| **imsi-prefix**  string | IMSI prefix. |
| **max-apn-restriction**  string | Maximum APN restriction value.  **Choices:**   - `"all"` - `"public-1"` - `"public-2"` - `"private-1"` - `"private-2"` |
| **messages**  list / elements=string | GTP messages.  **Choices:**   - `"create-req"` - `"create-res"` - `"update-req"` - `"update-res"` |
| **msisdn**  string | MSISDN prefix. |
| **msisdn-prefix**  string | MSISDN prefix. |
| **rai**  string | RAI pattern. |
| **rat-type**  list / elements=string | RAT Type.  **Choices:**   - `"any"` - `"utran"` - `"geran"` - `"wlan"` - `"gan"` - `"hspa"` - `"eutran"` - `"virtual"` - `"nbiot"` |
| **uli**  string | ULI pattern. |
| **policy-filter**  string | Advanced policy filter  **Choices:**   - `"disable"` - `"enable"` |
| **policy-v2**  list / elements=dictionary | Policy-V2. |
| **action**  string | Action.  **Choices:**   - `"deny"` - `"allow"` |
| **apn-sel-mode**  list / elements=string | APN selection mode.  **Choices:**   - `"ms"` - `"net"` - `"vrf"` |
| **apnmember**  any | (list or str) APN member. |
| **id**  integer | ID. |
| **imsi-prefix**  string | IMSI prefix. |
| **max-apn-restriction**  string | Maximum APN restriction value.  **Choices:**   - `"all"` - `"public-1"` - `"public-2"` - `"private-1"` - `"private-2"` |
| **mei**  string | MEI pattern. |
| **messages**  list / elements=string | GTP messages.  **Choices:**   - `"create-ses-req"` - `"create-ses-res"` - `"modify-bearer-req"` - `"modify-bearer-res"` |
| **msisdn-prefix**  string | MSISDN prefix. |
| **rat-type**  list / elements=string | RAT Type.  **Choices:**   - `"any"` - `"utran"` - `"geran"` - `"wlan"` - `"gan"` - `"hspa"` - `"eutran"` - `"virtual"` - `"nbiot"` - `"ltem"` - `"nr"` |
| **uli**  any | (list) GTPv2 ULI patterns |
| **port-notify**  integer | overbilling notify port |
| **rat-timeout-profile**  string | RAT timeout profile. |
| **rate-limit-mode**  string | GTP rate limit mode.  **Choices:**   - `"per-profile"` - `"per-stream"` - `"per-apn"` |
| **rate-limited-log**  string | log rate limited  **Choices:**   - `"disable"` - `"enable"` |
| **rate-sampling-interval**  integer | rate sampling interval |
| **remove-if-echo-expires**  string | remove if echo response expires  **Choices:**   - `"disable"` - `"enable"` |
| **remove-if-recovery-differ**  string | remove upon different Recovery IE  **Choices:**   - `"disable"` - `"enable"` |
| **reserved-ie**  string | reserved information element  **Choices:**   - `"allow"` - `"deny"` |
| **send-delete-when-timeout**  string | send DELETE request to path endpoints when GTPv0/v1 tunnel timeout.  **Choices:**   - `"disable"` - `"enable"` |
| **send-delete-when-timeout-v2**  string | send DELETE request to path endpoints when GTPv2 tunnel timeout.  **Choices:**   - `"disable"` - `"enable"` |
| **spoof-src-addr**  string | Spoofed source address for Mobile Station.  **Choices:**   - `"allow"` - `"deny"` |
| **state-invalid-log**  string | log state invalid  **Choices:**   - `"disable"` - `"enable"` |
| **sub-second-interval**  string | Sub-second interval  **Choices:**   - `"0.1"` - `"0.25"` - `"0.5"` |
| **sub-second-sampling**  string | Enable/disable sub-second sampling.  **Choices:**   - `"disable"` - `"enable"` |
| **traffic-count-log**  string | log tunnel traffic counter  **Choices:**   - `"disable"` - `"enable"` |
| **tunnel-limit**  integer | tunnel limit |
| **tunnel-limit-log**  string | tunnel limit  **Choices:**   - `"disable"` - `"enable"` |
| **tunnel-timeout**  integer | Established tunnel timeout |
| **unknown-version-action**  string | action for unknown gtp version  **Choices:**   - `"allow"` - `"deny"` |
| **user-plane-message-rate-limit**  integer | user plane message rate limit |
| **warning-threshold**  integer | Warning threshold for rate limiting |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_firewall_gtp_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_firewall_gtp_module.md#id4)

```yaml+jinja
- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: Configure GTP.
     fmgr_firewall_gtp:
        bypass_validation: False
        adom: FortiCarrier # This is FOC-only object, need a FortiCarrier adom
        state: present
        firewall_gtp:
           monitor-mode: disable #<value in [disable, enable, vdom]>
           name: 'ansible-test'

- name: gathering fortimanager facts
  hosts: fortimanager00
  gather_facts: no
  connection: httpapi
  collections:
    - fortinet.fortimanager
  vars:
    ansible_httpapi_use_ssl: True
    ansible_httpapi_validate_certs: False
    ansible_httpapi_port: 443
  tasks:
   - name: retrieve all the GTPs
     fmgr_fact:
       facts:
           selector: 'firewall_gtp'
           params:
               adom: 'FortiCarrier' # This is FOC-only object, need a FortiCarrier adom
               gtp: 'your_value'
```

## [Return Values](fmgr_firewall_gtp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meta**  dictionary | The result of the request.  **Returned:** always |
| **request_url**  string | The full url requested.  **Returned:** always  **Sample:** `"/sys/login/user"` |
| **response_code**  integer | The status of api request.  **Returned:** always  **Sample:** `0` |
| **response_data**  list / elements=string | The api response.  **Returned:** always |
| **response_message**  string | The descriptive message of the api response.  **Returned:** always  **Sample:** `"OK."` |
| **system_information**  dictionary | The information of the target system.  **Returned:** always |
| **rc**  integer | The status the request.  **Returned:** always  **Sample:** `0` |
| **version_check_warning**  list / elements=string | Warning if the parameters used in the playbook are not supported by the current FortiManager version.  **Returned:** complex |

### Authors

- Xinwei Du (@dux-fortinet)
- Xing Li (@lix-fortinet)
- Jie Xue (@JieX19)
- Link Zheng (@chillancezen)
- Frank Shen (@fshen01)
- Hongbin Lu (@fgtdev-hblu)

### Collection links

- [Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/issues)
- [Homepage](https://fortinet.com)
- [Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection)
