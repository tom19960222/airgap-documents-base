---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_hotspot20_hsprofile module – Configure hotspot profile."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_hotspot20_hsprofile_module.html
fetched_at: 2026-07-28T02:14:43+00:00
---
# fortinet.fortimanager.fmgr_hotspot20_hsprofile module – Configure hotspot profile.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_hotspot20_hsprofile`.

New in fortinet.fortimanager 2.0.0

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
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **hotspot20_hsprofile**  dictionary | the top level parameters set |
| **3gpp-plmn**  string | 3GPP PLMN name. |
| **access-network-asra**  string | Enable/disable additional step required for access  **Choices:**   - `"disable"` - `"enable"` |
| **access-network-esr**  string | Enable/disable emergency services reachable  **Choices:**   - `"disable"` - `"enable"` |
| **access-network-internet**  string | Enable/disable connectivity to the Internet.  **Choices:**   - `"disable"` - `"enable"` |
| **access-network-type**  string | Access network type.  **Choices:**   - `"private-network"` - `"private-network-with-guest-access"` - `"chargeable-public-network"` - `"free-public-network"` - `"personal-device-network"` - `"emergency-services-only-network"` - `"test-or-experimental"` - `"wildcard"` |
| **access-network-uesa**  string | Enable/disable unauthenticated emergency service accessible  **Choices:**   - `"disable"` - `"enable"` |
| **advice-of-charge**  string | Advice of charge. |
| **anqp-domain-id**  integer | ANQP Domain ID |
| **bss-transition**  string | Enable/disable basic service set  **Choices:**   - `"disable"` - `"enable"` |
| **conn-cap**  string | Connection capability name. |
| **deauth-request-timeout**  integer | Deauthentication request timeout |
| **dgaf**  string | Enable/disable downstream group-addressed forwarding  **Choices:**   - `"disable"` - `"enable"` |
| **domain-name**  string | Domain name. |
| **gas-comeback-delay**  integer | GAS comeback delay |
| **gas-fragmentation-limit**  integer | GAS fragmentation limit |
| **hessid**  string | Homogeneous extended service set identifier |
| **ip-addr-type**  string | IP address type name. |
| **l2tif**  string | Enable/disable Layer 2 traffic inspection and filtering.  **Choices:**   - `"disable"` - `"enable"` |
| **nai-realm**  string | NAI realm list name. |
| **name**  string / required | Hotspot profile name. |
| **network-auth**  string | Network authentication name. |
| **oper-friendly-name**  string | Operator friendly name. |
| **oper-icon**  string | Operator icon. |
| **osu-provider**  any | (list or str) Manually selected list of OSU provider |
| **osu-provider-nai**  string | OSU Provider NAI. |
| **osu-ssid**  string | Online sign up |
| **pame-bi**  string | Enable/disable Pre-Association Message Exchange BSSID Independent  **Choices:**   - `"disable"` - `"enable"` |
| **proxy-arp**  string | Enable/disable Proxy ARP.  **Choices:**   - `"disable"` - `"enable"` |
| **qos-map**  string | QoS MAP set ID. |
| **release**  integer | Hotspot 2. |
| **roaming-consortium**  string | Roaming consortium list name. |
| **terms-and-conditions**  string | Terms and conditions. |
| **venue-group**  string | Venue group.  **Choices:**   - `"unspecified"` - `"assembly"` - `"business"` - `"educational"` - `"factory"` - `"institutional"` - `"mercantile"` - `"residential"` - `"storage"` - `"utility"` - `"vehicular"` - `"outdoor"` |
| **venue-name**  string | Venue name. |
| **venue-type**  string | Venue type.  **Choices:**   - `"unspecified"` - `"arena"` - `"stadium"` - `"passenger-terminal"` - `"amphitheater"` - `"amusement-park"` - `"place-of-worship"` - `"convention-center"` - `"library"` - `"museum"` - `"restaurant"` - `"theater"` - `"bar"` - `"coffee-shop"` - `"zoo-or-aquarium"` - `"emergency-center"` - `"doctor-office"` - `"bank"` - `"fire-station"` - `"police-station"` - `"post-office"` - `"professional-office"` - `"research-facility"` - `"attorney-office"` - `"primary-school"` - `"secondary-school"` - `"university-or-college"` - `"factory"` - `"hospital"` - `"long-term-care-facility"` - `"rehab-center"` - `"group-home"` - `"prison-or-jail"` - `"retail-store"` - `"grocery-market"` - `"auto-service-station"` - `"shopping-mall"` - `"gas-station"` - `"private"` - `"hotel-or-motel"` - `"dormitory"` - `"boarding-house"` - `"automobile"` - `"airplane"` - `"bus"` - `"ferry"` - `"ship-or-boat"` - `"train"` - `"motor-bike"` - `"muni-mesh-network"` - `"city-park"` - `"rest-area"` - `"traffic-control"` - `"bus-stop"` - `"kiosk"` |
| **venue-url**  string | Venue name. |
| **wan-metrics**  string | WAN metric name. |
| **wnm-sleep-mode**  string | Enable/disable wireless network management  **Choices:**   - `"disable"` - `"enable"` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

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
    - name: Configure hotspot profile.
      fmgr_hotspot20_hsprofile:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        hotspot20_hsprofile:
          3gpp-plmn: <string>
          access-network-asra: <value in [disable, enable]>
          access-network-esr: <value in [disable, enable]>
          access-network-internet: <value in [disable, enable]>
          access-network-type: <value in [private-network, private-network-with-guest-access, chargeable-public-network, ...]>
          access-network-uesa: <value in [disable, enable]>
          anqp-domain-id: <integer>
          bss-transition: <value in [disable, enable]>
          conn-cap: <string>
          deauth-request-timeout: <integer>
          dgaf: <value in [disable, enable]>
          domain-name: <string>
          gas-comeback-delay: <integer>
          gas-fragmentation-limit: <integer>
          hessid: <string>
          ip-addr-type: <string>
          l2tif: <value in [disable, enable]>
          nai-realm: <string>
          name: <string>
          network-auth: <string>
          oper-friendly-name: <string>
          osu-provider: <list or string>
          osu-ssid: <string>
          pame-bi: <value in [disable, enable]>
          proxy-arp: <value in [disable, enable]>
          qos-map: <string>
          roaming-consortium: <string>
          venue-group: <value in [unspecified, assembly, business, ...]>
          venue-name: <string>
          venue-type: <value in [unspecified, arena, stadium, ...]>
          wan-metrics: <string>
          wnm-sleep-mode: <value in [disable, enable]>
          advice-of-charge: <string>
          oper-icon: <string>
          osu-provider-nai: <string>
          release: <integer>
          terms-and-conditions: <string>
          venue-url: <string>
```

## [Return Values](fmgr_hotspot20_hsprofile_module.md#id5)

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
