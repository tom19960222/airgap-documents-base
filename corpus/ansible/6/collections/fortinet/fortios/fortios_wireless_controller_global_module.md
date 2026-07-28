---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_wireless_controller_global module – Configure wireless controller global settings in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_wireless_controller_global_module.html
fetched_at: 2026-07-27T17:47:00+00:00
---
# fortinet.fortios.fortios_wireless_controller_global module – Configure wireless controller global settings in Fortinet’s FortiOS and FortiGate.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/fortinet/fortios) (version 2.2.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_wireless_controller_global_module.md#ansible-collections-fortinet-fortios-fortios-wireless-controller-global-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_wireless_controller_global`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_wireless_controller_global_module.md#synopsis)
- [Requirements](fortios_wireless_controller_global_module.md#requirements)
- [Parameters](fortios_wireless_controller_global_module.md#parameters)
- [Notes](fortios_wireless_controller_global_module.md#notes)
- [Examples](fortios_wireless_controller_global_module.md#examples)
- [Return Values](fortios_wireless_controller_global_module.md#return-values)

## [Synopsis](fortios_wireless_controller_global_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify wireless_controller feature and global category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_wireless_controller_global_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_wireless_controller_global_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |
| **wireless_controller_global**  dictionary | Configure wireless controller global settings. |
| **ap_log_server**  string | Enable/disable configuring FortiGate to redirect wireless event log messages or FortiAPs to send UTM log messages to a syslog server .  Choices:   - `"enable"` - `"disable"` |
| **ap_log_server_ip**  string | IP address that FortiGate or FortiAPs send log messages to. |
| **ap_log_server_port**  integer | Port that FortiGate or FortiAPs send log messages to. |
| **control_message_offload**  list / elements=string | Configure CAPWAP control message data channel offload.  Choices:   - `"ebp-frame"` - `"aeroscout-tag"` - `"ap-list"` - `"sta-list"` - `"sta-cap-list"` - `"stats"` - `"aeroscout-mu"` - `"sta-health"` - `"spectral-analysis"` |
| **data_ethernet_II**  string | Configure the wireless controller to use Ethernet II or 802.3 frames with 802.3 data tunnel mode .  Choices:   - `"enable"` - `"disable"` |
| **discovery_mc_addr**  string | Multicast IP address for AP discovery . |
| **fiapp_eth_type**  integer | Ethernet type for Fortinet Inter-Access Point Protocol (IAPP), or IEEE 802.11f, packets (0 - 65535). |
| **image_download**  string | Enable/disable WTP image download at join time.  Choices:   - `"enable"` - `"disable"` |
| **ipsec_base_ip**  string | Base IP address for IPsec VPN tunnels between the access points and the wireless controller . |
| **link_aggregation**  string | Enable/disable calculating the CAPWAP transmit hash to load balance sessions to link aggregation nodes .  Choices:   - `"enable"` - `"disable"` |
| **location**  string | Description of the location of the wireless controller. |
| **max_clients**  integer | Maximum number of clients that can connect simultaneously . |
| **max_retransmit**  integer | Maximum number of tunnel packet retransmissions (0 - 64). |
| **mesh_eth_type**  integer | Mesh Ethernet identifier included in backhaul packets (0 - 65535). |
| **nac_interval**  integer | Interval in seconds between two WiFi network access control (NAC) checks (10 - 600). |
| **name**  string | Name of the wireless controller. |
| **rogue_scan_mac_adjacency**  integer | Maximum numerical difference between an AP”s Ethernet and wireless MAC values to match for rogue detection (0 - 31). |
| **tunnel_mode**  string | Compatible/strict tunnel mode.  Choices:   - `"compatible"` - `"strict"` |
| **wtp_share**  string | Enable/disable sharing of WTPs between VDOMs.  Choices:   - `"enable"` - `"disable"` |

## [Notes](fortios_wireless_controller_global_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_wireless_controller_global_module.md#id5)

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
  - name: Configure wireless controller global settings.
    fortios_wireless_controller_global:
      vdom:  "{{ vdom }}"
      wireless_controller_global:
        ap_log_server: "enable"
        ap_log_server_ip: "<your_own_value>"
        ap_log_server_port: "0"
        control_message_offload: "ebp-frame"
        data_ethernet_II: "enable"
        discovery_mc_addr: "<your_own_value>"
        fiapp_eth_type: "5252"
        image_download: "enable"
        ipsec_base_ip: "<your_own_value>"
        link_aggregation: "enable"
        location: "<your_own_value>"
        max_clients: "0"
        max_retransmit: "3"
        mesh_eth_type: "8755"
        nac_interval: "120"
        name: "default_name_18"
        rogue_scan_mac_adjacency: "7"
        tunnel_mode: "compatible"
        wtp_share: "enable"
```

## [Return Values](fortios_wireless_controller_global_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  Returned: always  Sample: `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  Returned: always  Sample: `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  Returned: always  Sample: `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  Returned: success  Sample: `"id"` |
| **name**  string | Name of the table used to fulfill the request  Returned: always  Sample: `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  Returned: always  Sample: `"webfilter"` |
| **revision**  string | Internal revision number  Returned: always  Sample: `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  Returned: always  Sample: `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  Returned: always  Sample: `"success"` |
| **vdom**  string | Virtual domain used  Returned: always  Sample: `"root"` |
| **version**  string | Version of the FortiGate  Returned: always  Sample: `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
[Homepage](https://www.fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
