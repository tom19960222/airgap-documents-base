---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_system_npu module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_system_npu_module.html
fetched_at: 2026-07-27T17:36:44+00:00
---
# fortinet.fortimanager.fmgr_system_npu module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_npu`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_system_npu_module.md#synopsis)
- [Parameters](fmgr_system_npu_module.md#parameters)
- [Notes](fmgr_system_npu_module.md#notes)
- [Examples](fmgr_system_npu_module.md#examples)
- [Return Values](fmgr_system_npu_module.md#return-values)

## [Synopsis](fmgr_system_npu_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_system_npu_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **system_npu**  dictionary | the top level parameters set |
| **capwap-offload**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dedicated-management-affinity**  string | no description |
| **dedicated-management-cpu**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **fastpath**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **fp-anomaly**  dictionary | no description |
| **esp-minlen-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **icmp-csum-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **icmp-minlen-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **ipv4-csum-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **ipv4-ihl-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **ipv4-len-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **ipv4-opt-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **ipv4-ttlzero-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **ipv4-ver-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **ipv6-exthdr-len-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **ipv6-exthdr-order-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **ipv6-ihl-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **ipv6-plen-zero**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **ipv6-ver-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **tcp-csum-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **tcp-hlen-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **tcp-plen-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **udp-csum-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **udp-hlen-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **udp-len-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **udp-plen-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **udplite-cover-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **udplite-csum-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **unknproto-minlen-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **gtp-enhanced-cpu-range**  string | no description  Choices:   - `"0"` - `"1"` - `"2"` |
| **gtp-enhanced-mode**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **host-shortcut-mode**  string | no description  Choices:   - `"bi-directional"` - `"host-shortcut"` |
| **htx-gtse-quota**  string | no description  Choices:   - `"100Mbps"` - `"200Mbps"` - `"300Mbps"` - `"400Mbps"` - `"500Mbps"` - `"600Mbps"` - `"700Mbps"` - `"800Mbps"` - `"900Mbps"` - `"1Gbps"` - `"2Gbps"` - `"4Gbps"` - `"8Gbps"` - `"10Gbps"` |
| **intf-shaping-offload**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **iph-rsvd-re-cksum**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ipsec-dec-subengine-mask**  string | no description |
| **ipsec-enc-subengine-mask**  string | no description |
| **ipsec-inbound-cache**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ipsec-mtu-override**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ipsec-over-vlink**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **isf-np-queues**  dictionary | no description |
| **cos0**  string | no description |
| **cos1**  string | no description |
| **cos2**  string | no description |
| **cos3**  string | no description |
| **cos4**  string | no description |
| **cos5**  string | no description |
| **cos6**  string | no description |
| **cos7**  string | no description |
| **lag-out-port-select**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **mcast-session-accounting**  string | no description  Choices:   - `"disable"` - `"session-based"` - `"tpe-based"` |
| **np6-cps-optimization-mode**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **per-session-accounting**  string | no description  Choices:   - `"enable"` - `"disable"` - `"enable-by-log"` - `"all-enable"` - `"traffic-log-only"` |
| **port-cpu-map**  list / elements=string | description |
| **cpu-core**  string | no description |
| **interface**  string | no description |
| **port-npu-map**  list / elements=string | description |
| **interface**  string | no description |
| **npu-group-index**  integer | no description |
| **priority-protocol**  dictionary | no description |
| **bfd**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **bgp**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **slbc**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **qos-mode**  string | no description  Choices:   - `"disable"` - `"priority"` - `"round-robin"` |
| **rdp-offload**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **recover-np6-link**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **session-denied-offload**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sse-backpressure**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **strip-clear-text-padding**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **strip-esp-padding**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sw-eh-hash**  dictionary | no description |
| **computation**  string | no description  Choices:   - `"xor16"` - `"xor8"` - `"xor4"` - `"crc16"` |
| **destination-ip-lower-16**  string | no description  Choices:   - `"include"` - `"exclude"` |
| **destination-ip-upper-16**  string | no description  Choices:   - `"include"` - `"exclude"` |
| **destination-port**  string | no description  Choices:   - `"include"` - `"exclude"` |
| **ip-protocol**  string | no description  Choices:   - `"include"` - `"exclude"` |
| **netmask-length**  integer | no description |
| **source-ip-lower-16**  string | no description  Choices:   - `"include"` - `"exclude"` |
| **source-ip-upper-16**  string | no description  Choices:   - `"include"` - `"exclude"` |
| **source-port**  string | no description  Choices:   - `"include"` - `"exclude"` |
| **sw-np-bandwidth**  string | no description  Choices:   - `"0G"` - `"2G"` - `"4G"` - `"5G"` - `"6G"` - `"7G"` - `"8G"` - `"9G"` |
| **switch-np-hash**  string | no description  Choices:   - `"src-ip"` - `"dst-ip"` - `"src-dst-ip"` |
| **uesp-offload**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_system_npu_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_npu_module.md#id4)

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
     fmgr_system_npu:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        system_npu:
           capwap-offload: <value in [disable, enable]>
           dedicated-management-affinity: <value of string>
           dedicated-management-cpu: <value in [disable, enable]>
           fastpath: <value in [disable, enable]>
           fp-anomaly:
              esp-minlen-err: <value in [drop, trap-to-host]>
              icmp-csum-err: <value in [drop, trap-to-host]>
              icmp-minlen-err: <value in [drop, trap-to-host]>
              ipv4-csum-err: <value in [drop, trap-to-host]>
              ipv4-ihl-err: <value in [drop, trap-to-host]>
              ipv4-len-err: <value in [drop, trap-to-host]>
              ipv4-opt-err: <value in [drop, trap-to-host]>
              ipv4-ttlzero-err: <value in [drop, trap-to-host]>
              ipv4-ver-err: <value in [drop, trap-to-host]>
              ipv6-exthdr-len-err: <value in [drop, trap-to-host]>
              ipv6-exthdr-order-err: <value in [drop, trap-to-host]>
              ipv6-ihl-err: <value in [drop, trap-to-host]>
              ipv6-plen-zero: <value in [drop, trap-to-host]>
              ipv6-ver-err: <value in [drop, trap-to-host]>
              tcp-csum-err: <value in [drop, trap-to-host]>
              tcp-hlen-err: <value in [drop, trap-to-host]>
              tcp-plen-err: <value in [drop, trap-to-host]>
              udp-csum-err: <value in [drop, trap-to-host]>
              udp-hlen-err: <value in [drop, trap-to-host]>
              udp-len-err: <value in [drop, trap-to-host]>
              udp-plen-err: <value in [drop, trap-to-host]>
              udplite-cover-err: <value in [drop, trap-to-host]>
              udplite-csum-err: <value in [drop, trap-to-host]>
              unknproto-minlen-err: <value in [drop, trap-to-host]>
           gtp-enhanced-cpu-range: <value in [0, 1, 2]>
           gtp-enhanced-mode: <value in [disable, enable]>
           host-shortcut-mode: <value in [bi-directional, host-shortcut]>
           htx-gtse-quota: <value in [100Mbps, 200Mbps, 300Mbps, ...]>
           intf-shaping-offload: <value in [disable, enable]>
           iph-rsvd-re-cksum: <value in [disable, enable]>
           ipsec-dec-subengine-mask: <value of string>
           ipsec-enc-subengine-mask: <value of string>
           ipsec-inbound-cache: <value in [disable, enable]>
           ipsec-mtu-override: <value in [disable, enable]>
           ipsec-over-vlink: <value in [disable, enable]>
           isf-np-queues:
              cos0: <value of string>
              cos1: <value of string>
              cos2: <value of string>
              cos3: <value of string>
              cos4: <value of string>
              cos5: <value of string>
              cos6: <value of string>
              cos7: <value of string>
           lag-out-port-select: <value in [disable, enable]>
           mcast-session-accounting: <value in [disable, session-based, tpe-based]>
           np6-cps-optimization-mode: <value in [disable, enable]>
           per-session-accounting: <value in [enable, disable, enable-by-log, ...]>
           port-cpu-map:
             -
                 cpu-core: <value of string>
                 interface: <value of string>
           port-npu-map:
             -
                 interface: <value of string>
                 npu-group-index: <value of integer>
           priority-protocol:
              bfd: <value in [disable, enable]>
              bgp: <value in [disable, enable]>
              slbc: <value in [disable, enable]>
           qos-mode: <value in [disable, priority, round-robin]>
           rdp-offload: <value in [disable, enable]>
           recover-np6-link: <value in [disable, enable]>
           session-denied-offload: <value in [disable, enable]>
           sse-backpressure: <value in [disable, enable]>
           strip-clear-text-padding: <value in [disable, enable]>
           strip-esp-padding: <value in [disable, enable]>
           sw-eh-hash:
              computation: <value in [xor16, xor8, xor4, ...]>
              destination-ip-lower-16: <value in [include, exclude]>
              destination-ip-upper-16: <value in [include, exclude]>
              destination-port: <value in [include, exclude]>
              ip-protocol: <value in [include, exclude]>
              netmask-length: <value of integer>
              source-ip-lower-16: <value in [include, exclude]>
              source-ip-upper-16: <value in [include, exclude]>
              source-port: <value in [include, exclude]>
           sw-np-bandwidth: <value in [0G, 2G, 4G, ...]>
           switch-np-hash: <value in [src-ip, dst-ip, src-dst-ip]>
           uesp-offload: <value in [disable, enable]>
```

## [Return Values](fmgr_system_npu_module.md#id5)

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
