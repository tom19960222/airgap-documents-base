---
collection: ansible
version: "8"
title: "netbox.netbox.netbox_device_interface module – Creates or removes interfaces on devices from NetBox"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netbox/netbox/netbox_device_interface_module.html
fetched_at: 2026-07-28T02:45:01+00:00
---
# netbox.netbox.netbox_device_interface module – Creates or removes interfaces on devices from NetBox

> **Note:**
>
> This module is part of the [netbox.netbox collection](https://galaxy.ansible.com/ui/repo/published/netbox/netbox/) (version 3.15.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netbox.netbox`.
> You need further requirements to be able to use this module,
> see [Requirements](netbox_device_interface_module.md#ansible-collections-netbox-netbox-netbox-device-interface-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_device_interface`.

New in netbox.netbox 0.1.0

- [Synopsis](netbox_device_interface_module.md#synopsis)
- [Requirements](netbox_device_interface_module.md#requirements)
- [Parameters](netbox_device_interface_module.md#parameters)
- [Notes](netbox_device_interface_module.md#notes)
- [Examples](netbox_device_interface_module.md#examples)
- [Return Values](netbox_device_interface_module.md#return-values)

## [Synopsis](netbox_device_interface_module.md#id1)

- Creates or removes interfaces from NetBox

## [Requirements](netbox_device_interface_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_device_interface_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the interface configuration |
| **bridge**  any  *added in netbox.netbox 3.6.0* | Bridge the interface will connected to |
| **custom_fields**  dictionary | must exist in NetBox |
| **description**  string | The description of the interface |
| **device**  any | Name of the device the interface will be associated with (case-sensitive) |
| **duplex**  string  *added in netbox.netbox 3.7.0* | The duplex of the interface  **Choices:**   - `"half"` - `"full"` - `"auto"` |
| **enabled**  boolean | Sets whether interface shows enabled or disabled  **Choices:**   - `false` - `true` |
| **form_factor**  any | Form factor of the interface:  ex. 1000Base-T (1GE), Virtual, 10GBASE-T (10GE) This has to be specified exactly as what is found within UI |
| **label**  string | Physical label of the interface |
| **lag**  any | Parent LAG interface will be a member of |
| **mac_address**  string | The MAC address of the interface |
| **mark_connected**  boolean | Mark an interface as connected without a cable attached (netbox >= 2.11 required)  **Choices:**   - `false` - `true` |
| **mgmt_only**  boolean | This interface is used only for out-of-band management  **Choices:**   - `false` - `true` |
| **mode**  any | The mode of the interface |
| **mtu**  integer | The MTU of the interface |
| **name**  string / required | Name of the interface to be created |
| **parent_interface**  any  *added in netbox.netbox 3.2.0* | The device’s parent interface |
| **poe_mode**  any  *added in netbox.netbox 3.8.0* | This interface has PoE ability (NetBox release 3.3 and later) |
| **poe_type**  any  *added in netbox.netbox 3.8.0* | This interface’s power type (NetBox release 3.3 and later) |
| **speed**  integer  *added in netbox.netbox 3.7.0* | The speed of the interface |
| **tagged_vlans**  any | A list of tagged VLANS to be assigned to interface. Mode must be set to either `Tagged` or `Tagged All` |
| **tags**  list / elements=any | Any tags that the interface may need to be associated with |
| **tx_power**  integer  *added in netbox.netbox 3.14.0* | The interface’s configured output power, in dBm |
| **type**  string | Form factor of the interface:  ex. 1000Base-T (1GE), Virtual, 10GBASE-T (10GE) This has to be specified exactly as what is found within UI |
| **untagged_vlan**  any | The untagged VLAN to be assigned to interface |
| **vrf**  any  *added in netbox.netbox 3.7.0* | The VRF of the interface |
| **wwn**  string  *added in netbox.netbox 3.14.0* | The WWN of the interface |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **update_vc_child**  boolean | Use when master device is specified for `device` and the specified interface exists on a child device  and needs updated  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  **Default:** `true` |

## [Notes](netbox_device_interface_module.md#id4)

> **Note:**
>
> - Tags should be defined as a YAML list
> - This should be ran with connection `local` and hosts `localhost`

## [Examples](netbox_device_interface_module.md#id5)

```yaml+jinja
- name: "Test NetBox interface module"
  connection: local
  hosts: localhost
  gather_facts: False
  tasks:
    - name: Create interface within NetBox with only required information
      netbox.netbox.netbox_device_interface:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device: test100
          name: GigabitEthernet1
        state: present

    - name: Delete interface within netbox
      netbox.netbox.netbox_device_interface:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device: test100
          name: GigabitEthernet1
        state: absent

    - name: Create LAG with several specified options
      netbox.netbox.netbox_device_interface:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device: test100
          name: port-channel1
          type: Link Aggregation Group (LAG)
          mtu: 1600
          mgmt_only: false
          mode: Access
        state: present

    - name: Create interface and assign it to parent LAG
      netbox.netbox.netbox_device_interface:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device: test100
          name: GigabitEthernet1
          enabled: false
          type: 1000Base-t (1GE)
          lag:
            name: port-channel1
          mtu: 1600
          mgmt_only: false
          mode: Access
        state: present

    - name: Create interface as a trunk port
      netbox.netbox.netbox_device_interface:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device: test100
          name: GigabitEthernet25
          enabled: false
          type: 1000Base-t (1GE)
          untagged_vlan:
            name: Wireless
            site: Test Site
          tagged_vlans:
            - name: Data
              site: Test Site
            - name: VoIP
              site: Test Site
          mtu: 1600
          mgmt_only: true
          mode: Tagged
        state: present

    - name: Update interface on child device on virtual chassis
      netbox.netbox.netbox_device_interface:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device: test100
          name: GigabitEthernet2/0/1
          enabled: false
        update_vc_child: True

    - name: Mark interface as connected without a cable (netbox >= 2.11 required)
      netbox.netbox.netbox_device_interface:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device: test100
          name: GigabitEthernet1
          mark_connected: true
        state: present
```

## [Return Values](netbox_device_interface_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **interface**  dictionary | Serialized object as created or already existent within NetBox  **Returned:** on creation |
| **msg**  string | Message indicating failure or info about what has been achieved  **Returned:** always |

### Authors

- Mikhail Yohman (@FragmentedPacket)

### Collection links

- [Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
- [Repository (Sources)](https://github.com/netbox-community/ansible_modules)
