---
collection: ansible
version: "8"
title: "netbox.netbox.netbox_platform module – Create or delete platforms within NetBox"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netbox/netbox/netbox_platform_module.html
fetched_at: 2026-07-28T02:45:14+00:00
---
# netbox.netbox.netbox_platform module – Create or delete platforms within NetBox

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
> see [Requirements](netbox_platform_module.md#ansible-collections-netbox-netbox-netbox-platform-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_platform`.

New in netbox.netbox 0.1.0

- [Synopsis](netbox_platform_module.md#synopsis)
- [Requirements](netbox_platform_module.md#requirements)
- [Parameters](netbox_platform_module.md#parameters)
- [Notes](netbox_platform_module.md#notes)
- [Examples](netbox_platform_module.md#examples)
- [Return Values](netbox_platform_module.md#return-values)

## [Synopsis](netbox_platform_module.md#id1)

- Creates or removes platforms from NetBox

## [Requirements](netbox_platform_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_platform_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the platform configuration |
| **custom_fields**  dictionary  *added in netbox.netbox 3.6.0* | Must exist in NetBox |
| **description**  string | The description of the platform |
| **manufacturer**  any | The manufacturer the platform will be tied to |
| **name**  string / required | The name of the platform |
| **napalm_args**  dictionary | The optional arguments used for NAPALM connections |
| **napalm_driver**  string | The name of the NAPALM driver to be used when using the NAPALM plugin |
| **slug**  string | The slugified version of the name or custom slug.  This is auto-generated following NetBox rules if not provided |
| **tags**  list / elements=any  *added in netbox.netbox 3.6.0* | The tags to add/update |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  **Default:** `true` |

## [Notes](netbox_platform_module.md#id4)

> **Note:**
>
> - Tags should be defined as a YAML list
> - This should be ran with connection `local` and hosts `localhost`

## [Examples](netbox_platform_module.md#id5)

```yaml+jinja
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create platform within NetBox with only required information
      netbox.netbox.netbox_platform:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Platform
        state: present

    - name: Create platform within NetBox with only required information
      netbox.netbox.netbox_platform:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Platform All
          manufacturer: Test Manufacturer
          napalm_driver: ios
          napalm_args:
            global_delay_factor: 2
        state: present

    - name: Delete platform within netbox
      netbox.netbox.netbox_platform:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Platform
        state: absent
```

## [Return Values](netbox_platform_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Message indicating failure or info about what has been achieved  **Returned:** always |
| **platform**  dictionary | Serialized object as created or already existent within NetBox  **Returned:** success (when *state=present*) |

### Authors

- Mikhail Yohman (@FragmentedPacket)

### Collection links

- [Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
- [Repository (Sources)](https://github.com/netbox-community/ansible_modules)
