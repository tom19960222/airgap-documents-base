---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_wtpprofile_radio2 module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_wtpprofile_radio2_module.html
fetched_at: 2026-07-27T17:39:45+00:00
---
# fortinet.fortimanager.fmgr_wtpprofile_radio2 module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_wtpprofile_radio2`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_wtpprofile_radio2_module.md#synopsis)
- [Parameters](fmgr_wtpprofile_radio2_module.md#parameters)
- [Notes](fmgr_wtpprofile_radio2_module.md#notes)
- [Examples](fmgr_wtpprofile_radio2_module.md#examples)
- [Return Values](fmgr_wtpprofile_radio2_module.md#return-values)

## [Synopsis](fmgr_wtpprofile_radio2_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_wtpprofile_radio2_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |
| **wtp-profile**  string / required | the parameter (wtp-profile) in requested url |
| **wtpprofile_radio2**  dictionary | the top level parameters set |
| **airtime-fairness**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **amsdu**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ap-handoff**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ap-sniffer-addr**  string | no description |
| **ap-sniffer-bufsize**  integer | no description |
| **ap-sniffer-chan**  integer | no description |
| **ap-sniffer-ctl**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ap-sniffer-data**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ap-sniffer-mgmt-beacon**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ap-sniffer-mgmt-other**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ap-sniffer-mgmt-probe**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **arrp-profile**  string | no description |
| **auto-power-high**  integer | no description |
| **auto-power-level**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **auto-power-low**  integer | no description |
| **auto-power-target**  string | no description |
| **band**  string | no description  Choices:   - `"802.11b"` - `"802.11a"` - `"802.11g"` - `"802.11n"` - `"802.11ac"` - `"802.11n-5G"` - `"802.11g-only"` - `"802.11n-only"` - `"802.11n,g-only"` - `"802.11ac-only"` - `"802.11ac,n-only"` - `"802.11n-5G-only"` - `"802.11ax-5G"` - `"802.11ax"` - `"802.11ax-5G-only"` - `"802.11ax,ac-only"` - `"802.11ax,ac,n-only"` - `"802.11ax-only"` - `"802.11ax,n-only"` - `"802.11ax,n,g-only"` - `"802.11ac-2G"` |
| **band-5g-type**  string | no description  Choices:   - `"5g-full"` - `"5g-high"` - `"5g-low"` |
| **bandwidth-admission-control**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **bandwidth-capacity**  integer | no description |
| **beacon-interval**  integer | no description |
| **bss-color**  integer | no description |
| **bss-color-mode**  string | no description  Choices:   - `"auto"` - `"static"` |
| **call-admission-control**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **call-capacity**  integer | no description |
| **channel**  string | description |
| **channel-bonding**  string | no description  Choices:   - `"disable"` - `"enable"` - `"80MHz"` - `"40MHz"` - `"20MHz"` - `"160MHz"` |
| **channel-utilization**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **coexistence**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **darrp**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **drma**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **drma-sensitivity**  string | no description  Choices:   - `"low"` - `"medium"` - `"high"` |
| **dtim**  integer | no description |
| **frag-threshold**  integer | no description |
| **frequency-handoff**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **iperf-protocol**  string | no description  Choices:   - `"udp"` - `"tcp"` |
| **iperf-server-port**  integer | no description |
| **max-clients**  integer | no description |
| **max-distance**  integer | no description |
| **mode**  string | no description  Choices:   - `"disabled"` - `"ap"` - `"monitor"` - `"sniffer"` - `"sam"` |
| **power-level**  integer | no description |
| **power-mode**  string | no description  Choices:   - `"dBm"` - `"percentage"` |
| **power-value**  integer | no description |
| **powersave-optimize**  list / elements=string | description  Choices:   - `"tim"` - `"ac-vo"` - `"no-obss-scan"` - `"no-11b-rate"` - `"client-rate-follow"` |
| **protection-mode**  string | no description  Choices:   - `"rtscts"` - `"ctsonly"` - `"disable"` |
| **radio-id**  integer | no description |
| **rts-threshold**  integer | no description |
| **sam-bssid**  string | no description |
| **sam-captive-portal**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sam-cwp-failure-string**  string | no description |
| **sam-cwp-match-string**  string | no description |
| **sam-cwp-password**  string | description |
| **sam-cwp-success-string**  string | no description |
| **sam-cwp-test-url**  string | no description |
| **sam-cwp-username**  string | no description |
| **sam-password**  string | description |
| **sam-report-intv**  integer | no description |
| **sam-security-type**  string | no description  Choices:   - `"open"` - `"wpa-personal"` - `"wpa-enterprise"` |
| **sam-server**  string | no description |
| **sam-server-fqdn**  string | no description |
| **sam-server-ip**  string | no description |
| **sam-server-type**  string | no description  Choices:   - `"ip"` - `"fqdn"` |
| **sam-ssid**  string | no description |
| **sam-test**  string | no description  Choices:   - `"ping"` - `"iperf"` |
| **sam-username**  string | no description |
| **short-guard-interval**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **spectrum-analysis**  string | no description  Choices:   - `"disable"` - `"enable"` - `"scan-only"` |
| **transmit-optimize**  list / elements=string | description  Choices:   - `"disable"` - `"power-save"` - `"aggr-limit"` - `"retry-limit"` - `"send-bar"` |
| **vap-all**  string | no description  Choices:   - `"disable"` - `"enable"` - `"tunnel"` - `"bridge"` - `"manual"` |
| **vap1**  string | no description |
| **vap2**  string | no description |
| **vap3**  string | no description |
| **vap4**  string | no description |
| **vap5**  string | no description |
| **vap6**  string | no description |
| **vap7**  string | no description |
| **vap8**  string | no description |
| **vaps**  string | no description |
| **wids-profile**  string | no description |
| **zero-wait-dfs**  string | no description  Choices:   - `"disable"` - `"enable"` |

## [Notes](fmgr_wtpprofile_radio2_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_wtpprofile_radio2_module.md#id4)

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
     fmgr_wtpprofile_radio2:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        wtp-profile: <your own value>
        wtpprofile_radio2:
           amsdu: <value in [disable, enable]>
           ap-handoff: <value in [disable, enable]>
           ap-sniffer-addr: <value of string>
           ap-sniffer-bufsize: <value of integer>
           ap-sniffer-chan: <value of integer>
           ap-sniffer-ctl: <value in [disable, enable]>
           ap-sniffer-data: <value in [disable, enable]>
           ap-sniffer-mgmt-beacon: <value in [disable, enable]>
           ap-sniffer-mgmt-other: <value in [disable, enable]>
           ap-sniffer-mgmt-probe: <value in [disable, enable]>
           auto-power-high: <value of integer>
           auto-power-level: <value in [disable, enable]>
           auto-power-low: <value of integer>
           band: <value in [802.11b, 802.11a, 802.11g, ...]>
           bandwidth-admission-control: <value in [disable, enable]>
           bandwidth-capacity: <value of integer>
           beacon-interval: <value of integer>
           call-admission-control: <value in [disable, enable]>
           call-capacity: <value of integer>
           channel: <value of string>
           channel-bonding: <value in [disable, enable, 80MHz, ...]>
           channel-utilization: <value in [disable, enable]>
           coexistence: <value in [disable, enable]>
           darrp: <value in [disable, enable]>
           dtim: <value of integer>
           frag-threshold: <value of integer>
           frequency-handoff: <value in [disable, enable]>
           max-clients: <value of integer>
           max-distance: <value of integer>
           mode: <value in [disabled, ap, monitor, ...]>
           power-level: <value of integer>
           powersave-optimize:
             - tim
             - ac-vo
             - no-obss-scan
             - no-11b-rate
             - client-rate-follow
           protection-mode: <value in [rtscts, ctsonly, disable]>
           radio-id: <value of integer>
           rts-threshold: <value of integer>
           short-guard-interval: <value in [disable, enable]>
           spectrum-analysis: <value in [disable, enable, scan-only]>
           transmit-optimize:
             - disable
             - power-save
             - aggr-limit
             - retry-limit
             - send-bar
           vap-all: <value in [disable, enable, tunnel, ...]>
           vaps: <value of string>
           wids-profile: <value of string>
           airtime-fairness: <value in [disable, enable]>
           band-5g-type: <value in [5g-full, 5g-high, 5g-low]>
           zero-wait-dfs: <value in [disable, enable]>
           vap1: <value of string>
           vap2: <value of string>
           vap3: <value of string>
           vap4: <value of string>
           vap5: <value of string>
           vap6: <value of string>
           vap7: <value of string>
           vap8: <value of string>
           bss-color: <value of integer>
           auto-power-target: <value of string>
           drma: <value in [disable, enable]>
           drma-sensitivity: <value in [low, medium, high]>
           iperf-protocol: <value in [udp, tcp]>
           iperf-server-port: <value of integer>
           power-mode: <value in [dBm, percentage]>
           power-value: <value of integer>
           sam-bssid: <value of string>
           sam-captive-portal: <value in [disable, enable]>
           sam-password: <value of string>
           sam-report-intv: <value of integer>
           sam-security-type: <value in [open, wpa-personal, wpa-enterprise]>
           sam-server: <value of string>
           sam-ssid: <value of string>
           sam-test: <value in [ping, iperf]>
           sam-username: <value of string>
           arrp-profile: <value of string>
           bss-color-mode: <value in [auto, static]>
           sam-cwp-failure-string: <value of string>
           sam-cwp-match-string: <value of string>
           sam-cwp-password: <value of string>
           sam-cwp-success-string: <value of string>
           sam-cwp-test-url: <value of string>
           sam-cwp-username: <value of string>
           sam-server-fqdn: <value of string>
           sam-server-ip: <value of string>
           sam-server-type: <value in [ip, fqdn]>
```

## [Return Values](fmgr_wtpprofile_radio2_module.md#id5)

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
