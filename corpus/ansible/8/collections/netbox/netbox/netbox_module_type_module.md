---
collection: ansible
version: "8"
title: "netbox.netbox.netbox_module_type module – Create, update or delete module types within NetBox"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netbox/netbox/netbox_module_type_module.html
fetched_at: 2026-07-28T02:45:14+00:00
---
# netbox.netbox.netbox_module_type module – Create, update or delete module types within NetBox

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
> see [Requirements](netbox_module_type_module.md#ansible-collections-netbox-netbox-netbox-module-type-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_module_type`.

New in netbox.netbox 3.10.0

- [Synopsis](netbox_module_type_module.md#synopsis)
- [Requirements](netbox_module_type_module.md#requirements)
- [Parameters](netbox_module_type_module.md#parameters)
- [Notes](netbox_module_type_module.md#notes)
- [Examples](netbox_module_type_module.md#examples)
- [Return Values](netbox_module_type_module.md#return-values)

## [Synopsis](netbox_module_type_module.md#id1)

- Creates, updates or removes module types from NetBox

## [Requirements](netbox_module_type_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_module_type_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the device type configuration |
| **comments**  string | Comments that may include additional information in regards to the module type |
| **custom_fields**  dictionary | must exist in NetBox |
| **manufacturer**  any | The manufacturer of the module type |
| **model**  any / required | The model of the module type |
| **part_number**  string | The part number of the module type |
| **tags**  list / elements=any | Any tags that the module type may need to be associated with |
| **weight**  float | The weight of the device type |
| **weight_unit**  string  *added in netbox.netbox 3.10.0* | The weight unit  **Choices:**   - `"kg"` - `"g"` - `"lb"` - `"oz"` |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  **Default:** `true` |

## [Notes](netbox_module_type_module.md#id4)

> **Note:**
>
> - Tags should be defined as a YAML list
> - This should be ran with connection `local` and hosts `localhost`

## [Examples](netbox_module_type_module.md#id5)

```yaml+jinja
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create module type within NetBox with only required information
      netbox.netbox.netbox_module_type:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          model: ws-test-3750
          manufacturer: Test Manufacturer
        state: present

    - name: Create module type within NetBox
      netbox.netbox.netbox_module_type:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          model: ws-test-3750
          manufacturer: Test Manufacturer
          part_number: ws-3750g-v2
        state: present

    - name: Delete module type within netbox
      netbox.netbox.netbox_module_type:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          model: ws-test-3750
        state: absent
```

## [Return Values](netbox_module_type_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **module_type**  dictionary | Serialized object as created or already existent within NetBox  **Returned:** success (when *state=present*) |
| **msg**  string | Message indicating failure or info about what has been achieved  **Returned:** always |

### Authors

- Martin Rødvand (@rodvand)

### Collection links

- [Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
- [Repository (Sources)](https://github.com/netbox-community/ansible_modules)
