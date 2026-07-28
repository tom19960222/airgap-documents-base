---
collection: ansible
version: "8"
title: "netbox.netbox.netbox_inventory_item_role module – Create, update or delete devices roles within NetBox"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netbox/netbox/netbox_inventory_item_role_module.html
fetched_at: 2026-07-28T02:45:08+00:00
---
# netbox.netbox.netbox_inventory_item_role module – Create, update or delete devices roles within NetBox

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
> see [Requirements](netbox_inventory_item_role_module.md#ansible-collections-netbox-netbox-netbox-inventory-item-role-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_inventory_item_role`.

New in netbox.netbox 3.10.0

- [Synopsis](netbox_inventory_item_role_module.md#synopsis)
- [Requirements](netbox_inventory_item_role_module.md#requirements)
- [Parameters](netbox_inventory_item_role_module.md#parameters)
- [Notes](netbox_inventory_item_role_module.md#notes)
- [Examples](netbox_inventory_item_role_module.md#examples)
- [Return Values](netbox_inventory_item_role_module.md#return-values)

## [Synopsis](netbox_inventory_item_role_module.md#id1)

- Creates, updates or removes devices roles from NetBox

## [Requirements](netbox_inventory_item_role_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_inventory_item_role_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the inventory item role configuration |
| **color**  string | Hexidecimal code for a color, ex. FFFFFF |
| **custom_fields**  dictionary | Must exist in NetBox |
| **description**  string | The description of the inventory item role |
| **name**  string / required | The name of the inventory item role |
| **slug**  string | The slugified version of the name or custom slug.  This is auto-generated following NetBox rules if not provided |
| **tags**  list / elements=any | The tags to add/update |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  **Default:** `true` |

## [Notes](netbox_inventory_item_role_module.md#id4)

> **Note:**
>
> - Tags should be defined as a YAML list
> - This should be ran with connection `local` and hosts `localhost`

## [Examples](netbox_inventory_item_role_module.md#id5)

```yaml+jinja
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create inventory item role within NetBox with only required information
      netbox.netbox.netbox_inventory_item_role:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Inventory Item role
          color: FFFFFF
        state: present

    - name: Delete inventory item role within netbox
      netbox.netbox.netbox_inventory_item_role:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Inventory Item role
        state: absent
```

## [Return Values](netbox_inventory_item_role_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **inventory_item_role**  dictionary | Serialized object as created or already existent within NetBox  **Returned:** success (when *state=present*) |
| **msg**  string | Message indicating failure or info about what has been achieved  **Returned:** always |

### Authors

- Martin Rødvand (@rodvand)

### Collection links

- [Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
- [Repository (Sources)](https://github.com/netbox-community/ansible_modules)
