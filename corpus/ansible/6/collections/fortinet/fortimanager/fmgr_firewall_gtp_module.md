---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_firewall_gtp module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_firewall_gtp_module.html
fetched_at: 2026-07-27T17:31:01+00:00
---
# fortinet.fortimanager.fmgr_firewall_gtp module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_firewall_gtp`.

New in fortinet.fortimanager 1.0.0

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
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **firewall_gtp**  dictionary | the top level parameters set |
| **addr-notify**  string | no description |
| **apn**  list / elements=string | no description |
| **action**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **apnmember**  string | no description |
| **id**  integer | no description |
| **selection-mode**  list / elements=string | no description  Choices:   - `"ms"` - `"net"` - `"vrf"` |
| **apn-filter**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **authorized-ggsns**  string | no description |
| **authorized-ggsns6**  string | no description |
| **authorized-sgsns**  string | no description |
| **authorized-sgsns6**  string | no description |
| **comment**  string | no description |
| **context-id**  integer | no description |
| **control-plane-message-rate-limit**  integer | no description |
| **default-apn-action**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **default-imsi-action**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **default-ip-action**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **default-noip-action**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **default-policy-action**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **denied-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **echo-request-interval**  integer | no description |
| **extension-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **forwarded-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **global-tunnel-limit**  string | no description |
| **gtp-in-gtp**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **gtpu-denied-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **gtpu-forwarded-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **gtpu-log-freq**  integer | no description |
| **half-close-timeout**  integer | no description |
| **half-open-timeout**  integer | no description |
| **handover-group**  string | no description |
| **handover-group6**  string | no description |
| **ie-allow-list-v0v1**  string | no description |
| **ie-allow-list-v2**  string | no description |
| **ie-remove-policy**  list / elements=string | no description |
| **id**  integer | no description |
| **remove-ies**  list / elements=string | no description  Choices:   - `"apn-restriction"` - `"rat-type"` - `"rai"` - `"uli"` - `"imei"` |
| **sgsn-addr**  string | no description |
| **sgsn-addr6**  string | no description |
| **ie-remover**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ie-validation**  dictionary | no description |
| **apn-restriction**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **charging-gateway-addr**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **charging-ID**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **end-user-addr**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **gsn-addr**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **imei**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **imsi**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **mm-context**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ms-tzone**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ms-validated**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **msisdn**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **nsapi**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **pdp-context**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **qos-profile**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **rai**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **rat-type**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **reordering-required**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **selection-mode**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **uli**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ie-white-list-v0v1**  string | no description |
| **ie-white-list-v2**  string | no description |
| **imsi**  list / elements=string | no description |
| **action**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **apnmember**  string | no description |
| **id**  integer | no description |
| **mcc-mnc**  string | no description |
| **msisdn-prefix**  string | no description |
| **selection-mode**  list / elements=string | no description  Choices:   - `"ms"` - `"net"` - `"vrf"` |
| **imsi-filter**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **interface-notify**  string | no description |
| **invalid-reserved-field**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **invalid-sgsns-to-log**  string | no description |
| **invalid-sgsns6-to-log**  string | no description |
| **ip-filter**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ip-policy**  list / elements=string | no description |
| **action**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **dstaddr**  string | no description |
| **dstaddr6**  string | no description |
| **id**  integer | no description |
| **srcaddr**  string | no description |
| **srcaddr6**  string | no description |
| **log-freq**  integer | no description |
| **log-gtpu-limit**  integer | no description |
| **log-imsi-prefix**  string | no description |
| **log-msisdn-prefix**  string | no description |
| **max-message-length**  integer | no description |
| **message-filter-v0v1**  string | no description |
| **message-filter-v2**  string | no description |
| **message-rate-limit**  dictionary | no description |
| **create-aa-pdp-request**  integer | no description |
| **create-aa-pdp-response**  integer | no description |
| **create-mbms-request**  integer | no description |
| **create-mbms-response**  integer | no description |
| **create-pdp-request**  integer | no description |
| **create-pdp-response**  integer | no description |
| **delete-aa-pdp-request**  integer | no description |
| **delete-aa-pdp-response**  integer | no description |
| **delete-mbms-request**  integer | no description |
| **delete-mbms-response**  integer | no description |
| **delete-pdp-request**  integer | no description |
| **delete-pdp-response**  integer | no description |
| **echo-reponse**  integer | no description |
| **echo-request**  integer | no description |
| **error-indication**  integer | no description |
| **failure-report-request**  integer | no description |
| **failure-report-response**  integer | no description |
| **fwd-reloc-complete-ack**  integer | no description |
| **fwd-relocation-complete**  integer | no description |
| **fwd-relocation-request**  integer | no description |
| **fwd-relocation-response**  integer | no description |
| **fwd-srns-context**  integer | no description |
| **fwd-srns-context-ack**  integer | no description |
| **g-pdu**  integer | no description |
| **identification-request**  integer | no description |
| **identification-response**  integer | no description |
| **mbms-de-reg-request**  integer | no description |
| **mbms-de-reg-response**  integer | no description |
| **mbms-notify-rej-request**  integer | no description |
| **mbms-notify-rej-response**  integer | no description |
| **mbms-notify-request**  integer | no description |
| **mbms-notify-response**  integer | no description |
| **mbms-reg-request**  integer | no description |
| **mbms-reg-response**  integer | no description |
| **mbms-ses-start-request**  integer | no description |
| **mbms-ses-start-response**  integer | no description |
| **mbms-ses-stop-request**  integer | no description |
| **mbms-ses-stop-response**  integer | no description |
| **note-ms-request**  integer | no description |
| **note-ms-response**  integer | no description |
| **pdu-notify-rej-request**  integer | no description |
| **pdu-notify-rej-response**  integer | no description |
| **pdu-notify-request**  integer | no description |
| **pdu-notify-response**  integer | no description |
| **ran-info**  integer | no description |
| **relocation-cancel-request**  integer | no description |
| **relocation-cancel-response**  integer | no description |
| **send-route-request**  integer | no description |
| **send-route-response**  integer | no description |
| **sgsn-context-ack**  integer | no description |
| **sgsn-context-request**  integer | no description |
| **sgsn-context-response**  integer | no description |
| **support-ext-hdr-notify**  integer | no description |
| **update-mbms-request**  integer | no description |
| **update-mbms-response**  integer | no description |
| **update-pdp-request**  integer | no description |
| **update-pdp-response**  integer | no description |
| **version-not-support**  integer | no description |
| **message-rate-limit-v0**  dictionary | no description |
| **create-pdp-request**  integer | no description |
| **delete-pdp-request**  integer | no description |
| **echo-request**  integer | no description |
| **message-rate-limit-v1**  dictionary | no description |
| **create-pdp-request**  integer | no description |
| **delete-pdp-request**  integer | no description |
| **echo-request**  integer | no description |
| **message-rate-limit-v2**  dictionary | no description |
| **create-session-request**  integer | no description |
| **delete-session-request**  integer | no description |
| **echo-request**  integer | no description |
| **min-message-length**  integer | no description |
| **miss-must-ie**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **monitor-mode**  string | no description  Choices:   - `"disable"` - `"enable"` - `"vdom"` |
| **name**  string | no description |
| **noip-filter**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **noip-policy**  list / elements=string | no description |
| **action**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **end**  integer | no description |
| **id**  integer | no description |
| **start**  integer | no description |
| **type**  string | no description  Choices:   - `"etsi"` - `"ietf"` |
| **out-of-state-ie**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **out-of-state-message**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **per-apn-shaper**  list / elements=string | no description |
| **apn**  string | no description |
| **id**  integer | no description |
| **rate-limit**  integer | no description |
| **version**  integer | no description |
| **policy**  list / elements=string | no description |
| **action**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **apn-sel-mode**  list / elements=string | no description  Choices:   - `"ms"` - `"net"` - `"vrf"` |
| **apnmember**  string | no description |
| **id**  integer | no description |
| **imei**  string | no description |
| **imsi**  string | no description |
| **imsi-prefix**  string | no description |
| **max-apn-restriction**  string | no description  Choices:   - `"all"` - `"public-1"` - `"public-2"` - `"private-1"` - `"private-2"` |
| **messages**  list / elements=string | no description  Choices:   - `"create-req"` - `"create-res"` - `"update-req"` - `"update-res"` |
| **msisdn**  string | no description |
| **msisdn-prefix**  string | no description |
| **rai**  string | no description |
| **rat-type**  list / elements=string | no description  Choices:   - `"any"` - `"utran"` - `"geran"` - `"wlan"` - `"gan"` - `"hspa"` - `"eutran"` - `"virtual"` - `"nbiot"` |
| **uli**  string | no description |
| **policy-filter**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **policy-v2**  list / elements=string | no description |
| **action**  string | no description  Choices:   - `"deny"` - `"allow"` |
| **apn-sel-mode**  list / elements=string | no description  Choices:   - `"ms"` - `"net"` - `"vrf"` |
| **apnmember**  string | no description |
| **id**  integer | no description |
| **imsi-prefix**  string | no description |
| **max-apn-restriction**  string | no description  Choices:   - `"all"` - `"public-1"` - `"public-2"` - `"private-1"` - `"private-2"` |
| **mei**  string | no description |
| **messages**  list / elements=string | no description  Choices:   - `"create-ses-req"` - `"create-ses-res"` - `"modify-bearer-req"` - `"modify-bearer-res"` |
| **msisdn-prefix**  string | no description |
| **rat-type**  list / elements=string | no description  Choices:   - `"any"` - `"utran"` - `"geran"` - `"wlan"` - `"gan"` - `"hspa"` - `"eutran"` - `"virtual"` - `"nbiot"` - `"ltem"` - `"nr"` |
| **uli**  string | no description |
| **port-notify**  integer | no description |
| **rat-timeout-profile**  string | no description |
| **rate-limit-mode**  string | no description  Choices:   - `"per-profile"` - `"per-stream"` - `"per-apn"` |
| **rate-limited-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **rate-sampling-interval**  integer | no description |
| **remove-if-echo-expires**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **remove-if-recovery-differ**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **reserved-ie**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **send-delete-when-timeout**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **send-delete-when-timeout-v2**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **spoof-src-addr**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **state-invalid-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sub-second-interval**  string | no description  Choices:   - `"0.1"` - `"0.25"` - `"0.5"` |
| **sub-second-sampling**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **traffic-count-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **tunnel-limit**  integer | no description |
| **tunnel-limit-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **tunnel-timeout**  integer | no description |
| **unknown-version-action**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **user-plane-message-rate-limit**  integer | no description |
| **warning-threshold**  integer | no description |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

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
