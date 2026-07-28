---
collection: ansible
version: "6"
title: "wti.remote.cpm_iptables_config module – Set network IPTables parameters in WTI OOB and PDU devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/wti/remote/cpm_iptables_config_module.html
fetched_at: 2026-07-28T00:23:44+00:00
---
# wti.remote.cpm_iptables_config module – Set network IPTables parameters in WTI OOB and PDU devices

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
> To use it in a playbook, specify: `wti.remote.cpm_iptables_config`.

New in wti.remote 2.10.0

- [Synopsis](cpm_iptables_config_module.md#synopsis)
- [Parameters](cpm_iptables_config_module.md#parameters)
- [Notes](cpm_iptables_config_module.md#notes)
- [Examples](cpm_iptables_config_module.md#examples)
- [Return Values](cpm_iptables_config_module.md#return-values)

## [Synopsis](cpm_iptables_config_module.md#id1)

- Set network IPTables parameters in WTI OOB and PDU devices

## [Parameters](cpm_iptables_config_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **clear**  integer | Removes all the iptables for the protocol being defined before setting the newly defined entry.  Choices:   - `0` - `1` |
| **command**  list / elements=string / required | Actual iptables command to send to the WTI device. |
| **cpm_password**  string / required | This is the Password of the WTI device to send the module. |
| **cpm_url**  string / required | This is the URL of the WTI device to send the module. |
| **cpm_username**  string / required | This is the Username of the WTI device to send the module. |
| **index**  list / elements=integer | Index in which command should be inserted. If not defined entry will start at position one. |
| **protocol**  integer | The protocol that the iptables entry should be applied. 0 = ipv4, 1 = ipv6.  Choices:   - `0` - `1` |
| **use_https**  boolean | Designates to use an https connection or http connection.  Choices:   - `false` - `true` ← (default) |
| **use_proxy**  boolean | Flag to control if the lookup will observe HTTP proxy environment variables when present.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | If false, SSL certificates will not be validated. This should only be used  on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](cpm_iptables_config_module.md#id3)

> **Note:**
>
> - Use `groups/cpm` in `module_defaults` to set common options used between CPM modules.

## [Examples](cpm_iptables_config_module.md#id4)

```yaml+jinja
# Set Network IPTables Parameters
- name: Set the an IPTables Parameter for a WTI device
  cpm_iptables_config:
    cpm_url: "nonexist.wti.com"
    cpm_username: "super"
    cpm_password: "super"
    use_https: true
    validate_certs: false
    command: "iptables -A INPUT -p tcp -m state --state NEW -m tcp --dport 443 -j ACCEPT"

# Sets multiple Network IPTables Parameters
- name: Set the IPTables Parameters a WTI device
  cpm_iptables_config:
    cpm_url: "nonexist.wti.com"
    cpm_username: "super"
    cpm_password: "super"
    use_https: true
    validate_certs: false
    index:
      - 1
      - 2
    command:
      - "iptables -A INPUT -p tcp -m state --state NEW -m tcp --dport 443 -j ACCEPT"
      - "iptables -A INPUT -p tcp -m state --state NEW -m tcp --dport 22 -j ACCEPT"
```

## [Return Values](cpm_iptables_config_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | The output JSON returned from the commands sent  Returned: always |
| **iptables**  dictionary | Current k/v pairs of interface info for the WTI device after module execution.  Returned: always  Sample: `[{"eth0": {"ietf-ipv4": {"clear": 1, "entries": [{"entry": "iptables -A INPUT -p tcp -m state --state NEW -m tcp --dport 443 -j ACCEPT", "index": "1"}, {"entry": "iptables -A INPUT -p tcp -m state --state NEW -m tcp --dport 22 -j ACCEPT", "index": "2"}]}}}]` |

### Authors

- Western Telematic Inc. (@wtinetworkgear)

### Collection links

[Issue Tracker](https://github.com/wtinetworkgear/wti-collection/issues)
[Homepage](https://www.wti.com)
[Repository (Sources)](https://github.com/wtinetworkgear/wti-collection)
