---
collection: ansible
version: "8"
title: "cisco.ucs.ucs_timezone module – Configures timezone on Cisco UCS Manager"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ucs/ucs_timezone_module.html
fetched_at: 2026-07-28T01:39:44+00:00
---
# cisco.ucs.ucs_timezone module – Configures timezone on Cisco UCS Manager

> **Note:**
>
> This module is part of the [cisco.ucs collection](https://galaxy.ansible.com/ui/repo/published/cisco/ucs/) (version 1.10.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ucs`.
> You need further requirements to be able to use this module,
> see [Requirements](ucs_timezone_module.md#ansible-collections-cisco-ucs-ucs-timezone-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ucs.ucs_timezone`.

New in cisco.ucs 2.7

- [Synopsis](ucs_timezone_module.md#synopsis)
- [Requirements](ucs_timezone_module.md#requirements)
- [Parameters](ucs_timezone_module.md#parameters)
- [Examples](ucs_timezone_module.md#examples)

## [Synopsis](ucs_timezone_module.md#id1)

- Configures timezone on Cisco UCS Manager.

## [Requirements](ucs_timezone_module.md#id2)

The below requirements are needed on the host that executes this module.

- ucsmsdk

## [Parameters](ucs_timezone_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **admin_state**  string | The admin_state setting  The enabled admin_state indicates the timezone configuration is utilized by UCS Manager.  The disabled admin_state indicates the timezone configuration is ignored by UCS Manager.  **Choices:**   - `"disabled"` - `"enabled"` ← (default) |
| **description**  aliases: descr  string | A user-defined description of the timezone.  Enter up to 256 characters.  You can use any characters or spaces except the following:  ` (accent mark), (backslash), ^ (carat), ” (double quote), = (equal sign), > (greater than), < (less than), or ‘ (single quote).  **Default:** `""` |
| **hostname**  string / required | IP address or hostname of Cisco UCS Manager.  Modules can be used with the UCS Platform Emulator <https://cs.co/ucspe> |
| **password**  string / required | Password for Cisco UCS Manager authentication. |
| **port**  integer | Port number to be used during connection (by default uses 443 for https and 80 for http connection). |
| **proxy**  string | If use_proxy is no, specfies proxy to be used for connection. e.g. ‘<http://proxy.xy.z:8080>’ |
| **state**  string | If `absent`, will unset timezone.  If `present`, will set or update timezone.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **timezone**  string | The timezone name.  Time zone names are from the [tz database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)  The timezone name is case sensitive.  The timezone name can be between 0 and 510 alphanumeric characters.  You cannot use spaces or any special characters other than  “-” (hyphen), “_” (underscore), “/” (backslash). |
| **use_proxy**  boolean | If `no`, will not use the proxy as defined by system environment variable.  **Choices:**   - `false` - `true` ← (default) |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  **Choices:**   - `false` - `true` ← (default) |
| **username**  string | Username for Cisco UCS Manager authentication.  **Default:** `"admin"` |

## [Examples](ucs_timezone_module.md#id4)

```yaml+jinja
- name: Configure Time Zone
  cisco.ucs.ucs_timezone:
    hostname: 172.16.143.150
    username: admin
    password: password
    state: present
    admin_state: enabled
    timezone: America/Los_Angeles
    description: 'Time Zone for Los Angeles'

- name: Unconfigure Time Zone
  cisco.ucs.ucs_timezone:
    hostname: 172.16.143.150
    username: admin
    password: password
    state: absent
    admin_state: disabled
```

### Authors

- David Soper (@dsoper2)
- John McDonough (@movinalot)
- CiscoUcs (@CiscoUcs)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-ucs)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-ucs)
