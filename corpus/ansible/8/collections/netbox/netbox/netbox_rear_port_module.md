---
collection: ansible
version: "8"
title: "netbox.netbox.netbox_rear_port module – Create, update or delete rear ports within NetBox"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netbox/netbox/netbox_rear_port_module.html
fetched_at: 2026-07-28T02:45:23+00:00
---
# netbox.netbox.netbox_rear_port module – Create, update or delete rear ports within NetBox

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
> see [Requirements](netbox_rear_port_module.md#ansible-collections-netbox-netbox-netbox-rear-port-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_rear_port`.

New in netbox.netbox 0.2.3

- [Synopsis](netbox_rear_port_module.md#synopsis)
- [Requirements](netbox_rear_port_module.md#requirements)
- [Parameters](netbox_rear_port_module.md#parameters)
- [Notes](netbox_rear_port_module.md#notes)
- [Examples](netbox_rear_port_module.md#examples)
- [Return Values](netbox_rear_port_module.md#return-values)

## [Synopsis](netbox_rear_port_module.md#id1)

- Creates, updates or removes rear ports from NetBox

## [Requirements](netbox_rear_port_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_rear_port_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the rear port configuration |
| **description**  string | Description of the rear port |
| **device**  any / required | The device the rear port is attached to |
| **label**  string  *added in netbox.netbox 3.7.0* | Label of the rear port |
| **name**  string / required | The name of the rear port |
| **positions**  integer | The number of front ports which may be mapped to each rear port |
| **tags**  list / elements=any | Any tags that the rear port may need to be associated with |
| **type**  string / required | The type of the rear port  **Choices:**   - `"8p8c"` - `"110-punch"` - `"bnc"` - `"mrj21"` - `"fc"` - `"lc"` - `"lc-apc"` - `"lsh"` - `"lsh-apc"` - `"mpo"` - `"mtrj"` - `"sc"` - `"sc-apc"` - `"st"` |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  **Default:** `true` |

## [Notes](netbox_rear_port_module.md#id4)

> **Note:**
>
> - Tags should be defined as a YAML list
> - This should be ran with connection `local` and hosts `localhost`

## [Examples](netbox_rear_port_module.md#id5)

```yaml+jinja
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create rear port within NetBox with only required information
      netbox.netbox.netbox_rear_port:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Rear Port
          device: Test Device
          type: bnc
        state: present

    - name: Update rear port with other fields
      netbox.netbox.netbox_rear_port:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Rear Port
          device: Test Device
          type: bnc
          positions: 5
          description: rear port description
        state: present

    - name: Delete rear port within netbox
      netbox.netbox.netbox_rear_port:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Rear Port
          device: Test Device
          type: bnc
        state: absent
```

## [Return Values](netbox_rear_port_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Message indicating failure or info about what has been achieved  **Returned:** always |
| **rear_port**  dictionary | Serialized object as created or already existent within NetBox  **Returned:** success (when *state=present*) |

### Authors

- Tobias Groß (@toerb)

### Collection links

- [Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
- [Repository (Sources)](https://github.com/netbox-community/ansible_modules)
