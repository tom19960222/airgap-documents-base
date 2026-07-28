---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_pkg_firewall_consolidated_policy_sectionvalue module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_pkg_firewall_consolidated_policy_sectionvalue_module.html
fetched_at: 2026-07-27T17:33:45+00:00
---
# fortinet.fortimanager.fmgr_pkg_firewall_consolidated_policy_sectionvalue module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_pkg_firewall_consolidated_policy_sectionvalue`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_pkg_firewall_consolidated_policy_sectionvalue_module.md#synopsis)
- [Parameters](fmgr_pkg_firewall_consolidated_policy_sectionvalue_module.md#parameters)
- [Notes](fmgr_pkg_firewall_consolidated_policy_sectionvalue_module.md#notes)
- [Examples](fmgr_pkg_firewall_consolidated_policy_sectionvalue_module.md#examples)
- [Return Values](fmgr_pkg_firewall_consolidated_policy_sectionvalue_module.md#return-values)

## [Synopsis](fmgr_pkg_firewall_consolidated_policy_sectionvalue_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_pkg_firewall_consolidated_policy_sectionvalue_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **pkg**  string / required | the parameter (pkg) in requested url |
| **pkg_firewall_consolidated_policy_sectionvalue**  dictionary | the top level parameters set |
| **action**  string | no description  Choices:   - `"deny"` - `"accept"` - `"ipsec"` |
| **app-category**  string | no description |
| **app-group**  string | no description |
| **application**  integer | description |
| **application-list**  string | no description |
| **auto-asic-offload**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **av-profile**  string | no description |
| **captive-portal-exempt**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **cifs-profile**  string | no description |
| **comments**  string | no description |
| **diffserv-forward**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **diffserv-reverse**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **diffservcode-forward**  string | no description |
| **diffservcode-rev**  string | no description |
| **dlp-sensor**  string | no description |
| **dnsfilter-profile**  string | no description |
| **dstaddr-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dstaddr4**  string | no description |
| **dstaddr6**  string | no description |
| **dstintf**  string | no description |
| **emailfilter-profile**  string | no description |
| **fixedport**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **fsso-groups**  string | no description |
| **global-label**  string | no description |
| **groups**  string | no description |
| **http-policy-redirect**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **icap-profile**  string | no description |
| **inbound**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **inspection-mode**  string | no description  Choices:   - `"proxy"` - `"flow"` |
| **internet-service**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **internet-service-custom**  string | no description |
| **internet-service-custom-group**  string | no description |
| **internet-service-group**  string | no description |
| **internet-service-id**  string | no description |
| **internet-service-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **internet-service-src**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **internet-service-src-custom**  string | no description |
| **internet-service-src-custom-group**  string | no description |
| **internet-service-src-group**  string | no description |
| **internet-service-src-id**  string | no description |
| **internet-service-src-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ippool**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ips-sensor**  string | no description |
| **logtraffic**  string | no description  Choices:   - `"disable"` - `"all"` - `"utm"` |
| **logtraffic-start**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **mms-profile**  string | no description |
| **name**  string | no description |
| **nat**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **outbound**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **per-ip-shaper**  string | no description |
| **policyid**  integer | no description |
| **poolname4**  string | no description |
| **poolname6**  string | no description |
| **profile-group**  string | no description |
| **profile-protocol-options**  string | no description |
| **profile-type**  string | no description  Choices:   - `"single"` - `"group"` |
| **schedule**  string | no description |
| **service**  string | no description |
| **service-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **session-ttl**  integer | no description |
| **srcaddr-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **srcaddr4**  string | no description |
| **srcaddr6**  string | no description |
| **srcintf**  string | no description |
| **ssh-filter-profile**  string | no description |
| **ssh-policy-redirect**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ssl-ssh-profile**  string | no description |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **tcp-mss-receiver**  integer | no description |
| **tcp-mss-sender**  integer | no description |
| **traffic-shaper**  string | no description |
| **traffic-shaper-reverse**  string | no description |
| **url-category**  string | no description |
| **users**  string | no description |
| **utm-status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **uuid**  string | no description |
| **voip-profile**  string | no description |
| **vpntunnel**  string | no description |
| **waf-profile**  string | no description |
| **wanopt**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **wanopt-detection**  string | no description  Choices:   - `"active"` - `"passive"` - `"off"` |
| **wanopt-passive-opt**  string | no description  Choices:   - `"default"` - `"transparent"` - `"non-transparent"` |
| **wanopt-peer**  string | no description |
| **wanopt-profile**  string | no description |
| **webcache**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **webcache-https**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **webfilter-profile**  string | no description |
| **webproxy-forward-server**  string | no description |
| **webproxy-profile**  string | no description |
| **policy**  string / required | the parameter (policy) in requested url |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_pkg_firewall_consolidated_policy_sectionvalue_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_pkg_firewall_consolidated_policy_sectionvalue_module.md#id4)

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
     fmgr_pkg_firewall_consolidated_policy_sectionvalue:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        pkg: <your own value>
        policy: <your own value>
        state: <value in [present, absent]>
        pkg_firewall_consolidated_policy_sectionvalue:
           action: <value in [deny, accept, ipsec]>
           app-category: <value of string>
           app-group: <value of string>
           application: <value of integer>
           application-list: <value of string>
           auto-asic-offload: <value in [disable, enable]>
           av-profile: <value of string>
           cifs-profile: <value of string>
           comments: <value of string>
           diffserv-forward: <value in [disable, enable]>
           diffserv-reverse: <value in [disable, enable]>
           diffservcode-forward: <value of string>
           diffservcode-rev: <value of string>
           dlp-sensor: <value of string>
           dnsfilter-profile: <value of string>
           dstaddr4: <value of string>
           dstaddr6: <value of string>
           dstintf: <value of string>
           emailfilter-profile: <value of string>
           fixedport: <value in [disable, enable]>
           groups: <value of string>
           http-policy-redirect: <value in [disable, enable]>
           icap-profile: <value of string>
           inbound: <value in [disable, enable]>
           inspection-mode: <value in [proxy, flow]>
           internet-service: <value in [disable, enable]>
           internet-service-custom: <value of string>
           internet-service-custom-group: <value of string>
           internet-service-group: <value of string>
           internet-service-id: <value of string>
           internet-service-src: <value in [disable, enable]>
           internet-service-src-custom: <value of string>
           internet-service-src-custom-group: <value of string>
           internet-service-src-group: <value of string>
           internet-service-src-id: <value of string>
           ippool: <value in [disable, enable]>
           ips-sensor: <value of string>
           logtraffic: <value in [disable, all, utm]>
           logtraffic-start: <value in [disable, enable]>
           mms-profile: <value of string>
           name: <value of string>
           nat: <value in [disable, enable]>
           outbound: <value in [disable, enable]>
           per-ip-shaper: <value of string>
           policyid: <value of integer>
           poolname4: <value of string>
           poolname6: <value of string>
           profile-group: <value of string>
           profile-protocol-options: <value of string>
           profile-type: <value in [single, group]>
           schedule: <value of string>
           service: <value of string>
           session-ttl: <value of integer>
           srcaddr4: <value of string>
           srcaddr6: <value of string>
           srcintf: <value of string>
           ssh-filter-profile: <value of string>
           ssh-policy-redirect: <value in [disable, enable]>
           ssl-ssh-profile: <value of string>
           status: <value in [disable, enable]>
           tcp-mss-receiver: <value of integer>
           tcp-mss-sender: <value of integer>
           traffic-shaper: <value of string>
           traffic-shaper-reverse: <value of string>
           url-category: <value of string>
           users: <value of string>
           utm-status: <value in [disable, enable]>
           uuid: <value of string>
           voip-profile: <value of string>
           vpntunnel: <value of string>
           waf-profile: <value of string>
           wanopt: <value in [disable, enable]>
           wanopt-detection: <value in [active, passive, off]>
           wanopt-passive-opt: <value in [default, transparent, non-transparent]>
           wanopt-peer: <value of string>
           wanopt-profile: <value of string>
           webcache: <value in [disable, enable]>
           webcache-https: <value in [disable, enable]>
           webfilter-profile: <value of string>
           webproxy-forward-server: <value of string>
           webproxy-profile: <value of string>
           captive-portal-exempt: <value in [disable, enable]>
           dstaddr-negate: <value in [disable, enable]>
           fsso-groups: <value of string>
           global-label: <value of string>
           internet-service-negate: <value in [disable, enable]>
           internet-service-src-negate: <value in [disable, enable]>
           service-negate: <value in [disable, enable]>
           srcaddr-negate: <value in [disable, enable]>
```

## [Return Values](fmgr_pkg_firewall_consolidated_policy_sectionvalue_module.md#id5)

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
