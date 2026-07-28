---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_switchcontroller_managedswitch_ports module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_switchcontroller_managedswitch_ports_module.html
fetched_at: 2026-07-27T17:35:12+00:00
---
# fortinet.fortimanager.fmgr_switchcontroller_managedswitch_ports module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_switchcontroller_managedswitch_ports`.

New in fortinet.fortimanager 1.0.0

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
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **managed-switch**  string / required | the parameter (managed-switch) in requested url |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **switchcontroller_managedswitch_ports**  dictionary | the top level parameters set |
| **access-mode**  string | no description  Choices:   - `"normal"` - `"nac"` - `"dynamic"` - `"static"` |
| **aggregator-mode**  string | no description  Choices:   - `"bandwidth"` - `"count"` |
| **allowed-vlans**  string | no description |
| **allowed-vlans-all**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **arp-inspection-trust**  string | no description  Choices:   - `"untrusted"` - `"trusted"` |
| **bundle**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **description**  string | no description |
| **dhcp-snoop-option82-trust**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dhcp-snooping**  string | no description  Choices:   - `"trusted"` - `"untrusted"` |
| **discard-mode**  string | no description  Choices:   - `"none"` - `"all-untagged"` - `"all-tagged"` |
| **dsl-profile**  string | no description |
| **edge-port**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **export-to-pool-flag**  integer | no description |
| **fec-capable**  integer | no description |
| **fec-state**  string | no description  Choices:   - `"disabled"` - `"cl74"` - `"cl91"` |
| **flap-duration**  integer | no description |
| **flap-rate**  integer | no description |
| **flap-timeout**  integer | no description |
| **flapguard**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **flow-control**  string | no description  Choices:   - `"disable"` - `"tx"` - `"rx"` - `"both"` |
| **igmp-snooping**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **igmps-flood-reports**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **igmps-flood-traffic**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **interface-tags**  string | description |
| **ip-source-guard**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **lacp-speed**  string | no description  Choices:   - `"slow"` - `"fast"` |
| **learning-limit**  integer | no description |
| **lldp-profile**  string | no description |
| **lldp-status**  string | no description  Choices:   - `"disable"` - `"rx-only"` - `"tx-only"` - `"tx-rx"` |
| **loop-guard**  string | no description  Choices:   - `"disabled"` - `"enabled"` |
| **loop-guard-timeout**  integer | no description |
| **mac-addr**  string | no description |
| **matched-dpp-intf-tags**  string | no description |
| **matched-dpp-policy**  string | no description |
| **max-bundle**  integer | no description |
| **mclag**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **mclag-icl-port**  integer | no description |
| **media-type**  string | no description |
| **member-withdrawal-behavior**  string | no description  Choices:   - `"forward"` - `"block"` |
| **members**  string | description |
| **min-bundle**  integer | no description |
| **mode**  string | no description  Choices:   - `"static"` - `"lacp-passive"` - `"lacp-active"` |
| **p2p-port**  integer | no description |
| **packet-sample-rate**  integer | no description |
| **packet-sampler**  string | no description  Choices:   - `"disabled"` - `"enabled"` |
| **pause-meter**  integer | no description |
| **pause-meter-resume**  string | no description  Choices:   - `"25%"` - `"50%"` - `"75%"` |
| **poe-max-power**  string | no description |
| **poe-pre-standard-detection**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **poe-standard**  string | no description |
| **poe-status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **port-name**  string | no description |
| **port-owner**  string | no description |
| **port-policy**  string | no description |
| **port-security-policy**  string | no description |
| **port-selection-criteria**  string | no description  Choices:   - `"src-mac"` - `"dst-mac"` - `"src-dst-mac"` - `"src-ip"` - `"dst-ip"` - `"src-dst-ip"` |
| **qos-policy**  string | no description |
| **rpvst-port**  string | no description  Choices:   - `"disabled"` - `"enabled"` |
| **sample-direction**  string | no description  Choices:   - `"rx"` - `"tx"` - `"both"` |
| **sflow-counter-interval**  integer | no description |
| **sflow-sample-rate**  integer | no description |
| **sflow-sampler**  string | no description  Choices:   - `"disabled"` - `"enabled"` |
| **status**  string | no description  Choices:   - `"down"` - `"up"` |
| **sticky-mac**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **storm-control-policy**  string | no description |
| **stp-bpdu-guard**  string | no description  Choices:   - `"disabled"` - `"enabled"` |
| **stp-bpdu-guard-timeout**  integer | no description |
| **stp-root-guard**  string | no description  Choices:   - `"disabled"` - `"enabled"` |
| **stp-state**  string | no description  Choices:   - `"disabled"` - `"enabled"` |
| **trunk-member**  integer | no description |
| **type**  string | no description  Choices:   - `"physical"` - `"trunk"` |
| **untagged-vlans**  string | no description |
| **vlan**  string | no description |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

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
   - name: no description
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
           allowed-vlans: <value of string>
           allowed-vlans-all: <value in [disable, enable]>
           arp-inspection-trust: <value in [untrusted, trusted]>
           bundle: <value in [disable, enable]>
           description: <value of string>
           dhcp-snoop-option82-trust: <value in [disable, enable]>
           dhcp-snooping: <value in [trusted, untrusted]>
           discard-mode: <value in [none, all-untagged, all-tagged]>
           edge-port: <value in [disable, enable]>
           igmp-snooping: <value in [disable, enable]>
           igmps-flood-reports: <value in [disable, enable]>
           igmps-flood-traffic: <value in [disable, enable]>
           lacp-speed: <value in [slow, fast]>
           learning-limit: <value of integer>
           lldp-profile: <value of string>
           lldp-status: <value in [disable, rx-only, tx-only, ...]>
           loop-guard: <value in [disabled, enabled]>
           loop-guard-timeout: <value of integer>
           max-bundle: <value of integer>
           mclag: <value in [disable, enable]>
           member-withdrawal-behavior: <value in [forward, block]>
           members: <value of string>
           min-bundle: <value of integer>
           mode: <value in [static, lacp-passive, lacp-active]>
           poe-pre-standard-detection: <value in [disable, enable]>
           poe-status: <value in [disable, enable]>
           port-name: <value of string>
           port-owner: <value of string>
           port-security-policy: <value of string>
           port-selection-criteria: <value in [src-mac, dst-mac, src-dst-mac, ...]>
           qos-policy: <value of string>
           sample-direction: <value in [rx, tx, both]>
           sflow-counter-interval: <value of integer>
           sflow-sample-rate: <value of integer>
           sflow-sampler: <value in [disabled, enabled]>
           stp-bpdu-guard: <value in [disabled, enabled]>
           stp-bpdu-guard-timeout: <value of integer>
           stp-root-guard: <value in [disabled, enabled]>
           stp-state: <value in [disabled, enabled]>
           type: <value in [physical, trunk]>
           untagged-vlans: <value of string>
           vlan: <value of string>
           export-to-pool-flag: <value of integer>
           mac-addr: <value of string>
           packet-sample-rate: <value of integer>
           packet-sampler: <value in [disabled, enabled]>
           sticky-mac: <value in [disable, enable]>
           storm-control-policy: <value of string>
           access-mode: <value in [normal, nac, dynamic, ...]>
           ip-source-guard: <value in [disable, enable]>
           mclag-icl-port: <value of integer>
           p2p-port: <value of integer>
           aggregator-mode: <value in [bandwidth, count]>
           rpvst-port: <value in [disabled, enabled]>
           flow-control: <value in [disable, tx, rx, ...]>
           media-type: <value of string>
           pause-meter: <value of integer>
           pause-meter-resume: <value in [25%, 50%, 75%]>
           trunk-member: <value of integer>
           fec-capable: <value of integer>
           fec-state: <value in [disabled, cl74, cl91]>
           matched-dpp-intf-tags: <value of string>
           matched-dpp-policy: <value of string>
           port-policy: <value of string>
           status: <value in [down, up]>
           dsl-profile: <value of string>
           flap-duration: <value of integer>
           flap-rate: <value of integer>
           flap-timeout: <value of integer>
           flapguard: <value in [disable, enable]>
           interface-tags: <value of string>
           poe-max-power: <value of string>
           poe-standard: <value of string>
```

## [Return Values](fmgr_switchcontroller_managedswitch_ports_module.md#id5)

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
