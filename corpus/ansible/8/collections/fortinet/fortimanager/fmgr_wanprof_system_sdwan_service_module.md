---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_wanprof_system_sdwan_service module – Create SD-WAN rules"
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_wanprof_system_sdwan_service_module.html
fetched_at: 2026-07-28T02:22:31+00:00
---
# fortinet.fortimanager.fmgr_wanprof_system_sdwan_service module – Create SD-WAN rules

> **Note:**
>
> This module is part of the [fortinet.fortimanager collection](https://galaxy.ansible.com/ui/repo/published/fortinet/fortimanager/) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortimanager`.
>
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_wanprof_system_sdwan_service`.

New in fortinet.fortimanager 2.1.0

- [Synopsis](fmgr_wanprof_system_sdwan_service_module.md#synopsis)
- [Parameters](fmgr_wanprof_system_sdwan_service_module.md#parameters)
- [Notes](fmgr_wanprof_system_sdwan_service_module.md#notes)
- [Examples](fmgr_wanprof_system_sdwan_service_module.md#examples)
- [Return Values](fmgr_wanprof_system_sdwan_service_module.md#return-values)

## [Synopsis](fmgr_wanprof_system_sdwan_service_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_wanprof_system_sdwan_service_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **wanprof**  string / required | the parameter (wanprof) in requested url |
| **wanprof_system_sdwan_service**  dictionary | the top level parameters set |
| **addr-mode**  string | Address mode  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **agent-exclusive**  string | Set/unset the service as agent use exclusively.  **Choices:**   - `"disable"` - `"enable"` |
| **bandwidth-weight**  integer | Coefficient of reciprocal of available bidirectional bandwidth in the formula of custom-profile-1. |
| **default**  string | Enable/disable use of SD-WAN as default service.  **Choices:**   - `"disable"` - `"enable"` |
| **dscp-forward**  string | Enable/disable forward traffic DSCP tag.  **Choices:**   - `"disable"` - `"enable"` |
| **dscp-forward-tag**  string | Forward traffic DSCP tag. |
| **dscp-reverse**  string | Enable/disable reverse traffic DSCP tag.  **Choices:**   - `"disable"` - `"enable"` |
| **dscp-reverse-tag**  string | Reverse traffic DSCP tag. |
| **dst**  any | (list or str) Destination address name. |
| **dst-negate**  string | Enable/disable negation of destination address match.  **Choices:**   - `"disable"` - `"enable"` |
| **dst6**  any | (list or str) Destination address6 name. |
| **end-port**  integer | End destination port number. |
| **end-src-port**  integer | End source port number. |
| **gateway**  string | Enable/disable SD-WAN service gateway.  **Choices:**   - `"disable"` - `"enable"` |
| **groups**  any | (list or str) User groups. |
| **hash-mode**  string | Hash algorithm for selected priority members for load balance mode.  **Choices:**   - `"round-robin"` - `"source-ip-based"` - `"source-dest-ip-based"` - `"inbandwidth"` - `"outbandwidth"` - `"bibandwidth"` |
| **health-check**  any | (list or str) Health check list. |
| **hold-down-time**  integer | Waiting period in seconds when switching from the back-up member to the primary member |
| **id**  integer / required | SD-WAN rule ID |
| **input-device**  any | (list or str) Source interface name. |
| **input-device-negate**  string | Enable/disable negation of input device match.  **Choices:**   - `"disable"` - `"enable"` |
| **input-zone**  any | (list) no description |
| **internet-service**  string | Enable/disable use of Internet service for application-based load balancing.  **Choices:**   - `"disable"` - `"enable"` |
| **internet-service-app-ctrl**  any | (list) no description |
| **internet-service-app-ctrl-category**  any | (list) no description |
| **internet-service-app-ctrl-group**  any | (list or str) Application control based Internet Service group list. |
| **internet-service-custom**  any | (list or str) Custom Internet service name list. |
| **internet-service-custom-group**  any | (list or str) Custom Internet Service group list. |
| **internet-service-group**  any | (list or str) Internet Service group list. |
| **internet-service-name**  any | (list or str) Internet service name list. |
| **jitter-weight**  integer | Coefficient of jitter in the formula of custom-profile-1. |
| **latency-weight**  integer | Coefficient of latency in the formula of custom-profile-1. |
| **link-cost-factor**  string | Link cost factor.  **Choices:**   - `"latency"` - `"jitter"` - `"packet-loss"` - `"inbandwidth"` - `"outbandwidth"` - `"bibandwidth"` - `"custom-profile-1"` |
| **link-cost-threshold**  integer | Percentage threshold change of link cost values that will result in policy route regeneration |
| **load-balance**  string | Enable/disable load-balance.  **Choices:**   - `"disable"` - `"enable"` |
| **minimum-sla-meet-members**  integer | Minimum number of members which meet SLA. |
| **mode**  string | Control how the SD-WAN rule sets the priority of interfaces in the SD-WAN.  **Choices:**   - `"auto"` - `"manual"` - `"priority"` - `"sla"` - `"load-balance"` |
| **name**  string | SD-WAN rule name. |
| **packet-loss-weight**  integer | Coefficient of packet-loss in the formula of custom-profile-1. |
| **passive-measurement**  string | Enable/disable passive measurement based on the service criteria.  **Choices:**   - `"disable"` - `"enable"` |
| **priority-members**  any | (list or str) Member sequence number list. |
| **priority-zone**  any | (list or str) no description |
| **protocol**  integer | Protocol number. |
| **quality-link**  integer | Quality grade. |
| **role**  string | Service role to work with neighbor.  **Choices:**   - `"primary"` - `"secondary"` - `"standalone"` |
| **route-tag**  integer | IPv4 route map route-tag. |
| **shortcut**  string | Enable/disable shortcut for this service.  **Choices:**   - `"disable"` - `"enable"` |
| **shortcut-stickiness**  string | Enable/disable shortcut-stickiness of ADVPN.  **Choices:**   - `"disable"` - `"enable"` |
| **sla**  list / elements=dictionary | no description |
| **health-check**  string | SD-WAN health-check. |
| **id**  integer | SLA ID. |
| **sla-compare-method**  string | Method to compare SLA value for SLA mode.  **Choices:**   - `"order"` - `"number"` |
| **sla-stickiness**  string | Enable/disable SLA stickiness  **Choices:**   - `"disable"` - `"enable"` |
| **src**  any | (list or str) Source address name. |
| **src-negate**  string | Enable/disable negation of source address match.  **Choices:**   - `"disable"` - `"enable"` |
| **src6**  any | (list or str) Source address6 name. |
| **standalone-action**  string | Enable/disable service when selected neighbor role is standalone while service role is not standalone.  **Choices:**   - `"disable"` - `"enable"` |
| **start-port**  integer | Start destination port number. |
| **start-src-port**  integer | Start source port number. |
| **status**  string | Enable/disable SD-WAN service.  **Choices:**   - `"disable"` - `"enable"` |
| **tie-break**  string | Method of selecting member if more than one meets the SLA.  **Choices:**   - `"zone"` - `"cfg-order"` - `"fib-best-match"` - `"input-device"` |
| **tos**  string | Type of service bit pattern. |
| **tos-mask**  string | Type of service evaluated bits. |
| **use-shortcut-sla**  string | Enable/disable use of ADVPN shortcut for quality comparison.  **Choices:**   - `"disable"` - `"enable"` |
| **users**  any | (list or str) User name. |
| **zone-mode**  string | Enable/disable zone mode.  **Choices:**   - `"disable"` - `"enable"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_wanprof_system_sdwan_service_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_wanprof_system_sdwan_service_module.md#id4)

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
    - name: Create SD-WAN rules
      fmgr_wanprof_system_sdwan_service:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        wanprof: <your own value>
        state: <value in [present, absent]>
        wanprof_system_sdwan_service:
          addr-mode: <value in [ipv4, ipv6]>
          bandwidth-weight: <integer>
          default: <value in [disable, enable]>
          dscp-forward: <value in [disable, enable]>
          dscp-forward-tag: <string>
          dscp-reverse: <value in [disable, enable]>
          dscp-reverse-tag: <string>
          dst: <list or string>
          dst-negate: <value in [disable, enable]>
          dst6: <list or string>
          end-port: <integer>
          gateway: <value in [disable, enable]>
          groups: <list or string>
          hash-mode: <value in [round-robin, source-ip-based, source-dest-ip-based, ...]>
          health-check: <list or string>
          hold-down-time: <integer>
          id: <integer>
          input-device: <list or string>
          input-device-negate: <value in [disable, enable]>
          internet-service: <value in [disable, enable]>
          internet-service-app-ctrl: <list or integer>
          internet-service-app-ctrl-group: <list or string>
          internet-service-custom: <list or string>
          internet-service-custom-group: <list or string>
          internet-service-group: <list or string>
          internet-service-name: <list or string>
          jitter-weight: <integer>
          latency-weight: <integer>
          link-cost-factor: <value in [latency, jitter, packet-loss, ...]>
          link-cost-threshold: <integer>
          minimum-sla-meet-members: <integer>
          mode: <value in [auto, manual, priority, ...]>
          name: <string>
          packet-loss-weight: <integer>
          priority-members: <list or string>
          protocol: <integer>
          quality-link: <integer>
          role: <value in [primary, secondary, standalone]>
          route-tag: <integer>
          sla:
            -
              health-check: <string>
              id: <integer>
          sla-compare-method: <value in [order, number]>
          src: <list or string>
          src-negate: <value in [disable, enable]>
          src6: <list or string>
          standalone-action: <value in [disable, enable]>
          start-port: <integer>
          status: <value in [disable, enable]>
          tos: <string>
          tos-mask: <string>
          users: <list or string>
          tie-break: <value in [zone, cfg-order, fib-best-match, ...]>
          use-shortcut-sla: <value in [disable, enable]>
          input-zone: <list or string>
          internet-service-app-ctrl-category: <list or integer>
          passive-measurement: <value in [disable, enable]>
          priority-zone: <list or string>
          agent-exclusive: <value in [disable, enable]>
          shortcut: <value in [disable, enable]>
          shortcut-stickiness: <value in [disable, enable]>
          end-src-port: <integer>
          load-balance: <value in [disable, enable]>
          sla-stickiness: <value in [disable, enable]>
          start-src-port: <integer>
          zone-mode: <value in [disable, enable]>
```

## [Return Values](fmgr_wanprof_system_sdwan_service_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meta**  dictionary | The result of the request.  **Returned:** always |
| **request_url**  string | The full url requested.  **Returned:** always  **Sample:** `"/sys/login/user"` |
| **response_code**  integer | The status of api request.  **Returned:** always  **Sample:** `0` |
| **response_data**  list / elements=string | The api response.  **Returned:** always |
| **response_message**  string | The descriptive message of the api response.  **Returned:** always  **Sample:** `"OK."` |
| **system_information**  dictionary | The information of the target system.  **Returned:** always |
| **rc**  integer | The status the request.  **Returned:** always  **Sample:** `0` |
| **version_check_warning**  list / elements=string | Warning if the parameters used in the playbook are not supported by the current FortiManager version.  **Returned:** complex |

### Authors

- Xinwei Du (@dux-fortinet)
- Xing Li (@lix-fortinet)
- Jie Xue (@JieX19)
- Link Zheng (@chillancezen)
- Frank Shen (@fshen01)
- Hongbin Lu (@fgtdev-hblu)

### Collection links

- [Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/issues)
- [Homepage](https://fortinet.com)
- [Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection)
