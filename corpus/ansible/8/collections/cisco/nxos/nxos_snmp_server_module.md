---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_snmp_server module – SNMP Server resource module."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_snmp_server_module.html
fetched_at: 2026-07-28T01:39:11+00:00
---
# cisco.nxos.nxos_snmp_server module – SNMP Server resource module.

> **Note:**
>
> This module is part of the [cisco.nxos collection](https://galaxy.ansible.com/ui/repo/published/cisco/nxos/) (version 4.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nxos`.
>
> To use it in a playbook, specify: `cisco.nxos.nxos_snmp_server`.

New in cisco.nxos 2.8.0

- [Synopsis](nxos_snmp_server_module.md#synopsis)
- [Parameters](nxos_snmp_server_module.md#parameters)
- [Notes](nxos_snmp_server_module.md#notes)
- [Examples](nxos_snmp_server_module.md#examples)
- [Return Values](nxos_snmp_server_module.md#return-values)

## [Synopsis](nxos_snmp_server_module.md#id1)

- This module manages SNMP server configuration on devices running Cisco NX-OS.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: snmp_server

## [Parameters](nxos_snmp_server_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dict of SNMP server configuration |
| **aaa_user**  dictionary | Set duration for which aaa-cached snmp user exists. |
| **cache_timeout**  integer | Timeout for which aaa-cached user exists(in secs). |
| **communities**  list / elements=dictionary | Set community string and access privs. |
| **group**  string | Group to which the community belongs. |
| **name**  aliases: community  string | SNMP community string (Max Size 32). |
| **ro**  boolean | Read-only access with this community string.  **Choices:**   - `false` - `true` |
| **rw**  boolean | Read-write access with this community string.  **Choices:**   - `false` - `true` |
| **use_ipv4acl**  string | Specify IPv4 ACL, the ACL name specified must be IPv4 ACL.  This option is unsupported on MDS switches. |
| **use_ipv6acl**  string | Specify IPv6 ACL, the ACL name specified after must be IPv6 ACL.  This option is unsupported on MDS switches. |
| **contact**  string | Modify sysContact. |
| **context**  dictionary | SNMP context to be mapped. |
| **instance**  string | Name of the protocol instance (Max Size 32). |
| **name**  string | Name of the SNMP context (Max Size 32). |
| **topology**  string | Topology associated with the SNMP context. |
| **vrf**  string | VRF associated with the SNMP context.  This option is unsupported on MDS switches. |
| **counter**  dictionary | Configure port counter configuration.  This option is unsupported on MDS switches. |
| **cache**  dictionary | Port stats cache. |
| **enable**  boolean | Enable port stats cache.  **Choices:**   - `false` - `true` |
| **timeout**  integer | Timeout for which cached port stats exists(in secs). |
| **drop**  dictionary | Silently drop unknown v3 user packets.  This option is unsupported on MDS switches. |
| **unknown_engine_id**  boolean | Unknown v3 engine id.  **Choices:**   - `false` - `true` |
| **unknown_user**  boolean | Unknown v3 user.  **Choices:**   - `false` - `true` |
| **engine_id**  dictionary | Configure a local SNMPv3 engineID.  This option is unsupported on MDS switches. |
| **local**  string | EngineID of the local agent. |
| **global_enforce_priv**  boolean | Globally enforce privacy for all the users.  **Choices:**   - `false` - `true` |
| **hosts**  list / elements=dictionary | Specify hosts to receive SNMP notifications.  SNMP hosts config lines that appear separately in running-config must be added as individual dictionaries. |
| **auth**  string | Use the SNMPv3 authNoPriv Security Level. |
| **community**  string | SNMP community string or SNMPv3 user name (Max Size 32). |
| **filter_vrf**  string | Filters notifications to the notification host receiver based on the configured VRF.  This option is unsupported on MDS switches. |
| **host**  string | IPv4 or IPv6 address or DNS Name of SNMP notification host. |
| **informs**  boolean | Send Inform messages to this host.  **Choices:**   - `false` - `true` |
| **priv**  string | Use the SNMPv3 authPriv Security Level. |
| **source_interface**  string | Source interface to be used for sending out SNMP notifications to this host. |
| **traps**  boolean | Send Traps messages to this host.  **Choices:**   - `false` - `true` |
| **udp_port**  integer | The notification host’s UDP port number. |
| **use_vrf**  string | Configures SNMP to use the selected VRF to communicate with the host receiver.  This option is unsupported on MDS switches. |
| **version**  string | SNMP version to use for notification messages.  **Choices:**   - `"1"` - `"2c"` - `"3"` |
| **location**  string | Modify sysLocation. |
| **mib**  dictionary | Mib access parameters. |
| **community_map**  dictionary | SNMP community. |
| **community**  string | SNMP community string (Max Size 32). |
| **context**  string | Name of the SNMP context (Max Size 32). |
| **packetsize**  integer | Largest SNMP packet size |
| **protocol**  dictionary | Snmp protocol operations. |
| **enable**  boolean | Enable/Disable snmp protocol operations.  **Choices:**   - `false` - `true` |
| **source_interface**  dictionary | Source interface to be used for sending out SNMP notifications.  This option is unsupported on MDS switches. |
| **informs**  string | SNMP Inform notifications for which this source interface needs to be used. |
| **traps**  string | SNMP Trap notifications for which this source interface needs to be used. |
| **system_shutdown**  boolean | Configure snmp-server for reload(2).  **Choices:**   - `false` - `true` |
| **tcp_session**  dictionary | Enable one time authentication for snmp over tcp session. |
| **auth**  boolean | Enable one time authentication for snmp over tcp session.  **Choices:**   - `false` - `true` |
| **enable**  boolean | Enable tcp-session.  This option is unsupported on MDS switches.  **Choices:**   - `false` - `true` |
| **traps**  dictionary | Enable SNMP Traps |
| **aaa**  dictionary | AAA traps |
| **enable**  boolean | Enable AAA traps.  **Choices:**   - `false` - `true` |
| **server_state_change**  boolean | AAA server state change notification.  **Choices:**   - `false` - `true` |
| **bgp**  dictionary | SNMP BGP traps. |
| **enable**  boolean | Enable SNMP BGP traps.  **Choices:**   - `false` - `true` |
| **bridge**  dictionary | Bridge traps.  This option is unsupported on MDS switches. |
| **enable**  boolean | Enable bridge traps.  **Choices:**   - `false` - `true` |
| **newroot**  boolean | Enable SNMP STP Bridge MIB newroot traps.  **Choices:**   - `false` - `true` |
| **topologychange**  boolean | Enable SNMP STP Bridge MIB topologychange traps.  **Choices:**   - `false` - `true` |
| **callhome**  dictionary | Callhome traps. |
| **enable**  boolean | Enable callhome traps.  This option is unsupported on MDS switches.  **Choices:**   - `false` - `true` |
| **event_notify**  boolean | Callhome External Event Notification.  **Choices:**   - `false` - `true` |
| **smtp_send_fail**  boolean | SMTP Message Send Fail notification.  **Choices:**   - `false` - `true` |
| **cfs**  dictionary | CFS traps. |
| **enable**  boolean | Enable cfs traps.  This option is unsupported on MDS switches.  **Choices:**   - `false` - `true` |
| **merge_failure**  boolean | Merge failure notification.  **Choices:**   - `false` - `true` |
| **state_change_notif**  boolean | State change notification.  **Choices:**   - `false` - `true` |
| **config**  dictionary | Config traps. |
| **ccmCLIRunningConfigChanged**  boolean | Running config change trap.  **Choices:**   - `false` - `true` |
| **enable**  boolean | Enable config traps.  This option is unsupported on MDS switches.  **Choices:**   - `false` - `true` |
| **entity**  dictionary | Entity traps. |
| **cefcMIBEnableStatusNotification**  boolean | CefcMIBEnableStatusNotification.  **Choices:**   - `false` - `true` |
| **enable**  boolean | Enable entity traps.  **Choices:**   - `false` - `true` |
| **entity_fan_status_change**  boolean | Entity Fan Status Change.  **Choices:**   - `false` - `true` |
| **entity_mib_change**  boolean | Entity MIB change.  **Choices:**   - `false` - `true` |
| **entity_module_inserted**  boolean | Entity Module Inserted.  **Choices:**   - `false` - `true` |
| **entity_module_removed**  boolean | Entity Module Removed.  **Choices:**   - `false` - `true` |
| **entity_module_status_change**  boolean | Entity Module Status Change.  **Choices:**   - `false` - `true` |
| **entity_power_out_change**  boolean | Entity Power Out Change.  **Choices:**   - `false` - `true` |
| **entity_power_status_change**  boolean | Entity Power Status Change.  **Choices:**   - `false` - `true` |
| **entity_sensor**  boolean | Entity sensor.  **Choices:**   - `false` - `true` |
| **entity_unrecognised_module**  boolean | Entity Unrecognised Module.  **Choices:**   - `false` - `true` |
| **feature_control**  dictionary | Feature-Control traps. |
| **ciscoFeatOpStatusChange**  boolean | Feature operation status change Notification.  **Choices:**   - `false` - `true` |
| **enable**  boolean | Enable feature-control traps.  This option is unsupported on MDS switches.  **Choices:**   - `false` - `true` |
| **featureOpStatusChange**  boolean | Feature operation status change notification.  **Choices:**   - `false` - `true` |
| **generic**  dictionary | Generic traps. |
| **coldStart**  boolean | Generic coldStart trap.  **Choices:**   - `false` - `true` |
| **enable**  boolean | Enable generic traps.  This option is unsupported on MDS switches.  **Choices:**   - `false` - `true` |
| **warmStart**  boolean | Generic warmStart trap.  **Choices:**   - `false` - `true` |
| **license**  dictionary | License traps. |
| **enable**  boolean | Enable license traps.  This option is unsupported on MDS switches.  **Choices:**   - `false` - `true` |
| **notify_license_expiry**  boolean | License Expiry Notification.  **Choices:**   - `false` - `true` |
| **notify_license_expiry_warning**  boolean | License Expiry Warning Notification.  **Choices:**   - `false` - `true` |
| **notify_licensefile_missing**  boolean | License File Missing Notification.  **Choices:**   - `false` - `true` |
| **notify_no_license_for_feature**  boolean | No License installed for feature Notification.  **Choices:**   - `false` - `true` |
| **link**  dictionary | Link traps. |
| **cErrDisableInterfaceEventRev1**  boolean | Err-disable state notification.  This option is unsupported on MDS switches.  **Choices:**   - `false` - `true` |
| **cieLinkDown**  boolean | Cisco extended link state down notification.  **Choices:**   - `false` - `true` |
| **cieLinkUp**  boolean | Cisco extended link state up notification.  **Choices:**   - `false` - `true` |
| **cisco_xcvr_mon_status_chg**  boolean | Cisco interface transceiver monitor status change notification.  **Choices:**   - `false` - `true` |
| **cmn_mac_move_notification**  boolean | Mac addr move trap.  This option is unsupported on MDS switches.  **Choices:**   - `false` - `true` |
| **delayed_link_state_change**  boolean | Delayed link state change.  **Choices:**   - `false` - `true` |
| **enable**  boolean | Enable link traps.  This option is unsupported on MDS switches.  **Choices:**   - `false` - `true` |
| **extended_linkDown**  boolean | IETF extended link state down notification.  **Choices:**   - `false` - `true` |
| **extended_linkUp**  boolean | IETF extended link state up notification.  **Choices:**   - `false` - `true` |
| **linkDown**  boolean | IETF Link state down notification.  **Choices:**   - `false` - `true` |
| **linkUp**  boolean | IETF Link state up notification.  **Choices:**   - `false` - `true` |
| **mmode**  dictionary | MMode traps.  This option is unsupported on MDS switches. |
| **cseMaintModeChangeNotify**  boolean | Maint Mode Change Notification.  **Choices:**   - `false` - `true` |
| **cseNormalModeChangeNotify**  boolean | Normal Mode Change Notification.  **Choices:**   - `false` - `true` |
| **enable**  boolean | Enable mmode traps.  **Choices:**   - `false` - `true` |
| **ospf**  dictionary | SNMP OSPF traps. |
| **enable**  boolean | Enable SNMP OSPF traps.  **Choices:**   - `false` - `true` |
| **ospfv3**  dictionary | SNMP OSPFv3 traps. |
| **enable**  boolean | Enable SNMP OSPFv3 traps.  **Choices:**   - `false` - `true` |
| **rf**  dictionary | RF traps. |
| **enable**  boolean | Enable rf traps.  This option is unsupported on MDS switches.  **Choices:**   - `false` - `true` |
| **redundancy_framework**  boolean | Redundancy_Framework (RF) Sup switchover MIB.  **Choices:**   - `false` - `true` |
| **rmon**  dictionary | RMON traps. |
| **enable**  boolean | Enable rmon traps.  This option is unsupported on MDS switches.  **Choices:**   - `false` - `true` |
| **fallingAlarm**  boolean | Rmon falling alarm.  **Choices:**   - `false` - `true` |
| **hcFallingAlarm**  boolean | High capacity Rmon falling alarm.  **Choices:**   - `false` - `true` |
| **hcRisingAlarm**  boolean | High capacity Rmon rising alarm.  **Choices:**   - `false` - `true` |
| **risingAlarm**  boolean | Rmon rising alarm.  **Choices:**   - `false` - `true` |
| **snmp**  dictionary | SNMP traps. |
| **authentication**  boolean | SNMP authentication trap.  **Choices:**   - `false` - `true` |
| **enable**  boolean | Enable snmp traps.  This option is unsupported on MDS switches.  **Choices:**   - `false` - `true` |
| **storm_control**  dictionary | Storm-Control traps. |
| **cpscEventRev1**  boolean | Port-Storm-Control-Event.  This option is unsupported on MDS switches.  **Choices:**   - `false` - `true` |
| **enable**  boolean | Enable storm-control traps.  This option is unsupported on MDS switches.  **Choices:**   - `false` - `true` |
| **trap_rate**  boolean | Number of traps per minute.  **Choices:**   - `false` - `true` |
| **stpx**  dictionary | Stpx traps.  This option is unsupported on MDS switches. |
| **enable**  boolean | Enable stpx traps.  **Choices:**   - `false` - `true` |
| **inconsistency**  boolean | Enable SNMP STPX MIB InconsistencyUpdate traps.  **Choices:**   - `false` - `true` |
| **loop_inconsistency**  boolean | Enable SNMP STPX MIB LoopInconsistencyUpdate traps.  **Choices:**   - `false` - `true` |
| **root_inconsistency**  boolean | Enable SNMP STPX MIB RootInconsistencyUpdate traps.  **Choices:**   - `false` - `true` |
| **syslog**  dictionary | Enable syslog traps. |
| **enable**  boolean | Enable syslog traps.  This option is unsupported on MDS switches.  **Choices:**   - `false` - `true` |
| **message_generated**  boolean | Message Generated Notification.  **Choices:**   - `false` - `true` |
| **sysmgr**  dictionary | Sysmgr traps. |
| **cseFailSwCoreNotifyExtended**  boolean | Software Core Notification.  **Choices:**   - `false` - `true` |
| **enable**  boolean | Enable sysmgr traps.  This option is unsupported on MDS switches.  **Choices:**   - `false` - `true` |
| **system**  dictionary | System traps. |
| **clock_change_notification**  boolean | Clock-change-notification traps.  **Choices:**   - `false` - `true` |
| **enable**  boolean | Enable system traps.  This option is unsupported on MDS switches.  **Choices:**   - `false` - `true` |
| **upgrade**  dictionary | Upgrade traps. |
| **enable**  boolean | Enable upgrade traps.  This option is unsupported on MDS switches.  **Choices:**   - `false` - `true` |
| **upgradeJobStatusNotify**  boolean | Upgrade Job Status Notification.  **Choices:**   - `false` - `true` |
| **upgradeOpNotifyOnCompletion**  boolean | Upgrade Global Status Notification.  **Choices:**   - `false` - `true` |
| **vtp**  dictionary | VTP traps.  This option is unsupported on MDS switches. |
| **enable**  boolean | Enable VTP traps.  **Choices:**   - `false` - `true` |
| **notifs**  boolean | Enable vtpConfigRevNumberError vtpConfigDigestEnable vtpConfigRevNumberError vtpConfigDigestError vtpServerDisabled vtpVersionOneDeviceDetected vlanTrunkPortDynamicStatusChange vtpLocalModeChanged vtpVersionInUseChanged notification.  **Choices:**   - `false` - `true` |
| **vlancreate**  boolean | Enable vtpVlanCreated notification.  **Choices:**   - `false` - `true` |
| **vlandelete**  boolean | Enable vtpVlanDeleted notification.  **Choices:**   - `false` - `true` |
| **users**  dictionary | Define users who can access the SNMP engine. |
| **auth**  list / elements=dictionary | SNMP User authentication related settings |
| **authentication**  dictionary | Authentication parameters for the user. |
| **algorithm**  string | Select algorithm for authentication.  **Choices:**   - `"md5"` - `"sha"` - `"sha-256"` |
| **engine_id**  string | EngineID for configuring notif target user (for V3 informs).  This value needs to be enclosed in quotes in the task. |
| **localized_key**  boolean | Specifies whether the passwords are in localized key format.  **Choices:**   - `false` - `true` |
| **localizedv2_key**  boolean | Specifies whether the passwords are in localized V2 key format.  **Choices:**   - `false` - `true` |
| **password**  string | Authentication password for user (Max Size 127).  If this value is localized, it has to be enclosed in quotes in the task. |
| **priv**  dictionary | Encryption parameters for the user. |
| **aes_128**  boolean | Use 128-bit AES algorithm for privacy.  **Choices:**   - `false` - `true` |
| **privacy_password**  string | Privacy password for user (Max Size 130).  If this value is localized, it has to be enclosed in quotes in the task. |
| **group**  string | Group name (ignored for notif target user) (Max Size 28). |
| **user**  string | Name of the user (Max Size 28). |
| **use_acls**  list / elements=dictionary | Set IPv4 and IPv6 ACL to use. |
| **ipv4**  string | Specify IPv4 ACL, the ACL name specified after must be IPv4 ACL. |
| **ipv6**  string | Specify IPv6 ACL, the ACL name specified after must be IPv6 ACL. |
| **user**  string | Name of the user (Max Size 28). |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the NX-OS device by executing the command **show running-config | section ‘^snmp-server’**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  The states `replaced` and `overridden` have identical behaviour for this module.  Please refer to examples for more details.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"parsed"` - `"gathered"` - `"rendered"` |

## [Notes](nxos_snmp_server_module.md#id3)

> **Note:**
>
> - Tested against NX-OS 9.3.6 on Cisco Nexus Switches.
> - This module works with connection `network_cli` and `httpapi`.
> - Tested against Cisco MDS NX-OS 9.2(2) with connection `network_cli`.

## [Examples](nxos_snmp_server_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
# nxos-9k-rdo# show running-config | section "^snmp-server"
# snmp-server user admin network-admin auth md5 0xcbde46b02c46e0bcd3ac5af6a8b13da9 priv 0xcbde46b02c46e0bcd3ac5af6a8b13da9 localizedkey

- name: Merge the provided configuration with the existing running configuration
  cisco.nxos.nxos_snmp_server:
    config:
      aaa_user:
        cache_timeout: 36000
      communities:
        - community: public
          group: network-operator
        - community: private
          group: network-admin
      contact: nxosswitchadmin@localhost
      location: serverroom-1
      traps:
        aaa:
          server_state_change: True
        system:
          clock_change_notification: True
      hosts:
        - host: 192.0.2.1
          traps: True
          version: '1'
          community: public
        - host: 192.0.2.1
          source_interface: Ethernet1/1
        - host: 192.0.2.2
          informs: True
          version: '3'
          auth: NMS
      users:
        auth:
          - user: snmp_user_1
            group: network-operator
            authentication:
              algorithm: md5
              password: '0x5632724fb8ac3699296af26281e1d0f1'
              localized_key: True
          - user: snmp_user_2
            group: network-operator
            authentication:
              algorithm: md5
              password: '0x5632724fb8ac3699296af26281e1d0f1'
              localized_key: True
              priv:
                privacy_password: '0x5632724fb8ac3699296af26281e1d0f1'
                aes_128: True
        use_acls:
          - user: snmp_user_1
            ipv4: acl1
            ipv6: acl2
          - user: snmp_user_2
            ipv4: acl3
            ipv6: acl4

# Task output
# -------------
# before:
#   users:
#     auth:
#       - user: admin
#         group: network-admin
#         authentication:
#           algorithm: md5
#           password: "0xcbde46b02c46e0bcd3ac5af6a8b13da9"
#           localized_key: True
#           priv:
#             privacy_password: "0xcbde46b02c46e0bcd3ac5af6a8b13da9"
#
# commands:
#   - snmp-server contact nxosswitchadmin@localhost
#   - snmp-server location serverroom-1
#   - snmp-server aaa-user cache-timeout 36000
#   - snmp-server user snmp_user_1 network-operator auth md5 0x5632724fb8ac3699296af26281e1d0f1 localizedkey
#   - snmp-server user snmp_user_2 network-operator auth md5 0x5632724fb8ac3699296af26281e1d0f1 priv aes-128 0x5632724fb8ac3699296af26281e1d0f1 localizedkey
#   - snmp-server user snmp_user_1 use-ipv4acl acl1 use-ipv6acl acl2
#   - snmp-server user snmp_user_2 use-ipv4acl acl3 use-ipv6acl acl4
#   - snmp-server host 192.0.2.1 traps version 1 public
#   - snmp-server host 192.0.2.1 source-interface Ethernet1/1
#   - snmp-server host 192.0.2.2 informs version 3 auth NMS
#   - snmp-server community private group network-admin
#   - snmp-server community public group network-operator
#   - snmp-server enable traps aaa server-state-change
#   - snmp-server enable traps system Clock-change-notification
#
# after:
#   aaa_user:
#      cache_timeout: 36000
#    communities:
#      - community: private
#        group: network-admin
#      - community: public
#        group: network-operator
#    contact: nxosswitchadmin@localhost
#    location: serverroom-1
#    traps:
#      aaa:
#        server_state_change: True
#      system:
#        clock_change_notification: True
#    hosts:
#      - host: 192.0.2.1
#        traps: true
#        version: "1"
#        community: public
#
#      - host: 192.0.2.1
#        source_interface: Ethernet1/1
#
#      - host: 192.0.2.2
#        informs: true
#        version: "3"
#        auth: NMS
#    users:
#      auth:
#        - user: admin
#          group: network-admin
#          authentication:
#            algorithm: md5
#            password: "0xcbde46b02c46e0bcd3ac5af6a8b13da9"
#            localized_key: True
#            priv:
#              privacy_password: "0xcbde46b02c46e0bcd3ac5af6a8b13da9"
#
#        - user: snmp_user_1
#          group: network-operator
#          authentication:
#            algorithm: md5
#            password: "0x5632724fb8ac3699296af26281e1d0f1"
#            localized_key: True
#
#        - authentication:
#            algorithm: md5
#            localized_key: true
#            password: "0x5632724fb8ac3699296af26281e1d0f1"
#            priv:
#              aes_128: true
#              privacy_password: "0x5632724fb8ac3699296af26281e1d0f1"
#          group: network-operator
#          user: snmp_user_2
#
#      use_acls:
#        - user: snmp_user_1
#          ipv4: acl1
#          ipv6: acl2
#        - user: snmp_user_2
#          ipv4: acl3
#          ipv6: acl4

# After state:
# ------------
# nxos-9k-rdo# show running-config | section "^snmp-server"
# snmp-server contact nxosswitchadmin@localhost
# snmp-server location serverroom-1
# snmp-server aaa-user cache-timeout 36000
# snmp-server user admin network-admin auth md5 0xcbde46b02c46e0bcd3ac5af6a8b13da9 priv 0xcbde46b02c46e0bcd3ac5af6a8b13da9 localizedkey
# snmp-server user snmp_user_1 network-operator auth md5 0x5632724fb8ac3699296af26281e1d0f1 localizedkey
# snmp-server user snmp_user_2 network-operator auth md5 0x5632724fb8ac3699296af26281e1d0f1 priv aes-128 0x5632724fb8ac3699296af26281e1d0f1 localizedkey
# snmp-server user snmp_user_1 use-ipv4acl acl1 use-ipv6acl acl2
# snmp-server user snmp_user_2 use-ipv4acl acl3 use-ipv6acl acl4
# snmp-server host 192.0.2.1 traps version 1 public
# snmp-server host 192.0.2.1 source-interface Ethernet1/1
# snmp-server host 192.0.2.2 informs version 3 auth NMS
# snmp-server community private group network-admin
# snmp-server community public group network-operator
# snmp-server enable traps aaa server-state-change
# snmp-server enable traps system Clock-change-notification

# Using replaced

# Before state:
# ------------
# nxos-9k-rdo# show running-config | section "^snmp-server"
# snmp-server contact nxosswitchadmin@localhost
# snmp-server location serverroom-1
# snmp-server aaa-user cache-timeout 36000
# snmp-server user admin network-admin auth md5 0xcbde46b02c46e0bcd3ac5af6a8b13da9 priv 0xcbde46b02c46e0bcd3ac5af6a8b13da9 localizedkey
# snmp-server user snmp_user_1 network-operator auth md5 0x5632724fb8ac3699296af26281e1d0f1 localizedkey
# snmp-server user snmp_user_2 network-operator auth md5 0x5632724fb8ac3699296af26281e1d0f1 priv aes-128 0x5632724fb8ac3699296af26281e1d0f1 localizedkey
# snmp-server user snmp_user_1 use-ipv4acl acl1 use-ipv6acl acl2
# snmp-server user snmp_user_2 use-ipv4acl acl3 use-ipv6acl acl4
# snmp-server host 192.0.2.1 traps version 1 public
# snmp-server host 192.0.2.1 source-interface Ethernet1/1
# snmp-server host 192.0.2.2 informs version 3 auth NMS
# snmp-server community private group network-admin
# snmp-server community public group network-operator
# snmp-server enable traps aaa server-state-change
# snmp-server enable traps system Clock-change-notification

- name: Replace snmp-server configurations of listed snmp-server with provided configurations
  cisco.nxos.nxos_snmp_server:
    config:
      aaa_user:
        cache_timeout: 36000
      communities:
        - community: public
          group: network-operator
        - community: secret
          group: network-operator
      contact: nxosswitchadmin2@localhost
      location: serverroom-2
      traps:
        aaa:
          server_state_change: True
      hosts:
        - host: 192.0.2.1
          traps: True
          version: '1'
          community: public
        - host: 192.0.2.1
          source_interface: Ethernet1/1
        - host: 192.0.3.2
          informs: True
          version: '3'
          auth: NMS
      users:
        auth:
          - user: admin
            group: network-admin
            authentication:
              algorithm: md5
              password: "0xcbde46b02c46e0bcd3ac5af6a8b13da9"
              localized_key: True
              priv:
                privacy_password: "0xcbde46b02c46e0bcd3ac5af6a8b13da9"

          - user: snmp_user_1
            group: network-operator
            authentication:
              algorithm: md5
              password: '0x5632724fb8ac3699296af26281e1d0f1'
              localized_key: True

          - user: snmp_user_2
            group: network-operator
            authentication:
              algorithm: md5
              password: '0x5632724fb8ac3699296af26281e1d0f1'
              localized_key: True
              priv:
                privacy_password: '0x5632724fb8ac3699296af26281e1d0f1'
                aes_128: True
        use_acls:
          - user: snmp_user_1
            ipv4: acl1
            ipv6: acl2
    state: replaced

# Task output
# -------------
# before:
#   aaa_user:
#      cache_timeout: 36000
#    communities:
#      - community: private
#        group: network-admin
#      - community: public
#        group: network-operator
#    contact: nxosswitchadmin@localhost
#    location: serverroom-1
#    traps:
#      aaa:
#        server_state_change: True
#      system:
#        clock_change_notification: True
#    hosts:
#      - host: 192.0.2.1
#        traps: true
#        version: "1"
#        community: public
#
#      - host: 192.0.2.1
#        source_interface: Ethernet1/1
#
#      - host: 192.0.2.2
#        informs: true
#        version: "3"
#        auth: NMS
#    users:
#      auth:
#        - user: admin
#          group: network-admin
#          authentication:
#            algorithm: md5
#            password: "0xcbde46b02c46e0bcd3ac5af6a8b13da9"
#            localized_key: True
#            priv:
#              privacy_password: "0xcbde46b02c46e0bcd3ac5af6a8b13da9"
#
#        - user: snmp_user_1
#          group: network-operator
#          authentication:
#            algorithm: md5
#            password: "0x5632724fb8ac3699296af26281e1d0f1"
#            localized_key: True
#
#        - authentication:
#            algorithm: md5
#            localized_key: true
#            password: "0x5632724fb8ac3699296af26281e1d0f1"
#            priv:
#              aes_128: true
#              privacy_password: "0x5632724fb8ac3699296af26281e1d0f1"
#          group: network-operator
#          user: snmp_user_2
#
#      use_acls:
#        - user: snmp_user_1
#          ipv4: acl1
#          ipv6: acl2
#        - user: snmp_user_2
#          ipv4: acl3
#          ipv6: acl4
#
# commands:
#   - snmp-server contact nxosswitchadmin2@localhost
#   - no snmp-server enable traps system Clock-change-notification
#   - snmp-server location serverroom-2
#   - no snmp-server user snmp_user_2 use-ipv4acl acl3 use-ipv6acl acl4
#   - no snmp-server host 192.0.2.2 informs version 3 auth NMS
#   - snmp-server host 192.0.3.2 informs version 3 auth NMS
#   - no snmp-server community private group network-admin
#   - snmp-server community secret group network-operator
#
# after:
#   aaa_user:
#      cache_timeout: 36000
#    communities:
#      - community: public
#        group: network-operator
#      - community: secret
#        group: network-operator
#    contact: nxosswitchadmin2@localhost
#    location: serverroom-2
#    traps:
#      aaa:
#        server_state_change: True
#    hosts:
#      - host: 192.0.2.1
#        traps: True
#        version: '1'
#        community: public
#      - host: 192.0.2.1
#        source_interface: Ethernet1/1
#      - host: 192.0.3.2
#        informs: True
#        version: '3'
#        auth: NMS
#    users:
#      auth:
#        - user: admin
#          group: network-admin
#          authentication:
#            algorithm: md5
#            password: "0xcbde46b02c46e0bcd3ac5af6a8b13da9"
#            localized_key: True
#            priv:
#              privacy_password: "0xcbde46b02c46e0bcd3ac5af6a8b13da9"
#
#        - user: snmp_user_1
#          group: network-operator
#          authentication:
#            algorithm: md5
#            password: '0x5632724fb8ac3699296af26281e1d0f1'
#            localized_key: True
#
#        - user: snmp_user_2
#          group: network-operator
#          authentication:
#            algorithm: md5
#            password: '0x5632724fb8ac3699296af26281e1d0f1'
#            localized_key: True
#            priv:
#              privacy_password: '0x5632724fb8ac3699296af26281e1d0f1'
#              aes_128: True
#
#      use_acls:
#        - user: snmp_user_1
#          ipv4: acl1
#          ipv6: acl2
#

# After state:
# ------------
# nxos-9k-rdo# show running-config | section "^snmp-server"
# snmp-server contact nxosswitchadmin2@localhost
# snmp-server location serverroom-2
# snmp-server aaa-user cache-timeout 36000
# snmp-server user admin network-admin auth md5 0xcbde46b02c46e0bcd3ac5af6a8b13da9 priv 0xcbde46b02c46e0bcd3ac5af6a8b13da9 localizedkey
# snmp-server user snmp_user_1 network-operator auth md5 0x5632724fb8ac3699296af26281e1d0f1 localizedkey
# snmp-server user snmp_user_2 network-operator auth md5 0x5632724fb8ac3699296af26281e1d0f1 priv aes-128 0x5632724fb8ac3699296af26281e1d0f1 localizedkey
# snmp-server user snmp_user_1 use-ipv4acl acl1 use-ipv6acl acl2
# snmp-server user snmp_user_2 use-ipv4acl acl3 use-ipv6acl acl4
# snmp-server host 192.0.2.1 traps version 1 public
# snmp-server host 192.0.2.1 source-interface Ethernet1/1
# snmp-server host 192.0.2.2 informs version 3 auth NMS
# snmp-server community secret group network-operator
# snmp-server community public group network-operator
# snmp-server enable traps aaa server-state-change
# snmp-server enable traps system Clock-change-notification

# Using deleted

# Before state:
# ------------
# nxos-9k-rdo# show running-config | section "^snmp-server"
# snmp-server contact nxosswitchadmin@localhost
# snmp-server location serverroom-1
# snmp-server aaa-user cache-timeout 36000
# snmp-server user admin network-admin auth md5 0xcbde46b02c46e0bcd3ac5af6a8b13da9 priv 0xcbde46b02c46e0bcd3ac5af6a8b13da9 localizedkey
# snmp-server user snmp_user_1 network-operator auth md5 0x5632724fb8ac3699296af26281e1d0f1 localizedkey
# snmp-server user snmp_user_2 network-operator auth md5 0x5632724fb8ac3699296af26281e1d0f1 priv aes-128 0x5632724fb8ac3699296af26281e1d0f1 localizedkey
# snmp-server user snmp_user_1 use-ipv4acl acl1 use-ipv6acl acl2
# snmp-server user snmp_user_2 use-ipv4acl acl3 use-ipv6acl acl4
# snmp-server host 192.0.2.1 traps version 1 public
# snmp-server host 192.0.2.1 source-interface Ethernet1/1
# snmp-server host 192.0.2.2 informs version 3 auth NMS
# snmp-server community private group network-admin
# snmp-server community public group network-operator
# snmp-server enable traps aaa server-state-change
# snmp-server enable traps system Clock-change-notification

- name: Delete SNMP Server configurations from the device (admin user will not be deleted)
  cisco.nxos.nxos_snmp_server:
    state: deleted

# Task output
# -------------
# before:
#   aaa_user:
#      cache_timeout: 36000
#    communities:
#      - community: private
#        group: network-admin
#      - community: public
#        group: network-operator
#    contact: nxosswitchadmin@localhost
#    location: serverroom-1
#    traps:
#      aaa:
#        server_state_change: True
#      system:
#        clock_change_notification: True
#    hosts:
#      - host: 192.0.2.1
#        traps: true
#        version: "1"
#        community: public
#
#      - host: 192.0.2.1
#        source_interface: Ethernet1/1
#
#      - host: 192.0.2.2
#        informs: true
#        version: "3"
#        auth: NMS
#    users:
#      auth:
#        - user: admin
#          group: network-admin
#          authentication:
#            algorithm: md5
#            password: "0xcbde46b02c46e0bcd3ac5af6a8b13da9"
#            localized_key: True
#            priv:
#              privacy_password: "0xcbde46b02c46e0bcd3ac5af6a8b13da9"
#
#        - user: snmp_user_1
#          group: network-operator
#          authentication:
#            algorithm: md5
#            password: "0x5632724fb8ac3699296af26281e1d0f1"
#            localized_key: True
#
#        - authentication:
#            algorithm: md5
#            localized_key: true
#            password: "0x5632724fb8ac3699296af26281e1d0f1"
#            priv:
#              aes_128: true
#              privacy_password: "0x5632724fb8ac3699296af26281e1d0f1"
#          group: network-operator
#          user: snmp_user_2
#
#      use_acls:
#        - user: snmp_user_1
#          ipv4: acl1
#          ipv6: acl2
#        - user: snmp_user_2
#          ipv4: acl3
#          ipv6: acl4
#
# commands:
#   - no snmp-server contact nxosswitchadmin@localhost
#   - no snmp-server location serverroom-1
#   - no snmp-server aaa-user cache-timeout 36000
#   - no snmp-server user admin network-admin auth md5 0xcbde46b02c46e0bcd3ac5af6a8b13da9 priv 0xcbde46b02c46e0bcd3ac5af6a8b13da9 localizedkey
#   - no snmp-server user snmp_user_1 network-operator auth md5 0x5632724fb8ac3699296af26281e1d0f1 localizedkey
#   - no snmp-server user snmp_user_2 network-operator auth md5 0x5632724fb8ac3699296af26281e1d0f1 priv aes-128 0x5632724fb8ac3699296af26281e1d0f1 localizedkey
#   - no snmp-server user snmp_user_1 use-ipv4acl acl1 use-ipv6acl acl2
#   - no snmp-server user snmp_user_2 use-ipv4acl acl3 use-ipv6acl acl4
#   - no snmp-server host 192.0.2.1 traps version 1 public
#   - no snmp-server host 192.0.2.1 source-interface Ethernet1/1
#   - no snmp-server host 192.0.2.2 informs version 3 auth NMS
#   - no snmp-server community private group network-admin
#   - no snmp-server community public group network-operator
#   - no snmp-server enable traps aaa server-state-change
#   - no snmp-server enable traps system Clock-change-notification
#
# after:
#   users:
#     auth:
#       - user: admin
#         group: network-admin
#         authentication:
#           algorithm: md5
#           password: "0xcbde46b02c46e0bcd3ac5af6a8b13da9"
#           localized_key: True
#           priv:
#             privacy_password: "0xcbde46b02c46e0bcd3ac5af6a8b13da9"

# After state:
# ------------
# nxos-9k-rdo# show running-config | section "^snmp-server"
# snmp-server user admin network-admin auth md5 0xcbde46b02c46e0bcd3ac5af6a8b13da9 priv 0xcbde46b02c46e0bcd3ac5af6a8b13da9 localizedkey

# Using rendered
# ---------------

- name: Render platform specific configuration lines with state rendered (without connecting to the device)
  cisco.nxos.nxos_snmp_server:
    config:
      aaa_user:
        cache_timeout: 36000
      communities:
        - community: public
          group: network-operator
        - community: private
          group: network-admin
      contact: nxosswitchadmin@localhost
      location: serverroom-1
      traps:
        aaa:
          server_state_change: True
        system:
          clock_change_notification: True
      hosts:
        - host: 192.0.2.1
          traps: True
          version: '1'
          community: public
        - host: 192.0.2.1
          source_interface: Ethernet1/1
        - host: 192.0.2.2
          informs: True
          version: '3'
          auth: NMS
      users:
        auth:
          - user: snmp_user_1
            group: network-operator
            authentication:
              algorithm: md5
              password: '0x5632724fb8ac3699296af26281e1d0f1'
              localized_key: True
          - user: snmp_user_2
            group: network-operator
            authentication:
              algorithm: md5
              password: '0x5632724fb8ac3699296af26281e1d0f1'
              localized_key: True
              priv:
                privacy_password: '0x5632724fb8ac3699296af26281e1d0f1'
                aes_128: True
        use_acls:
          - user: snmp_user_1
            ipv4: acl1
            ipv6: acl2
          - user: snmp_user_2
            ipv4: acl3
            ipv6: acl4
    state: rendered

# Task Output (redacted)
# -----------------------
#  rendered:
#    - snmp-server contact nxosswitchadmin@localhost
#    - snmp-server location serverroom-1
#    - snmp-server aaa-user cache-timeout 36000
#    - snmp-server user snmp_user_1 network-operator auth md5 0x5632724fb8ac3699296af26281e1d0f1 localizedkey
#    - snmp-server user snmp_user_2 network-operator auth md5 0x5632724fb8ac3699296af26281e1d0f1 priv aes-128 0x5632724fb8ac3699296af26281e1d0f1 localizedkey
#    - snmp-server user snmp_user_1 use-ipv4acl acl1 use-ipv6acl acl2
#    - snmp-server user snmp_user_2 use-ipv4acl acl3 use-ipv6acl acl4
#    - snmp-server host 192.0.2.1 traps version 1 public
#    - snmp-server host 192.0.2.1 source-interface Ethernet1/1
#    - snmp-server host 192.0.2.2 informs version 3 auth NMS
#    - snmp-server community private group network-admin
#    - snmp-server community public group network-operator
#    - snmp-server enable traps aaa server-state-change
#    - snmp-server enable traps system Clock-change-notification

# Using parsed

# parsed.cfg
# ------------
# snmp-server contact nxosswitchadmin@localhost
# snmp-server location serverroom-1
# snmp-server aaa-user cache-timeout 36000
# snmp-server user snmp_user_1 network-operator auth md5 0x5632724fb8ac3699296af26281e1d0f1 localizedkey
# snmp-server user snmp_user_2 network-operator auth md5 0x5632724fb8ac3699296af26281e1d0f1 priv aes-128 0x5632724fb8ac3699296af26281e1d0f1 localizedkey
# snmp-server user snmp_user_1 use-ipv4acl acl1 use-ipv6acl acl2
# snmp-server user snmp_user_2 use-ipv4acl acl3 use-ipv6acl acl4
# snmp-server host 192.0.2.1 traps version 1 public
# snmp-server host 192.0.2.1 source-interface Ethernet1/1
# snmp-server host 192.0.2.2 informs version 3 auth NMS
# snmp-server community private group network-admin
# snmp-server community public group network-operator
# snmp-server enable traps aaa server-state-change
# snmp-server enable traps system Clock-change-notification

- name: Parse externally provided snmp-server configuration
  cisco.nxos.nxos_snmp_server:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed

# Task output (redacted)
# -----------------------
#  parsed:
#   aaa_user:
#      cache_timeout: 36000
#    communities:
#      - community: private
#        group: network-admin
#      - community: public
#        group: network-operator
#    contact: nxosswitchadmin@localhost
#    location: serverroom-1
#    traps:
#      aaa:
#        server_state_change: True
#      system:
#        clock_change_notification: True
#    hosts:
#      - host: 192.0.2.1
#        traps: true
#        version: "1"
#        community: public
#
#      - host: 192.0.2.1
#        source_interface: Ethernet1/1
#
#      - host: 192.0.2.2
#        informs: true
#        version: "3"
#        auth: NMS
#    users:
#      auth:
#        - user: snmp_user_1
#          group: network-operator
#          authentication:
#            algorithm: md5
#            password: "0x5632724fb8ac3699296af26281e1d0f1"
#            localized_key: True
#
#        - authentication:
#            algorithm: md5
#            localized_key: true
#            password: "0x5632724fb8ac3699296af26281e1d0f1"
#            priv:
#              aes_128: true
#              privacy_password: "0x5632724fb8ac3699296af26281e1d0f1"
#          group: network-operator
#          user: snmp_user_2
#
#      use_acls:
#        - user: snmp_user_1
#          ipv4: acl1
#          ipv6: acl2
#        - user: snmp_user_2
#          ipv4: acl3
#          ipv6: acl4
#
```

## [Return Values](nxos_snmp_server_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  **Returned:** when changed  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `["sample command 1", "sample command 2", "sample command 3"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when *state* is `gathered`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  **Returned:** when *state* is `parsed`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  **Returned:** when *state* is `rendered`  **Sample:** `["sample command 1", "sample command 2", "sample command 3"]` |

### Authors

- Nilashish Chakraborty (@NilashishC)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
