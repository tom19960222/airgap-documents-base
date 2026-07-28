---
collection: ansible
version: "8"
title: "wti.remote.cpm_snmp_config module – Set network IPTables parameters in WTI OOB and PDU devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/wti/remote/cpm_snmp_config_module.html
fetched_at: 2026-07-28T02:59:44+00:00
---
# wti.remote.cpm_snmp_config module – Set network IPTables parameters in WTI OOB and PDU devices

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
> To use it in a playbook, specify: `wti.remote.cpm_snmp_config`.

New in wti.remote 2.10.0

- [Synopsis](cpm_snmp_config_module.md#synopsis)
- [Parameters](cpm_snmp_config_module.md#parameters)
- [Notes](cpm_snmp_config_module.md#notes)
- [Examples](cpm_snmp_config_module.md#examples)
- [Return Values](cpm_snmp_config_module.md#return-values)

## [Synopsis](cpm_snmp_config_module.md#id1)

- Set network IPTables parameters in WTI OOB and PDU devices

## [Parameters](cpm_snmp_config_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **authpass**  list / elements=string | Sets the Authentication Password for SNMPv3 (V3 only). |
| **authpriv**  list / elements=integer | Configures the Authentication and Privacy features for SNMPv3 communication, 0 = Auth/NoPriv, 1 = Auth/Priv (V3 only). |
| **authproto**  list / elements=integer | Which authentication protocol will be used, 0 = MD5, 1 = SHA1 (V3 only). |
| **clear**  integer | Removes all the users for the protocol being defined before setting the newly defined entries.  **Choices:**   - `0` - `1` |
| **contact**  string | The name of the administrator responsible for SNMP issues. |
| **cpm_password**  string / required | This is the Password of the WTI device to send the module. |
| **cpm_url**  string / required | This is the URL of the WTI device to send the module. |
| **cpm_username**  string / required | This is the Username of the WTI device to send the module. |
| **enable**  integer | The activates SNMP polling for the specified interface and protocol.  **Choices:**   - `0` - `1` |
| **index**  list / elements=integer | Index of the user being modified (V3 only). |
| **interface**  string / required | The ethernet port for the SNMP we are defining.  **Choices:**   - `"eth0"` - `"eth1"` - `"ppp0"` - `"qmimux0"` |
| **location**  string | The location of the SNMP Server. |
| **privpass**  list / elements=string | Sets the Privacy Password for SNMPv3 (V3 only) (V3 only). |
| **privproto**  list / elements=integer | Which privacy protocol will be used, 0 = DES, 1 = AES128 (V3 only). |
| **protocol**  integer | The protocol that the SNMP entry should be applied. 0 = ipv4, 1 = ipv6.  **Choices:**   - `0` - `1` |
| **readonly**  integer | Controls the ability to change configuration parameters with SNMP.  **Choices:**   - `0` - `1` |
| **rocommunity**  string | Read Only Community Password, not used for SNMP V3. |
| **rwcommunity**  string | Read/Write Community Password, not used for SNMP V3. |
| **systemname**  string | The hostname of the WTI Device. |
| **use_https**  boolean | Designates to use an https connection or http connection.  **Choices:**   - `false` - `true` ← (default) |
| **use_proxy**  boolean | Flag to control if the lookup will observe HTTP proxy environment variables when present.  **Choices:**   - `false` ← (default) - `true` |
| **username**  list / elements=string | Sets the User Name for SNMPv3 access (V3 only). |
| **validate_certs**  boolean | If false, SSL certificates will not be validated. This should only be used  on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **version**  integer | Defined which version of SNMP the device will respond to 0 = V1/V2 Only, 1 = V3 Only, 2 = V1/V2/V3.  **Choices:**   - `0` - `1` - `2` |

## [Notes](cpm_snmp_config_module.md#id3)

> **Note:**
>
> - Use `groups/cpm` in `module_defaults` to set common options used between CPM modules.

## [Examples](cpm_snmp_config_module.md#id4)

```yaml+jinja
# Sets the device SNMP Parameters
- name: Set the an SNMP Parameter for a WTI device
  cpm_iptables_config:
    cpm_url: "nonexist.wti.com"
    cpm_username: "super"
    cpm_password: "super"
    interface: "eth0"
    use_https: true
    validate_certs: false
    protocol: 0
    clear: 1
    enable: 1
    readonly: 0
    version: 0
    rocommunity: "ropassword"
    rwcommunity: "rwpassword"

# Sets the device SNMP Parameters
- name: Set the SNMP Parameters a WTI device
  cpm_iptables_config:
    cpm_url: "nonexist.wti.com"
    cpm_username: "super"
    cpm_password: "super"
    use_https: true
    validate_certs: false
    version: 1
    index:
      - 1
      - 2
    username:
      - "username1"
      - "username2"
    authpriv:
      - 1
      - 1
    authpass:
      - "authpass1"
      - "uthpass2"
    authproto:
      - 1
      - 1
    privpass:
      - "authpass1"
      - "uthpass2"
    privproto:
      - 1
      - 1
```

## [Return Values](cpm_snmp_config_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | The output JSON returned from the commands sent  **Returned:** always |
| **snmpaccess**  dictionary | Current k/v pairs of interface info for the WTI device after module execution.  **Returned:** always  **Sample:** `[{"eth0": {"ietf-ipv4": {"clear": 1, "enable": 0, "readonly": 0, "users": [{"authpass": "testpass", "authpriv": "1", "authproto": "0", "index": "1", "privpass": "privpass1", "privproto": "0", "username": "username1"}], "version": 0}}}]` |

### Authors

- Western Telematic Inc. (@wtinetworkgear)

### Collection links

- [Issue Tracker](https://github.com/wtinetworkgear/wti-collection/issues)
- [Homepage](https://www.wti.com)
- [Repository (Sources)](https://github.com/wtinetworkgear/wti-collection)
