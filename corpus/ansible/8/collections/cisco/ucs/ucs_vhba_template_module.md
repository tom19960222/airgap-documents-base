---
collection: ansible
version: "8"
title: "cisco.ucs.ucs_vhba_template module – Configures vHBA templates on Cisco UCS Manager"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ucs/ucs_vhba_template_module.html
fetched_at: 2026-07-28T01:39:46+00:00
---
# cisco.ucs.ucs_vhba_template module – Configures vHBA templates on Cisco UCS Manager

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
> see [Requirements](ucs_vhba_template_module.md#ansible-collections-cisco-ucs-ucs-vhba-template-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ucs.ucs_vhba_template`.

New in cisco.ucs 2.5

- [Synopsis](ucs_vhba_template_module.md#synopsis)
- [Requirements](ucs_vhba_template_module.md#requirements)
- [Parameters](ucs_vhba_template_module.md#parameters)
- [Examples](ucs_vhba_template_module.md#examples)

## [Synopsis](ucs_vhba_template_module.md#id1)

- Configures vHBA templates on Cisco UCS Manager.

## [Requirements](ucs_vhba_template_module.md#id2)

The below requirements are needed on the host that executes this module.

- ucsmsdk

## [Parameters](ucs_vhba_template_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  aliases: descr  string | A user-defined description of the template.  Enter up to 256 characters.  You can use any characters or spaces except the following:  ` (accent mark), (backslash), ^ (carat), ” (double quote), = (equal sign), > (greater than), < (less than), or ‘ (single quote). |
| **fabric**  string | The Fabric ID field.  The name of the fabric interconnect that vHBAs created with this template are associated with.  **Choices:**   - `"A"` ← (default) - `"B"` |
| **hostname**  string / required | IP address or hostname of Cisco UCS Manager.  Modules can be used with the UCS Platform Emulator <https://cs.co/ucspe> |
| **max_data**  string | The Max Data Field Size field.  The maximum size of the Fibre Channel frame payload bytes that the vHBA supports.  Enter an string between ‘256’ and ‘2112’.  **Default:** `"2048"` |
| **name**  string / required | The name of the virtual HBA template.  This name can be between 1 and 16 alphanumeric characters.  You cannot use spaces or any special characters other than - (hyphen), “_” (underscore), : (colon), and . (period).  You cannot change this name after the template is created. |
| **org_dn**  string | Org dn (distinguished name)  **Default:** `"org-root"` |
| **password**  string / required | Password for Cisco UCS Manager authentication. |
| **pin_group**  string | The SAN pin group that is associated with vHBAs created from this template. |
| **port**  integer | Port number to be used during connection (by default uses 443 for https and 80 for http connection). |
| **proxy**  string | If use_proxy is no, specfies proxy to be used for connection. e.g. ‘<http://proxy.xy.z:8080>’ |
| **qos_policy**  string | The QoS policy that is associated with vHBAs created from this template. |
| **redundancy_type**  string | The Redundancy Type used for template pairing from the Primary or Secondary redundancy template.  primary — Creates configurations that can be shared with the Secondary template.  Any other shared changes on the Primary template are automatically synchronized to the Secondary template.  secondary — All shared configurations are inherited from the Primary template.  none - Legacy vHBA template behavior. Select this option if you do not want to use redundancy.  **Choices:**   - `"none"` ← (default) - `"primary"` - `"secondary"` |
| **state**  string | If `present`, will verify vHBA templates are present and will create if needed.  If `absent`, will verify vHBA templates are absent and will delete if needed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **stats_policy**  string | The statistics collection policy that is associated with vHBAs created from this template.  **Default:** `"default"` |
| **template_type**  string | The Template Type field.  This can be one of the following:  initial-template — vHBAs created from this template are not updated if the template changes.  updating-template - vHBAs created from this template are updated if the template changes.  **Choices:**   - `"initial-template"` ← (default) - `"updating-template"` |
| **use_proxy**  boolean | If `no`, will not use the proxy as defined by system environment variable.  **Choices:**   - `false` - `true` ← (default) |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  **Choices:**   - `false` - `true` ← (default) |
| **username**  string | Username for Cisco UCS Manager authentication.  **Default:** `"admin"` |
| **vsan**  string | The VSAN to associate with vHBAs created from this template.  **Default:** `"default"` |
| **wwpn_pool**  string | The WWPN pool that a vHBA created from this template uses to derive its WWPN address.  **Default:** `"default"` |

## [Examples](ucs_vhba_template_module.md#id4)

```yaml+jinja
- name: Configure vHBA template
  cisco.ucs.ucs_vhba_template:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: vHBA-A
    fabric: A
    vsan: VSAN-A
    wwpn_pool: WWPN-Pool-A

- name: Remote vHBA template
  cisco.ucs.ucs_vhba_template:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: vHBA-A
    state: absent
```

### Authors

- David Soper (@dsoper2)
- John McDonough (@movinalot)
- CiscoUcs (@CiscoUcs)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-ucs)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-ucs)
