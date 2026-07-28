---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_wireless_controller_hotspot20_hs_profile module – Configure hotspot profile in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_wireless_controller_hotspot20_hs_profile_module.html
fetched_at: 2026-07-28T02:31:15+00:00
---
# fortinet.fortios.fortios_wireless_controller_hotspot20_hs_profile module – Configure hotspot profile in Fortinet’s FortiOS and FortiGate.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/ui/repo/published/fortinet/fortios/) (version 2.3.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_wireless_controller_hotspot20_hs_profile_module.md#ansible-collections-fortinet-fortios-fortios-wireless-controller-hotspot20-hs-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_wireless_controller_hotspot20_hs_profile`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_wireless_controller_hotspot20_hs_profile_module.md#synopsis)
- [Requirements](fortios_wireless_controller_hotspot20_hs_profile_module.md#requirements)
- [Parameters](fortios_wireless_controller_hotspot20_hs_profile_module.md#parameters)
- [Notes](fortios_wireless_controller_hotspot20_hs_profile_module.md#notes)
- [Examples](fortios_wireless_controller_hotspot20_hs_profile_module.md#examples)
- [Return Values](fortios_wireless_controller_hotspot20_hs_profile_module.md#return-values)

## [Synopsis](fortios_wireless_controller_hotspot20_hs_profile_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify wireless_controller_hotspot20 feature and hs_profile category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_wireless_controller_hotspot20_hs_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_wireless_controller_hotspot20_hs_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |
| **wireless_controller_hotspot20_hs_profile**  dictionary | Configure hotspot profile. |
| **access_network_asra**  string | Enable/disable additional step required for access (ASRA).  **Choices:**   - `"enable"` - `"disable"` |
| **access_network_esr**  string | Enable/disable emergency services reachable (ESR).  **Choices:**   - `"enable"` - `"disable"` |
| **access_network_internet**  string | Enable/disable connectivity to the Internet.  **Choices:**   - `"enable"` - `"disable"` |
| **access_network_type**  string | Access network type.  **Choices:**   - `"private-network"` - `"private-network-with-guest-access"` - `"chargeable-public-network"` - `"free-public-network"` - `"personal-device-network"` - `"emergency-services-only-network"` - `"test-or-experimental"` - `"wildcard"` |
| **access_network_uesa**  string | Enable/disable unauthenticated emergency service accessible (UESA).  **Choices:**   - `"enable"` - `"disable"` |
| **advice_of_charge**  string | Advice of charge. Source wireless-controller.hotspot20.h2qp-advice-of-charge.name. |
| **anqp_domain_id**  integer | ANQP Domain ID (0-65535). |
| **bss_transition**  string | Enable/disable basic service set (BSS) transition Support.  **Choices:**   - `"enable"` - `"disable"` |
| **conn_cap**  string | Connection capability name. Source wireless-controller.hotspot20.h2qp-conn-capability.name. |
| **deauth_request_timeout**  integer | Deauthentication request timeout (in seconds). |
| **dgaf**  string | Enable/disable downstream group-addressed forwarding (DGAF).  **Choices:**   - `"enable"` - `"disable"` |
| **domain_name**  string | Domain name. |
| **gas_comeback_delay**  integer | GAS comeback delay (0 or 100 - 10000 milliseconds). |
| **gas_fragmentation_limit**  integer | GAS fragmentation limit (512 - 4096). |
| **hessid**  string | Homogeneous extended service set identifier (HESSID). |
| **ip_addr_type**  string | IP address type name. Source wireless-controller.hotspot20.anqp-ip-address-type.name. |
| **l2tif**  string | Enable/disable Layer 2 traffic inspection and filtering.  **Choices:**   - `"enable"` - `"disable"` |
| **nai_realm**  string | NAI realm list name. Source wireless-controller.hotspot20.anqp-nai-realm.name. |
| **name**  string / required | Hotspot profile name. |
| **network_auth**  string | Network authentication name. Source wireless-controller.hotspot20.anqp-network-auth-type.name. |
| **oper_friendly_name**  string | Operator friendly name. Source wireless-controller.hotspot20.h2qp-operator-name.name. |
| **oper_icon**  string | Operator icon. Source wireless-controller.hotspot20.icon.name. |
| **osu_provider**  list / elements=dictionary | Manually selected list of OSU provider(s). |
| **name**  string / required | OSU provider name. Source wireless-controller.hotspot20.h2qp-osu-provider.name. |
| **osu_provider_nai**  string | OSU Provider NAI. Source wireless-controller.hotspot20.h2qp-osu-provider-nai.name. |
| **osu_ssid**  string | Online sign up (OSU) SSID. |
| **pame_bi**  string | Enable/disable Pre-Association Message Exchange BSSID Independent (PAME-BI).  **Choices:**   - `"disable"` - `"enable"` |
| **plmn_3gpp**  string | 3GPP PLMN name. Source wireless-controller.hotspot20.anqp-3gpp-cellular.name. |
| **proxy_arp**  string | Enable/disable Proxy ARP.  **Choices:**   - `"enable"` - `"disable"` |
| **qos_map**  string | QoS MAP set ID. Source wireless-controller.hotspot20.qos-map.name. |
| **release**  integer | Hotspot 2.0 Release number (1, 2, 3). |
| **roaming_consortium**  string | Roaming consortium list name. Source wireless-controller.hotspot20.anqp-roaming-consortium.name. |
| **terms_and_conditions**  string | Terms and conditions. Source wireless-controller.hotspot20.h2qp-terms-and-conditions.name. |
| **venue_group**  string | Venue group.  **Choices:**   - `"unspecified"` - `"assembly"` - `"business"` - `"educational"` - `"factory"` - `"institutional"` - `"mercantile"` - `"residential"` - `"storage"` - `"utility"` - `"vehicular"` - `"outdoor"` |
| **venue_name**  string | Venue name. Source wireless-controller.hotspot20.anqp-venue-name.name. |
| **venue_type**  string | Venue type.  **Choices:**   - `"unspecified"` - `"arena"` - `"stadium"` - `"passenger-terminal"` - `"amphitheater"` - `"amusement-park"` - `"place-of-worship"` - `"convention-center"` - `"library"` - `"museum"` - `"restaurant"` - `"theater"` - `"bar"` - `"coffee-shop"` - `"zoo-or-aquarium"` - `"emergency-center"` - `"doctor-office"` - `"bank"` - `"fire-station"` - `"police-station"` - `"post-office"` - `"professional-office"` - `"research-facility"` - `"attorney-office"` - `"primary-school"` - `"secondary-school"` - `"university-or-college"` - `"factory"` - `"hospital"` - `"long-term-care-facility"` - `"rehab-center"` - `"group-home"` - `"prison-or-jail"` - `"retail-store"` - `"grocery-market"` - `"auto-service-station"` - `"shopping-mall"` - `"gas-station"` - `"private"` - `"hotel-or-motel"` - `"dormitory"` - `"boarding-house"` - `"automobile"` - `"airplane"` - `"bus"` - `"ferry"` - `"ship-or-boat"` - `"train"` - `"motor-bike"` - `"muni-mesh-network"` - `"city-park"` - `"rest-area"` - `"traffic-control"` - `"bus-stop"` - `"kiosk"` |
| **venue_url**  string | Venue name. Source wireless-controller.hotspot20.anqp-venue-url.name. |
| **wan_metrics**  string | WAN metric name. Source wireless-controller.hotspot20.h2qp-wan-metric.name. |
| **wnm_sleep_mode**  string | Enable/disable wireless network management (WNM) sleep mode.  **Choices:**   - `"enable"` - `"disable"` |

## [Notes](fortios_wireless_controller_hotspot20_hs_profile_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_wireless_controller_hotspot20_hs_profile_module.md#id5)

```yaml+jinja
- hosts: fortigates
  collections:
    - fortinet.fortios
  connection: httpapi
  vars:
   vdom: "root"
   ansible_httpapi_use_ssl: yes
   ansible_httpapi_validate_certs: no
   ansible_httpapi_port: 443
  tasks:
  - name: Configure hotspot profile.
    fortios_wireless_controller_hotspot20_hs_profile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      wireless_controller_hotspot20_hs_profile:
        plmn_3gpp: "<your_own_value> (source wireless-controller.hotspot20.anqp-3gpp-cellular.name)"
        access_network_asra: "enable"
        access_network_esr: "enable"
        access_network_internet: "enable"
        access_network_type: "private-network"
        access_network_uesa: "enable"
        advice_of_charge: "<your_own_value> (source wireless-controller.hotspot20.h2qp-advice-of-charge.name)"
        anqp_domain_id: "0"
        bss_transition: "enable"
        conn_cap: "<your_own_value> (source wireless-controller.hotspot20.h2qp-conn-capability.name)"
        deauth_request_timeout: "60"
        dgaf: "enable"
        domain_name: "<your_own_value>"
        gas_comeback_delay: "500"
        gas_fragmentation_limit: "1024"
        hessid: "<your_own_value>"
        ip_addr_type: "<your_own_value> (source wireless-controller.hotspot20.anqp-ip-address-type.name)"
        l2tif: "enable"
        nai_realm: "<your_own_value> (source wireless-controller.hotspot20.anqp-nai-realm.name)"
        name: "default_name_22"
        network_auth: "<your_own_value> (source wireless-controller.hotspot20.anqp-network-auth-type.name)"
        oper_friendly_name: "<your_own_value> (source wireless-controller.hotspot20.h2qp-operator-name.name)"
        oper_icon: "<your_own_value> (source wireless-controller.hotspot20.icon.name)"
        osu_provider:
         -
            name: "default_name_27 (source wireless-controller.hotspot20.h2qp-osu-provider.name)"
        osu_provider_nai: "<your_own_value> (source wireless-controller.hotspot20.h2qp-osu-provider-nai.name)"
        osu_ssid: "<your_own_value>"
        pame_bi: "disable"
        proxy_arp: "enable"
        qos_map: "<your_own_value> (source wireless-controller.hotspot20.qos-map.name)"
        release: "2"
        roaming_consortium: "<your_own_value> (source wireless-controller.hotspot20.anqp-roaming-consortium.name)"
        terms_and_conditions: "<your_own_value> (source wireless-controller.hotspot20.h2qp-terms-and-conditions.name)"
        venue_group: "unspecified"
        venue_name: "<your_own_value> (source wireless-controller.hotspot20.anqp-venue-name.name)"
        venue_type: "unspecified"
        venue_url: "<your_own_value> (source wireless-controller.hotspot20.anqp-venue-url.name)"
        wan_metrics: "<your_own_value> (source wireless-controller.hotspot20.h2qp-wan-metric.name)"
        wnm_sleep_mode: "enable"
```

## [Return Values](fortios_wireless_controller_hotspot20_hs_profile_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  **Returned:** always  **Sample:** `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  **Returned:** always  **Sample:** `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  **Returned:** always  **Sample:** `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  **Returned:** success  **Sample:** `"id"` |
| **name**  string | Name of the table used to fulfill the request  **Returned:** always  **Sample:** `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  **Returned:** always  **Sample:** `"webfilter"` |
| **revision**  string | Internal revision number  **Returned:** always  **Sample:** `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  **Returned:** always  **Sample:** `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  **Returned:** always  **Sample:** `"success"` |
| **vdom**  string | Virtual domain used  **Returned:** always  **Sample:** `"root"` |
| **version**  string | Version of the FortiGate  **Returned:** always  **Sample:** `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

- [Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
- [Homepage](https://www.fortinet.com)
- [Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
