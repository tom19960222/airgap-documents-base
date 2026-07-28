---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_voip_profile_sip module – SIP."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_voip_profile_sip_module.html
fetched_at: 2026-07-28T02:21:36+00:00
---
# fortinet.fortimanager.fmgr_voip_profile_sip module – SIP.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_voip_profile_sip`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_voip_profile_sip_module.md#synopsis)
- [Parameters](fmgr_voip_profile_sip_module.md#parameters)
- [Notes](fmgr_voip_profile_sip_module.md#notes)
- [Examples](fmgr_voip_profile_sip_module.md#examples)
- [Return Values](fmgr_voip_profile_sip_module.md#return-values)

## [Synopsis](fmgr_voip_profile_sip_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_voip_profile_sip_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **profile**  string / required | the parameter (profile) in requested url |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **voip_profile_sip**  dictionary | the top level parameters set |
| **ack-rate**  integer | ACK request rate limit |
| **ack-rate-track**  string | Track the packet protocol field.  **Choices:**   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **block-ack**  string | Enable/disable block ACK requests.  **Choices:**   - `"disable"` - `"enable"` |
| **block-bye**  string | Enable/disable block BYE requests.  **Choices:**   - `"disable"` - `"enable"` |
| **block-cancel**  string | Enable/disable block CANCEL requests.  **Choices:**   - `"disable"` - `"enable"` |
| **block-geo-red-options**  string | Enable/disable block OPTIONS requests, but OPTIONS requests still notify for redundancy.  **Choices:**   - `"disable"` - `"enable"` |
| **block-info**  string | Enable/disable block INFO requests.  **Choices:**   - `"disable"` - `"enable"` |
| **block-invite**  string | Enable/disable block INVITE requests.  **Choices:**   - `"disable"` - `"enable"` |
| **block-long-lines**  string | Enable/disable block requests with headers exceeding max-line-length.  **Choices:**   - `"disable"` - `"enable"` |
| **block-message**  string | Enable/disable block MESSAGE requests.  **Choices:**   - `"disable"` - `"enable"` |
| **block-notify**  string | Enable/disable block NOTIFY requests.  **Choices:**   - `"disable"` - `"enable"` |
| **block-options**  string | Enable/disable block OPTIONS requests and no OPTIONS as notifying message for redundancy either.  **Choices:**   - `"disable"` - `"enable"` |
| **block-prack**  string | Enable/disable block prack requests.  **Choices:**   - `"disable"` - `"enable"` |
| **block-publish**  string | Enable/disable block PUBLISH requests.  **Choices:**   - `"disable"` - `"enable"` |
| **block-refer**  string | Enable/disable block REFER requests.  **Choices:**   - `"disable"` - `"enable"` |
| **block-register**  string | Enable/disable block REGISTER requests.  **Choices:**   - `"disable"` - `"enable"` |
| **block-subscribe**  string | Enable/disable block SUBSCRIBE requests.  **Choices:**   - `"disable"` - `"enable"` |
| **block-unknown**  string | Block unrecognized SIP requests  **Choices:**   - `"disable"` - `"enable"` |
| **block-update**  string | Enable/disable block UPDATE requests.  **Choices:**   - `"disable"` - `"enable"` |
| **bye-rate**  integer | BYE request rate limit |
| **bye-rate-track**  string | Track the packet protocol field.  **Choices:**   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **call-id-regex**  string | Validate PCRE regular expression for Call-Id header value. |
| **call-keepalive**  integer | Continue tracking calls with no RTP for this many minutes. |
| **cancel-rate**  integer | CANCEL request rate limit |
| **cancel-rate-track**  string | Track the packet protocol field.  **Choices:**   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **contact-fixup**  string | Fixup contact anyway even if contacts IP  **Choices:**   - `"disable"` - `"enable"` |
| **content-type-regex**  string | Validate PCRE regular expression for Content-Type header value. |
| **hnt-restrict-source-ip**  string | Enable/disable restrict RTP source IP to be the same as SIP source IP when HNT is enabled.  **Choices:**   - `"disable"` - `"enable"` |
| **hosted-nat-traversal**  string | Hosted NAT Traversal  **Choices:**   - `"disable"` - `"enable"` |
| **info-rate**  integer | INFO request rate limit |
| **info-rate-track**  string | Track the packet protocol field.  **Choices:**   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **invite-rate**  integer | INVITE request rate limit |
| **invite-rate-track**  string | Track the packet protocol field.  **Choices:**   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **ips-rtp**  string | Enable/disable allow IPS on RTP.  **Choices:**   - `"disable"` - `"enable"` |
| **log-call-summary**  string | Enable/disable logging of SIP call summary.  **Choices:**   - `"disable"` - `"enable"` |
| **log-violations**  string | Enable/disable logging of SIP violations.  **Choices:**   - `"disable"` - `"enable"` |
| **malformed-header-allow**  string | Action for malformed Allow header.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-call-id**  string | Action for malformed Call-ID header.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-contact**  string | Action for malformed Contact header.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-content-length**  string | Action for malformed Content-Length header.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-content-type**  string | Action for malformed Content-Type header.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-cseq**  string | Action for malformed CSeq header.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-expires**  string | Action for malformed Expires header.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-from**  string | Action for malformed From header.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-max-forwards**  string | Action for malformed Max-Forwards header.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-no-proxy-require**  string | Action for malformed SIP messages without Proxy-Require header.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-no-require**  string | Action for malformed SIP messages without Require header.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-p-asserted-identity**  string | Action for malformed P-Asserted-Identity header.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-rack**  string | Action for malformed RAck header.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-record-route**  string | Action for malformed Record-Route header.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-route**  string | Action for malformed Route header.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-rseq**  string | Action for malformed RSeq header.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-sdp-a**  string | Action for malformed SDP a line.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-sdp-b**  string | Action for malformed SDP b line.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-sdp-c**  string | Action for malformed SDP c line.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-sdp-i**  string | Action for malformed SDP i line.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-sdp-k**  string | Action for malformed SDP k line.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-sdp-m**  string | Action for malformed SDP m line.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-sdp-o**  string | Action for malformed SDP o line.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-sdp-r**  string | Action for malformed SDP r line.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-sdp-s**  string | Action for malformed SDP s line.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-sdp-t**  string | Action for malformed SDP t line.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-sdp-v**  string | Action for malformed SDP v line.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-sdp-z**  string | Action for malformed SDP z line.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-to**  string | Action for malformed To header.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-via**  string | Action for malformed VIA header.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-request-line**  string | Action for malformed request line.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **max-body-length**  integer | Maximum SIP message body length |
| **max-dialogs**  integer | Maximum number of concurrent calls/dialogs |
| **max-idle-dialogs**  integer | Maximum number established but idle dialogs to retain |
| **max-line-length**  integer | Maximum SIP header line length |
| **message-rate**  integer | MESSAGE request rate limit |
| **message-rate-track**  string | Track the packet protocol field.  **Choices:**   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **nat-port-range**  string | RTP NAT port range. |
| **nat-trace**  string | Enable/disable preservation of original IP in SDP i line.  **Choices:**   - `"disable"` - `"enable"` |
| **no-sdp-fixup**  string | Enable/disable no SDP fix-up.  **Choices:**   - `"disable"` - `"enable"` |
| **notify-rate**  integer | NOTIFY request rate limit |
| **notify-rate-track**  string | Track the packet protocol field.  **Choices:**   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **open-contact-pinhole**  string | Enable/disable open pinhole for non-REGISTER Contact port.  **Choices:**   - `"disable"` - `"enable"` |
| **open-record-route-pinhole**  string | Enable/disable open pinhole for Record-Route port.  **Choices:**   - `"disable"` - `"enable"` |
| **open-register-pinhole**  string | Enable/disable open pinhole for REGISTER Contact port.  **Choices:**   - `"disable"` - `"enable"` |
| **open-via-pinhole**  string | Enable/disable open pinhole for Via port.  **Choices:**   - `"disable"` - `"enable"` |
| **options-rate**  integer | OPTIONS request rate limit |
| **options-rate-track**  string | Track the packet protocol field.  **Choices:**   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **prack-rate**  integer | PRACK request rate limit |
| **prack-rate-track**  string | Track the packet protocol field.  **Choices:**   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **preserve-override**  string | Override i line to preserve original IPS  **Choices:**   - `"disable"` - `"enable"` |
| **provisional-invite-expiry-time**  integer | Expiry time for provisional INVITE |
| **publish-rate**  integer | PUBLISH request rate limit |
| **publish-rate-track**  string | Track the packet protocol field.  **Choices:**   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **refer-rate**  integer | REFER request rate limit |
| **refer-rate-track**  string | Track the packet protocol field.  **Choices:**   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **register-contact-trace**  string | Enable/disable trace original IP/port within the contact header of REGISTER requests.  **Choices:**   - `"disable"` - `"enable"` |
| **register-rate**  integer | REGISTER request rate limit |
| **register-rate-track**  string | Track the packet protocol field.  **Choices:**   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **rfc2543-branch**  string | Enable/disable support via branch compliant with RFC 2543.  **Choices:**   - `"disable"` - `"enable"` |
| **rtp**  string | Enable/disable create pinholes for RTP traffic to traverse firewall.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-algorithm**  string | Relative strength of encryption algorithms accepted in negotiation.  **Choices:**   - `"high"` - `"medium"` - `"low"` |
| **ssl-auth-client**  string | Require a client certificate and authenticate it with the peer/peergrp. |
| **ssl-auth-server**  string | Authenticate the servers certificate with the peer/peergrp. |
| **ssl-client-certificate**  string | Name of Certificate to offer to server if requested. |
| **ssl-client-renegotiation**  string | Allow/block client renegotiation by server.  **Choices:**   - `"allow"` - `"deny"` - `"secure"` |
| **ssl-max-version**  string | Highest SSL/TLS version to negotiate.  **Choices:**   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl-min-version**  string | Lowest SSL/TLS version to negotiate.  **Choices:**   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl-mode**  string | SSL/TLS mode for encryption & decryption of traffic.  **Choices:**   - `"off"` - `"full"` |
| **ssl-pfs**  string | SSL Perfect Forward Secrecy.  **Choices:**   - `"require"` - `"deny"` - `"allow"` |
| **ssl-send-empty-frags**  string | Send empty fragments to avoid attack on CBC IV  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-server-certificate**  string | Name of Certificate return to the client in every SSL connection. |
| **status**  string | Enable/disable SIP.  **Choices:**   - `"disable"` - `"enable"` |
| **strict-register**  string | Enable/disable only allow the registrar to connect.  **Choices:**   - `"disable"` - `"enable"` |
| **subscribe-rate**  integer | SUBSCRIBE request rate limit |
| **subscribe-rate-track**  string | Track the packet protocol field.  **Choices:**   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **unknown-header**  string | Action for unknown SIP header.  **Choices:**   - `"pass"` - `"discard"` - `"respond"` |
| **update-rate**  integer | UPDATE request rate limit |
| **update-rate-track**  string | Track the packet protocol field.  **Choices:**   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_voip_profile_sip_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_voip_profile_sip_module.md#id4)

```yaml+jinja
- hosts: fortimanager-inventory
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
    ansible_httpapi_use_ssl: True
    ansible_httpapi_validate_certs: False
    ansible_httpapi_port: 443
  tasks:
    - name: SIP.
      fmgr_voip_profile_sip:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        profile: <your own value>
        voip_profile_sip:
          ack-rate: <integer>
          block-ack: <value in [disable, enable]>
          block-bye: <value in [disable, enable]>
          block-cancel: <value in [disable, enable]>
          block-geo-red-options: <value in [disable, enable]>
          block-info: <value in [disable, enable]>
          block-invite: <value in [disable, enable]>
          block-long-lines: <value in [disable, enable]>
          block-message: <value in [disable, enable]>
          block-notify: <value in [disable, enable]>
          block-options: <value in [disable, enable]>
          block-prack: <value in [disable, enable]>
          block-publish: <value in [disable, enable]>
          block-refer: <value in [disable, enable]>
          block-register: <value in [disable, enable]>
          block-subscribe: <value in [disable, enable]>
          block-unknown: <value in [disable, enable]>
          block-update: <value in [disable, enable]>
          bye-rate: <integer>
          call-keepalive: <integer>
          cancel-rate: <integer>
          contact-fixup: <value in [disable, enable]>
          hnt-restrict-source-ip: <value in [disable, enable]>
          hosted-nat-traversal: <value in [disable, enable]>
          info-rate: <integer>
          invite-rate: <integer>
          ips-rtp: <value in [disable, enable]>
          log-call-summary: <value in [disable, enable]>
          log-violations: <value in [disable, enable]>
          malformed-header-allow: <value in [pass, discard, respond]>
          malformed-header-call-id: <value in [pass, discard, respond]>
          malformed-header-contact: <value in [pass, discard, respond]>
          malformed-header-content-length: <value in [pass, discard, respond]>
          malformed-header-content-type: <value in [pass, discard, respond]>
          malformed-header-cseq: <value in [pass, discard, respond]>
          malformed-header-expires: <value in [pass, discard, respond]>
          malformed-header-from: <value in [pass, discard, respond]>
          malformed-header-max-forwards: <value in [pass, discard, respond]>
          malformed-header-p-asserted-identity: <value in [pass, discard, respond]>
          malformed-header-rack: <value in [pass, discard, respond]>
          malformed-header-record-route: <value in [pass, discard, respond]>
          malformed-header-route: <value in [pass, discard, respond]>
          malformed-header-rseq: <value in [pass, discard, respond]>
          malformed-header-sdp-a: <value in [pass, discard, respond]>
          malformed-header-sdp-b: <value in [pass, discard, respond]>
          malformed-header-sdp-c: <value in [pass, discard, respond]>
          malformed-header-sdp-i: <value in [pass, discard, respond]>
          malformed-header-sdp-k: <value in [pass, discard, respond]>
          malformed-header-sdp-m: <value in [pass, discard, respond]>
          malformed-header-sdp-o: <value in [pass, discard, respond]>
          malformed-header-sdp-r: <value in [pass, discard, respond]>
          malformed-header-sdp-s: <value in [pass, discard, respond]>
          malformed-header-sdp-t: <value in [pass, discard, respond]>
          malformed-header-sdp-v: <value in [pass, discard, respond]>
          malformed-header-sdp-z: <value in [pass, discard, respond]>
          malformed-header-to: <value in [pass, discard, respond]>
          malformed-header-via: <value in [pass, discard, respond]>
          malformed-request-line: <value in [pass, discard, respond]>
          max-body-length: <integer>
          max-dialogs: <integer>
          max-idle-dialogs: <integer>
          max-line-length: <integer>
          message-rate: <integer>
          nat-trace: <value in [disable, enable]>
          no-sdp-fixup: <value in [disable, enable]>
          notify-rate: <integer>
          open-contact-pinhole: <value in [disable, enable]>
          open-record-route-pinhole: <value in [disable, enable]>
          open-register-pinhole: <value in [disable, enable]>
          open-via-pinhole: <value in [disable, enable]>
          options-rate: <integer>
          prack-rate: <integer>
          preserve-override: <value in [disable, enable]>
          provisional-invite-expiry-time: <integer>
          publish-rate: <integer>
          refer-rate: <integer>
          register-contact-trace: <value in [disable, enable]>
          register-rate: <integer>
          rfc2543-branch: <value in [disable, enable]>
          rtp: <value in [disable, enable]>
          ssl-algorithm: <value in [high, medium, low]>
          ssl-auth-client: <string>
          ssl-auth-server: <string>
          ssl-client-certificate: <string>
          ssl-client-renegotiation: <value in [allow, deny, secure]>
          ssl-max-version: <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
          ssl-min-version: <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
          ssl-mode: <value in [off, full]>
          ssl-pfs: <value in [require, deny, allow]>
          ssl-send-empty-frags: <value in [disable, enable]>
          ssl-server-certificate: <string>
          status: <value in [disable, enable]>
          strict-register: <value in [disable, enable]>
          subscribe-rate: <integer>
          unknown-header: <value in [pass, discard, respond]>
          update-rate: <integer>
          nat-port-range: <string>
          ack-rate-track: <value in [none, src-ip, dest-ip]>
          bye-rate-track: <value in [none, src-ip, dest-ip]>
          cancel-rate-track: <value in [none, src-ip, dest-ip]>
          info-rate-track: <value in [none, src-ip, dest-ip]>
          invite-rate-track: <value in [none, src-ip, dest-ip]>
          malformed-header-no-proxy-require: <value in [pass, discard, respond]>
          malformed-header-no-require: <value in [pass, discard, respond]>
          message-rate-track: <value in [none, src-ip, dest-ip]>
          notify-rate-track: <value in [none, src-ip, dest-ip]>
          options-rate-track: <value in [none, src-ip, dest-ip]>
          prack-rate-track: <value in [none, src-ip, dest-ip]>
          publish-rate-track: <value in [none, src-ip, dest-ip]>
          refer-rate-track: <value in [none, src-ip, dest-ip]>
          register-rate-track: <value in [none, src-ip, dest-ip]>
          subscribe-rate-track: <value in [none, src-ip, dest-ip]>
          update-rate-track: <value in [none, src-ip, dest-ip]>
          call-id-regex: <string>
          content-type-regex: <string>
```

## [Return Values](fmgr_voip_profile_sip_module.md#id5)

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
