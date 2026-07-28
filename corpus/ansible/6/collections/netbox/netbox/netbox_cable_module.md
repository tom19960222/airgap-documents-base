---
collection: ansible
version: "6"
title: "netbox.netbox.netbox_cable module – Create, update or delete cables within NetBox"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netbox/netbox/netbox_cable_module.html
fetched_at: 2026-07-28T00:14:32+00:00
---
# netbox.netbox.netbox_cable module – Create, update or delete cables within NetBox

> **Note:**
>
> This module is part of the [netbox.netbox collection](https://galaxy.ansible.com/netbox/netbox) (version 3.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netbox.netbox`.
> You need further requirements to be able to use this module,
> see [Requirements](netbox_cable_module.md#ansible-collections-netbox-netbox-netbox-cable-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_cable`.

New in netbox.netbox 0.3.0

- [Synopsis](netbox_cable_module.md#synopsis)
- [Requirements](netbox_cable_module.md#requirements)
- [Parameters](netbox_cable_module.md#parameters)
- [Notes](netbox_cable_module.md#notes)
- [Examples](netbox_cable_module.md#examples)
- [Return Values](netbox_cable_module.md#return-values)

## [Synopsis](netbox_cable_module.md#id1)

- Creates, updates or removes cables from NetBox

## [Requirements](netbox_cable_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_cable_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the cable configuration |
| **color**  string | The color of the cable |
| **custom_fields**  dictionary  added in netbox.netbox 3.6.0 | Must exist in NetBox |
| **label**  string | The label of the cable |
| **length**  float | The length of the cable |
| **length_unit**  string | The unit in which the length of the cable is measured  Choices:   - `"m"` - `"cm"` - `"ft"` - `"in"` |
| **status**  string | The status of the cable  Choices:   - `"connected"` - `"planned"` - `"decommissioning"` |
| **tags**  list / elements=any | Any tags that the cable may need to be associated with |
| **termination_a**  any / required | The termination a |
| **termination_a_type**  string / required | The type of the termination a  Choices:   - `"circuits.circuittermination"` - `"dcim.consoleport"` - `"dcim.consoleserverport"` - `"dcim.frontport"` - `"dcim.interface"` - `"dcim.powerfeed"` - `"dcim.poweroutlet"` - `"dcim.powerport"` - `"dcim.rearport"` |
| **termination_b**  any / required | The termination b |
| **termination_b_type**  string / required | The type of the termination b  Choices:   - `"circuits.circuittermination"` - `"dcim.consoleport"` - `"dcim.consoleserverport"` - `"dcim.frontport"` - `"dcim.interface"` - `"dcim.powerfeed"` - `"dcim.poweroutlet"` - `"dcim.powerport"` - `"dcim.rearport"` |
| **type**  string | The type of the cable  Choices:   - `"cat3"` - `"cat5"` - `"cat5e"` - `"cat6"` - `"cat6a"` - `"cat7"` - `"dac-active"` - `"dac-passive"` - `"mrj21-trunk"` - `"coaxial"` - `"mmf"` - `"mmf-om1"` - `"mmf-om2"` - `"mmf-om3"` - `"mmf-om4"` - `"smf"` - `"smf-os1"` - `"smf-os2"` - `"aoc"` - `"power"` |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  Default: `true` |

## [Notes](netbox_cable_module.md#id4)

> **Note:**
>
> - Tags should be defined as a YAML list
> - This should be ran with connection `local` and hosts `localhost`

## [Examples](netbox_cable_module.md#id5)

```yaml+jinja
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create cable within NetBox with only required information
      netbox_cable:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          termination_a_type: dcim.interface
          termination_a:
            device: Test Nexus Child One
            name: Ethernet2/2
          termination_b_type: dcim.interface
          termination_b:
            device: Test Nexus Child One
            name: Ethernet2/1
        state: present

    - name: Update cable with other fields
      netbox_cable:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          termination_a_type: dcim.interface
          termination_a:
            device: Test Nexus Child One
            name: Ethernet2/2
          termination_b_type: dcim.interface
          termination_b:
            device: Test Nexus Child One
            name: Ethernet2/1
          type: mmf-om4
          status: planned
          label: label123
          color: abcdef
          length: 30
          length_unit: m
          tags:
            - foo
        state: present

    - name: Delete cable within netbox
      netbox_cable:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          termination_a_type: dcim.interface
          termination_a:
            device: Test Nexus Child One
            name: Ethernet2/2
          termination_b_type: dcim.interface
          termination_b:
            device: Test Nexus Child One
            name: Ethernet2/1
        state: absent
```

## [Return Values](netbox_cable_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cable**  dictionary | Serialized object as created or already existent within NetBox  Returned: success (when *state=present*) |
| **msg**  string | Message indicating failure or info about what has been achieved  Returned: always |

### Authors

- Tobias Groß (@toerb)

### Collection links

[Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
[Repository (Sources)](https://github.com/netbox-community/ansible_modules)
