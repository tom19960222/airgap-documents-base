---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_pm_config_pblock_firewall_policy module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_pm_config_pblock_firewall_policy_module.html
fetched_at: 2026-07-27T17:34:12+00:00
---
# fortinet.fortimanager.fmgr_pm_config_pblock_firewall_policy module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_pm_config_pblock_firewall_policy`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_pm_config_pblock_firewall_policy_module.md#synopsis)
- [Parameters](fmgr_pm_config_pblock_firewall_policy_module.md#parameters)
- [Notes](fmgr_pm_config_pblock_firewall_policy_module.md#notes)
- [Examples](fmgr_pm_config_pblock_firewall_policy_module.md#examples)
- [Return Values](fmgr_pm_config_pblock_firewall_policy_module.md#return-values)

## [Synopsis](fmgr_pm_config_pblock_firewall_policy_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_pm_config_pblock_firewall_policy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **pblock**  string / required | the parameter (pblock) in requested url |
| **pm_config_pblock_firewall_policy**  dictionary | the top level parameters set |
| **_policy_block**  integer | no description |
| **action**  string | no description  Choices:   - `"deny"` - `"accept"` - `"ipsec"` - `"ssl-vpn"` - `"redirect"` - `"isolate"` |
| **anti-replay**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **application-list**  string | no description |
| **auth-cert**  string | no description |
| **auth-path**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **auth-redirect-addr**  string | no description |
| **auto-asic-offload**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **av-profile**  string | no description |
| **block-notification**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **captive-portal-exempt**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **capture-packet**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **cifs-profile**  string | no description |
| **comments**  string | no description |
| **custom-log-fields**  string | description |
| **decrypted-traffic-mirror**  string | no description |
| **delay-tcp-npu-session**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **diffserv-forward**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **diffserv-reverse**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **diffservcode-forward**  string | no description |
| **diffservcode-rev**  string | no description |
| **disclaimer**  string | no description  Choices:   - `"disable"` - `"enable"` - `"user"` - `"domain"` - `"policy"` |
| **dlp-profile**  string | no description |
| **dnsfilter-profile**  string | no description |
| **dsri**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dstaddr**  string | description |
| **dstaddr-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dstaddr6**  string | description |
| **dstintf**  string | description |
| **dynamic-shaping**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **email-collect**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **emailfilter-profile**  string | no description |
| **fec**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **file-filter-profile**  string | no description |
| **firewall-session-dirty**  string | no description  Choices:   - `"check-all"` - `"check-new"` |
| **fixedport**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **fsso-agent-for-ntlm**  string | no description |
| **fsso-groups**  string | description |
| **geoip-anycast**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **geoip-match**  string | no description  Choices:   - `"physical-location"` - `"registered-location"` |
| **global-label**  string | no description |
| **groups**  string | description |
| **gtp-profile**  string | no description |
| **http-policy-redirect**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **icap-profile**  string | no description |
| **identity-based-route**  string | no description |
| **inbound**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **inspection-mode**  string | no description  Choices:   - `"proxy"` - `"flow"` |
| **internet-service**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **internet-service-custom**  string | description |
| **internet-service-custom-group**  string | description |
| **internet-service-group**  string | description |
| **internet-service-name**  string | description |
| **internet-service-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **internet-service-src**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **internet-service-src-custom**  string | description |
| **internet-service-src-custom-group**  string | description |
| **internet-service-src-group**  string | description |
| **internet-service-src-name**  string | description |
| **internet-service-src-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ippool**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ips-sensor**  string | no description |
| **label**  string | no description |
| **logtraffic**  string | no description  Choices:   - `"disable"` - `"enable"` - `"all"` - `"utm"` |
| **logtraffic-start**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **match-vip**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **match-vip-only**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **name**  string | no description |
| **nat**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **nat46**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **nat64**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **natinbound**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **natip**  string | no description |
| **natoutbound**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **np-acceleration**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ntlm**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ntlm-enabled-browsers**  string | description |
| **ntlm-guest**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **outbound**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **passive-wan-health-measurement**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **per-ip-shaper**  string | no description |
| **permit-any-host**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **permit-stun-host**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **pfcp-profile**  string | no description |
| **policy-expiry**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **policy-expiry-date**  string | no description |
| **policyid**  integer | no description |
| **poolname**  string | description |
| **poolname6**  string | description |
| **profile-group**  string | no description |
| **profile-protocol-options**  string | no description |
| **profile-type**  string | no description  Choices:   - `"single"` - `"group"` |
| **radius-mac-auth-bypass**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **redirect-url**  string | no description |
| **replacemsg-override-group**  string | no description |
| **reputation-direction**  string | no description  Choices:   - `"source"` - `"destination"` |
| **reputation-minimum**  integer | no description |
| **rtp-addr**  string | description |
| **rtp-nat**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **schedule**  string | no description |
| **schedule-timeout**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sctp-filter-profile**  string | no description |
| **send-deny-packet**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **service**  string | description |
| **service-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **session-ttl**  integer | no description |
| **sgt**  integer | description |
| **sgt-check**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **src-vendor-mac**  string | description |
| **srcaddr**  string | description |
| **srcaddr-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **srcaddr6**  string | description |
| **srcintf**  string | description |
| **ssh-filter-profile**  string | no description |
| **ssh-policy-redirect**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ssl-ssh-profile**  string | no description |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **tcp-mss-receiver**  integer | no description |
| **tcp-mss-sender**  integer | no description |
| **tcp-session-without-syn**  string | no description  Choices:   - `"all"` - `"data-only"` - `"disable"` |
| **timeout-send-rst**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **tos**  string | no description |
| **tos-mask**  string | no description |
| **tos-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **traffic-shaper**  string | no description |
| **traffic-shaper-reverse**  string | no description |
| **users**  string | description |
| **utm-status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **uuid**  string | no description |
| **videofilter-profile**  string | no description |
| **vlan-cos-fwd**  integer | no description |
| **vlan-cos-rev**  integer | no description |
| **vlan-filter**  string | no description |
| **voip-profile**  string | no description |
| **vpntunnel**  string | no description |
| **waf-profile**  string | no description |
| **wanopt**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **wanopt-detection**  string | no description  Choices:   - `"active"` - `"passive"` - `"off"` |
| **wanopt-passive-opt**  string | no description  Choices:   - `"default"` - `"transparent"` - `"non-transparent"` |
| **wanopt-peer**  string | no description |
| **wanopt-profile**  string | no description |
| **wccp**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **webcache**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **webcache-https**  string | no description  Choices:   - `"disable"` - `"ssl-server"` - `"any"` - `"enable"` |
| **webfilter-profile**  string | no description |
| **webproxy-forward-server**  string | no description |
| **webproxy-profile**  string | no description |
| **ztna-ems-tag**  string | description |
| **ztna-geo-tag**  string | description |
| **ztna-status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_pm_config_pblock_firewall_policy_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_pm_config_pblock_firewall_policy_module.md#id4)

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
     fmgr_pm_config_pblock_firewall_policy:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        pblock: <your own value>
        state: <value in [present, absent]>
        pm_config_pblock_firewall_policy:
           _policy_block: <value of integer>
           action: <value in [deny, accept, ipsec, ...]>
           anti-replay: <value in [disable, enable]>
           application-list: <value of string>
           auth-cert: <value of string>
           auth-path: <value in [disable, enable]>
           auth-redirect-addr: <value of string>
           auto-asic-offload: <value in [disable, enable]>
           av-profile: <value of string>
           block-notification: <value in [disable, enable]>
           captive-portal-exempt: <value in [disable, enable]>
           capture-packet: <value in [disable, enable]>
           cifs-profile: <value of string>
           comments: <value of string>
           custom-log-fields: <value of string>
           decrypted-traffic-mirror: <value of string>
           delay-tcp-npu-session: <value in [disable, enable]>
           diffserv-forward: <value in [disable, enable]>
           diffserv-reverse: <value in [disable, enable]>
           diffservcode-forward: <value of string>
           diffservcode-rev: <value of string>
           disclaimer: <value in [disable, enable, user, ...]>
           dlp-profile: <value of string>
           dnsfilter-profile: <value of string>
           dsri: <value in [disable, enable]>
           dstaddr: <value of string>
           dstaddr-negate: <value in [disable, enable]>
           dstaddr6: <value of string>
           dstintf: <value of string>
           dynamic-shaping: <value in [disable, enable]>
           email-collect: <value in [disable, enable]>
           emailfilter-profile: <value of string>
           fec: <value in [disable, enable]>
           file-filter-profile: <value of string>
           firewall-session-dirty: <value in [check-all, check-new]>
           fixedport: <value in [disable, enable]>
           fsso-agent-for-ntlm: <value of string>
           fsso-groups: <value of string>
           geoip-anycast: <value in [disable, enable]>
           geoip-match: <value in [physical-location, registered-location]>
           global-label: <value of string>
           groups: <value of string>
           gtp-profile: <value of string>
           http-policy-redirect: <value in [disable, enable]>
           icap-profile: <value of string>
           identity-based-route: <value of string>
           inbound: <value in [disable, enable]>
           inspection-mode: <value in [proxy, flow]>
           internet-service: <value in [disable, enable]>
           internet-service-custom: <value of string>
           internet-service-custom-group: <value of string>
           internet-service-group: <value of string>
           internet-service-name: <value of string>
           internet-service-negate: <value in [disable, enable]>
           internet-service-src: <value in [disable, enable]>
           internet-service-src-custom: <value of string>
           internet-service-src-custom-group: <value of string>
           internet-service-src-group: <value of string>
           internet-service-src-name: <value of string>
           internet-service-src-negate: <value in [disable, enable]>
           ippool: <value in [disable, enable]>
           ips-sensor: <value of string>
           label: <value of string>
           logtraffic: <value in [disable, enable, all, ...]>
           logtraffic-start: <value in [disable, enable]>
           match-vip: <value in [disable, enable]>
           match-vip-only: <value in [disable, enable]>
           name: <value of string>
           nat: <value in [disable, enable]>
           nat46: <value in [disable, enable]>
           nat64: <value in [disable, enable]>
           natinbound: <value in [disable, enable]>
           natip: <value of string>
           natoutbound: <value in [disable, enable]>
           np-acceleration: <value in [disable, enable]>
           ntlm: <value in [disable, enable]>
           ntlm-enabled-browsers: <value of string>
           ntlm-guest: <value in [disable, enable]>
           outbound: <value in [disable, enable]>
           passive-wan-health-measurement: <value in [disable, enable]>
           per-ip-shaper: <value of string>
           permit-any-host: <value in [disable, enable]>
           permit-stun-host: <value in [disable, enable]>
           pfcp-profile: <value of string>
           policy-expiry: <value in [disable, enable]>
           policy-expiry-date: <value of string>
           policyid: <value of integer>
           poolname: <value of string>
           poolname6: <value of string>
           profile-group: <value of string>
           profile-protocol-options: <value of string>
           profile-type: <value in [single, group]>
           radius-mac-auth-bypass: <value in [disable, enable]>
           redirect-url: <value of string>
           replacemsg-override-group: <value of string>
           reputation-direction: <value in [source, destination]>
           reputation-minimum: <value of integer>
           rtp-addr: <value of string>
           rtp-nat: <value in [disable, enable]>
           schedule: <value of string>
           schedule-timeout: <value in [disable, enable]>
           sctp-filter-profile: <value of string>
           send-deny-packet: <value in [disable, enable]>
           service: <value of string>
           service-negate: <value in [disable, enable]>
           session-ttl: <value of integer>
           sgt: <value of integer>
           sgt-check: <value in [disable, enable]>
           src-vendor-mac: <value of string>
           srcaddr: <value of string>
           srcaddr-negate: <value in [disable, enable]>
           srcaddr6: <value of string>
           srcintf: <value of string>
           ssh-filter-profile: <value of string>
           ssh-policy-redirect: <value in [disable, enable]>
           ssl-ssh-profile: <value of string>
           status: <value in [disable, enable]>
           tcp-mss-receiver: <value of integer>
           tcp-mss-sender: <value of integer>
           tcp-session-without-syn: <value in [all, data-only, disable]>
           timeout-send-rst: <value in [disable, enable]>
           tos: <value of string>
           tos-mask: <value of string>
           tos-negate: <value in [disable, enable]>
           traffic-shaper: <value of string>
           traffic-shaper-reverse: <value of string>
           users: <value of string>
           utm-status: <value in [disable, enable]>
           uuid: <value of string>
           videofilter-profile: <value of string>
           vlan-cos-fwd: <value of integer>
           vlan-cos-rev: <value of integer>
           vlan-filter: <value of string>
           voip-profile: <value of string>
           vpntunnel: <value of string>
           waf-profile: <value of string>
           wanopt: <value in [disable, enable]>
           wanopt-detection: <value in [active, passive, off]>
           wanopt-passive-opt: <value in [default, transparent, non-transparent]>
           wanopt-peer: <value of string>
           wanopt-profile: <value of string>
           wccp: <value in [disable, enable]>
           webcache: <value in [disable, enable]>
           webcache-https: <value in [disable, ssl-server, any, ...]>
           webfilter-profile: <value of string>
           webproxy-forward-server: <value of string>
           webproxy-profile: <value of string>
           ztna-ems-tag: <value of string>
           ztna-geo-tag: <value of string>
           ztna-status: <value in [disable, enable]>
```

## [Return Values](fmgr_pm_config_pblock_firewall_policy_module.md#id5)

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
