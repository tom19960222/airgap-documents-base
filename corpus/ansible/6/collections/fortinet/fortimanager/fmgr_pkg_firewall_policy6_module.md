---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_pkg_firewall_policy6 module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_pkg_firewall_policy6_module.html
fetched_at: 2026-07-27T17:33:55+00:00
---
# fortinet.fortimanager.fmgr_pkg_firewall_policy6 module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_pkg_firewall_policy6`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_pkg_firewall_policy6_module.md#synopsis)
- [Parameters](fmgr_pkg_firewall_policy6_module.md#parameters)
- [Notes](fmgr_pkg_firewall_policy6_module.md#notes)
- [Examples](fmgr_pkg_firewall_policy6_module.md#examples)
- [Return Values](fmgr_pkg_firewall_policy6_module.md#return-values)

## [Synopsis](fmgr_pkg_firewall_policy6_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_pkg_firewall_policy6_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **pkg**  string / required | the parameter (pkg) in requested url |
| **pkg_firewall_policy6**  dictionary | the top level parameters set |
| **action**  string | no description  Choices:   - `"deny"` - `"accept"` - `"ipsec"` - `"ssl-vpn"` |
| **anti-replay**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **app-category**  string | no description |
| **app-group**  string | no description |
| **application**  integer | no description |
| **application-list**  string | no description |
| **auto-asic-offload**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **av-profile**  string | no description |
| **cifs-profile**  string | no description |
| **comments**  string | no description |
| **custom-log-fields**  string | no description |
| **decrypted-traffic-mirror**  string | no description |
| **devices**  string | no description |
| **diffserv-forward**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **diffserv-reverse**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **diffservcode-forward**  string | no description |
| **diffservcode-rev**  string | no description |
| **dlp-sensor**  string | no description |
| **dnsfilter-profile**  string | no description |
| **dscp-match**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dscp-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dscp-value**  string | no description |
| **dsri**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dstaddr**  string | no description |
| **dstaddr-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dstintf**  string | no description |
| **emailfilter-profile**  string | no description |
| **firewall-session-dirty**  string | no description  Choices:   - `"check-all"` - `"check-new"` |
| **fixedport**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **fsso-groups**  string | no description |
| **global-label**  string | no description |
| **groups**  string | no description |
| **http-policy-redirect**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **icap-profile**  string | no description |
| **inbound**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **inspection-mode**  string | no description  Choices:   - `"proxy"` - `"flow"` |
| **ippool**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ips-sensor**  string | no description |
| **label**  string | no description |
| **logtraffic**  string | no description  Choices:   - `"disable"` - `"enable"` - `"all"` - `"utm"` |
| **logtraffic-start**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **mms-profile**  string | no description |
| **name**  string | no description |
| **nat**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **natinbound**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **natoutbound**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **np-accelation**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **np-acceleration**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **outbound**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **per-ip-shaper**  string | no description |
| **policyid**  integer | no description |
| **poolname**  string | no description |
| **profile-group**  string | no description |
| **profile-protocol-options**  string | no description |
| **profile-type**  string | no description  Choices:   - `"single"` - `"group"` |
| **replacemsg-override-group**  string | no description |
| **rsso**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **schedule**  string | no description |
| **send-deny-packet**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **service**  string | no description |
| **service-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **session-ttl**  integer | no description |
| **spamfilter-profile**  string | no description |
| **srcaddr**  string | no description |
| **srcaddr-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
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
| **vlan-cos-fwd**  integer | no description |
| **vlan-cos-rev**  integer | no description |
| **vlan-filter**  string | no description |
| **voip-profile**  string | no description |
| **vpntunnel**  string | no description |
| **waf-profile**  string | no description |
| **webcache**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **webcache-https**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **webfilter-profile**  string | no description |
| **webproxy-forward-server**  string | no description |
| **webproxy-profile**  string | no description |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_pkg_firewall_policy6_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_pkg_firewall_policy6_module.md#id4)

```yaml+jinja
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
   - name: retrieve all the IPv6 policies
     fmgr_fact:
       facts:
           selector: 'pkg_firewall_policy6'
           params:
               adom: 'ansible'
               pkg: 'ansible' # package name
               policy6: 'your_value'
- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: Configure IPv6 policies.
     fmgr_pkg_firewall_policy6:
        bypass_validation: False
        adom: ansible
        pkg: ansible # package name
        state: present
        pkg_firewall_policy6:
           action: accept #<value in [deny, accept, ipsec, ...]>
           comments: ansible-comment
           dstaddr: all
           dstintf: any
           name: ansible-test-policy6
           nat: disable
           policyid: 1
           schedule: always
           service: ALL
           srcaddr: all
           srcintf: any
           status: disable
```

## [Return Values](fmgr_pkg_firewall_policy6_module.md#id5)

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
