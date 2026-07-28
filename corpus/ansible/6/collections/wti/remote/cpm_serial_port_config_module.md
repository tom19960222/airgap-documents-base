---
collection: ansible
version: "6"
title: "wti.remote.cpm_serial_port_config module – Set Serial port parameters in WTI OOB and PDU devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/wti/remote/cpm_serial_port_config_module.html
fetched_at: 2026-07-28T00:23:50+00:00
---
# wti.remote.cpm_serial_port_config module – Set Serial port parameters in WTI OOB and PDU devices

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
> To use it in a playbook, specify: `wti.remote.cpm_serial_port_config`.

New in wti.remote 2.9.0

- [Synopsis](cpm_serial_port_config_module.md#synopsis)
- [Parameters](cpm_serial_port_config_module.md#parameters)
- [Notes](cpm_serial_port_config_module.md#notes)
- [Examples](cpm_serial_port_config_module.md#examples)
- [Return Values](cpm_serial_port_config_module.md#return-values)

## [Synopsis](cpm_serial_port_config_module.md#id1)

- Set Serial port parameters in WTI OOB and PDU devices

## [Parameters](cpm_serial_port_config_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **baud**  integer | This is the baud rate to assign to the port.  0=300, 1=1200, 2=2400, 3=4800, 4=9600, 5=19200, 6=38400, 7=57600, 8=115200, 9=230400, 10=460800  Choices:   - `0` - `1` - `2` - `3` - `4` - `5` - `6` - `7` - `8` - `9` - `10` |
| **break_allow**  boolean | This is if the break character is allowed to be passed through the port, 0=Off, 1=On  Choices:   - `false` - `true` |
| **cmd**  integer | This is the Admin Mode to assign to the port, 0=Deny, 1=Permit.  Choices:   - `0` - `1` |
| **cpm_password**  string / required | This is the Password of the WTI device to send the module. |
| **cpm_url**  string / required | This is the URL of the WTI device to send the module. |
| **cpm_username**  string / required | This is the Username of the WTI device to send the module. |
| **echo**  boolean | -This is the command echo parameter to assign to the port, 0=Off, 1=On  Choices:   - `false` - `true` |
| **handshake**  integer | This is the handshake to assign to the port, 0=None, 1=XON/XOFF, 2=RTS/CTS, 3=Both.  Choices:   - `0` - `1` - `2` - `3` |
| **logoff**  string | This is the logout character to assign to the port  If preceded by a ^ character, the sequence will be a control character. Used if seq is set to 0 or 1 |
| **mode**  integer | This is the port mode to assign to the port, 0=Any-to-Any. 1=Passive, 2=Buffer, 3=Modem, 4=ModemPPP.  Choices:   - `0` - `1` - `2` - `3` - `4` |
| **parity**  integer | This is the parity to assign to the port, 0=7-None, 1=7-Even, 2=7-Odd, 3=8-None, 4=8-Even, 5=8-Odd.  Choices:   - `0` - `1` - `2` - `3` - `4` - `5` |
| **port**  integer / required | This is the port number that is getting the action performed on. |
| **portname**  string | This is the Name of the Port that is displayed. |
| **seq**  integer | This is the type of Sequence Disconnect to assign to the port, 1=Three Characters (before and after), 2=One Character Only, 3=Off  Choices:   - `1` - `2` - `3` |
| **stopbits**  integer | This is the stop bits to assign to the port, 1=1 Stop Bit, 2=2 Stop Bit.  Choices:   - `1` - `2` |
| **tout**  integer | This is the Port Activity Timeout to assign to the port, 0=Off, 1=5 Min, 2=15 Min, 3=30 Min, 4=90 Min, 5=1 Min.  Choices:   - `0` - `1` - `2` - `3` - `4` - `5` |
| **use_https**  boolean | Designates to use an https connection or http connection.  Choices:   - `false` - `true` ← (default) |
| **use_proxy**  boolean | Flag to control if the lookup will observe HTTP proxy environment variables when present.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | If false, SSL certificates will not be validated. This should only be used  on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](cpm_serial_port_config_module.md#id3)

> **Note:**
>
> - Use `groups/cpm` in `module_defaults` to set common options used between CPM modules.

## [Examples](cpm_serial_port_config_module.md#id4)

```yaml+jinja
# Set Serial Port Parameters
- name: Set the Port Parameters for port 2 of a WTI device
  cpm_serial_port_config:
    cpm_url: "nonexist.wti.com"
    cpm_username: "super"
    cpm_password: "super"
    use_https: true
    validate_certs: false
    port: "2"
    portname: "RouterLabel"
    baud: "7"
    handshake: "1"
    stopbits: "1"
    parity: "0"
    mode: "0"
    cmd: "0"
    seq: "1"
    tout: "1"
    echo: "0"
    break_allow: "0"
    logoff: "^H"

# Set Serial Port Port Name and Baud Rate Parameters
- name: Set New port name and baud rate (115k) for port 4 of a WTI device
  cpm_serial_port_config:
    cpm_url: "nonexist.wti.com"
    cpm_username: "super"
    cpm_password: "super"
    use_https: true
    validate_certs: false
    port: "4"
    portname: "NewPortName1"
    baud: "8"
```

## [Return Values](cpm_serial_port_config_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  string | The output JSON returned from the commands sent  Returned: always |

### Authors

- Western Telematic Inc. (@wtinetworkgear)

### Collection links

[Issue Tracker](https://github.com/wtinetworkgear/wti-collection/issues)
[Homepage](https://www.wti.com)
[Repository (Sources)](https://github.com/wtinetworkgear/wti-collection)
