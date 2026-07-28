---
collection: ansible
version: "6"
title: "netbox.netbox.netbox_power_outlet module – Create, update or delete power outlets within NetBox"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netbox/netbox/netbox_power_outlet_module.html
fetched_at: 2026-07-28T00:14:56+00:00
---
# netbox.netbox.netbox_power_outlet module – Create, update or delete power outlets within NetBox

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
> see [Requirements](netbox_power_outlet_module.md#ansible-collections-netbox-netbox-netbox-power-outlet-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_power_outlet`.

New in netbox.netbox 0.2.3

- [Synopsis](netbox_power_outlet_module.md#synopsis)
- [Requirements](netbox_power_outlet_module.md#requirements)
- [Parameters](netbox_power_outlet_module.md#parameters)
- [Notes](netbox_power_outlet_module.md#notes)
- [Examples](netbox_power_outlet_module.md#examples)
- [Return Values](netbox_power_outlet_module.md#return-values)

## [Synopsis](netbox_power_outlet_module.md#id1)

- Creates, updates or removes power outlets from NetBox

## [Requirements](netbox_power_outlet_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_power_outlet_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the power outlet configuration |
| **description**  string | Description of the power outlet |
| **device**  any / required | The device the power outlet is attached to |
| **feed_leg**  string | The phase, in case of three-phase feed  Choices:   - `"A"` - `"B"` - `"C"` |
| **name**  string / required | The name of the power outlet |
| **power_port**  any | The attached power port |
| **tags**  list / elements=any | Any tags that the power outlet may need to be associated with |
| **type**  string | The type of the power outlet  Choices:   - `"iec-60320-c5"` - `"iec-60320-c7"` - `"iec-60320-c13"` - `"iec-60320-c15"` - `"iec-60320-c19"` - `"iec-60309-p-n-e-4h"` - `"iec-60309-p-n-e-6h"` - `"iec-60309-p-n-e-9h"` - `"iec-60309-2p-e-4h"` - `"iec-60309-2p-e-6h"` - `"iec-60309-2p-e-9h"` - `"iec-60309-3p-e-4h"` - `"iec-60309-3p-e-6h"` - `"iec-60309-3p-e-9h"` - `"iec-60309-3p-n-e-4h"` - `"iec-60309-3p-n-e-6h"` - `"iec-60309-3p-n-e-9h"` - `"nema-5-15r"` - `"nema-5-20r"` - `"nema-5-30r"` - `"nema-5-50r"` - `"nema-6-15r"` - `"nema-6-20r"` - `"nema-6-30r"` - `"nema-6-50r"` - `"nema-l5-15r"` - `"nema-l5-20r"` - `"nema-l5-30r"` - `"nema-l5-50r"` - `"nema-l6-20r"` - `"nema-l6-30r"` - `"nema-l6-50r"` - `"nema-l14-20r"` - `"nema-l14-30r"` - `"nema-l21-20r"` - `"nema-l21-30r"` - `"CS6360C"` - `"CS6364C"` - `"CS8164C"` - `"CS8264C"` - `"CS8364C"` - `"CS8464C"` - `"ita-e"` - `"ita-f"` - `"ita-g"` - `"ita-h"` - `"ita-i"` - `"ita-j"` - `"ita-k"` - `"ita-l"` - `"ita-m"` - `"ita-n"` - `"ita-o"` - `"hdot-cx"` |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  Default: `true` |

## [Notes](netbox_power_outlet_module.md#id4)

> **Note:**
>
> - Tags should be defined as a YAML list
> - This should be ran with connection `local` and hosts `localhost`

## [Examples](netbox_power_outlet_module.md#id5)

```yaml+jinja
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create power port within NetBox with only required information
      netbox_power_outlet:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Power Outlet
          device: Test Device
        state: present

    - name: Update power port with other fields
      netbox_power_outlet:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Power Outlet
          device: Test Device
          type: iec-60320-c6
          power_port: Test Power Port
          feed_leg: A
          description: power port description
        state: present

    - name: Delete power port within netbox
      netbox_power_outlet:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Power Outlet
          device: Test Device
        state: absent
```

## [Return Values](netbox_power_outlet_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Message indicating failure or info about what has been achieved  Returned: always |
| **power_outlet**  dictionary | Serialized object as created or already existent within NetBox  Returned: success (when *state=present*) |

### Authors

- Tobias Groß (@toerb)

### Collection links

[Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
[Repository (Sources)](https://github.com/netbox-community/ansible_modules)
