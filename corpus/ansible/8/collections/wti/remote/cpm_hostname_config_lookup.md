---
collection: ansible
version: "8"
title: "wti.remote.cpm_hostname_config lookup – Set Hostname (Site ID), Location, Asset Tag parameters in WTI OOB and PDU devices."
source_url: https://docs.ansible.com/projects/ansible/8/collections/wti/remote/cpm_hostname_config_lookup.html
fetched_at: 2026-07-28T02:59:57+00:00
---
# wti.remote.cpm_hostname_config lookup – Set Hostname (Site ID), Location, Asset Tag parameters in WTI OOB and PDU devices.

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
> To use it in a playbook, specify: `wti.remote.cpm_hostname_config`.

New in wti.remote 2.11.0

- [Synopsis](cpm_hostname_config_lookup.md#synopsis)
- [Keyword parameters](cpm_hostname_config_lookup.md#keyword-parameters)
- [Notes](cpm_hostname_config_lookup.md#notes)
- [Examples](cpm_hostname_config_lookup.md#examples)
- [Return Value](cpm_hostname_config_lookup.md#return-value)

## [Synopsis](cpm_hostname_config_lookup.md#id1)

- Set Hostname (Site ID), Location, Asset Tag parameters parameters in WTI OOB and PDU devices

## [Keyword parameters](cpm_hostname_config_lookup.md#id2)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('wti.remote.cpm_hostname_config', key1=value1, key2=value2, ...)` and `query('wti.remote.cpm_hostname_config', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **assettag**  string | This is the Asset Tag to be set for the WTI OOB and PDU device. |
| **cpm_password**  string / required | This is the Password of the WTI device to send the module. |
| **cpm_url**  string / required | This is the URL of the WTI device to send the module. |
| **cpm_username**  string / required | This is the Username of the WTI device to send the module. |
| **hostname**  string | This is the Hostname (Site-ID) tag to be set for the WTI OOB and PDU device. |
| **location**  string | This is the Location tag to be set for the WTI OOB and PDU device. |
| **use_https**  boolean | Designates to use an https connection or http connection.  **Choices:**   - `false` - `true` ← (default) |
| **use_proxy**  boolean | Flag to control if the lookup will observe HTTP proxy environment variables when present.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | If false, SSL certificates will not be validated. This should only be used  on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](cpm_hostname_config_lookup.md#id3)

> **Note:**
>
> - Use `groups/cpm` in `module_defaults` to set common options used between CPM modules.

## [Examples](cpm_hostname_config_lookup.md#id4)

```yaml+jinja
# Set Hostname, Location and Site-ID variables of a WTI device
- name: Set known fixed hostname variables of a WTI device
  cpm_time_config:
    cpm_url: "nonexist.wti.com"
    cpm_username: "super"
    cpm_password: "super"
    use_https: true
    validate_certs: false
    hostname: "myhostname"
    location: "Irvine"
    assettag: "irvine92395"

# Set the Hostname variable of a WTI device
- name: Set the Hostname of a WTI device
  cpm_time_config:
    cpm_url: "nonexist.wti.com"
    cpm_username: "super"
    cpm_password: "super"
    use_https: true
    validate_certs: false
    hostname: "myhostname"
```

## [Return Value](cpm_hostname_config_lookup.md#id5)

| Key | Description |
| --- | --- |
| **data**  complex | The output JSON returned from the commands sent  **Returned:** always |
| **assettag**  integer | Current Asset Tag of the WTI device after module execution.  **Returned:** success  **Sample:** `"irvine92395"` |
| **hostname**  string | Current Hostname (Site-ID) of the WTI device after module execution.  **Returned:** success  **Sample:** `"myhostname"` |
| **location**  integer | Current Location of the WTI device after module execution.  **Returned:** success  **Sample:** `"Irvine"` |
| **timestamp**  string | Current timestamp of the WTI device after module execution.  **Returned:** success  **Sample:** `"2021-08-17T21:33:50+00:00"` |

### Authors

- Western Telematic Inc. (@wtinetworkgear)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/wtinetworkgear/wti-collection/issues)
- [Homepage](https://www.wti.com)
- [Repository (Sources)](https://github.com/wtinetworkgear/wti-collection)
