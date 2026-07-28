---
collection: ansible
version: "8"
title: "wti.remote.cpm_serial_port_info module – Get Serial port parameters in WTI OOB and PDU devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/wti/remote/cpm_serial_port_info_module.html
fetched_at: 2026-07-28T02:59:43+00:00
---
# wti.remote.cpm_serial_port_info module – Get Serial port parameters in WTI OOB and PDU devices

> **Note:**
>
> This module is part of the [wti.remote collection](https://galaxy.ansible.com/ui/repo/published/wti/remote/) (version 1.0.5).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install wti.remote`.
>
> To use it in a playbook, specify: `wti.remote.cpm_serial_port_info`.

New in wti.remote 2.9.0

- [Synopsis](cpm_serial_port_info_module.md#synopsis)
- [Parameters](cpm_serial_port_info_module.md#parameters)
- [Notes](cpm_serial_port_info_module.md#notes)
- [Examples](cpm_serial_port_info_module.md#examples)
- [Return Values](cpm_serial_port_info_module.md#return-values)

## [Synopsis](cpm_serial_port_info_module.md#id1)

- Get Serial port parameters from WTI OOB and PDU devices

## [Parameters](cpm_serial_port_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cpm_password**  string / required | This is the Password of the WTI device to send the module. |
| **cpm_url**  string / required | This is the URL of the WTI device to send the module. |
| **cpm_username**  string / required | This is the Username of the WTI device to send the module. |
| **port**  list / elements=string | This is the serial port number that is getting retrieved. It can include a single port  number, multiple port numbers separated by commas, a list of port numbers, or an ‘\*’ character for all ports.  **Default:** `["*"]` |
| **use_https**  boolean | Designates to use an https connection or http connection.  **Choices:**   - `false` ← (default) - `true` |
| **use_proxy**  boolean | Flag to control if the lookup will observe HTTP proxy environment variables when present.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | If false, SSL certificates will not be validated. This should only be used  on personally controlled sites using self-signed certificates.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](cpm_serial_port_info_module.md#id3)

> **Note:**
>
> - Use `groups/cpm` in `module_defaults` to set common options used between CPM modules.)

## [Examples](cpm_serial_port_info_module.md#id4)

```yaml+jinja
- name: Get the Serial Port Parameters for port 2 of a WTI device
  cpm_serial_port_info:
    cpm_url: "nonexist.wti.com"
    cpm_username: "super"
    cpm_password: "super"
    use_https: true
    validate_certs: false
    port: 2

- name: Get the Serial Port Parameters for ports 2 and 4 of a WTI device
  cpm_serial_port_info:
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

## [Return Values](cpm_serial_port_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | The output JSON returned from the commands sent  **Returned:** always |
| **serialports**  list / elements=string | List of data for each serial port  **Returned:** success  **Sample:** `[{"baud": 4, "break": 1, "cmd": 1, "connstatus": "Free", "echo": 1, "handshake": 2, "logoff": "^X", "mode": 1, "parity": 3, "port": 2, "portname": "switch", "seq": 2, "stopbits": 1, "tout": 0}, {"baud": 3, "break": 1, "cmd": 1, "connstatus": "Free", "echo": 1, "handshake": 2, "logoff": "^X", "mode": 1, "parity": 1, "port": 4, "portname": "router", "seq": 2, "stopbits": 1, "tout": 1}]` |

### Authors

- Western Telematic Inc. (@wtinetworkgear)

### Collection links

- [Issue Tracker](https://github.com/wtinetworkgear/wti-collection/issues)
- [Homepage](https://www.wti.com)
- [Repository (Sources)](https://github.com/wtinetworkgear/wti-collection)
