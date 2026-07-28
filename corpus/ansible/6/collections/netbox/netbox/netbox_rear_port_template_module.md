---
collection: ansible
version: "6"
title: "netbox.netbox.netbox_rear_port_template module – Create, update or delete rear port templates within NetBox"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netbox/netbox/netbox_rear_port_template_module.html
fetched_at: 2026-07-28T00:15:04+00:00
---
# netbox.netbox.netbox_rear_port_template module – Create, update or delete rear port templates within NetBox

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
> see [Requirements](netbox_rear_port_template_module.md#ansible-collections-netbox-netbox-netbox-rear-port-template-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_rear_port_template`.

New in netbox.netbox 0.2.3

- [Synopsis](netbox_rear_port_template_module.md#synopsis)
- [Requirements](netbox_rear_port_template_module.md#requirements)
- [Parameters](netbox_rear_port_template_module.md#parameters)
- [Notes](netbox_rear_port_template_module.md#notes)
- [Examples](netbox_rear_port_template_module.md#examples)
- [Return Values](netbox_rear_port_template_module.md#return-values)

## [Synopsis](netbox_rear_port_template_module.md#id1)

- Creates, updates or removes rear port templates from NetBox

## [Requirements](netbox_rear_port_template_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_rear_port_template_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the rear port template configuration |
| **description**  string  added in netbox.netbox 3.7.0 | Description of the rear port |
| **device_type**  any / required | The device type the rear port template is attached to |
| **label**  string  added in netbox.netbox 3.7.0 | Label of the rear port |
| **name**  string / required | The name of the rear port template |
| **positions**  integer | The number of front ports which may be mapped to each rear port |
| **type**  string | The type of the rear port  Choices:   - `"8p8c"` - `"110-punch"` - `"bnc"` - `"mrj21"` - `"fc"` - `"lc"` - `"lc-apc"` - `"lsh"` - `"lsh-apc"` - `"mpo"` - `"mtrj"` - `"sc"` - `"sc-apc"` - `"st"` |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  Default: `true` |

## [Notes](netbox_rear_port_template_module.md#id4)

> **Note:**
>
> - Tags should be defined as a YAML list
> - This should be ran with connection `local` and hosts `localhost`

## [Examples](netbox_rear_port_template_module.md#id5)

```yaml+jinja
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create rear port template within NetBox with only required information
      netbox_rear_port_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Rear Port Template
          device_type: Test Device Type
          type: bnc
        state: present

    - name: Update rear port template with other fields
      netbox_rear_port_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Rear Port Template
          device_type: Test Device Type
          type: bnc
          positions: 5
        state: present

    - name: Delete rear port template within netbox
      netbox_rear_port_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Rear Port Template
          device_type: Test Device Type
          type: bnc
        state: absent
```

## [Return Values](netbox_rear_port_template_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Message indicating failure or info about what has been achieved  Returned: always |
| **rear_port_template**  dictionary | Serialized object as created or already existent within NetBox  Returned: success (when *state=present*) |

### Authors

- Tobias Groß (@toerb)

### Collection links

[Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
[Repository (Sources)](https://github.com/netbox-community/ansible_modules)
