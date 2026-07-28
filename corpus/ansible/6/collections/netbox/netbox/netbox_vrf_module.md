---
collection: ansible
version: "6"
title: "netbox.netbox.netbox_vrf module – Create, update or delete vrfs within NetBox"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netbox/netbox/netbox_vrf_module.html
fetched_at: 2026-07-28T00:15:14+00:00
---
# netbox.netbox.netbox_vrf module – Create, update or delete vrfs within NetBox

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
> see [Requirements](netbox_vrf_module.md#ansible-collections-netbox-netbox-netbox-vrf-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_vrf`.

New in netbox.netbox 0.1.0

- [Synopsis](netbox_vrf_module.md#synopsis)
- [Requirements](netbox_vrf_module.md#requirements)
- [Parameters](netbox_vrf_module.md#parameters)
- [Notes](netbox_vrf_module.md#notes)
- [Examples](netbox_vrf_module.md#examples)
- [Return Values](netbox_vrf_module.md#return-values)

## [Synopsis](netbox_vrf_module.md#id1)

- Creates, updates or removes vrfs from NetBox

## [Requirements](netbox_vrf_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_vrf_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the vrf configuration |
| **custom_fields**  dictionary | must exist in NetBox |
| **description**  string | The description of the vrf |
| **enforce_unique**  boolean | Prevent duplicate prefixes/IP addresses within this VRF  Choices:   - `false` - `true` |
| **export_targets**  list / elements=string  added in netbox.netbox 2.0.0 | Export targets tied to VRF |
| **import_targets**  list / elements=string  added in netbox.netbox 2.0.0 | Import targets tied to VRF |
| **name**  string / required | The name of the vrf |
| **rd**  string | The RD of the VRF. Must be quoted to pass as a string. |
| **tags**  list / elements=any | Any tags that the vrf may need to be associated with |
| **tenant**  any | The tenant that the vrf will be assigned to |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  Default: `true` |

## [Notes](netbox_vrf_module.md#id4)

> **Note:**
>
> - Tags should be defined as a YAML list
> - This should be ran with connection `local` and hosts `localhost`

## [Examples](netbox_vrf_module.md#id5)

```yaml+jinja
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create vrf within NetBox with only required information
      netbox_vrf:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test VRF
        state: present

    - name: Delete vrf within netbox
      netbox_vrf:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test VRF
        state: absent

    - name: Create vrf with all information
      netbox_vrf:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test VRF
          rd: "65000:1"
          tenant: Test Tenant
          enforce_unique: true
          import_targets:
            - "65000:65001"
          export_targets:
            - "65000:65001"
          description: VRF description
          tags:
            - Schnozzberry
        state: present
```

## [Return Values](netbox_vrf_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Message indicating failure or info about what has been achieved  Returned: always |
| **vrf**  dictionary | Serialized object as created or already existent within NetBox  Returned: success (when *state=present*) |

### Authors

- Mikhail Yohman (@FragmentedPacket)

### Collection links

[Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
[Repository (Sources)](https://github.com/netbox-community/ansible_modules)
