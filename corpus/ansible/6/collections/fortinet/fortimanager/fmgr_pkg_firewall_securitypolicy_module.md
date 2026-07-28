---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_pkg_firewall_securitypolicy module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_pkg_firewall_securitypolicy_module.html
fetched_at: 2026-07-27T17:34:01+00:00
---
# fortinet.fortimanager.fmgr_pkg_firewall_securitypolicy module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_pkg_firewall_securitypolicy`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_pkg_firewall_securitypolicy_module.md#synopsis)
- [Parameters](fmgr_pkg_firewall_securitypolicy_module.md#parameters)
- [Notes](fmgr_pkg_firewall_securitypolicy_module.md#notes)
- [Examples](fmgr_pkg_firewall_securitypolicy_module.md#examples)
- [Return Values](fmgr_pkg_firewall_securitypolicy_module.md#return-values)

## [Synopsis](fmgr_pkg_firewall_securitypolicy_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_pkg_firewall_securitypolicy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **pkg**  string / required | the parameter (pkg) in requested url |
| **pkg_firewall_securitypolicy**  dictionary | the top level parameters set |
| **_policy_block**  integer | no description |
| **action**  string | no description  Choices:   - `"deny"` - `"accept"` |
| **app-category**  string | no description |
| **app-group**  string | no description |
| **application**  integer | no description |
| **application-list**  string | no description |
| **av-profile**  string | no description |
| **cifs-profile**  string | no description |
| **comments**  string | no description |
| **dlp-profile**  string | no description |
| **dlp-sensor**  string | no description |
| **dnsfilter-profile**  string | no description |
| **dstaddr**  string | no description |
| **dstaddr-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dstaddr4**  string | no description |
| **dstaddr6**  string | no description |
| **dstintf**  string | no description |
| **emailfilter-profile**  string | no description |
| **enforce-default-app-port**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **file-filter-profile**  string | no description |
| **fsso-groups**  string | no description |
| **global-label**  string | no description |
| **groups**  string | no description |
| **icap-profile**  string | no description |
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
| **ips-sensor**  string | no description |
| **learning-mode**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **logtraffic**  string | no description  Choices:   - `"disable"` - `"all"` - `"utm"` |
| **logtraffic-start**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **mms-profile**  string | no description |
| **name**  string | no description |
| **nat46**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **nat64**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **policyid**  integer | no description |
| **profile-group**  string | no description |
| **profile-protocol-options**  string | no description |
| **profile-type**  string | no description  Choices:   - `"single"` - `"group"` |
| **schedule**  string | no description |
| **sctp-filter-profile**  string | no description |
| **send-deny-packet**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **service**  string | no description |
| **service-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **srcaddr**  string | no description |
| **srcaddr-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **srcaddr4**  string | no description |
| **srcaddr6**  string | no description |
| **srcintf**  string | no description |
| **ssh-filter-profile**  string | no description |
| **ssl-ssh-profile**  string | no description |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **url-category**  string | no description |
| **users**  string | no description |
| **utm-status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **uuid**  string | no description |
| **videofilter-profile**  string | no description |
| **voip-profile**  string | no description |
| **webfilter-profile**  string | no description |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_pkg_firewall_securitypolicy_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_pkg_firewall_securitypolicy_module.md#id4)

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
     fmgr_pkg_firewall_securitypolicy:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        pkg: <your own value>
        state: <value in [present, absent]>
        pkg_firewall_securitypolicy:
           action: <value in [deny, accept]>
           app-category: <value of string>
           app-group: <value of string>
           application: <value of integer>
           application-list: <value of string>
           av-profile: <value of string>
           cifs-profile: <value of string>
           comments: <value of string>
           dlp-sensor: <value of string>
           dnsfilter-profile: <value of string>
           dstaddr4: <value of string>
           dstaddr6: <value of string>
           dstintf: <value of string>
           emailfilter-profile: <value of string>
           enforce-default-app-port: <value in [disable, enable]>
           groups: <value of string>
           icap-profile: <value of string>
           internet-service: <value in [disable, enable]>
           internet-service-custom: <value of string>
           internet-service-custom-group: <value of string>
           internet-service-group: <value of string>
           internet-service-id: <value of string>
           internet-service-negate: <value in [disable, enable]>
           internet-service-src: <value in [disable, enable]>
           internet-service-src-custom: <value of string>
           internet-service-src-custom-group: <value of string>
           internet-service-src-group: <value of string>
           internet-service-src-id: <value of string>
           internet-service-src-negate: <value in [disable, enable]>
           ips-sensor: <value of string>
           logtraffic: <value in [disable, all, utm]>
           logtraffic-start: <value in [disable, enable]>
           mms-profile: <value of string>
           name: <value of string>
           policyid: <value of integer>
           profile-group: <value of string>
           profile-protocol-options: <value of string>
           profile-type: <value in [single, group]>
           schedule: <value of string>
           service: <value of string>
           service-negate: <value in [disable, enable]>
           srcaddr4: <value of string>
           srcaddr6: <value of string>
           srcintf: <value of string>
           ssh-filter-profile: <value of string>
           ssl-ssh-profile: <value of string>
           status: <value in [disable, enable]>
           url-category: <value of string>
           users: <value of string>
           utm-status: <value in [disable, enable]>
           uuid: <value of string>
           voip-profile: <value of string>
           webfilter-profile: <value of string>
           fsso-groups: <value of string>
           global-label: <value of string>
           send-deny-packet: <value in [disable, enable]>
           dstaddr: <value of string>
           internet-service-name: <value of string>
           internet-service-src-name: <value of string>
           srcaddr: <value of string>
           dstaddr-negate: <value in [disable, enable]>
           file-filter-profile: <value of string>
           srcaddr-negate: <value in [disable, enable]>
           learning-mode: <value in [disable, enable]>
           videofilter-profile: <value of string>
           _policy_block: <value of integer>
           dlp-profile: <value of string>
           nat46: <value in [disable, enable]>
           nat64: <value in [disable, enable]>
           sctp-filter-profile: <value of string>
```

## [Return Values](fmgr_pkg_firewall_securitypolicy_module.md#id5)

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
