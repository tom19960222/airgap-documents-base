---
collection: ansible
version: "6"
title: "cisco.ucs.ucs_san_connectivity module – Configures SAN Connectivity Policies on Cisco UCS Manager"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ucs/ucs_san_connectivity_module.html
fetched_at: 2026-07-27T17:02:50+00:00
---
# cisco.ucs.ucs_san_connectivity module – Configures SAN Connectivity Policies on Cisco UCS Manager

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
> see [Requirements](ucs_san_connectivity_module.md#ansible-collections-cisco-ucs-ucs-san-connectivity-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ucs.ucs_san_connectivity`.

New in cisco.ucs 2.5

- [Synopsis](ucs_san_connectivity_module.md#synopsis)
- [Requirements](ucs_san_connectivity_module.md#requirements)
- [Parameters](ucs_san_connectivity_module.md#parameters)
- [Examples](ucs_san_connectivity_module.md#examples)

## [Synopsis](ucs_san_connectivity_module.md#id1)

- Configures SAN Connectivity Policies on Cisco UCS Manager.

## [Requirements](ucs_san_connectivity_module.md#id2)

The below requirements are needed on the host that executes this module.

- ucsmsdk

## [Parameters](ucs_san_connectivity_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  aliases: descr  string | A description of the policy.  Cisco recommends including information about where and when to use the policy.  Enter up to 256 characters.  You can use any characters or spaces except the following:  ` (accent mark), (backslash), ^ (carat), ” (double quote), = (equal sign), > (greater than), < (less than), or ‘ (single quote). |
| **hostname**  string / required | IP address or hostname of Cisco UCS Manager.  Modules can be used with the UCS Platform Emulator <https://cs.co/ucspe> |
| **name**  string / required | The name of the SAN Connectivity Policy.  This name can be between 1 and 16 alphanumeric characters.  You cannot use spaces or any special characters other than - (hyphen), “_” (underscore), : (colon), and . (period).  You cannot change this name after the policy is created. |
| **org_dn**  string | Org dn (distinguished name)  Default: `"org-root"` |
| **password**  string / required | Password for Cisco UCS Manager authentication. |
| **port**  integer | Port number to be used during connection (by default uses 443 for https and 80 for http connection). |
| **proxy**  string | If use_proxy is no, specfies proxy to be used for connection. e.g. ‘<http://proxy.xy.z:8080>’ |
| **state**  string | If `present`, will verify SAN Connectivity Policies are present and will create if needed.  If `absent`, will verify SAN Connectivity Policies are absent and will delete if needed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **use_proxy**  boolean | If `no`, will not use the proxy as defined by system environment variable.  Choices:   - `false` - `true` ← (default) |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  Choices:   - `false` - `true` ← (default) |
| **username**  string | Username for Cisco UCS Manager authentication.  Default: `"admin"` |
| **vhba_list**  string | List of vHBAs used by the SAN Connectivity Policy.  vHBAs used by the SAN Connectivity Policy must be created from a vHBA template.  Each list element has the following suboptions:  = name  The name of the virtual HBA (required).  = vhba_template  The name of the virtual HBA template (required).   - adapter_policy  The name of the Fibre Channel adapter policy.  A user defined policy can be used, or one of the system defined policies (default, Linux, Solaris, VMware, Windows, WindowsBoot)  [Default: default] - order  String specifying the vHBA assignment order (e.g., ‘1’, ‘2’).  [Default: unspecified] |
| **wwnn_pool**  string | Name of the WWNN pool to use for WWNN assignment.  Default: `"default"` |

## [Examples](ucs_san_connectivity_module.md#id4)

```yaml+jinja
- name: Configure SAN Connectivity Policy
  cisco.ucs.ucs_san_connectivity:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: Cntr-FC-Boot
    wwnn_pool: WWNN-Pool
    vhba_list:
    - name: Fabric-A
      vhba_template: vHBA-Template-A
      adapter_policy: Linux
    - name: Fabric-B
      vhba_template: vHBA-Template-B
      adapter_policy: Linux

- name: Remove SAN Connectivity Policy
  cisco.ucs.ucs_san_connectivity:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: Cntr-FC-Boot
    state: absent
```

### Authors

- David Soper (@dsoper2)
- John McDonough (@movinalot)
- CiscoUcs (@CiscoUcs)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-ucs)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-ucs)
