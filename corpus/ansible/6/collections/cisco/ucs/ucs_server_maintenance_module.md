---
collection: ansible
version: "6"
title: "cisco.ucs.ucs_server_maintenance module – Creates Server Maintenance Policy on Cisco UCS Manager"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ucs/ucs_server_maintenance_module.html
fetched_at: 2026-07-27T17:02:52+00:00
---
# cisco.ucs.ucs_server_maintenance module – Creates Server Maintenance Policy on Cisco UCS Manager

> **Note:**
>
> This module is part of the [cisco.ucs collection](https://galaxy.ansible.com/cisco/ucs) (version 1.8.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ucs`.
> You need further requirements to be able to use this module,
> see [Requirements](ucs_server_maintenance_module.md#ansible-collections-cisco-ucs-ucs-server-maintenance-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ucs.ucs_server_maintenance`.

New in cisco.ucs 2.1

- [Synopsis](ucs_server_maintenance_module.md#synopsis)
- [Requirements](ucs_server_maintenance_module.md#requirements)
- [Parameters](ucs_server_maintenance_module.md#parameters)
- [Examples](ucs_server_maintenance_module.md#examples)

## [Synopsis](ucs_server_maintenance_module.md#id1)

- Configures Server Maintenance Policy on Cisco UCS Manager.

## [Requirements](ucs_server_maintenance_module.md#id2)

The below requirements are needed on the host that executes this module.

- ucsmsdk

## [Parameters](ucs_server_maintenance_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  aliases: descr  string | A description of the Server Maintenance Package Policy.  Cisco recommends including information about where and when to use the policy.  Enter up to 256 characters.  You can use any characters or spaces except the following:  ` (accent mark), (backslash), ^ (carat), ” (double quote), = (equal sign), > (greater than), < (less than), or ‘ (single quote). |
| **hostname**  string / required | IP address or hostname of Cisco UCS Manager.  Modules can be used with the UCS Platform Emulator <https://cs.co/ucspe> |
| **name**  string / required | The name assigned to the Server Maintenance Policy.  The Server Maintenance Policy name is case sensitive.  This name can be between 1 and 16 alphanumeric characters.  You cannot use spaces or any special characters other than - (hyphen), “_” (underscore), : (colon), and . (period).  You cannot change this name after the Server Maintenance Policy is created. |
| **password**  string / required | Password for Cisco UCS Manager authentication. |
| **port**  integer | Port number to be used during connection (by default uses 443 for https and 80 for http connection). |
| **proxy**  string | If use_proxy is no, specfies proxy to be used for connection. e.g. ‘<http://proxy.xy.z:8080>’ |
| **state**  string | If `present`, will verify Server Maintenance Policy is present and will create if needed.  If `absent`, will verify Server Maintenance Policy is absent and will delete if needed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **trigger_config**  string | This option is used in combination with either User Ack (user-ack) or Timer Automatic (timer-automatic).  When the On Next Boot option is enabled, the host OS reboot, shutdown, or server reset also triggers the associated FSM to apply the changes.  Note that de-selecting the On Next Boot option disables the Maintenance Policy on the BMC.  Choices:   - `"on-next-boot"` |
| **uptime_disr**  string / required | When a Server profile is associated with a Server, or when changes are made to a Server profile that is already associated with a Server, you must reboot the Server to complete the process.  The Reboot Policy field determines when the reboot occurs for Server associated with any Server profiles that include this maintenance policy.  Choices:   - `"immediate"` - `"timer-automatic"` - `"user-ack"` |
| **use_proxy**  boolean | If `no`, will not use the proxy as defined by system environment variable.  Choices:   - `false` - `true` ← (default) |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  Choices:   - `false` - `true` ← (default) |
| **username**  string | Username for Cisco UCS Manager authentication.  Default: `"admin"` |

## [Examples](ucs_server_maintenance_module.md#id4)

```yaml+jinja
- name: Add Server Maintenance Policy
  cisco.ucs.ucs_server_maintenance:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: user-ack
    uptime_disr: user-ack
    trigger_config: on-next-boot
```

### Authors

- Brett Johnson (@brettjohnson008)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-ucs)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-ucs)
