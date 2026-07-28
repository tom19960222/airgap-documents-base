---
collection: ansible
version: "8"
title: "cisco.ucs.ucs_system_qos module – Configures system QoS settings"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ucs/ucs_system_qos_module.html
fetched_at: 2026-07-28T01:39:44+00:00
---
# cisco.ucs.ucs_system_qos module – Configures system QoS settings

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
> see [Requirements](ucs_system_qos_module.md#ansible-collections-cisco-ucs-ucs-system-qos-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ucs.ucs_system_qos`.

New in cisco.ucs 2.1

- [Synopsis](ucs_system_qos_module.md#synopsis)
- [Requirements](ucs_system_qos_module.md#requirements)
- [Parameters](ucs_system_qos_module.md#parameters)
- [Examples](ucs_system_qos_module.md#examples)

## [Synopsis](ucs_system_qos_module.md#id1)

- Configures system QoS settings

## [Requirements](ucs_system_qos_module.md#id2)

The below requirements are needed on the host that executes this module.

- ucsmsdk

## [Parameters](ucs_system_qos_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **admin_state**  string | Admin state of QoS Policy  **Choices:**   - `"disabled"` - `"enabled"` ← (default) |
| **cos**  string / required | CoS setting  **Choices:**   - `"any"` - `"0-6"` |
| **drop**  string | Set multicast optimization options  **Choices:**   - `"drop"` ← (default) - `"no-drop"` |
| **hostname**  string / required | IP address or hostname of Cisco UCS Manager.  Modules can be used with the UCS Platform Emulator <https://cs.co/ucspe> |
| **mtu**  string | MTU size  **Choices:**   - `"fc"` - `"normal"` ← (default) - `"0-4294967295"` |
| **multicast_optimize**  string | Set multicast optimization options  **Choices:**   - `"false"` - `"no"` - `"true"` - `"yes"` |
| **password**  string / required | Password for Cisco UCS Manager authentication. |
| **port**  integer | Port number to be used during connection (by default uses 443 for https and 80 for http connection). |
| **priority**  string / required | Priority to configure  **Choices:**   - `"best-effort"` - `"bronze"` - `"fc"` - `"gold"` - `"platinum"` - `"silver"` |
| **proxy**  string | If use_proxy is no, specfies proxy to be used for connection. e.g. ‘<http://proxy.xy.z:8080>’ |
| **use_proxy**  boolean | If `no`, will not use the proxy as defined by system environment variable.  **Choices:**   - `false` - `true` ← (default) |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  **Choices:**   - `false` - `true` ← (default) |
| **username**  string | Username for Cisco UCS Manager authentication.  **Default:** `"admin"` |
| **weight**  string / required | CoS profile weight  **Choices:**   - `"best-effort"` - `"none"` - `"0-10"` |

## [Examples](ucs_system_qos_module.md#id4)

```yaml+jinja
- name:
  cisco.ucs.ucs_system_qos:
    priority: platinum
    admin_state: enabled
    multicast_optimize: no
    cos: '5'
    weight: '10'
    mtu: '9216'
    hostname: 192.168.99.100
    username: admin
    password: password
```

### Authors

- Brett Johnson (@sdbrett)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-ucs)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-ucs)
