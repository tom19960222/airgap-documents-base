---
collection: ansible
version: "8"
title: "cisco.ios.ios_snmp_server module – Resource module to configure snmp server."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ios/ios_snmp_server_module.html
fetched_at: 2026-07-28T01:26:27+00:00
---
# cisco.ios.ios_snmp_server module – Resource module to configure snmp server.

> **Note:**
>
> This module is part of the [cisco.ios collection](https://galaxy.ansible.com/ui/repo/published/cisco/ios/) (version 4.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ios`.
>
> To use it in a playbook, specify: `cisco.ios.ios_snmp_server`.

New in cisco.ios 2.6.0

- [Synopsis](ios_snmp_server_module.md#synopsis)
- [Parameters](ios_snmp_server_module.md#parameters)
- [Notes](ios_snmp_server_module.md#notes)
- [Examples](ios_snmp_server_module.md#examples)
- [Return Values](ios_snmp_server_module.md#return-values)

## [Synopsis](ios_snmp_server_module.md#id1)

- This module provides declarative management of SNMP server on Cisco IOS devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: snmp_server

## [Parameters](ios_snmp_server_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dictionary of SNMP server configuration |
| **accounting**  dictionary | SNMP Accounting parameters |
| **command**  string | For SNMP set commands |
| **cache**  integer | Enable SNMP cache and MIB expiry interval |
| **chassis_id**  string | String to uniquely identify this chassis (Hexadecimal) |
| **communities**  list / elements=dictionary | Community name configuration. |
| **acl_v4**  string | standard access-list name |
| **acl_v6**  string | IPv6 access list name |
| **name**  string | Community name (default RO) |
| **ro**  boolean | Only reads are permitted  **Choices:**   - `false` - `true` |
| **rw**  boolean | Read-write access  **Choices:**   - `false` - `true` |
| **view**  string | MIB view name |
| **contact**  string | Text for mib object sysContact |
| **context**  list / elements=string | Create/Delete a context apart from default |
| **drop**  dictionary | Silently drop SNMP packets |
| **unknown_user**  boolean | Silently drop unknown v3 user packets  **Choices:**   - `false` - `true` |
| **vrf_traffic**  boolean | Silently drop SNMP packets that come on VRF interfaces  **Choices:**   - `false` - `true` |
| **engine_id**  list / elements=dictionary | Configure a local or remote SNMPv3 engineID |
| **id**  string | engine ID octet string |
| **local**  boolean | Local SNMP agent  **Choices:**   - `false` - `true` |
| **remote**  dictionary | Remote SNMP agent |
| **host**  string | Hostname or IP address of remote SNMP notification host |
| **udp_port**  integer | The remote SNMP notification host’s UDP port number. |
| **vrf**  string | The remote notification host’s VPN routing instance |
| **file_transfer**  dictionary | File transfer related commands |
| **access_group**  string | Access control for file transfers |
| **protocol**  list / elements=string | Access control protocol for file transfers |
| **groups**  list / elements=dictionary | Define a User Security Model group |
| **acl_v4**  string | specify an access-list associated with this group |
| **acl_v6**  string | specify an access-list associated with this group |
| **context**  string | Specify a context to associate with the group |
| **group**  string | SNMP group for the user |
| **notify**  string | View to restrict notifications |
| **read**  string | View to restrict read access |
| **version**  string | snmp security group version  **Choices:**   - `"v1"` - `"v3"` - `"v2c"` |
| **version_option**  string | community name to the host.  **Choices:**   - `"auth"` - `"noauth"` - `"priv"` |
| **write**  string | View to restrict write access |
| **hosts**  list / elements=dictionary | Specify hosts to receive SNMP notifications |
| **community_string**  string | SNMPv1/v2c community string or SNMPv3 user name |
| **host**  string | Hostname or IP address of SNMP notification host. |
| **informs**  boolean | Use SNMP inform messages.  **Choices:**   - `false` - `true` |
| **traps**  list / elements=string | Use SNMP trap messages |
| **version**  string | Notification message SNMP version.  **Choices:**   - `"1"` - `"2c"` - `"3"` |
| **version_option**  string | community name to the host.  **Choices:**   - `"auth"` - `"noauth"` - `"priv"` |
| **vrf**  string | Specify the VRF in which the host is configured |
| **if_index**  boolean | Enable ifindex persistence  **Choices:**   - `false` - `true` |
| **inform**  dictionary | Configure SNMP Informs options |
| **pending**  integer | Set number of unacked informs to hold |
| **retries**  integer | Set retry count for informs |
| **timeout**  integer | Set timeout for informs |
| **ip**  dictionary | IP ToS configuration for SNMP traffic |
| **dscp**  integer | IP DSCP value for SNMP traffic |
| **precedence**  integer | IP Precedence value for SNMP traffic |
| **location**  string | Text for mib object sysLocation |
| **manager**  integer | Modify SNMP manager parameters |
| **packet_size**  integer | Largest SNMP packet size |
| **password_policy**  list / elements=dictionary | SNMP v3 users password policy |
| **change**  integer | Number of Character changes b/w old and new password |
| **digits**  integer | Number of digits |
| **lower_case**  integer | Number of lower-case characters |
| **max_len**  integer | Maximum password length |
| **min_len**  integer | Minimum password length |
| **policy_name**  string | Name of the policy |
| **special_char**  integer | Number of special case character |
| **upper_case**  integer | Number of upper-case characters |
| **username**  string | Name of the user |
| **queue_length**  integer | Message queue length for each TRAP host |
| **source_interface**  string | Source interface to be used for sending out SNMP notifications. |
| **system_shutdown**  boolean | Enable use of the SNMP reload command  **Choices:**   - `false` - `true` |
| **trap_source**  string | Assign an interface for the source address of all traps |
| **trap_timeout**  integer | Set timeout for TRAP message retransmissions |
| **traps**  dictionary | Enable SNMP Traps |
| **auth_framework**  dictionary | Enable SNMP CISCO-AUTH-FRAMEWORK-MIB traps |
| **enable**  boolean | Enable/disable auth framework  **Choices:**   - `false` - `true` |
| **sec_violation**  boolean | Mode sec_violation  **Choices:**   - `false` - `true` |
| **bfd**  dictionary | Allow SNMP BFD traps |
| **enable**  boolean | Enable/disable bfd  **Choices:**   - `false` - `true` |
| **session_down**  boolean | Enable BFD session down traps  **Choices:**   - `false` - `true` |
| **session_up**  boolean | Enable BFD session up traps  **Choices:**   - `false` - `true` |
| **bgp**  dictionary | Allow bgp traps |
| **cbgp2**  boolean | Enable BGP MIBv2 traps  **Choices:**   - `false` - `true` |
| **enable**  boolean | Enable/disable bgp traps  **Choices:**   - `false` - `true` |
| **state_changes**  dictionary | Traps for FSM state changes |
| **all**  boolean | CISCO specific trap for all fsm state changes  **Choices:**   - `false` - `true` |
| **backward_trans**  boolean | CISCO specific trap for backward transition  **Choices:**   - `false` - `true` |
| **enable**  boolean | Enable/disable bgp state_changes traps  **Choices:**   - `false` - `true` |
| **limited**  boolean | Trap for standard backward transition and established  **Choices:**   - `false` - `true` |
| **threshold**  dictionary | Mode threshold |
| **prefix**  boolean | Enable/disable bgp threshold traps  **Choices:**   - `false` - `true` |
| **bridge**  dictionary | Allow bridge related traps |
| **enable**  boolean | Enable/disable bridge traps  **Choices:**   - `false` - `true` |
| **newroot**  boolean | Enable SNMP STP Bridge MIB newroot traps  **Choices:**   - `false` - `true` |
| **topologychange**  boolean | Enable SNMP STP Bridge MIB topologychange traps  **Choices:**   - `false` - `true` |
| **casa**  boolean | Enable SNMP config casa traps  **Choices:**   - `false` - `true` |
| **cef**  dictionary | Allow cef related traps |
| **enable**  boolean | Enable/disable cef traps  **Choices:**   - `false` - `true` |
| **inconsistency**  boolean | Enable SNMP CEF Inconsistency traps  **Choices:**   - `false` - `true` |
| **peer_fib_state_change**  boolean | Enable SNMP CEF Peer FIB State change traps  **Choices:**   - `false` - `true` |
| **peer_state_change**  boolean | Enable SNMP CEF Peer state change traps  **Choices:**   - `false` - `true` |
| **resource_failure**  boolean | Enable SNMP CEF Resource Failure traps  **Choices:**   - `false` - `true` |
| **cnpd**  boolean | Enable SNMP cnpd traps  **Choices:**   - `false` - `true` |
| **config**  boolean | Enable SNMP config traps  **Choices:**   - `false` - `true` |
| **config_copy**  boolean | Enable SNMP config copy traps  **Choices:**   - `false` - `true` |
| **config_ctid**  boolean | Enable SNMP config ctid traps  **Choices:**   - `false` - `true` |
| **cpu**  dictionary | Allow CPU related traps |
| **enable**  boolean | Enable/disable cpu traps  **Choices:**   - `false` - `true` |
| **threshold**  boolean | Mode threshold  **Choices:**   - `false` - `true` |
| **dhcp**  boolean | Enable SNMP dhcp traps  **Choices:**   - `false` - `true` |
| **dlsw**  dictionary | Allow dlsw related traps |
| **circuit**  boolean | Enable SNMP dlsw circuit traps  **Choices:**   - `false` - `true` |
| **enable**  boolean | Enable/disable cef traps  **Choices:**   - `false` - `true` |
| **tconn**  boolean | Enable SNMP dlsw peer transport connection traps  **Choices:**   - `false` - `true` |
| **eigrp**  boolean | Enable SNMP eigrp traps  **Choices:**   - `false` - `true` |
| **energywise**  boolean | Enable SNMP energywise traps  **Choices:**   - `false` - `true` |
| **entity**  boolean | Enable SNMP entity traps  **Choices:**   - `false` - `true` |
| **envmon**  dictionary | Allow envmon related traps |
| **fan**  dictionary | Enable SNMP envmon fan traps |
| **enable**  boolean | Enable/disable fan traps  **Choices:**   - `false` - `true` |
| **shutdown**  boolean | Enable SNMP environmental monitor shutdown traps  **Choices:**   - `false` - `true` |
| **status**  boolean | Enable SNMP environmental status change traps  **Choices:**   - `false` - `true` |
| **supply**  boolean | Enable SNMP environmental monitor supply traps  **Choices:**   - `false` - `true` |
| **temperature**  boolean | Enable SNMP environmental monitor temperature traps  **Choices:**   - `false` - `true` |
| **shutdown**  boolean | Enable SNMP environmental monitor shutdown traps  **Choices:**   - `false` - `true` |
| **status**  boolean | Enable SNMP environmental status change traps  **Choices:**   - `false` - `true` |
| **supply**  boolean | Enable SNMP environmental monitor supply traps  **Choices:**   - `false` - `true` |
| **temperature**  boolean | Enable SNMP environmental monitor temperature traps  **Choices:**   - `false` - `true` |
| **ethernet**  dictionary | Allow ethernet traps |
| **cfm**  dictionary | Enable SNMP Ethernet CFM traps |
| **alarm**  boolean | Enable SNMP Ethernet CFM fault alarm trap  **Choices:**   - `false` - `true` |
| **cc**  dictionary | Enable SNMP Ethernet CC trap |
| **config**  boolean | Enable SNMP Ethernet CFM configuration error traps  **Choices:**   - `false` - `true` |
| **cross_connect**  boolean | Enable SNMP Ethernet CFM cross-connect traps  **Choices:**   - `false` - `true` |
| **loop**  boolean | Enable SNMP Ethernet CFM loop traps  **Choices:**   - `false` - `true` |
| **mep_down**  boolean | Enable SNMP Ethernet CFM CC Down traps  **Choices:**   - `false` - `true` |
| **mep_up**  boolean | Enable SNMP Ethernet CFM CC Up traps  **Choices:**   - `false` - `true` |
| **crosscheck**  dictionary | Enable SNMP Ethernet CC crosscheck trap |
| **mep_missing**  boolean | Enable SNMP Ethernet CC crosscheck missing trap  **Choices:**   - `false` - `true` |
| **mep_unknown**  boolean | Enable SNMP Ethernet CC crosscheck unknown traps  **Choices:**   - `false` - `true` |
| **service_up**  boolean | Enable SNMP Ethernet CC crosscheck service traps  **Choices:**   - `false` - `true` |
| **evc**  dictionary | Enable SNMP Ethernet EVC traps |
| **create**  boolean | Enable SNMP Ethernet EVC create traps  **Choices:**   - `false` - `true` |
| **delete**  boolean | Enable SNMP Ethernet EVC delete traps  **Choices:**   - `false` - `true` |
| **status**  boolean | Enable SNMP Ethernet EVC status traps  **Choices:**   - `false` - `true` |
| **event_manager**  boolean | Enable SNMP event-manager traps  **Choices:**   - `false` - `true` |
| **firewall**  dictionary | Enable SNMP firewall traps |
| **enable**  boolean | Enable/disable firewall traps  **Choices:**   - `false` - `true` |
| **serverstatus**  boolean | Enable firewall server status change trap  **Choices:**   - `false` - `true` |
| **flowmon**  boolean | Enable SNMP flowmon traps  **Choices:**   - `false` - `true` |
| **frame_relay**  dictionary | Allow frame-relay traps |
| **enable**  boolean | Enable/disable frame-relay traps  **Choices:**   - `false` - `true` |
| **subif**  dictionary | Enable SNMP frame-relay subinterface traps |
| **count**  integer | Maximum number of traps sent per interval |
| **enable**  boolean | Enable/disable subif traps  **Choices:**   - `false` - `true` |
| **interval**  integer | Interval duration in which to limit the number of traps sent |
| **fru_ctrl**  boolean | Enable SNMP fru-ctrl traps  **Choices:**   - `false` - `true` |
| **hsrp**  boolean | Enable SNMP hsrp traps  **Choices:**   - `false` - `true` |
| **ike**  dictionary | Allow ike traps |
| **policy**  dictionary | Enable IKE Policy traps |
| **add**  boolean | Enable IKE Policy add trap  **Choices:**   - `false` - `true` |
| **delete**  boolean | Enable IKE Policy delete trap  **Choices:**   - `false` - `true` |
| **tunnel**  dictionary | Enable IKE Tunnel traps |
| **start**  boolean | Enable IKE Tunnel start trap  **Choices:**   - `false` - `true` |
| **stop**  boolean | Enable IKE Tunnel stop trap  **Choices:**   - `false` - `true` |
| **ipmulticast**  boolean | Enable SNMP ip multi cast traps  **Choices:**   - `false` - `true` |
| **ipsec**  dictionary | Allow ike traps |
| **cryptomap**  dictionary | Enable IPsec Cryptomap traps |
| **add**  boolean | Enable IPsec Cryptomap add trap  **Choices:**   - `false` - `true` |
| **attach**  boolean | Enable IPsec Cryptomap Attach trap  **Choices:**   - `false` - `true` |
| **delete**  boolean | Enable IPsec Cryptomap delete trap  **Choices:**   - `false` - `true` |
| **detach**  boolean | Enable IPsec Cryptomap Detach trap  **Choices:**   - `false` - `true` |
| **too_many_sas**  boolean | Enable IPsec Tunnel Start trap  **Choices:**   - `false` - `true` |
| **tunnel**  dictionary | Enable IPsec Tunnel traps |
| **start**  boolean | Enable IPsec Tunnel start trap  **Choices:**   - `false` - `true` |
| **stop**  boolean | Enable IPsec Tunnel stop trap  **Choices:**   - `false` - `true` |
| **ipsla**  boolean | Enable SNMP ipsla traps  **Choices:**   - `false` - `true` |
| **isis**  boolean | Enable SNMP isis traps  **Choices:**   - `false` - `true` |
| **l2tun**  dictionary | Allow SNMP l2tun traps |
| **pseudowire_status**  boolean | Enable BFD pseudo wire status traps  **Choices:**   - `false` - `true` |
| **session**  boolean | Enable BFD session traps  **Choices:**   - `false` - `true` |
| **mpls_vpn**  boolean | Enable SNMP mpls traps  **Choices:**   - `false` - `true` |
| **msdp**  boolean | Enable SNMP msdp traps  **Choices:**   - `false` - `true` |
| **mvpn**  boolean | Enable SNMP mvpn traps  **Choices:**   - `false` - `true` |
| **ospf**  dictionary | Allow ospf related traps |
| **cisco_specific**  dictionary | Cisco specific traps |
| **error**  boolean | error traps  **Choices:**   - `false` - `true` |
| **lsa**  boolean | Lsa related traps  **Choices:**   - `false` - `true` |
| **retransmit**  boolean | Packet retransmit traps  **Choices:**   - `false` - `true` |
| **state_change**  dictionary | state change traps |
| **nssa_trans_change**  boolean | Nssa translator state changes  **Choices:**   - `false` - `true` |
| **shamlink**  dictionary | Config mismatch errors on virtual interfaces |
| **interface**  boolean | Sham link interface state changes  **Choices:**   - `false` - `true` |
| **neighbor**  boolean | Sham link neighbor state changes  **Choices:**   - `false` - `true` |
| **error**  boolean | Enable error traps  **Choices:**   - `false` - `true` |
| **lsa**  boolean | Enable/disable ospf lsa traps  **Choices:**   - `false` - `true` |
| **retransmit**  boolean | Enable/disable ospf retransmit traps  **Choices:**   - `false` - `true` |
| **state_change**  boolean | Enable/disable state change traps  **Choices:**   - `false` - `true` |
| **pim**  dictionary | Allow PIM traps |
| **enable**  boolean | Enable/disable PIM traps  **Choices:**   - `false` - `true` |
| **invalid_pim_message**  boolean | Enable invalid pim message trap  **Choices:**   - `false` - `true` |
| **neighbor_change**  boolean | Enable neighbor change trap  **Choices:**   - `false` - `true` |
| **rp_mapping_change**  boolean | Enable rp mapping change trap  **Choices:**   - `false` - `true` |
| **pki**  boolean | Enable SNMP pki traps  **Choices:**   - `false` - `true` |
| **pw_vc**  boolean | Enable SNMP pw vc traps  **Choices:**   - `false` - `true` |
| **rsvp**  boolean | Enable SNMP RSVP traps  **Choices:**   - `false` - `true` |
| **snmp**  dictionary | Enable SNMP traps |
| **authentication**  boolean | Enable authentication trap  **Choices:**   - `false` - `true` |
| **coldstart**  boolean | Enable coldStart trap  **Choices:**   - `false` - `true` |
| **linkdown**  boolean | Enable linkDown trap  **Choices:**   - `false` - `true` |
| **linkup**  boolean | Enable linkUp trap  **Choices:**   - `false` - `true` |
| **warmstart**  boolean | Enable warmStart trap  **Choices:**   - `false` - `true` |
| **syslog**  boolean | Enable SNMP syslog traps  **Choices:**   - `false` - `true` |
| **transceiver_all**  boolean | Enable SNMP transceiver traps  **Choices:**   - `false` - `true` |
| **tty**  boolean | Enable SNMP tty TCP connection traps  **Choices:**   - `false` - `true` |
| **vrfmib**  dictionary | Allow vrfmib traps |
| **vnet_trunk_down**  boolean | Enable vnet-trunk-down traps  **Choices:**   - `false` - `true` |
| **vnet_trunk_up**  boolean | Enable vnet-trunk-up trap  **Choices:**   - `false` - `true` |
| **vrf_down**  boolean | Enable vrf-down trap  **Choices:**   - `false` - `true` |
| **vrf_up**  boolean | Enable vrf-up trap  **Choices:**   - `false` - `true` |
| **vrrp**  boolean | Enable SNMP vrrp traps  **Choices:**   - `false` - `true` |
| **users**  list / elements=dictionary | Define a user who can access the SNMP engine |
| **acl_v4**  string | Access list ipv4 associated |
| **acl_v6**  string | Access list ipv6 associated |
| **authentication**  dictionary | Authentication parameters for the user.  Effects idempotency of module as configuration applied is not reflected in running-config. |
| **algorithm**  string | Select algorithm for authentication.  **Choices:**   - `"md5"` - `"sha"` |
| **password**  string | Authentication password for user. |
| **encryption**  dictionary | Encryption parameters for the user.  Effects idempotency of module as configuration applied is not reflected in running-config. |
| **password**  string | Authentication password for user. |
| **priv**  string | Select algorithm for encryption.  **Choices:**   - `"3des"` - `"aes"` - `"des"` |
| **priv_option**  string | Add extra option for specific priv if any. |
| **group**  string | SNMP group for the user. |
| **remote**  string | System where an SNMPv3 user is hosted |
| **udp_port**  integer | UDP port used by the remote SNMP system |
| **username**  string | SNMP user name |
| **version**  string | SNMP security version  **Choices:**   - `"v1"` - `"v2c"` - `"v3"` |
| **version_option**  string | Enable encrypted version option.  **Choices:**   - `"encrypted"` |
| **vrf**  string | The remote SNMP entity’s VPN Routing instance |
| **views**  list / elements=dictionary | Define an SNMPv2 MIB view |
| **excluded**  boolean | MIB family is excluded from the view  **Choices:**   - `false` - `true` |
| **family_name**  string | MIB view family name |
| **included**  boolean | MIB family is included in the view  **Choices:**   - `false` - `true` |
| **name**  string | Name of the view |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS device by executing the command **show running-config | include snmp-server**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  Refer to examples for more details.  The states *replaced* and *overridden* have identical behaviour for this module.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"parsed"` - `"gathered"` - `"rendered"` |

## [Notes](ios_snmp_server_module.md#id3)

> **Note:**
>
> - Tested against Cisco IOSXE Version 17.3 on CML.
> - This module works with connection `network_cli`.

## [Examples](ios_snmp_server_module.md#id4)

```yaml+jinja
# Using state: merged

# Before state:
# -------------

# router-ios#show running-config | section ^snmp-server
# --------------------- EMPTY -----------------

# Merged play:
# ------------

- name: Apply the provided configuration
  cisco.ios.ios_snmp_server:
    config:
      communities:
        - acl_v4: testACL
          name: mergedComm
          rw: true
      contact: contact updated using merged
      engine_id:
        - id: AB0C5342FF0F
          remote:
            host: 172.16.0.12
            udp_port: 25
      groups:
        - group: mergedGroup
          version: v3
          version_option: auth
      file_transfer:
        access_group: test
        protocol:
          - ftp
      hosts:
        - community_string: mergedComm
          host: 172.16.2.9
          informs: true
          traps:
            - msdp
            - stun
            - pki
          version: 2c
        - community_string: mergedComm
          host: 172.16.2.9
          traps:
            - slb
            - pki
      password_policy:
        - change: 3
          digits: 23
          lower_case: 12
          max_len: 24
          policy_name: MergedPolicy
          special_char: 32
          upper_case: 12
        - change: 43
          min_len: 12
          policy_name: MergedPolicy2
          special_char: 22
          upper_case: 12
        - change: 11
          digits: 23
          max_len: 12
          min_len: 12
          policy_name: policy3
          special_char: 22
          upper_case: 12
      traps:
        cef:
          enable: true
          inconsistency: true
          peer_fib_state_change: true
          peer_state_change: true
          resource_failure: true
        msdp: true
        ospf:
          cisco_specific:
            error: true
            lsa: true
            retransmit: true
            state_change:
              nssa_trans_change: true
              shamlink:
                interface: true
                neighbor: true
          error: true
          lsa: true
          retransmit: true
          state_change: true
        syslog: true
        tty: true
      users:
        - acl_v4: "24"
          group: dev
          username: userPaul
          version: v1
    state: merged

# Commands Fired:
# ---------------

# "commands": [
#         "snmp-server contact contact updated using merged",
#         "snmp-server file-transfer access-group test protocol ftp",
#         "snmp-server enable traps msdp",
#         "snmp-server enable traps syslog",
#         "snmp-server enable traps tty",
#         "snmp-server enable traps ospf cisco-specific errors",
#         "snmp-server enable traps ospf cisco-specific retransmit",
#         "snmp-server enable traps ospf cisco-specific lsa",
#         "snmp-server enable traps ospf cisco-specific state-change nssa-trans-change",
#         "snmp-server enable traps ospf cisco-specific state-change shamlink interface",
#         "snmp-server enable traps ospf cisco-specific state-change shamlink neighbor",
#         "snmp-server enable traps ospf errors",
#         "snmp-server enable traps ospf retransmit",
#         "snmp-server enable traps ospf lsa",
#         "snmp-server enable traps ospf state-change",
#         "snmp-server enable traps cef resource-failure peer-state-change peer-fib-state-change inconsistency",
#         "snmp-server host 172.16.2.9 informs version 2c mergedComm msdp stun pki",
#         "snmp-server host 172.16.2.9 mergedComm slb pki",
#         "snmp-server group mergedGroup v3 auth",
#         "snmp-server engineID remote 172.16.0.12 udp-port 25 AB0C5342FF0F",
#         "snmp-server community mergedComm rw testACL",
#         "snmp-server password-policy MergedPolicy define max-len 24 upper-case 12 lower-case 12 special-char 32 digits 23 change 3",
#         "snmp-server password-policy MergedPolicy2 define min-len 12 upper-case 12 special-char 22 change 43",
#         "snmp-server password-policy policy3 define min-len 12 max-len 12 upper-case 12 special-char 22 digits 23 change 11",
#         "snmp-server user userPaul dev v1 access 24"
# ],

# After state:
# ------------

# router-ios#show running-config | section ^snmp-server
# snmp-server engineID remote 172.16.0.12 udp-port 25 AB0C5342FF0F
# snmp-server user userPaul dev v1 access 24
# snmp-server group mergedGroup v3 auth
# snmp-server community mergedComm RW testACL
# snmp-server contact contact updated using merged
# snmp-server enable traps tty
# snmp-server enable traps ospf state-change
# snmp-server enable traps ospf errors
# snmp-server enable traps ospf retransmit
# snmp-server enable traps ospf lsa
# snmp-server enable traps ospf cisco-specific state-change nssa-trans-change
# snmp-server enable traps ospf cisco-specific state-change shamlink interface
# snmp-server enable traps ospf cisco-specific state-change shamlink neighbor
# snmp-server enable traps ospf cisco-specific errors
# snmp-server enable traps ospf cisco-specific retransmit
# snmp-server enable traps ospf cisco-specific lsa
# snmp-server enable traps cef resource-failure peer-state-change peer-fib-state-change inconsistency
# snmp-server enable traps msdp
# snmp-server enable traps syslog
# snmp-server host 172.16.2.9 informs version 2c mergedComm  msdp stun pki
# snmp-server host 172.16.2.9 mergedComm  slb pki
# snmp-server file-transfer access-group test protocol ftp
# snmp-server password-policy MergedPolicy define max-len 24 upper-case 12 lower-case 12 special-char 32 digits 23 change 3
# snmp-server password-policy MergedPolicy2 define min-len 12 upper-case 12 special-char 22 change 43
# snmp-server password-policy policy3 define min-len 12 max-len 12 upper-case 12 special-char 22 digits 23 change 11

# Using state: deleted

# Before state:
# -------------

# router-ios#show running-config | section ^snmp-server
# snmp-server engineID remote 172.16.0.12 udp-port 25 AB0C5342FF0F
# snmp-server user userPaul dev v1 access 24
# snmp-server group mergedGroup v3 auth
# snmp-server community mergedComm RW testACL
# snmp-server contact contact updated using merged
# snmp-server enable traps tty
# snmp-server enable traps ospf state-change
# snmp-server enable traps ospf errors
# snmp-server enable traps ospf retransmit
# snmp-server enable traps ospf lsa
# snmp-server enable traps ospf cisco-specific state-change nssa-trans-change
# snmp-server enable traps ospf cisco-specific state-change shamlink interface
# snmp-server enable traps ospf cisco-specific state-change shamlink neighbor
# snmp-server enable traps ospf cisco-specific errors
# snmp-server enable traps ospf cisco-specific retransmit
# snmp-server enable traps ospf cisco-specific lsa
# snmp-server enable traps cef resource-failure peer-state-change peer-fib-state-change inconsistency
# snmp-server enable traps msdp
# snmp-server enable traps syslog
# snmp-server host 172.16.2.9 informs version 2c mergedComm  msdp stun pki
# snmp-server host 172.16.2.9 mergedComm  slb pki
# snmp-server file-transfer access-group test protocol ftp
# snmp-server password-policy MergedPolicy define max-len 24 upper-case 12 lower-case 12 special-char 32 digits 23 change 3
# snmp-server password-policy MergedPolicy2 define min-len 12 upper-case 12 special-char 22 change 43
# snmp-server password-policy policy3 define min-len 12 max-len 12 upper-case 12 special-char 22 digits 23 change 11

# Deleted play:
# -------------

- name: Remove all existing configuration
  cisco.ios.ios_snmp_server:
    state: deleted

# Commands Fired:
# ---------------

# "commands": [
#     "no snmp-server contact contact updated using merged",
#     "no snmp-server file-transfer access-group test protocol ftp",
#     "no snmp-server enable traps msdp",
#     "no snmp-server enable traps syslog",
#     "no snmp-server enable traps tty",
#     "no snmp-server enable traps ospf cisco-specific errors",
#     "no snmp-server enable traps ospf cisco-specific retransmit",
#     "no snmp-server enable traps ospf cisco-specific lsa",
#     "no snmp-server enable traps ospf cisco-specific state-change nssa-trans-change",
#     "no snmp-server enable traps ospf cisco-specific state-change shamlink interface",
#     "no snmp-server enable traps ospf cisco-specific state-change shamlink neighbor",
#     "no snmp-server enable traps ospf errors",
#     "no snmp-server enable traps ospf retransmit",
#     "no snmp-server enable traps ospf lsa",
#     "no snmp-server enable traps ospf state-change",
#     "no snmp-server enable traps cef resource-failure peer-state-change peer-fib-state-change inconsistency",
#     "no snmp-server host 172.16.2.9 informs version 2c mergedComm msdp stun pki",
#     "no snmp-server host 172.16.2.9 mergedComm slb pki",
#     "no snmp-server group mergedGroup v3 auth",
#     "no snmp-server engineID remote 172.16.0.12 udp-port 25 AB0C5342FF0F",
#     "no snmp-server community mergedComm rw testACL",
#     "no snmp-server password-policy MergedPolicy define max-len 24 upper-case 12 lower-case 12 special-char 32 digits 23 change 3",
#     "no snmp-server password-policy MergedPolicy2 define min-len 12 upper-case 12 special-char 22 change 43",
#     "no snmp-server password-policy policy3 define min-len 12 max-len 12 upper-case 12 special-char 22 digits 23 change 11",
#     "no snmp-server user userPaul dev v1 access 24"
# ],

# After state:
# ------------

# router-ios#show running-config | section ^snmp-server
# --------------------- EMPTY -----------------

# Using state: overridden

# Before state:
# -------------

# router-ios#show running-config | section ^snmp-server
# snmp-server engineID remote 172.16.0.12 udp-port 25 AB0C5342FF0F
# snmp-server user userPaul dev v1 access 24
# snmp-server group mergedGroup v3 auth
# snmp-server community mergedComm RW testACL
# snmp-server contact contact updated using merged
# snmp-server enable traps tty
# snmp-server enable traps ospf state-change
# snmp-server enable traps ospf errors
# snmp-server enable traps ospf retransmit
# snmp-server enable traps ospf lsa
# snmp-server enable traps ospf cisco-specific state-change nssa-trans-change
# snmp-server enable traps ospf cisco-specific state-change shamlink interface
# snmp-server enable traps ospf cisco-specific state-change shamlink neighbor
# snmp-server enable traps ospf cisco-specific errors
# snmp-server enable traps ospf cisco-specific retransmit
# snmp-server enable traps ospf cisco-specific lsa
# snmp-server enable traps cef resource-failure peer-state-change peer-fib-state-change inconsistency
# snmp-server enable traps msdp
# snmp-server enable traps syslog
# snmp-server host 172.16.2.9 informs version 2c mergedComm  msdp stun pki
# snmp-server host 172.16.2.9 mergedComm  slb pki
# snmp-server file-transfer access-group test protocol ftp
# snmp-server password-policy MergedPolicy define max-len 24 upper-case 12 lower-case 12 special-char 32 digits 23 change 3
# snmp-server password-policy MergedPolicy2 define min-len 12 upper-case 12 special-char 22 change 43
# snmp-server password-policy policy3 define min-len 12 max-len 12 upper-case 12 special-char 22 digits 23 change 11

# Overridden play:
# ----------------

- name: Override commands with provided configuration
  cisco.ios.ios_snmp_server:
    config:
      location: "location entry for snmp"
      packet_size: 500
      communities:
        - acl_v4: acl_uq
          name: communityOverriden
          rw: true
    state: overridden

# Commands Fired:
# ---------------
# "commands": [
#       "no snmp-server contact contact updated using merged",
#       "no snmp-server file-transfer access-group test protocol ftp",
#       "snmp-server location location entry for snmp",
#       "snmp-server packetsize 500",
#       "no snmp-server enable traps msdp",
#       "no snmp-server enable traps syslog",
#       "no snmp-server enable traps tty",
#       "no snmp-server enable traps ospf cisco-specific errors",
#       "no snmp-server enable traps ospf cisco-specific retransmit",
#       "no snmp-server enable traps ospf cisco-specific lsa",
#       "no snmp-server enable traps ospf cisco-specific state-change nssa-trans-change",
#       "no snmp-server enable traps ospf cisco-specific state-change shamlink interface",
#       "no snmp-server enable traps ospf cisco-specific state-change shamlink neighbor",
#       "no snmp-server enable traps ospf errors",
#       "no snmp-server enable traps ospf retransmit",
#       "no snmp-server enable traps ospf lsa",
#       "no snmp-server enable traps ospf state-change",
#       "no snmp-server enable traps cef resource-failure peer-state-change peer-fib-state-change inconsistency",
#       "no snmp-server host 172.16.2.9 informs version 2c mergedComm msdp stun pki",
#       "no snmp-server host 172.16.2.9 mergedComm slb pki",
#       "no snmp-server group mergedGroup v3 auth",
#       "no snmp-server engineID remote 172.16.0.12 udp-port 25 AB0C5342FF0F",
#       "snmp-server community communityOvverriden rw acl_uq",
#       "no snmp-server community mergedComm rw testACL",
#       "no snmp-server password-policy MergedPolicy define max-len 24 upper-case 12 lower-case 12 special-char 32 digits 23 change 3",
#       "no snmp-server password-policy MergedPolicy2 define min-len 12 upper-case 12 special-char 22 change 43",
#       "no snmp-server password-policy policy3 define min-len 12 max-len 12 upper-case 12 special-char 22 digits 23 change 11",
#       "no snmp-server user userPaul dev v1 access 24"
#     ],

# After state:
# ------------

# router-ios#show running-config | section ^snmp-server
# snmp-server community communityOverriden RW acl_uq
# snmp-server packetsize 500
# snmp-server location location entry for snmp

# Using state: replaced

# Before state:
# -------------

# router-ios#show running-config | section ^snmp-server
# snmp-server community communityOverriden RW acl_uq
# snmp-server packetsize 500
# snmp-server location location entry for snmp

# Replaced play:
# --------------

- name: Replace commands with provided configuration
  cisco.ios.ios_snmp_server:
    config:
      location: "updated location entry"
      packet_size: 500
      communities:
        - acl_v4: acl_uq
          name: communityOverriden
          rw: true
    state: replaced

# Commands Fired:
# ---------------

# "commands": [
#     "snmp-server location updated location entry"
#     ],

# After state:
# ------------

# router-ios#show running-config | section ^snmp-server
# snmp-server community communityOverriden RW acl_uq
# snmp-server packetsize 500
# snmp-server location updated location entry

# Using state: gathered

# Before state:
# -------------

#router-ios#show running-config | section ^snmp-server
# snmp-server engineID remote 172.16.0.12 udp-port 25 AB0C5342FF0F
# snmp-server user userPaul dev v1 access 24
# snmp-server group mergedGroup v3 auth
# snmp-server community communityOvverriden RW acl_uq
# snmp-server community mergedComm RW testACL
# snmp-server packetsize 500
# snmp-server location updated location entry
# snmp-server contact contact updated using merged
# snmp-server enable traps tty
# snmp-server enable traps ospf state-change
# snmp-server enable traps ospf errors
# snmp-server enable traps ospf retransmit
# snmp-server enable traps ospf lsa
# snmp-server enable traps ospf cisco-specific state-change nssa-trans-change
# snmp-server enable traps ospf cisco-specific state-change shamlink interface
# snmp-server enable traps ospf cisco-specific state-change shamlink neighbor
# snmp-server enable traps ospf cisco-specific errors
# snmp-server enable traps ospf cisco-specific retransmit
# snmp-server enable traps ospf cisco-specific lsa
# snmp-server enable traps cef resource-failure peer-state-change peer-fib-state-change inconsistency
# snmp-server enable traps msdp
# snmp-server enable traps syslog
# snmp-server host 172.16.2.9 informs version 2c mergedComm  msdp stun pki
# snmp-server host 172.16.2.9 mergedComm  slb pki
# snmp-server file-transfer access-group test protocol ftp
# snmp-server password-policy MergedPolicy define max-len 24 upper-case 12 lower-case 12 special-char 32 digits 23 change 3
# snmp-server password-policy MergedPolicy2 define min-len 12 upper-case 12 special-char 22 change 43
# snmp-server password-policy policy3 define min-len 12 max-len 12 upper-case 12 special-char 22 digits 23 change 11

# Gathered play:
# --------------

- name: Gather listed snmp config
  cisco.ios.ios_snmp_server:
    state: gathered

# Module Execution Result:
# ------------------------

#   "gathered": {
#         "communities": [
#             {
#                 "acl_v4": "acl_uq",
#                 "name": "communityOvverriden",
#                 "rw": true
#             },
#             {
#                 "acl_v4": "testACL",
#                 "name": "mergedComm",
#                 "rw": true
#             }
#         ],
#         "contact": "contact updated using merged",
#         "engine_id": [
#             {
#                 "id": "AB0C5342FF0F",
#                 "remote": {
#                     "host": "172.16.0.12",
#                     "udp_port": 25
#                 }
#             }
#         ],
#         "file_transfer": {
#             "access_group": "test",
#             "protocol": [
#                 "ftp"
#             ]
#         },
#         "groups": [
#             {
#                 "group": "mergedGroup",
#                 "version": "v3",
#                 "version_option": "auth"
#             }
#         ],
#         "hosts": [
#             {
#                 "community_string": "mergedComm",
#                 "host": "172.16.2.9",
#                 "informs": true,
#                 "traps": [
#                     "msdp",
#                     "stun",
#                     "pki"
#                 ],
#                 "version": "2c"
#             },
#             {
#                 "community_string": "mergedComm",
#                 "host": "172.16.2.9",
#                 "traps": [
#                     "slb",
#                     "pki"
#                 ]
#             }
#         ],
#         "location": "updated location entry",
#         "packet_size": 500,
#         "password_policy": [
#             {
#                 "change": 3,
#                 "digits": 23,
#                 "lower_case": 12,
#                 "max_len": 24,
#                 "policy_name": "MergedPolicy",
#                 "special_char": 32,
#                 "upper_case": 12
#             },
#             {
#                 "change": 43,
#                 "min_len": 12,
#                 "policy_name": "MergedPolicy2",
#                 "special_char": 22,
#                 "upper_case": 12
#             },
#             {
#                 "change": 11,
#                 "digits": 23,
#                 "max_len": 12,
#                 "min_len": 12,
#                 "policy_name": "policy3",
#                 "special_char": 22,
#                 "upper_case": 12
#             }
#         ],
#         "traps": {
#             "cef": {
#                 "enable": true,
#                 "inconsistency": true,
#                 "peer_fib_state_change": true,
#                 "peer_state_change": true,
#                 "resource_failure": true
#             },
#             "msdp": true,
#             "ospf": {
#                 "cisco_specific": {
#                     "error": true,
#                     "lsa": true,
#                     "retransmit": true,
#                     "state_change": {
#                         "nssa_trans_change": true,
#                         "shamlink": {
#                             "interface": true,
#                             "neighbor": true
#                         }
#                     }
#                 },
#                 "error": true,
#                 "lsa": true,
#                 "retransmit": true,
#                 "state_change": true
#             },
#             "syslog": true,
#             "tty": true
#         },
#         "users": [
#             {
#                 "acl_v4": "24",
#                 "group": "dev",
#                 "username": "userPaul",
#                 "version": "v1"
#             }
#         ]
#     },

# Using state: rendered

# Rendered play:
# --------------

- name: Render the commands for provided configuration
  cisco.ios.ios_snmp_server:
    config:
      accounting:
        command: default
      cache: 2
      chassis_id: entry for chassis id
      communities:
        - acl_v6: te
          name: test
          ro: true
          view: terst1
        - acl_v4: "1322"
          name: wete
          ro: true
        - acl_v4: paul
          name: weteww
          rw: true
      contact: details contact
      context:
        - contextA
        - contextB
      engine_id:
        - id: AB0C5342FA0A
          local: true
        - id: AB0C5342FAAB
          remote:
            host: 172.16.0.2
            udp_port: 23
        - id: AB0C5342FAAA
          remote:
            host: 172.16.0.1
            udp_port: 22
      file_transfer:
        access_group: testAcl
        protocol:
          - ftp
          - rcp
      groups:
        - group: grpFamily
          version: v3
          version_option: auth
        - context: mycontext
          group: grpFamily
          version: v1
        - acl_v4: "2"
          group: grp1
          notify: me
          version: v1
        - group: newtera
          version: v3
          version_option: priv
        - group: relaplacing
          version: v3
          version_option: noauth
      hosts:
        - community_string: check
          host: 172.16.2.99
          informs: true
          traps:
            - msdp
            - stun
          version: 2c
        - community_string: check
          host: 172.16.2.99
          traps:
            - slb
            - pki
        - community_string: checktrap
          host: 172.16.2.99
          traps:
            - isis
            - hsrp
        - community_string: newtera
          host: 172.16.2.1
          traps:
            - rsrb
            - pim
            - rsvp
            - slb
            - pki
          version: "3"
          version_option: priv
        - community_string: relaplacing
          host: 172.16.2.1
          traps:
            - slb
            - pki
          version: "3"
          version_option: noauth
        - community_string: trapsac
          host: 172.16.2.1
          traps:
            - tty
            - bgp
          version: 2c
        - community_string: www
          host: 172.16.1.1
          traps:
            - tty
            - bgp
          version: "3"
          version_option: auth
      inform:
        pending: 2
      ip:
        dscp: 2
      location: "entry for snmp location"
      packet_size: 500
      password_policy:
        - change: 3
          digits: 23
          lower_case: 12
          max_len: 24
          policy_name: policy1
          special_char: 32
          upper_case: 12
        - change: 9
          min_len: 12
          policy_name: policy2
          special_char: 22
          upper_case: 12
        - change: 11
          digits: 23
          max_len: 12
          min_len: 12
          policy_name: policy3
          special_char: 22
          upper_case: 12
      queue_length: 2
      source_interface: Loopback999
      system_shutdown: true
      trap_source: GigabitEthernet0/0
      trap_timeout: 2
      traps:
        auth_framework:
          enable: true
        bgp:
          cbgp2: true
          enable: true
        bfd:
          enable: true
          session_down: true
          session_up: true
        bridge:
          enable: true
          newroot: true
          topologychange: true
        casa: true
        cef:
          enable: true
          inconsistency: true
          peer_fib_state_change: true
          peer_state_change: true
          resource_failure: true
        dlsw:
          enable: true
        eigrp: true
        ethernet:
          cfm:
            alarm: true
          evc:
            status: true
        event_manager: true
        flowmon: true
        frame_relay:
          enable: true
          subif:
            enable: true
        hsrp: true
        ike:
          policy:
            add: true
            delete: true
          tunnel:
            start: true
            stop: true
        ipmulticast: true
        ipsec:
          cryptomap:
            add: true
            attach: true
            delete: true
            detach: true
          too_many_sas: true
          tunnel:
            start: true
            stop: true
        ipsla: true
        l2tun:
          pseudowire_status: true
          session: true
        msdp: true
        ospf:
          cisco_specific:
            error: true
            lsa: true
            retransmit: true
            state_change:
              nssa_trans_change: true
              shamlink:
                interface: true
                neighbor: true
          error: true
          lsa: true
          retransmit: true
          state_change: true
        pim:
          enable: true
          invalid_pim_message: true
          neighbor_change: true
          rp_mapping_change: true
        pki: true
        rsvp: true
        snmp:
          authentication: true
          coldstart: true
          linkdown: true
          linkup: true
          warmstart: true
        syslog: true
        tty: true
      users:
        - acl_v4: "24"
          group: groupFamily
          username: paul
          version: v1
        - acl_v4: ipv6
          group: groupFamily
          username: domnic
          version: v3
        - group: relaplacing
          username: relaplacing
          version: v3
    state: rendered

# Module Execution Result:
# ------------------------

# "rendered": [
#     "snmp-server accounting commands default",
#     "snmp-server cache interval 2",
#     "snmp-server chassis-id entry for chassis id",
#     "snmp-server contact details contact",
#     "snmp-server file-transfer access-group testAcl protocol ftp rcp",
#     "snmp-server inform pending 2",
#     "snmp-server ip dscp 2",
#     "snmp-server location entry for snmp location",
#     "snmp-server packetsize 500",
#     "snmp-server queue-length 2",
#     "snmp-server trap timeout 2",
#     "snmp-server source-interface informs Loopback999",
#     "snmp-server trap-source GigabitEthernet0/0",
#     "snmp-server system-shutdown",
#     "snmp-server enable traps auth-framework",
#     "snmp-server enable traps bfd session-down session-up",
#     "snmp-server enable traps bgp cbgp2",
#     "snmp-server enable traps bridge newroot topologychange",
#     "snmp-server enable traps casa",
#     "snmp-server enable traps eigrp",
#     "snmp-server enable traps event-manager",
#     "snmp-server enable traps flowmon",
#     "snmp-server enable traps hsrp",
#     "snmp-server enable traps ipsla",
#     "snmp-server enable traps msdp",
#     "snmp-server enable traps pki",
#     "snmp-server enable traps rsvp",
#     "snmp-server enable traps syslog",
#     "snmp-server enable traps tty",
#     "snmp-server enable traps ipmulticast",
#     "snmp-server enable traps ike policy add",
#     "snmp-server enable traps ike policy delete",
#     "snmp-server enable traps ike tunnel start",
#     "snmp-server enable traps ike tunnel stop",
#     "snmp-server enable traps ipsec cryptomap add",
#     "snmp-server enable traps ipsec cryptomap delete",
#     "snmp-server enable traps ipsec cryptomap attach",
#     "snmp-server enable traps ipsec cryptomap detach",
#     "snmp-server enable traps ipsec tunnel start",
#     "snmp-server enable traps ipsec tunnel stop",
#     "snmp-server enable traps ipsec too-many-sas",
#     "snmp-server enable traps ospf cisco-specific errors",
#     "snmp-server enable traps ospf cisco-specific retransmit",
#     "snmp-server enable traps ospf cisco-specific lsa",
#     "snmp-server enable traps ospf cisco-specific state-change nssa-trans-change",
#     "snmp-server enable traps ospf cisco-specific state-change shamlink interface",
#     "snmp-server enable traps ospf cisco-specific state-change shamlink neighbor",
#     "snmp-server enable traps ospf errors",
#     "snmp-server enable traps ospf retransmit",
#     "snmp-server enable traps ospf lsa",
#     "snmp-server enable traps ospf state-change",
#     "snmp-server enable traps l2tun pseudowire status",
#     "snmp-server enable traps l2tun session",
#     "snmp-server enable traps pim neighbor-change rp-mapping-change invalid-pim-message",
#     "snmp-server enable traps snmp authentication linkdown linkup warmstart coldstart",
#     "snmp-server enable traps frame-relay",
#     "snmp-server enable traps cef resource-failure peer-state-change peer-fib-state-change inconsistency",
#     "snmp-server enable traps dlsw",
#     "snmp-server enable traps ethernet evc status",
#     "snmp-server enable traps ethernet cfm alarm",
#     "snmp-server host 172.16.2.99 informs version 2c check msdp stun",
#     "snmp-server host 172.16.2.99 check slb pki",
#     "snmp-server host 172.16.2.99 checktrap isis hsrp",
#     "snmp-server host 172.16.2.1 version 3 priv newtera rsrb pim rsvp slb pki",
#     "snmp-server host 172.16.2.1 version 3 noauth relaplacing slb pki",
#     "snmp-server host 172.16.2.1 version 2c trapsac tty bgp",
#     "snmp-server host 172.16.1.1 version 3 auth www tty bgp",
#     "snmp-server group grpFamily v1 context mycontext",
#     "snmp-server group grp1 v1 notify me access 2",
#     "snmp-server group newtera v3 priv",
#     "snmp-server group relaplacing v3 noauth",
#     "snmp-server engineID local AB0C5342FA0A",
#     "snmp-server engineID remote 172.16.0.2 udp-port 23 AB0C5342FAAB",
#     "snmp-server engineID remote 172.16.0.1 udp-port 22 AB0C5342FAAA",
#     "snmp-server community test view terst1 ro ipv6 te",
#     "snmp-server community wete ro 1322",
#     "snmp-server community weteww rw paul",
#     "snmp-server context contextA",
#     "snmp-server context contextB",
#     "snmp-server password-policy policy1 define max-len 24 upper-case 12 lower-case 12 special-char 32 digits 23 change 3",
#     "snmp-server password-policy policy2 define min-len 12 upper-case 12 special-char 22 change 9",
#     "snmp-server password-policy policy3 define min-len 12 max-len 12 upper-case 12 special-char 22 digits 23 change 11",
#     "snmp-server user paul groupFamily v1 access 24",
#     "snmp-server user domnic groupFamily v3 access ipv6",
#     "snmp-server user relaplacing relaplacing v3"
# ]

# Using state: parsed

# File: parsed.cfg
# ----------------

# snmp-server engineID local AB0C5342FA0A
# snmp-server engineID remote 172.16.0.2 udp-port 23 AB0C5342FAAB
# snmp-server engineID remote 172.16.0.1 udp-port 22 AB0C5342FAAA
# snmp-server user newuser newfamily v1 access 24
# snmp-server user paul familypaul v3 access ipv6 ipv6acl
# snmp-server user replaceUser replaceUser v3
# snmp-server group group0 v3 auth
# snmp-server group group1 v1 notify me access 2
# snmp-server group group2 v3 priv
# snmp-server group replaceUser v3 noauth
# snmp-server community commu1 view view1 RO ipv6 te
# snmp-server community commu2 RO 1322
# snmp-server community commu3 RW paul
# snmp-server trap timeout 2
# snmp-server trap-source GigabitEthernet0/0
# snmp-server source-interface informs Loopback999
# snmp-server packetsize 500
# snmp-server enable traps vrfmib vrf-up vrf-down vnet-trunk-up vnet-trunk-down
# snmp-server host 172.16.2.99 informs version 2c check  msdp stun
# snmp-server host 172.16.2.1 version 2c trapsac  tty bgp
# snmp-server host 172.16.1.1 version 3 auth group0  tty bgp
# snmp-server context contextWord1
# snmp-server context contextWord2
# snmp-server file-transfer access-group testAcl protocol ftp
# snmp-server file-transfer access-group testAcl protocol rcp
# snmp-server cache interval 2
# snmp-server password-policy policy2 define min-len 12 upper-case 12 special-char 22 change 9
# snmp-server password-policy policy3 define min-len 12 max-len 12 upper-case 12 special-char 22 digits 23 change 11
# snmp-server accounting commands default
# snmp-server inform pending 2

# Parsed play:
# ------------

- name: Parse the provided configuration with the existing running configuration
  cisco.ios.ios_snmp_server:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Module Execution Result:
# ------------------------
#
#  "parsed": {
#     "accounting": {
#         "command": "default"
#     },
#     "cache": 2,
#     "communities": [
#         {
#             "acl_v6": "te",
#             "name": "commu1",
#             "ro": true,
#             "view": "view1"
#         },
#         {
#             "acl_v4": "1322",
#             "name": "commu2",
#             "ro": true
#         },
#         {
#             "acl_v4": "paul",
#             "name": "commu3",
#             "rw": true
#         }
#     ],
#     "context": [
#         "contextWord1",
#         "contextWord2"
#     ],
#     "engine_id": [
#         {
#             "id": "AB0C5342FA0A",
#             "local": true
#         },
#         {
#             "id": "AB0C5342FAAA",
#             "remote": {
#                 "host": "172.16.0.1",
#                 "udp_port": 22
#             }
#         },
#         {
#             "id": "AB0C5342FAAB",
#             "remote": {
#                 "host": "172.16.0.2",
#                 "udp_port": 23
#             }
#         }
#     ],
#     "file_transfer": {
#         "access_group": "testAcl",
#         "protocol": [
#             "rcp",
#             "ftp"
#         ]
#     },
#     "groups": [
#         {
#             "group": "group0",
#             "version": "v3",
#             "version_option": "auth"
#         },
#         {
#             "acl_v4": "2",
#             "group": "group1",
#             "notify": "me",
#             "version": "v1"
#         },
#         {
#             "group": "group2",
#             "version": "v3",
#             "version_option": "priv"
#         },
#         {
#             "group": "replaceUser",
#             "version": "v3",
#             "version_option": "noauth"
#         }
#     ],
#     "hosts": [
#         {
#             "community_string": "group0",
#             "host": "172.16.1.1",
#             "traps": [
#                 "tty",
#                 "bgp"
#             ],
#             "version": "3",
#             "version_option": "auth"
#         },
#         {
#             "community_string": "trapsac",
#             "host": "172.16.2.1",
#             "traps": [
#                 "tty",
#                 "bgp"
#             ],
#             "version": "2c"
#         },
#         {
#             "community_string": "check",
#             "host": "172.16.2.99",
#             "informs": true,
#             "traps": [
#                 "msdp",
#                 "stun"
#             ],
#             "version": "2c"
#         }
#     ],
#     "inform": {
#         "pending": 2
#     },
#     "packet_size": 500,
#     "password_policy": [
#         {
#             "change": 9,
#             "min_len": 12,
#             "policy_name": "policy2",
#             "special_char": 22,
#             "upper_case": 12
#         },
#         {
#             "change": 11,
#             "digits": 23,
#             "max_len": 12,
#             "min_len": 12,
#             "policy_name": "policy3",
#             "special_char": 22,
#             "upper_case": 12
#         }
#     ],
#     "source_interface": "Loopback999",
#     "trap_source": "GigabitEthernet0/0",
#     "trap_timeout": 2,
#     "traps": {
#         "vrfmib": {
#             "vnet_trunk_down": true,
#             "vnet_trunk_up": true,
#             "vrf_down": true,
#             "vrf_up": true
#         }
#     },
#     "users": [
#         {
#             "acl_v4": "24",
#             "group": "newfamily",
#             "username": "newuser",
#             "version": "v1"
#         },
#         {
#             "acl_v4": "ipv6",
#             "group": "familypaul",
#             "username": "paul",
#             "version": "v3"
#         },
#         {
#             "group": "replaceUser",
#             "username": "replaceUser",
#             "version": "v3"
#         }
#     ]
# }
```

## [Return Values](ios_snmp_server_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  **Returned:** when changed  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `["snmp-server host 172.16.2.99 informs version 2c check msdp stun", "snmp-server engineID remote 172.16.0.2 udp-port 23 AB0C5342FAAB", "snmp-server group grp1 v1 notify me access 2"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when *state* is `gathered`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  **Returned:** when *state* is `parsed`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  **Returned:** when *state* is `rendered`  **Sample:** `["snmp-server enable traps ipsec cryptomap attach", "snmp-server password-policy policy1 define max-len 24 upper-case 12 lower-case 12 special-char 32 digits 23 change 3", "snmp-server cache interval 2"]` |

### Authors

- Sagar Paul (@KB-perByte)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
