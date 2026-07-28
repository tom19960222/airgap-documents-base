---
collection: ansible
version: "8"
title: "netbox.netbox.netbox_console_port_template module – Create, update or delete console port templates within NetBox"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netbox/netbox/netbox_console_port_template_module.html
fetched_at: 2026-07-28T02:44:53+00:00
---
# netbox.netbox.netbox_console_port_template module – Create, update or delete console port templates within NetBox

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
> see [Requirements](netbox_console_port_template_module.md#ansible-collections-netbox-netbox-netbox-console-port-template-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_console_port_template`.

New in netbox.netbox 0.2.3

- [Synopsis](netbox_console_port_template_module.md#synopsis)
- [Requirements](netbox_console_port_template_module.md#requirements)
- [Parameters](netbox_console_port_template_module.md#parameters)
- [Notes](netbox_console_port_template_module.md#notes)
- [Examples](netbox_console_port_template_module.md#examples)
- [Return Values](netbox_console_port_template_module.md#return-values)

## [Synopsis](netbox_console_port_template_module.md#id1)

- Creates, updates or removes console port templates from NetBox

## [Requirements](netbox_console_port_template_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_console_port_template_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the console port template configuration |
| **device_type**  any / required | The device type the console port template is attached to |
| **name**  string / required | The name of the console port template |
| **type**  string | The type of the console port template  **Choices:**   - `"de-9"` - `"db-25"` - `"rj-11"` - `"rj-12"` - `"rj-45"` - `"usb-a"` - `"usb-b"` - `"usb-c"` - `"usb-mini-a"` - `"usb-mini-b"` - `"usb-micro-a"` - `"usb-micro-b"` - `"other"` |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  **Default:** `true` |

## [Notes](netbox_console_port_template_module.md#id4)

> **Note:**
>
> - Tags should be defined as a YAML list
> - This should be ran with connection `local` and hosts `localhost`

## [Examples](netbox_console_port_template_module.md#id5)

```yaml+jinja
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create console port template within NetBox with only required information
      netbox.netbox.netbox_console_port_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Console Port Template
          device_type: Test Device Type
        state: present

    - name: Update console port template with other fields
      netbox.netbox.netbox_console_port_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Console Port Template
          device_type: Test Device Type
          type: iec-60320-c6
        state: present

    - name: Delete console port template within netbox
      netbox.netbox.netbox_console_port_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Console Port Template
          device_type: Test Device Type
        state: absent
```

## [Return Values](netbox_console_port_template_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **console_port_template**  dictionary | Serialized object as created or already existent within NetBox  **Returned:** success (when *state=present*) |
| **msg**  string | Message indicating failure or info about what has been achieved  **Returned:** always |

### Authors

- Tobias Groß (@toerb)

### Collection links

- [Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
- [Repository (Sources)](https://github.com/netbox-community/ansible_modules)
