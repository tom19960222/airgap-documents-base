---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_wtpprofile_radio3 module – Configuration options for radio 3."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_wtpprofile_radio3_module.html
fetched_at: 2026-07-28T02:23:11+00:00
---
# fortinet.fortimanager.fmgr_wtpprofile_radio3 module – Configuration options for radio 3.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_wtpprofile_radio3`.

New in fortinet.fortimanager 2.1.0

- [Synopsis](fmgr_wtpprofile_radio3_module.md#synopsis)
- [Parameters](fmgr_wtpprofile_radio3_module.md#parameters)
- [Notes](fmgr_wtpprofile_radio3_module.md#notes)
- [Examples](fmgr_wtpprofile_radio3_module.md#examples)
- [Return Values](fmgr_wtpprofile_radio3_module.md#return-values)

## [Synopsis](fmgr_wtpprofile_radio3_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_wtpprofile_radio3_module.md#id2)

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
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |
| **wtp-profile**  string / required | the parameter (wtp-profile) in requested url |
| **wtpprofile_radio3**  dictionary | the top level parameters set |
| **80211d**  string | Enable/disable 802.  **Choices:**   - `"disable"` - `"enable"` |
| **airtime-fairness**  string | Enable/disable airtime fairness  **Choices:**   - `"disable"` - `"enable"` |
| **amsdu**  string | Enable/disable 802.  **Choices:**   - `"disable"` - `"enable"` |
| **ap-handoff**  string | Enable/disable AP handoff of clients to other APs  **Choices:**   - `"disable"` - `"enable"` |
| **ap-sniffer-addr**  string | MAC address to monitor. |
| **ap-sniffer-bufsize**  integer | Sniffer buffer size |
| **ap-sniffer-chan**  integer | Channel on which to operate the sniffer |
| **ap-sniffer-ctl**  string | Enable/disable sniffer on WiFi control frame  **Choices:**   - `"disable"` - `"enable"` |
| **ap-sniffer-data**  string | Enable/disable sniffer on WiFi data frame  **Choices:**   - `"disable"` - `"enable"` |
| **ap-sniffer-mgmt-beacon**  string | Enable/disable sniffer on WiFi management Beacon frames  **Choices:**   - `"disable"` - `"enable"` |
| **ap-sniffer-mgmt-other**  string | Enable/disable sniffer on WiFi management other frames  **Choices:**   - `"disable"` - `"enable"` |
| **ap-sniffer-mgmt-probe**  string | Enable/disable sniffer on WiFi management probe frames  **Choices:**   - `"disable"` - `"enable"` |
| **arrp-profile**  string | Distributed Automatic Radio Resource Provisioning |
| **auto-power-high**  integer | The upper bound of automatic transmit power adjustment in dBm |
| **auto-power-level**  string | Enable/disable automatic power-level adjustment to prevent co-channel interference  **Choices:**   - `"disable"` - `"enable"` |
| **auto-power-low**  integer | The lower bound of automatic transmit power adjustment in dBm |
| **auto-power-target**  string | The target of automatic transmit power adjustment in dBm. |
| **band**  string | WiFi band that Radio 3 operates on.  **Choices:**   - `"802.11b"` - `"802.11a"` - `"802.11g"` - `"802.11n"` - `"802.11ac"` - `"802.11n-5G"` - `"802.11ax-5G"` - `"802.11ax"` - `"802.11g-only"` - `"802.11n-only"` - `"802.11n,g-only"` - `"802.11ac-only"` - `"802.11ac,n-only"` - `"802.11n-5G-only"` - `"802.11ax-5G-only"` - `"802.11ax,ac-only"` - `"802.11ax,ac,n-only"` - `"802.11ax-only"` - `"802.11ax,n-only"` - `"802.11ax,n,g-only"` - `"802.11ac-2G"` - `"802.11ax-6G"` |
| **band-5g-type**  string | WiFi 5G band type.  **Choices:**   - `"5g-full"` - `"5g-high"` - `"5g-low"` |
| **bandwidth-admission-control**  string | Enable/disable WiFi multimedia  **Choices:**   - `"disable"` - `"enable"` |
| **bandwidth-capacity**  integer | Maximum bandwidth capacity allowed |
| **beacon-interval**  integer | Beacon interval. |
| **bss-color**  integer | BSS color value for this 11ax radio |
| **bss-color-mode**  string | BSS color mode for this 11ax radio  **Choices:**   - `"auto"` - `"static"` |
| **call-admission-control**  string | Enable/disable WiFi multimedia  **Choices:**   - `"disable"` - `"enable"` |
| **call-capacity**  integer | Maximum number of Voice over WLAN |
| **channel**  any | (list) no description |
| **channel-bonding**  string | Channel bandwidth  **Choices:**   - `"80MHz"` - `"40MHz"` - `"20MHz"` - `"160MHz"` |
| **channel-utilization**  string | Enable/disable measuring channel utilization.  **Choices:**   - `"disable"` - `"enable"` |
| **coexistence**  string | Enable/disable allowing both HT20 and HT40 on the same radio  **Choices:**   - `"disable"` - `"enable"` |
| **darrp**  string | Enable/disable Distributed Automatic Radio Resource Provisioning  **Choices:**   - `"disable"` - `"enable"` |
| **drma**  string | Enable/disable dynamic radio mode assignment  **Choices:**   - `"disable"` - `"enable"` |
| **drma-sensitivity**  string | Network Coverage Factor  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **dtim**  integer | Delivery Traffic Indication Map |
| **frag-threshold**  integer | Maximum packet size that can be sent without fragmentation |
| **frequency-handoff**  string | Enable/disable frequency handoff of clients to other channels  **Choices:**   - `"disable"` - `"enable"` |
| **iperf-protocol**  string | Iperf test protocol  **Choices:**   - `"udp"` - `"tcp"` |
| **iperf-server-port**  integer | Iperf service port number. |
| **max-clients**  integer | Maximum number of stations |
| **max-distance**  integer | Maximum expected distance between the AP and clients |
| **mimo-mode**  string | Configure radio MIMO mode  **Choices:**   - `"default"` - `"1x1"` - `"2x2"` - `"3x3"` - `"4x4"` - `"8x8"` |
| **mode**  string | Mode of radio 3.  **Choices:**   - `"disabled"` - `"ap"` - `"monitor"` - `"sniffer"` - `"sam"` |
| **optional-antenna**  string | Optional antenna used on FAP  **Choices:**   - `"none"` - `"FANT-04ABGN-0606-O-N"` - `"FANT-04ABGN-1414-P-N"` - `"FANT-04ABGN-8065-P-N"` - `"FANT-04ABGN-0606-O-R"` - `"FANT-04ABGN-0606-P-R"` - `"FANT-10ACAX-1213-D-N"` - `"FANT-08ABGN-1213-D-R"` |
| **power-level**  integer | Radio power level as a percentage of the maximum transmit power |
| **power-mode**  string | Set radio effective isotropic radiated power  **Choices:**   - `"dBm"` - `"percentage"` |
| **power-value**  integer | Radio EIRP power in dBm |
| **powersave-optimize**  list / elements=string | no description  **Choices:**   - `"tim"` - `"ac-vo"` - `"no-obss-scan"` - `"no-11b-rate"` - `"client-rate-follow"` |
| **protection-mode**  string | Enable/disable 802.  **Choices:**   - `"rtscts"` - `"ctsonly"` - `"disable"` |
| **radio-id**  integer | no description |
| **rts-threshold**  integer | Maximum packet size for RTS transmissions, specifying the maximum size of a data packet before RTS/CTS |
| **sam-bssid**  string | BSSID for WiFi network. |
| **sam-captive-portal**  string | Enable/disable Captive Portal Authentication  **Choices:**   - `"disable"` - `"enable"` |
| **sam-cwp-failure-string**  string | Failure identification on the page after an incorrect login. |
| **sam-cwp-match-string**  string | Identification string from the captive portal login form. |
| **sam-cwp-password**  any | (list) no description |
| **sam-cwp-success-string**  string | Success identification on the page after a successful login. |
| **sam-cwp-test-url**  string | Website the client is trying to access. |
| **sam-cwp-username**  string | Username for captive portal authentication. |
| **sam-password**  any | (list) no description |
| **sam-report-intv**  integer | SAM report interval |
| **sam-security-type**  string | Select WiFi network security type  **Choices:**   - `"open"` - `"wpa-personal"` - `"wpa-enterprise"` |
| **sam-server**  string | SAM test server IP address or domain name. |
| **sam-server-fqdn**  string | SAM test server domain name. |
| **sam-server-ip**  string | SAM test server IP address. |
| **sam-server-type**  string | Select SAM server type  **Choices:**   - `"ip"` - `"fqdn"` |
| **sam-ssid**  string | SSID for WiFi network. |
| **sam-test**  string | Select SAM test type  **Choices:**   - `"ping"` - `"iperf"` |
| **sam-username**  string | Username for WiFi network connection. |
| **short-guard-interval**  string | Use either the short guard interval  **Choices:**   - `"disable"` - `"enable"` |
| **spectrum-analysis**  string | Enable/disable spectrum analysis to find interference that would negatively impact wireless performance.  **Choices:**   - `"disable"` - `"enable"` - `"scan-only"` |
| **transmit-optimize**  list / elements=string | no description  **Choices:**   - `"disable"` - `"power-save"` - `"aggr-limit"` - `"retry-limit"` - `"send-bar"` |
| **vap-all**  string | Enable/disable the automatic inheritance of all Virtual Access Points  **Choices:**   - `"disable"` - `"enable"` - `"tunnel"` - `"bridge"` - `"manual"` |
| **vap1**  string | Virtual Access Point |
| **vap2**  string | Virtual Access Point |
| **vap3**  string | Virtual Access Point |
| **vap4**  string | Virtual Access Point |
| **vap5**  string | Virtual Access Point |
| **vap6**  string | Virtual Access Point |
| **vap7**  string | Virtual Access Point |
| **vap8**  string | Virtual Access Point |
| **vaps**  any | (list or str) Manually selected list of Virtual Access Points |
| **wids-profile**  string | Wireless Intrusion Detection System |
| **zero-wait-dfs**  string | Enable/disable zero wait DFS on radio  **Choices:**   - `"disable"` - `"enable"` |

## [Notes](fmgr_wtpprofile_radio3_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_wtpprofile_radio3_module.md#id4)

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
    - name: Configuration options for radio 3.
      fmgr_wtpprofile_radio3:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        wtp-profile: <your own value>
        wtpprofile_radio3:
          airtime-fairness: <value in [disable, enable]>
          amsdu: <value in [disable, enable]>
          ap-handoff: <value in [disable, enable]>
          ap-sniffer-addr: <string>
          ap-sniffer-bufsize: <integer>
          ap-sniffer-chan: <integer>
          ap-sniffer-ctl: <value in [disable, enable]>
          ap-sniffer-data: <value in [disable, enable]>
          ap-sniffer-mgmt-beacon: <value in [disable, enable]>
          ap-sniffer-mgmt-other: <value in [disable, enable]>
          ap-sniffer-mgmt-probe: <value in [disable, enable]>
          auto-power-high: <integer>
          auto-power-level: <value in [disable, enable]>
          auto-power-low: <integer>
          band: <value in [802.11b, 802.11a, 802.11g, ...]>
          bandwidth-admission-control: <value in [disable, enable]>
          bandwidth-capacity: <integer>
          beacon-interval: <integer>
          call-admission-control: <value in [disable, enable]>
          call-capacity: <integer>
          channel: <list or string>
          channel-bonding: <value in [80MHz, 40MHz, 20MHz, ...]>
          channel-utilization: <value in [disable, enable]>
          coexistence: <value in [disable, enable]>
          darrp: <value in [disable, enable]>
          dtim: <integer>
          frag-threshold: <integer>
          frequency-handoff: <value in [disable, enable]>
          max-clients: <integer>
          max-distance: <integer>
          mode: <value in [disabled, ap, monitor, ...]>
          power-level: <integer>
          powersave-optimize:
            - tim
            - ac-vo
            - no-obss-scan
            - no-11b-rate
            - client-rate-follow
          protection-mode: <value in [rtscts, ctsonly, disable]>
          radio-id: <integer>
          rts-threshold: <integer>
          short-guard-interval: <value in [disable, enable]>
          spectrum-analysis: <value in [disable, enable, scan-only]>
          transmit-optimize:
            - disable
            - power-save
            - aggr-limit
            - retry-limit
            - send-bar
          vap-all: <value in [disable, enable, tunnel, ...]>
          vaps: <list or string>
          wids-profile: <string>
          band-5g-type: <value in [5g-full, 5g-high, 5g-low]>
          zero-wait-dfs: <value in [disable, enable]>
          vap1: <string>
          vap2: <string>
          vap3: <string>
          vap4: <string>
          vap5: <string>
          vap6: <string>
          vap7: <string>
          vap8: <string>
          bss-color: <integer>
          auto-power-target: <string>
          drma: <value in [disable, enable]>
          drma-sensitivity: <value in [low, medium, high]>
          iperf-protocol: <value in [udp, tcp]>
          iperf-server-port: <integer>
          power-mode: <value in [dBm, percentage]>
          power-value: <integer>
          sam-bssid: <string>
          sam-captive-portal: <value in [disable, enable]>
          sam-password: <list or string>
          sam-report-intv: <integer>
          sam-security-type: <value in [open, wpa-personal, wpa-enterprise]>
          sam-server: <string>
          sam-ssid: <string>
          sam-test: <value in [ping, iperf]>
          sam-username: <string>
          arrp-profile: <string>
          bss-color-mode: <value in [auto, static]>
          sam-cwp-failure-string: <string>
          sam-cwp-match-string: <string>
          sam-cwp-password: <list or string>
          sam-cwp-success-string: <string>
          sam-cwp-test-url: <string>
          sam-cwp-username: <string>
          sam-server-fqdn: <string>
          sam-server-ip: <string>
          sam-server-type: <value in [ip, fqdn]>
          80211d: <value in [disable, enable]>
          optional-antenna: <value in [none, FANT-04ABGN-0606-O-N, FANT-04ABGN-1414-P-N, ...]>
          mimo-mode: <value in [default, 1x1, 2x2, ...]>
```

## [Return Values](fmgr_wtpprofile_radio3_module.md#id5)

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
