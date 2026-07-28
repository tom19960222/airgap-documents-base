---
collection: ansible
version: "8"
title: "community.general.nmcli module – Manage Networking"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/nmcli_module.html
fetched_at: 2026-07-28T01:48:09+00:00
---
# community.general.nmcli module – Manage Networking

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](nmcli_module.md#ansible-collections-community-general-nmcli-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.nmcli`.

- [Synopsis](nmcli_module.md#synopsis)
- [Requirements](nmcli_module.md#requirements)
- [Parameters](nmcli_module.md#parameters)
- [Attributes](nmcli_module.md#attributes)
- [Examples](nmcli_module.md#examples)

## [Synopsis](nmcli_module.md#id1)

- Manage the network devices. Create, modify and manage various connection and device type e.g., ethernet, teams, bonds, vlans etc.
- On CentOS 8 and Fedora >=29 like systems, the requirements can be met by installing the following packages: NetworkManager.
- On CentOS 7 and Fedora <=28 like systems, the requirements can be met by installing the following packages: NetworkManager-tui.
- On Ubuntu and Debian like systems, the requirements can be met by installing the following packages: network-manager
- On openSUSE, the requirements can be met by installing the following packages: NetworkManager.

Aliases: net_tools.nmcli

## [Requirements](nmcli_module.md#id2)

The below requirements are needed on the host that executes this module.

- nmcli

## [Parameters](nmcli_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **addr_gen_mode6**  string  *added in community.general 4.2.0* | Configure method for creating the address for use with IPv6 Stateless Address Autoconfiguration.  `default` and `default-or-eui64` have been added in community.general 6.5.0.  **Choices:**   - `"default"` - `"default-or-eui64"` - `"eui64"` - `"stable-privacy"` |
| **ageingtime**  integer | This is only used with bridge - [ageing-time <0-1000000>] the Ethernet MAC address aging time, in seconds.  **Default:** `300` |
| **arp_interval**  integer | This is only used with bond - ARP interval. |
| **arp_ip_target**  string | This is only used with bond - ARP IP target. |
| **autoconnect**  boolean | Whether the connection should start on boot.  Whether the connection profile can be automatically activated  **Choices:**   - `false` - `true` ← (default) |
| **conn_name**  string / required | The name used to call the connection. Pattern is <type>[-<ifname>][-<num>]. |
| **dhcp_client_id**  string | DHCP Client Identifier sent to the DHCP server. |
| **dns4**  list / elements=string | A list of up to 3 DNS servers.  The entries must be IPv4 addresses, for example `192.0.2.53`. |
| **dns4_ignore_auto**  boolean  *added in community.general 3.2.0* | Ignore automatically configured IPv4 name servers.  **Choices:**   - `false` ← (default) - `true` |
| **dns4_options**  list / elements=string  *added in community.general 7.2.0* | A list of DNS options. |
| **dns4_search**  list / elements=string | A list of DNS search domains. |
| **dns6**  list / elements=string | A list of up to 3 DNS servers.  The entries must be IPv6 addresses, for example `2001:4860:4860::8888`. |
| **dns6_ignore_auto**  boolean  *added in community.general 3.2.0* | Ignore automatically configured IPv6 name servers.  **Choices:**   - `false` ← (default) - `true` |
| **dns6_options**  list / elements=string  *added in community.general 7.2.0* | A list of DNS options. |
| **dns6_search**  list / elements=string | A list of DNS search domains. |
| **downdelay**  integer | This is only used with bond - downdelay. |
| **egress**  string | This is only used with VLAN - VLAN egress priority mapping. |
| **flags**  string | This is only used with VLAN - flags. |
| **forwarddelay**  integer | This is only used with bridge - [forward-delay <2-30>] STP forwarding delay, in seconds.  **Default:** `15` |
| **gsm**  dictionary  *added in community.general 3.7.0* | The configuration of the GSM connection.  Note the list of suboption attributes may vary depending on which version of NetworkManager/nmcli is installed on the host.  An up-to-date list of supported attributes can be found here: <https://networkmanager.dev/docs/api/latest/settings-gsm.html>.  For instance to use apn, pin, username and password: `{apn: provider.apn, pin: 1234, username: apn.username, password: apn.password}`. |
| **apn**  string | The GPRS Access Point Name specifying the APN used when establishing a data session with the GSM-based network.  The APN often determines how the user will be billed for their network usage and whether the user has access to the Internet or just a provider-specific walled-garden, so it is important to use the correct APN for the user’s mobile broadband plan.  The APN may only be composed of the characters a-z, 0-9, ., and - per GSM 03.60 Section 14.9. |
| **auto-config**  boolean | When `true`, the settings such as `gsm.apn`, `gsm.username`, or `gsm.password` will default to values that match the network the modem will register to in the Mobile Broadband Provider database.  **Choices:**   - `false` ← (default) - `true` |
| **device-id**  string | The device unique identifier (as given by the `WWAN` management service) which this connection applies to.  If given, the connection will only apply to the specified device. |
| **home-only**  boolean | When `true`, only connections to the home network will be allowed.  Connections to roaming networks will not be made.  **Choices:**   - `false` ← (default) - `true` |
| **mtu**  integer | If non-zero, only transmit packets of the specified size or smaller, breaking larger packets up into multiple Ethernet frames.  **Default:** `0` |
| **network-id**  string | The Network ID (GSM LAI format, ie MCC-MNC) to force specific network registration.  If the Network ID is specified, NetworkManager will attempt to force the device to register only on the specified network.  This can be used to ensure that the device does not roam when direct roaming control of the device is not otherwise possible. |
| **number**  string | Legacy setting that used to help establishing PPP data sessions for GSM-based modems. |
| **password**  string | The password used to authenticate with the network, if required.  Many providers do not require a password, or accept any password.  But if a password is required, it is specified here. |
| **password-flags**  integer | NMSettingSecretFlags indicating how to handle the `gsm.password` property.  Following choices are allowed: `0` **NONE**: The system is responsible for providing and storing this secret (default), `1` **AGENT_OWNED**: A user secret agent is responsible for providing and storing this secret; when it is required agents will be asked to retrieve it `2` **NOT_SAVED**: This secret should not be saved, but should be requested from the user each time it is needed `4` **NOT_REQUIRED**: In situations where it cannot be automatically determined that the secret is required (some VPNs and PPP providers do not require all secrets) this flag indicates that the specific secret is not required.  **Choices:**   - `0` ← (default) - `1` - `2` - `4` |
| **pin**  string | If the SIM is locked with a PIN it must be unlocked before any other operations are requested.  Specify the PIN here to allow operation of the device. |
| **pin-flags**  integer | NMSettingSecretFlags indicating how to handle the `gsm.pin` property.  See `gsm.password-flags` for NMSettingSecretFlags choices.  **Choices:**   - `0` ← (default) - `1` - `2` - `4` |
| **sim-id**  string | The SIM card unique identifier (as given by the `WWAN` management service) which this connection applies to.  If given, the connection will apply to any device also allowed by `gsm.device-id` which contains a SIM card matching the given identifier. |
| **sim-operator-id**  string | A MCC/MNC string like `310260` or `21601I` identifying the specific mobile network operator which this connection applies to.  If given, the connection will apply to any device also allowed by `gsm.device-id` and `gsm.sim-id` which contains a SIM card provisioned by the given operator. |
| **username**  string | The username used to authenticate with the network, if required.  Many providers do not require a username, or accept any username.  But if a username is required, it is specified here. |
| **gw4**  string | The IPv4 gateway for this interface.  Use the format `192.0.2.1`.  This parameter is mutually_exclusive with never_default4 parameter. |
| **gw4_ignore_auto**  boolean  *added in community.general 3.2.0* | Ignore automatically configured IPv4 routes.  **Choices:**   - `false` ← (default) - `true` |
| **gw6**  string | The IPv6 gateway for this interface.  Use the format `2001:db8::1`. |
| **gw6_ignore_auto**  boolean  *added in community.general 3.2.0* | Ignore automatically configured IPv6 routes.  **Choices:**   - `false` ← (default) - `true` |
| **hairpin**  boolean | This is only used with ‘bridge-slave’ - ‘hairpin mode’ for the slave, which allows frames to be sent back out through the slave the frame was received on.  The default change to `false` in community.general 7.0.0. It used to be `true` before.  **Choices:**   - `false` ← (default) - `true` |
| **hellotime**  integer | This is only used with bridge - [hello-time <1-10>] STP hello time, in seconds.  **Default:** `2` |
| **ifname**  string | The interface to bind the connection to.  The connection will only be applicable to this interface name.  A special value of `'*'` can be used for interface-independent connections.  The ifname argument is mandatory for all connection types except bond, team, bridge, vlan and vpn.  This parameter defaults to `conn_name` when left unset for all connection types except vpn that removes it. |
| **ignore_unsupported_suboptions**  boolean  *added in community.general 3.6.0* | Ignore suboptions which are invalid or unsupported by the version of NetworkManager/nmcli installed on the host.  Only `wifi` and `wifi_sec` options are currently affected.  **Choices:**   - `false` ← (default) - `true` |
| **ingress**  string | This is only used with VLAN - VLAN ingress priority mapping. |
| **ip4**  list / elements=string | List of IPv4 addresses to this interface.  Use the format `192.0.2.24/24` or `192.0.2.24`.  If defined and `method4` is not specified, automatically set `ipv4.method` to `manual`. |
| **ip6**  list / elements=string | List of IPv6 addresses to this interface.  Use the format `abbe::cafe/128` or `abbe::cafe`.  If defined and `method6` is not specified, automatically set `ipv6.method` to `manual`. |
| **ip_privacy6**  string  *added in community.general 4.2.0* | If enabled, it makes the kernel generate a temporary IPv6 address in addition to the public one.  **Choices:**   - `"disabled"` - `"prefer-public-addr"` - `"prefer-temp-addr"` - `"unknown"` |
| **ip_tunnel_dev**  string | This is used with GRE/IPIP/SIT - parent device this GRE/IPIP/SIT tunnel, can use ifname. |
| **ip_tunnel_input_key**  string  *added in community.general 3.6.0* | The key used for tunnel input packets.  Only used when `type=gre`. |
| **ip_tunnel_local**  string | This is used with GRE/IPIP/SIT - GRE/IPIP/SIT local IP address. |
| **ip_tunnel_output_key**  string  *added in community.general 3.6.0* | The key used for tunnel output packets.  Only used when `type=gre`. |
| **ip_tunnel_remote**  string | This is used with GRE/IPIP/SIT - GRE/IPIP/SIT destination IP address. |
| **mac**  string | MAC address of the connection.  Note this requires a recent kernel feature, originally introduced in 3.15 upstream kernel. |
| **macvlan**  dictionary  *added in community.general 6.6.0* | The configuration of the MAC VLAN connection.  Note the list of suboption attributes may vary depending on which version of NetworkManager/nmcli is installed on the host.  An up-to-date list of supported attributes can be found here: <https://networkmanager.dev/docs/api/latest/settings-macvlan.html>. |
| **mode**  integer / required | The macvlan mode, which specifies the communication mechanism between multiple macvlans on the same lower device.  Following choices are allowed: `1` **vepa**, `2` **bridge**, `3` **private**, `4` **passthru** and `5` **source**  **Choices:**   - `1` - `2` - `3` - `4` - `5` |
| **parent**  string / required | If given, specifies the parent interface name or parent connection UUID from which this MAC-VLAN interface should be created. If this property is not specified, the connection must contain an “802-3-ethernet” setting with a “mac-address” property. |
| **promiscuous**  boolean | Whether the interface should be put in promiscuous mode.  **Choices:**   - `false` - `true` |
| **tap**  boolean | Whether the interface should be a MACVTAP.  **Choices:**   - `false` - `true` |
| **master**  string | Master <master (ifname, or connection UUID or conn_name) of bridge, team, bond master connection profile.  Mandatory if `slave_type` is defined. |
| **maxage**  integer | This is only used with bridge - [max-age <6-42>] STP maximum message age, in seconds.  **Default:** `20` |
| **may_fail4**  boolean  *added in community.general 3.3.0* | If you need `ip4` configured before `network-online.target` is reached, set this option to `false`.  This option applies when `method4` is not `disabled`.  **Choices:**   - `false` - `true` ← (default) |
| **method4**  string  *added in community.general 2.2.0* | Configuration method to be used for IPv4.  If `ip4` is set, `ipv4.method` is automatically set to `manual` and this parameter is not needed.  **Choices:**   - `"auto"` - `"link-local"` - `"manual"` - `"shared"` - `"disabled"` |
| **method6**  string  *added in community.general 2.2.0* | Configuration method to be used for IPv6  If `ip6` is set, `ipv6.method` is automatically set to `manual` and this parameter is not needed.  `disabled` was added in community.general 3.3.0.  **Choices:**   - `"ignore"` - `"auto"` - `"dhcp"` - `"link-local"` - `"manual"` - `"shared"` - `"disabled"` |
| **miimon**  integer | This is only used with bond - miimon.  This parameter defaults to `100` when unset. |
| **mode**  string | This is the type of device or network connection that you wish to create for a bond or bridge.  **Choices:**   - `"802.3ad"` - `"active-backup"` - `"balance-alb"` - `"balance-rr"` ← (default) - `"balance-tlb"` - `"balance-xor"` - `"broadcast"` |
| **mtu**  integer | The connection MTU, e.g. 9000. This can’t be applied when creating the interface and is done once the interface has been created.  Can be used when modifying Team, VLAN, Ethernet (Future plans to implement wifi, gsm, pppoe, infiniband)  This parameter defaults to `1500` when unset. |
| **never_default4**  boolean  *added in community.general 2.0.0* | Set as default route.  This parameter is mutually_exclusive with gw4 parameter.  **Choices:**   - `false` ← (default) - `true` |
| **path_cost**  integer | This is only used with ‘bridge-slave’ - [<1-65535>] - STP port cost for destinations via this slave.  **Default:** `100` |
| **primary**  string | This is only used with bond and is the primary interface name (for “active-backup” mode), this is the usually the ‘ifname’. |
| **priority**  integer | This is only used with ‘bridge’ - sets STP priority.  **Default:** `128` |
| **route_metric4**  integer  *added in community.general 2.0.0* | Set metric level of ipv4 routes configured on interface. |
| **route_metric6**  integer  *added in community.general 4.4.0* | Set metric level of IPv6 routes configured on interface. |
| **routes4**  list / elements=string  *added in community.general 2.0.0* | The list of IPv4 routes.  Use the format `192.0.3.0/24 192.0.2.1`.  To specify more complex routes, use the `routes4_extended` option. |
| **routes4_extended**  list / elements=dictionary | The list of IPv4 routes. |
| **cwnd**  integer | The clamp for congestion window. |
| **ip**  string / required | IP or prefix of route.  Use the format `192.0.3.0/24`. |
| **metric**  integer | Route metric. |
| **mtu**  integer | If non-zero, only transmit packets of the specified size or smaller. |
| **next_hop**  string | Use the format `192.0.2.1`. |
| **onlink**  boolean | Pretend that the nexthop is directly attached to this link, even if it does not match any interface prefix.  **Choices:**   - `false` - `true` |
| **table**  integer | The table to add this route to.  The default depends on `ipv4.route-table`. |
| **tos**  integer | The Type Of Service. |
| **routes6**  list / elements=string  *added in community.general 4.4.0* | The list of IPv6 routes.  Use the format `fd12:3456:789a:1::/64 2001:dead:beef::1`.  To specify more complex routes, use the `routes6_extended` option. |
| **routes6_extended**  list / elements=dictionary | The list of IPv6 routes but with parameters. |
| **cwnd**  integer | The clamp for congestion window. |
| **ip**  string / required | IP or prefix of route.  Use the format `fd12:3456:789a:1::/64`. |
| **metric**  integer | Route metric. |
| **mtu**  integer | If non-zero, only transmit packets of the specified size or smaller. |
| **next_hop**  string | Use the format `2001:dead:beef::1`. |
| **onlink**  boolean | Pretend that the nexthop is directly attached to this link, even if it does not match any interface prefix.  **Choices:**   - `false` - `true` |
| **table**  integer | The table to add this route to.  The default depends on `ipv6.route-table`. |
| **routing_rules4**  list / elements=string  *added in community.general 3.3.0* | Is the same as in an `ip rule add` command, except always requires specifying a priority. |
| **runner**  string  *added in community.general 3.4.0* | This is the type of device or network connection that you wish to create for a team.  **Choices:**   - `"broadcast"` - `"roundrobin"` ← (default) - `"activebackup"` - `"loadbalance"` - `"lacp"` |
| **runner_fast_rate**  boolean  *added in community.general 6.5.0* | Option specifies the rate at which our link partner is asked to transmit LACPDU packets. If this is `true` then packets will be sent once per second. Otherwise they will be sent every 30 seconds.  Only allowed for `runner=lacp`.  **Choices:**   - `false` - `true` |
| **runner_hwaddr_policy**  string  *added in community.general 3.4.0* | This defines the policy of how hardware addresses of team device and port devices should be set during the team lifetime.  **Choices:**   - `"same_all"` - `"by_active"` - `"only_active"` |
| **slave_type**  string  *added in community.general 7.0.0* | Type of the device of this slave’s master connection (for example `bond`).  **Choices:**   - `"bond"` - `"bridge"` - `"team"` |
| **slavepriority**  integer | This is only used with ‘bridge-slave’ - [<0-63>] - STP priority of this slave.  **Default:** `32` |
| **ssid**  string  *added in community.general 3.0.0* | Name of the Wireless router or the access point. |
| **state**  string / required | Whether the device should exist or not, taking action if the state is different from what is stated.  **Choices:**   - `"absent"` - `"present"` |
| **stp**  boolean | This is only used with bridge and controls whether Spanning Tree Protocol (STP) is enabled for this bridge.  **Choices:**   - `false` - `true` ← (default) |
| **transport_mode**  string  *added in community.general 5.8.0* | This option sets the connection type of Infiniband IPoIB devices.  **Choices:**   - `"datagram"` - `"connected"` |
| **type**  string | This is the type of device or network connection that you wish to create or modify.  Type `dummy` is added in community.general 3.5.0.  Type `generic` is added in Ansible 2.5.  Type `infiniband` is added in community.general 2.0.0.  Type `gsm` is added in community.general 3.7.0.  Type `macvlan` is added in community.general 6.6.0.  Type `wireguard` is added in community.general 4.3.0.  Type `vpn` is added in community.general 5.1.0.  Using `bond-slave`, `bridge-slave`, or `team-slave` implies `ethernet` connection type with corresponding `slave_type` option.  If you want to control non-ethernet connection attached to `bond`, `bridge`, or `team` consider using `slave_type` option.  **Choices:**   - `"bond"` - `"bond-slave"` - `"bridge"` - `"bridge-slave"` - `"dummy"` - `"ethernet"` - `"generic"` - `"gre"` - `"infiniband"` - `"ipip"` - `"macvlan"` - `"sit"` - `"team"` - `"team-slave"` - `"vlan"` - `"vxlan"` - `"wifi"` - `"gsm"` - `"wireguard"` - `"vpn"` |
| **updelay**  integer | This is only used with bond - updelay. |
| **vlandev**  string | This is only used with VLAN - parent device this VLAN is on, can use ifname. |
| **vlanid**  integer | This is only used with VLAN - VLAN ID in range <0-4095>. |
| **vpn**  dictionary  *added in community.general 5.1.0* | Configuration of a VPN connection (PPTP and L2TP).  In order to use L2TP you need to be sure that `network-manager-l2tp` - and `network-manager-l2tp-gnome` if host has UI - are installed on the host. |
| **gateway**  string / required | The gateway to connection. It can be an IP address (for example `192.0.2.1`) or a FQDN address (for example `vpn.example.com`). |
| **ipsec-enabled**  boolean | Enable or disable IPSec tunnel to L2TP host.  This option is need when `vpn.service-type` is `org.freedesktop.NetworkManager.l2tp`.  **Choices:**   - `false` - `true` |
| **ipsec-psk**  string | The pre-shared key in base64 encoding.  You can encode using this Ansible jinja2 expression: `"0s{{ '[YOUR PRE-SHARED KEY]' | ansible.builtin.b64encode }}"`.  This is only used when `vpn.ipsec-enabled=true`. |
| **password-flags**  integer | NMSettingSecretFlags indicating how to handle the `vpn.password` property.  Following choices are allowed: `0` **NONE**: The system is responsible for providing and storing this secret (default); `1` **AGENT_OWNED**: A user secret agent is responsible for providing and storing this secret; when it is required agents will be asked to retrieve it; `2` **NOT_SAVED**: This secret should not be saved, but should be requested from the user each time it is needed; `4` **NOT_REQUIRED**: In situations where it cannot be automatically determined that the secret is required (some VPNs and PPP providers do not require all secrets) this flag indicates that the specific secret is not required.  **Choices:**   - `0` ← (default) - `1` - `2` - `4` |
| **permissions**  string / required | User that will have permission to use the connection. |
| **service-type**  string / required | This defines the service type of connection. |
| **user**  string / required | Username provided by VPN administrator. |
| **vxlan_id**  integer | This is only used with VXLAN - VXLAN ID. |
| **vxlan_local**  string | This is only used with VXLAN - VXLAN local IP address. |
| **vxlan_remote**  string | This is only used with VXLAN - VXLAN destination IP address. |
| **wifi**  dictionary  *added in community.general 3.5.0* | The configuration of the WiFi connection.  Note the list of suboption attributes may vary depending on which version of NetworkManager/nmcli is installed on the host.  An up-to-date list of supported attributes can be found here: <https://networkmanager.dev/docs/api/latest/settings-802-11-wireless.html>.  For instance to create a hidden AP mode WiFi connection: `{hidden: true, mode: ap}`. |
| **ap-isolation**  integer | Configures AP isolation, which prevents communication between wireless devices connected to this AP.  This property can be set to a value different from `-1` only when the interface is configured in AP mode.  If set to `1`, devices are not able to communicate with each other. This increases security because it protects devices against attacks from other clients in the network. At the same time, it prevents devices to access resources on the same wireless networks as file shares, printers, etc.  If set to `0`, devices can talk to each other.  When set to `-1`, the global default is used; in case the global default is unspecified it is assumed to be `0`.  **Choices:**   - `-1` ← (default) - `0` - `1` |
| **assigned-mac-address**  string | The new field for the cloned MAC address.  It can be either a hardware address in ASCII representation, or one of the special values `preserve`, `permanent`, `random` or `stable`.  This field replaces the deprecated `wifi.cloned-mac-address` on D-Bus, which can only contain explicit hardware addresses.  Note that this property only exists in D-Bus API. libnm and nmcli continue to call this property `cloned-mac-address`. |
| **band**  string | 802.11 frequency band of the network.  One of `a` for 5GHz 802.11a or `bg` for 2.4GHz 802.11.  This will lock associations to the Wi-Fi network to the specific band, so for example, if `a` is specified, the device will not associate with the same network in the 2.4GHz band even if the network’s settings are compatible.  This setting depends on specific driver capability and may not work with all drivers.  **Choices:**   - `"a"` - `"bg"` |
| **bssid**  string | If specified, directs the device to only associate with the given access point.  This capability is highly driver dependent and not supported by all devices.  Note this property does not control the BSSID used when creating an Ad-Hoc network and is unlikely to in the future. |
| **channel**  integer | Wireless channel to use for the Wi-Fi connection.  The device will only join (or create for Ad-Hoc networks) a Wi-Fi network on the specified channel.  Because channel numbers overlap between bands, this property also requires the `wifi.band` property to be set.  **Default:** `0` |
| **cloned-mac-address**  string | This D-Bus field is deprecated in favor of `wifi.assigned-mac-address` which is more flexible and allows specifying special variants like `random`.  For libnm and nmcli, this field is called `cloned-mac-address`. |
| **generate-mac-address-mask**  string | With `wifi.cloned-mac-address` setting `random` or `stable`, by default all bits of the MAC address are scrambled and a locally-administered, unicast MAC address is created. This property allows to specify that certain bits are fixed.  Note that the least significant bit of the first MAC address will always be unset to create a unicast MAC address.  If the property is `null`, it is eligible to be overwritten by a default connection setting.  If the value is still `null` or an empty string, the default is to create a locally-administered, unicast MAC address.  If the value contains one MAC address, this address is used as mask. The set bits of the mask are to be filled with the current MAC address of the device, while the unset bits are subject to randomization.  Setting `FE:FF:FF:00:00:00` means to preserve the OUI of the current MAC address and only randomize the lower 3 bytes using the `random` or `stable` algorithm.  If the value contains one additional MAC address after the mask, this address is used instead of the current MAC address to fill the bits that shall not be randomized.  For example, a value of `FE:FF:FF:00:00:00 68:F7:28:00:00:00` will set the OUI of the MAC address to 68:F7:28, while the lower bits are randomized.  A value of `02:00:00:00:00:00 00:00:00:00:00:00` will create a fully scrambled globally-administered, burned-in MAC address.  If the value contains more than one additional MAC addresses, one of them is chosen randomly. For example, `02:00:00:00:00:00 00:00:00:00:00:00 02:00:00:00:00:00` will create a fully scrambled MAC address, randomly locally or globally administered. |
| **hidden**  boolean | If `true`, indicates that the network is a non-broadcasting network that hides its SSID. This works both in infrastructure and AP mode.  In infrastructure mode, various workarounds are used for a more reliable discovery of hidden networks, such as probe-scanning the SSID. However, these workarounds expose inherent insecurities with hidden SSID networks, and thus hidden SSID networks should be used with caution.  In AP mode, the created network does not broadcast its SSID.  Note that marking the network as hidden may be a privacy issue for you (in infrastructure mode) or client stations (in AP mode), as the explicit probe-scans are distinctly recognizable on the air.  **Choices:**   - `false` ← (default) - `true` |
| **mac-address**  string | If specified, this connection will only apply to the Wi-Fi device whose permanent MAC address matches.  This property does not change the MAC address of the device (for example for MAC spoofing). |
| **mac-address-blacklist**  list / elements=string | A list of permanent MAC addresses of Wi-Fi devices to which this connection should never apply.  Each MAC address should be given in the standard hex-digits-and-colons notation (for example, `00:11:22:33:44:55`). |
| **mac-address-randomization**  integer | One of `0` (never randomize unless the user has set a global default to randomize and the supplicant supports randomization), `1` (never randomize the MAC address), or `2` (always randomize the MAC address).  This property is deprecated for `wifi.cloned-mac-address`.  **Choices:**   - `0` ← (default) - `1` - `2` |
| **mode**  string | Wi-Fi network mode. If blank, `infrastructure` is assumed.  **Choices:**   - `"infrastructure"` ← (default) - `"mesh"` - `"adhoc"` - `"ap"` |
| **mtu**  integer | If non-zero, only transmit packets of the specified size or smaller, breaking larger packets up into multiple Ethernet frames.  **Default:** `0` |
| **powersave**  integer | One of `2` (disable Wi-Fi power saving), `3` (enable Wi-Fi power saving), `1` (don’t touch currently configure setting) or `0` (use the globally configured value).  All other values are reserved.  **Choices:**   - `0` ← (default) - `1` - `2` - `3` |
| **rate**  integer | If non-zero, directs the device to only use the specified bitrate for communication with the access point.  Units are in Kb/s, so for example `5500` = 5.5 Mbit/s.  This property is highly driver dependent and not all devices support setting a static bitrate.  **Default:** `0` |
| **tx-power**  integer | If non-zero, directs the device to use the specified transmit power.  Units are dBm.  This property is highly driver dependent and not all devices support setting a static transmit power.  **Default:** `0` |
| **wake-on-wlan**  integer | The NMSettingWirelessWakeOnWLan options to enable. Not all devices support all options.  May be any combination of `NM_SETTING_WIRELESS_WAKE_ON_WLAN_ANY` (`0x2`), `NM_SETTING_WIRELESS_WAKE_ON_WLAN_DISCONNECT` (`0x4`), `NM_SETTING_WIRELESS_WAKE_ON_WLAN_MAGIC` (`0x8`), `NM_SETTING_WIRELESS_WAKE_ON_WLAN_GTK_REKEY_FAILURE` (`0x10`), `NM_SETTING_WIRELESS_WAKE_ON_WLAN_EAP_IDENTITY_REQUEST` (`0x20`), `NM_SETTING_WIRELESS_WAKE_ON_WLAN_4WAY_HANDSHAKE` (`0x40`), `NM_SETTING_WIRELESS_WAKE_ON_WLAN_RFKILL_RELEASE` (`0x80`), `NM_SETTING_WIRELESS_WAKE_ON_WLAN_TCP` (`0x100`) or the special values `0x1` (to use global settings) and `0x8000` (to disable management of Wake-on-LAN in NetworkManager).  Note the option values’ sum must be specified in order to combine multiple options.  **Default:** `1` |
| **wifi_sec**  dictionary  *added in community.general 3.0.0* | The security configuration of the WiFi connection.  Note the list of suboption attributes may vary depending on which version of NetworkManager/nmcli is installed on the host.  An up-to-date list of supported attributes can be found here: <https://networkmanager.dev/docs/api/latest/settings-802-11-wireless-security.html>.  For instance to use common WPA-PSK auth with a password: `{key-mgmt: wpa-psk, psk: my_password}`. |
| **auth-alg**  string | When WEP is used (that is, if `wifi_sec.key-mgmt` is `none` or `ieee8021x`) indicate the 802.11 authentication algorithm required by the AP here.  One of `open` for Open System, `shared` for Shared Key, or `leap` for Cisco LEAP.  When using Cisco LEAP (that is, if `wifi_sec.key-mgmt=ieee8021x` and `wifi_sec.auth-alg=leap`) the `wifi_sec.leap-username` and `wifi_sec.leap-password` properties must be specified.  **Choices:**   - `"open"` - `"shared"` - `"leap"` |
| **fils**  integer | Indicates whether Fast Initial Link Setup (802.11ai) must be enabled for the connection.  One of `0` (use global default value), `1` (disable FILS), `2` (enable FILS if the supplicant and the access point support it) or `3` (enable FILS and fail if not supported).  When set to `0` and no global default is set, FILS will be optionally enabled.  **Choices:**   - `0` ← (default) - `1` - `2` - `3` |
| **group**  list / elements=string | A list of group/broadcast encryption algorithms which prevents connections to Wi-Fi networks that do not utilize one of the algorithms in the list.  For maximum compatibility leave this property empty.  **Choices:**   - `"wep40"` - `"wep104"` - `"tkip"` - `"ccmp"` |
| **key-mgmt**  string | Key management used for the connection.  One of `none` (WEP or no password protection), `ieee8021x` (Dynamic WEP), `owe` (Opportunistic Wireless Encryption), `wpa-psk` (WPA2 + WPA3 personal), `sae` (WPA3 personal only), `wpa-eap` (WPA2 + WPA3 enterprise) or `wpa-eap-suite-b-192` (WPA3 enterprise only).  This property must be set for any Wi-Fi connection that uses security.  **Choices:**   - `"none"` - `"ieee8021x"` - `"owe"` - `"wpa-psk"` - `"sae"` - `"wpa-eap"` - `"wpa-eap-suite-b-192"` |
| **leap-password**  string | The login password for legacy LEAP connections (that is, if `wifi_sec.key-mgmt=ieee8021x` and `wifi_sec.auth-alg=leap`). |
| **leap-password-flags**  list / elements=integer | Flags indicating how to handle the `wifi_sec.leap-password` property. |
| **leap-username**  string | The login username for legacy LEAP connections (that is, if `wifi_sec.key-mgmt=ieee8021x` and `wifi_sec.auth-alg=leap`). |
| **pairwise**  list / elements=string | A list of pairwise encryption algorithms which prevents connections to Wi-Fi networks that do not utilize one of the algorithms in the list.  For maximum compatibility leave this property empty.  **Choices:**   - `"tkip"` - `"ccmp"` |
| **pmf**  integer | Indicates whether Protected Management Frames (802.11w) must be enabled for the connection.  One of `0` (use global default value), `1` (disable PMF), `2` (enable PMF if the supplicant and the access point support it) or `3` (enable PMF and fail if not supported).  When set to `0` and no global default is set, PMF will be optionally enabled.  **Choices:**   - `0` ← (default) - `1` - `2` - `3` |
| **proto**  list / elements=string | List of strings specifying the allowed WPA protocol versions to use.  Each element may be `wpa` (allow WPA) or `rsn` (allow WPA2/RSN).  If not specified, both WPA and RSN connections are allowed.  **Choices:**   - `"wpa"` - `"rsn"` |
| **psk**  string | Pre-Shared-Key for WPA networks.  For WPA-PSK, it is either an ASCII passphrase of 8 to 63 characters that is (as specified in the 802.11i standard) hashed to derive the actual key, or the key in form of 64 hexadecimal character.  The WPA3-Personal networks use a passphrase of any length for SAE authentication. |
| **psk-flags**  list / elements=integer | Flags indicating how to handle the `wifi_sec.psk` property. |
| **wep-key-flags**  list / elements=integer | Flags indicating how to handle the `wifi_sec.wep-key0`, `wifi_sec.wep-key1`, `wifi_sec.wep-key2`, and `wifi_sec.wep-key3` properties. |
| **wep-key-type**  integer | Controls the interpretation of WEP keys.  Allowed values are `1`, in which case the key is either a 10- or 26-character hexadecimal string, or a 5- or 13-character ASCII password; or `2`, in which case the passphrase is provided as a string and will be hashed using the de-facto MD5 method to derive the actual WEP key.  **Choices:**   - `1` - `2` |
| **wep-key0**  string | Index 0 WEP key. This is the WEP key used in most networks.  See the `wifi_sec.wep-key-type` property for a description of how this key is interpreted. |
| **wep-key1**  string | Index 1 WEP key. This WEP index is not used by most networks.  See the `wifi_sec.wep-key-type` property for a description of how this key is interpreted. |
| **wep-key2**  string | Index 2 WEP key. This WEP index is not used by most networks.  See the `wifi_sec.wep-key-type` property for a description of how this key is interpreted. |
| **wep-key3**  string | Index 3 WEP key. This WEP index is not used by most networks.  See the `wifi_sec.wep-key-type` property for a description of how this key is interpreted. |
| **wep-tx-keyidx**  integer | When static WEP is used (that is, if `wifi_sec.key-mgmt=none`) and a non-default WEP key index is used by the AP, put that WEP key index here.  Valid values are `0` (default key) through `3`.  Note that some consumer access points (like the Linksys WRT54G) number the keys `1` to `4`.  **Choices:**   - `0` ← (default) - `1` - `2` - `3` |
| **wps-method**  integer | Flags indicating which mode of WPS is to be used if any.  There is little point in changing the default setting as NetworkManager will automatically determine whether it is feasible to start WPS enrollment from the Access Point capabilities.  WPS can be disabled by setting this property to a value of `1`.  **Default:** `0` |
| **wireguard**  dictionary  *added in community.general 4.3.0* | The configuration of the Wireguard connection.  Note the list of suboption attributes may vary depending on which version of NetworkManager/nmcli is installed on the host.  An up-to-date list of supported attributes can be found here: <https://networkmanager.dev/docs/api/latest/settings-wireguard.html>.  For instance to configure a listen port: `{listen-port: 12345}`. |
| **fwmark**  integer | The 32-bit fwmark for outgoing packets.  The use of fwmark is optional and is by default off. Setting it to 0 disables it.  Note that `wireguard.ip4-auto-default-route` or `wireguard.ip6-auto-default-route` enabled, implies to automatically choose a fwmark. |
| **ip4-auto-default-route**  boolean | Whether to enable special handling of the IPv4 default route.  If enabled, the IPv4 default route from `wireguard.peer-routes` will be placed to a dedicated routing-table and two policy routing rules will be added.  The fwmark number is also used as routing-table for the default-route, and if fwmark is zero, an unused fwmark/table is chosen automatically. This corresponds to what wg-quick does with Table=auto and what WireGuard calls “Improved Rule-based Routing”  **Choices:**   - `false` - `true` |
| **ip6-auto-default-route**  boolean | Like `wireguard.ip4-auto-default-route`, but for the IPv6 default route.  **Choices:**   - `false` - `true` |
| **listen-port**  integer | The WireGuard connection listen-port. If not specified, the port will be chosen randomly when the interface comes up. |
| **mtu**  integer | If non-zero, only transmit packets of the specified size or smaller, breaking larger packets up into multiple fragments.  If zero a default MTU is used. Note that contrary to wg-quick’s MTU setting, this does not take into account the current routes at the time of activation. |
| **peer-routes**  boolean | Whether to automatically add routes for the AllowedIPs ranges of the peers.  If `true` (the default), NetworkManager will automatically add routes in the routing tables according to `ipv4.route-table` and `ipv6.route-table`. Usually you want this automatism enabled.  If `false`, no such routes are added automatically. In this case, the user may want to configure static routes in `ipv4.routes` and `ipv6.routes`, respectively.  Note that if the peer’s AllowedIPs is `0.0.0.0/0` or `::/0` and the profile’s `ipv4.never-default` or `ipv6.never-default` setting is enabled, the peer route for this peer won’t be added automatically.  **Choices:**   - `false` - `true` |
| **private-key**  string | The 256 bit private-key in base64 encoding. |
| **private-key-flags**  integer | `NMSettingSecretFlags` indicating how to handle the `wireguard.private-key` property.  **Choices:**   - `0` - `1` - `2` |
| **xmit_hash_policy**  string  *added in community.general 5.6.0* | This is only used with bond - xmit_hash_policy type. |
| **zone**  string  *added in community.general 2.0.0* | The trust level of the connection.  When updating this property on a currently activated connection, the change takes effect immediately. |

## [Attributes](nmcli_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](nmcli_module.md#id5)

```yaml+jinja
# These examples are using the following inventory:
#
# ## Directory layout:
#
# |_/inventory/cloud-hosts
# |           /group_vars/openstack-stage.yml
# |           /host_vars/controller-01.openstack.host.com
# |           /host_vars/controller-02.openstack.host.com
# |_/playbook/library/nmcli.py
# |          /playbook-add.yml
# |          /playbook-del.yml
# ```
#
# ## inventory examples
# ### groups_vars
# ```yml
# ---
# #devops_os_define_network
# storage_gw: "192.0.2.254"
# external_gw: "198.51.100.254"
# tenant_gw: "203.0.113.254"
#
# #Team vars
# nmcli_team:
#   - conn_name: tenant
#     ip4: '{{ tenant_ip }}'
#     gw4: '{{ tenant_gw }}'
#   - conn_name: external
#     ip4: '{{ external_ip }}'
#     gw4: '{{ external_gw }}'
#   - conn_name: storage
#     ip4: '{{ storage_ip }}'
#     gw4: '{{ storage_gw }}'
# nmcli_team_slave:
#   - conn_name: em1
#     ifname: em1
#     master: tenant
#   - conn_name: em2
#     ifname: em2
#     master: tenant
#   - conn_name: p2p1
#     ifname: p2p1
#     master: storage
#   - conn_name: p2p2
#     ifname: p2p2
#     master: external
#
# #bond vars
# nmcli_bond:
#   - conn_name: tenant
#     ip4: '{{ tenant_ip }}'
#     gw4: ''
#     mode: balance-rr
#   - conn_name: external
#     ip4: '{{ external_ip }}'
#     gw4: ''
#     mode: balance-rr
#   - conn_name: storage
#     ip4: '{{ storage_ip }}'
#     gw4: '{{ storage_gw }}'
#     mode: balance-rr
# nmcli_bond_slave:
#   - conn_name: em1
#     ifname: em1
#     master: tenant
#   - conn_name: em2
#     ifname: em2
#     master: tenant
#   - conn_name: p2p1
#     ifname: p2p1
#     master: storage
#   - conn_name: p2p2
#     ifname: p2p2
#     master: external
#
# #ethernet vars
# nmcli_ethernet:
#   - conn_name: em1
#     ifname: em1
#     ip4:
#       - '{{ tenant_ip }}'
#       - '{{ second_tenant_ip }}'
#     gw4: '{{ tenant_gw }}'
#   - conn_name: em2
#     ifname: em2
#     ip4: '{{ tenant_ip1 }}'
#     gw4: '{{ tenant_gw }}'
#   - conn_name: p2p1
#     ifname: p2p1
#     ip4: '{{ storage_ip }}'
#     gw4: '{{ storage_gw }}'
#   - conn_name: p2p2
#     ifname: p2p2
#     ip4: '{{ external_ip }}'
#     gw4: '{{ external_gw }}'
# ```
#
# ### host_vars
# ```yml
# ---
# storage_ip: "192.0.2.91/23"
# external_ip: "198.51.100.23/21"
# tenant_ip: "203.0.113.77/23"
# second_tenant_ip: "204.0.113.77/23"
# ```

## playbook-add.yml example

---
- hosts: openstack-stage
  remote_user: root
  tasks:

  - name: Install needed network manager libs
    ansible.builtin.package:
      name:
        - NetworkManager-libnm
        - nm-connection-editor
        - libsemanage-python
        - policycoreutils-python
      state: present

##### Working with all cloud nodes - Teaming
  - name: Try nmcli add team - conn_name only & ip4 gw4
    community.general.nmcli:
      type: team
      conn_name: '{{ item.conn_name }}'
      ip4: '{{ item.ip4 }}'
      gw4: '{{ item.gw4 }}'
      state: present
    with_items:
      - '{{ nmcli_team }}'

  - name: Try nmcli add teams-slave
    community.general.nmcli:
      type: team-slave
      conn_name: '{{ item.conn_name }}'
      ifname: '{{ item.ifname }}'
      master: '{{ item.master }}'
      state: present
    with_items:
      - '{{ nmcli_team_slave }}'

###### Working with all cloud nodes - Bonding
  - name: Try nmcli add bond - conn_name only & ip4 gw4 mode
    community.general.nmcli:
      type: bond
      conn_name: '{{ item.conn_name }}'
      ip4: '{{ item.ip4 }}'
      gw4: '{{ item.gw4 }}'
      mode: '{{ item.mode }}'
      state: present
    with_items:
      - '{{ nmcli_bond }}'

  - name: Try nmcli add bond-slave
    community.general.nmcli:
      type: bond-slave
      conn_name: '{{ item.conn_name }}'
      ifname: '{{ item.ifname }}'
      master: '{{ item.master }}'
      state: present
    with_items:
      - '{{ nmcli_bond_slave }}'

##### Working with all cloud nodes - Ethernet
  - name: Try nmcli add Ethernet - conn_name only & ip4 gw4
    community.general.nmcli:
      type: ethernet
      conn_name: '{{ item.conn_name }}'
      ip4: '{{ item.ip4 }}'
      gw4: '{{ item.gw4 }}'
      state: present
    with_items:
      - '{{ nmcli_ethernet }}'

## playbook-del.yml example
- hosts: openstack-stage
  remote_user: root
  tasks:

  - name: Try nmcli del team - multiple
    community.general.nmcli:
      conn_name: '{{ item.conn_name }}'
      state: absent
    with_items:
      - conn_name: em1
      - conn_name: em2
      - conn_name: p1p1
      - conn_name: p1p2
      - conn_name: p2p1
      - conn_name: p2p2
      - conn_name: tenant
      - conn_name: storage
      - conn_name: external
      - conn_name: team-em1
      - conn_name: team-em2
      - conn_name: team-p1p1
      - conn_name: team-p1p2
      - conn_name: team-p2p1
      - conn_name: team-p2p2

  - name: Add an Ethernet connection with static IP configuration
    community.general.nmcli:
      conn_name: my-eth1
      ifname: eth1
      type: ethernet
      ip4: 192.0.2.100/24
      gw4: 192.0.2.1
      state: present

  - name: Add an Team connection with static IP configuration
    community.general.nmcli:
      conn_name: my-team1
      ifname: my-team1
      type: team
      ip4: 192.0.2.100/24
      gw4: 192.0.2.1
      state: present
      autoconnect: true

  - name: Optionally, at the same time specify IPv6 addresses for the device
    community.general.nmcli:
      conn_name: my-eth1
      ifname: eth1
      type: ethernet
      ip4: 192.0.2.100/24
      gw4: 192.0.2.1
      ip6: 2001:db8::cafe
      gw6: 2001:db8::1
      state: present

  - name: Add two IPv4 DNS server addresses
    community.general.nmcli:
      conn_name: my-eth1
      type: ethernet
      dns4:
      - 192.0.2.53
      - 198.51.100.53
      state: present

  - name: Make a profile usable for all compatible Ethernet interfaces
    community.general.nmcli:
      ctype: ethernet
      name: my-eth1
      ifname: '*'
      state: present

  - name: Change the property of a setting e.g. MTU
    community.general.nmcli:
      conn_name: my-eth1
      mtu: 9000
      type: ethernet
      state: present

  - name: Add second ip4 address
    community.general.nmcli:
      conn_name: my-eth1
      ifname: eth1
      type: ethernet
      ip4:
        - 192.0.2.100/24
        - 192.0.3.100/24
      state: present

  - name: Add second ip6 address
    community.general.nmcli:
      conn_name: my-eth1
      ifname: eth1
      type: ethernet
      ip6:
        - 2001:db8::cafe
        - 2002:db8::cafe
      state: present

  - name: Add VxLan
    community.general.nmcli:
      type: vxlan
      conn_name: vxlan_test1
      vxlan_id: 16
      vxlan_local: 192.168.1.2
      vxlan_remote: 192.168.1.5

  - name: Add gre
    community.general.nmcli:
      type: gre
      conn_name: gre_test1
      ip_tunnel_dev: eth0
      ip_tunnel_local: 192.168.1.2
      ip_tunnel_remote: 192.168.1.5

  - name: Add ipip
    community.general.nmcli:
      type: ipip
      conn_name: ipip_test1
      ip_tunnel_dev: eth0
      ip_tunnel_local: 192.168.1.2
      ip_tunnel_remote: 192.168.1.5

  - name: Add sit
    community.general.nmcli:
      type: sit
      conn_name: sit_test1
      ip_tunnel_dev: eth0
      ip_tunnel_local: 192.168.1.2
      ip_tunnel_remote: 192.168.1.5

  - name: Add zone
    community.general.nmcli:
      type: ethernet
      conn_name: my-eth1
      zone: external
      state: present

# nmcli exits with status 0 if it succeeds and exits with a status greater
# than zero when there is a failure. The following list of status codes may be
# returned:
#
#     - 0 Success - indicates the operation succeeded
#     - 1 Unknown or unspecified error
#     - 2 Invalid user input, wrong nmcli invocation
#     - 3 Timeout expired (see --wait option)
#     - 4 Connection activation failed
#     - 5 Connection deactivation failed
#     - 6 Disconnecting device failed
#     - 7 Connection deletion failed
#     - 8 NetworkManager is not running
#     - 9 nmcli and NetworkManager versions mismatch
#     - 10 Connection, device, or access point does not exist.

- name: Create the wifi connection
  community.general.nmcli:
    type: wifi
    conn_name: Brittany
    ifname: wlp4s0
    ssid: Brittany
    wifi_sec:
      key-mgmt: wpa-psk
      psk: my_password
    autoconnect: true
    state: present

- name: Create a hidden AP mode wifi connection
  community.general.nmcli:
    type: wifi
    conn_name: ChocoMaster
    ifname: wlo1
    ssid: ChocoMaster
    wifi:
      hidden: true
      mode: ap
    autoconnect: true
    state: present

- name: Create a gsm connection
  community.general.nmcli:
    type: gsm
    conn_name: my-gsm-provider
    ifname: cdc-wdm0
    gsm:
        apn: my.provider.apn
        username: my-provider-username
        password: my-provider-password
        pin: my-sim-pin
    autoconnect: true
    state: present

- name: Create a macvlan connection
  community.general.nmcli:
    type: macvlan
    conn_name: my-macvlan-connection
    ifname: mymacvlan0
    macvlan:
        mode: 2
        parent: eth1
    autoconnect: true
    state: present

- name: Create a wireguard connection
  community.general.nmcli:
    type: wireguard
    conn_name: my-wg-provider
    ifname: mywg0
    wireguard:
        listen-port: 51820
        private-key: my-private-key
    autoconnect: true
    state: present

- name: >-
    Create a VPN L2TP connection for ansible_user to connect on vpn.example.com
    authenticating with user 'brittany' and pre-shared key as 'Brittany123'
  community.general.nmcli:
    type: vpn
    conn_name: my-vpn-connection
    vpn:
        permissions: "{{ ansible_user }}"
        service-type: org.freedesktop.NetworkManager.l2tp
        gateway: vpn.example.com
        password-flags: 2
        user: brittany
        ipsec-enabled: true
        ipsec-psk: "0s{{ 'Brittany123' | ansible.builtin.b64encode }}"
    autoconnect: false
    state: present

## Creating bond attached to bridge example
- name: Create bond attached to bridge
  community.general.nmcli:
    type: bond
    conn_name: bond0
    slave_type: bridge
    master: br0
    state: present

- name: Create master bridge
  community.general.nmcli:
    type: bridge
    conn_name: br0
    method4: disabled
    method6: disabled
    state: present

## Creating vlan connection attached to bridge
- name: Create master bridge
  community.general.nmcli:
    type: bridge
    conn_name: br0
    state: present

- name: Create VLAN 5
  community.general.nmcli:
    type: vlan
    conn_name: eth0.5
    slave_type: bridge
    master: br0
    vlandev: eth0
    vlanid: 5
    state: present

## Defining ip rules while setting a static IP
## table 'production' is set with id 200 in this example.
- name: Set Static ips for interface with ip rules and routes
  community.general.nmcli:
    type: ethernet
    conn_name: 'eth0'
    ip4: '192.168.1.50'
    gw4: '192.168.1.1'
    state: present
    routes4_extended:
      - ip: "0.0.0.0/0"
        next_hop: "192.168.1.1"
        table: "production"
    routing_rules4:
      - "priority 0 from 192.168.1.50 table 200"
```

### Authors

- Chris Long (@alcamie101)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
