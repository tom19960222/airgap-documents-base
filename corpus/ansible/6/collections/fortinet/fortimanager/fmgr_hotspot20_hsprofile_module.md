---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_hotspot20_hsprofile module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_hotspot20_hsprofile_module.html
fetched_at: 2026-07-27T17:33:23+00:00
---
# fortinet.fortimanager.fmgr_hotspot20_hsprofile module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_hotspot20_hsprofile`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_hotspot20_hsprofile_module.md#synopsis)
- [Parameters](fmgr_hotspot20_hsprofile_module.md#parameters)
- [Notes](fmgr_hotspot20_hsprofile_module.md#notes)
- [Examples](fmgr_hotspot20_hsprofile_module.md#examples)
- [Return Values](fmgr_hotspot20_hsprofile_module.md#return-values)

## [Synopsis](fmgr_hotspot20_hsprofile_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_hotspot20_hsprofile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **hotspot20_hsprofile**  dictionary | the top level parameters set |
| **3gpp-plmn**  string | no description |
| **access-network-asra**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **access-network-esr**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **access-network-internet**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **access-network-type**  string | no description  Choices:   - `"private-network"` - `"private-network-with-guest-access"` - `"chargeable-public-network"` - `"free-public-network"` - `"personal-device-network"` - `"emergency-services-only-network"` - `"test-or-experimental"` - `"wildcard"` |
| **access-network-uesa**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **advice-of-charge**  string | no description |
| **anqp-domain-id**  integer | no description |
| **bss-transition**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **conn-cap**  string | no description |
| **deauth-request-timeout**  integer | no description |
| **dgaf**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **domain-name**  string | no description |
| **gas-comeback-delay**  integer | no description |
| **gas-fragmentation-limit**  integer | no description |
| **hessid**  string | no description |
| **ip-addr-type**  string | no description |
| **l2tif**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **nai-realm**  string | no description |
| **name**  string | no description |
| **network-auth**  string | no description |
| **oper-friendly-name**  string | no description |
| **oper-icon**  string | no description |
| **osu-provider**  string | no description |
| **osu-provider-nai**  string | no description |
| **osu-ssid**  string | no description |
| **pame-bi**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **proxy-arp**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **qos-map**  string | no description |
| **release**  integer | no description |
| **roaming-consortium**  string | no description |
| **terms-and-conditions**  string | no description |
| **venue-group**  string | no description  Choices:   - `"unspecified"` - `"assembly"` - `"business"` - `"educational"` - `"factory"` - `"institutional"` - `"mercantile"` - `"residential"` - `"storage"` - `"utility"` - `"vehicular"` - `"outdoor"` |
| **venue-name**  string | no description |
| **venue-type**  string | no description  Choices:   - `"unspecified"` - `"arena"` - `"stadium"` - `"passenger-terminal"` - `"amphitheater"` - `"amusement-park"` - `"place-of-worship"` - `"convention-center"` - `"library"` - `"museum"` - `"restaurant"` - `"theater"` - `"bar"` - `"coffee-shop"` - `"zoo-or-aquarium"` - `"emergency-center"` - `"doctor-office"` - `"bank"` - `"fire-station"` - `"police-station"` - `"post-office"` - `"professional-office"` - `"research-facility"` - `"attorney-office"` - `"primary-school"` - `"secondary-school"` - `"university-or-college"` - `"factory"` - `"hospital"` - `"long-term-care-facility"` - `"rehab-center"` - `"group-home"` - `"prison-or-jail"` - `"retail-store"` - `"grocery-market"` - `"auto-service-station"` - `"shopping-mall"` - `"gas-station"` - `"private"` - `"hotel-or-motel"` - `"dormitory"` - `"boarding-house"` - `"automobile"` - `"airplane"` - `"bus"` - `"ferry"` - `"ship-or-boat"` - `"train"` - `"motor-bike"` - `"muni-mesh-network"` - `"city-park"` - `"rest-area"` - `"traffic-control"` - `"bus-stop"` - `"kiosk"` |
| **venue-url**  string | no description |
| **wan-metrics**  string | no description |
| **wnm-sleep-mode**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_hotspot20_hsprofile_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_hotspot20_hsprofile_module.md#id4)

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
     fmgr_hotspot20_hsprofile:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        hotspot20_hsprofile:
           3gpp-plmn: <value of string>
           access-network-asra: <value in [disable, enable]>
           access-network-esr: <value in [disable, enable]>
           access-network-internet: <value in [disable, enable]>
           access-network-type: <value in [private-network, private-network-with-guest-access, chargeable-public-network, ...]>
           access-network-uesa: <value in [disable, enable]>
           anqp-domain-id: <value of integer>
           bss-transition: <value in [disable, enable]>
           conn-cap: <value of string>
           deauth-request-timeout: <value of integer>
           dgaf: <value in [disable, enable]>
           domain-name: <value of string>
           gas-comeback-delay: <value of integer>
           gas-fragmentation-limit: <value of integer>
           hessid: <value of string>
           ip-addr-type: <value of string>
           l2tif: <value in [disable, enable]>
           nai-realm: <value of string>
           name: <value of string>
           network-auth: <value of string>
           oper-friendly-name: <value of string>
           osu-provider: <value of string>
           osu-ssid: <value of string>
           pame-bi: <value in [disable, enable]>
           proxy-arp: <value in [disable, enable]>
           qos-map: <value of string>
           roaming-consortium: <value of string>
           venue-group: <value in [unspecified, assembly, business, ...]>
           venue-name: <value of string>
           venue-type: <value in [unspecified, arena, stadium, ...]>
           wan-metrics: <value of string>
           wnm-sleep-mode: <value in [disable, enable]>
           advice-of-charge: <value of string>
           oper-icon: <value of string>
           osu-provider-nai: <value of string>
           release: <value of integer>
           terms-and-conditions: <value of string>
           venue-url: <value of string>
```

## [Return Values](fmgr_hotspot20_hsprofile_module.md#id5)

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
