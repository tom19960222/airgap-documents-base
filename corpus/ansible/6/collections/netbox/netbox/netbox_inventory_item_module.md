---
collection: ansible
version: "6"
title: "netbox.netbox.netbox_inventory_item module – Creates or removes inventory items from NetBox"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netbox/netbox/netbox_inventory_item_module.html
fetched_at: 2026-07-28T00:14:50+00:00
---
# netbox.netbox.netbox_inventory_item module – Creates or removes inventory items from NetBox

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
> see [Requirements](netbox_inventory_item_module.md#ansible-collections-netbox-netbox-netbox-inventory-item-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_inventory_item`.

New in netbox.netbox 0.1.0

- [Synopsis](netbox_inventory_item_module.md#synopsis)
- [Requirements](netbox_inventory_item_module.md#requirements)
- [Parameters](netbox_inventory_item_module.md#parameters)
- [Notes](netbox_inventory_item_module.md#notes)
- [Examples](netbox_inventory_item_module.md#examples)
- [Return Values](netbox_inventory_item_module.md#return-values)

## [Synopsis](netbox_inventory_item_module.md#id1)

- Creates or removes inventory items from NetBox

## [Requirements](netbox_inventory_item_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_inventory_item_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the inventory item configuration |
| **asset_tag**  string | The asset tag of the inventory item |
| **custom_fields**  dictionary  added in netbox.netbox 3.4.0 | must exist in Netbox |
| **description**  string | The description of the inventory item |
| **device**  any | Name of the device the inventory item belongs to |
| **discovered**  boolean | Set the discovery flag for the inventory item  Choices:   - `false` ← (default) - `true` |
| **label**  string  added in netbox.netbox 3.4.0 | The physical label of the inventory item |
| **manufacturer**  any | The manufacturer of the inventory item |
| **name**  string / required | Name of the inventory item to be created |
| **parent_inventory_item**  any  added in netbox.netbox 3.5.0 | The parent inventory item the inventory item will be associated with |
| **part_id**  string | The part ID of the inventory item |
| **serial**  string | The serial number of the inventory item |
| **tags**  list / elements=any | Any tags that the device may need to be associated with |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  Default: `true` |

## [Notes](netbox_inventory_item_module.md#id4)

> **Note:**
>
> - Tags should be defined as a YAML list
> - This should be ran with connection `local` and hosts `localhost`

## [Examples](netbox_inventory_item_module.md#id5)

```yaml+jinja
- name: "Test NetBox inventory_item module"
  connection: local
  hosts: localhost
  gather_facts: False
  tasks:
    - name: Create inventory item within NetBox with only required information
      netbox_inventory_item:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device: test100
          name: "10G-SFP+"
        state: present

    - name: Update inventory item
      netbox_inventory_item:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device: test100
          name: "10G-SFP+"
          manufacturer: "Cisco"
          part_id: "10G-SFP+"
          serial: "1234"
          asset_tag: "1234"
          description: "New SFP"
        state: present

    - name: Create inventory item with parent
      netbox_inventory_item:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          parent_inventory_item:
            name: "Line Card 1"
            device: test100
          name: "10G-SFP+"
          device: test100
        state: present

    - name: Delete inventory item within netbox
      netbox_inventory_item:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device: test100
          name: "10G-SFP+"
        state: absent
```

## [Return Values](netbox_inventory_item_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **inventory_item**  dictionary | Serialized object as created or already existent within NetBox  Returned: on creation |
| **msg**  string | Message indicating failure or info about what has been achieved  Returned: always |

### Authors

- Mikhail Yohman (@FragmentedPacket)

### Collection links

[Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
[Repository (Sources)](https://github.com/netbox-community/ansible_modules)
