---
collection: ansible
version: "8"
title: "cisco.ucs.ucs_org module – Manages UCS Organizations for UCS Manager"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ucs/ucs_org_module.html
fetched_at: 2026-07-28T01:39:36+00:00
---
# cisco.ucs.ucs_org module – Manages UCS Organizations for UCS Manager

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
> see [Requirements](ucs_org_module.md#ansible-collections-cisco-ucs-ucs-org-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ucs.ucs_org`.

New in cisco.ucs 2.8

- [Synopsis](ucs_org_module.md#synopsis)
- [Requirements](ucs_org_module.md#requirements)
- [Parameters](ucs_org_module.md#parameters)
- [Examples](ucs_org_module.md#examples)

## [Synopsis](ucs_org_module.md#id1)

- Manages UCS Organizations for UCS Manager.

## [Requirements](ucs_org_module.md#id2)

The below requirements are needed on the host that executes this module.

- ucsmsdk

## [Parameters](ucs_org_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **delegate_to**  string | Where the module will be run  **Default:** `"localhost"` |
| **description**  aliases: descr  string | A user-defined description of the organization.  Enter up to 256 characters.  You can use any characters or spaces except the following:  ` (accent mark), (backslash), ^ (carat), ” (double quote), = (equal sign), > (greater than), < (less than), or ‘ (single quote). |
| **hostname**  string / required | IP address or hostname of Cisco UCS Manager.  Modules can be used with the UCS Platform Emulator <https://cs.co/ucspe> |
| **org_name**  aliases: name  string | The name of the organization.  Enter up to 16 characters.  You can use any characters or spaces except the following:  ` (accent mark), (backslash), ^ (carat), ” (double quote), = (equal sign), > (greater than), < (less than), or ‘ (single quote). |
| **parent_org_path**  string | A forward slash / separated hierarchical path from the root organization to the parent of the organization to be added or updated.  UCS Manager supports a hierarchical structure of organizations up to five levels deep not including the root organization.  For example the parent_org_path for an organization named level5 could be root/level1/level2/level3/level4  **Default:** `"root"` |
| **password**  string / required | Password for Cisco UCS Manager authentication. |
| **port**  integer | Port number to be used during connection (by default uses 443 for https and 80 for http connection). |
| **proxy**  string | If use_proxy is no, specfies proxy to be used for connection. e.g. ‘<http://proxy.xy.z:8080>’ |
| **state**  string | If `absent`, will remove organization.  If `present`, will create or update organization.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **use_proxy**  boolean | If `no`, will not use the proxy as defined by system environment variable.  **Choices:**   - `false` - `true` ← (default) |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  **Choices:**   - `false` - `true` ← (default) |
| **username**  string | Username for Cisco UCS Manager authentication.  **Default:** `"admin"` |

## [Examples](ucs_org_module.md#id4)

```yaml+jinja
- name: Add UCS Organization
  cisco.ucs.ucs_org:
    hostname: "{{ ucs_hostname }}"
    username: "{{ ucs_username }}"
    password: "{{ ucs_password }}"
    org_name: test
    description: testing org
    state: present
    delegate_to: localhost

- name: Update UCS Organization
  cisco.ucs.ucs_org:
    hostname: "{{ ucs_hostname }}"
    username: "{{ ucs_username }}"
    password: "{{ ucs_password }}"
    org_name: test
    description: Testing org
    state: present
    delegate_to: localhost

- name: Add UCS Organization
  cisco.ucs.ucs_org:
    hostname: "{{ ucs_hostname }}"
    username: "{{ ucs_username }}"
    password: "{{ ucs_password }}"
    org_name: level1
    parent_org_path: root
    description: level1 org
    state: present
    delegate_to: localhost

- name: Add UCS Organization
  cisco.ucs.ucs_org:
    hostname: "{{ ucs_hostname }}"
    username: "{{ ucs_username }}"
    password: "{{ ucs_password }}"
    org_name: level2
    parent_org_path: root/level1
    description: level2 org
    state: present

- name: Add UCS Organization
  cisco.ucs.ucs_org:
    hostname: "{{ ucs_hostname }}"
    username: "{{ ucs_username }}"
    password: "{{ ucs_password }}"
    org_name: level3
    parent_org_path: root/level1/level2
    description: level3 org
    state: present

- name: Remove UCS Organization
  cisco.ucs.ucs_org:
    hostname: "{{ ucs_hostname }}"
    username: "{{ ucs_username }}"
    password: "{{ ucs_password }}"
    org_name: level2
    parent_org_path: root/level1
    state: absent
```

### Authors

- David Soper (@dsoper2)
- John McDonough (@movinalot)
- CiscoUcs (@CiscoUcs)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-ucs)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-ucs)
