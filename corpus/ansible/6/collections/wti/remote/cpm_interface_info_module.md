---
collection: ansible
version: "6"
title: "wti.remote.cpm_interface_info module – Get network interface parameters from WTI OOB and PDU devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/wti/remote/cpm_interface_info_module.html
fetched_at: 2026-07-28T00:23:43+00:00
---
# wti.remote.cpm_interface_info module – Get network interface parameters from WTI OOB and PDU devices

> **Note:**
>
> This module is part of the [wti.remote collection](https://galaxy.ansible.com/wti/remote) (version 1.0.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install wti.remote`.
>
> To use it in a playbook, specify: `wti.remote.cpm_interface_info`.

New in wti.remote 2.10.0

- [Synopsis](cpm_interface_info_module.md#synopsis)
- [Parameters](cpm_interface_info_module.md#parameters)
- [Notes](cpm_interface_info_module.md#notes)
- [Examples](cpm_interface_info_module.md#examples)
- [Return Values](cpm_interface_info_module.md#return-values)

## [Synopsis](cpm_interface_info_module.md#id1)

- Get network interface parameters from WTI OOB and PDU devices

## [Parameters](cpm_interface_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cpm_password**  string / required | This is the Password of the WTI device to send the module. |
| **cpm_url**  string / required | This is the URL of the WTI device to send the module. |
| **cpm_username**  string / required | This is the Username of the WTI device to send the module. |
| **face**  list / elements=any | This is the ethernet port name that is getting retrieved. It can include a single ethernet  port name, multiple ethernet port names separated by commas or not defined for all ports. |
| **interface**  list / elements=string | This is the ethernet port name that is getting retrieved. It can include a single ethernet  port name, multiple ethernet port names separated by commas or not defined for all ports.  Choices:   - `"eth0"` - `"eth1"` - `"ppp0"` - `"qmimux0"` |
| **use_https**  boolean | Designates to use an https connection or http connection.  Choices:   - `false` - `true` ← (default) |
| **use_proxy**  boolean | Flag to control if the lookup will observe HTTP proxy environment variables when present.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | If false, SSL certificates will not be validated. This should only be used  on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](cpm_interface_info_module.md#id3)

> **Note:**
>
> - Use `groups/cpm` in `module_defaults` to set common options used between CPM modules.)

## [Examples](cpm_interface_info_module.md#id4)

```yaml+jinja
- name: Get the network interface Parameters for a WTI device for all interfaces
  cpm_interface_info:
    cpm_url: "nonexist.wti.com"
    cpm_username: "super"
    cpm_password: "super"
    use_https: true
    validate_certs: false

- name: Get the network interface Parameters for a WTI device for a specific interface
  cpm_interface_info:
    cpm_url: "nonexist.wti.com"
    cpm_username: "super"
    cpm_password: "super"
    interface: "eth0,eth1"
    use_https: false
    validate_certs: false
```

## [Return Values](cpm_interface_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | The output JSON returned from the commands sent  Returned: always |
| **interface**  dictionary | Current k/v pairs of interface info for the WTI device after module execution.  Returned: always  Sample: `{"ietf-ipv4": {"address": [{"gateway": "", "ip": "10.10.10.2", "netmask": "255.255.255.0"}], "dhcpclient": [{"enable": 0, "hostname": "", "lease": -1, "obdns": 1, "updns": 1}]}, "ietf-ipv6": {"address": [{"gateway": "", "ip": "", "netmask": ""}]}, "is_gig": "1", "is_up": "0", "mac_address": "00-09-9b-02-45-db", "name": "eth1", "negotiation": "0", "speed": "10", "type": "0"}` |
| **totalports**  integer | Total ethernet ports requested of the WTI device.  Returned: success  Sample: `1` |

### Authors

- Western Telematic Inc. (@wtinetworkgear)

### Collection links

[Issue Tracker](https://github.com/wtinetworkgear/wti-collection/issues)
[Homepage](https://www.wti.com)
[Repository (Sources)](https://github.com/wtinetworkgear/wti-collection)
