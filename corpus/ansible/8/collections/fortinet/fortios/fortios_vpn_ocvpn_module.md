---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_vpn_ocvpn module – Configure Overlay Controller VPN settings in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_vpn_ocvpn_module.html
fetched_at: 2026-07-28T02:30:25+00:00
---
# fortinet.fortios.fortios_vpn_ocvpn module – Configure Overlay Controller VPN settings in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_vpn_ocvpn_module.md#ansible-collections-fortinet-fortios-fortios-vpn-ocvpn-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_vpn_ocvpn`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_vpn_ocvpn_module.md#synopsis)
- [Requirements](fortios_vpn_ocvpn_module.md#requirements)
- [Parameters](fortios_vpn_ocvpn_module.md#parameters)
- [Notes](fortios_vpn_ocvpn_module.md#notes)
- [Examples](fortios_vpn_ocvpn_module.md#examples)
- [Return Values](fortios_vpn_ocvpn_module.md#return-values)

## [Synopsis](fortios_vpn_ocvpn_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify vpn feature and ocvpn category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_vpn_ocvpn_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_vpn_ocvpn_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |
| **vpn_ocvpn**  dictionary | Configure Overlay Controller VPN settings. |
| **auto_discovery**  string | Enable/disable auto-discovery shortcuts.  **Choices:**   - `"enable"` - `"disable"` |
| **auto_discovery_shortcut_mode**  string | Control deletion of child short-cut tunnels when the parent tunnel goes down.  **Choices:**   - `"independent"` - `"dependent"` |
| **eap**  string | Enable/disable EAP client authentication.  **Choices:**   - `"enable"` - `"disable"` |
| **eap_users**  string | EAP authentication user group. Source user.group.name. |
| **forticlient_access**  dictionary | Configure FortiClient settings. |
| **auth_groups**  list / elements=dictionary | FortiClient user authentication groups. |
| **auth_group**  string | Authentication user group for FortiClient access. Source user.group.name. |
| **name**  string / required | Group name. |
| **overlays**  list / elements=dictionary | OCVPN overlays to allow access to. |
| **overlay_name**  string / required | Overlay name. Source vpn.ocvpn.overlays.overlay-name. |
| **psksecret**  string | Pre-shared secret for FortiClient PSK authentication (ASCII string or hexadecimal encoded with a leading 0x). |
| **status**  string | Enable/disable FortiClient to access OCVPN networks.  **Choices:**   - `"enable"` - `"disable"` |
| **ha_alias**  string | Hidden HA alias. |
| **ip_allocation_block**  string | Class B subnet reserved for private IP address assignment. |
| **multipath**  string | Enable/disable multipath redundancy.  **Choices:**   - `"enable"` - `"disable"` |
| **nat**  string | Enable/disable NAT support.  **Choices:**   - `"enable"` - `"disable"` |
| **overlays**  list / elements=dictionary | Network overlays to register with Overlay Controller VPN service. |
| **assign_ip**  string | Enable/disable mode-cfg address assignment.  **Choices:**   - `"enable"` - `"disable"` |
| **id**  integer | ID. |
| **inter_overlay**  string | Allow or deny traffic from other overlays.  **Choices:**   - `"allow"` - `"deny"` |
| **ipv4_end_ip**  string | End of IPv4 range. |
| **ipv4_start_ip**  string | Start of IPv4 range. |
| **name**  string | Overlay name. |
| **overlay_name**  string / required | Overlay name. |
| **subnets**  list / elements=dictionary | Internal subnets to register with OCVPN service. |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **interface**  string | LAN interface. Source system.interface.name. |
| **subnet**  string | IPv4 address and subnet mask. |
| **type**  string | Subnet type.  **Choices:**   - `"subnet"` - `"interface"` |
| **poll_interval**  integer | Overlay Controller VPN polling interval. |
| **role**  string | Set device role.  **Choices:**   - `"spoke"` - `"primary-hub"` - `"secondary-hub"` |
| **sdwan**  string | Enable/disable adding OCVPN tunnels to SD-WAN.  **Choices:**   - `"enable"` - `"disable"` |
| **sdwan_zone**  string | Set SD-WAN zone. Source system.sdwan.zone.name. |
| **status**  string | Enable/disable Overlay Controller cloud assisted VPN.  **Choices:**   - `"enable"` - `"disable"` |
| **subnets**  list / elements=dictionary | Internal subnets to register with Overlay Controller VPN service. |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **interface**  string | LAN interface. Source system.interface.name. |
| **subnet**  string | IPv4 address and subnet mask. |
| **type**  string | Subnet type.  **Choices:**   - `"subnet"` - `"interface"` |
| **wan_interface**  list / elements=dictionary | FortiGate WAN interfaces to use with OCVPN. |
| **name**  string / required | Interface name. Source system.interface.name. |

## [Notes](fortios_vpn_ocvpn_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_vpn_ocvpn_module.md#id5)

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
  - name: Configure Overlay Controller VPN settings.
    fortios_vpn_ocvpn:
      vdom:  "{{ vdom }}"
      vpn_ocvpn:
        auto_discovery: "enable"
        auto_discovery_shortcut_mode: "independent"
        eap: "enable"
        eap_users: "<your_own_value> (source user.group.name)"
        forticlient_access:
            auth_groups:
             -
                auth_group: "<your_own_value> (source user.group.name)"
                name: "default_name_10"
                overlays:
                 -
                    overlay_name: "<your_own_value> (source vpn.ocvpn.overlays.overlay-name)"
            psksecret: "<your_own_value>"
            status: "enable"
        ha_alias: "<your_own_value>"
        ip_allocation_block: "<your_own_value>"
        multipath: "enable"
        nat: "enable"
        overlays:
         -
            assign_ip: "enable"
            id:  "21"
            inter_overlay: "allow"
            ipv4_end_ip: "<your_own_value>"
            ipv4_start_ip: "<your_own_value>"
            name: "default_name_25"
            overlay_name: "<your_own_value>"
            subnets:
             -
                id:  "28"
                interface: "<your_own_value> (source system.interface.name)"
                subnet: "<your_own_value>"
                type: "subnet"
        poll_interval: "30"
        role: "spoke"
        sdwan: "enable"
        sdwan_zone: "<your_own_value> (source system.sdwan.zone.name)"
        status: "enable"
        subnets:
         -
            id:  "38"
            interface: "<your_own_value> (source system.interface.name)"
            subnet: "<your_own_value>"
            type: "subnet"
        wan_interface:
         -
            name: "default_name_43 (source system.interface.name)"
```

## [Return Values](fortios_vpn_ocvpn_module.md#id6)

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
