---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_vpn_ipsec_phase1 module – Configure VPN remote gateway in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_vpn_ipsec_phase1_module.html
fetched_at: 2026-07-28T02:30:20+00:00
---
# fortinet.fortios.fortios_vpn_ipsec_phase1 module – Configure VPN remote gateway in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_vpn_ipsec_phase1_module.md#ansible-collections-fortinet-fortios-fortios-vpn-ipsec-phase1-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_vpn_ipsec_phase1`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_vpn_ipsec_phase1_module.md#synopsis)
- [Requirements](fortios_vpn_ipsec_phase1_module.md#requirements)
- [Parameters](fortios_vpn_ipsec_phase1_module.md#parameters)
- [Notes](fortios_vpn_ipsec_phase1_module.md#notes)
- [Examples](fortios_vpn_ipsec_phase1_module.md#examples)
- [Return Values](fortios_vpn_ipsec_phase1_module.md#return-values)

## [Synopsis](fortios_vpn_ipsec_phase1_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify vpn_ipsec feature and phase1 category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_vpn_ipsec_phase1_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_vpn_ipsec_phase1_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |
| **vpn_ipsec_phase1**  dictionary | Configure VPN remote gateway. |
| **acct_verify**  string | Enable/disable verification of RADIUS accounting record.  **Choices:**   - `"enable"` - `"disable"` |
| **add_gw_route**  string | Enable/disable automatically add a route to the remote gateway.  **Choices:**   - `"enable"` - `"disable"` |
| **add_route**  string | Enable/disable control addition of a route to peer destination selector.  **Choices:**   - `"disable"` - `"enable"` |
| **assign_ip**  string | Enable/disable assignment of IP to IPsec interface via configuration method.  **Choices:**   - `"disable"` - `"enable"` |
| **assign_ip_from**  string | Method by which the IP address will be assigned.  **Choices:**   - `"range"` - `"usrgrp"` - `"dhcp"` - `"name"` |
| **authmethod**  string | Authentication method.  **Choices:**   - `"psk"` - `"signature"` |
| **authmethod_remote**  string | Authentication method (remote side).  **Choices:**   - `"psk"` - `"signature"` |
| **authpasswd**  string | XAuth password (max 35 characters). |
| **authusr**  string | XAuth user name. |
| **authusrgrp**  string | Authentication user group. Source user.group.name. |
| **auto_negotiate**  string | Enable/disable automatic initiation of IKE SA negotiation.  **Choices:**   - `"enable"` - `"disable"` |
| **backup_gateway**  list / elements=dictionary | Instruct unity clients about the backup gateway address(es). |
| **address**  string / required | Address of backup gateway. |
| **banner**  string | Message that unity client should display after connecting. |
| **cert_id_validation**  string | Enable/disable cross validation of peer ID and the identity in the peer”s certificate as specified in RFC 4945.  **Choices:**   - `"enable"` - `"disable"` |
| **certificate**  list / elements=dictionary | Names of up to 4 signed personal certificates. |
| **name**  string / required | Certificate name. Source vpn.certificate.local.name. |
| **childless_ike**  string | Enable/disable childless IKEv2 initiation (RFC 6023).  **Choices:**   - `"enable"` - `"disable"` |
| **client_auto_negotiate**  string | Enable/disable allowing the VPN client to bring up the tunnel when there is no traffic.  **Choices:**   - `"disable"` - `"enable"` |
| **client_keep_alive**  string | Enable/disable allowing the VPN client to keep the tunnel up when there is no traffic.  **Choices:**   - `"disable"` - `"enable"` |
| **comments**  string | Comment. |
| **dhcp6_ra_linkaddr**  string | Relay agent IPv6 link address to use in DHCP6 requests. |
| **dhcp_ra_giaddr**  string | Relay agent gateway IP address to use in the giaddr field of DHCP requests. |
| **dhgrp**  list / elements=string | DH group.  **Choices:**   - `"1"` - `"2"` - `"5"` - `"14"` - `"15"` - `"16"` - `"17"` - `"18"` - `"19"` - `"20"` - `"21"` - `"27"` - `"28"` - `"29"` - `"30"` - `"31"` - `"32"` |
| **digital_signature_auth**  string | Enable/disable IKEv2 Digital Signature Authentication (RFC 7427).  **Choices:**   - `"enable"` - `"disable"` |
| **distance**  integer | Distance for routes added by IKE (1 - 255). |
| **dns_mode**  string | DNS server mode.  **Choices:**   - `"manual"` - `"auto"` |
| **domain**  string | Instruct unity clients about the single default DNS domain. |
| **dpd**  string | Dead Peer Detection mode.  **Choices:**   - `"disable"` - `"on-idle"` - `"on-demand"` |
| **dpd_retrycount**  integer | Number of DPD retry attempts. |
| **dpd_retryinterval**  string | DPD retry interval. |
| **eap**  string | Enable/disable IKEv2 EAP authentication.  **Choices:**   - `"enable"` - `"disable"` |
| **eap_exclude_peergrp**  string | Peer group excluded from EAP authentication. Source user.peergrp.name. |
| **eap_identity**  string | IKEv2 EAP peer identity type.  **Choices:**   - `"use-id-payload"` - `"send-request"` |
| **enforce_unique_id**  string | Enable/disable peer ID uniqueness check.  **Choices:**   - `"disable"` - `"keep-new"` - `"keep-old"` |
| **esn**  string | Extended sequence number (ESN) negotiation.  **Choices:**   - `"require"` - `"allow"` - `"disable"` |
| **fec_base**  integer | Number of base Forward Error Correction packets (1 - 20). |
| **fec_codec**  string | Forward Error Correction encoding/decoding algorithm.  **Choices:**   - `"rs"` - `"xor"` |
| **fec_egress**  string | Enable/disable Forward Error Correction for egress IPsec traffic.  **Choices:**   - `"enable"` - `"disable"` |
| **fec_health_check**  string | SD-WAN health check. Source system.sdwan.health-check.name. |
| **fec_ingress**  string | Enable/disable Forward Error Correction for ingress IPsec traffic.  **Choices:**   - `"enable"` - `"disable"` |
| **fec_mapping_profile**  string | Forward Error Correction (FEC) mapping profile. |
| **fec_receive_timeout**  integer | Timeout in milliseconds before dropping Forward Error Correction packets (1 - 1000). |
| **fec_redundant**  integer | Number of redundant Forward Error Correction packets (1 - 5 for reed-solomon, 1 for xor). |
| **fec_send_timeout**  integer | Timeout in milliseconds before sending Forward Error Correction packets (1 - 1000). |
| **fgsp_sync**  string | Enable/disable IPsec syncing of tunnels for FGSP IPsec.  **Choices:**   - `"enable"` - `"disable"` |
| **forticlient_enforcement**  string | Enable/disable FortiClient enforcement.  **Choices:**   - `"enable"` - `"disable"` |
| **fragmentation**  string | Enable/disable fragment IKE message on re-transmission.  **Choices:**   - `"enable"` - `"disable"` |
| **fragmentation_mtu**  integer | IKE fragmentation MTU (500 - 16000). |
| **group_authentication**  string | Enable/disable IKEv2 IDi group authentication.  **Choices:**   - `"enable"` - `"disable"` |
| **group_authentication_secret**  string | Password for IKEv2 ID group authentication. ASCII string or hexadecimal indicated by a leading 0x. |
| **ha_sync_esp_seqno**  string | Enable/disable sequence number jump ahead for IPsec HA.  **Choices:**   - `"enable"` - `"disable"` |
| **idle_timeout**  string | Enable/disable IPsec tunnel idle timeout.  **Choices:**   - `"enable"` - `"disable"` |
| **idle_timeoutinterval**  integer | IPsec tunnel idle timeout in minutes (5 - 43200). |
| **ike_version**  string | IKE protocol version.  **Choices:**   - `"1"` - `"2"` |
| **inbound_dscp_copy**  string | Enable/disable copy the dscp in the ESP header to the inner IP Header.  **Choices:**   - `"enable"` - `"disable"` |
| **include_local_lan**  string | Enable/disable allow local LAN access on unity clients.  **Choices:**   - `"disable"` - `"enable"` |
| **interface**  string | Local physical, aggregate, or VLAN outgoing interface. Source system.interface.name. |
| **internal_domain_list**  list / elements=dictionary | One or more internal domain names in quotes separated by spaces. |
| **domain_name**  string / required | Domain name. |
| **ip_delay_interval**  integer | IP address reuse delay interval in seconds (0 - 28800). |
| **ipv4_dns_server1**  string | IPv4 DNS server 1. |
| **ipv4_dns_server2**  string | IPv4 DNS server 2. |
| **ipv4_dns_server3**  string | IPv4 DNS server 3. |
| **ipv4_end_ip**  string | End of IPv4 range. |
| **ipv4_exclude_range**  list / elements=dictionary | Configuration Method IPv4 exclude ranges. |
| **end_ip**  string | End of IPv4 exclusive range. |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **start_ip**  string | Start of IPv4 exclusive range. |
| **ipv4_name**  string | IPv4 address name. Source firewall.address.name firewall.addrgrp.name. |
| **ipv4_netmask**  string | IPv4 Netmask. |
| **ipv4_split_exclude**  string | IPv4 subnets that should not be sent over the IPsec tunnel. Source firewall.address.name firewall.addrgrp.name. |
| **ipv4_split_include**  string | IPv4 split-include subnets. Source firewall.address.name firewall.addrgrp.name. |
| **ipv4_start_ip**  string | Start of IPv4 range. |
| **ipv4_wins_server1**  string | WINS server 1. |
| **ipv4_wins_server2**  string | WINS server 2. |
| **ipv6_dns_server1**  string | IPv6 DNS server 1. |
| **ipv6_dns_server2**  string | IPv6 DNS server 2. |
| **ipv6_dns_server3**  string | IPv6 DNS server 3. |
| **ipv6_end_ip**  string | End of IPv6 range. |
| **ipv6_exclude_range**  list / elements=dictionary | Configuration method IPv6 exclude ranges. |
| **end_ip**  string | End of IPv6 exclusive range. |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **start_ip**  string | Start of IPv6 exclusive range. |
| **ipv6_name**  string | IPv6 address name. Source firewall.address6.name firewall.addrgrp6.name. |
| **ipv6_prefix**  integer | IPv6 prefix. |
| **ipv6_split_exclude**  string | IPv6 subnets that should not be sent over the IPsec tunnel. Source firewall.address6.name firewall.addrgrp6.name. |
| **ipv6_split_include**  string | IPv6 split-include subnets. Source firewall.address6.name firewall.addrgrp6.name. |
| **ipv6_start_ip**  string | Start of IPv6 range. |
| **keepalive**  integer | NAT-T keep alive interval. |
| **keylife**  integer | Time to wait in seconds before phase 1 encryption key expires. |
| **local_gw**  string | Local VPN gateway. |
| **localid**  string | Local ID. |
| **localid_type**  string | Local ID type.  **Choices:**   - `"auto"` - `"fqdn"` - `"user-fqdn"` - `"keyid"` - `"address"` - `"asn1dn"` |
| **loopback_asymroute**  string | Enable/disable asymmetric routing for IKE traffic on loopback interface.  **Choices:**   - `"enable"` - `"disable"` |
| **mesh_selector_type**  string | Add selectors containing subsets of the configuration depending on traffic.  **Choices:**   - `"disable"` - `"subnet"` - `"host"` |
| **mode**  string | ID protection mode used to establish a secure channel.  **Choices:**   - `"aggressive"` - `"main"` |
| **mode_cfg**  string | Enable/disable configuration method.  **Choices:**   - `"disable"` - `"enable"` |
| **mode_cfg_allow_client_selector**  string | Enable/disable mode-cfg client to use custom phase2 selectors.  **Choices:**   - `"disable"` - `"enable"` |
| **name**  string / required | IPsec remote gateway name. |
| **nattraversal**  string | Enable/disable NAT traversal.  **Choices:**   - `"enable"` - `"disable"` - `"forced"` |
| **negotiate_timeout**  integer | IKE SA negotiation timeout in seconds (1 - 300). |
| **network_id**  integer | VPN gateway network ID. |
| **network_overlay**  string | Enable/disable network overlays.  **Choices:**   - `"disable"` - `"enable"` |
| **npu_offload**  string | Enable/disable offloading NPU.  **Choices:**   - `"enable"` - `"disable"` |
| **peer**  string | Accept this peer certificate. Source user.peer.name. |
| **peergrp**  string | Accept this peer certificate group. Source user.peergrp.name. |
| **peerid**  string | Accept this peer identity. |
| **peertype**  string | Accept this peer type.  **Choices:**   - `"any"` - `"one"` - `"dialup"` - `"peer"` - `"peergrp"` |
| **ppk**  string | Enable/disable IKEv2 Postquantum Preshared Key (PPK).  **Choices:**   - `"disable"` - `"allow"` - `"require"` |
| **ppk_identity**  string | IKEv2 Postquantum Preshared Key Identity. |
| **ppk_secret**  string | IKEv2 Postquantum Preshared Key (ASCII string or hexadecimal encoded with a leading 0x). |
| **priority**  integer | Priority for routes added by IKE (1 - 65535). |
| **proposal**  list / elements=string | Phase1 proposal.  **Choices:**   - `"des-md5"` - `"des-sha1"` - `"des-sha256"` - `"des-sha384"` - `"des-sha512"` - `"3des-md5"` - `"3des-sha1"` - `"3des-sha256"` - `"3des-sha384"` - `"3des-sha512"` - `"aes128-md5"` - `"aes128-sha1"` - `"aes128-sha256"` - `"aes128-sha384"` - `"aes128-sha512"` - `"aes128gcm-prfsha1"` - `"aes128gcm-prfsha256"` - `"aes128gcm-prfsha384"` - `"aes128gcm-prfsha512"` - `"aes192-md5"` - `"aes192-sha1"` - `"aes192-sha256"` - `"aes192-sha384"` - `"aes192-sha512"` - `"aes256-md5"` - `"aes256-sha1"` - `"aes256-sha256"` - `"aes256-sha384"` - `"aes256-sha512"` - `"aes256gcm-prfsha1"` - `"aes256gcm-prfsha256"` - `"aes256gcm-prfsha384"` - `"aes256gcm-prfsha512"` - `"chacha20poly1305-prfsha1"` - `"chacha20poly1305-prfsha256"` - `"chacha20poly1305-prfsha384"` - `"chacha20poly1305-prfsha512"` - `"aria128-md5"` - `"aria128-sha1"` - `"aria128-sha256"` - `"aria128-sha384"` - `"aria128-sha512"` - `"aria192-md5"` - `"aria192-sha1"` - `"aria192-sha256"` - `"aria192-sha384"` - `"aria192-sha512"` - `"aria256-md5"` - `"aria256-sha1"` - `"aria256-sha256"` - `"aria256-sha384"` - `"aria256-sha512"` - `"seed-md5"` - `"seed-sha1"` - `"seed-sha256"` - `"seed-sha384"` - `"seed-sha512"` |
| **psksecret**  string | Pre-shared secret for PSK authentication (ASCII string or hexadecimal encoded with a leading 0x). |
| **psksecret_remote**  string | Pre-shared secret for remote side PSK authentication (ASCII string or hexadecimal encoded with a leading 0x). |
| **reauth**  string | Enable/disable re-authentication upon IKE SA lifetime expiration.  **Choices:**   - `"disable"` - `"enable"` |
| **rekey**  string | Enable/disable phase1 rekey.  **Choices:**   - `"enable"` - `"disable"` |
| **remote_gw**  string | Remote VPN gateway. |
| **remotegw_ddns**  string | Domain name of remote gateway. For example, name.ddns.com. |
| **rsa_signature_format**  string | Digital Signature Authentication RSA signature format.  **Choices:**   - `"pkcs1"` - `"pss"` |
| **rsa_signature_hash_override**  string | Enable/disable IKEv2 RSA signature hash algorithm override.  **Choices:**   - `"enable"` - `"disable"` |
| **save_password**  string | Enable/disable saving XAuth username and password on VPN clients.  **Choices:**   - `"disable"` - `"enable"` |
| **send_cert_chain**  string | Enable/disable sending certificate chain.  **Choices:**   - `"enable"` - `"disable"` |
| **signature_hash_alg**  list / elements=string | Digital Signature Authentication hash algorithms.  **Choices:**   - `"sha1"` - `"sha2-256"` - `"sha2-384"` - `"sha2-512"` |
| **split_include_service**  string | Split-include services. Source firewall.service.group.name firewall.service.custom.name. |
| **suite_b**  string | Use Suite-B.  **Choices:**   - `"disable"` - `"suite-b-gcm-128"` - `"suite-b-gcm-256"` |
| **type**  string | Remote gateway type.  **Choices:**   - `"static"` - `"dynamic"` - `"ddns"` |
| **unity_support**  string | Enable/disable support for Cisco UNITY Configuration Method extensions.  **Choices:**   - `"disable"` - `"enable"` |
| **usrgrp**  string | User group name for dialup peers. Source user.group.name. |
| **wizard_type**  string | GUI VPN Wizard Type.  **Choices:**   - `"custom"` - `"dialup-forticlient"` - `"dialup-ios"` - `"dialup-android"` - `"dialup-windows"` - `"dialup-cisco"` - `"static-fortigate"` - `"dialup-fortigate"` - `"static-cisco"` - `"dialup-cisco-fw"` - `"simplified-static-fortigate"` - `"hub-fortigate-auto-discovery"` - `"spoke-fortigate-auto-discovery"` |
| **xauthtype**  string | XAuth type.  **Choices:**   - `"disable"` - `"client"` - `"pap"` - `"chap"` - `"auto"` |

## [Notes](fortios_vpn_ipsec_phase1_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_vpn_ipsec_phase1_module.md#id5)

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
  - name: Configure VPN remote gateway.
    fortios_vpn_ipsec_phase1:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      vpn_ipsec_phase1:
        acct_verify: "enable"
        add_gw_route: "enable"
        add_route: "disable"
        assign_ip: "disable"
        assign_ip_from: "range"
        authmethod: "psk"
        authmethod_remote: "psk"
        authpasswd: "<your_own_value>"
        authusr: "<your_own_value>"
        authusrgrp: "<your_own_value> (source user.group.name)"
        auto_negotiate: "enable"
        backup_gateway:
         -
            address: "<your_own_value>"
        banner: "<your_own_value>"
        cert_id_validation: "enable"
        certificate:
         -
            name: "default_name_19 (source vpn.certificate.local.name)"
        childless_ike: "enable"
        client_auto_negotiate: "disable"
        client_keep_alive: "disable"
        comments: "<your_own_value>"
        dhcp_ra_giaddr: "<your_own_value>"
        dhcp6_ra_linkaddr: "<your_own_value>"
        dhgrp: "1"
        digital_signature_auth: "enable"
        distance: "15"
        dns_mode: "manual"
        domain: "<your_own_value>"
        dpd: "disable"
        dpd_retrycount: "3"
        dpd_retryinterval: "<your_own_value>"
        eap: "enable"
        eap_exclude_peergrp: "<your_own_value> (source user.peergrp.name)"
        eap_identity: "use-id-payload"
        enforce_unique_id: "disable"
        esn: "require"
        fec_base: "10"
        fec_codec: "rs"
        fec_egress: "enable"
        fec_health_check: "<your_own_value> (source system.sdwan.health-check.name)"
        fec_ingress: "enable"
        fec_mapping_profile: "<your_own_value>"
        fec_receive_timeout: "50"
        fec_redundant: "1"
        fec_send_timeout: "5"
        fgsp_sync: "enable"
        forticlient_enforcement: "enable"
        fragmentation: "enable"
        fragmentation_mtu: "1200"
        group_authentication: "enable"
        group_authentication_secret: "<your_own_value>"
        ha_sync_esp_seqno: "enable"
        idle_timeout: "enable"
        idle_timeoutinterval: "15"
        ike_version: "1"
        inbound_dscp_copy: "enable"
        include_local_lan: "disable"
        interface: "<your_own_value> (source system.interface.name)"
        internal_domain_list:
         -
            domain_name: "<your_own_value>"
        ip_delay_interval: "0"
        ipv4_dns_server1: "<your_own_value>"
        ipv4_dns_server2: "<your_own_value>"
        ipv4_dns_server3: "<your_own_value>"
        ipv4_end_ip: "<your_own_value>"
        ipv4_exclude_range:
         -
            end_ip: "<your_own_value>"
            id:  "70"
            start_ip: "<your_own_value>"
        ipv4_name: "<your_own_value> (source firewall.address.name firewall.addrgrp.name)"
        ipv4_netmask: "<your_own_value>"
        ipv4_split_exclude: "<your_own_value> (source firewall.address.name firewall.addrgrp.name)"
        ipv4_split_include: "<your_own_value> (source firewall.address.name firewall.addrgrp.name)"
        ipv4_start_ip: "<your_own_value>"
        ipv4_wins_server1: "<your_own_value>"
        ipv4_wins_server2: "<your_own_value>"
        ipv6_dns_server1: "<your_own_value>"
        ipv6_dns_server2: "<your_own_value>"
        ipv6_dns_server3: "<your_own_value>"
        ipv6_end_ip: "<your_own_value>"
        ipv6_exclude_range:
         -
            end_ip: "<your_own_value>"
            id:  "85"
            start_ip: "<your_own_value>"
        ipv6_name: "<your_own_value> (source firewall.address6.name firewall.addrgrp6.name)"
        ipv6_prefix: "128"
        ipv6_split_exclude: "<your_own_value> (source firewall.address6.name firewall.addrgrp6.name)"
        ipv6_split_include: "<your_own_value> (source firewall.address6.name firewall.addrgrp6.name)"
        ipv6_start_ip: "<your_own_value>"
        keepalive: "10"
        keylife: "86400"
        local_gw: "<your_own_value>"
        localid: "<your_own_value>"
        localid_type: "auto"
        loopback_asymroute: "enable"
        mesh_selector_type: "disable"
        mode: "aggressive"
        mode_cfg: "disable"
        mode_cfg_allow_client_selector: "disable"
        name: "default_name_102"
        nattraversal: "enable"
        negotiate_timeout: "30"
        network_id: "0"
        network_overlay: "disable"
        npu_offload: "enable"
        peer: "<your_own_value> (source user.peer.name)"
        peergrp: "<your_own_value> (source user.peergrp.name)"
        peerid: "<your_own_value>"
        peertype: "any"
        ppk: "disable"
        ppk_identity: "<your_own_value>"
        ppk_secret: "<your_own_value>"
        priority: "1"
        proposal: "des-md5"
        psksecret: "<your_own_value>"
        psksecret_remote: "<your_own_value>"
        reauth: "disable"
        rekey: "enable"
        remote_gw: "<your_own_value>"
        remotegw_ddns: "<your_own_value>"
        rsa_signature_format: "pkcs1"
        rsa_signature_hash_override: "enable"
        save_password: "disable"
        send_cert_chain: "enable"
        signature_hash_alg: "sha1"
        split_include_service: "<your_own_value> (source firewall.service.group.name firewall.service.custom.name)"
        suite_b: "disable"
        type: "static"
        unity_support: "disable"
        usrgrp: "<your_own_value> (source user.group.name)"
        wizard_type: "custom"
        xauthtype: "disable"
```

## [Return Values](fortios_vpn_ipsec_phase1_module.md#id6)

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
