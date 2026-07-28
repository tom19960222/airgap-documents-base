---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_voip_profile module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_voip_profile_module.html
fetched_at: 2026-07-27T17:38:23+00:00
---
# fortinet.fortimanager.fmgr_voip_profile module – no description

> **Note:**
>
> This module is part of the [fortinet.fortimanager collection](https://galaxy.ansible.com/fortinet/fortimanager) (version 2.1.7).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortimanager`.
>
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_voip_profile`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_voip_profile_module.md#synopsis)
- [Parameters](fmgr_voip_profile_module.md#parameters)
- [Notes](fmgr_voip_profile_module.md#notes)
- [Examples](fmgr_voip_profile_module.md#examples)
- [Return Values](fmgr_voip_profile_module.md#return-values)

## [Synopsis](fmgr_voip_profile_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_voip_profile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **voip_profile**  dictionary | the top level parameters set |
| **comment**  string | no description |
| **feature-set**  string | no description  Choices:   - `"flow"` - `"proxy"` |
| **msrp**  dictionary | no description |
| **log-violations**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **max-msg-size**  integer | no description |
| **max-msg-size-action**  string | no description  Choices:   - `"pass"` - `"block"` - `"reset"` - `"monitor"` |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **name**  string | no description |
| **sccp**  dictionary | no description |
| **block-mcast**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **log-call-summary**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **log-violations**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **max-calls**  integer | no description |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **verify-header**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sip**  dictionary | no description |
| **ack-rate**  integer | no description |
| **ack-rate-track**  string | no description  Choices:   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **block-ack**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **block-bye**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **block-cancel**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **block-geo-red-options**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **block-info**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **block-invite**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **block-long-lines**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **block-message**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **block-notify**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **block-options**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **block-prack**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **block-publish**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **block-refer**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **block-register**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **block-subscribe**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **block-unknown**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **block-update**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **bye-rate**  integer | no description |
| **bye-rate-track**  string | no description  Choices:   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **call-keepalive**  integer | no description |
| **cancel-rate**  integer | no description |
| **cancel-rate-track**  string | no description  Choices:   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **contact-fixup**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **hnt-restrict-source-ip**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **hosted-nat-traversal**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **info-rate**  integer | no description |
| **info-rate-track**  string | no description  Choices:   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **invite-rate**  integer | no description |
| **invite-rate-track**  string | no description  Choices:   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **ips-rtp**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **log-call-summary**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **log-violations**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **malformed-header-allow**  string | no description  Choices:   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-call-id**  string | no description  Choices:   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-contact**  string | no description  Choices:   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-content-length**  string | no description  Choices:   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-content-type**  string | no description  Choices:   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-cseq**  string | no description  Choices:   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-expires**  string | no description  Choices:   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-from**  string | no description  Choices:   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-max-forwards**  string | no description  Choices:   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-no-proxy-require**  string | no description  Choices:   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-no-require**  string | no description  Choices:   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-p-asserted-identity**  string | no description  Choices:   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-rack**  string | no description  Choices:   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-record-route**  string | no description  Choices:   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-route**  string | no description  Choices:   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-rseq**  string | no description  Choices:   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-sdp-a**  string | no description  Choices:   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-sdp-b**  string | no description  Choices:   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-sdp-c**  string | no description  Choices:   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-sdp-i**  string | no description  Choices:   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-sdp-k**  string | no description  Choices:   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-sdp-m**  string | no description  Choices:   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-sdp-o**  string | no description  Choices:   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-sdp-r**  string | no description  Choices:   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-sdp-s**  string | no description  Choices:   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-sdp-t**  string | no description  Choices:   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-sdp-v**  string | no description  Choices:   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-sdp-z**  string | no description  Choices:   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-to**  string | no description  Choices:   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-header-via**  string | no description  Choices:   - `"pass"` - `"discard"` - `"respond"` |
| **malformed-request-line**  string | no description  Choices:   - `"pass"` - `"discard"` - `"respond"` |
| **max-body-length**  integer | no description |
| **max-dialogs**  integer | no description |
| **max-idle-dialogs**  integer | no description |
| **max-line-length**  integer | no description |
| **message-rate**  integer | no description |
| **message-rate-track**  string | no description  Choices:   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **nat-port-range**  string | no description |
| **nat-trace**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **no-sdp-fixup**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **notify-rate**  integer | no description |
| **notify-rate-track**  string | no description  Choices:   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **open-contact-pinhole**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **open-record-route-pinhole**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **open-register-pinhole**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **open-via-pinhole**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **options-rate**  integer | no description |
| **options-rate-track**  string | no description  Choices:   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **prack-rate**  integer | no description |
| **prack-rate-track**  string | no description  Choices:   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **preserve-override**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **provisional-invite-expiry-time**  integer | no description |
| **publish-rate**  integer | no description |
| **publish-rate-track**  string | no description  Choices:   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **refer-rate**  integer | no description |
| **refer-rate-track**  string | no description  Choices:   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **register-contact-trace**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **register-rate**  integer | no description |
| **register-rate-track**  string | no description  Choices:   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **rfc2543-branch**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **rtp**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ssl-algorithm**  string | no description  Choices:   - `"high"` - `"medium"` - `"low"` |
| **ssl-auth-client**  string | no description |
| **ssl-auth-server**  string | no description |
| **ssl-client-certificate**  string | no description |
| **ssl-client-renegotiation**  string | no description  Choices:   - `"allow"` - `"deny"` - `"secure"` |
| **ssl-max-version**  string | no description  Choices:   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl-min-version**  string | no description  Choices:   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl-mode**  string | no description  Choices:   - `"off"` - `"full"` |
| **ssl-pfs**  string | no description  Choices:   - `"require"` - `"deny"` - `"allow"` |
| **ssl-send-empty-frags**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ssl-server-certificate**  string | no description |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **strict-register**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **subscribe-rate**  integer | no description |
| **subscribe-rate-track**  string | no description  Choices:   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **unknown-header**  string | no description  Choices:   - `"pass"` - `"discard"` - `"respond"` |
| **update-rate**  integer | no description |
| **update-rate-track**  string | no description  Choices:   - `"none"` - `"src-ip"` - `"dest-ip"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_voip_profile_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_voip_profile_module.md#id4)

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
   - name: no description
     fmgr_voip_profile:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        voip_profile:
           comment: <value of string>
           name: <value of string>
           sccp:
              block-mcast: <value in [disable, enable]>
              log-call-summary: <value in [disable, enable]>
              log-violations: <value in [disable, enable]>
              max-calls: <value of integer>
              status: <value in [disable, enable]>
              verify-header: <value in [disable, enable]>
           sip:
              ack-rate: <value of integer>
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
              bye-rate: <value of integer>
              call-keepalive: <value of integer>
              cancel-rate: <value of integer>
              contact-fixup: <value in [disable, enable]>
              hnt-restrict-source-ip: <value in [disable, enable]>
              hosted-nat-traversal: <value in [disable, enable]>
              info-rate: <value of integer>
              invite-rate: <value of integer>
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
              max-body-length: <value of integer>
              max-dialogs: <value of integer>
              max-idle-dialogs: <value of integer>
              max-line-length: <value of integer>
              message-rate: <value of integer>
              nat-port-range: <value of string>
              nat-trace: <value in [disable, enable]>
              no-sdp-fixup: <value in [disable, enable]>
              notify-rate: <value of integer>
              open-contact-pinhole: <value in [disable, enable]>
              open-record-route-pinhole: <value in [disable, enable]>
              open-register-pinhole: <value in [disable, enable]>
              open-via-pinhole: <value in [disable, enable]>
              options-rate: <value of integer>
              prack-rate: <value of integer>
              preserve-override: <value in [disable, enable]>
              provisional-invite-expiry-time: <value of integer>
              publish-rate: <value of integer>
              refer-rate: <value of integer>
              register-contact-trace: <value in [disable, enable]>
              register-rate: <value of integer>
              rfc2543-branch: <value in [disable, enable]>
              rtp: <value in [disable, enable]>
              ssl-algorithm: <value in [high, medium, low]>
              ssl-auth-client: <value of string>
              ssl-auth-server: <value of string>
              ssl-client-certificate: <value of string>
              ssl-client-renegotiation: <value in [allow, deny, secure]>
              ssl-max-version: <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
              ssl-min-version: <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
              ssl-mode: <value in [off, full]>
              ssl-pfs: <value in [require, deny, allow]>
              ssl-send-empty-frags: <value in [disable, enable]>
              ssl-server-certificate: <value of string>
              status: <value in [disable, enable]>
              strict-register: <value in [disable, enable]>
              subscribe-rate: <value of integer>
              unknown-header: <value in [pass, discard, respond]>
              update-rate: <value of integer>
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
           feature-set: <value in [flow, proxy]>
           msrp:
              log-violations: <value in [disable, enable]>
              max-msg-size: <value of integer>
              max-msg-size-action: <value in [pass, block, reset, ...]>
              status: <value in [disable, enable]>
```

## [Return Values](fmgr_voip_profile_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **request_url**  string | The full url requested  Returned: always  Sample: `"/sys/login/user"` |
| **response_code**  integer | The status of api request  Returned: always  Sample: `0` |
| **response_message**  string | The descriptive message of the api response  Returned: always  Sample: `"OK."` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Frank Shen (@fshen01)
- Hongbin Lu (@fgtdev-hblu)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/issues)
[Homepage](https://fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/tree/galaxy/2.1.7)
