---
collection: ansible
version: "8"
title: "cisco.ucs.ucs_scrub_policy module – Manages UCS Scrub Policies on UCS Manager"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ucs/ucs_scrub_policy_module.html
fetched_at: 2026-07-28T01:39:38+00:00
---
# cisco.ucs.ucs_scrub_policy module – Manages UCS Scrub Policies on UCS Manager

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
> see [Requirements](ucs_scrub_policy_module.md#ansible-collections-cisco-ucs-ucs-scrub-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ucs.ucs_scrub_policy`.

New in cisco.ucs 2.9

- [Synopsis](ucs_scrub_policy_module.md#synopsis)
- [Requirements](ucs_scrub_policy_module.md#requirements)
- [Parameters](ucs_scrub_policy_module.md#parameters)
- [Examples](ucs_scrub_policy_module.md#examples)

## [Synopsis](ucs_scrub_policy_module.md#id1)

- Manages UCS Scrub Policies on UCS Manager.

## [Requirements](ucs_scrub_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- ucsmsdk

## [Parameters](ucs_scrub_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **bios_settings_scrub**  string | Scrub the BIOS settings.  If the field is set to Yes, when a service profile containing this  scrub policy is disassociated from a server, the BIOS settings for  that server are erased and reset to the defaults for that server  type and vendor. If this field is set to No, the BIOS settings are  preserved.  yes scrub the BIOS settings.  no do not scrub the BIOS settings.  **Choices:**   - `"True"` - `"False"` |
| **description**  aliases: descr  string | A user-defined description of the organization.  Enter up to 256 characters.  You can use any characters or spaces except the following:  ` (accent mark), (backslash), ^ (carat), ” (double quote)  = (equal sign), > (greater than), < (less than), ‘ (single quote). |
| **disk_scrub**  string | Scrub the BIOS settings.  If this field is set to Yes, when a service profile containing this  scrub policy is disassociated from a server, all data on the server  local drives is completely erased. If this field is set to No, the  data on the local drives is preserved, including all local storage  configuration.  yes scrub the server disks.  no do not scrub the server disks.  **Choices:**   - `"True"` - `"False"` |
| **flex_flash_scrub**  string | Scrub the BIOS settings.  If the field is set to Yes, the HV partition on the SD card is  formatted using the PNUOS formatting utility when the server is  reacknowledged. If this field is set to No, the SD card is preserved.  yes scrub the flex flash.  no do not scrub the flex flash.  **Choices:**   - `"True"` - `"False"` |
| **hostname**  string / required | IP address or hostname of Cisco UCS Manager.  Modules can be used with the UCS Platform Emulator <https://cs.co/ucspe> |
| **name**  string / required | The name of the organization.  Enter up to 16 characters.  You can use any characters or spaces except the following:  ` (accent mark), (backslash), ^ (carat), ” (double quote)  = (equal sign), > (greater than), < (less than), ‘ (single quote). |
| **org_dn**  string | Org dn (distinguished name)  **Default:** `"org-root"` |
| **password**  string / required | Password for Cisco UCS Manager authentication. |
| **persistent_memory_scrub**  string | Scrub the BIOS settings.  If the field is set to Yes, when a service profile containing this  scrub policy is disassociated from a server, all persistent memory  modules for that server are erased and reset to the defaults for that  server type and vendor. If this field is set to No, the persistent  memory modules are preserved.  yes scrub the persistent memory.  no do not scrub the persistent memory.  **Choices:**   - `"True"` - `"False"` |
| **port**  integer | Port number to be used during connection (by default uses 443 for https and 80 for http connection). |
| **proxy**  string | If use_proxy is no, specfies proxy to be used for connection. e.g. ‘<http://proxy.xy.z:8080>’ |
| **state**  string | If `absent`, will remove organization.  If `present`, will create or update organization.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **use_proxy**  boolean | If `no`, will not use the proxy as defined by system environment variable.  **Choices:**   - `false` - `true` ← (default) |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  **Choices:**   - `false` - `true` ← (default) |
| **username**  string | Username for Cisco UCS Manager authentication.  **Default:** `"admin"` |

## [Examples](ucs_scrub_policy_module.md#id4)

```yaml+jinja
- name: Add UCS Scrub Policy
  cisco.ucs.ucs_scrub_policy:
    hostname: "{{ ucs_hostname }}"
    username: "{{ ucs_username }}"
    password: "{{ ucs_password }}"
    state: present
    description: Scrub All Policy
    name: all_scrub
    bios_settings_scrub: yes
    disk_scrub: yes
    flex_flash_scrub: yes
    persistent_memory_scrub: yes
  delegate_to: localhost

- name: Add UCS Scrub Policy in an Organization
  cisco.ucs.ucs_scrub_policy:
    hostname: "{{ ucs_hostname }}"
    username: "{{ ucs_username }}"
    password: "{{ ucs_password }}"
    state: present
    org_dn: org-root/org-prod
    name: all_scrub
    description: Scrub All Policy Org Prod servers
    bios_settings_scrub: yes
    disk_scrub: yes
    flex_flash_scrub: yes
    persistent_memory_scrub: yes
  delegate_to: localhost

- name: Update UCS Scrub Policy
  cisco.ucs.ucs_scrub_policy:
    hostname: "{{ ucs_hostname }}"
    username: "{{ ucs_username }}"
    password: "{{ ucs_password }}"
    state: present
    org_dn: org-root/org-prod
    name: BD_scrub
    description: Scrub BIOS and Disk Policy Org Prod servers
    bios_settings_scrub: yes
    disk_scrub: yes
    flex_flash_scrub: no
    persistent_memory_scrub: no
  delegate_to: localhost

- name: Update UCS Scrub Policy
  cisco.ucs.ucs_scrub_policy:
    hostname: "{{ ucs_hostname }}"
    username: "{{ ucs_username }}"
    password: "{{ ucs_password }}"
    state: present
    org_dn: org-root/org-prod
    name: BD_scrub
    description: Scrub BIOS and Disk Policy Org Prod servers
    bios_settings_scrub: yes
    disk_scrub: yes
    flex_flash_scrub: yes
  delegate_to: localhost

- name: Delete UCS Scrub Policy
  cisco.ucs.ucs_scrub_policy:
    hostname: "{{ ucs_hostname }}"
    username: "{{ ucs_username }}"
    password: "{{ ucs_password }}"
    state: absent
    org_dn: org-root/org-prod
    name: BD_scrub
  delegate_to: localhost

- name: Delete UCS Scrub Policy
  cisco.ucs.ucs_scrub_policy:
    hostname: "{{ ucs_hostname }}"
    username: "{{ ucs_username }}"
    password: "{{ ucs_password }}"
    state: absent
    name: BD_scrub
  delegate_to: localhost
```

### Authors

- John McDonough (@movinalot)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-ucs)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-ucs)
