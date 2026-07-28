---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_switchcontroller_managedswitch_ports module – Managed-switch port list."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_switchcontroller_managedswitch_ports_module.html
fetched_at: 2026-07-28T02:17:24+00:00
---
# fortinet.fortimanager.fmgr_switchcontroller_managedswitch_ports module – Managed-switch port list.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_switchcontroller_managedswitch_ports`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_switchcontroller_managedswitch_ports_module.md#synopsis)
- [Parameters](fmgr_switchcontroller_managedswitch_ports_module.md#parameters)
- [Notes](fmgr_switchcontroller_managedswitch_ports_module.md#notes)
- [Examples](fmgr_switchcontroller_managedswitch_ports_module.md#examples)
- [Return Values](fmgr_switchcontroller_managedswitch_ports_module.md#return-values)

## [Synopsis](fmgr_switchcontroller_managedswitch_ports_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_switchcontroller_managedswitch_ports_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **managed-switch**  string / required | the parameter (managed-switch) in requested url |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **switchcontroller_managedswitch_ports**  dictionary | the top level parameters set |
| **access-mode**  string | Access mode of the port.  **Choices:**   - `"normal"` - `"nac"` - `"dynamic"` - `"static"` |
| **acl-group**  any | (list) no description |
| **aggregator-mode**  string | LACP member select mode.  **Choices:**   - `"bandwidth"` - `"count"` |
| **allowed-vlans**  any | (list or str) Configure switch port tagged vlans |
| **allowed-vlans-all**  string | Enable/disable all defined vlans on this port.  **Choices:**   - `"disable"` - `"enable"` |
| **arp-inspection-trust**  string | Trusted or untrusted dynamic ARP inspection.  **Choices:**   - `"untrusted"` - `"trusted"` |
| **authenticated-port**  integer | no description |
| **bundle**  string | Enable/disable Link Aggregation Group  **Choices:**   - `"disable"` - `"enable"` |
| **description**  string | Description for port. |
| **dhcp-snoop-option82-override**  list / elements=dictionary | no description |
| **circuit-id**  string | Circuit ID string. |
| **remote-id**  string | Remote ID string. |
| **vlan-name**  string | DHCP snooping option 82 VLAN. |
| **dhcp-snoop-option82-trust**  string | Enable/disable allowance of DHCP with option-82 on untrusted interface.  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp-snooping**  string | Trusted or untrusted DHCP-snooping interface.  **Choices:**   - `"trusted"` - `"untrusted"` |
| **discard-mode**  string | Configure discard mode for port.  **Choices:**   - `"none"` - `"all-untagged"` - `"all-tagged"` |
| **dot1x-enable**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **dsl-profile**  string | DSL policy configuration. |
| **edge-port**  string | Enable/disable this interface as an edge port, bridging connections between workstations and/or computers.  **Choices:**   - `"disable"` - `"enable"` |
| **encrypted-port**  integer | no description |
| **export-to-pool-flag**  integer | Switch controller export port to pool-list. |
| **fec-capable**  integer | FEC capable. |
| **fec-state**  string | State of forward error correction.  **Choices:**   - `"disabled"` - `"cl74"` - `"cl91"` |
| **flap-duration**  integer | Period over which flap events are calculated |
| **flap-rate**  integer | Number of stage change events needed within flap-duration. |
| **flap-timeout**  integer | Flap guard disabling protection |
| **flapguard**  string | Enable/disable flap guard.  **Choices:**   - `"disable"` - `"enable"` |
| **flow-control**  string | Flow control direction.  **Choices:**   - `"disable"` - `"tx"` - `"rx"` - `"both"` |
| **fortiswitch-acls**  any | (list) no description |
| **igmp-snooping**  string | Set IGMP snooping mode for the physical port interface.  **Choices:**   - `"disable"` - `"enable"` |
| **igmp-snooping-flood-reports**  string | Enable/disable flooding of IGMP reports to this interface when igmp-snooping enabled.  **Choices:**   - `"disable"` - `"enable"` |
| **igmps-flood-reports**  string | Enable/disable flooding of IGMP reports to this interface when igmp-snooping enabled.  **Choices:**   - `"disable"` - `"enable"` |
| **igmps-flood-traffic**  string | Enable/disable flooding of IGMP snooping traffic to this interface.  **Choices:**   - `"disable"` - `"enable"` |
| **interface-tags**  any | (list or str) no description |
| **ip-source-guard**  string | Enable/disable IP source guard.  **Choices:**   - `"disable"` - `"enable"` |
| **isl-peer-device-sn**  string | no description |
| **lacp-speed**  string | end Link Aggregation Control Protocol  **Choices:**   - `"slow"` - `"fast"` |
| **learning-limit**  integer | Limit the number of dynamic MAC addresses on this Port |
| **link-status**  string | no description  **Choices:**   - `"down"` - `"up"` |
| **lldp-profile**  string | LLDP port TLV profile. |
| **lldp-status**  string | LLDP transmit and receive status.  **Choices:**   - `"disable"` - `"rx-only"` - `"tx-only"` - `"tx-rx"` |
| **loop-guard**  string | Enable/disable loop-guard on this interface, an STP optimization used to prevent network loops.  **Choices:**   - `"disabled"` - `"enabled"` |
| **loop-guard-timeout**  integer | Loop-guard timeout |
| **mac-addr**  string | Port/Trunk MAC. |
| **matched-dpp-intf-tags**  string | Matched interface tags in the dynamic port policy. |
| **matched-dpp-policy**  string | Matched child policy in the dynamic port policy. |
| **max-bundle**  integer | Maximum size of LAG bundle |
| **max-miss-heartbeats**  integer | Maximum tolerant missed heartbeats. |
| **mcast-snooping-flood-traffic**  string | Enable/disable flooding of IGMP snooping traffic to this interface.  **Choices:**   - `"disable"` - `"enable"` |
| **mclag**  string | Enable/disable multi-chassis link aggregation  **Choices:**   - `"disable"` - `"enable"` |
| **mclag-icl-port**  integer | no description |
| **media-type**  string | no description |
| **member-withdrawal-behavior**  string | Port behavior after it withdraws because of loss of control packets.  **Choices:**   - `"forward"` - `"block"` |
| **members**  any | (list) no description |
| **min-bundle**  integer | Minimum size of LAG bundle |
| **mode**  string | LACP mode  **Choices:**   - `"static"` - `"lacp-passive"` - `"lacp-active"` |
| **p2p-port**  integer | no description |
| **packet-sample-rate**  integer | Packet sampling rate |
| **packet-sampler**  string | Enable/disable packet sampling on this interface.  **Choices:**   - `"disabled"` - `"enabled"` |
| **pause-meter**  integer | Configure ingress pause metering rate, in kbps |
| **pause-meter-resume**  string | Resume threshold for resuming traffic on ingress port.  **Choices:**   - `"25%"` - `"50%"` - `"75%"` |
| **poe-max-power**  string | no description |
| **poe-mode-bt-cabable**  integer | PoE mode IEEE 802. |
| **poe-port-mode**  string | Configure PoE port mode.  **Choices:**   - `"ieee802-3af"` - `"ieee802-3at"` - `"ieee802-3bt"` |
| **poe-port-power**  string | Configure PoE port power.  **Choices:**   - `"normal"` - `"perpetual"` - `"perpetual-fast"` |
| **poe-port-priority**  string | Configure PoE port priority.  **Choices:**   - `"critical-priority"` - `"high-priority"` - `"low-priority"` - `"medium-priority"` |
| **poe-pre-standard-detection**  string | Enable/disable PoE pre-standard detection.  **Choices:**   - `"disable"` - `"enable"` |
| **poe-standard**  string | no description |
| **poe-status**  string | Enable/disable PoE status.  **Choices:**   - `"disable"` - `"enable"` |
| **port-name**  string / required | Switch port name. |
| **port-owner**  string | Switch port name. |
| **port-policy**  string | Switch controller dynamic port policy from available options. |
| **port-security-policy**  string | Switch controller authentication policy to apply to this managed switch from available options. |
| **port-selection-criteria**  string | Algorithm for aggregate port selection.  **Choices:**   - `"src-mac"` - `"dst-mac"` - `"src-dst-mac"` - `"src-ip"` - `"dst-ip"` - `"src-dst-ip"` |
| **ptp-status**  string | Enable/disable PTP policy on this FortiSwitch port.  **Choices:**   - `"disable"` - `"enable"` |
| **qos-policy**  string | Switch controller QoS policy from available options. |
| **restricted-auth-port**  integer | no description |
| **rpvst-port**  string | Enable/disable inter-operability with rapid PVST on this interface.  **Choices:**   - `"disabled"` - `"enabled"` |
| **sample-direction**  string | sFlow sample direction.  **Choices:**   - `"rx"` - `"tx"` - `"both"` |
| **sflow-counter-interval**  integer | sFlow sampler counter polling interval |
| **sflow-sample-rate**  integer | sFlow sampler sample rate |
| **sflow-sampler**  string | Enable/disable sFlow protocol on this interface.  **Choices:**   - `"disabled"` - `"enabled"` |
| **status**  string | Switch port admin status  **Choices:**   - `"down"` - `"up"` |
| **sticky-mac**  string | Enable or disable sticky-mac on the interface.  **Choices:**   - `"disable"` - `"enable"` |
| **storm-control-policy**  string | Switch controller storm control policy from available options. |
| **stp-bpdu-guard**  string | Enable/disable STP BPDU guard on this interface.  **Choices:**   - `"disabled"` - `"enabled"` |
| **stp-bpdu-guard-timeout**  integer | BPDU Guard disabling protection |
| **stp-root-guard**  string | Enable/disable STP root guard on this interface.  **Choices:**   - `"disabled"` - `"enabled"` |
| **stp-state**  string | Enable/disable Spanning Tree Protocol  **Choices:**   - `"disabled"` - `"enabled"` |
| **trunk-member**  integer | Trunk member. |
| **type**  string | Interface type  **Choices:**   - `"physical"` - `"trunk"` |
| **untagged-vlans**  any | (list or str) Configure switch port untagged vlans |
| **vlan**  string | Assign switch ports to a VLAN. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_switchcontroller_managedswitch_ports_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_switchcontroller_managedswitch_ports_module.md#id4)

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
    - name: Managed-switch port list.
      fmgr_switchcontroller_managedswitch_ports:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        managed-switch: <your own value>
        state: <value in [present, absent]>
        switchcontroller_managedswitch_ports:
          allowed-vlans: <list or string>
          allowed-vlans-all: <value in [disable, enable]>
          arp-inspection-trust: <value in [untrusted, trusted]>
          bundle: <value in [disable, enable]>
          description: <string>
          dhcp-snoop-option82-trust: <value in [disable, enable]>
          dhcp-snooping: <value in [trusted, untrusted]>
          discard-mode: <value in [none, all-untagged, all-tagged]>
          edge-port: <value in [disable, enable]>
          igmp-snooping: <value in [disable, enable]>
          igmps-flood-reports: <value in [disable, enable]>
          igmps-flood-traffic: <value in [disable, enable]>
          lacp-speed: <value in [slow, fast]>
          learning-limit: <integer>
          lldp-profile: <string>
          lldp-status: <value in [disable, rx-only, tx-only, ...]>
          loop-guard: <value in [disabled, enabled]>
          loop-guard-timeout: <integer>
          max-bundle: <integer>
          mclag: <value in [disable, enable]>
          member-withdrawal-behavior: <value in [forward, block]>
          members: <list or string>
          min-bundle: <integer>
          mode: <value in [static, lacp-passive, lacp-active]>
          poe-pre-standard-detection: <value in [disable, enable]>
          poe-status: <value in [disable, enable]>
          port-name: <string>
          port-owner: <string>
          port-security-policy: <string>
          port-selection-criteria: <value in [src-mac, dst-mac, src-dst-mac, ...]>
          qos-policy: <string>
          sample-direction: <value in [rx, tx, both]>
          sflow-counter-interval: <integer>
          sflow-sample-rate: <integer>
          sflow-sampler: <value in [disabled, enabled]>
          stp-bpdu-guard: <value in [disabled, enabled]>
          stp-bpdu-guard-timeout: <integer>
          stp-root-guard: <value in [disabled, enabled]>
          stp-state: <value in [disabled, enabled]>
          type: <value in [physical, trunk]>
          untagged-vlans: <list or string>
          vlan: <string>
          export-to-pool-flag: <integer>
          mac-addr: <string>
          packet-sample-rate: <integer>
          packet-sampler: <value in [disabled, enabled]>
          sticky-mac: <value in [disable, enable]>
          storm-control-policy: <string>
          dot1x-enable: <value in [disable, enable]>
          max-miss-heartbeats: <integer>
          access-mode: <value in [normal, nac, dynamic, ...]>
          ip-source-guard: <value in [disable, enable]>
          mclag-icl-port: <integer>
          p2p-port: <integer>
          aggregator-mode: <value in [bandwidth, count]>
          rpvst-port: <value in [disabled, enabled]>
          flow-control: <value in [disable, tx, rx, ...]>
          media-type: <string>
          pause-meter: <integer>
          pause-meter-resume: <value in [25%, 50%, 75%]>
          trunk-member: <integer>
          fec-capable: <integer>
          fec-state: <value in [disabled, cl74, cl91]>
          matched-dpp-intf-tags: <string>
          matched-dpp-policy: <string>
          port-policy: <string>
          status: <value in [down, up]>
          dsl-profile: <string>
          flap-duration: <integer>
          flap-rate: <integer>
          flap-timeout: <integer>
          flapguard: <value in [disable, enable]>
          interface-tags: <list or string>
          poe-max-power: <string>
          poe-standard: <string>
          igmp-snooping-flood-reports: <value in [disable, enable]>
          mcast-snooping-flood-traffic: <value in [disable, enable]>
          link-status: <value in [down, up]>
          poe-mode-bt-cabable: <integer>
          poe-port-mode: <value in [ieee802-3af, ieee802-3at, ieee802-3bt]>
          poe-port-power: <value in [normal, perpetual, perpetual-fast]>
          poe-port-priority: <value in [critical-priority, high-priority, low-priority, ...]>
          acl-group: <list or string>
          dhcp-snoop-option82-override:
            -
              circuit-id: <string>
              remote-id: <string>
              vlan-name: <string>
          fortiswitch-acls: <list or integer>
          isl-peer-device-sn: <string>
          authenticated-port: <integer>
          encrypted-port: <integer>
          ptp-status: <value in [disable, enable]>
          restricted-auth-port: <integer>
```

## [Return Values](fmgr_switchcontroller_managedswitch_ports_module.md#id5)

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
