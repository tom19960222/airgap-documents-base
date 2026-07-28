---
collection: ansible
version: "8"
title: "cisco.ucs.ucs_serial_over_lan_policy module – Manages UCS Serial Over Lan Policies on UCS Manager"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ucs/ucs_serial_over_lan_policy_module.html
fetched_at: 2026-07-28T01:39:39+00:00
---
# cisco.ucs.ucs_serial_over_lan_policy module – Manages UCS Serial Over Lan Policies on UCS Manager

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
> see [Requirements](ucs_serial_over_lan_policy_module.md#ansible-collections-cisco-ucs-ucs-serial-over-lan-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ucs.ucs_serial_over_lan_policy`.

New in cisco.ucs 2.9

- [Synopsis](ucs_serial_over_lan_policy_module.md#synopsis)
- [Requirements](ucs_serial_over_lan_policy_module.md#requirements)
- [Parameters](ucs_serial_over_lan_policy_module.md#parameters)
- [Examples](ucs_serial_over_lan_policy_module.md#examples)

## [Synopsis](ucs_serial_over_lan_policy_module.md#id1)

- Manages UCS Serial Over Lan Policies on UCS Manager.

## [Requirements](ucs_serial_over_lan_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- ucsmsdk

## [Parameters](ucs_serial_over_lan_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **admin_state**  string | The administrative state of the serial over lan policy.  disable Serial over LAN access is blocked.  enable Serial over LAN access is permitted.  **Choices:**   - `"disable"` - `"enable"` |
| **description**  aliases: descr  string | A user-defined description of the serial over lan policy.  Enter up to 256 characters.  You can use any characters or spaces except the following:  ` (accent mark), (backslash), ^ (carat), ” (double quote)  = (equal sign), > (greater than), < (less than), ‘ (single quote). |
| **hostname**  string / required | IP address or hostname of Cisco UCS Manager.  Modules can be used with the UCS Platform Emulator <https://cs.co/ucspe> |
| **name**  string / required | The name of the serial over lan policy.  Enter up to 16 characters.  You can use any characters or spaces except the following:  ` (accent mark), (backslash), ^ (carat), ” (double quote)  = (equal sign), > (greater than), < (less than), ‘ (single quote). |
| **org_dn**  string | Org dn (distinguished name) of the serial over lan policy.  **Default:** `"org-root"` |
| **password**  string / required | Password for Cisco UCS Manager authentication. |
| **port**  integer | Port number to be used during connection (by default uses 443 for https and 80 for http connection). |
| **proxy**  string | If use_proxy is no, specfies proxy to be used for connection. e.g. ‘<http://proxy.xy.z:8080>’ |
| **speed**  string | The transmission speed of the serial over lan policy.  **Choices:**   - `"9600"` - `"19200"` - `"38400"` - `"57600"` - `"115200"` |
| **state**  string | If `absent`, will remove Serial Over Lan Policy.  If `present`, will create or update Serial Over Lan Policy.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **use_proxy**  boolean | If `no`, will not use the proxy as defined by system environment variable.  **Choices:**   - `false` - `true` ← (default) |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  **Choices:**   - `false` - `true` ← (default) |
| **username**  string | Username for Cisco UCS Manager authentication.  **Default:** `"admin"` |

## [Examples](ucs_serial_over_lan_policy_module.md#id4)

```yaml+jinja
- name: Add UCS Serial Over Lan Policy
  cisco.ucs.ucs_serial_over_lan:
    hostname: "{{ ucs_hostname }}"
    username: "{{ ucs_username }}"
    password: "{{ ucs_password }}"
    state: present
    name: sol_org_root
    description: Serial Over Lan for Org root servers
    admin_state: enable
    speed: 115200
  delegate_to: localhost

- name: Add UCS Serial Over Lan Policy in Organization
  cisco.ucs.ucs_serial_over_lan:
    hostname: "{{ ucs_hostname }}"
    username: "{{ ucs_username }}"
    password: "{{ ucs_password }}"
    state: present
    org_dn: org-root/org-prod
    name: sol_org_prod
    description: Serial Over Lan for Org Prod servers
    admin_state: enable
    speed: 115200
  delegate_to: localhost

- name: Update UCS Serial Over Lan Policy in Organization
  cisco.ucs.ucs_serial_over_lan:
    hostname: "{{ ucs_hostname }}"
    username: "{{ ucs_username }}"
    password: "{{ ucs_password }}"
    state: present
    org_dn: org-root/org-prod
    name: sol_org_prod
    description: Serial Over Lan for Org Prod servers
    admin_state: enable
    speed: 38400
  delegate_to: localhost

- name: Update UCS Serial Over Lan Policy in Organization
  cisco.ucs.ucs_serial_over_lan:
    hostname: "{{ ucs_hostname }}"
    username: "{{ ucs_username }}"
    password: "{{ ucs_password }}"
    state: present
    org_dn: org-root/org-prod
    name: sol_org_prod
    descr: Serial Over Lan for Org Prod servers
    admin_state: enable
    speed: 57600
  delegate_to: localhost

- name: Delete UCS Serial Over Lan Policy in Organization
  cisco.ucs.ucs_serial_over_lan:
    hostname: "{{ ucs_hostname }}"
    username: "{{ ucs_username }}"
    password: "{{ ucs_password }}"
    state: absent
    org_dn: org-root/org-prod
    name: sol_org_prod
  delegate_to: localhost

- name: Delete UCS Serial Over Lan Policy
  cisco.ucs.ucs_serial_over_lan:
    hostname: "{{ ucs_hostname }}"
    username: "{{ ucs_username }}"
    password: "{{ ucs_password }}"
    state: absent
    name: sol_org_root
  delegate_to: localhost
```

### Authors

- John McDonough (@movinalot)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-ucs)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-ucs)
