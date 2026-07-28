---
collection: ansible
version: "8"
title: "netbox.netbox.netbox_rack module – Create, update or delete racks within NetBox"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netbox/netbox/netbox_rack_module.html
fetched_at: 2026-07-28T02:45:21+00:00
---
# netbox.netbox.netbox_rack module – Create, update or delete racks within NetBox

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
> see [Requirements](netbox_rack_module.md#ansible-collections-netbox-netbox-netbox-rack-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_rack`.

New in netbox.netbox 0.1.0

- [Synopsis](netbox_rack_module.md#synopsis)
- [Requirements](netbox_rack_module.md#requirements)
- [Parameters](netbox_rack_module.md#parameters)
- [Notes](netbox_rack_module.md#notes)
- [Examples](netbox_rack_module.md#examples)
- [Return Values](netbox_rack_module.md#return-values)

## [Synopsis](netbox_rack_module.md#id1)

- Creates, updates or removes racks from NetBox

## [Requirements](netbox_rack_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_rack_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the rack configuration |
| **asset_tag**  string | Asset tag that is associated to the rack |
| **comments**  string | Comments that may include additional information in regards to the rack |
| **custom_fields**  dictionary | must exist in NetBox |
| **desc_units**  boolean | Rack units will be numbered top-to-bottom  **Choices:**   - `false` - `true` |
| **description**  string  *added in netbox.netbox 3.10.0* | Description of the rack |
| **facility_id**  string | The unique rack ID assigned by the facility |
| **location**  any  *added in netbox.netbox 3.1.0* | The location the rack will be associated to (NetBox 2.11+) |
| **max_weight**  integer  *added in netbox.netbox 3.10.0* | Maximum load capacity of the rack |
| **mounting_depth**  integer  *added in netbox.netbox 3.10.0* | The mounting depth of the rack |
| **name**  string / required | The name of the rack |
| **outer_depth**  integer | The outer depth of the rack |
| **outer_unit**  string | Whether the rack unit is in Millimeters or Inches and is *required* if outer_width/outer_depth is specified  **Choices:**   - `"Millimeters"` - `"Inches"` |
| **outer_width**  integer | The outer width of the rack |
| **rack_group**  any | The rack group the rack will be associated to (NetBox < 2.11)  Will be removed in version 5.0.0 |
| **rack_role**  any | The rack role the rack will be associated to |
| **serial**  string | Serial number of the rack |
| **site**  any | Required if *state=present* and the rack does not exist yet |
| **status**  any | The status of the rack |
| **tags**  list / elements=any | Any tags that the rack may need to be associated with |
| **tenant**  any | The tenant that the device will be assigned to |
| **type**  string | The type of rack  **Choices:**   - `"2-post frame"` - `"4-post frame"` - `"4-post cabinet"` - `"Wall-mounted frame"` - `"Wall-mounted cabinet"` |
| **u_height**  integer | The height of the rack in rack units |
| **weight**  float  *added in netbox.netbox 3.10.0* | The weight of the rack |
| **weight_unit**  string  *added in netbox.netbox 3.10.0* | The weight unit  **Choices:**   - `"kg"` - `"g"` - `"lb"` - `"oz"` |
| **width**  integer | The rail-to-rail width  **Choices:**   - `10` - `19` - `21` - `23` |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  **Default:** `true` |

## [Notes](netbox_rack_module.md#id4)

> **Note:**
>
> - Tags should be defined as a YAML list
> - This should be ran with connection `local` and hosts `localhost`

## [Examples](netbox_rack_module.md#id5)

```yaml+jinja
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create rack within NetBox with only required information
      netbox.netbox.netbox_rack:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test rack
          site: Test Site
        state: present

    - name: Create rack within NetBox with only required information - Pre 2.11
      netbox.netbox.netbox_rack:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test rack
          site: Test Site
          rack_group: Test Rack Group
        state: present

    - name: Create rack within NetBox with only required information - Post 2.11
      netbox.netbox.netbox_rack:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test rack
          site: Test Site
          location: Test Location
        state: present

    - name: Delete rack within netbox
      netbox.netbox.netbox_rack:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Rack
        state: absent
```

## [Return Values](netbox_rack_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Message indicating failure or info about what has been achieved  **Returned:** always |
| **rack**  dictionary | Serialized object as created or already existent within NetBox  **Returned:** success (when *state=present*) |

### Authors

- Mikhail Yohman (@FragmentedPacket)

### Collection links

- [Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
- [Repository (Sources)](https://github.com/netbox-community/ansible_modules)
