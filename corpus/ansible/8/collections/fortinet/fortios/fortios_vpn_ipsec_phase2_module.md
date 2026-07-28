---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_vpn_ipsec_phase2 module – Configure VPN autokey tunnel in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_vpn_ipsec_phase2_module.html
fetched_at: 2026-07-28T02:30:22+00:00
---
# fortinet.fortios.fortios_vpn_ipsec_phase2 module – Configure VPN autokey tunnel in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_vpn_ipsec_phase2_module.md#ansible-collections-fortinet-fortios-fortios-vpn-ipsec-phase2-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_vpn_ipsec_phase2`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_vpn_ipsec_phase2_module.md#synopsis)
- [Requirements](fortios_vpn_ipsec_phase2_module.md#requirements)
- [Parameters](fortios_vpn_ipsec_phase2_module.md#parameters)
- [Notes](fortios_vpn_ipsec_phase2_module.md#notes)
- [Examples](fortios_vpn_ipsec_phase2_module.md#examples)
- [Return Values](fortios_vpn_ipsec_phase2_module.md#return-values)

## [Synopsis](fortios_vpn_ipsec_phase2_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify vpn_ipsec feature and phase2 category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_vpn_ipsec_phase2_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_vpn_ipsec_phase2_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |
| **vpn_ipsec_phase2**  dictionary | Configure VPN autokey tunnel. |
| **add_route**  string | Enable/disable automatic route addition.  **Choices:**   - `"phase1"` - `"enable"` - `"disable"` |
| **auto_negotiate**  string | Enable/disable IPsec SA auto-negotiation.  **Choices:**   - `"enable"` - `"disable"` |
| **comments**  string | Comment. |
| **dhcp_ipsec**  string | Enable/disable DHCP-IPsec.  **Choices:**   - `"enable"` - `"disable"` |
| **dhgrp**  list / elements=string | Phase2 DH group.  **Choices:**   - `"1"` - `"2"` - `"5"` - `"14"` - `"15"` - `"16"` - `"17"` - `"18"` - `"19"` - `"20"` - `"21"` - `"27"` - `"28"` - `"29"` - `"30"` - `"31"` - `"32"` |
| **diffserv**  string | Enable/disable applying DSCP value to the IPsec tunnel outer IP header.  **Choices:**   - `"enable"` - `"disable"` |
| **diffservcode**  string | DSCP value to be applied to the IPsec tunnel outer IP header. |
| **dst_addr_type**  string | Remote proxy ID type.  **Choices:**   - `"subnet"` - `"range"` - `"ip"` - `"name"` |
| **dst_end_ip**  string | Remote proxy ID IPv4 end. |
| **dst_end_ip6**  string | Remote proxy ID IPv6 end. |
| **dst_name**  string | Remote proxy ID name. Source firewall.address.name firewall.addrgrp.name. |
| **dst_name6**  string | Remote proxy ID name. Source firewall.address6.name firewall.addrgrp6.name. |
| **dst_port**  integer | Quick mode destination port (1 - 65535 or 0 for all). |
| **dst_start_ip**  string | Remote proxy ID IPv4 start. |
| **dst_start_ip6**  string | Remote proxy ID IPv6 start. |
| **dst_subnet**  string | Remote proxy ID IPv4 subnet. |
| **dst_subnet6**  string | Remote proxy ID IPv6 subnet. |
| **encapsulation**  string | ESP encapsulation mode.  **Choices:**   - `"tunnel-mode"` - `"transport-mode"` |
| **inbound_dscp_copy**  string | Enable/disable copying of the DSCP in the ESP header to the inner IP header.  **Choices:**   - `"phase1"` - `"enable"` - `"disable"` |
| **initiator_ts_narrow**  string | Enable/disable traffic selector narrowing for IKEv2 initiator.  **Choices:**   - `"enable"` - `"disable"` |
| **ipv4_df**  string | Enable/disable setting and resetting of IPv4 “Don”t Fragment” bit.  **Choices:**   - `"enable"` - `"disable"` |
| **keepalive**  string | Enable/disable keep alive.  **Choices:**   - `"enable"` - `"disable"` |
| **keylife_type**  string | Keylife type.  **Choices:**   - `"seconds"` - `"kbs"` - `"both"` |
| **keylifekbs**  integer | Phase2 key life in number of kilobytes of traffic (5120 - 4294967295). |
| **keylifeseconds**  integer | Phase2 key life in time in seconds (120 - 172800). |
| **l2tp**  string | Enable/disable L2TP over IPsec.  **Choices:**   - `"enable"` - `"disable"` |
| **name**  string / required | IPsec tunnel name. |
| **pfs**  string | Enable/disable PFS feature.  **Choices:**   - `"enable"` - `"disable"` |
| **phase1name**  string | Phase 1 determines the options required for phase 2. Source vpn.ipsec.phase1.name. |
| **proposal**  list / elements=string | Phase2 proposal.  **Choices:**   - `"null-md5"` - `"null-sha1"` - `"null-sha256"` - `"null-sha384"` - `"null-sha512"` - `"des-null"` - `"des-md5"` - `"des-sha1"` - `"des-sha256"` - `"des-sha384"` - `"des-sha512"` - `"3des-null"` - `"3des-md5"` - `"3des-sha1"` - `"3des-sha256"` - `"3des-sha384"` - `"3des-sha512"` - `"aes128-null"` - `"aes128-md5"` - `"aes128-sha1"` - `"aes128-sha256"` - `"aes128-sha384"` - `"aes128-sha512"` - `"aes128gcm"` - `"aes192-null"` - `"aes192-md5"` - `"aes192-sha1"` - `"aes192-sha256"` - `"aes192-sha384"` - `"aes192-sha512"` - `"aes256-null"` - `"aes256-md5"` - `"aes256-sha1"` - `"aes256-sha256"` - `"aes256-sha384"` - `"aes256-sha512"` - `"aes256gcm"` - `"chacha20poly1305"` - `"aria128-null"` - `"aria128-md5"` - `"aria128-sha1"` - `"aria128-sha256"` - `"aria128-sha384"` - `"aria128-sha512"` - `"aria192-null"` - `"aria192-md5"` - `"aria192-sha1"` - `"aria192-sha256"` - `"aria192-sha384"` - `"aria192-sha512"` - `"aria256-null"` - `"aria256-md5"` - `"aria256-sha1"` - `"aria256-sha256"` - `"aria256-sha384"` - `"aria256-sha512"` - `"seed-null"` - `"seed-md5"` - `"seed-sha1"` - `"seed-sha256"` - `"seed-sha384"` - `"seed-sha512"` |
| **protocol**  integer | Quick mode protocol selector (1 - 255 or 0 for all). |
| **replay**  string | Enable/disable replay detection.  **Choices:**   - `"enable"` - `"disable"` |
| **route_overlap**  string | Action for overlapping routes.  **Choices:**   - `"use-old"` - `"use-new"` - `"allow"` |
| **selector_match**  string | Match type to use when comparing selectors.  **Choices:**   - `"exact"` - `"subset"` - `"auto"` |
| **single_source**  string | Enable/disable single source IP restriction.  **Choices:**   - `"enable"` - `"disable"` |
| **src_addr_type**  string | Local proxy ID type.  **Choices:**   - `"subnet"` - `"range"` - `"ip"` - `"name"` |
| **src_end_ip**  string | Local proxy ID end. |
| **src_end_ip6**  string | Local proxy ID IPv6 end. |
| **src_name**  string | Local proxy ID name. Source firewall.address.name firewall.addrgrp.name. |
| **src_name6**  string | Local proxy ID name. Source firewall.address6.name firewall.addrgrp6.name. |
| **src_port**  integer | Quick mode source port (1 - 65535 or 0 for all). |
| **src_start_ip**  string | Local proxy ID start. |
| **src_start_ip6**  string | Local proxy ID IPv6 start. |
| **src_subnet**  string | Local proxy ID subnet. |
| **src_subnet6**  string | Local proxy ID IPv6 subnet. |
| **use_natip**  string | Enable to use the FortiGate public IP as the source selector when outbound NAT is used.  **Choices:**   - `"enable"` - `"disable"` |

## [Notes](fortios_vpn_ipsec_phase2_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_vpn_ipsec_phase2_module.md#id5)

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
  - name: Configure VPN autokey tunnel.
    fortios_vpn_ipsec_phase2:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      vpn_ipsec_phase2:
        add_route: "phase1"
        auto_negotiate: "enable"
        comments: "<your_own_value>"
        dhcp_ipsec: "enable"
        dhgrp: "1"
        diffserv: "enable"
        diffservcode: "<your_own_value>"
        dst_addr_type: "subnet"
        dst_end_ip: "<your_own_value>"
        dst_end_ip6: "<your_own_value>"
        dst_name: "<your_own_value> (source firewall.address.name firewall.addrgrp.name)"
        dst_name6: "<your_own_value> (source firewall.address6.name firewall.addrgrp6.name)"
        dst_port: "0"
        dst_start_ip: "<your_own_value>"
        dst_start_ip6: "<your_own_value>"
        dst_subnet: "<your_own_value>"
        dst_subnet6: "<your_own_value>"
        encapsulation: "tunnel-mode"
        inbound_dscp_copy: "phase1"
        initiator_ts_narrow: "enable"
        ipv4_df: "enable"
        keepalive: "enable"
        keylife_type: "seconds"
        keylifekbs: "5120"
        keylifeseconds: "43200"
        l2tp: "enable"
        name: "default_name_29"
        pfs: "enable"
        phase1name: "<your_own_value> (source vpn.ipsec.phase1.name)"
        proposal: "null-md5"
        protocol: "0"
        replay: "enable"
        route_overlap: "use-old"
        selector_match: "exact"
        single_source: "enable"
        src_addr_type: "subnet"
        src_end_ip: "<your_own_value>"
        src_end_ip6: "<your_own_value>"
        src_name: "<your_own_value> (source firewall.address.name firewall.addrgrp.name)"
        src_name6: "<your_own_value> (source firewall.address6.name firewall.addrgrp6.name)"
        src_port: "0"
        src_start_ip: "<your_own_value>"
        src_start_ip6: "<your_own_value>"
        src_subnet: "<your_own_value>"
        src_subnet6: "<your_own_value>"
        use_natip: "enable"
```

## [Return Values](fortios_vpn_ipsec_phase2_module.md#id6)

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
