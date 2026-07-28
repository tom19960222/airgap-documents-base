---
collection: ansible
version: "6"
title: "wti.remote.cpm_syslog_server_config lookup – Set network SYSLOG Server parameters in WTI OOB and PDU devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/wti/remote/cpm_syslog_server_config_lookup.html
fetched_at: 2026-07-28T00:24:18+00:00
---
# wti.remote.cpm_syslog_server_config lookup – Set network SYSLOG Server parameters in WTI OOB and PDU devices

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
> To use it in a playbook, specify: `wti.remote.cpm_syslog_server_config`.

New in wti.remote 2.11.0

- [Synopsis](cpm_syslog_server_config_lookup.md#synopsis)
- [Keyword parameters](cpm_syslog_server_config_lookup.md#keyword-parameters)
- [Notes](cpm_syslog_server_config_lookup.md#notes)
- [Examples](cpm_syslog_server_config_lookup.md#examples)
- [Return Value](cpm_syslog_server_config_lookup.md#return-value)

## [Synopsis](cpm_syslog_server_config_lookup.md#id1)

- Set network SYSLOG Server parameters in WTI OOB and PDU devices

## [Keyword parameters](cpm_syslog_server_config_lookup.md#id2)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('wti.remote.cpm_syslog_server_config', key1=value1, key2=value2, ...)` and `query('wti.remote.cpm_syslog_server_config', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **address**  list / elements=any | Sets the IP Address to block message logging. |
| **clear**  integer | Removes all the IP block entries for the protocol being defined before setting the newly defined entries.  Choices:   - `0` - `1` |
| **cpm_password**  string / required | This is the Password of the WTI device to send the module. |
| **cpm_url**  string / required | This is the URL of the WTI device to send the module. |
| **cpm_username**  string / required | This is the Username of the WTI device to send the module. |
| **enable**  integer | Activates SYSLOG listening for the specified interface and protocol.  Choices:   - `0` - `1` |
| **index**  list / elements=any | Index of the IP block being modified. |
| **interface**  string / required | The ethernet port for the SYSLOG we are defining.  Choices:   - `"eth0"` - `"eth1"` - `"ppp0"` - `"qmimux0"` |
| **port**  integer | Defines the port number used by the SYSLOG Server (1 - 65535). |
| **protocol**  integer | The protocol that the SYSLOG entry should be applied. 0 = ipv4, 1 = ipv6.  Choices:   - `0` - `1` |
| **secure**  integer | Defines if a secure connection is used by the SYSLOG Server (TCP Transport required).  Choices:   - `0` - `1` |
| **transport**  integer | Defines the transfer protocol type used by the SYSLOG Server. 0=UDP, 1=TCP;  Choices:   - `0` - `1` |
| **use_https**  boolean | Designates to use an https connection or http connection.  Choices:   - `false` - `true` ← (default) |
| **use_proxy**  boolean | Flag to control if the lookup will observe HTTP proxy environment variables when present.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | If false, SSL certificates will not be validated. This should only be used  on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](cpm_syslog_server_config_lookup.md#id3)

> **Note:**
>
> - Use `groups/cpm` in `module_defaults` to set common options used between CPM modules.

## [Examples](cpm_syslog_server_config_lookup.md#id4)

```yaml+jinja
# Sets the device SYSLOG Server Parameters
- name: Set the an SYSLOG Server Parameter for a WTI device
  cpm_iptables_config:
    cpm_url: "nonexist.wti.com"
    cpm_username: "super"
    cpm_password: "super"
    use_https: true
    validate_certs: false
    interface: "eth0"
    protocol: 0
    port: 514
    transport: 0
    secure: 0
    clear: 1

# Sets the device SYSLOG Server Parameters
- name: Set the SYSLOG Server Parameters a WTI device
  cpm_iptables_config:
    cpm_url: "nonexist.wti.com"
    cpm_username: "super"
    cpm_password: "super"
    use_https: true
    validate_certs: false
    interface: "eth0"
    protocol: 0
    port: 514
    transport: 0
    secure: 0
    clear: 1
    index:
      - 1
      - 2
    block:
      - "192.168.50.4"
      - "72.76.4.56"
```

## [Return Value](cpm_syslog_server_config_lookup.md#id5)

| Key | Description |
| --- | --- |
| **data**  complex | The output JSON returned from the commands sent  Returned: always |
| **syslogserver**  dictionary | Current k/v pairs of interface info for the WTI device after module execution.  Returned: always  Sample: `{"syslogserver": {"eth0": [{"ietf-ipv4": {"block": [{"address": "", "index": "1"}, {"address": "", "index": "2"}, {"address": "", "index": "3"}, {"address": "", "index": "4"}], "enable": 0, "port": "514", "secure": "0", "transport": "0"}, "ietf-ipv6": {"block": [{"address": "", "index": "1"}, {"address": "", "index": "2"}, {"address": "", "index": "3"}, {"address": "", "index": "4"}], "enable": 0, "port": "514", "secure": "0", "transport": "0"}}]}}` |

### Authors

- Western Telematic Inc. (@wtinetworkgear)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/wtinetworkgear/wti-collection/issues)
[Homepage](https://www.wti.com)
[Repository (Sources)](https://github.com/wtinetworkgear/wti-collection)
