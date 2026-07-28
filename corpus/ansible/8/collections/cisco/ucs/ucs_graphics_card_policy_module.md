---
collection: ansible
version: "8"
title: "cisco.ucs.ucs_graphics_card_policy module – Manages UCS Graphics Card Policies on UCS Manager"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ucs/ucs_graphics_card_policy_module.html
fetched_at: 2026-07-28T01:39:32+00:00
---
# cisco.ucs.ucs_graphics_card_policy module – Manages UCS Graphics Card Policies on UCS Manager

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
> see [Requirements](ucs_graphics_card_policy_module.md#ansible-collections-cisco-ucs-ucs-graphics-card-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ucs.ucs_graphics_card_policy`.

New in cisco.ucs 2.9

- [Synopsis](ucs_graphics_card_policy_module.md#synopsis)
- [Requirements](ucs_graphics_card_policy_module.md#requirements)
- [Parameters](ucs_graphics_card_policy_module.md#parameters)
- [Examples](ucs_graphics_card_policy_module.md#examples)

## [Synopsis](ucs_graphics_card_policy_module.md#id1)

- Manages UCS Graphics Card Policies on UCS Manager.

## [Requirements](ucs_graphics_card_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- ucsmsdk

## [Parameters](ucs_graphics_card_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  aliases: descr  string | A user-defined description of the organization.  Enter up to 256 characters.  You can use any characters or spaces except the following:  ` (accent mark), (backslash), ^ (carat), ” (double quote)  = (equal sign), > (greater than), < (less than), ‘ (single quote). |
| **graphics_card_mode**  string | Set the Graphics Card Mode.  **Choices:**   - `"any-configuration"` - `"compute"` - `"graphics"` |
| **hostname**  string / required | IP address or hostname of Cisco UCS Manager.  Modules can be used with the UCS Platform Emulator <https://cs.co/ucspe> |
| **name**  string / required | The name of the organization.  Enter up to 16 characters.  You can use any characters or spaces except the following:  ` (accent mark), (backslash), ^ (carat), ” (double quote)  = (equal sign), > (greater than), < (less than), ‘ (single quote). |
| **org_dn**  string | Org dn (distinguished name)  **Default:** `"org-root"` |
| **password**  string / required | Password for Cisco UCS Manager authentication. |
| **port**  integer | Port number to be used during connection (by default uses 443 for https and 80 for http connection). |
| **proxy**  string | If use_proxy is no, specfies proxy to be used for connection. e.g. ‘<http://proxy.xy.z:8080>’ |
| **state**  string | If `absent`, will remove organization.  If `present`, will create or update organization.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **use_proxy**  boolean | If `no`, will not use the proxy as defined by system environment variable.  **Choices:**   - `false` - `true` ← (default) |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  **Choices:**   - `false` - `true` ← (default) |
| **username**  string | Username for Cisco UCS Manager authentication.  **Default:** `"admin"` |

## [Examples](ucs_graphics_card_policy_module.md#id4)

```yaml+jinja
- name: Add UCS Graphics Card Policy
  cisco.ucs.ucs_graphics_card_policy:
    hostname: "{{ ucs_hostname }}"
    username: "{{ ucs_username }}"
    password: "{{ ucs_password }}"
    state: present
    description: Any Graphics Mode Policy
    name: any_graphics
    graphics_card_mode: any-configuration
  delegate_to: localhost

- name: Add UCS Graphics Card Policy in an Organization
  cisco.ucs.ucs_graphics_card_policy:
    hostname: "{{ ucs_hostname }}"
    username: "{{ ucs_username }}"
    password: "{{ ucs_password }}"
    state: present
    org_dn: org-root/org-prod
    description: Any Graphics Mode Policy
    name: prod_graphics
    graphics_card_mode: any-configuration
  delegate_to: localhost

- name: Update UCS Graphics Card Policy in an Organization
  cisco.ucs.ucs_graphics_card_policy:
    hostname: "{{ ucs_hostname }}"
    username: "{{ ucs_username }}"
    password: "{{ ucs_password }}"
    state: present
    org_dn: org-root/org-prod
    description: Graphics Mode Policy
    name: prod_graphics
    graphics_card_mode: graphics
  delegate_to: localhost

- name: Update UCS Graphics Card Policy in an Organization
  cisco.ucs.ucs_graphics_card_policy:
    hostname: "{{ ucs_hostname }}"
    username: "{{ ucs_username }}"
    password: "{{ ucs_password }}"
    state: present
    org_dn: org-root/org-prod
    description: Compute Mode Policy
    name: prod_graphics
    graphics_card_mode: compute
  delegate_to: localhost

- name: Delete UCS Graphics Card Policy in an Organization
  cisco.ucs.ucs_graphics_card_policy:
    hostname: "{{ ucs_hostname }}"
    username: "{{ ucs_username }}"
    password: "{{ ucs_password }}"
    state: absent
    org_dn: org-root/org-prod
    name: prod_graphics
  delegate_to: localhost

- name: Delete UCS Graphics Card Policy
  cisco.ucs.ucs_graphics_card_policy:
    hostname: "{{ ucs_hostname }}"
    username: "{{ ucs_username }}"
    password: "{{ ucs_password }}"
    state: absent
    name: any_graphics
  delegate_to: localhost
```

### Authors

- John McDonough (@movinalot)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-ucs)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-ucs)
