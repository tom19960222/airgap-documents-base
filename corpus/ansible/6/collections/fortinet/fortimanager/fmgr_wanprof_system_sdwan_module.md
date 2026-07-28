---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_wanprof_system_sdwan module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_wanprof_system_sdwan_module.html
fetched_at: 2026-07-27T17:39:08+00:00
---
# fortinet.fortimanager.fmgr_wanprof_system_sdwan module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_wanprof_system_sdwan`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_wanprof_system_sdwan_module.md#synopsis)
- [Parameters](fmgr_wanprof_system_sdwan_module.md#parameters)
- [Notes](fmgr_wanprof_system_sdwan_module.md#notes)
- [Examples](fmgr_wanprof_system_sdwan_module.md#examples)
- [Return Values](fmgr_wanprof_system_sdwan_module.md#return-values)

## [Synopsis](fmgr_wanprof_system_sdwan_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_wanprof_system_sdwan_module.md#id2)

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
| **wanprof_system_sdwan**  dictionary | the top level parameters set |
| **duplication**  list / elements=string | description |
| **dstaddr**  string | no description |
| **dstaddr6**  string | no description |
| **dstintf**  string | no description |
| **id**  integer | no description |
| **packet-de-duplication**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **packet-duplication**  string | no description  Choices:   - `"disable"` - `"force"` - `"on-demand"` |
| **service**  string | no description |
| **service-id**  string | no description |
| **sla-match-service**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **srcaddr**  string | no description |
| **srcaddr6**  string | no description |
| **srcintf**  string | no description |
| **duplication-max-num**  integer | no description |
| **fail-detect**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **health-check**  list / elements=string | description |
| **_dynamic-server**  string | no description |
| **addr-mode**  string | no description  Choices:   - `"ipv4"` - `"ipv6"` |
| **detect-mode**  string | no description  Choices:   - `"active"` - `"passive"` - `"prefer-passive"` |
| **diffservcode**  string | no description |
| **dns-match-ip**  string | no description |
| **dns-request-domain**  string | no description |
| **failtime**  integer | no description |
| **ftp-file**  string | no description |
| **ftp-mode**  string | no description  Choices:   - `"passive"` - `"port"` |
| **ha-priority**  integer | no description |
| **http-agent**  string | no description |
| **http-get**  string | no description |
| **http-match**  string | no description |
| **interval**  integer | no description |
| **members**  string | no description |
| **mos-codec**  string | no description  Choices:   - `"g711"` - `"g722"` - `"g729"` |
| **name**  string | no description |
| **packet-size**  integer | no description |
| **password**  string | description |
| **port**  integer | no description |
| **probe-count**  integer | no description |
| **probe-packets**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **probe-timeout**  integer | no description |
| **protocol**  string | no description  Choices:   - `"ping"` - `"tcp-echo"` - `"udp-echo"` - `"http"` - `"twamp"` - `"ping6"` - `"dns"` - `"tcp-connect"` - `"ftp"` |
| **quality-measured-method**  string | no description  Choices:   - `"half-close"` - `"half-open"` |
| **recoverytime**  integer | no description |
| **security-mode**  string | no description  Choices:   - `"none"` - `"authentication"` |
| **server**  string | description |
| **sla**  list / elements=string | description |
| **id**  integer | no description |
| **jitter-threshold**  integer | no description |
| **latency-threshold**  integer | no description |
| **link-cost-factor**  list / elements=string | description  Choices:   - `"latency"` - `"jitter"` - `"packet-loss"` - `"mos"` |
| **mos-threshold**  string | no description |
| **packetloss-threshold**  integer | no description |
| **sla-fail-log-period**  integer | no description |
| **sla-pass-log-period**  integer | no description |
| **source**  string | no description |
| **system-dns**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **threshold-alert-jitter**  integer | no description |
| **threshold-alert-latency**  integer | no description |
| **threshold-alert-packetloss**  integer | no description |
| **threshold-warning-jitter**  integer | no description |
| **threshold-warning-latency**  integer | no description |
| **threshold-warning-packetloss**  integer | no description |
| **update-cascade-interface**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **update-static-route**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **user**  string | no description |
| **vrf**  integer | no description |
| **load-balance-mode**  string | no description  Choices:   - `"source-ip-based"` - `"weight-based"` - `"usage-based"` - `"source-dest-ip-based"` - `"measured-volume-based"` |
| **members**  list / elements=string | description |
| **_dynamic-member**  string | no description |
| **comment**  string | no description |
| **cost**  integer | no description |
| **gateway**  string | no description |
| **gateway6**  string | no description |
| **ingress-spillover-threshold**  integer | no description |
| **interface**  string | no description |
| **priority**  integer | no description |
| **priority6**  integer | no description |
| **seq-num**  integer | no description |
| **source**  string | no description |
| **source6**  string | no description |
| **spillover-threshold**  integer | no description |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **volume-ratio**  integer | no description |
| **weight**  integer | no description |
| **zone**  string | no description |
| **neighbor**  list / elements=string | description |
| **health-check**  string | no description |
| **ip**  string | no description |
| **member**  string | no description |
| **minimum-sla-meet-members**  integer | no description |
| **mode**  string | no description  Choices:   - `"sla"` - `"speedtest"` |
| **role**  string | no description  Choices:   - `"primary"` - `"secondary"` - `"standalone"` |
| **sla-id**  integer | no description |
| **neighbor-hold-boot-time**  integer | no description |
| **neighbor-hold-down**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **neighbor-hold-down-time**  integer | no description |
| **service**  list / elements=string | description |
| **addr-mode**  string | no description  Choices:   - `"ipv4"` - `"ipv6"` |
| **bandwidth-weight**  integer | no description |
| **default**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dscp-forward**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dscp-forward-tag**  string | no description |
| **dscp-reverse**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dscp-reverse-tag**  string | no description |
| **dst**  string | no description |
| **dst-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dst6**  string | no description |
| **end-port**  integer | no description |
| **gateway**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **groups**  string | no description |
| **hash-mode**  string | no description  Choices:   - `"round-robin"` - `"source-ip-based"` - `"source-dest-ip-based"` - `"inbandwidth"` - `"outbandwidth"` - `"bibandwidth"` |
| **health-check**  string | no description |
| **hold-down-time**  integer | no description |
| **id**  integer | no description |
| **input-device**  string | no description |
| **input-device-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **input-zone**  string | description |
| **internet-service**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **internet-service-app-ctrl**  integer | description |
| **internet-service-app-ctrl-category**  integer | description |
| **internet-service-app-ctrl-group**  string | no description |
| **internet-service-custom**  string | no description |
| **internet-service-custom-group**  string | no description |
| **internet-service-group**  string | no description |
| **internet-service-name**  string | no description |
| **jitter-weight**  integer | no description |
| **latency-weight**  integer | no description |
| **link-cost-factor**  string | no description  Choices:   - `"latency"` - `"jitter"` - `"packet-loss"` - `"inbandwidth"` - `"outbandwidth"` - `"bibandwidth"` - `"custom-profile-1"` |
| **link-cost-threshold**  integer | no description |
| **minimum-sla-meet-members**  integer | no description |
| **mode**  string | no description  Choices:   - `"auto"` - `"manual"` - `"priority"` - `"sla"` - `"load-balance"` |
| **name**  string | no description |
| **packet-loss-weight**  integer | no description |
| **passive-measurement**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **priority-members**  string | no description |
| **priority-zone**  string | description |
| **protocol**  integer | no description |
| **quality-link**  integer | no description |
| **role**  string | no description  Choices:   - `"primary"` - `"secondary"` - `"standalone"` |
| **route-tag**  integer | no description |
| **sla**  list / elements=string | description |
| **health-check**  string | no description |
| **id**  integer | no description |
| **sla-compare-method**  string | no description  Choices:   - `"order"` - `"number"` |
| **src**  string | no description |
| **src-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **src6**  string | no description |
| **standalone-action**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **start-port**  integer | no description |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **tie-break**  string | no description  Choices:   - `"zone"` - `"cfg-order"` - `"fib-best-match"` - `"input-device"` |
| **tos**  string | no description |
| **tos-mask**  string | no description |
| **use-shortcut-sla**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **users**  string | no description |
| **speedtest-bypass-routing**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **zone**  list / elements=string | description |
| **name**  string | no description |
| **service-sla-tie-break**  string | no description  Choices:   - `"cfg-order"` - `"fib-best-match"` - `"input-device"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_wanprof_system_sdwan_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_wanprof_system_sdwan_module.md#id4)

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
     fmgr_wanprof_system_sdwan:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        wanprof: <your own value>
        wanprof_system_sdwan:
           duplication:
             -
                 dstaddr: <value of string>
                 dstaddr6: <value of string>
                 dstintf: <value of string>
                 id: <value of integer>
                 packet-de-duplication: <value in [disable, enable]>
                 packet-duplication: <value in [disable, force, on-demand]>
                 service: <value of string>
                 srcaddr: <value of string>
                 srcaddr6: <value of string>
                 srcintf: <value of string>
                 service-id: <value of string>
                 sla-match-service: <value in [disable, enable]>
           duplication-max-num: <value of integer>
           fail-detect: <value in [disable, enable]>
           health-check:
             -
                 _dynamic-server: <value of string>
                 addr-mode: <value in [ipv4, ipv6]>
                 diffservcode: <value of string>
                 dns-match-ip: <value of string>
                 dns-request-domain: <value of string>
                 failtime: <value of integer>
                 ftp-file: <value of string>
                 ftp-mode: <value in [passive, port]>
                 ha-priority: <value of integer>
                 http-agent: <value of string>
                 http-get: <value of string>
                 http-match: <value of string>
                 interval: <value of integer>
                 members: <value of string>
                 name: <value of string>
                 packet-size: <value of integer>
                 password: <value of string>
                 port: <value of integer>
                 probe-count: <value of integer>
                 probe-packets: <value in [disable, enable]>
                 probe-timeout: <value of integer>
                 protocol: <value in [ping, tcp-echo, udp-echo, ...]>
                 quality-measured-method: <value in [half-close, half-open]>
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
                         - mos
                       packetloss-threshold: <value of integer>
                       mos-threshold: <value of string>
                 sla-fail-log-period: <value of integer>
                 sla-pass-log-period: <value of integer>
                 system-dns: <value in [disable, enable]>
                 threshold-alert-jitter: <value of integer>
                 threshold-alert-latency: <value of integer>
                 threshold-alert-packetloss: <value of integer>
                 threshold-warning-jitter: <value of integer>
                 threshold-warning-latency: <value of integer>
                 threshold-warning-packetloss: <value of integer>
                 update-cascade-interface: <value in [disable, enable]>
                 update-static-route: <value in [disable, enable]>
                 user: <value of string>
                 detect-mode: <value in [active, passive, prefer-passive]>
                 mos-codec: <value in [g711, g722, g729]>
                 source: <value of string>
                 vrf: <value of integer>
           load-balance-mode: <value in [source-ip-based, weight-based, usage-based, ...]>
           members:
             -
                 _dynamic-member: <value of string>
                 comment: <value of string>
                 cost: <value of integer>
                 gateway: <value of string>
                 gateway6: <value of string>
                 ingress-spillover-threshold: <value of integer>
                 interface: <value of string>
                 priority: <value of integer>
                 seq-num: <value of integer>
                 source: <value of string>
                 source6: <value of string>
                 spillover-threshold: <value of integer>
                 status: <value in [disable, enable]>
                 volume-ratio: <value of integer>
                 weight: <value of integer>
                 zone: <value of string>
                 priority6: <value of integer>
           neighbor:
             -
                 health-check: <value of string>
                 ip: <value of string>
                 member: <value of string>
                 role: <value in [primary, secondary, standalone]>
                 sla-id: <value of integer>
                 minimum-sla-meet-members: <value of integer>
                 mode: <value in [sla, speedtest]>
           neighbor-hold-boot-time: <value of integer>
           neighbor-hold-down: <value in [disable, enable]>
           neighbor-hold-down-time: <value of integer>
           service:
             -
                 addr-mode: <value in [ipv4, ipv6]>
                 bandwidth-weight: <value of integer>
                 default: <value in [disable, enable]>
                 dscp-forward: <value in [disable, enable]>
                 dscp-forward-tag: <value of string>
                 dscp-reverse: <value in [disable, enable]>
                 dscp-reverse-tag: <value of string>
                 dst: <value of string>
                 dst-negate: <value in [disable, enable]>
                 dst6: <value of string>
                 end-port: <value of integer>
                 gateway: <value in [disable, enable]>
                 groups: <value of string>
                 hash-mode: <value in [round-robin, source-ip-based, source-dest-ip-based, ...]>
                 health-check: <value of string>
                 hold-down-time: <value of integer>
                 id: <value of integer>
                 input-device: <value of string>
                 input-device-negate: <value in [disable, enable]>
                 internet-service: <value in [disable, enable]>
                 internet-service-app-ctrl: <value of integer>
                 internet-service-app-ctrl-group: <value of string>
                 internet-service-custom: <value of string>
                 internet-service-custom-group: <value of string>
                 internet-service-group: <value of string>
                 internet-service-name: <value of string>
                 jitter-weight: <value of integer>
                 latency-weight: <value of integer>
                 link-cost-factor: <value in [latency, jitter, packet-loss, ...]>
                 link-cost-threshold: <value of integer>
                 minimum-sla-meet-members: <value of integer>
                 mode: <value in [auto, manual, priority, ...]>
                 name: <value of string>
                 packet-loss-weight: <value of integer>
                 priority-members: <value of string>
                 protocol: <value of integer>
                 quality-link: <value of integer>
                 role: <value in [primary, secondary, standalone]>
                 route-tag: <value of integer>
                 sla:
                   -
                       health-check: <value of string>
                       id: <value of integer>
                 sla-compare-method: <value in [order, number]>
                 src: <value of string>
                 src-negate: <value in [disable, enable]>
                 src6: <value of string>
                 standalone-action: <value in [disable, enable]>
                 start-port: <value of integer>
                 status: <value in [disable, enable]>
                 tos: <value of string>
                 tos-mask: <value of string>
                 users: <value of string>
                 tie-break: <value in [zone, cfg-order, fib-best-match, ...]>
                 use-shortcut-sla: <value in [disable, enable]>
                 input-zone: <value of string>
                 internet-service-app-ctrl-category: <value of integer>
                 passive-measurement: <value in [disable, enable]>
                 priority-zone: <value of string>
           status: <value in [disable, enable]>
           zone:
             -
                 name: <value of string>
                 service-sla-tie-break: <value in [cfg-order, fib-best-match, input-device]>
           speedtest-bypass-routing: <value in [disable, enable]>
```

## [Return Values](fmgr_wanprof_system_sdwan_module.md#id5)

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
