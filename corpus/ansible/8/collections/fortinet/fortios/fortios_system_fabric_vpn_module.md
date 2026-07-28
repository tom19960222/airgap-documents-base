---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_system_fabric_vpn module – Setup for self orchestrated fabric auto discovery VPN in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_system_fabric_vpn_module.html
fetched_at: 2026-07-28T02:28:17+00:00
---
# fortinet.fortios.fortios_system_fabric_vpn module – Setup for self orchestrated fabric auto discovery VPN in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_system_fabric_vpn_module.md#ansible-collections-fortinet-fortios-fortios-system-fabric-vpn-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_fabric_vpn`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_fabric_vpn_module.md#synopsis)
- [Requirements](fortios_system_fabric_vpn_module.md#requirements)
- [Parameters](fortios_system_fabric_vpn_module.md#parameters)
- [Notes](fortios_system_fabric_vpn_module.md#notes)
- [Examples](fortios_system_fabric_vpn_module.md#examples)
- [Return Values](fortios_system_fabric_vpn_module.md#return-values)

## [Synopsis](fortios_system_fabric_vpn_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and fabric_vpn category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_fabric_vpn_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_system_fabric_vpn_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **system_fabric_vpn**  dictionary | Setup for self orchestrated fabric auto discovery VPN. |
| **advertised_subnets**  list / elements=dictionary | Local advertised subnets. |
| **access**  string | Access policy direction.  **Choices:**   - `"inbound"` - `"bidirectional"` |
| **bgp_network**  integer | Underlying BGP network. Source router.bgp.network.id. |
| **firewall_address**  string | Underlying firewall address. Source firewall.address.name. |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **policies**  list / elements=integer | Underlying policies. Source firewall.policy.policyid. |
| **prefix**  string | Network prefix. |
| **bgp_as**  integer | BGP Router AS number, valid from 1 to 4294967295. |
| **branch_name**  string | Branch name. |
| **health_checks**  list / elements=string | Underlying health checks. Source system.sdwan.health-check.name. |
| **loopback_address_block**  string | IPv4 address and subnet mask for hub”s loopback address, syntax: X.X.X.X/24. |
| **loopback_advertised_subnet**  integer | Loopback advertised subnet reference. Source system.fabric-vpn.advertised-subnets.id. |
| **loopback_interface**  string | Loopback interface. Source system.interface.name. |
| **overlays**  list / elements=dictionary | Local overlay interfaces table. |
| **bgp_neighbor**  string | Underlying BGP neighbor entry. Source router.bgp.neighbor.ip. |
| **bgp_neighbor_group**  string | Underlying BGP neighbor group entry. Source router.bgp.neighbor-group.name. |
| **bgp_neighbor_range**  integer | Underlying BGP neighbor range entry. Source router.bgp.neighbor-range.id. |
| **bgp_network**  integer | Underlying BGP network. Source router.bgp.network.id. |
| **interface**  string | Underlying interface name. Source system.interface.name. |
| **ipsec_phase1**  string | IPsec interface. Source vpn.ipsec.phase1-interface.name. |
| **name**  string / required | Overlay name. |
| **overlay_policy**  integer | The overlay policy to allow ADVPN thru traffic. Source firewall.policy.policyid. |
| **overlay_tunnel_block**  string | IPv4 address and subnet mask for the overlay tunnel , syntax: X.X.X.X/24. |
| **remote_gw**  string | IP address of the hub gateway (Set by hub). |
| **route_policy**  integer | Underlying router policy. Source router.policy.seq-num. |
| **sdwan_member**  integer | Reference to SD-WAN member entry. Source system.sdwan.members.seq-num. |
| **policy_rule**  string | Policy creation rule.  **Choices:**   - `"health-check"` - `"manual"` - `"auto"` |
| **psksecret**  string | Pre-shared secret for ADVPN. |
| **sdwan_zone**  string | Reference to created SD-WAN zone. Source system.sdwan.zone.name. |
| **status**  string | Enable/disable Fabric VPN.  **Choices:**   - `"enable"` - `"disable"` |
| **sync_mode**  string | Setting synchronised by fabric or manual.  **Choices:**   - `"enable"` - `"disable"` |
| **vpn_role**  string | Fabric VPN role.  **Choices:**   - `"hub"` - `"spoke"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_system_fabric_vpn_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_fabric_vpn_module.md#id5)

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
  - name: Setup for self orchestrated fabric auto discovery VPN.
    fortios_system_fabric_vpn:
      vdom:  "{{ vdom }}"
      system_fabric_vpn:
        advertised_subnets:
         -
            access: "inbound"
            bgp_network: "0"
            firewall_address: "<your_own_value> (source firewall.address.name)"
            id:  "7"
            policies: "<your_own_value> (source firewall.policy.policyid)"
            prefix: "<your_own_value>"
        bgp_as: "0"
        branch_name: "<your_own_value>"
        health_checks: "<your_own_value> (source system.sdwan.health-check.name)"
        loopback_address_block: "<your_own_value>"
        loopback_advertised_subnet: "0"
        loopback_interface: "<your_own_value> (source system.interface.name)"
        overlays:
         -
            bgp_neighbor: "<your_own_value> (source router.bgp.neighbor.ip)"
            bgp_neighbor_group: "<your_own_value> (source router.bgp.neighbor-group.name)"
            bgp_neighbor_range: "0"
            bgp_network: "0"
            interface: "<your_own_value> (source system.interface.name)"
            ipsec_phase1: "<your_own_value> (source vpn.ipsec.phase1-interface.name)"
            name: "default_name_23"
            overlay_policy: "0"
            overlay_tunnel_block: "<your_own_value>"
            remote_gw: "<your_own_value>"
            route_policy: "0"
            sdwan_member: "0"
        policy_rule: "health-check"
        psksecret: "<your_own_value>"
        sdwan_zone: "<your_own_value> (source system.sdwan.zone.name)"
        status: "enable"
        sync_mode: "enable"
        vpn_role: "hub"
```

## [Return Values](fortios_system_fabric_vpn_module.md#id6)

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
