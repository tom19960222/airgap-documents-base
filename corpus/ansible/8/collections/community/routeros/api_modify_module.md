---
collection: ansible
version: "8"
title: "community.routeros.api_modify module – Modify data at paths with API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/routeros/api_modify_module.html
fetched_at: 2026-07-28T01:59:02+00:00
---
# community.routeros.api_modify module – Modify data at paths with API

> **Note:**
>
> This module is part of the [community.routeros collection](https://galaxy.ansible.com/ui/repo/published/community/routeros/) (version 2.11.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.routeros`.
> You need further requirements to be able to use this module,
> see [Requirements](api_modify_module.md#ansible-collections-community-routeros-api-modify-module-requirements) for details.
>
> To use it in a playbook, specify: `community.routeros.api_modify`.

New in community.routeros 2.2.0

- [Synopsis](api_modify_module.md#synopsis)
- [Requirements](api_modify_module.md#requirements)
- [Parameters](api_modify_module.md#parameters)
- [Attributes](api_modify_module.md#attributes)
- [Notes](api_modify_module.md#notes)
- [See Also](api_modify_module.md#see-also)
- [Examples](api_modify_module.md#examples)
- [Return Values](api_modify_module.md#return-values)

## [Synopsis](api_modify_module.md#id1)

- Allows to modify information for a path using the API.
- Use the [community.routeros.api_find_and_modify](api_find_and_modify_module.md#ansible-collections-community-routeros-api-find-and-modify-module) module to modify one or multiple entries in a controlled way depending on some search conditions.
- To make a backup of a path that can be restored with this module, use the [community.routeros.api_info](api_info_module.md#ansible-collections-community-routeros-api-info-module) module.
- The module ignores dynamic and builtin entries.
- **Note** that this module is still heavily in development, and only supports **some** paths. If you want to support new paths, or think you found problems with existing paths, please first [create an issue in the community.routeros Issue Tracker](https://github.com/ansible-collections/community.routeros/issues/).

## [Requirements](api_modify_module.md#id2)

The below requirements are needed on the host that executes this module.

- Needs [ordereddict](https://pypi.org/project/ordereddict) for Python 2.6
- Python >= 3.6 (for librouteros)
- librouteros

## [Parameters](api_modify_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  *added in community.routeros 1.2.0* | PEM formatted file that contains a CA certificate to be used for certificate validation.  See also `validate_cert_hostname`. Only used when `tls=true` and `validate_certs=true`. |
| **data**  list / elements=dictionary / required | Data to ensure that is present for this path.  Fields not provided will not be modified.  If `.id` appears in an entry, it will be ignored. |
| **encoding**  string  *added in community.routeros 2.1.0* | Use the specified encoding when communicating with the RouterOS device.  Default is `ASCII`. Note that `UTF-8` requires librouteros 3.2.1 or newer.  **Default:** `"ASCII"` |
| **ensure_order**  boolean | Whether to ensure the same order of the config as present in `data`.  Requires `handle_absent_entries=remove`.  **Choices:**   - `false` ← (default) - `true` |
| **force_no_cert**  boolean  *added in community.routeros 2.4.0* | Set to `true` to connect without a certificate when `tls=true`.  See also `validate_certs`.  **Note:** this forces the use of anonymous Diffie-Hellman (ADH) ciphers. The protocol is susceptible to Man-in-the-Middle attacks, because the keys used in the exchange are not authenticated. Instead of simply connecting without a certificate to “make things work” have a look at `validate_certs` and `ca_path`.  **Choices:**   - `false` ← (default) - `true` |
| **handle_absent_entries**  string | How to handle entries that are present in the current config, but not in `data`.  `ignore` ignores them.  `remove` removes them.  **Choices:**   - `"ignore"` ← (default) - `"remove"` |
| **handle_entries_content**  string | For a single entry in `data`, this describes how to handle fields that are not mentioned in that entry, but appear in the actual config.  If `ignore`, they are not modified.  If `remove`, they are removed. If at least one cannot be removed, the module will fail.  If `remove_as_much_as_possible`, all that can be removed will be removed. The ones that cannot be removed will be kept.  Note that `remove` and `remove_as_much_as_possible` do not apply to write-only fields.  **Choices:**   - `"ignore"` ← (default) - `"remove"` - `"remove_as_much_as_possible"` |
| **handle_read_only**  string  *added in community.routeros 2.10.0* | How to handle values passed in for read-only fields.  If `ignore`, they are not passed to the API.  If `validate`, the values are not passed for creation, and for updating they are compared to the value returned for the object. If they differ, the module fails.  If `error`, the module will fail if read-only fields are provided.  **Choices:**   - `"ignore"` - `"validate"` - `"error"` ← (default) |
| **handle_write_only**  string  *added in community.routeros 2.10.0* | How to handle values passed in for write-only fields.  If `create_only`, they are passed on creation, and ignored for updating.  If `always_update`, they are always passed to the API. This means that if such a value is present, the module will always result in `changed` since there is no way to validate whether the value actually changed.  If `error`, the module will fail if write-only fields are provided.  **Choices:**   - `"create_only"` ← (default) - `"always_update"` - `"error"` |
| **hostname**  string / required | RouterOS hostname API. |
| **password**  string / required | RouterOS user password. |
| **path**  string / required | Path to query.  An example value is `ip address`. This is equivalent to running modification commands in `/ip address` in the RouterOS CLI.  **Choices:**   - `"caps-man aaa"` - `"caps-man access-list"` - `"caps-man channel"` - `"caps-man configuration"` - `"caps-man datapath"` - `"caps-man manager"` - `"caps-man manager interface"` - `"caps-man provisioning"` - `"caps-man security"` - `"certificate settings"` - `"interface bonding"` - `"interface bridge"` - `"interface bridge mlag"` - `"interface bridge port"` - `"interface bridge port-controller"` - `"interface bridge port-extender"` - `"interface bridge settings"` - `"interface bridge vlan"` - `"interface detect-internet"` - `"interface eoip"` - `"interface ethernet"` - `"interface ethernet poe"` - `"interface ethernet switch"` - `"interface ethernet switch port"` - `"interface gre"` - `"interface gre6"` - `"interface l2tp-server server"` - `"interface list"` - `"interface list member"` - `"interface ovpn-server server"` - `"interface ppp-client"` - `"interface pppoe-client"` - `"interface pptp-server server"` - `"interface sstp-server server"` - `"interface vlan"` - `"interface vrrp"` - `"interface wireguard"` - `"interface wireguard peers"` - `"interface wireless"` - `"interface wireless align"` - `"interface wireless cap"` - `"interface wireless security-profiles"` - `"interface wireless sniffer"` - `"interface wireless snooper"` - `"iot modbus"` - `"ip accounting"` - `"ip accounting web-access"` - `"ip address"` - `"ip arp"` - `"ip cloud"` - `"ip cloud advanced"` - `"ip dhcp-client"` - `"ip dhcp-client option"` - `"ip dhcp-server"` - `"ip dhcp-server config"` - `"ip dhcp-server lease"` - `"ip dhcp-server network"` - `"ip dhcp-server option"` - `"ip dhcp-server option sets"` - `"ip dns"` - `"ip dns static"` - `"ip firewall address-list"` - `"ip firewall connection tracking"` - `"ip firewall filter"` - `"ip firewall layer7-protocol"` - `"ip firewall mangle"` - `"ip firewall nat"` - `"ip firewall raw"` - `"ip firewall service-port"` - `"ip hotspot service-port"` - `"ip ipsec identity"` - `"ip ipsec peer"` - `"ip ipsec policy"` - `"ip ipsec profile"` - `"ip ipsec proposal"` - `"ip ipsec settings"` - `"ip neighbor discovery-settings"` - `"ip pool"` - `"ip proxy"` - `"ip route"` - `"ip route vrf"` - `"ip service"` - `"ip settings"` - `"ip smb"` - `"ip socks"` - `"ip ssh"` - `"ip tftp settings"` - `"ip traffic-flow"` - `"ip traffic-flow ipfix"` - `"ip traffic-flow target"` - `"ip upnp"` - `"ip upnp interfaces"` - `"ipv6 address"` - `"ipv6 dhcp-client"` - `"ipv6 dhcp-server"` - `"ipv6 dhcp-server option"` - `"ipv6 firewall address-list"` - `"ipv6 firewall filter"` - `"ipv6 firewall mangle"` - `"ipv6 firewall nat"` - `"ipv6 firewall raw"` - `"ipv6 nd"` - `"ipv6 nd prefix default"` - `"ipv6 route"` - `"ipv6 settings"` - `"mpls"` - `"mpls ldp"` - `"port firmware"` - `"port remote-access"` - `"ppp aaa"` - `"ppp profile"` - `"queue interface"` - `"queue tree"` - `"radius incoming"` - `"routing bgp connection"` - `"routing bgp instance"` - `"routing filter rule"` - `"routing filter select-rule"` - `"routing id"` - `"routing mme"` - `"routing ospf area"` - `"routing ospf area range"` - `"routing ospf instance"` - `"routing ospf interface-template"` - `"routing pimsm instance"` - `"routing pimsm interface-template"` - `"routing rip"` - `"routing ripng"` - `"routing table"` - `"snmp"` - `"snmp community"` - `"system clock"` - `"system clock manual"` - `"system identity"` - `"system leds settings"` - `"system logging"` - `"system logging action"` - `"system note"` - `"system ntp client"` - `"system ntp client servers"` - `"system ntp server"` - `"system package update"` - `"system routerboard settings"` - `"system scheduler"` - `"system script"` - `"system upgrade mirror"` - `"system ups"` - `"system watchdog"` - `"tool bandwidth-server"` - `"tool e-mail"` - `"tool graphing"` - `"tool graphing interface"` - `"tool graphing resource"` - `"tool mac-server"` - `"tool mac-server mac-winbox"` - `"tool mac-server ping"` - `"tool netwatch"` - `"tool romon"` - `"tool sms"` - `"tool sniffer"` - `"tool traffic-generator"` - `"user"` - `"user aaa"` - `"user group"` - `"user settings"` |
| **port**  integer | RouterOS api port. If `tls` is set, port will apply to TLS/SSL connection.  Defaults are `8728` for the HTTP API, and `8729` for the HTTPS API. |
| **timeout**  integer  *added in community.routeros 2.3.0* | Timeout for the request.  **Default:** `10` |
| **tls**  aliases: ssl  boolean | If is set TLS will be used for RouterOS API connection.  **Choices:**   - `false` ← (default) - `true` |
| **username**  string / required | RouterOS login user. |
| **validate_cert_hostname**  boolean  *added in community.routeros 1.2.0* | Set to `true` to validate hostnames in certificates.  See also `validate_certs`. Only used when `tls=true` and `validate_certs=true`.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean  *added in community.routeros 1.2.0* | Set to `false` to skip validation of TLS certificates.  See also `validate_cert_hostname`. Only used when `tls=true`.  **Note:** instead of simply deactivating certificate validations to “make things work”, please consider creating your own CA certificate and using it to sign certificates used for your router. You can tell the module about your CA certificate with the `ca_path` option.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](api_modify_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | **Action group:** **community.routeros.api** | Use `group/community.routeros.api` in `module_defaults` to set defaults for this module. |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |
| **platform** | **Platform:** **RouterOS** | Target OS/families that can be operated against. |

## [Notes](api_modify_module.md#id5)

> **Note:**
>
> - If write-only fields are present in the path, the module is **not idempotent** in a strict sense, since it is not able to verify the current value of these fields. The behavior the module should assume can be controlled with the `handle_write_only` option.

## [See Also](api_modify_module.md#id6)

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
> [community.routeros.api_info](api_info_module.md#ansible-collections-community-routeros-api-info-module)
> :   Retrieve information from API.
>
> [How to connect to RouterOS devices with the RouterOS API](docsite/api-guide.md#ansible-collections-community-routeros-docsite-api-guide)
> :   How to connect to RouterOS devices with the RouterOS API

## [Examples](api_modify_module.md#id7)

```yaml+jinja
---
- name: Setup DHCP server networks
  # Ensures that we have exactly two DHCP server networks (in the specified order)
  community.routeros.api_modify:
    path: ip dhcp-server network
    handle_absent_entries: remove
    handle_entries_content: remove_as_much_as_possible
    ensure_order: true
    data:
      - address: 192.168.88.0/24
        comment: admin network
        dns-server: 192.168.88.1
        gateway: 192.168.88.1
      - address: 192.168.1.0/24
        comment: customer network 1
        dns-server: 192.168.1.1
        gateway: 192.168.1.1
        netmask: 24

- name: Adjust NAT
  community.routeros.api_modify:
    hostname: "{{ hostname }}"
    password: "{{ password }}"
    username: "{{ username }}"
    path: ip firewall nat
    data:
      - action: masquerade
        chain: srcnat
        comment: NAT to WAN
        out-interface-list: WAN
        # Three ways to unset values:
        #   - nothing after `:`
        #   - "empty" value (null/~/None)
        #   - prepend '!'
        out-interface:
        to-addresses: ~
        '!to-ports':
```

## [Return Values](api_modify_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **new_data**  list / elements=dictionary | A list of all elements for the current path after a change was made.  **Returned:** always  **Sample:** `[{".id": "*1", "actual-interface": "bridge", "address": "192.168.1.1/24", "comment": "awesome", "disabled": false, "dynamic": false, "interface": "bridge", "invalid": false, "network": "192.168.1.0"}]` |
| **old_data**  list / elements=dictionary | A list of all elements for the current path before a change was made.  **Returned:** always  **Sample:** `[{".id": "*1", "actual-interface": "bridge", "address": "192.168.88.1/24", "comment": "defconf", "disabled": false, "dynamic": false, "interface": "bridge", "invalid": false, "network": "192.168.88.0"}]` |

### Authors

- Felix Fontein (@felixfontein)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.routeros/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.routeros)
- [Submit a bug report](https://github.com/ansible-collections/community.routeros/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.routeros/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-routeros)
