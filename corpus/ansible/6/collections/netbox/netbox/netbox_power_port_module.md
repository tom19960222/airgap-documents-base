---
collection: ansible
version: "6"
title: "netbox.netbox.netbox_power_port module – Create, update or delete power ports within NetBox"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netbox/netbox/netbox_power_port_module.html
fetched_at: 2026-07-28T00:14:58+00:00
---
# netbox.netbox.netbox_power_port module – Create, update or delete power ports within NetBox

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
> see [Requirements](netbox_power_port_module.md#ansible-collections-netbox-netbox-netbox-power-port-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_power_port`.

New in netbox.netbox 0.2.3

- [Synopsis](netbox_power_port_module.md#synopsis)
- [Requirements](netbox_power_port_module.md#requirements)
- [Parameters](netbox_power_port_module.md#parameters)
- [Notes](netbox_power_port_module.md#notes)
- [Examples](netbox_power_port_module.md#examples)
- [Return Values](netbox_power_port_module.md#return-values)

## [Synopsis](netbox_power_port_module.md#id1)

- Creates, updates or removes power ports from NetBox

## [Requirements](netbox_power_port_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_power_port_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the power port configuration |
| **allocated_draw**  integer | The allocated draw of the power port in watt |
| **description**  string | Description of the power port |
| **device**  any / required | The device the power port is attached to |
| **maximum_draw**  integer | The maximum permissible draw of the power port in watt |
| **name**  string / required | The name of the power port |
| **tags**  list / elements=any | Any tags that the power port may need to be associated with |
| **type**  string | The type of the power port  Choices:   - `"iec-60320-c6"` - `"iec-60320-c8"` - `"iec-60320-c14"` - `"iec-60320-c16"` - `"iec-60320-c20"` - `"iec-60309-p-n-e-4h"` - `"iec-60309-p-n-e-6h"` - `"iec-60309-p-n-e-9h"` - `"iec-60309-2p-e-4h"` - `"iec-60309-2p-e-6h"` - `"iec-60309-2p-e-9h"` - `"iec-60309-3p-e-4h"` - `"iec-60309-3p-e-6h"` - `"iec-60309-3p-e-9h"` - `"iec-60309-3p-n-e-4h"` - `"iec-60309-3p-n-e-6h"` - `"iec-60309-3p-n-e-9h"` - `"nema-5-15p"` - `"nema-5-20p"` - `"nema-5-30p"` - `"nema-5-50p"` - `"nema-6-15p"` - `"nema-6-20p"` - `"nema-6-30p"` - `"nema-6-50p"` - `"nema-l5-15p"` - `"nema-l5-20p"` - `"nema-l5-30p"` - `"nema-l5-50p"` - `"nema-l6-20p"` - `"nema-l6-30p"` - `"nema-l6-50p"` - `"nema-l14-20p"` - `"nema-l14-30p"` - `"nema-l21-20p"` - `"nema-l21-30p"` - `"cs6361c"` - `"cs6365c"` - `"cs8165c"` - `"cs8265c"` - `"cs8365c"` - `"cs8465c"` - `"ita-e"` - `"ita-f"` - `"ita-ef"` - `"ita-g"` - `"ita-h"` - `"ita-i"` - `"ita-j"` - `"ita-k"` - `"ita-l"` - `"ita-m"` - `"ita-n"` - `"ita-o"` |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  Default: `true` |

## [Notes](netbox_power_port_module.md#id4)

> **Note:**
>
> - Tags should be defined as a YAML list
> - This should be ran with connection `local` and hosts `localhost`

## [Examples](netbox_power_port_module.md#id5)

```yaml+jinja
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create power port within NetBox with only required information
      netbox_power_port:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Power Port
          device: Test Device
        state: present

    - name: Update power port with other fields
      netbox_power_port:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Power Port
          device: Test Device
          type: iec-60320-c6
          allocated_draw: 16
          maximum_draw: 80
          description: power port description
        state: present

    - name: Delete power port within netbox
      netbox_power_port:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Power Port
          device: Test Device
        state: absent
```

## [Return Values](netbox_power_port_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Message indicating failure or info about what has been achieved  Returned: always |
| **power_port**  dictionary | Serialized object as created or already existent within NetBox  Returned: success (when *state=present*) |

### Authors

- Tobias Groß (@toerb)

### Collection links

[Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
[Repository (Sources)](https://github.com/netbox-community/ansible_modules)
