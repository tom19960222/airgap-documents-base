---
collection: ansible
version: "6"
title: "community.routeros.api_info module – Retrieve information from API"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/routeros/api_info_module.html
fetched_at: 2026-07-27T17:20:53+00:00
---
# community.routeros.api_info module – Retrieve information from API

> **Note:**
>
> This module is part of the [community.routeros collection](https://galaxy.ansible.com/community/routeros) (version 2.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.routeros`.
> You need further requirements to be able to use this module,
> see [Requirements](api_info_module.md#ansible-collections-community-routeros-api-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.routeros.api_info`.

New in community.routeros 2.2.0

- [Synopsis](api_info_module.md#synopsis)
- [Requirements](api_info_module.md#requirements)
- [Parameters](api_info_module.md#parameters)
- [Attributes](api_info_module.md#attributes)
- [See Also](api_info_module.md#see-also)
- [Examples](api_info_module.md#examples)
- [Return Values](api_info_module.md#return-values)

## [Synopsis](api_info_module.md#id1)

- Allows to retrieve information for a path using the API.
- This can be used to backup a path to restore it with the [community.routeros.api_modify](api_modify_module.md#ansible-collections-community-routeros-api-modify-module) module.
- Entries are normalized, dynamic and builtin entries are not returned. Use the *handle_disabled* and *hide_defaults* options to control normalization, the *include_dynamic* and *include_builtin* options to also return dynamic resp. builtin entries, and use *unfiltered* to return all fields including counters.
- **Note** that this module is still heavily in development, and only supports **some** paths. If you want to support new paths, or think you found problems with existing paths, please first [create an issue in the community.routeros Issue Tracker](https://github.com/ansible-collections/community.routeros/issues/).

## [Requirements](api_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- librouteros
- Python >= 3.6 (for librouteros)

## [Parameters](api_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  added in community.routeros 1.2.0 | PEM formatted file that contains a CA certificate to be used for certificate validation.  See also *validate_cert_hostname*. Only used when *tls=true* and *validate_certs=true*. |
| **encoding**  string  added in community.routeros 2.1.0 | Use the specified encoding when communicating with the RouterOS device.  Default is `ASCII`. Note that `UTF-8` requires librouteros 3.2.1 or newer.  Default: `"ASCII"` |
| **force_no_cert**  boolean  added in community.routeros 2.4.0 | Set to `true` to connect without a certificate when *tls=true*.  See also *validate_certs*.  **Note:** this forces the use of anonymous Diffie-Hellman (ADH) ciphers. The protocol is susceptible to Man-in-the-Middle attacks, because the keys used in the exchange are not authenticated. Instead of simply connecting without a certificate to “make things work” have a look at *validate_certs* and *ca_path*.  Choices:   - `false` ← (default) - `true` |
| **handle_disabled**  string | How to handle unset values.  `exclamation` prepends the keys with `!` in the output with value `null`.  `null-value` uses the regular key with value `null`.  `omit` omits these values from the result.  Choices:   - `"exclamation"` ← (default) - `"null-value"` - `"omit"` |
| **hide_defaults**  boolean | Whether to hide default values.  Choices:   - `false` - `true` ← (default) |
| **hostname**  string / required | RouterOS hostname API. |
| **include_builtin**  boolean  added in community.routeros 2.4.0 | Whether to include builtin values.  By default, they are not returned, and the `builtin` keys are omitted.  If set to `true`, they are returned as well, and the `builtin` keys are returned as well.  Choices:   - `false` ← (default) - `true` |
| **include_dynamic**  boolean | Whether to include dynamic values.  By default, they are not returned, and the `dynamic` keys are omitted.  If set to `true`, they are returned as well, and the `dynamic` keys are returned as well.  Choices:   - `false` ← (default) - `true` |
| **password**  string / required | RouterOS user password. |
| **path**  string / required | Path to query.  An example value is `ip address`. This is equivalent to running `/ip address print` in the RouterOS CLI.  Choices:   - `"caps-man aaa"` - `"caps-man access-list"` - `"caps-man configuration"` - `"caps-man datapath"` - `"caps-man manager"` - `"caps-man provisioning"` - `"caps-man security"` - `"certificate settings"` - `"interface bonding"` - `"interface bridge"` - `"interface bridge mlag"` - `"interface bridge port"` - `"interface bridge port-controller"` - `"interface bridge port-extender"` - `"interface bridge settings"` - `"interface bridge vlan"` - `"interface detect-internet"` - `"interface eoip"` - `"interface ethernet"` - `"interface ethernet poe"` - `"interface ethernet switch"` - `"interface ethernet switch port"` - `"interface gre"` - `"interface gre6"` - `"interface l2tp-server server"` - `"interface list"` - `"interface list member"` - `"interface ovpn-server server"` - `"interface pppoe-client"` - `"interface pptp-server server"` - `"interface sstp-server server"` - `"interface vlan"` - `"interface vrrp"` - `"interface wireless align"` - `"interface wireless cap"` - `"interface wireless sniffer"` - `"interface wireless snooper"` - `"ip accounting"` - `"ip accounting web-access"` - `"ip address"` - `"ip cloud"` - `"ip cloud advanced"` - `"ip dhcp-client"` - `"ip dhcp-client option"` - `"ip dhcp-server"` - `"ip dhcp-server config"` - `"ip dhcp-server lease"` - `"ip dhcp-server network"` - `"ip dns"` - `"ip dns static"` - `"ip firewall address-list"` - `"ip firewall connection tracking"` - `"ip firewall filter"` - `"ip firewall mangle"` - `"ip firewall nat"` - `"ip firewall service-port"` - `"ip hotspot service-port"` - `"ip ipsec identity"` - `"ip ipsec peer"` - `"ip ipsec policy"` - `"ip ipsec profile"` - `"ip ipsec proposal"` - `"ip ipsec settings"` - `"ip neighbor discovery-settings"` - `"ip pool"` - `"ip proxy"` - `"ip route"` - `"ip route vrf"` - `"ip service"` - `"ip settings"` - `"ip smb"` - `"ip socks"` - `"ip ssh"` - `"ip tftp settings"` - `"ip traffic-flow"` - `"ip traffic-flow ipfix"` - `"ip upnp"` - `"ipv6 address"` - `"ipv6 dhcp-client"` - `"ipv6 dhcp-server"` - `"ipv6 dhcp-server option"` - `"ipv6 firewall address-list"` - `"ipv6 firewall filter"` - `"ipv6 firewall mangle"` - `"ipv6 nd"` - `"ipv6 nd prefix default"` - `"ipv6 route"` - `"ipv6 settings"` - `"mpls"` - `"mpls ldp"` - `"port firmware"` - `"ppp aaa"` - `"queue interface"` - `"queue tree"` - `"radius incoming"` - `"routing bgp instance"` - `"routing mme"` - `"routing ospf area"` - `"routing ospf area range"` - `"routing ospf instance"` - `"routing ospf interface-template"` - `"routing pimsm instance"` - `"routing pimsm interface-template"` - `"routing rip"` - `"routing ripng"` - `"snmp"` - `"system clock"` - `"system clock manual"` - `"system identity"` - `"system leds settings"` - `"system logging"` - `"system logging action"` - `"system note"` - `"system ntp client"` - `"system ntp client servers"` - `"system ntp server"` - `"system package update"` - `"system routerboard settings"` - `"system scheduler"` - `"system script"` - `"system upgrade mirror"` - `"system ups"` - `"system watchdog"` - `"tool bandwidth-server"` - `"tool e-mail"` - `"tool graphing"` - `"tool mac-server"` - `"tool mac-server mac-winbox"` - `"tool mac-server ping"` - `"tool romon"` - `"tool sms"` - `"tool sniffer"` - `"tool traffic-generator"` - `"user aaa"` - `"user group"` |
| **port**  integer | RouterOS api port. If *tls* is set, port will apply to TLS/SSL connection.  Defaults are `8728` for the HTTP API, and `8729` for the HTTPS API. |
| **timeout**  integer  added in community.routeros 2.3.0 | Timeout for the request.  Default: `10` |
| **tls**  aliases: ssl  boolean | If is set TLS will be used for RouterOS API connection.  Choices:   - `false` ← (default) - `true` |
| **unfiltered**  boolean | Whether to output all fields, and not just the ones supported as input for [community.routeros.api_modify](api_modify_module.md#ansible-collections-community-routeros-api-modify-module).  Unfiltered output can contain counters and other state information.  Choices:   - `false` ← (default) - `true` |
| **username**  string / required | RouterOS login user. |
| **validate_cert_hostname**  boolean  added in community.routeros 1.2.0 | Set to `true` to validate hostnames in certificates.  See also *validate_certs*. Only used when *tls=true* and *validate_certs=true*.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean  added in community.routeros 1.2.0 | Set to `false` to skip validation of TLS certificates.  See also *validate_cert_hostname*. Only used when *tls=true*.  **Note:** instead of simply deactivating certificate validations to “make things work”, please consider creating your own CA certificate and using it to sign certificates used for your router. You can tell the module about your CA certificate with the *ca_path* option.  Choices:   - `false` - `true` ← (default) |

## [Attributes](api_info_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | Action group: community.routeros.api | Use `group/community.routeros.api` in `module_defaults` to set defaults for this module. |
| **check_mode** | Support: full  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support:  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |
| **platform** | Platform: RouterOS | Target OS/families that can be operated against. |

## [See Also](api_info_module.md#id5)

> **See also:**
>
> [community.routeros.api](api_module.md#ansible-collections-community-routeros-api-module)
> :   Ansible module for RouterOS API.
>
> [community.routeros.api_facts](api_facts_module.md#ansible-collections-community-routeros-api-facts-module)
> :   Collect facts from remote devices running MikroTik RouterOS using the API.
>
> [community.routeros.api_find_and_modify](api_find_and_modify_module.md#ansible-collections-community-routeros-api-find-and-modify-module)
> :   Find and modify information using the API.
>
> [community.routeros.api_modify](api_modify_module.md#ansible-collections-community-routeros-api-modify-module)
> :   Modify data at paths with API.
>
> [How to connect to RouterOS devices with the RouterOS API](docsite/api-guide.md#ansible-collections-community-routeros-docsite-api-guide)
> :   How to connect to RouterOS devices with the RouterOS API

## [Examples](api_info_module.md#id6)

```yaml+jinja
---
- name: Get IP addresses
  community.routeros.api_info:
    hostname: "{{ hostname }}"
    password: "{{ password }}"
    username: "{{ username }}"
    path: ip address
  register: ip_addresses

- name: Print data for IP addresses
  ansible.builtin.debug:
    var: ip_addresses.result
```

## [Return Values](api_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  list / elements=dictionary | A list of all elements for the current path.  Returned: always  Sample: `[{".id": "*1", "actual-interface": "bridge", "address": "192.168.88.1/24", "comment": "defconf", "disabled": false, "dynamic": false, "interface": "bridge", "invalid": false, "network": "192.168.88.0"}]` |

### Authors

- Felix Fontein (@felixfontein)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.routeros/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.routeros)
[Submit a bug report](https://github.com/ansible-collections/community.routeros/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.routeros/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-routeros)
