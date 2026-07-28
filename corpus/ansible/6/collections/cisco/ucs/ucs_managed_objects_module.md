---
collection: ansible
version: "6"
title: "cisco.ucs.ucs_managed_objects module – Configures Managed Objects on Cisco UCS Manager"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ucs/ucs_managed_objects_module.html
fetched_at: 2026-07-27T17:02:47+00:00
---
# cisco.ucs.ucs_managed_objects module – Configures Managed Objects on Cisco UCS Manager

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
> see [Requirements](ucs_managed_objects_module.md#ansible-collections-cisco-ucs-ucs-managed-objects-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ucs.ucs_managed_objects`.

New in cisco.ucs 2.8

- [Synopsis](ucs_managed_objects_module.md#synopsis)
- [Requirements](ucs_managed_objects_module.md#requirements)
- [Parameters](ucs_managed_objects_module.md#parameters)
- [Examples](ucs_managed_objects_module.md#examples)

## [Synopsis](ucs_managed_objects_module.md#id1)

- Configures Managed Objects on Cisco UCS Manager.
- The Python SDK module, Python class within the module (UCSM Class), and all properties must be directly specified.
- More information on the UCSM Python SDK and how to directly configure Managed Objects is available at [UCSM Python SDK](http://ucsmsdk.readthedocs.io/).

## [Requirements](ucs_managed_objects_module.md#id2)

The below requirements are needed on the host that executes this module.

- ucsmsdk

## [Parameters](ucs_managed_objects_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **hostname**  string / required | IP address or hostname of Cisco UCS Manager.  Modules can be used with the UCS Platform Emulator <https://cs.co/ucspe> |
| **objects**  string / required | List of managed objects to configure. Each managed object has suboptions the specify the Python SDK module, class, and properties to configure. |
| **children**  string | Optional list of child objects. Each child has its own module, class, and properties suboptions.  The parent_mo_or_dn property for child objects is automatically set as the list of children is configured. |
| **class_name**  string / required | Name of the Python class that will be used to configure the Managed Object. |
| **module**  string / required | Name of the Python SDK module implementing the required class. |
| **properties**  string / required | List of properties to configure on the Managed Object. See the UCSM Python SDK for information on properties for each class. |
| **password**  string / required | Password for Cisco UCS Manager authentication. |
| **port**  integer | Port number to be used during connection (by default uses 443 for https and 80 for http connection). |
| **proxy**  string | If use_proxy is no, specfies proxy to be used for connection. e.g. ‘<http://proxy.xy.z:8080>’ |
| **state**  string | If `present`, will verify that the Managed Objects are present and will create if needed.  If `absent`, will verify that the Managed Objects are absent and will delete if needed.  Choices:   - `"absent"` - `"present"` ← (default) |
| **use_proxy**  boolean | If `no`, will not use the proxy as defined by system environment variable.  Choices:   - `false` - `true` ← (default) |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  Choices:   - `false` - `true` ← (default) |
| **username**  string | Username for Cisco UCS Manager authentication.  Default: `"admin"` |

## [Examples](ucs_managed_objects_module.md#id4)

```yaml+jinja
- name: Configure Network Control Policy
  cisco.ucs.ucs_managed_objects:
    hostname: 172.16.143.150
    username: admin
    password: password
    objects:
    - module: ucsmsdk.mometa.nwctrl.NwctrlDefinition
      class: NwctrlDefinition
      properties:
        parent_mo_or_dn: org-root
        cdp: enabled
        descr: ''
        lldp_receive: enabled
        lldp_transmit: enabled
        name: Enable-CDP-LLDP

- name: Remove Network Control Policy
  cisco.ucs.ucs_managed_objects:
    hostname: 172.16.143.150
    username: admin
    password: password
    objects:
    - module: ucsmsdk.mometa.nwctrl.NwctrlDefinition
      class: NwctrlDefinition
      properties:
        parent_mo_or_dn: org-root
        name: Enable-CDP-LLDP
    state: absent

- name: Configure Boot Policy Using JSON objects list with children
  cisco.ucs.ucs_managed_objects:
    hostname: 172.16.143.150
    username: admin
    password: password
    objects:
    - {
          "module": "ucsmsdk.mometa.lsboot.LsbootPolicy",
          "class": "LsbootPolicy",
          "properties": {
              "parent_mo_or_dn": "org-root",
              "name": "Python_SDS",
              "enforce_vnic_name": "yes",
              "boot_mode": "legacy",
              "reboot_on_update": "no"
          },
          "children": [
              {
                  "module": "ucsmsdk.mometa.lsboot.LsbootVirtualMedia",
                  "class": "LsbootVirtualMedia",
                  "properties": {
                      "access": "read-only-local",
                      "lun_id": "0",
                      "order": "2"
                  }
              },
              {
                  "module": "ucsmsdk.mometa.lsboot.LsbootStorage",
                  "class": "LsbootStorage",
                  "properties": {
                      "order": "1"
                  },
                  "children": [
                      {
                          "module": "ucsmsdk.mometa.lsboot.LsbootLocalStorage",
                          "class": "LsbootLocalStorage",
                          "properties": {},
                          "children": [
                              {
                                  "module": "ucsmsdk.mometa.lsboot.LsbootDefaultLocalImage",
                                  "class": "LsbootDefaultLocalImage",
                                  "properties": {
                                      "order": "1"
                                  }
                              }
                          ]
                      }
                  ]
              }
          ]
      }

- name: Remove Boot Policy Using JSON objects list
  cisco.ucs.ucs_managed_objects:
    hostname: 172.16.143.150
    username: admin
    password: password
    objects:
    - {
          "module": "ucsmsdk.mometa.lsboot.LsbootPolicy",
          "class": "LsbootPolicy",
          "properties": {
              "parent_mo_or_dn": "org-root",
              "name": "Python_SDS"
          }
      }
    state: absent
```

### Authors

- David Soper (@dsoper2)
- CiscoUcs (@CiscoUcs)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-ucs)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-ucs)
