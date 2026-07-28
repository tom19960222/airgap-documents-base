---
collection: ansible
version: "8"
title: "wti.remote.cpm_interface_config lookup – Set network interface parameters in WTI OOB and PDU devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/wti/remote/cpm_interface_config_lookup.html
fetched_at: 2026-07-28T02:59:59+00:00
---
# wti.remote.cpm_interface_config lookup – Set network interface parameters in WTI OOB and PDU devices

> **Note:**
>
> This lookup plugin is part of the [wti.remote collection](https://galaxy.ansible.com/ui/repo/published/wti/remote/) (version 1.0.5).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install wti.remote`.
>
> To use it in a playbook, specify: `wti.remote.cpm_interface_config`.

New in wti.remote 2.10.0

- [Synopsis](cpm_interface_config_lookup.md#synopsis)
- [Keyword parameters](cpm_interface_config_lookup.md#keyword-parameters)
- [Notes](cpm_interface_config_lookup.md#notes)
- [Examples](cpm_interface_config_lookup.md#examples)
- [Return Value](cpm_interface_config_lookup.md#return-value)

## [Synopsis](cpm_interface_config_lookup.md#id1)

- Set network interface parameters in WTI OOB and PDU devices

## [Keyword parameters](cpm_interface_config_lookup.md#id2)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('wti.remote.cpm_interface_config', key1=value1, key2=value2, ...)` and `query('wti.remote.cpm_interface_config', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **cpm_password**  string / required | This is the Password of the WTI device to send the module. |
| **cpm_url**  string / required | This is the URL of the WTI device to send the module. |
| **cpm_username**  string / required | This is the Username of the WTI device to send the module. |
| **interface**  string | This is the ethernet port name that is getting configured.  **Choices:**   - `"eth0"` - `"eth1"` |
| **ipv4address**  string | IPv4 format IP address for the defined interface Port. |
| **ipv4dhcpdefgateway**  integer | Enable or Disable this ports configuration as the default IPv4 route for the device.  **Choices:**   - `0` - `1` |
| **ipv4dhcpenable**  integer | Enable IPv4 DHCP request call to obtain confufuration information.  **Choices:**   - `0` - `1` |
| **ipv4dhcphostname**  string | Define IPv4 DHCP Hostname. |
| **ipv4dhcplease**  integer | IPv4 DHCP Lease Time. |
| **ipv4dhcpobdns**  integer | IPv6 DHCP Obtain DNS addresses auto.  **Choices:**   - `0` - `1` |
| **ipv4dhcpupdns**  integer | IPv4 DHCP DNS Server Update.  **Choices:**   - `0` - `1` |
| **ipv4gateway**  string | IPv4 format Gateway address for the defined interface Port. |
| **ipv4netmask**  string | IPv4 format Netmask for the defined interface Port. |
| **ipv6address**  string | IPv6 format IP address for the defined interface Port. |
| **ipv6gateway**  string | IPv6 format Gateway address for the defined interface Port. |
| **ipv6subnetprefix**  string | IPv6 format Subnet Prefix for the defined interface Port. |
| **negotiation**  integer | This is the speed of the interface port being configured.  0=Auto, 1=10/half, 2=10/full, 3=100/half, 4=100/full, 5=1000/half, 6=1000/full  **Choices:**   - `0` - `1` - `2` - `3` - `4` - `5` - `6` |
| **use_https**  boolean | Designates to use an https connection or http connection.  **Choices:**   - `false` - `true` ← (default) |
| **use_proxy**  boolean | Flag to control if the lookup will observe HTTP proxy environment variables when present.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | If false, SSL certificates will not be validated. This should only be used  on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](cpm_interface_config_lookup.md#id3)

> **Note:**
>
> - Use `groups/cpm` in `module_defaults` to set common options used between CPM modules.

## [Examples](cpm_interface_config_lookup.md#id4)

```yaml+jinja
# Set Network Interface Parameters
- name: Set the Interface Parameters for port eth1 of a WTI device
  cpm_interface_config:
    cpm_url: "nonexist.wti.com"
    cpm_username: "super"
    cpm_password: "super"
    use_https: true
    validate_certs: false
    interface: "eth1"
    ipv4address: "192.168.0.14"
    ipv4netmask: "255.255.255.0"
    ipv4gateway: "192.168.0.1"
    negotiation: 0

# Set Network Interface Parameters
- name: Set the Interface Parameters for port eth1 to DHCP of a WTI device
  cpm_interface_config:
    cpm_url: "nonexist.wti.com"
    cpm_username: "super"
    cpm_password: "super"
    use_https: true
    validate_certs: false
    interface: "eth1"
    negotiation: 0
    ipv4dhcpenable: 1
    ipv4dhcphostname: ""
    ipv4dhcplease: -1
    ipv4dhcpobdns: 0
    ipv4dhcpupdns: 0
    ipv4dhcpdefgateway: 0
```

## [Return Value](cpm_interface_config_lookup.md#id5)

| Key | Description |
| --- | --- |
| **data**  complex | The output JSON returned from the commands sent  **Returned:** always |
| **interface**  dictionary | Current k/v pairs of interface info for the WTI device after module execution.  **Returned:** always  **Sample:** `{"ietf-ipv4": {"address": [{"gateway": "", "ip": "10.10.10.2", "netmask": "255.255.255.0"}], "dhcpclient": [{"enable": 0, "hostname": "", "lease": -1, "obdns": 1, "updns": 1}]}, "ietf-ipv6": {"address": [{"gateway": "", "ip": "", "netmask": ""}]}, "is_gig": "1", "is_up": "0", "mac_address": "00-09-9b-02-45-db", "name": "eth1", "negotiation": "0", "speed": "10", "type": "0"}` |
| **totalports**  integer | Total interface ports requested of the WTI device.  **Returned:** success  **Sample:** `1` |

### Authors

- Western Telematic Inc. (@wtinetworkgear)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/wtinetworkgear/wti-collection/issues)
- [Homepage](https://www.wti.com)
- [Repository (Sources)](https://github.com/wtinetworkgear/wti-collection)
