---
collection: ansible
version: "6"
title: "wti.remote.cpm_serial_port_action_info lookup – Get Serial port connection status in WTI OOB and PDU devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/wti/remote/cpm_serial_port_action_info_lookup.html
fetched_at: 2026-07-28T00:24:11+00:00
---
# wti.remote.cpm_serial_port_action_info lookup – Get Serial port connection status in WTI OOB and PDU devices

> **Note:**
>
> This lookup plugin is part of the [wti.remote collection](https://galaxy.ansible.com/wti/remote) (version 1.0.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install wti.remote`.
>
> To use it in a playbook, specify: `wti.remote.cpm_serial_port_action_info`.

New in wti.remote 2.9.0

- [Synopsis](cpm_serial_port_action_info_lookup.md#synopsis)
- [Keyword parameters](cpm_serial_port_action_info_lookup.md#keyword-parameters)
- [Notes](cpm_serial_port_action_info_lookup.md#notes)
- [Examples](cpm_serial_port_action_info_lookup.md#examples)
- [Return Value](cpm_serial_port_action_info_lookup.md#return-value)

## [Synopsis](cpm_serial_port_action_info_lookup.md#id1)

- Get Serial port connection status from WTI OOB and PDU devices

## [Keyword parameters](cpm_serial_port_action_info_lookup.md#id2)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('wti.remote.cpm_serial_port_action_info', key1=value1, key2=value2, ...)` and `query('wti.remote.cpm_serial_port_action_info', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **cpm_password**  string / required | This is the Password of the WTI device to send the module. |
| **cpm_url**  string / required | This is the URL of the WTI device to send the module. |
| **cpm_username**  string / required | This is the Username of the WTI device to send the module. |
| **port**  list / elements=any | This is the serial port number that is getting retrieved. It can include a single port  number, multiple port numbers separated by commas, a list of port numbers, or an ‘\*’ character for all ports.  Default: `["*"]` |
| **use_https**  boolean | Designates to use an https connection or http connection.  Choices:   - `false` ← (default) - `true` |
| **use_proxy**  boolean | Flag to control if the lookup will observe HTTP proxy environment variables when present.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | If false, SSL certificates will not be validated. This should only be used  on personally controlled sites using self-signed certificates.  Choices:   - `false` ← (default) - `true` |

## [Notes](cpm_serial_port_action_info_lookup.md#id3)

> **Note:**
>
> - Use `groups/cpm` in `module_defaults` to set common options used between CPM modules.)

## [Examples](cpm_serial_port_action_info_lookup.md#id4)

```yaml+jinja
- name: Get the Serial Port Parameters for port 2 of a WTI device
  cpm_serial_port_action_info:
    cpm_url: "nonexist.wti.com"
    cpm_username: "super"
    cpm_password: "super"
    use_https: true
    validate_certs: false
    port: 2

- name: Get the Serial Port Parameters for ports 2 and 4 of a WTI device
  cpm_serial_port_action_info:
    cpm_url: "nonexist.wti.com"
    cpm_username: "super"
    cpm_password: "super"
    use_https: true
    validate_certs: false
    port: 2,4

- name: Get the Serial Port Parameters for all ports of a WTI device
  cpm_serial_port_info:
    cpm_url: "nonexist.wti.com"
    cpm_username: "super"
    cpm_password: "super"
    use_https: true
    validate_certs: false
    port: "*"
```

## [Return Value](cpm_serial_port_action_info_lookup.md#id5)

| Key | Description |
| --- | --- |
| **data**  complex | The output JSON returned from the commands sent  Returned: always |
| **ports**  list / elements=string | List of connection status for each serial port  Returned: success  Sample: `[{"connstatus": "Free", "port": 2}, {"connstatus": " C-06", "port": 4}]` |

### Authors

- Western Telematic Inc. (@wtinetworkgear)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/wtinetworkgear/wti-collection/issues)
[Homepage](https://www.wti.com)
[Repository (Sources)](https://github.com/wtinetworkgear/wti-collection)
