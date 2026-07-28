---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_pkg_firewall_policy module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_pkg_firewall_policy_module.html
fetched_at: 2026-07-27T17:33:54+00:00
---
# fortinet.fortimanager.fmgr_pkg_firewall_policy module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_pkg_firewall_policy`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_pkg_firewall_policy_module.md#synopsis)
- [Parameters](fmgr_pkg_firewall_policy_module.md#parameters)
- [Notes](fmgr_pkg_firewall_policy_module.md#notes)
- [Examples](fmgr_pkg_firewall_policy_module.md#examples)
- [Return Values](fmgr_pkg_firewall_policy_module.md#return-values)

## [Synopsis](fmgr_pkg_firewall_policy_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_pkg_firewall_policy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **pkg**  string / required | the parameter (pkg) in requested url |
| **pkg_firewall_policy**  dictionary | the top level parameters set |
| **_policy_block**  integer | no description |
| **action**  string | no description  Choices:   - `"deny"` - `"accept"` - `"ipsec"` - `"ssl-vpn"` - `"redirect"` - `"isolate"` |
| **anti-replay**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **app-category**  string | no description |
| **app-group**  string | no description |
| **application**  integer | no description |
| **application-list**  string | no description |
| **auth-cert**  string | no description |
| **auth-path**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **auth-redirect-addr**  string | no description |
| **auto-asic-offload**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **av-profile**  string | no description |
| **best-route**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **block-notification**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **captive-portal-exempt**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **capture-packet**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **cifs-profile**  string | no description |
| **comments**  string | no description |
| **custom-log-fields**  string | no description |
| **decrypted-traffic-mirror**  string | no description |
| **delay-tcp-npu-session**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **devices**  string | no description |
| **diffserv-forward**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **diffserv-reverse**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **diffservcode-forward**  string | no description |
| **diffservcode-rev**  string | no description |
| **disclaimer**  string | no description  Choices:   - `"disable"` - `"enable"` - `"user"` - `"domain"` - `"policy"` |
| **dlp-profile**  string | no description |
| **dlp-sensor**  string | no description |
| **dnsfilter-profile**  string | no description |
| **dscp-match**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dscp-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dscp-value**  string | no description |
| **dsri**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dstaddr**  string | no description |
| **dstaddr-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dstaddr6**  string | no description |
| **dstintf**  string | no description |
| **dynamic-shaping**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **email-collect**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **emailfilter-profile**  string | no description |
| **fec**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **file-filter-profile**  string | no description |
| **firewall-session-dirty**  string | no description  Choices:   - `"check-all"` - `"check-new"` |
| **fixedport**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **fsso**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **fsso-agent-for-ntlm**  string | no description |
| **fsso-groups**  string | no description |
| **geoip-anycast**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **geoip-match**  string | no description  Choices:   - `"physical-location"` - `"registered-location"` |
| **global-label**  string | no description |
| **groups**  string | no description |
| **gtp-profile**  string | no description |
| **http-policy-redirect**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **icap-profile**  string | no description |
| **identity-based-route**  string | no description |
| **inbound**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **inspection-mode**  string | no description  Choices:   - `"proxy"` - `"flow"` |
| **internet-service**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **internet-service-custom**  string | no description |
| **internet-service-custom-group**  string | no description |
| **internet-service-group**  string | no description |
| **internet-service-id**  string | no description |
| **internet-service-name**  string | no description |
| **internet-service-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **internet-service-src**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **internet-service-src-custom**  string | no description |
| **internet-service-src-custom-group**  string | no description |
| **internet-service-src-group**  string | no description |
| **internet-service-src-id**  string | no description |
| **internet-service-src-name**  string | no description |
| **internet-service-src-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ippool**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ips-sensor**  string | no description |
| **label**  string | no description |
| **learning-mode**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **logtraffic**  string | no description  Choices:   - `"disable"` - `"enable"` - `"all"` - `"utm"` |
| **logtraffic-start**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **match-vip**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **match-vip-only**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **mms-profile**  string | no description |
| **name**  string | no description |
| **nat**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **nat46**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **nat64**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **natinbound**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **natip**  string | no description |
| **natoutbound**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **np-acceleration**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ntlm**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ntlm-enabled-browsers**  string | no description |
| **ntlm-guest**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **object position**  list / elements=string | description |
| **outbound**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **passive-wan-health-measurement**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **per-ip-shaper**  string | no description |
| **permit-any-host**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **permit-stun-host**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **pfcp-profile**  string | no description |
| **policy-expiry**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **policy-expiry-date**  string | no description |
| **policyid**  integer | no description |
| **poolname**  string | no description |
| **poolname6**  string | no description |
| **profile-group**  string | no description |
| **profile-protocol-options**  string | no description |
| **profile-type**  string | no description  Choices:   - `"single"` - `"group"` |
| **radius-mac-auth-bypass**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **redirect-url**  string | no description |
| **replacemsg-override-group**  string | no description |
| **reputation-direction**  string | no description  Choices:   - `"source"` - `"destination"` |
| **reputation-minimum**  integer | no description |
| **rsso**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **rtp-addr**  string | no description |
| **rtp-nat**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **scan-botnet-connections**  string | no description  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **schedule**  string | no description |
| **schedule-timeout**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sctp-filter-profile**  string | no description |
| **send-deny-packet**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **service**  string | no description |
| **service-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **session-ttl**  integer | no description |
| **sgt**  integer | description |
| **sgt-check**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **spamfilter-profile**  string | no description |
| **src-vendor-mac**  string | no description |
| **srcaddr**  string | no description |
| **srcaddr-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **srcaddr6**  string | no description |
| **srcintf**  string | no description |
| **ssh-filter-profile**  string | no description |
| **ssh-policy-redirect**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ssl-mirror**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ssl-mirror-intf**  string | no description |
| **ssl-ssh-profile**  string | no description |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **tags**  string | no description |
| **tcp-mss-receiver**  integer | no description |
| **tcp-mss-sender**  integer | no description |
| **tcp-session-without-syn**  string | no description  Choices:   - `"all"` - `"data-only"` - `"disable"` |
| **timeout-send-rst**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **tos**  string | no description |
| **tos-mask**  string | no description |
| **tos-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **traffic-shaper**  string | no description |
| **traffic-shaper-reverse**  string | no description |
| **url-category**  string | no description |
| **users**  string | no description |
| **utm-status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **uuid**  string | no description |
| **videofilter-profile**  string | no description |
| **vlan-cos-fwd**  integer | no description |
| **vlan-cos-rev**  integer | no description |
| **vlan-filter**  string | no description |
| **voip-profile**  string | no description |
| **vpn_dst_node**  list / elements=string | no description |
| **host**  string | no description |
| **seq**  integer | no description |
| **subnet**  string | no description |
| **vpn_src_node**  list / elements=string | no description |
| **host**  string | no description |
| **seq**  integer | no description |
| **subnet**  string | no description |
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
| **wsso**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ztna-ems-tag**  string | no description |
| **ztna-geo-tag**  string | no description |
| **ztna-status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_pkg_firewall_policy_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_pkg_firewall_policy_module.md#id4)

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
   - name: Configure IPv4 policies.
     fmgr_pkg_firewall_policy:
        bypass_validation: False
        adom: ansible
        pkg: ansible # package name
        state: present
        pkg_firewall_policy:
           action: accept #<value in [deny, accept, ipsec, ...]>
           comments: ansible-comment
           dstaddr: all
           dstintf: any
           #name: ansible-test-policy
           nat: disable
           policyid: 1
           schedule: always
           service: ALL
           srcaddr: all
           srcintf: any
           status: disable

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
   - name: retrieve all the IPv4 policies
     fmgr_fact:
       facts:
           selector: 'pkg_firewall_policy'
           params:
               adom: 'ansible'
               pkg: 'ansible' # package name
               policy: 'your_value'
```

## [Return Values](fmgr_pkg_firewall_policy_module.md#id5)

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
