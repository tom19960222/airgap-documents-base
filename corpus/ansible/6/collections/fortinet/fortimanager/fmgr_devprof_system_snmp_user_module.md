---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_devprof_system_snmp_user module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_devprof_system_snmp_user_module.html
fetched_at: 2026-07-27T17:29:07+00:00
---
# fortinet.fortimanager.fmgr_devprof_system_snmp_user module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_devprof_system_snmp_user`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_devprof_system_snmp_user_module.md#synopsis)
- [Parameters](fmgr_devprof_system_snmp_user_module.md#parameters)
- [Notes](fmgr_devprof_system_snmp_user_module.md#notes)
- [Examples](fmgr_devprof_system_snmp_user_module.md#examples)
- [Return Values](fmgr_devprof_system_snmp_user_module.md#return-values)

## [Synopsis](fmgr_devprof_system_snmp_user_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_devprof_system_snmp_user_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **devprof**  string / required | the parameter (devprof) in requested url |
| **devprof_system_snmp_user**  dictionary | the top level parameters set |
| **auth-proto**  string | no description  Choices:   - `"md5"` - `"sha"` - `"sha224"` - `"sha256"` - `"sha384"` - `"sha512"` |
| **auth-pwd**  string | description |
| **events**  list / elements=string | description  Choices:   - `"cpu-high"` - `"mem-low"` - `"log-full"` - `"intf-ip"` - `"vpn-tun-up"` - `"vpn-tun-down"` - `"ha-switch"` - `"fm-conf-change"` - `"ips-signature"` - `"ips-anomaly"` - `"temperature-high"` - `"voltage-alert"` - `"av-virus"` - `"av-oversize"` - `"av-pattern"` - `"av-fragmented"` - `"ha-hb-failure"` - `"fan-failure"` - `"ha-member-up"` - `"ha-member-down"` - `"ent-conf-change"` - `"av-conserve"` - `"av-bypass"` - `"av-oversize-passed"` - `"av-oversize-blocked"` - `"ips-pkg-update"` - `"fm-if-change"` - `"power-supply-failure"` - `"amc-bypass"` - `"faz-disconnect"` - `"bgp-established"` - `"bgp-backward-transition"` - `"wc-ap-up"` - `"wc-ap-down"` - `"fswctl-session-up"` - `"fswctl-session-down"` - `"ips-fail-open"` - `"load-balance-real-server-down"` - `"device-new"` - `"enter-intf-bypass"` - `"exit-intf-bypass"` - `"per-cpu-high"` - `"power-blade-down"` - `"confsync_failure"` - `"dhcp"` - `"pool-usage"` - `"power-redundancy-degrade"` - `"power-redundancy-failure"` - `"ospf-nbr-state-change"` - `"ospf-virtnbr-state-change"` - `"disk-failure"` - `"disk-overload"` |
| **ha-direct**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **mib-view**  string | no description |
| **name**  string | no description |
| **notify-hosts**  string | description |
| **notify-hosts6**  string | no description |
| **priv-proto**  string | no description  Choices:   - `"aes"` - `"des"` - `"aes256"` - `"aes256cisco"` |
| **priv-pwd**  string | description |
| **queries**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **query-port**  integer | no description |
| **security-level**  string | no description  Choices:   - `"no-auth-no-priv"` - `"auth-no-priv"` - `"auth-priv"` |
| **source-ip**  string | no description |
| **source-ipv6**  string | no description |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **trap-lport**  integer | no description |
| **trap-rport**  integer | no description |
| **trap-status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **vdoms**  string | description |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_devprof_system_snmp_user_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_devprof_system_snmp_user_module.md#id4)

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
   - name: SNMP user configuration.
     fmgr_devprof_system_snmp_user:
        bypass_validation: False
        adom: ansible
        devprof: 'ansible-test' # system template name, could find it in FortiManager UI: Device Manager --> Provisioning Templates --> System Templates
        state: present
        devprof_system_snmp_user:
           auth-proto: md5
           auth-pwd: 'fortinet'
           events:
             - cpu-high
             - mem-low
             - log-full
             - intf-ip
             - vpn-tun-up
             - vpn-tun-down
             - ha-switch
             - fm-conf-change
             - ips-signature
             - ips-anomaly
             - temperature-high
             - voltage-alert
             - av-virus
             - av-oversize
             - av-pattern
             - av-fragmented
             - ha-hb-failure
             - fan-failure
             - ha-member-up
             - ha-member-down
             - ent-conf-change
             - av-conserve
             - av-bypass
             - av-oversize-passed
             - av-oversize-blocked
             - ips-pkg-update
             - fm-if-change
             - power-supply-failure
             - amc-bypass
             - faz-disconnect
             - bgp-established
             - bgp-backward-transition
             - wc-ap-up
             - wc-ap-down
             - fswctl-session-up
             - fswctl-session-down
             - ips-fail-open
             - load-balance-real-server-down
             - device-new
             - enter-intf-bypass
             - exit-intf-bypass
             - per-cpu-high
             - power-blade-down
             - confsync_failure
           ha-direct: disable
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
   - name: retrieve all the scripts
     fmgr_fact:
       facts:
           selector: 'devprof_system_snmp_user'
           params:
               adom: 'ansible'
               devprof: 'ansible-test' # system template name, could find it in FortiManager UI: Device Manager --> Provisioning Templates --> System Templates
               user: 'your_value'
```

## [Return Values](fmgr_devprof_system_snmp_user_module.md#id5)

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
