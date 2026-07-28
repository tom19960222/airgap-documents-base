---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_wanprof_system_virtualwanlink_healthcheck module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_wanprof_system_virtualwanlink_healthcheck_module.html
fetched_at: 2026-07-27T17:39:15+00:00
---
# fortinet.fortimanager.fmgr_wanprof_system_virtualwanlink_healthcheck module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_wanprof_system_virtualwanlink_healthcheck`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_wanprof_system_virtualwanlink_healthcheck_module.md#synopsis)
- [Parameters](fmgr_wanprof_system_virtualwanlink_healthcheck_module.md#parameters)
- [Notes](fmgr_wanprof_system_virtualwanlink_healthcheck_module.md#notes)
- [Examples](fmgr_wanprof_system_virtualwanlink_healthcheck_module.md#examples)
- [Return Values](fmgr_wanprof_system_virtualwanlink_healthcheck_module.md#return-values)

## [Synopsis](fmgr_wanprof_system_virtualwanlink_healthcheck_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_wanprof_system_virtualwanlink_healthcheck_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **wanprof**  string / required | the parameter (wanprof) in requested url |
| **wanprof_system_virtualwanlink_healthcheck**  dictionary | the top level parameters set |
| **_dynamic-server**  string | no description |
| **addr-mode**  string | no description  Choices:   - `"ipv4"` - `"ipv6"` |
| **diffservcode**  string | no description |
| **dns-request-domain**  string | no description |
| **failtime**  integer | no description |
| **ha-priority**  integer | no description |
| **http-agent**  string | no description |
| **http-get**  string | no description |
| **http-match**  string | no description |
| **internet-service-id**  string | no description |
| **interval**  integer | no description |
| **members**  string | no description |
| **name**  string | no description |
| **packet-size**  integer | no description |
| **password**  string | description |
| **port**  integer | no description |
| **probe-count**  integer | no description |
| **probe-packets**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **probe-timeout**  integer | no description |
| **protocol**  string | no description  Choices:   - `"ping"` - `"tcp-echo"` - `"udp-echo"` - `"http"` - `"twamp"` - `"ping6"` - `"dns"` |
| **recoverytime**  integer | no description |
| **security-mode**  string | no description  Choices:   - `"none"` - `"authentication"` |
| **server**  string | description |
| **sla**  list / elements=string | description |
| **id**  integer | no description |
| **jitter-threshold**  integer | no description |
| **latency-threshold**  integer | no description |
| **link-cost-factor**  list / elements=string | description  Choices:   - `"latency"` - `"jitter"` - `"packet-loss"` |
| **packetloss-threshold**  integer | no description |
| **sla-fail-log-period**  integer | no description |
| **sla-pass-log-period**  integer | no description |
| **system-dns**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **threshold-alert-jitter**  integer | no description |
| **threshold-alert-latency**  integer | no description |
| **threshold-alert-packetloss**  integer | no description |
| **threshold-warning-jitter**  integer | no description |
| **threshold-warning-latency**  integer | no description |
| **threshold-warning-packetloss**  integer | no description |
| **update-cascade-interface**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **update-static-route**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_wanprof_system_virtualwanlink_healthcheck_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_wanprof_system_virtualwanlink_healthcheck_module.md#id4)

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
     fmgr_wanprof_system_virtualwanlink_healthcheck:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        wanprof: <your own value>
        state: <value in [present, absent]>
        wanprof_system_virtualwanlink_healthcheck:
           _dynamic-server: <value of string>
           addr-mode: <value in [ipv4, ipv6]>
           failtime: <value of integer>
           http-agent: <value of string>
           http-get: <value of string>
           http-match: <value of string>
           interval: <value of integer>
           members: <value of string>
           name: <value of string>
           packet-size: <value of integer>
           password: <value of string>
           port: <value of integer>
           protocol: <value in [ping, tcp-echo, udp-echo, ...]>
           recoverytime: <value of integer>
           security-mode: <value in [none, authentication]>
           server: <value of string>
           sla:
             -
                 id: <value of integer>
                 jitter-threshold: <value of integer>
                 latency-threshold: <value of integer>
                 link-cost-factor:
                   - latency
                   - jitter
                   - packet-loss
                 packetloss-threshold: <value of integer>
           threshold-alert-jitter: <value of integer>
           threshold-alert-latency: <value of integer>
           threshold-alert-packetloss: <value of integer>
           threshold-warning-jitter: <value of integer>
           threshold-warning-latency: <value of integer>
           threshold-warning-packetloss: <value of integer>
           update-cascade-interface: <value in [disable, enable]>
           update-static-route: <value in [disable, enable]>
           internet-service-id: <value of string>
           probe-packets: <value in [disable, enable]>
           sla-fail-log-period: <value of integer>
           sla-pass-log-period: <value of integer>
           ha-priority: <value of integer>
           diffservcode: <value of string>
           probe-timeout: <value of integer>
           dns-request-domain: <value of string>
           probe-count: <value of integer>
           system-dns: <value in [disable, enable]>
```

## [Return Values](fmgr_wanprof_system_virtualwanlink_healthcheck_module.md#id5)

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
